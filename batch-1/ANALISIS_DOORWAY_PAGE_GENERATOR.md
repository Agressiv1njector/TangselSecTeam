# 🔴 Analisis Malware: PHP Doorway Page Generator untuk SEO Spam

> **Tanggal Analisis:** 5 Februari 2026  
> **Analyst:** TangselSecTeam  
> **Threat Level:** HIGH  
> **Category:** SEO Spam / Doorway Pages / Government Domain Abuse
https://pastebin.com/raw/ECH1pWUs
---

## 📋 Executive Summary

Script PHP ini merupakan **doorway page generator** yang digunakan untuk membuat halaman spam SEO dalam skala besar. Script ini menyamar sebagai website resmi **Pemerintah Kota Tangerang Selatan** (layanan LASIK kesehatan mata) namun sebenarnya digunakan untuk mempromosikan situs **judi online/togel ilegal**.

### Key Findings:
- ✅ Abuse domain pemerintah `.go.id`
- ✅ Anti-detection mechanism terhadap Google Search Console
- ✅ Template hijacking dari Squarespace
- ✅ 21,134+ keyword variations
- ✅ Redirect ke situs judi online

---

## 🎯 Threat Overview

| Attribute | Value |
|-----------|-------|
| **Threat Type** | Doorway Page / SEO Spam |
| **Target** | Search Engine Rankings |
| **Disguise** | Layanan Kesehatan Pemerintah |
| **Actual Purpose** | Promosi Judi Online |
| **Scale** | 21,134+ halaman dinamis |

---

## 🔍 Technical Analysis

### 1. Anti-Detection Mechanism

```php
<?php 
// Mendapatkan referer HTTP
$referrer = isset($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : '';

// Domain yang ingin diblokir
$blocked_domain = 'https://search.google.com/search-console/remove-outdated-content?hl=en';
$blocked_domain = 'https://search.google.com/search-console/remove-outdated-content?hl=id';

// Mengecek apakah referer mengandung domain yang diblokir
if (strpos($referrer, $blocked_domain) !== false) {
    header('HTTP/1.0 403 Forbidden');
    echo 'Access is blocked from this referrer.';
    exit();
}
```

**Analisis:**
- Script memblokir akses dari **Google Search Console Removal Tool**
- Tujuan: Mencegah admin website melaporkan konten spam untuk dihapus dari index Google
- Menggunakan HTTP Referer checking

---

### 2. Dynamic Keyword System

```php
$tunnel = "app";
$filename = "pmz.txt";

if (isset($_GET[$tunnel])) {
    $lines = file($filename, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    $target_string = strtolower($_GET[$tunnel]);
    
    foreach ($lines as $value => $item) {
        if (strtolower($item) === $target_string) {
            $BRAND = strtolower($target_string);
            $NUMLIST = $value + 1;
        }
    }
}
```

**Analisis:**
- File `pmz.txt` berisi **21,134+ keyword** judi online
- Parameter `?app=` digunakan untuk memilih keyword
- Contoh: `domain.com/?app=slot88`, `domain.com/?app=togel4d`
- Setiap keyword menghasilkan halaman unik

---

### 3. URL Structure & Redirect Chain

```php
$URL = "https://lasik.tangerangselatankota.go.id/v2/svp/?app=".str_replace(" ","+",$BRAND);
$PAGEURL = "https://lasik.tangerangselatankota.go.id/v2/svp/?app=".str_replace(" ","+",$BRAND);
$AMP = "https://sdnbre.pages.dev/lasik/?s=".str_replace(" ","+",$BRAND);
$DAFTAR = "https://sdnbre.pages.dev/";
$BANNER = "https://jalurpintas.shop/meme/sdn-bnr3.webp";
$LOGO = "https://jalurpintas.shop/meme/sdn.png";
```

**URL Mapping:**

| Variable | URL | Purpose |
|----------|-----|---------|
| `$URL` | `lasik.tangerangselatankota.go.id` | Main doorway page |
| `$AMP` | `sdnbre.pages.dev` | AMP version / Landing |
| `$DAFTAR` | `sdnbre.pages.dev` | Registration redirect |
| `$BANNER` | `jalurpintas.shop` | Banner images |
| `$LOGO` | `jalurpintas.shop` | Logo assets |

---

### 4. SEO Manipulation Techniques

#### A. Meta Tags Poisoning
```php
$keyword = "$brand, login $brand, daftar $brand, situs $brand, rtp $brand, link alternatif $brand";

$TITLE = strtoupper($BRAND) . " - Layanan LASIK Gratis Resmi Pemkot Tangerang Selatan";
$DESCRIPTION = strtoupper($BRAND) . " merupakan platform layanan LASIK untuk masyarkat publik yang diresmikan oleh pemerintah setempat tangsel. Layanan ini gratis tidak dipungut biaya!";
```

