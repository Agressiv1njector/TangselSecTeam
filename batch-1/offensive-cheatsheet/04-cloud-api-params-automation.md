# 🔎 RECON & OSINT FULL CHEATSHEET — Part 4

## 📑 Table of Contents (Part 4)
10. [Cloud & Asset Discovery](#10-cloud--asset-discovery)
11. [API & Endpoint Discovery](#11-api--endpoint-discovery)
12. [Parameter & Hidden Input Discovery](#12-parameter--hidden-input-discovery)
13. [Automation Framework (All-in-One)](#13-automation-framework-all-in-one)

---

# 10. Cloud & Asset Discovery

## ☁️ CloudEnum
**Deskripsi**: Multi-cloud OSINT tool. Enumerate cloud resources publik (S3, Azure, GCP) berdasarkan keyword.

```bash
# Install
git clone https://github.com/initstring/cloud_enum.git
cd cloud_enum
pip install -r requirements.txt

# Basic scan
python3 cloud_enum.py -k target

# Multiple keywords
python3 cloud_enum.py -k target -k targetcorp -k target-prod

# Dari file
python3 cloud_enum.py -kf keywords.txt

# Spesifik cloud
python3 cloud_enum.py -k target --disable-azure --disable-gcp   # AWS only
python3 cloud_enum.py -k target --disable-aws --disable-gcp     # Azure only
python3 cloud_enum.py -k target --disable-aws --disable-azure   # GCP only

# Custom mutations
python3 cloud_enum.py -k target -m mutations.txt

# Threads
python3 cloud_enum.py -k target -t 10

# Output
python3 cloud_enum.py -k target -l output.txt
```

**Yang dicari**:
- AWS S3 Buckets, Azure Blobs, GCP Buckets
- Open/listable storage
- Sensitive files (backups, configs, databases)

---

## ☁️ S3Scanner
**Deskripsi**: Scan S3 buckets untuk permission issues (public read, write, list).

```bash
# Install
pip install s3scanner

# Scan single bucket
s3scanner scan --bucket target-bucket

# Dari file
s3scanner scan --buckets-file bucket_names.txt

# Dump (download) public bucket contents
s3scanner dump --bucket target-public-bucket --out-dir ./dump/

# Enumerate objects
s3scanner scan --bucket target-bucket --enumerate

# Check permissions
s3scanner scan --bucket target-bucket --check-permissions

# Generate bucket names (common patterns)
# target, target-prod, target-dev, target-staging
# target-backup, target-data, target-assets
# target.com, www.target.com
```

---

## ☁️ BucketFinder
**Deskripsi**: Tool untuk menemukan S3 buckets yang terbuka berdasarkan wordlist.

```bash
# Install
git clone https://github.com/FishermansEnemy/bucket_finder.git

# Basic
ruby bucket_finder.rb wordlist.txt

# Dengan download
ruby bucket_finder.rb --download wordlist.txt

# Dengan region
ruby bucket_finder.rb --region us-east-1 wordlist.txt

# Wordlist example (bucket_names.txt):
# target
# target-backup
# target-dev
# target-staging
# target-prod
# target-assets
# target-data
# target-uploads
# target-logs
# target.com
```

---

## ☁️ AWSBucketDump
**Deskripsi**: Enumerate S3 buckets dan search content untuk sensitive information.

```bash
# Install
git clone https://github.com/jordanpotti/AWSBucketDump.git
cd AWSBucketDump
pip install -r requirements.txt

# Basic
python AWSBucketDump.py -l bucket_names.txt -g interesting_keywords.txt

# Download matches
python AWSBucketDump.py -l bucket_names.txt -g keywords.txt -D

# Max file size
python AWSBucketDump.py -l bucket_names.txt -g keywords.txt -m 1024

# Threads
python AWSBucketDump.py -l bucket_names.txt -g keywords.txt -t 10

# Keywords file (interesting_keywords.txt):
# password
# secret
# credential
# backup
# config
# .env
# private
# key
# token
# database
```

---

## ☁️ GrayhatWarfare
**Deskripsi**: Search engine untuk open S3 buckets dan Azure blobs.

```bash
# Web-based: https://buckets.grayhatwarfare.com

# Search by keyword
https://buckets.grayhatwarfare.com/files?keywords=target.com

# API (paid plans)
# List buckets
curl "https://buckets.grayhatwarfare.com/api/v2/buckets?keywords=target" \
  -H "Authorization: Bearer API_KEY"

# Search files
curl "https://buckets.grayhatwarfare.com/api/v2/files?keywords=password&bucket=target" \
  -H "Authorization: Bearer API_KEY"

# Filters: bucket type, file extension, etc.
```

---

# 11. API & Endpoint Discovery

## 📱 Postman (Manual Testing)
**Deskripsi**: GUI tool untuk API testing. Manual exploration, collection building, environment variables.

```
# Download: https://www.postman.com/downloads/

# Workflow:
1. Import API spec (Swagger/OpenAPI/GraphQL)
2. Atau manual: New Request → set method, URL, headers, body
3. Collections → organize endpoints
4. Environments → manage variables (base_url, token, etc.)

# Useful Features:
- Pre-request scripts: auto-generate auth tokens
- Tests tab: validate responses
- Collection Runner: batch test all endpoints
- Interceptor: capture browser requests

# Tips untuk recon:
- Import swagger.json / openapi.yaml
- Use Collection Runner untuk test semua endpoints
- Check authorization: try accessing without token
- Check IDOR: iterate IDs
- Check method tampering: GET → POST → PUT → DELETE
```

---

## 📱 Kiterunner
**Deskripsi**: API endpoint discovery tool. Brute force API routes dengan context-aware wordlists.

```bash
# Install
git clone https://github.com/assetnote/kiterunner.git
cd kiterunner && make build

# Download wordlists
kr kb update

# ===== SCAN MODE =====
# Basic API scan
kr scan https://target.com -w routes-large.kite

# Wordlist mode
kr brute https://target.com -w /path/to/wordlist.txt

# Multiple targets
kr scan -f hosts.txt -w routes-large.kite

# ===== OPTIONS =====
# Concurrency
kr scan https://target.com -w routes-large.kite -x 20

# Headers
kr scan https://target.com -w routes-large.kite -H "Authorization: Bearer TOKEN"

# Filter status
kr scan https://target.com -w routes-large.kite --success-status-codes 200,201,204

# Output
kr scan https://target.com -w routes-large.kite -o results.txt

# ===== REPLAY (investigate findings) =====
kr kb replay -w routes-large.kite "GET /api/v1/users 200"
```

---

## 📱 Arjun (Parameter Discovery)
**Deskripsi**: Tool untuk menemukan hidden HTTP parameters di web applications.

```bash
# Install
pip install arjun

# GET parameter discovery
arjun -u https://target.com/page

# POST parameters
arjun -u https://target.com/page -m POST

# JSON parameters
arjun -u https://target.com/api -m JSON

# Custom wordlist
arjun -u https://target.com/page -w /path/to/params.txt

# Headers
arjun -u https://target.com/page --headers "Cookie: session=abc123"

# Multiple URLs
arjun -i urls.txt

# Output
arjun -u https://target.com/page -oJ output.json
arjun -u https://target.com/page -oT output.txt

# Threads
arjun -u https://target.com/page -t 10

# Stable mode (slower but accurate)
arjun -u https://target.com/page --stable

# Delay
arjun -u https://target.com/page -d 2

# Include headers as parameters
arjun -u https://target.com/page --include "Content-Type"
```

---

## 📱 ParamSpider
**Deskripsi**: Mining parameters dari web archives (Wayback Machine). Menemukan parameter unik per endpoint.

```bash
# Install
pip install paramspider

# Basic
paramspider -d target.com

# Exclude extensions
paramspider -d target.com --exclude woff,css,js,png,jpg,gif,svg

# Level (crawl depth)
paramspider -d target.com -l high

# Output
paramspider -d target.com -o params.txt

# Placeholder (for fuzzing)
paramspider -d target.com -p "FUZZ"

# Pipeline: ParamSpider → SQLi testing
paramspider -d target.com -p "FUZZ" | httpx -silent | nuclei -t sqli/

# Pipeline: ParamSpider → XSS testing  
paramspider -d target.com | dalfox pipe
```

---

# 12. Parameter & Hidden Input Discovery

## 🧪 Arjun
> Sudah dicover di Section 11. Lihat di atas.

---

## 🧪 ParamSpider
> Sudah dicover di Section 11. Lihat di atas.

---

## 🧪 x8
**Deskripsi**: Hidden parameter discovery tool. Mendeteksi parameter tersembunyi di URL, headers, dan body.

```bash
# Install
cargo install x8
# atau download binary dari releases

# URL parameter discovery
x8 -u "https://target.com/page" -w params.txt

# POST body
x8 -u "https://target.com/page" -w params.txt -m POST

# Headers discovery
x8 -u "https://target.com/page" -w params.txt --headers

# Custom wordlist
x8 -u "https://target.com/page" -w /path/to/wordlist.txt

# JSON body
x8 -u "https://target.com/api" -w params.txt -b '{"test":"value"}' -t json

# Cookie
x8 -u "https://target.com/page" -w params.txt -H "Cookie: session=abc"

# Output
x8 -u "https://target.com/page" -w params.txt -o results.json

# Concurrency
x8 -u "https://target.com/page" -w params.txt -c 10

# Custom header injection point
x8 -u "https://target.com/page" -w params.txt --param-template "%%=value"
```

---

## 🧪 gf (Pattern Matching)
**Deskripsi**: Grep wrapper dari tomnomnom. Menggunakan pattern files untuk extract specific patterns dari URL lists.

```bash
# Install
go install github.com/tomnomnom/gf@latest

# Install patterns
git clone https://github.com/1ndianl33t/Gf-Patterns.git
cp Gf-Patterns/*.json ~/.gf/

# ===== USAGE =====
# Cari potential XSS
cat urls.txt | gf xss

# Cari potential SQLi
cat urls.txt | gf sqli

# Cari potential SSRF
cat urls.txt | gf ssrf

# Cari potential LFI
cat urls.txt | gf lfi

# Cari potential RCE
cat urls.txt | gf rce

# Cari potential IDOR
cat urls.txt | gf idor

# Cari potential Open Redirect
cat urls.txt | gf redirect

# Cari potential SSTI
cat urls.txt | gf ssti

# Cari debug/error pages
cat urls.txt | gf debug-logic

# Cari interesting parameters
cat urls.txt | gf interestingparams

# Cari AWS keys
cat urls.txt | gf aws-keys

# ===== PIPELINE =====
# Full workflow
echo "target.com" | gau | gf sqli | httpx -silent | nuclei -t sqli/

echo "target.com" | gau | gf xss | dalfox pipe

echo "target.com" | waybackurls | gf lfi | httpx -silent > lfi_targets.txt

# ===== CUSTOM PATTERN =====
# ~/.gf/custom.json
cat << 'EOF' > ~/.gf/custom.json
{
    "flags": "-HnrE",
    "patterns": [
        "admin",
        "config",
        "secret",
        "token"
    ]
}
EOF
cat urls.txt | gf custom
```

---

# 13. Automation Framework (All-in-One)

## 🧰 ReconFTW
**Deskripsi**: All-in-one recon framework. Menjalankan semua tools recon secara otomatis dan menghasilkan report komprehensif.

```bash
# Install
git clone https://github.com/six2dez/reconftw.git
cd reconftw
./install.sh

# ===== BASIC =====
# Full recon
./reconftw.sh -d target.com -r

# All (reconnaissance + vulnerability)
./reconftw.sh -d target.com -a

# ===== SPECIFIC MODULES =====
# Subdomain enumeration only
./reconftw.sh -d target.com -s

# Web probing
./reconftw.sh -d target.com -p

# OSINT
./reconftw.sh -d target.com -o

# Vulnerability scanning
./reconftw.sh -d target.com -v

# Full scan (tanpa fuzzing)
./reconftw.sh -d target.com -r

# ===== OPTIONS =====
# Multiple domains
./reconftw.sh -l domains.txt -r

# Custom config
./reconftw.sh -d target.com -r -c custom_config.cfg

# Output directory
./reconftw.sh -d target.com -r -o /path/to/output

# ===== MODULES INCLUDED =====
# Subdomain enum: subfinder, amass, findomain, assetfinder, crt.sh
# DNS resolution: dnsx, puredns
# Web probing: httpx
# Screenshots: gowitness
# Port scanning: naabu
# Directory brute: ffuf, dirsearch
# URL gathering: waybackurls, gau, katana
# Vulnerability: nuclei, nikto
# JS analysis: linkfinder, secretfinder
# CORS check, SSRF check, Open redirect check, etc.
```

---

## 🧰 LazyRecon
**Deskripsi**: Automated recon script. Subdomain discovery → port scan → content discovery → screenshot.

```bash
# Install
git clone https://github.com/nahamsec/lazyrecon.git
cd lazyrecon

# Edit config
nano lazyrecon.sh  # set paths to tools & wordlists

# Run
./lazyrecon.sh -d target.com

# Features:
# - Subdomain enumeration (subfinder, assetfinder, amass)
# - DNS resolution
# - HTTP probing
# - Port scanning (nmap/masscan)
# - Content discovery (ffuf/gobuster)
# - Screenshot (aquatone)
# - Report generation
```

---

## 🧰 AutoRecon
**Deskripsi**: Multi-threaded network reconnaissance tool. Otomatis enumerate services yang ditemukan.

```bash
# Install
pip install autorecon
# atau
sudo apt install autorecon

# Basic scan (single target)
autorecon target.com

# Multiple targets
autorecon target1.com target2.com 192.168.1.0/24

# Dari file
autorecon -t targets.txt

# Specific ports
autorecon target.com -p 80,443,8080

# All ports
autorecon target.com --only-scans-dir

# Verbose
autorecon target.com -v

# Output directory
autorecon target.com -o /path/to/output

# Concurrent targets
autorecon target.com --single-target

# ===== OUTPUT STRUCTURE =====
# results/
# └── target.com/
#     ├── scans/
#     │   ├── tcp_port_scan.nmap
#     │   ├── udp_port_scan.nmap
#     │   ├── tcp_80_http_nmap.txt
#     │   ├── tcp_80_http_gobuster.txt
#     │   ├── tcp_80_http_nikto.txt
#     │   └── ...
#     ├── exploit/
#     └── loot/
```

---

## 🧰 Osmedeus
**Deskripsi**: Workflow engine untuk offensive security. Automated recon dengan customizable workflows.

```bash
# Install
go install -v github.com/j3ssie/osmedeus@latest
osmedeus health

# ===== BASIC =====
# Full scan domain
osmedeus scan -t target.com

# ===== WORKFLOWS =====
# List available workflows
osmedeus scan --wflist

# Specific workflow
osmedeus scan -f general -t target.com      # General recon
osmedeus scan -f subdomain -t target.com    # Subdomain only
osmedeus scan -f vuln -t target.com         # Vulnerability scan
osmedeus scan -f urls -t target.com         # URL gathering

# ===== MULTIPLE TARGETS =====
osmedeus scan -T targets.txt

# ===== OPTIONS =====
# Concurrency
osmedeus scan -t target.com -c 10

# Resume scan
osmedeus scan -t target.com --resume

# Custom output
osmedeus scan -t target.com -o /path/to/output

# Params
osmedeus scan -t target.com -p "wordlists=/path/to/wordlist.txt"

# ===== CLOUD =====
osmedeus cloud -t target.com --token YOUR_TOKEN

# ===== WEB UI =====
osmedeus server
# Access: http://127.0.0.1:8000
```

---

## 🧰 Sn1per
**Deskripsi**: Automated pentest recon scanner. Full reconnaissance + vulnerability assessment.

```bash
# Install
git clone https://github.com/1N3/Sn1per.git
cd Sn1per
./install.sh

# ===== SCAN MODES =====
# Normal (non-invasive)
sniper -t target.com

# OSINT (passive only)
sniper -t target.com -o -re

# Stealth (rate-limited)
sniper -t target.com -m stealth -o -re

# Discover (scan semua hosts in subnet)
sniper -t 192.168.1.0/24 -m discover

# Port scan
sniper -t target.com -m port -p 80,443,8080

# Fullportonly
sniper -t target.com -m fullportonly

# Web mode
sniper -t target.com -m web

# Brute force
sniper -t target.com -m bruteforce

# Vulnerability scan
sniper -t target.com -m vulnscan

# ===== OPTIONS =====
# Workspace
sniper -t target.com -w workspace_name

# Output
sniper -t target.com -o

# Re-run
sniper -t target.com -re

# Delete workspace
sniper -t target.com --delete

# ===== REPORT =====
# Lihat report
sniper --report target.com

# Web UI
sniper --status
# http://127.0.0.1:1337

# ===== MODULES =====
# Subdomain enum, port scanning, web crawling
# Directory brute force, vulnerability scanning
# OSINT, email harvesting, screenshot
# Brute force (SSH, FTP, SMTP, etc.)
# Exploit suggestion
```

---

# 🚀 Quick Reference: Recon Workflow Pipeline

```bash
# ============================================================
# COMPLETE AUTOMATED RECON PIPELINE (One-liner style)
# ============================================================

# 1. SUBDOMAIN ENUMERATION
subfinder -d target.com -silent -o subs_subfinder.txt
amass enum -passive -d target.com -o subs_amass.txt
findomain -t target.com -u subs_findomain.txt
assetfinder --subs-only target.com > subs_assetfinder.txt
cat subs_*.txt | sort -u > all_subdomains.txt

# 2. DNS RESOLUTION & PROBE
cat all_subdomains.txt | httpx -silent -status-code -title -tech-detect -o live_hosts.txt

# 3. PORT SCANNING
sudo naabu -list all_subdomains.txt -top-ports 1000 -silent -o open_ports.txt

# 4. SCREENSHOTS
cat live_hosts.txt | aquatone -out screenshots/

# 5. CONTENT DISCOVERY
ffuf -u https://target.com/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc 200,301,302,403 -o dirs.json -of json

# 6. URL GATHERING
echo "target.com" | gau --blacklist png,jpg,gif,css,woff,svg --threads 5 > gau_urls.txt
echo "target.com" | waybackurls > wayback_urls.txt
cat gau_urls.txt wayback_urls.txt | sort -u > all_urls.txt

# 7. PARAMETER EXTRACTION
cat all_urls.txt | gf xss > xss_params.txt
cat all_urls.txt | gf sqli > sqli_params.txt
cat all_urls.txt | gf ssrf > ssrf_params.txt
cat all_urls.txt | gf lfi > lfi_params.txt

# 8. VULNERABILITY SCANNING
nuclei -l live_hosts.txt -s critical,high -o nuclei_results.txt

# ============================================================
# ATAU gunakan all-in-one:
# reconftw -d target.com -a
# ============================================================
```

---

> ⚠️ **DISCLAIMER**: Cheatsheet ini hanya untuk tujuan pendidikan dan ethical hacking/penetration testing yang sudah mendapatkan izin tertulis. Penggunaan tools ini tanpa izin merupakan pelanggaran hukum.
