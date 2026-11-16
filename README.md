# Coarena AutoRegister

> **Coarena AI 平台谷歌登录后 100% 纯协议注册与 API Key 极速提纯工具**  
> 遵循“开箱即用，极简交付”原则，零复杂配置，一键下号并提取可用 API Key。

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/playwright-stealth-orange.svg)](https://playwright.dev/)
[![Powered By](https://img.shields.io/badge/Powered%20By-AutoRegister%20Community-purple.svg)](https://github.com/waw666waw666/register-community)

---

##  框架母港与生态互链 (Ecosystem Backlink)

>  **项目背景与互相引流说明**：  
> 本独立工程由 **[AutoRegister Community](https://github.com/waw666waw666/register-community)** 开源注册自动化主框架一键解耦派生。  
> 
> 如果你需要探索**更多站点的自动化支持**（如 Deepgram、100MilionSeek、AMD、Coarena、QuanticData 等）、**三通道公网临时邮箱轮换**、**账号资产全生命周期审计**、或通过**脚手架一键生成新站点适配器**，欢迎前往并 Star 我们的主框架仓库：  
> 
>  **主框架项目传送门**：**[https://github.com/waw666waw666/register-community](https://github.com/waw666waw666/register-community)**

---

##  项目简介

针对 Coarena (https://coarena.ai) 打造的 OAuth 会话捕获与纯协议接管示范工具。在 Google 授权后 100% 通过 REST 协议完成平台条款签署、永久 API Key 签发与每日额度核验。

###  核心优势与技术特征

-  **OAuth 鉴权后协议接管**：生动示范浏览器仅用于换取会话 Cookie，后续业务全部纯协议接管
-  **100% 协议提纯**：POST /api/me/consent 签署条款 + POST /api/me/keys 毫秒级直出 Key
-  **额度实时验活**：调用 GET /api/v1/limits 自动校验每日可用额度与权限
- ️ **环境自洽与会话隔离**：独立临时 Session 运行，绝不干扰用户本地常用浏览器

---

##  极速上手

### 1. 环境准备与依赖安装

确保你的系统已安装 **Python ≥ 3.10**：

```bash
# 1. 克隆本项目
git clone https://github.com/waw666waw666/coarena-register.git
cd coarena-register

# 2. 安装核心依赖
pip install -r requirements.txt

# 3. 安装 Playwright 浏览器驱动内核
playwright install chromium
```

### 2. 运行配置 (可选)

项目根目录提供开箱即用的 `config.example.json`。如需挂载本地代理或修改超时，直接复制为 `config.json` 即可：

```json
{
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

### 3. 一键启动下号

在 Windows 终端中直接双击 **`run.bat`** 交互菜单，或在命令行运行：

```bash
# 默认生成 1 个账号凭据
python main.py

# 批量生成指定数量账号（如 5 个）
python main.py -n 5

# 无头静默模式运行
python main.py --headless -n 1
```

执行完毕后，所有生成的账号凭据将原子持久化落盘至 **`results/accounts.txt`**：
```text
邮箱----密码----有效API_Key----时间戳
```

---

## ️ 体系化生态矩阵

本工程为 AutoRegister 家族核心实战矩阵之一：

| 独立开源项目 | 核心特色与福利 | 源码直达 |
| :--- | :--- | :--- |
| **AutoRegister Community** |  通用自动化注册母港与脚手架引擎 | [GitHub](https://github.com/waw666waw666/register-community) |
| **Deepgram AutoRegister** |  官方 $200 免费额度 + 谷歌人机穿透 + 纯协议提 Key | [GitHub](https://github.com/waw666waw666/deepgram-register) |
| **100MilionSeek AutoRegister** |  每天免费 1 亿 Token 算力 + 免收信秒出 Key + 母号裂变 | [GitHub](https://github.com/waw666waw666/100milionseek-register) |
| **AMD AI Dev AutoRegister** |  AMD 官方大厂计划 + Akamai 遥测 + OneTrust 穿透 | [GitHub](https://github.com/waw666waw666/amd-register) |
| **Coarena AutoRegister** |  谷歌登录后 100% 协议提 Key 与每日额度审计 | [GitHub](https://github.com/waw666waw666/coarena-register) |

---

## ️ 免责声明 (Disclaimer)

本项目仅供软件工程自动化、浏览器驾驶协议与网络可用性技术交流与合法测试使用。使用者必须严格遵守目标平台服务条款与当地法律法规，严禁将本项目用于未经授权的大规模滥用或非法用途。作者不对任何因使用本项目造成的损失承担法律责任。详见 [DISCLAIMER.zh.md](DISCLAIMER.zh.md)。