#### B. Open Graph Tags
```html
<meta property="og:site_name" content="<?php echo $BRANDS ?>" />
<meta property="og:title" content="<?php echo $TITLE ?>" />
<meta property="og:url" content="<?php echo $URL ?>" />
<meta property="og:type" content="product" />
<meta property="og:description" content="<?php echo $DESCRIPTION ?>" />
<meta property="og:image" content="<?php echo $BANNER ?>" />
```

#### C. Structured Data (JSON-LD)
```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "<?php echo $BRANDS ?>",
    "operatingSystem": "ANDROID",
    "applicationCategory": "GameApplication",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "8899888"
    },
    "offers": {
        "@type": "Offer",
        "price": "0.00",
        "priceCurrency": "IDR"
    }
}
</script>
```

**Analisis:**
- Mengklaim sebagai aplikasi game dengan rating 5 bintang
- Review count palsu: 8,899,888
- Price: Free (menarik perhatian)

---

### 5. Template Hijacking

Script ini menggunakan **template Squarespace** yang di-copy secara utuh:

```javascript
Static.SQUARESPACE_CONTEXT = {
    "facebookAppId": "314192535267336",
    "website": {
        "id": "65fd0f981ec2594cc8fa0178",
        "identifier": "flamingo-elk-f2ll",
        "websiteType": 1,
        "siteTitle": "<?php echo $BRANDS ?>",
        ...
    },
    "authenticatedAccount": {
        "displayName": "<?php echo $BRANDS ?> togel 4D",
        "firstName": "Togel",
        "lastName": "Online",
        "email": "primahengkiki@gmail.com",
        ...
    }
}
```

**Assets yang digunakan:**
- Squarespace CSS/JS dari CDN resmi
- TypeKit fonts
- Template ID: `5c5a519771c10ba3470d8101`

---

## ⚠️ Indicators of Compromise (IoC)

### Domain & URLs

| Type | Indicator | Description |
|------|-----------|-------------|
| **Compromised Domain** | `lasik.tangerangselatankota.go.id` | Domain pemerintah yang di-abuse |
| **Malicious Landing** | `sdnbre.pages.dev` | Cloudflare Pages untuk judi |
| **Asset Server** | `jalurpintas.shop` | Host gambar/banner |
| **AMP Page** | `lasiktangerang.pages.dev` | Halaman AMP |

### Email Addresses

| Email | Context |
|-------|---------|
| `primahengkiki@gmail.com` | Account dalam Squarespace context |

### File Indicators

| Filename | Purpose |
|----------|---------|
| `pmz.txt` | Keyword database (21,134+ lines) |
| `svp/` | Directory untuk script |

### Network Indicators

```
# Legitimate Squarespace CDN (abused)
assets.squarespace.com
static1.squarespace.com
images.squarespace-cdn.com

# Malicious Infrastructure
jalurpintas.shop
sdnbre.pages.dev
lasiktangerang.pages.dev
```

---

## 🛠️ Attack Techniques (MITRE ATT&CK Mapping)

| Technique ID | Name | Description |
|--------------|------|-------------|
| T1584.001 | Compromise Infrastructure: Domains | Abuse domain pemerintah |
| T1608.005 | Stage Capabilities: Link Target | Doorway pages untuk redirect |
| T1036.005 | Masquerading: Match Legitimate Name | Menyamar sebagai layanan kesehatan |
| T1059.004 | Command and Scripting Interpreter: PHP | PHP script execution |

---

## 📊 Social Engineering Elements

### Visual Deception

```html
<style>
    .login, .login-button {
        background: linear-gradient(to bottom, #084100 0%, #084100 100%);
        border: 2px solid #f8f9e5;
        box-shadow: 0px 0px 3px #ff0000;
    }
    .register, .register-button {
        background: linear-gradient(to bottom, #084100 0%, #084100 100%);
        border: 2px solid #f8f9e5;
        box-shadow: 0px 0px 3px #ff0000;
    }
</style>
```

### Call-to-Action Buttons

```html
<div class="n-columns-2">
    <a href="<?php echo $AMP ?>" rel="nofollow noreferrer" class="login">LOGIN</a>
    <a href="<?php echo $AMP ?>" rel="nofollow noreferrer" class="register">DAFTAR</a>
</div>
```

---

## 🔄 Attack Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                      ATTACK FLOW DIAGRAM                         │
└─────────────────────────────────────────────────────────────────┘

[1] Attacker uploads script ke server pemerintah
                    │
                    ▼
[2] Script membaca keyword dari pmz.txt (21,134+ keywords)
                    │
                    ▼
[3] Google mengindex halaman doorway
    URL: lasik.tangerangselatankota.go.id/v2/svp/?app=slot88
                    │
                    ▼
