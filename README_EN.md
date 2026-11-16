<h1 align="center">Coarena Register</h1>

<p align="center">
  <b>Post-Google OAuth Pure Protocol Registration & Key Minting Tool for Coarena AI</b><br>
  <i>Built for zero-configuration, production-grade automated account generation and API key minting.</i>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-22272e.svg?style=flat-square" alt="License"></a>
  <a href="DISCLAIMER.md"><img src="https://img.shields.io/badge/Disclaimer-Legal%20Terms-red.svg?style=flat-square" alt="Disclaimer"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10%2B-3776ab.svg?style=flat-square&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://playwright.dev/"><img src="https://img.shields.io/badge/Playwright-Stealth-2EAD33.svg?style=flat-square&logo=playwright&logoColor=white" alt="Playwright"></a>
  <a href="https://github.com/waw666waw666/RegisterHub"><img src="https://img.shields.io/badge/Powered%20By-RegisterHub-purple.svg?style=flat-square" alt="Powered By"></a>
</p>

<p align="center">
  <a href="./README_EN.md">English</a> | <a href="./README.md">简体中文</a>
</p>

---

## Ecosystem & Backlink Notice

> **Framework Origin**:  
> This standalone tool is derived directly from **[RegisterHub](https://github.com/waw666waw666/RegisterHub)**, a general-purpose automated account registration and credential management framework.  
> 
> If you need multi-site orchestration, tri-channel disposable mailbox rotators, lifecycle credential verification, or automated adapter code generation scaffolds, check out our primary repository:  
> 
> **Main Framework Repository**: **[https://github.com/waw666waw666/RegisterHub](https://github.com/waw666waw666/RegisterHub)**

---

## Overview

A reference implementation for OAuth session capture and pure protocol takeover on Coarena (https://coarena.ai). Executes terms consent, API key minting, and quota validation via 100% REST protocol after Google authentication.

### Key Highlights

- **Post-OAuth Protocol Takeover**: Uses browser solely for session capture, followed by 100% pure protocol operations
- **Pure Protocol Key Minting**: Atomically signs terms and mints keys via REST endpoints
- **Real-time Quota Audit**: Verifies daily USD allowances via GET /api/v1/limits
- **Session Isolation**: Operates in isolated temporary profiles without host browser interference

---

## Quickstart

### 1. Prerequisites and Installation

Requires **Python ≥ 3.10**:

```bash
# Clone the repository
git clone https://github.com/waw666waw666/coarena-register.git
cd coarena-register

# Install dependencies
pip install -r requirements.txt

# Install Playwright browser binaries
playwright install chromium
```

### 2. Configuration & Crucial Guidance

Copy `config.example.json` to `config.json` to configure proxies or headless mode:

```json
{
  "email": null,
  "browser": {
    "headless": false,
    "slow_mo": 50,
    "timeout": 35000,
    "channel": "chrome",
    "proxy": "http://127.0.0.1:7897"
  },
  "output_dir": "./results"
}
```

### Crucial: Google OAuth Handoff & Pure Protocol Minting

1. **Google OAuth Authorization Handoff**:
   - Coarena does not support traditional password registration; authentication is 100% Google OAuth based;
   - When launched, click **"Continue with Google"** in the browser window to complete authentication;
2. **100% Pure REST Protocol Takeover**:
   - No UI clicking required after login;
   - The script captures session cookies and directly executes REST protocol endpoints:
     - Calls `/api/me/consent` to sign platform terms;
     - Calls `/api/me/keys` to mint a permanent API key named `RegisterHub-Key`;
     - Calls `/api/v1/limits` to verify daily quota, saving output to `results/accounts.txt`.

### 3. Execution

Launch via **`run.bat`** on Windows or execute directly via CLI:

```bash
# Mint 1 account & API key
python main.py

# Batch generate multiple accounts
python main.py -n 5

# Run headlessly in the background
python main.py --headless -n 1
```

Extracted credentials will be safely recorded in **`results/accounts.txt`**:
```text
email----password----api_key----timestamp
```

### 4. AI Co-Pilot Workflow (Cursor / Claude Code / Windsurf / Gemini)

This subproject is optimized for seamless interaction with AI coding assistants:

**Prerequisite**: Open this project folder (**`coarena-register`**) as your active workspace root in your AI editor.

Choose between two workflows:

- **Method 1: Direct Prompting (Quick Interaction)**: Ask your AI: `Please inspect the environment, configure config.json, run main.py, and ensure new account records are written to results/accounts.txt`.
- **Method 2: Provide Runtime Logs & Screenshots (Recommended for Precision)**: Run once manually or inspect the flow in your browser, then send live logs or screenshots directly to the AI:
  ```text
  I encountered this state while running the project (logs/screenshots attached). Please inspect according to AGENTS.md rules and resolve the blockage!
  ```
  The AI will directly correlate your real-world feedback with the project's stealth and pilot layers to patch the issue accurately!

---

## Ecosystem Portfolio

Part of the RegisterHub open-source automation family:

| Standalone Project | Characteristics | Source Repository |
| :--- | :--- | :--- |
| **RegisterHub** | General Registration Engine & Scaffolding | [GitHub](https://github.com/waw666waw666/RegisterHub) |
| **Deepgram Register** | $200 USD Allowance + reCAPTCHA v2 Penetration | [GitHub](https://github.com/waw666waw666/deepgram-register) |
| **100MilionSeek Register** | 100M Tokens/day + Instant Card Key Harvester | [GitHub](https://github.com/waw666waw666/100milionseek-register) |
| **AMD AI Dev Register** | Official AMD Program + Akamai Telemetry Parity | [GitHub](https://github.com/waw666waw666/amd-register) |
| **Coarena Register** | Post-OAuth Pure REST Protocol Key Minting | [GitHub](https://github.com/waw666waw666/coarena-register) |

---

## Legal Disclaimer

This project is intended strictly for authorized educational research, browser automation benchmarking, and legitimate quality assurance. Users must strictly adhere to the target platform's Terms of Service and all applicable regional laws. See [DISCLAIMER.md](DISCLAIMER.md).

---

## Community & Support

Join our developer community for technical discussions, custom adapter requests, and browser automation best practices:

- **Discord Community**: [Join Discord](https://discord.gg/USnVJ9YQX)
- **QQ Group**: 1130324020
