# 🔎 RECON & OSINT FULL CHEATSHEET — Part 1

## 📑 Table of Contents (Part 1)
1. [Domain & DNS Intelligence](#1-domain--dns-intelligence)
2. [Subdomain Enumeration](#2-subdomain-enumeration)
3. [OSINT & Metadata](#3-osint--metadata)

---

# 1. Domain & DNS Intelligence

## 🌐 DNSDumpster
**Deskripsi**: Passive DNS recon tool berbasis web. Menampilkan DNS records, subdomains, dan host mapping.

```bash
# Web-based: https://dnsdumpster.com
# API via Python
pip install dnsdumpster
python -c "from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI; res = DNSDumpsterAPI().search('target.com'); print(res)"
```

**Tips**:
- Gratis, tanpa registrasi
- Export hasil ke XLS/PNG
- Cocok untuk quick recon awal

---

## 🌐 crt.sh (Certificate Transparency)
**Deskripsi**: Database publik SSL/TLS certificate. Sangat berguna untuk menemukan subdomain via certificate logs.

```bash
# Browser
https://crt.sh/?q=%25.target.com

# CLI dengan curl + jq
curl -s "https://crt.sh/?q=%25.target.com&output=json" | jq -r '.[].name_value' | sort -u

# Filter wildcard & deduplicate
curl -s "https://crt.sh/?q=%25.target.com&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u

# Simpan ke file
curl -s "https://crt.sh/?q=%25.target.com&output=json" | jq -r '.[].name_value' | sort -u > subdomains_crt.txt
```

---

## 🌐 SecurityTrails
**Deskripsi**: Platform DNS & domain intelligence dengan historical data, subdomain enumeration, dan WHOIS lookup.

```bash
# API Key required (free tier available)
# Subdomain list
curl -s "https://api.securitytrails.com/v1/domain/target.com/subdomains" \
  -H "APIKEY: YOUR_API_KEY" | jq -r '.subdomains[]' | sed 's/$/.target.com/'

# DNS History
curl -s "https://api.securitytrails.com/v1/history/target.com/dns/a" \
  -H "APIKEY: YOUR_API_KEY" | jq

# WHOIS
curl -s "https://api.securitytrails.com/v1/domain/target.com/whois" \
  -H "APIKEY: YOUR_API_KEY" | jq

# Associated domains (by email/org)
curl -s "https://api.securitytrails.com/v1/domain/target.com/associated" \
  -H "APIKEY: YOUR_API_KEY" | jq
```

---

## 🌐 Whois / WhoIsLookup
**Deskripsi**: Query WHOIS database untuk informasi registrant, registrar, nameserver, dan tanggal expiry domain.

```bash
# Basic WHOIS
whois target.com

# Spesifik server
whois -h whois.verisign-grs.com target.com

# Grep info penting
whois target.com | grep -iE "registrant|admin|tech|name server|creation|expir"

# IP WHOIS
whois 1.2.3.4

# Bulk WHOIS (script)
while read domain; do echo "=== $domain ===" && whois $domain | grep -i "registrant"; done < domains.txt
```

**Online Alternatives**:
- https://who.is
- https://whois.domaintools.com
- https://lookup.icann.org

---

## 🌐 ViewDNS
**Deskripsi**: Suite tools DNS: reverse IP, port scanner, DNS propagation, IP history, dll.

```bash
# Reverse IP (domain yang sharing IP)
curl -s "https://api.viewdns.info/reverseip/?host=target.com&apikey=YOUR_KEY&output=json" | jq

# IP History
curl -s "https://api.viewdns.info/iphistory/?domain=target.com&apikey=YOUR_KEY&output=json" | jq

# DNS Record Lookup
curl -s "https://api.viewdns.info/dnsrecord/?domain=target.com&apikey=YOUR_KEY&output=json" | jq

# Reverse Whois
curl -s "https://api.viewdns.info/reversewhois/?q=admin@target.com&apikey=YOUR_KEY&output=json" | jq
```

**Web Interface**: https://viewdns.info

---

## 🌐 DNSRecon
**Deskripsi**: Tool DNS enumeration lengkap. Mendukung zone transfer, brute force, reverse lookup, Google dork, dan SRV enumeration.

```bash
# Install
pip install dnsrecon
# atau
sudo apt install dnsrecon

# Standard enumeration (semua record types)
dnsrecon -d target.com

# Zone transfer attempt
dnsrecon -d target.com -t axfr

# Brute force subdomains
dnsrecon -d target.com -t brt -D /usr/share/wordlists/subdomains-top1million-5000.txt

# Reverse lookup range
dnsrecon -r 192.168.1.0/24

# Google dork enumeration
dnsrecon -d target.com -t goo

# SRV record enumeration
dnsrecon -d target.com -t srv

# Cache snooping
dnsrecon -d target.com -t snoop -n 8.8.8.8

# Output ke file (XML/JSON/CSV)
dnsrecon -d target.com -j output.json
dnsrecon -d target.com --xml output.xml
dnsrecon -d target.com -c output.csv

# Full scan (semua teknik)
dnsrecon -d target.com -a -s -g -w -z
```

---

## 🌐 DNSenum
**Deskripsi**: DNS enumeration tool yang melakukan host discovery, zone transfer attempt, brute force, Google scraping, dan reverse lookup.

```bash
# Install
sudo apt install dnsenum

# Basic enumeration
dnsenum target.com

# Brute force dengan wordlist
dnsenum --enum -f /usr/share/wordlists/dns/subdomains-top1million-5000.txt target.com

# Dengan thread dan halaman Google
dnsenum --threads 5 -p 5 target.com

# Tanpa reverse lookup (lebih cepat)
dnsenum --noreverse target.com

# Simpan output
dnsenum target.com -o output.xml

# Private range reverse
dnsenum -r target.com

# Recursive subdomain brute
dnsenum -s 20 --threads 10 -f subdomains.txt target.com
```

---

## 🌐 Fierce
**Deskripsi**: DNS reconnaissance tool fokus pada menemukan non-contiguous IP space dan hostnames terhadap suatu domain.

```bash
# Install
pip install fierce

# Basic scan
fierce --domain target.com

# Custom DNS server
fierce --domain target.com --dns-servers 8.8.8.8

# Custom wordlist
fierce --domain target.com --subdomain-file /path/to/wordlist.txt

# Output ke file
fierce --domain target.com > fierce_output.txt

# Traverse nearby IPs (range)
fierce --domain target.com --traverse 10

# Delay antar query
fierce --domain target.com --delay 1
```

---

## 🌐 Sublist3r
**Deskripsi**: Tool enumerasi subdomain menggunakan banyak search engine (Google, Yahoo, Bing, Baidu, Virustotal, dll).

```bash
# Install
git clone https://github.com/aboul3la/Sublist3r.git
cd Sublist3r
pip install -r requirements.txt

# Basic enumeration
python sublist3r.py -d target.com

# Dengan port scanning
python sublist3r.py -d target.com -p 80,443,8080

# Jumlah threads
python sublist3r.py -d target.com -t 50

# Output ke file
python sublist3r.py -d target.com -o subdomains.txt

# Spesifik search engine
python sublist3r.py -d target.com -e google,virustotal,crtsh

# Verbose mode
python sublist3r.py -d target.com -v
```

---

# 2. Subdomain Enumeration

## 🌍 Subfinder
**Deskripsi**: Fast passive subdomain enumeration tool dari ProjectDiscovery. Menggunakan banyak sources (Censys, Shodan, VirusTotal, dll).

```bash
# Install
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Basic
subfinder -d target.com

# Output ke file
subfinder -d target.com -o subdomains.txt

# Silent mode (hanya subdomain)
subfinder -d target.com -silent

# Recursive enumeration
subfinder -d target.com -recursive

# Multiple domains
subfinder -dL domains.txt -o all_subdomains.txt

# Dengan specific sources
subfinder -d target.com -sources virustotal,crtsh,shodan

# JSON output
subfinder -d target.com -json -o subdomains.json

# Exclude sources
subfinder -d target.com -es github

# All sources (verbose)
subfinder -d target.com -all -v

# Config file: ~/.config/subfinder/provider-config.yaml
# Tambahkan API keys di config untuk hasil lebih banyak
```

---

## 🌍 Amass
**Deskripsi**: OWASP project untuk network mapping. Sangat powerful untuk subdomain enumeration, ASN discovery, dan infrastructure mapping.

```bash
# Install
go install -v github.com/owasp-amass/amass/v4/...@master
# atau
sudo apt install amass

# ===== AMASS INTEL (Reconnaissance) =====
# Discover root domains dari ASN
amass intel -asn 12345

# Discover dari CIDR
amass intel -cidr 192.168.0.0/16

# Reverse whois
amass intel -whois -d target.com

# Discover ASN dari domain
amass intel -org "Target Corp"

# ===== AMASS ENUM (Enumeration) =====
# Passive enumeration
amass enum -passive -d target.com -o passive_subs.txt

# Active enumeration (DNS resolution + brute force)
amass enum -active -d target.com -o active_subs.txt

# Brute force
amass enum -brute -d target.com -w wordlist.txt

# Full aggressive scan
amass enum -active -brute -d target.com -src -ip -o full_enum.txt

# Multiple domains
amass enum -d target1.com,target2.com

# Dengan config file
amass enum -d target.com -config config.yaml

# Output formats
amass enum -d target.com -json output.json
amass enum -d target.com -dir ./amass_output

# ===== AMASS DB (Database) =====
amass db -names -d target.com
amass db -summary -d target.com
```

---

## 🌍 Findomain
**Deskripsi**: Cross-platform subdomain finder. Sangat cepat, ditulis dalam Rust.

```bash
# Install
curl -LO https://github.com/Findomain/Findomain/releases/latest/download/findomain-linux.zip
unzip findomain-linux.zip && chmod +x findomain && sudo mv findomain /usr/local/bin/

# Basic
findomain -t target.com

# Output ke file
findomain -t target.com -u subdomains.txt

# Resolve IPs
findomain -t target.com -r

# Multiple targets
findomain -f domains.txt -u all_subs.txt

# Dengan monitoring (alert new subdomains)
findomain -t target.com --monitoring-flag

# JSON output
findomain -t target.com --json

# Quiet mode
findomain -t target.com -q
```

---

## 🌍 Assetfinder
**Deskripsi**: Tool ringan untuk menemukan domain dan subdomain terkait suatu domain.

```bash
# Install
go install github.com/tomnomnom/assetfinder@latest

# Basic (termasuk related domains)
assetfinder target.com

# Hanya subdomains
assetfinder --subs-only target.com

# Pipeline
assetfinder --subs-only target.com | sort -u > subs.txt

# Combine dengan tools lain
assetfinder --subs-only target.com | httpx -silent -title -status-code
```

---

## 🌍 Chaos (ProjectDiscovery)
**Deskripsi**: ProjectDiscovery's Chaos dataset. Menyediakan DNS data untuk bug bounty programs.

```bash
# Install
go install -v github.com/projectdiscovery/chaos-client/cmd/chaos@latest

# Set API key
export PDCP_API_KEY=YOUR_KEY

# Get subdomains
chaos -d target.com

# Output ke file
chaos -d target.com -o chaos_subs.txt

# Silent mode
chaos -d target.com -silent

# JSON output
chaos -d target.com -json

# Hanya count
chaos -d target.com -count
```

---

## 🌍 Knockpy
**Deskripsi**: Python-based subdomain scanner. Menggunakan wordlist + VirusTotal untuk enumeration.

```bash
# Install
pip install knockpy

# Basic scan
knockpy target.com

# Custom wordlist
knockpy target.com -w /path/to/wordlist.txt

# DNS resolver
knockpy target.com --dns 8.8.8.8

# Save report
knockpy target.com --save report.json

# No VirusTotal
knockpy target.com --no-virustotal
```

---

## 🌍 Subjack (Subdomain Takeover Check)
**Deskripsi**: Tool untuk mengecek apakah subdomain rentan terhadap subdomain takeover.

```bash
# Install
go install github.com/haccer/subjack@latest

# Basic check
subjack -w subdomains.txt -t 100 -timeout 30 -ssl -c ~/go/src/github.com/haccer/subjack/fingerprints.json -v

# Output ke file
subjack -w subdomains.txt -o takeover_results.txt

# Dengan concurrency
subjack -w subdomains.txt -t 200 -timeout 30 -ssl -c fingerprints.json

# Manual check (CNAME)
dig CNAME subdomain.target.com
# Jika CNAME → service yang sudah tidak aktif = VULNERABLE
```

**Service yang sering vulnerable**:
- GitHub Pages, Heroku, AWS S3, Shopify, Tumblr, WordPress.com, Zendesk, Fastly

---

## 🌍 GitHub Subdomains
**Deskripsi**: Mencari subdomain yang ter-expose di GitHub repositories & code.

```bash
# github-subdomains tool
go install github.com/gwen001/github-subdomains@latest

# Basic (butuh GitHub token)
github-subdomains -d target.com -t ghp_YOUR_TOKEN

# Output
github-subdomains -d target.com -t ghp_YOUR_TOKEN -o github_subs.txt

# Manual GitHub Dork
# Di browser: site:github.com "target.com"
# Atau: "target.com" extension:env
# Atau: "target.com" password OR secret OR api_key
```

---

# 3. OSINT & Metadata

## 🧠 theHarvester
**Deskripsi**: Tool OSINT untuk gathering email, subdomain, host, employee names, open ports, dan banners dari sumber publik.

```bash
# Install
sudo apt install theharvester
# atau
pip install theHarvester

# Basic email & subdomain
theHarvester -d target.com -b all

# Spesifik source
theHarvester -d target.com -b google,bing,linkedin,crtsh,virustotal

# Limit results
theHarvester -d target.com -b google -l 500

# DNS brute force
theHarvester -d target.com -b all -c

# Output ke file
theHarvester -d target.com -b all -f output.html

# Virtual hosts
theHarvester -d target.com -b all -v

# DNS TLD expansion
theHarvester -d target -b all -t

# Shodan integration
theHarvester -d target.com -b shodan -s

# Full recon
theHarvester -d target.com -b all -l 1000 -f full_harvest
```

**Sources tersedia**: baidu, bing, bingapi, certspotter, crtsh, dnsdumpster, duckduckgo, github-code, google, hackertarget, hunter, linkedin, netcraft, otx, rapiddns, securityTrails, shodan, sublist3r, threatcrowd, trello, twitter, urlscan, virustotal, yahoo

---

## 🧠 Maltego
**Deskripsi**: GUI-based OSINT & graphical link analysis tool. Visualisasi relasi antara entities (people, companies, domains, IP, dll).

```
# Maltego adalah GUI application
# Download: https://www.maltego.com/downloads/

# Transforms yang berguna:
- Domain → DNS Names
- Domain → Email Addresses
- Email → Person
- Person → Phone Numbers
- IP → Geolocation
- Domain → Technologies
- Company → People (LinkedIn)

# Workflow:
1. New Graph → Drag entity (Domain) ke canvas
2. Masukkan target.com
3. Klik kanan → Run Transform → All Transforms
4. Explore relationships
5. Export graph
```

**Editions**:
- Maltego CE (Community Edition) - Free, limited transforms
- Maltego Classic - Paid, full transforms
- Maltego XL - Enterprise

---

## 🧠 SpiderFoot
**Deskripsi**: Automated OSINT framework. Scan dari domain/IP/email/name → mengumpulkan data dari 100+ sources.

```bash
# Install
pip install spiderfoot
# atau
git clone https://github.com/smicallef/spiderfoot.git
cd spiderfoot
pip install -r requirements.txt

# Web UI mode
python sf.py -l 127.0.0.1:5001
# Buka http://127.0.0.1:5001

# CLI scan
python sf.py -s target.com -t DOMAIN -m sfp_dns,sfp_whois -q

# Semua modules
python sf.py -s target.com -t DOMAIN -m all

# Scan email
python sf.py -s admin@target.com -t EMAIL_ADDRESS

# Scan IP
python sf.py -s 1.2.3.4 -t IP_ADDRESS

# Output format
python sf.py -s target.com -t DOMAIN -o csv -q > output.csv
python sf.py -s target.com -t DOMAIN -o json -q > output.json

# SpiderFoot HX (cloud version): https://hx.spiderfoot.net
```

---

## 🧠 Recon-ng
**Deskripsi**: Full-featured web reconnaissance framework. Modular design mirip Metasploit.

```bash
# Install
sudo apt install recon-ng
# atau
git clone https://github.com/lanmaster53/recon-ng.git
cd recon-ng
pip install -r REQUIREMENTS

# Jalankan
recon-ng

# ===== WORKSPACE =====
workspaces create target_recon
workspaces load target_recon

# ===== MARKETPLACE (Install modules) =====
marketplace search
marketplace search subdomain
marketplace install recon/domains-hosts/hackertarget
marketplace install recon/domains-hosts/certificate_transparency
marketplace install recon/domains-contacts/whois_pocs
marketplace install recon/hosts-hosts/resolve

# ===== SET TARGET =====
db insert domains
# masukkan: target.com

# ===== RUN MODULES =====
modules load recon/domains-hosts/hackertarget
options set SOURCE target.com
run

modules load recon/domains-hosts/certificate_transparency
run

# ===== VIEW RESULTS =====
show hosts
show contacts
show credentials

# ===== API KEYS =====
keys list
keys add shodan_api YOUR_KEY
keys add virustotal_api YOUR_KEY
keys add github_api YOUR_KEY

# ===== REPORTING =====
modules load reporting/html
options set FILENAME /path/to/report.html
run

modules load reporting/csv
options set FILENAME /path/to/report.csv
run
```

---

## 🧠 FOCA
**Deskripsi**: Windows-based tool untuk metadata extraction dari dokumen publik (PDF, DOC, XLS, PPT, dll). Mengungkap usernames, software versions, email, paths, dll.

```
# FOCA adalah Windows GUI application
# Download: https://github.com/ElevenPaths/FOCA

# Workflow:
1. New Project → set target domain
2. Network Discovery → DNS, WHOIS
3. Search engines → find documents (PDF, DOCX, XLSX, PPTX)
4. Download documents
5. Extract metadata:
   - Usernames & email addresses
   - Software versions
   - OS information
   - Printer names
   - Directory paths
   - Hidden comments
6. Analyze → Map internal network structure

# Alternatif CLI (ExifTool):
# Extract metadata dari file
exiftool document.pdf
exiftool -r -ext pdf /path/to/docs/

# Bulk extract
find . -name "*.pdf" -exec exiftool {} \; > metadata.txt

# Specific fields
exiftool -Author -Creator -Producer -ModifyDate document.pdf
```

---

> **Pro Tip**: Kombinasikan multiple tools untuk hasil maksimal:
> ```bash
> # Pipeline recon workflow
> subfinder -d target.com -silent | \
>   httpx -silent -status-code -title | \
>   tee live_subdomains.txt
> ```
