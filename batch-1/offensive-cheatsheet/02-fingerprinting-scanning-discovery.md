# 🔎 RECON & OSINT FULL CHEATSHEET — Part 2

## 📑 Table of Contents (Part 2)
4. [Web Fingerprinting & Tech Detection](#4-web-fingerprinting--tech-detection)
5. [Port Scanning & Network Discovery](#5-port-scanning--network-discovery)
6. [Directory & File Discovery](#6-directory--file-discovery)

---

# 4. Web Fingerprinting & Tech Detection

## 🕸️ WhatWeb
**Deskripsi**: Web scanner untuk identifikasi teknologi website: CMS, framework, server, JS libraries, dll.

```bash
# Install
sudo apt install whatweb

# Basic scan
whatweb target.com

# Aggressive mode (level 1-4)
whatweb -a 3 target.com

# Verbose
whatweb -v target.com

# Multiple targets
whatweb target1.com target2.com target3.com

# Dari file
whatweb -i urls.txt

# Output format
whatweb target.com --log-json=output.json
whatweb target.com --log-xml=output.xml
whatweb target.com --log-csv=output.csv

# Custom User-Agent
whatweb -U "Custom Agent" target.com

# Follow redirects
whatweb --follow-redirect=always target.com

# Plugin list
whatweb --list-plugins

# Scan entire subnet
whatweb 192.168.1.0/24

# Spesifik plugin
whatweb --plugins=Apache,PHP,WordPress target.com

# Proxy
whatweb --proxy http://127.0.0.1:8080 target.com
```

---

## 🕸️ Wappalyzer
**Deskripsi**: Browser extension & CLI tool untuk detect teknologi web (CMS, ecommerce, CDN, analytics, dll).

```bash
# CLI version (wappalyzer-cli)
npm install -g wappalyzer

# Basic scan
wappalyzer https://target.com

# JSON output
wappalyzer https://target.com --pretty

# Batch scan
cat urls.txt | while read url; do echo "=== $url ===" && wappalyzer "$url"; done

# Browser extension:
# Chrome: https://chrome.google.com/webstore/detail/wappalyzer
# Firefox: https://addons.mozilla.org/en-US/firefox/addon/wappalyzer/
```

**Detectable Categories**: CMS, JavaScript frameworks, Analytics, CDN, Server, Caching, Marketing, Payment processors, Security, Widgets, dll.

---

## 🕸️ BuiltWith
**Deskripsi**: Web-based technology profiler. Menunjukkan semua teknologi yang digunakan website.

```bash
# Web-based: https://builtwith.com
# Masukkan URL → lihat full tech stack

# API (paid)
curl "https://api.builtwith.com/free1/api.json?KEY=YOUR_KEY&LOOKUP=target.com" | jq

# Informasi yang didapat:
# - Web server (Nginx, Apache, IIS)
# - CMS (WordPress, Drupal, Joomla)
# - JavaScript frameworks
# - Analytics (Google Analytics, Hotjar)
# - CDN (Cloudflare, Akamai)
# - SSL Certificate provider
# - Email services
# - Advertising networks
# - Payment processors
```

---

## 🕸️ HTTPX (ProjectDiscovery)
**Deskripsi**: Fast HTTP toolkit. Probe URLs, detect technologies, status codes, titles, dan banyak lagi.

```bash
# Install
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest

# Basic probe (check alive)
cat subdomains.txt | httpx -silent

# Dengan status code & title
cat subdomains.txt | httpx -status-code -title -tech-detect

# Full recon
cat subdomains.txt | httpx -status-code -title -tech-detect -content-length -web-server -ip -cname -cdn

# Follow redirects
cat subdomains.txt | httpx -follow-redirects -status-code

# Screenshot
cat subdomains.txt | httpx -screenshot -system-chrome

# Filter by status code
cat subdomains.txt | httpx -mc 200,301,302,403

# JSON output
cat subdomains.txt | httpx -json -o results.json

# Custom ports
cat subdomains.txt | httpx -ports 80,443,8080,8443

# Content-type filter
cat subdomains.txt | httpx -content-type -match-string "text/html"

# Favicon hash (technology detection)
cat subdomains.txt | httpx -favicon

# Pipeline with subfinder
subfinder -d target.com -silent | httpx -silent -title -status-code -tech-detect
```

---

## 🕸️ Webanalyze
**Deskripsi**: Port of Wappalyzer untuk CLI. Menggunakan Wappalyzer fingerprints.

```bash
# Install
go install github.com/rverton/webanalyze/cmd/webanalyze@latest

# Update fingerprints
webanalyze -update

# Basic scan
webanalyze -host target.com

# Multiple hosts
webanalyze -hosts urls.txt

# Workers
webanalyze -hosts urls.txt -worker 10

# Output CSV
webanalyze -host target.com -output csv
```

---

## 🕸️ Nmap (Service Detection)
**Deskripsi**: Network scanner. Untuk fingerprinting: version detection, OS detection, dan NSE scripts.

```bash
# Service version detection
nmap -sV target.com

# Aggressive scan (OS + version + script + traceroute)
nmap -A target.com

# OS detection
nmap -O target.com

# NSE scripts untuk web
nmap --script=http-headers,http-title,http-server-header target.com -p 80,443

# HTTP enum
nmap --script=http-enum target.com -p 80,443

# SSL/TLS info
nmap --script=ssl-enum-ciphers,ssl-cert target.com -p 443

# WAF detection
nmap --script=http-waf-detect,http-waf-fingerprint target.com -p 80,443

# Technologies detect
nmap --script=http-generator target.com -p 80,443

# Full web fingerprint
nmap -sV --script=http-headers,http-title,http-server-header,http-enum,http-robots.txt target.com -p 80,443,8080,8443
```

---

# 5. Port Scanning & Network Discovery

## 📡 Nmap (Full Reference)
**Deskripsi**: The king of port scanners. Network discovery, port scanning, version detection, OS fingerprinting.

```bash
# ===== SCAN TYPES =====
nmap -sS target.com          # TCP SYN (stealth/half-open)
nmap -sT target.com          # TCP Connect
nmap -sU target.com          # UDP scan
nmap -sA target.com          # ACK scan (firewall detection)
nmap -sW target.com          # Window scan
nmap -sN target.com          # NULL scan
nmap -sF target.com          # FIN scan
nmap -sX target.com          # Xmas scan

# ===== PORT SPECIFICATION =====
nmap -p 80 target.com             # Single port
nmap -p 80,443,8080 target.com    # Multiple ports
nmap -p 1-1000 target.com         # Port range
nmap -p- target.com               # ALL 65535 ports
nmap --top-ports 100 target.com   # Top 100 common ports
nmap -p U:53,T:80,443 target.com  # UDP + TCP

# ===== HOST DISCOVERY =====
nmap -sn 192.168.1.0/24      # Ping sweep (no port scan)
nmap -Pn target.com           # Skip host discovery
nmap -PS22,80,443 target.com  # TCP SYN discovery
nmap -PA80,443 target.com     # TCP ACK discovery
nmap -PU53 target.com         # UDP discovery
nmap -sL 192.168.1.0/24      # List scan (DNS only)

# ===== TIMING =====
nmap -T0 target.com    # Paranoid (IDS evasion)
nmap -T1 target.com    # Sneaky
nmap -T2 target.com    # Polite
nmap -T3 target.com    # Normal (default)
nmap -T4 target.com    # Aggressive
nmap -T5 target.com    # Insane

# ===== OUTPUT =====
nmap -oN output.txt target.com     # Normal
nmap -oX output.xml target.com     # XML
nmap -oG output.gnmap target.com   # Grepable
nmap -oA output_all target.com     # All formats
nmap -oS output.txt target.com     # Script kiddie (lol)

# ===== EVASION =====
nmap -f target.com                  # Fragment packets
nmap -D RND:10 target.com          # Decoy scan
nmap --source-port 53 target.com   # Source port spoof
nmap --data-length 200 target.com  # Append random data
nmap -S 1.2.3.4 target.com        # Spoof source IP
nmap --proxies http://proxy:8080 target.com

# ===== NSE SCRIPTS =====
nmap --script=default target.com
nmap --script=vuln target.com
nmap --script=safe target.com
nmap --script=exploit target.com
nmap --script="http-*" target.com
nmap --script-updatedb

# ===== COMMON COMBOS =====
# Quick scan
nmap -sV -sC -O -T4 target.com

# Full TCP
nmap -sS -sV -sC -O -A -p- -T4 target.com -oA full_scan

# Quick UDP
nmap -sU --top-ports 20 target.com

# Vulnerability scan
nmap --script vuln -sV target.com

# Firewall evasion
nmap -sS -T2 -f --data-length 200 -D RND:5 target.com
```

---

## 📡 Masscan
**Deskripsi**: Internet-scale port scanner. Sangat cepat (bisa scan seluruh internet dalam 5 menit).

```bash
# Install
sudo apt install masscan

# Basic scan
sudo masscan -p80,443 192.168.1.0/24

# All ports
sudo masscan -p0-65535 target.com --rate 1000

# Common web ports
sudo masscan -p80,443,8080,8443 192.168.1.0/24 --rate 10000

# Output formats
sudo masscan -p80 192.168.1.0/24 -oL output.txt     # List
sudo masscan -p80 192.168.1.0/24 -oJ output.json     # JSON
sudo masscan -p80 192.168.1.0/24 -oX output.xml       # XML
sudo masscan -p80 192.168.1.0/24 -oG output.gnmap     # Grepable

# Banner grabbing
sudo masscan -p80,443 192.168.1.0/24 --banners

# Rate control
sudo masscan -p80 0.0.0.0/0 --rate 100000 --excludefile exclude.txt

# Exclude file
sudo masscan -p80 10.0.0.0/8 --excludefile exclude.txt

# Pipeline: masscan → nmap
sudo masscan -p- target.com --rate 1000 -oL masscan_output.txt
# Parse dan scan dengan nmap untuk detail
```

---

## 📡 RustScan
**Deskripsi**: Modern port scanner ditulis Rust. Sangat cepat, otomatis pipe ke Nmap.

```bash
# Install
cargo install rustscan
# atau Docker
docker pull rustscan/rustscan

# Basic (auto pipes to nmap)
rustscan -a target.com

# Spesifik ports
rustscan -a target.com -p 80,443,8080

# Port range
rustscan -a target.com -r 1-65535

# Batch size (speed control)
rustscan -a target.com -b 500

# Timeout
rustscan -a target.com -t 1500

# Multiple targets
rustscan -a target1.com,target2.com

# Custom nmap arguments
rustscan -a target.com -- -sV -sC -A

# Docker
docker run -it --rm rustscan/rustscan -a target.com -- -sV -sC
```

---

## 📡 Naabu (ProjectDiscovery)
**Deskripsi**: Fast port scanner dari ProjectDiscovery. Designed untuk speed dan integration.

```bash
# Install
go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest

# Basic scan
naabu -host target.com

# All ports
naabu -host target.com -p -

# Common ports
naabu -host target.com -top-ports 100

# Specific ports
naabu -host target.com -p 80,443,8080

# From file
naabu -list hosts.txt

# SYN scan (requires root)
sudo naabu -host target.com -s s

# JSON output
naabu -host target.com -json -o results.json

# Rate limit
naabu -host target.com -rate 1000

# Pipeline
subfinder -d target.com -silent | naabu -silent | httpx -silent

# Exclude CDN
naabu -host target.com -exclude-cdn

# Nmap integration
naabu -host target.com -nmap-cli "nmap -sV -sC"
```

---

## 📡 Zmap
**Deskripsi**: Single-packet network scanner. Designed untuk internet-wide scans.

```bash
# Install
sudo apt install zmap

# Basic (scan port 80 pada subnet)
sudo zmap -p 80 192.168.0.0/16 -o results.txt

# Multiple ports (harus jalankan terpisah)
sudo zmap -p 443 192.168.0.0/16 -o results_443.txt

# Rate limit
sudo zmap -p 80 10.0.0.0/8 -r 10000 -o results.txt

# Blacklist
sudo zmap -p 80 0.0.0.0/0 -b blacklist.txt -o results.txt

# Banner grab (zgrab2)
sudo zmap -p 80 192.168.0.0/16 | zgrab2 http -o http_results.json
sudo zmap -p 443 192.168.0.0/16 | zgrab2 tls -o tls_results.json

# Output fields
sudo zmap -p 80 192.168.0.0/16 -f "saddr,sport" -o results.csv

# Interface
sudo zmap -p 80 192.168.0.0/16 -i eth0
```

---

# 6. Directory & File Discovery (Content Discovery)

## 📂 ffuf (Fuzz Faster U Fool)
**Deskripsi**: Fast web fuzzer. Directory brute force, vhost discovery, parameter fuzzing.

```bash
# Install
go install github.com/ffuf/ffuf/v2@latest

# ===== DIRECTORY BRUTE FORCE =====
ffuf -u https://target.com/FUZZ -w /usr/share/wordlists/dirb/common.txt

# Dengan extensions
ffuf -u https://target.com/FUZZ -w wordlist.txt -e .php,.html,.js,.txt,.bak

# Filter by status code
ffuf -u https://target.com/FUZZ -w wordlist.txt -mc 200,301,302,403

# Filter OUT status code
ffuf -u https://target.com/FUZZ -w wordlist.txt -fc 404

# Filter by response size
ffuf -u https://target.com/FUZZ -w wordlist.txt -fs 1234

# Filter by word count
ffuf -u https://target.com/FUZZ -w wordlist.txt -fw 42

# ===== VHOST DISCOVERY =====
ffuf -u https://target.com -w vhosts.txt -H "Host: FUZZ.target.com" -fs 1234

# ===== PARAMETER FUZZING (GET) =====
ffuf -u "https://target.com/page?FUZZ=value" -w params.txt -fs 1234

# ===== PARAMETER VALUE FUZZING =====
ffuf -u "https://target.com/page?id=FUZZ" -w numbers.txt

# ===== POST DATA FUZZING =====
ffuf -u https://target.com/login -X POST -d "user=FUZZ&pass=test" -w usernames.txt -fc 401

# ===== SUBDOMAIN FUZZING =====
ffuf -u https://FUZZ.target.com -w subdomains.txt -fs 1234

# ===== RECURSIVE =====
ffuf -u https://target.com/FUZZ -w wordlist.txt -recursion -recursion-depth 3

# ===== MULTI WORDLIST =====
ffuf -u https://target.com/FUZZ1/FUZZ2 -w wordlist1.txt:FUZZ1 -w wordlist2.txt:FUZZ2

# ===== OUTPUT =====
ffuf -u https://target.com/FUZZ -w wordlist.txt -o output.json -of json
ffuf -u https://target.com/FUZZ -w wordlist.txt -o output.csv -of csv
ffuf -u https://target.com/FUZZ -w wordlist.txt -o output.html -of html

# ===== SPEED & THREADS =====
ffuf -u https://target.com/FUZZ -w wordlist.txt -t 100 -rate 100

# ===== AUTH =====
ffuf -u https://target.com/FUZZ -w wordlist.txt -H "Authorization: Bearer TOKEN"
ffuf -u https://target.com/FUZZ -w wordlist.txt -H "Cookie: session=abc123"
```

---

## 📂 Gobuster
**Deskripsi**: Brute force tool untuk directories, DNS, vhosts, S3 buckets.

```bash
# Install
go install github.com/OJ/gobuster/v3@latest

# ===== DIR MODE =====
gobuster dir -u https://target.com -w /usr/share/wordlists/dirb/common.txt

# Dengan extensions
gobuster dir -u https://target.com -w wordlist.txt -x php,html,txt,js,bak

# Status codes
gobuster dir -u https://target.com -w wordlist.txt -s 200,301,302,403

# Threads
gobuster dir -u https://target.com -w wordlist.txt -t 50

# Follow redirects
gobuster dir -u https://target.com -w wordlist.txt -r

# Auth
gobuster dir -u https://target.com -w wordlist.txt -H "Authorization: Bearer TOKEN"
gobuster dir -u https://target.com -w wordlist.txt -c "session=abc123"

# Output
gobuster dir -u https://target.com -w wordlist.txt -o results.txt

# ===== DNS MODE =====
gobuster dns -d target.com -w subdomains.txt

# Dengan wildcard detection
gobuster dns -d target.com -w subdomains.txt --wildcard

# ===== VHOST MODE =====
gobuster vhost -u https://target.com -w vhosts.txt

# ===== S3 MODE =====
gobuster s3 -w bucket_names.txt

# ===== FUZZ MODE =====
gobuster fuzz -u https://target.com/FUZZ -w wordlist.txt
```

---

## 📂 Dirb
**Deskripsi**: Web content scanner. Brute force directories dan files berdasarkan wordlist.

```bash
# Install
sudo apt install dirb

# Basic scan
dirb https://target.com

# Custom wordlist
dirb https://target.com /usr/share/wordlists/dirb/big.txt

# Extensions
dirb https://target.com -X .php,.html,.txt

# Auth
dirb https://target.com -a "User-Agent-String"
dirb https://target.com -u admin:password

# Cookie
dirb https://target.com -c "PHPSESSID=abc123"

# Proxy
dirb https://target.com -p http://127.0.0.1:8080

# Non-recursive
dirb https://target.com -r

# Output
dirb https://target.com -o output.txt

# Ignore specific response codes
dirb https://target.com -N 404
```

---

## 📂 Dirsearch
**Deskripsi**: Advanced web path brute-forcer. Supports recursive scanning, multi-threading, proxy.

```bash
# Install
pip install dirsearch

# Basic
dirsearch -u https://target.com

# Extensions
dirsearch -u https://target.com -e php,html,js,txt

# Wordlist
dirsearch -u https://target.com -w /path/to/wordlist.txt

# Recursive
dirsearch -u https://target.com -r -R 3

# Threads
dirsearch -u https://target.com -t 50

# Exclude status codes
dirsearch -u https://target.com --exclude-status 404,403

# Output
dirsearch -u https://target.com -o results.txt --format json

# Multiple targets
dirsearch -l urls.txt -e php,html

# Proxy
dirsearch -u https://target.com --proxy http://127.0.0.1:8080

# Headers
dirsearch -u https://target.com -H "Authorization: Bearer TOKEN"

# Follow redirects
dirsearch -u https://target.com --follow-redirects

# Force extensions
dirsearch -u https://target.com -f -e php,html
```

---

## 📂 Wfuzz
**Deskripsi**: Web application fuzzer. Brute force parameters, directories, headers, dll.

```bash
# Install
pip install wfuzz

# Directory brute force
wfuzz -c -w wordlist.txt --hc 404 https://target.com/FUZZ

# Dengan extensions
wfuzz -c -w wordlist.txt -z list,-.php-.html-.txt --hc 404 https://target.com/FUZZFUZ2Z

# Hide responses by size
wfuzz -c -w wordlist.txt --hh 1234 https://target.com/FUZZ

# POST parameter
wfuzz -c -w wordlist.txt -d "user=FUZZ&pass=test" --hc 401 https://target.com/login

# Header fuzzing
wfuzz -c -w wordlist.txt -H "Host: FUZZ.target.com" --hh 1234 https://target.com

# Cookie
wfuzz -c -w wordlist.txt -b "session=abc123" --hc 404 https://target.com/FUZZ

# Auth
wfuzz -c -w wordlist.txt --basic admin:FUZZ --hc 401 https://target.com/admin

# Multiple payloads
wfuzz -c -w users.txt -w passwords.txt --hc 401 -d "user=FUZZ&pass=FUZ2Z" https://target.com/login

# Range payload
wfuzz -c -z range,1-100 --hc 404 https://target.com/page/FUZZ

# Output
wfuzz -c -w wordlist.txt --hc 404 -o json https://target.com/FUZZ > output.json
```

---

## 📂 Feroxbuster
**Deskripsi**: Fast recursive content discovery tool ditulis Rust. Support recursive scanning by default.

```bash
# Install
curl -sL https://raw.githubusercontent.com/epi052/feroxbuster/main/install-nix.sh | bash

# Basic (recursive by default)
feroxbuster -u https://target.com

# Wordlist
feroxbuster -u https://target.com -w /usr/share/wordlists/dirb/common.txt

# Extensions
feroxbuster -u https://target.com -x php,html,js,txt

# Threads
feroxbuster -u https://target.com -t 50

# Depth
feroxbuster -u https://target.com --depth 3

# Filter status codes
feroxbuster -u https://target.com -C 404,403

# Filter by size
feroxbuster -u https://target.com -S 1234

# Output
feroxbuster -u https://target.com -o results.txt --json

# Headers
feroxbuster -u https://target.com -H "Authorization: Bearer TOKEN"

# Rate limit
feroxbuster -u https://target.com --rate-limit 100

# Proxy
feroxbuster -u https://target.com --proxy http://127.0.0.1:8080

# Auto-tune
feroxbuster -u https://target.com --auto-tune

# Multiple targets
feroxbuster --stdin < urls.txt
```

---

## 📂 Burp Suite (Content Discovery)
**Deskripsi**: Fitur Content Discovery di Burp Suite Pro.

```
# Engagement Tools → Discover Content
1. Right-click target di Site map
2. Engagement tools → Discover content
3. Configure:
   - Built-in wordlist
   - Custom wordlist
   - File extensions
   - Recursion depth
4. Start

# Passive Discovery (Spider)
1. Target → Site map → klik kanan target
2. Spider this branch / Crawl this host
3. Review discovered content di Site map

# Intruder (Manual brute force)
1. Send request ke Intruder
2. Set payload position pada path
3. Load wordlist
4. Configure grep match rules
5. Start attack
```

---

> **Wordlists Recommended**:
> ```bash
> # SecLists (wajib punya)
> git clone https://github.com/danielmiessler/SecLists.git
>
> # Paths:
> # SecLists/Discovery/Web-Content/common.txt
> # SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
> # SecLists/Discovery/Web-Content/raft-large-files.txt
> # SecLists/Discovery/DNS/subdomains-top1million-5000.txt
> ```
