"""
Coarena Site Adapter.
Automated protocol registration and API Key minting adapter for Coarena (https://coarena.ai).

Workflow Architecture:
1. Stage 1 (OAuth Session Catch): Connects or prompts Google OAuth sign-in, capturing NextAuth session tokens.
2. Stage 2 (Post-OAuth Protocol Minting): 100% pure REST protocol takes over:
   - POST /api/me/consent (Accepts platform terms)
   - POST /api/me/keys (Mints permanent API Key)
   - GET /api/v1/limits (Validates key and daily allowance)
"""
import time
import requests
from typing import Dict, Any, Optional
from urllib.parse import urlsplit

from core.adapter import BaseSiteAdapter
from core.pilot import smart_click


class CoarenaAdapter(BaseSiteAdapter):
    """
    Registration adapter for Coarena.
    Target URL: https://coarena.ai/account/api
    Note: Executes pure REST protocol after Google OAuth session authorization.
    """

    def __init__(self, page, context, config=None):
        super().__init__(page, context, config)
        self.api_key: Optional[str] = None
        self.daily_quota: Optional[float] = None

    def target_url(self) -> str:
        return "https://coarena.ai/account/api"

    def fill_form(self, identity: Dict[str, Any]) -> bool:
        """
        Check for Google OAuth session or trigger Google Sign-In flow.
        """
        print("[*] [Coarena] Navigating to Coarena account dashboard...")
        self.page.goto(self.target_url(), wait_until="domcontentloaded", timeout=30000)
        time.sleep(2)

        # Check if already authenticated
        cookies = self.context.cookies()
        has_session = any("next-auth" in c["name"].lower() or "session" in c["name"].lower() for c in cookies)

        if not has_session:
            print("[*] [Coarena] Triggering Google OAuth sign-in flow...")
            g_btn = self.page.locator('button:has-text("Continue with Google"), button:has-text("Sign in")').first
            if g_btn.count() > 0 and g_btn.is_visible():
                smart_click(self.page, g_btn)
                print("[*] [Coarena] Please complete Google OAuth in the window if prompted...")

            # Wait for redirection back to coarena.ai with session
            start_wait = time.time()
            while time.time() - start_wait < 60:
                cur_url = self.page.url
                if "coarena.ai" in urlsplit(cur_url).netloc and "auth" not in cur_url:
                    break
                time.sleep(1.0)

        return True

    def submit_and_confirm(self) -> bool:
        """
        Execute post-OAuth pure REST protocol: accept terms, mint API Key, and verify limits.
        """
        print("[*] [Coarena] OAuth authenticated. Extracting session cookies for pure protocol execution...")
        cookies = self.context.cookies()
        session = requests.Session()
        ua = self.page.evaluate("() => navigator.userAgent") if self.page else "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
        session.headers.update({
            "User-Agent": ua,
            "Accept": "application/json",
            "Referer": "https://coarena.ai/account/api",
            "Origin": "https://coarena.ai",
        })

        for c in cookies:
            session.cookies.set(c["name"], c["value"], domain=c.get("domain", "coarena.ai"))

        # Copy proxy configuration if set
        proxy_url = self.config.get("browser", {}).get("proxy")
        if proxy_url:
            session.proxies = {"http": proxy_url, "https": proxy_url}

        # Protocol Step 1: Verify /api/me identity
        print("[*] [Coarena] [Protocol] Checking session identity via /api/me...")
        me_resp = session.get("https://coarena.ai/api/me", timeout=15)
        if me_resp.status_code != 200:
            print(f"[-] [Coarena] Failed to access /api/me (HTTP {me_resp.status_code})")
            return False

        me = me_resp.json()
        if not me.get("user"):
            print("[-] [Coarena] Active user not found in session response.")
            return False

        # Protocol Step 2: Accept Terms of Service if not current
        if not me.get("consentCurrent"):
            print("[*] [Coarena] [Protocol] Submitting terms consent via /api/me/consent...")
            c_resp = session.post("https://coarena.ai/api/me/consent", timeout=15)
            if c_resp.status_code not in (200, 201, 204):
                print(f"[-] [Coarena] Failed to accept terms: HTTP {c_resp.status_code}")
                return False

        # Protocol Step 3: Mint new API Key
        print("[*] [Coarena] [Protocol] Minting new API Key via /api/me/keys...")
        mint_resp = session.post(
            "https://coarena.ai/api/me/keys",
            json={"name": "RegisterHub-Key"},
            headers={"Content-Type": "application/json"},
            timeout=15
        )
        if mint_resp.status_code not in (200, 201):
            print(f"[-] [Coarena] Mint key failed: HTTP {mint_resp.status_code} {mint_resp.text[:120]}")
            return False

        kdata = mint_resp.json()
        self.api_key = kdata.get("apiKey") or (kdata.get("data", {}).get("apiKey") if isinstance(kdata.get("data"), dict) else None)
        if not self.api_key:
            # Fallback to key listing
            keys_list_resp = session.get("https://coarena.ai/api/me/keys", timeout=15)
            if keys_list_resp.status_code == 200:
                active_keys = keys_list_resp.json().get("keys", [])
                if active_keys:
                    self.api_key = active_keys[-1].get("apiKey") or active_keys[-1].get("id")

        if not self.api_key:
            print("[-] [Coarena] Could not parse API Key from mint response.")
            return False

        # Protocol Step 4: Verify key limits
        print(f"[+] [Coarena] Key minted: {self.api_key[:12]}***")
        try:
            lim_resp = session.get("https://coarena.ai/api/v1/limits", headers={"Authorization": f"Bearer {self.api_key}"}, timeout=15)
            if lim_resp.status_code == 200:
                lim_data = lim_resp.json().get("data", {})
                self.daily_quota = lim_data.get("usd_per_day", 0)
                print(f"[+] [Coarena] Verified API Key! Daily quota: ${self.daily_quota}/day")
        except Exception as e:
            print(f"[*] [Coarena] Quota verify notice: {e}")

        self.account_data["api_key"] = self.api_key
        return True