[4] Korban search "slot88" di Google
                    │
                    ▼
[5] Hasil search menampilkan domain .go.id (trusted)
                    │
                    ▼
[6] Korban klik → Tampil halaman "LASIK Pemkot Tangsel"
                    │
                    ▼
[7] Korban klik LOGIN/DAFTAR
                    │
                    ▼
[8] Redirect ke sdnbre.pages.dev (situs judi actual)
```

---

## 🛡️ Detection & Mitigation

### Detection Rules

#### YARA Rule
```yara
rule PHP_Doorway_SEO_Spam {
    meta:
        description = "Detects PHP doorway page generator for SEO spam"
        author = "TangselSecTeam"
        date = "2026-02-05"
        threat_level = "high"
    
    strings:
        $referer_block = "HTTP_REFERER" ascii
        $google_console = "search-console/remove-outdated-content" ascii
        $keyword_file = "FILE_IGNORE_NEW_LINES" ascii
        $brand_var = "$BRAND" ascii
        $squarespace = "SQUARESPACE_CONTEXT" ascii
        $gambling = /togel|slot|judi|gacor/i
        
    condition:
        all of ($referer_block, $google_console) or
        (3 of them and $gambling)
}
```

#### Sigma Rule
```yaml
title: PHP Doorway Page Access Pattern
status: experimental
description: Detects access patterns typical of doorway page generators
logsource:
    category: webserver
    product: apache/nginx
detection:
    selection:
        cs-uri-query|contains:
            - 'app='
            - 'brand='
            - 'keyword='
    filter:
        cs-referer|contains:
            - 'search.google.com'
            - 'search-console'
    condition: selection and filter
level: high
```

### Mitigation Steps

#### For Website Administrators

1. **Immediate Actions:**
   ```bash
   # Find suspicious PHP files
   find /var/www -name "*.php" -exec grep -l "HTTP_REFERER.*search-console" {} \;
   
   # Check for keyword files
   find /var/www -name "*.txt" -size +100k
   
   # Review recently modified files
   find /var/www -name "*.php" -mtime -7
   ```

2. **File Integrity Monitoring:**
   ```bash
   # Generate baseline
   find /var/www -type f -exec md5sum {} \; > baseline.txt
   
   # Compare for changes
   md5sum -c baseline.txt | grep -i "FAILED"
   ```

3. **Web Application Firewall Rules:**
   ```nginx
   # Block suspicious query patterns
   if ($query_string ~* "(app|brand|keyword)=[a-z0-9]+(slot|togel|judi)") {
       return 403;
   }
   ```

#### For Google/Search Engines

1. Gunakan **Google Search Console Removal Tool**
2. Submit **spam report** ke Google
3. Request **manual review**

---

## 📚 Lessons Learned

### Untuk Tim Keamanan

1. **Domain Pemerintah Tidak Selalu Aman**
   - Domain `.go.id` bisa di-compromise
   - Jangan percaya domain semata

2. **SEO Spam = Indikator Compromise**
   - Jika website muncul di search dengan keyword aneh → investigate

3. **Monitoring Berkala**
   - Google Search Console alerts
   - File integrity monitoring
   - Access log analysis

### Untuk Pengguna

1. **Verifikasi URL Sebelum Klik**
   - Perhatikan path URL, bukan hanya domain
   
2. **Waspada Redirect**
   - Jika redirect ke domain berbeda → suspicious

3. **Report Spam**
   - Gunakan "Report spam" di Google search results

---

## 🔗 References

1. [Google Safe Browsing](https://safebrowsing.google.com/)
2. [MITRE ATT&CK - Compromise Infrastructure](https://attack.mitre.org/techniques/T1584/)
3. [OWASP - Doorway Pages](https://owasp.org/www-community/attacks/Doorway_Pages)
4. [Google Webmaster Guidelines - Cloaking](https://developers.google.com/search/docs/essentials/spam-policies)

---

## 📎 Appendix

### A. Sample Keyword List (dari pmz.txt)

```
slot88
togel4d
slot gacor
rtp live
bocoran slot
link alternatif
daftar slot
login togel
situs gacor
...
(21,134+ total keywords)
```

### B. Full HTTP Headers Sent

```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
X-UA-Compatible: IE=edge,chrome=1
Cache-Control: max-age=3600
```

### C. Related Samples

| Hash | Filename | First Seen |
|------|----------|------------|
| [TBD] | svp/index.php | 2026-02-05 |
| [TBD] | pmz.txt | 2026-02-05 |

---

> **Disclaimer:** Dokumentasi ini dibuat untuk tujuan edukasi keamanan siber. Jangan gunakan informasi ini untuk aktivitas ilegal.

---

**TangselSecTeam - Batch 1**  
*Security Research & Education*
