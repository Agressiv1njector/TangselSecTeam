# 🔎 RECON & OSINT FULL CHEATSHEET — Part 3

## 📑 Table of Contents (Part 3)
7. [URL & Historical Data Mining](#7-url--historical-data-mining)
8. [Web Crawling & Spidering](#8-web-crawling--spidering)
9. [Vulnerability Scanning](#9-vulnerability-scanning)

---

# 7. URL & Historical Data Mining

## 🔗 waybackurls
**Deskripsi**: Fetch semua URL yang pernah di-crawl oleh Wayback Machine untuk suatu domain.

```bash
# Install
go install github.com/tomnomnom/waybackurls@latest

# Basic
echo "target.com" | waybackurls

# Simpan ke file
echo "target.com" | waybackurls > wayback_urls.txt

# Hanya unique
echo "target.com" | waybackurls | sort -u > unique_urls.txt

# Filter extensions
echo "target.com" | waybackurls | grep -E "\.(php|asp|aspx|jsp|json|action|do|cfm)" > interesting_urls.txt

# Cari parameter
echo "target.com" | waybackurls | grep "=" > params_urls.txt

# Cari sensitive files
echo "target.com" | waybackurls | grep -iE "(config|backup|admin|login|api|secret|password|\.env|\.git|\.sql|\.bak)"

# Timestamps
echo "target.com" | waybackurls -dates

# Pipeline: check alive
echo "target.com" | waybackurls | httpx -silent -status-code -mc 200
```

---

## 🔗 gau (GetAllURLs)
**Deskripsi**: Fetch URLs dari Wayback Machine, Common Crawl, OTX, dan URLScan.

```bash
# Install
go install github.com/lc/gau/v2/cmd/gau@latest

# Basic
echo "target.com" | gau

# Simpan
echo "target.com" | gau -o gau_urls.txt

# Dari file
gau -i domains.txt -o all_urls.txt

# Filter providers
echo "target.com" | gau --providers wayback,commoncrawl,otx,urlscan

# Filter by mime
echo "target.com" | gau --mc 200

# Blacklist extension
echo "target.com" | gau --blacklist png,jpg,gif,css,woff,svg,ico

# Dengan threads
echo "target.com" | gau --threads 5

# Cari endpoints menarik
echo "target.com" | gau | grep -E "(api|graphql|rest|v[0-9])" | sort -u

# Cari parameters
echo "target.com" | gau | grep "=" | uro | sort -u

# JSON output
echo "target.com" | gau --json
```

---

## 🔗 waymore
**Deskripsi**: Versi yang lebih lengkap dari waybackurls/gau. Mencari URLs dari lebih banyak sumber dan bisa download archived responses.

```bash
# Install
pip install waymore

# Basic URL collection
waymore -i target.com -mode U

# Download responses
waymore -i target.com -mode R

# Both
waymore -i target.com -mode B

# Filter
waymore -i target.com -mode U -f -fc 404

# Limit
waymore -i target.com -mode U -l 1000

# Output directory
waymore -i target.com -mode U -oU urls.txt

# Config: ~/.config/waymore/config.yml
```

---

## 🔗 hakrawler
**Deskripsi**: Fast web crawler untuk URL discovery dan endpoint extraction.

```bash
# Install
go install github.com/hakluke/hakrawler@latest

# Basic (dari stdin)
echo "https://target.com" | hakrawler

# Depth
echo "https://target.com" | hakrawler -d 3

# Scope (only same domain)
echo "https://target.com" | hakrawler -subs

# With headers
echo "https://target.com" | hakrawler -h "Authorization: Bearer TOKEN"

# Insecure (skip SSL verify)
echo "https://target.com" | hakrawler -insecure

# Output
echo "https://target.com" | hakrawler > crawled_urls.txt

# Pipeline
echo "https://target.com" | hakrawler | grep "=" | uro > params.txt
```

---

## 🔗 katana (ProjectDiscovery Crawler)
**Deskripsi**: Next-gen web crawler dari ProjectDiscovery. Support headless browsing, JavaScript rendering.

```bash
# Install
go install github.com/projectdiscovery/katana/cmd/katana@latest

# Basic crawl
katana -u https://target.com

# Dari file
katana -list urls.txt

# Depth
katana -u https://target.com -d 5

# Headless (JavaScript rendering)
katana -u https://target.com -headless

# Form fill (auto-fill forms)
katana -u https://target.com -headless -form-fill

# Scope control
katana -u https://target.com -cs target.com  # crawl scope
katana -u https://target.com -fs logout      # filter scope

# Fields to display
katana -u https://target.com -f url,path,fqdn,endpoint

# Extension filter
katana -u https://target.com -em php,html,js,json

# Output
katana -u https://target.com -o output.txt
katana -u https://target.com -jsonl -o output.json

# Concurrency
katana -u https://target.com -c 20 -p 10

# Headers
katana -u https://target.com -H "Cookie: session=abc123"

# JavaScript file parsing
katana -u https://target.com -jc

# Automatic form fill
katana -u https://target.com -aff

# Pipeline
subfinder -d target.com -silent | httpx -silent | katana -d 3 -jc -o all_endpoints.txt
```

---

## 🔗 Wayback Machine (Manual)
**Deskripsi**: Web interface untuk browsing archived pages.

```bash
# Web Interface
https://web.archive.org/web/*/target.com

# CDX API (search archived URLs)
curl "https://web.archive.org/cdx/search/cdx?url=*.target.com&output=json&fl=original&collapse=urlkey" | jq

# Specific timestamp
https://web.archive.org/web/20230101/https://target.com

# Availability API
curl "https://archive.org/wayback/available?url=target.com" | jq

# Bulk CDX query
curl "https://web.archive.org/cdx/search/cdx?url=target.com/*&output=text&fl=original,statuscode,timestamp&collapse=urlkey" > archived_urls.txt
```

---

# 8. Web Crawling & Spidering

## 🕷️ hakrawler
> Sudah dicover di Section 7. Lihat di atas.

---

## 🕷️ katana
> Sudah dicover di Section 7. Lihat di atas.

---

## 🕷️ gospider
**Deskripsi**: Fast web spider dari Go. Crawl website, extract links, JS files, subdomains.

```bash
# Install
go install github.com/jaeles-project/gospider@latest

# Basic
gospider -s https://target.com

# Depth
gospider -s https://target.com -d 3

# Concurrent
gospider -s https://target.com -c 10 -t 5

# Include subdomains
gospider -s https://target.com --subs

# Include other sources (Wayback, CommonCrawl, VirusTotal)
gospider -s https://target.com --other-source

# Sitemap
gospider -s https://target.com --sitemap

# Robots.txt
gospider -s https://target.com --robots

# Custom header
gospider -s https://target.com -H "Cookie: session=abc123"

# Output
gospider -s https://target.com -o output_dir

# Dari file
gospider -S urls.txt -c 10 -d 3 -o output_dir

# Blacklist
gospider -s https://target.com --blacklist ".(jpg|jpeg|gif|css|png|svg|ico|woff)"

# Pipeline: extract JS files
gospider -s https://target.com -d 2 --js | grep "\.js$" > js_files.txt
```

---

## 🕷️ crawlergo
**Deskripsi**: Browser-based crawler menggunakan headless Chrome. Bagus untuk SPA / dynamic websites.

```bash
# Install
# Download dari https://github.com/nicedoc/crawlergo/releases

# Basic
./crawlergo -c /path/to/chrome -t 5 https://target.com

# Dengan output
./crawlergo -c /path/to/chrome -t 5 -o output.json https://target.com

# Custom headers
./crawlergo -c /path/to/chrome --custom-headers '{"Cookie":"session=abc"}' https://target.com

# Push to proxy (Burp)
./crawlergo -c /path/to/chrome --push-to-proxy http://127.0.0.1:8080 https://target.com

# Incognito mode
./crawlergo -c /path/to/chrome --incognito-context https://target.com

# Max crawl count
./crawlergo -c /path/to/chrome --max-crawled-count 1000 https://target.com
```

---

## 🕷️ Burp Suite Crawler
**Deskripsi**: Built-in crawler di Burp Suite Pro. Support authenticated crawling.

```
# Burp Suite Pro → Target tab

# Passive Spider (otomatis saat browsing via proxy):
1. Set browser proxy → 127.0.0.1:8080
2. Browse target secara manual
3. Semua links & resources tercapture di Site Map

# Active Crawler:
1. Target → Site map → klik kanan domain
2. "Crawl this host" atau "Scan" → Crawl only
3. Configure:
   - Crawl optimization: Faster/Normal/Thorough
   - Maximum crawl depth
   - Maximum unique locations
   - Login credentials (for authenticated crawl)
4. Start crawl

# Crawl dengan Login:
1. New Scan → Crawl
2. Application login → Record login sequence
3. Atau set session handling rules
4. Start

# Export URLs:
1. Target → Site map → Select all
2. Right-click → Copy URLs
3. Atau: Save selected items
```

---

# 9. Vulnerability Scanning

## 🔐 Nuclei (Template-based)
**Deskripsi**: Fast vulnerability scanner dari ProjectDiscovery. Menggunakan YAML templates. Sangat extensible.

```bash
# Install
go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest

# Update templates
nuclei -update-templates

# ===== BASIC SCANNING =====
nuclei -u https://target.com

# Dari file
nuclei -l urls.txt

# ===== FILTER TEMPLATES =====
# By severity
nuclei -u https://target.com -s critical,high
nuclei -u https://target.com -s medium,low,info

# By tag
nuclei -u https://target.com -tags cve,rce,sqli,xss,lfi
nuclei -u https://target.com -tags tech,exposure,misconfig

# By template ID
nuclei -u https://target.com -t cves/2024/

# By author
nuclei -u https://target.com -author pdteam

# Exclude
nuclei -u https://target.com -exclude-tags dos,fuzz

# ===== SPECIFIC TEMPLATES =====
nuclei -u https://target.com -t http/cves/
nuclei -u https://target.com -t http/exposures/
nuclei -u https://target.com -t http/misconfiguration/
nuclei -u https://target.com -t http/technologies/
nuclei -u https://target.com -t http/vulnerabilities/

# Custom template
nuclei -u https://target.com -t /path/to/custom-template.yaml

# ===== OUTPUT =====
nuclei -u https://target.com -o results.txt
nuclei -u https://target.com -json -o results.json
nuclei -u https://target.com -me output_dir  # markdown export

# ===== PERFORMANCE =====
nuclei -l urls.txt -c 50 -rl 150  # concurrency & rate limit
nuclei -l urls.txt -bs 50         # bulk size
nuclei -l urls.txt -timeout 10

# ===== PIPELINE =====
subfinder -d target.com -silent | httpx -silent | nuclei -s critical,high -o vulns.txt

# ===== CUSTOM TEMPLATE EXAMPLE =====
cat << 'EOF' > custom-check.yaml
id: custom-sensitive-file
info:
  name: Sensitive File Check
  severity: high
  tags: exposure
http:
  - method: GET
    path:
      - "{{BaseURL}}/.env"
      - "{{BaseURL}}/.git/config"
      - "{{BaseURL}}/wp-config.php.bak"
    matchers:
      - type: status
        status:
          - 200
EOF
nuclei -u https://target.com -t custom-check.yaml
```

---

## 🔐 Nikto
**Deskripsi**: Web server scanner. Checks untuk dangerous files, outdated software, misconfigurations.

```bash
# Install
sudo apt install nikto

# Basic scan
nikto -h https://target.com

# Specific port
nikto -h target.com -p 8080

# Multiple ports
nikto -h target.com -p 80,443,8080,8443

# Tuning (test types)
nikto -h target.com -T 1234567890abcde
# 1=Files, 2=Misconfig, 3=Info, 4=Injection
# 5=Remote, 6=DOS, 7=Remote, 8=Command exec
# 9=SQL Injection, a=Auth bypass, b=Software ID

# SSL
nikto -h https://target.com -ssl

# Proxy
nikto -h target.com -useproxy http://127.0.0.1:8080

# Output
nikto -h target.com -o report.html -Format html
nikto -h target.com -o report.csv -Format csv
nikto -h target.com -o report.xml -Format xml

# Custom headers
nikto -h target.com -H "Cookie: session=abc123"

# Evasion
nikto -h target.com -evasion 1
# 1=Random URI encoding, 2=Directory self-reference
# 3=Premature URL ending, 4=Prepend long random
# 5=Fake parameter, 6=TAB as request spacer
# 7=Change URL case, 8=Use Windows dir separator

# Dari file
nikto -h hosts.txt

# Update database
nikto -update
```

---

## 🔐 OpenVAS
**Deskripsi**: Open-source vulnerability scanner. Full network vulnerability assessment.

```bash
# Install (Kali/Debian)
sudo apt install openvas
sudo gvm-setup          # Initial setup
sudo gvm-start          # Start services

# Web Interface: https://127.0.0.1:9392
# Default: admin / (generated password from setup)

# CLI (gvm-cli)
gvm-cli --gmp-username admin --gmp-password PASSWORD socket --socketpath /run/gvmd.sock

# Workflow:
# 1. Configuration → Targets → New Target
# 2. Set host/IP range
# 3. Scans → Tasks → New Task
# 4. Select target & scan config
# 5. Start task
# 6. View results & reports

# Scan Configs:
# - Discovery: Host discovery only
# - Host Discovery: Quick host discovery
# - System Discovery: OS & service detection
# - Full and Fast: Complete vulnerability scan (recommended)
# - Full and Deep: Thorough (slower)
```

---

## 🔐 Nessus
**Deskripsi**: Commercial vulnerability scanner dari Tenable. Industry standard.

```bash
# Install
# Download dari https://www.tenable.com/products/nessus
# Linux:
sudo dpkg -i Nessus-*.deb
sudo systemctl start nessusd

# Web Interface: https://127.0.0.1:8834

# Nessus CLI (nessuscli)
/opt/nessus/sbin/nessuscli update              # Update plugins
/opt/nessus/sbin/nessuscli adduser             # Add user

# API
# List scans
curl -k -X GET "https://127.0.0.1:8834/scans" \
  -H "X-ApiKeys: accessKey=ACCESS;secretKey=SECRET"

# Launch scan
curl -k -X POST "https://127.0.0.1:8834/scans/SCAN_ID/launch" \
  -H "X-ApiKeys: accessKey=ACCESS;secretKey=SECRET"

# Scan Types:
# - Basic Network Scan
# - Advanced Scan
# - Web Application Tests
# - Credentialed Patch Audit
# - Malware Scan
# - Policy Compliance
```

---

## 🔐 Acunetix
**Deskripsi**: Commercial web application vulnerability scanner. DAST (Dynamic Application Security Testing).

```bash
# Web Interface (setelah install)
# https://127.0.0.1:3443

# API
# Add target
curl -k -X POST "https://127.0.0.1:3443/api/v1/targets" \
  -H "X-Auth: API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"address":"https://target.com","description":"Test"}'

# Start scan
curl -k -X POST "https://127.0.0.1:3443/api/v1/scans" \
  -H "X-Auth: API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target_id":"TARGET_ID","profile_id":"PROFILE_ID"}'

# Scan Profiles:
# - Full Scan
# - High Risk Vulnerabilities
# - SQL Injection
# - XSS
# - Weak Passwords
# - Crawl Only
# - Malware Scan
```

---

## 🔐 OWASP ZAP (zaproxy)
**Deskripsi**: Open-source web application security scanner. Proxy, spider, active/passive scanner.

```bash
# Install
sudo apt install zaproxy
# atau download dari https://www.zaproxy.org/download/

# GUI mode
zaproxy

# Headless/daemon mode
zaproxy -daemon -port 8080

# ===== CLI SCANNING =====
# Quick scan
zap-cli quick-scan https://target.com

# Active scan
zap-cli active-scan https://target.com

# Spider
zap-cli spider https://target.com

# Full scan (spider + active)
zap-cli quick-scan -s all -r -l Informational https://target.com

# ===== API =====
# Spider
curl "http://127.0.0.1:8080/JSON/spider/action/scan/?apikey=API_KEY&url=https://target.com"

# Active scan
curl "http://127.0.0.1:8080/JSON/ascan/action/scan/?apikey=API_KEY&url=https://target.com"

# Get alerts
curl "http://127.0.0.1:8080/JSON/alert/view/alerts/?apikey=API_KEY" | jq

# ===== DOCKER =====
# Baseline scan (passive only)
docker run -t zaproxy/zap-stable zap-baseline.py -t https://target.com

# Full scan
docker run -t zaproxy/zap-stable zap-full-scan.py -t https://target.com

# API scan
docker run -t zaproxy/zap-stable zap-api-scan.py -t https://target.com/api/swagger.json -f openapi

# Report output
docker run -v $(pwd):/zap/wrk/:rw -t zaproxy/zap-stable zap-baseline.py \
  -t https://target.com -r report.html

# ===== ZAP FEATURES =====
# Proxy: 127.0.0.1:8080 (default)
# Passive Scanner: otomatis saat traffic lewat proxy
# Active Scanner: klik kanan URL → Attack → Active Scan
# Fuzzer: klik kanan parameter → Fuzz
# Break: intercept & modify requests
# Script Console: custom scripts (JS, Python, Groovy)
```
