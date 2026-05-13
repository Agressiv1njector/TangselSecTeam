# 🔎 RECON, OSINT & EXPLOITATION — FULL CHEATSHEET

> **Author**: TangselSecTeam | **Last Updated**: April 2026
>
> ⚠️ **Hanya untuk tujuan pendidikan & ethical hacking dengan izin tertulis.**

---

## 📁 File Structure

| # | File | OWASP | Content |
|---|------|-------|---------|
| 1 | [01-information-gathering.md](./01-information-gathering.md) | Recon | DNS, Subdomain, OSINT (22 tools) |
| 2 | [02-fingerprinting-scanning-discovery.md](./02-fingerprinting-scanning-discovery.md) | Recon | Nmap, ffuf, Gobuster (18 tools) |
| 3 | [03-url-crawling-vulnscan.md](./03-url-crawling-vulnscan.md) | Recon | gau, katana, Nuclei (14 tools) |
| 4 | [04-cloud-api-params-automation.md](./04-cloud-api-params-automation.md) | Recon | Cloud, API, Automation (18 tools) |
| 5A | [05a-vulnscan-web-exploits.md](./05a-vulnscan-web-exploits.md) | Exploit | ZAP, Burp Suite, SQLMap, XSS |
| 5B | [05b-exploitation-postexploit.md](./05b-exploitation-postexploit.md) | Exploit | Metasploit, Hydra, Hashcat, PrivEsc |
| 5C-1 | [05c1-injection-sqli-xss-cmdi.md](./05c1-injection-sqli-xss-cmdi.md) | A03 Inj | SQLi, XSS, CMDi (10 CWEs) |
| 5C-2 | [05c2-injection-ldap-xpath-xxe-ssti.md](./05c2-injection-ldap-xpath-xxe-ssti.md) | A03 Inj | LDAP, XPath, XXE, SSTI (27 CWEs) |
| 6A | [06a-access-control-traversal-csrf-ssrf.md](./06a-access-control-traversal-csrf-ssrf.md) | A01 | Path Traversal, CSRF, SSRF |
| 6B | [06b-access-control-authz-idor-exposure.md](./06b-access-control-authz-idor-exposure.md) | A01 | IDOR, AuthZ, Info Exposure |
| 7A | [07a-auth-bypass-jwt-bruteforce.md](./07a-auth-bypass-jwt-bruteforce.md) | A07 | Auth Bypass, JWT, Brute Force |
| 7B | [07b-session-credentials-recovery.md](./07b-session-credentials-recovery.md) | A07 | Session, Credentials, Recovery |
| 8 | [08-supply-chain-failures.md](./08-supply-chain-failures.md) | A03:2025 | SBOM, CI/CD, Dependencies |
| 9 | [09-ssrf-deep-dive.md](./09-ssrf-deep-dive.md) | A10 | SSRF full exploitation chain |
| 10 | [10-social-engineering-phishing.md](./10-social-engineering-phishing.md) | SE | IDN Homograph, Phishing, 25 techniques |
| 11 | [11-insecure-design-misconfig.md](./11-insecure-design-misconfig.md) | A04+A05 | File Upload, Smuggling, CORS, Cloud |

---

## 🎯 PoC Cheatsheet (Proof of Concept)

| Level | File | Jumlah PoC | Fokus |
|-------|------|------------|-------|
| 🟢 Low | [poc-level-low.md](./poc-level-low.md) | 20 PoC | IDOR, Disclosure, Cookie, Headers, Misconfiguration |
| 🟡 Medium | [poc-level-medium.md](./poc-level-medium.md) | 25 PoC | XSS, SQLi, CSRF, SSRF, XXE, JWT, File Upload |
| 🔴 High | [poc-level-high.md](./poc-level-high.md) | 20 PoC | RCE, Takeover, Race Condition, Attack Chain |

---

## 🔧 Tools

| Tool | Path | Description |
|------|------|-------------|
| `homograph_edu.py` | [tools/homograph_edu.py](./tools/homograph_edu.py) | IDN Homograph education tool |

---

## 📊 Coverage

| Category | Files | Count |
|----------|-------|-------|
| 🔎 Recon & OSINT | Part 1-4 | 80+ tools |
| 🔧 Exploitation | Part 5A-5B | 20+ tools |
| 💉 A03 Injection | Part 5C | 37 CWEs |
| 🔓 A01 Access Control | Part 6A-6B | 40 CWEs |
| 🔑 A07 Auth Failures | Part 7A-7B | 37 CWEs |
| 📦 A03:2025 Supply Chain | Part 8 | 6 CWEs |
| 🌐 A10 SSRF Deep Dive | Part 9 | Full exploit chain |
| 🎭 Social Engineering | Part 10 | 25 phishing techniques |
| 🏗️ A04+A05 Design+Misconfig | Part 11 | 40 CWEs + cloud/CORS/TLS |
| 🎯 PoC Praktik | Low+Med+High | 65 PoC scenarios |

**Total: 80+ tools | 160+ CWEs | 65 PoC | 20 files | ~360KB**
