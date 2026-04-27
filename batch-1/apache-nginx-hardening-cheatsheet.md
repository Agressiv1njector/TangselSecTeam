# 🔒 Complete Web Server Hardening Cheatsheet
## Apache & Nginx Security Configuration

---

## 📋 Table of Contents
1. [Apache Hardening](#1-apache-hardening)
   - [Main Configuration](#apache-main-configuration)
   - [.htaccess Security](#htaccess-security)
   - [ModSecurity WAF](#modsecurity-waf)
2. [Nginx Hardening](#2-nginx-hardening)
   - [Main Configuration](#nginx-main-configuration)
   - [Security Headers](#nginx-security-headers)
   - [Rate Limiting](#nginx-rate-limiting)
3. [SSL/TLS Configuration](#3-ssltls-configuration)
4. [Comparison & Quick Reference](#4-comparison--quick-reference)

---

# 1. APACHE HARDENING

## Apache Main Configuration

### 📂 Configuration Files Location
```bash
# Debian/Ubuntu
/etc/apache2/apache2.conf
/etc/apache2/sites-available/
/etc/apache2/sites-enabled/
/etc/apache2/conf-available/
/etc/apache2/mods-available/

# RHEL/CentOS
/etc/httpd/conf/httpd.conf
/etc/httpd/conf.d/
/etc/httpd/conf.modules.d/
```

### 🔧 Basic Hardening (httpd.conf / apache2.conf)

```apache
# ===== HIDE SERVER INFORMATION =====
# Jangan tampilkan versi Apache
ServerTokens Prod
ServerSignature Off

# Disable server-generated pages
TraceEnable Off

# ===== DISABLE DIRECTORY LISTING =====
<Directory /var/www/html>
    Options -Indexes -FollowSymLinks -ExecCGI
    AllowOverride None
</Directory>

# ===== DISABLE .htaccess (jika tidak diperlukan) =====
<Directory />
    AllowOverride None
</Directory>

# ===== ENABLE .htaccess (jika diperlukan) =====
<Directory /var/www/html>
    AllowOverride All
</Directory>

# ===== LIMIT HTTP METHODS =====
<Directory /var/www/html>
    <LimitExcept GET POST HEAD>
        Require all denied
    </LimitExcept>
</Directory>

# Alternative: Only allow specific methods
<Location />
    <Limit PUT DELETE PATCH OPTIONS TRACE CONNECT>
        Require all denied
    </Limit>
</Location>

# ===== PREVENT CLICKJACKING =====
Header always set X-Frame-Options "SAMEORIGIN"

# ===== XSS PROTECTION =====
Header always set X-XSS-Protection "1; mode=block"

# ===== CONTENT TYPE SNIFFING =====
Header always set X-Content-Type-Options "nosniff"

# ===== REFERRER POLICY =====
Header always set Referrer-Policy "strict-origin-when-cross-origin"

# ===== CONTENT SECURITY POLICY =====
Header always set Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-ancestors 'self';"

# ===== PERMISSIONS POLICY =====
Header always set Permissions-Policy "geolocation=(), microphone=(), camera=(), payment=()"

# ===== STRICT TRANSPORT SECURITY (HSTS) =====
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"

# ===== TIMEOUT SETTINGS =====
Timeout 60
KeepAlive On
KeepAliveTimeout 5
MaxKeepAliveRequests 100

# ===== LIMIT REQUEST SIZE =====
LimitRequestBody 10485760
LimitRequestFields 50
LimitRequestFieldSize 8190
LimitRequestLine 8190

# ===== LIMIT XML REQUEST BODY =====
LimitXMLRequestBody 10485760

# ===== PROTECT SENSITIVE FILES =====
<FilesMatch "^\.ht">
    Require all denied
</FilesMatch>

<FilesMatch "\.(htaccess|htpasswd|ini|log|sh|bak|config|sql|fla|psd|vb|vbs|git|svn)$">
    Require all denied
</FilesMatch>

# ===== BLOCK ACCESS TO BACKUP FILES =====
<FilesMatch "(\.(bak|backup|old|orig|original|save|tmp|swp)|~)$">
    Require all denied
</FilesMatch>

# ===== PROTECT WP-CONFIG (WordPress) =====
<Files wp-config.php>
    Require all denied
</Files>

# ===== PROTECT .ENV FILE =====
<Files .env>
    Require all denied
</Files>

# ===== DISABLE ETAGs =====
FileETag None
Header unset ETag

# ===== SET SECURE COOKIE FLAGS =====
Header edit Set-Cookie ^(.*)$ "$1; HttpOnly; Secure; SameSite=Strict"

# ===== LOG CONFIGURATION =====
LogLevel warn
ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/access.log combined

# Log format with more details
LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" %T %D" detailed
CustomLog ${APACHE_LOG_DIR}/access_detailed.log detailed
```

### 🛡️ Anti-DDoS Configuration

```apache
# ===== MOD_EVASIVE (Anti-DDoS) =====
# Install: apt install libapache2-mod-evasive

<IfModule mod_evasive20.c>
    DOSHashTableSize    3097
    DOSPageCount        5
    DOSSiteCount        100
    DOSPageInterval     1
    DOSSiteInterval     1
    DOSBlockingPeriod   10
    DOSEmailNotify      admin@example.com
    DOSSystemCommand    "su - root -c '/sbin/iptables -A INPUT -s %s -j DROP'"
    DOSLogDir           "/var/log/mod_evasive"
    DOSWhitelist        127.0.0.1
    DOSWhitelist        192.168.1.*
</IfModule>

# ===== MOD_RATELIMIT =====
<IfModule mod_ratelimit.c>
    <Location /downloads>
        SetOutputFilter RATE_LIMIT
        SetEnv rate-limit 400
        SetEnv rate-initial-burst 512
    </Location>
</IfModule>

# ===== MOD_REQTIMEOUT (Slowloris Protection) =====
<IfModule mod_reqtimeout.c>
    RequestReadTimeout header=20-40,MinRate=500 body=20,MinRate=500
</IfModule>

# ===== LIMIT CONCURRENT CONNECTIONS =====
# Requires mod_limitipconn
<IfModule mod_limitipconn.c>
    <Location />
        MaxConnPerIP 10
        NoIPLimit image/*
    </Location>
</IfModule>

# ===== LIMIT REQUEST BODY FOR UPLOADS =====
<Directory /var/www/html/uploads>
    LimitRequestBody 5242880
</Directory>
```

### 🔐 Authentication & Access Control

```apache
# ===== BASIC AUTHENTICATION =====
<Directory /var/www/html/admin>
    AuthType Basic
    AuthName "Restricted Area"
    AuthUserFile /etc/apache2/.htpasswd
    Require valid-user
</Directory>

# Create password file
# htpasswd -c /etc/apache2/.htpasswd admin

# ===== DIGEST AUTHENTICATION (More Secure) =====
<Directory /var/www/html/secure>
    AuthType Digest
    AuthName "secure"
    AuthDigestProvider file
    AuthUserFile /etc/apache2/.htdigest
    Require valid-user
</Directory>

# Create digest file
# htdigest -c /etc/apache2/.htdigest secure admin

# ===== IP WHITELIST =====
<Directory /var/www/html/admin>
    Require ip 192.168.1.0/24
    Require ip 10.0.0.1
</Directory>

# ===== IP BLACKLIST =====
<Directory /var/www/html>
    <RequireAll>
        Require all granted
        Require not ip 1.2.3.4
        Require not ip 5.6.7.0/24
    </RequireAll>
</Directory>

# ===== COMBINE IP + AUTH =====
<Directory /var/www/html/admin>
    AuthType Basic
    AuthName "Admin Area"
    AuthUserFile /etc/apache2/.htpasswd
    <RequireAll>
        Require valid-user
        Require ip 192.168.1.0/24
    </RequireAll>
</Directory>
```

### 🌍 GeoIP Blocking

```apache
# Install: apt install libapache2-mod-geoip
<IfModule mod_geoip.c>
    GeoIPEnable On
    GeoIPDBFile /usr/share/GeoIP/GeoIP.dat
    
    # Block specific countries
    SetEnvIf GEOIP_COUNTRY_CODE CN BlockCountry
    SetEnvIf GEOIP_COUNTRY_CODE RU BlockCountry
    SetEnvIf GEOIP_COUNTRY_CODE KP BlockCountry
    
    <Directory /var/www/html>
        <RequireAll>
            Require all granted
            Require not env BlockCountry
        </RequireAll>
    </Directory>
</IfModule>
```

---

## .htaccess Security

### 📂 Location
```
/var/www/html/.htaccess
```

### 🔧 Complete Security .htaccess

```apache
# ====================================================
# COMPLETE SECURITY .htaccess
# Author: TangselSecTeam
# ====================================================

# ===== DISABLE DIRECTORY LISTING =====
Options -Indexes

# ===== DISABLE SERVER SIGNATURE =====
ServerSignature Off

# ===== FOLLOW SYMLINKS =====
Options -FollowSymLinks
Options +SymLinksIfOwnerMatch

# ===== DISABLE SCRIPT EXECUTION IN UPLOADS =====
<Directory /uploads>
    Options -ExecCGI
    AddHandler cgi-script .php .pl .py .jsp .asp .htm .shtml .sh .cgi
</Directory>

# ===== PROTECT .htaccess FILE =====
<Files .htaccess>
    Order allow,deny
    Deny from all
</Files>

# ===== PROTECT SENSITIVE FILES =====
<FilesMatch "^(wp-config\.php|\.htaccess|\.htpasswd|php\.ini|\.env|composer\.(json|lock)|package\.(json|lock)|\.git|\.svn)">
    Order allow,deny
    Deny from all
</FilesMatch>

# ===== BLOCK ACCESS TO HIDDEN FILES =====
<FilesMatch "^\.">
    Order allow,deny
    Deny from all
</FilesMatch>

# ===== BLOCK BACKUP FILES =====
<FilesMatch "\.(bak|backup|old|orig|save|swp|tmp)$">
    Order allow,deny
    Deny from all
</FilesMatch>

# ===== BLOCK LOG FILES =====
<FilesMatch "\.(log|logs)$">
    Order allow,deny
    Deny from all
</FilesMatch>

# ===== BLOCK SQL FILES =====
<FilesMatch "\.(sql|sqlite|db)$">
    Order allow,deny
    Deny from all
</FilesMatch>

# ===== SECURITY HEADERS =====
<IfModule mod_headers.c>
    # Prevent Clickjacking
    Header always set X-Frame-Options "SAMEORIGIN"
    
    # XSS Protection
    Header always set X-XSS-Protection "1; mode=block"
    
    # Prevent MIME Sniffing
    Header always set X-Content-Type-Options "nosniff"
    
    # Referrer Policy
    Header always set Referrer-Policy "strict-origin-when-cross-origin"
    
    # Content Security Policy
    Header always set Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self'; connect-src 'self'; frame-ancestors 'self'; base-uri 'self'; form-action 'self';"
    
    # Permissions Policy
    Header always set Permissions-Policy "geolocation=(), microphone=(), camera=(), payment=(), usb=(), magnetometer=(), gyroscope=(), accelerometer=()"
    
    # HSTS (Uncomment for HTTPS only)
    # Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
    
    # Remove Server Header
    Header unset Server
    Header unset X-Powered-By
    
    # Remove ETag
    Header unset ETag
    FileETag None
    
    # Secure Cookies
    Header edit Set-Cookie ^(.*)$ "$1; HttpOnly; Secure; SameSite=Strict"
</IfModule>

# ===== LIMIT HTTP METHODS =====
<LimitExcept GET POST HEAD>
    Order deny,allow
    Deny from all
</LimitExcept>

# ===== BLOCK BAD BOTS =====
<IfModule mod_rewrite.c>
    RewriteEngine On
    
    # Block bad bots
    RewriteCond %{HTTP_USER_AGENT} ^.*(Bot|Crawl|Spider|Wget|curl|libwww|HTTrack|harvest|extract|nikto|scan|grab|siphon).*$ [NC]
    RewriteRule .* - [F,L]
    
    # Block empty user agents
    RewriteCond %{HTTP_USER_AGENT} ^-?$
    RewriteRule .* - [F,L]
    
    # Block specific bad bots
    SetEnvIfNoCase User-Agent "^Wget" bad_bot
    SetEnvIfNoCase User-Agent "^HTTrack" bad_bot
    SetEnvIfNoCase User-Agent "^nikto" bad_bot
    SetEnvIfNoCase User-Agent "^sqlmap" bad_bot
    SetEnvIfNoCase User-Agent "^Nmap" bad_bot
    SetEnvIfNoCase User-Agent "^masscan" bad_bot
    SetEnvIfNoCase User-Agent "^ZmEu" bad_bot
    SetEnvIfNoCase User-Agent "^Morfeus" bad_bot
    SetEnvIfNoCase User-Agent "^Toata" bad_bot
    
    <RequireAll>
        Require all granted
        Require not env bad_bot
    </RequireAll>
</IfModule>

# ===== BLOCK SUSPICIOUS REQUEST METHODS =====
RewriteCond %{REQUEST_METHOD} ^(TRACE|DELETE|TRACK|DEBUG|CONNECT) [NC]
RewriteRule .* - [F,L]

# ===== BLOCK SUSPICIOUS QUERY STRINGS =====
<IfModule mod_rewrite.c>
    RewriteEngine On
    
    # Block SQL injection attempts
    RewriteCond %{QUERY_STRING} (\<|%3C).*script.*(\>|%3E) [NC,OR]
    RewriteCond %{QUERY_STRING} GLOBALS(=|\[|\%[0-9A-Z]{0,2}) [OR]
    RewriteCond %{QUERY_STRING} _REQUEST(=|\[|\%[0-9A-Z]{0,2}) [OR]
    RewriteCond %{QUERY_STRING} proc/self/environ [OR]
    RewriteCond %{QUERY_STRING} mosConfig_[a-zA-Z_]{1,21}(=|\%3D) [OR]
    RewriteCond %{QUERY_STRING} base64_(en|de)code[^(]*\([^)]*\) [OR]
    RewriteCond %{QUERY_STRING} (<|%3C)([^s]*s)+cript.*(>|%3E) [NC,OR]
    RewriteCond %{QUERY_STRING} UNION.*SELECT [NC,OR]
    RewriteCond %{QUERY_STRING} SELECT.*FROM [NC,OR]
    RewriteCond %{QUERY_STRING} INSERT.*INTO [NC,OR]
    RewriteCond %{QUERY_STRING} DROP.*TABLE [NC,OR]
    RewriteCond %{QUERY_STRING} UPDATE.*SET [NC,OR]
    RewriteCond %{QUERY_STRING} \.\./ [OR]
    RewriteCond %{QUERY_STRING} /etc/passwd [OR]
    RewriteCond %{QUERY_STRING} boot\.ini [NC,OR]
    RewriteCond %{QUERY_STRING} ftp: [NC,OR]
    RewriteCond %{QUERY_STRING} http: [NC,OR]
    RewriteCond %{QUERY_STRING} https: [NC,OR]
    RewriteCond %{QUERY_STRING} (<|%3C).*embed.*(>|%3E) [NC,OR]
    RewriteCond %{QUERY_STRING} (<|%3C).*iframe.*(>|%3E) [NC,OR]
    RewriteCond %{QUERY_STRING} (<|%3C).*object.*(>|%3E) [NC,OR]
    RewriteCond %{QUERY_STRING} (\.|%2e)(\.|%2e)(\./|%2f) [NC,OR]
    RewriteCond %{QUERY_STRING} (;|'|"|%22|%27).*(drop|insert|md5|select|union) [NC]
    RewriteRule .* - [F,L]
</IfModule>

# ===== BLOCK FILE INJECTION (RFI/LFI) =====
<IfModule mod_rewrite.c>
    RewriteCond %{REQUEST_METHOD} GET
    RewriteCond %{QUERY_STRING} [a-zA-Z0-9_]=http:// [OR]
    RewriteCond %{QUERY_STRING} [a-zA-Z0-9_]=https:// [OR]
    RewriteCond %{QUERY_STRING} [a-zA-Z0-9_]=ftp:// [OR]
    RewriteCond %{QUERY_STRING} [a-zA-Z0-9_]=php:// [OR]
    RewriteCond %{QUERY_STRING} [a-zA-Z0-9_]=data:// [OR]
    RewriteCond %{QUERY_STRING} [a-zA-Z0-9_]=expect:// [OR]
    RewriteCond %{QUERY_STRING} [a-zA-Z0-9_]=input:// [OR]
    RewriteCond %{QUERY_STRING} [a-zA-Z0-9_]=zip:// [OR]
    RewriteCond %{QUERY_STRING} [a-zA-Z0-9_]=(\.\.//?)+ [OR]
    RewriteCond %{QUERY_STRING} [a-zA-Z0-9_]=/([a-z0-9_.]//?)+ [NC]
    RewriteRule .* - [F,L]
</IfModule>

# ============================================================
# CSRF PROTECTION (Cross-Site Request Forgery)
# ============================================================

# ===== CSRF - BLOCK REQUESTS FROM DIFFERENT ORIGIN/REFERER =====
<IfModule mod_rewrite.c>
    RewriteEngine On
    
    # Block POST requests without valid Referer (CSRF Protection)
    RewriteCond %{REQUEST_METHOD} POST
    RewriteCond %{HTTP_REFERER} !^https?://(www\.)?yourdomain\.com [NC]
    RewriteCond %{HTTP_REFERER} !^$
    RewriteRule .* - [F,L]
    
    # Block POST to sensitive endpoints without same-origin referer
    RewriteCond %{REQUEST_METHOD} POST
    RewriteCond %{REQUEST_URI} ^/(admin|login|register|checkout|payment|transfer|api|upload|delete|update|edit|settings|profile|password|account) [NC]
    RewriteCond %{HTTP_REFERER} !^https?://(www\.)?yourdomain\.com [NC]
    RewriteRule .* - [F,L]
    
    # Block if Origin header doesn't match
    RewriteCond %{REQUEST_METHOD} POST
    RewriteCond %{HTTP:Origin} !^$
    RewriteCond %{HTTP:Origin} !^https?://(www\.)?yourdomain\.com [NC]
    RewriteRule .* - [F,L]
</IfModule>

# ===== CSRF - BLOCK CROSS-ORIGIN AJAX REQUESTS =====
<IfModule mod_headers.c>
    # Set CORS headers untuk whitelist origins
    SetEnvIf Origin "^https?://(www\.)?(yourdomain\.com|subdomain\.yourdomain\.com)$" ORIGIN_OK=1
    Header always set Access-Control-Allow-Origin "%{HTTP_ORIGIN}e" env=ORIGIN_OK
    Header always set Access-Control-Allow-Methods "GET, POST, OPTIONS" env=ORIGIN_OK
    Header always set Access-Control-Allow-Headers "Content-Type, X-Requested-With, X-CSRF-Token" env=ORIGIN_OK
    Header always set Access-Control-Allow-Credentials "true" env=ORIGIN_OK
    
    # Block requests without proper Origin for state-changing operations
    <If "%{REQUEST_METHOD} in {'POST', 'PUT', 'DELETE', 'PATCH'}">
        SetEnvIf Origin "." ORIGIN_SET=1
        SetEnvIf Referer "." REFERER_SET=1
    </If>
</IfModule>

# ============================================================
# ADVANCED SQL INJECTION PROTECTION
# ============================================================

<IfModule mod_rewrite.c>
    RewriteEngine On
    
    # Block SQL injection in URI
    RewriteCond %{REQUEST_URI} (\%27)|(\')|(\-\-)|(\%23)|(#) [NC,OR]
    RewriteCond %{REQUEST_URI} (union)(.*)(select) [NC,OR]
    RewriteCond %{REQUEST_URI} (select)(.*)(from) [NC,OR]
    RewriteCond %{REQUEST_URI} (insert)(.*)(into) [NC,OR]
    RewriteCond %{REQUEST_URI} (drop)(.*)(table) [NC,OR]
    RewriteCond %{REQUEST_URI} (delete)(.*)(from) [NC,OR]
    RewriteCond %{REQUEST_URI} (update)(.*)(set) [NC,OR]
    RewriteCond %{REQUEST_URI} (create)(.*)(table) [NC,OR]
    RewriteCond %{REQUEST_URI} (alter)(.*)(table) [NC,OR]
    RewriteCond %{REQUEST_URI} (truncate)(.*)(table) [NC,OR]
    RewriteCond %{REQUEST_URI} (exec|execute)(\s|\+|\%20)*(xp_|sp_) [NC,OR]
    RewriteCond %{REQUEST_URI} (benchmark|sleep|waitfor|delay)(\s|\+|\%20)*\( [NC,OR]
    RewriteCond %{REQUEST_URI} (load_file|into\s+outfile|into\s+dumpfile) [NC,OR]
    RewriteCond %{REQUEST_URI} (information_schema|mysql\.|sys\.) [NC,OR]
    RewriteCond %{REQUEST_URI} (\/\*.*\*\/) [NC,OR]
    RewriteCond %{REQUEST_URI} (concat|group_concat|char|chr|ascii|hex|unhex|ord)(\s|\+|\%20)*\( [NC,OR]
    RewriteCond %{REQUEST_URI} (;|\||`|>|<|\*|\\|{|}|\[|\]|\^|~) [NC]
    RewriteRule .* - [F,L]
    
    # Block SQL injection in Query String (comprehensive)
    RewriteCond %{QUERY_STRING} (\%27)|(\')|(\-\-)|(\%23)|(#) [NC,OR]
    RewriteCond %{QUERY_STRING} (union)(.*)(select) [NC,OR]
    RewriteCond %{QUERY_STRING} (select)(.*)(from) [NC,OR]
    RewriteCond %{QUERY_STRING} (insert)(.*)(into) [NC,OR]
    RewriteCond %{QUERY_STRING} (drop)(.*)(table|database|column|index) [NC,OR]
    RewriteCond %{QUERY_STRING} (delete)(.*)(from) [NC,OR]
    RewriteCond %{QUERY_STRING} (update)(.*)(set) [NC,OR]
    RewriteCond %{QUERY_STRING} (create)(.*)(table|database|function|procedure) [NC,OR]
    RewriteCond %{QUERY_STRING} (alter)(.*)(table|database|column) [NC,OR]
    RewriteCond %{QUERY_STRING} (truncate)(.*)(table) [NC,OR]
    RewriteCond %{QUERY_STRING} (%00|%0a|%0d|%27|%3c|%3e|%3C|%3E) [NC,OR]
    RewriteCond %{QUERY_STRING} (benchmark|sleep|waitfor\s+delay)(\s|\+|\%20)*\( [NC,OR]
    RewriteCond %{QUERY_STRING} (load_file|into\s+(out|dump)file) [NC,OR]
    RewriteCond %{QUERY_STRING} (information_schema|mysql\.|sys\.|performance_schema) [NC,OR]
    RewriteCond %{QUERY_STRING} (\/\*.*\*\/|\/\*!.*\*\/) [NC,OR]
    RewriteCond %{QUERY_STRING} (concat|group_concat|char|chr|ascii|hex|unhex|ord|conv)(\s|\+|\%20)*\( [NC,OR]
    RewriteCond %{QUERY_STRING} (exec|execute)(\s|\+|\%20)*(xp_|sp_|master\.) [NC,OR]
    RewriteCond %{QUERY_STRING} (having|order\s+by|group\s+by)(\s|\+|\%20)+[0-9] [NC,OR]
    RewriteCond %{QUERY_STRING} (\|\||&&|;|`|>|<|\\x) [NC]
    RewriteRule .* - [F,L]
    
    # Block SQL injection in Cookies
    RewriteCond %{HTTP_COOKIE} (\%27)|(\')|(\-\-)|(\%23)|(#) [NC,OR]
    RewriteCond %{HTTP_COOKIE} (union)(.*)(select) [NC,OR]
    RewriteCond %{HTTP_COOKIE} (select)(.*)(from) [NC]
    RewriteRule .* - [F,L]
</IfModule>

# ============================================================
# RCE (Remote Code Execution) PROTECTION
# ============================================================

<IfModule mod_rewrite.c>
    RewriteEngine On
    
    # Block command injection in URI
    RewriteCond %{REQUEST_URI} (;|\||`|\$\(|\$\{|&&|\|\|) [NC,OR]
    RewriteCond %{REQUEST_URI} (\%3B|\%7C|\%60|\%24\%28|\%26\%26) [NC,OR]
    RewriteCond %{REQUEST_URI} (cmd|command)(=|%3D) [NC,OR]
    RewriteCond %{REQUEST_URI} (exec|shell|system|passthru|popen|proc_open)(=|%3D|\() [NC,OR]
    RewriteCond %{REQUEST_URI} (/bin/(bash|sh|csh|ksh|tcsh|zsh|dash)) [NC,OR]
    RewriteCond %{REQUEST_URI} (/usr/(bin|sbin|local)/) [NC,OR]
    RewriteCond %{REQUEST_URI} (wget|curl|fetch|lwp-download)(\s|\+|\%20) [NC,OR]
    RewriteCond %{REQUEST_URI} (nc|netcat|ncat)(\s|\+|\%20)+-[a-z] [NC,OR]
    RewriteCond %{REQUEST_URI} (python|perl|ruby|php|node)(\s|\+|\%20)+-[a-z] [NC]
    RewriteRule .* - [F,L]
    
    # Block command injection in Query String
    RewriteCond %{QUERY_STRING} (;|\||`|\$\(|\$\{|&&|\|\||\n|\r) [NC,OR]
    RewriteCond %{QUERY_STRING} (cmd|command|exec|execute|run)(=|%3D) [NC,OR]
    RewriteCond %{QUERY_STRING} (passthru|shell_exec|system|popen|proc_open|pcntl_exec)(=|%3D|\() [NC,OR]
    RewriteCond %{QUERY_STRING} (eval|assert|preg_replace.*\/e|create_function)(\s|\+|\%20)*\( [NC,OR]
    RewriteCond %{QUERY_STRING} (/bin/(bash|sh|csh|ksh|dash|zsh)) [NC,OR]
    RewriteCond %{QUERY_STRING} (/etc/(passwd|shadow|group|hosts)) [NC,OR]
    RewriteCond %{QUERY_STRING} (/proc/(self|version|cmdline)) [NC,OR]
    RewriteCond %{QUERY_STRING} (wget|curl|fetch|lwp-download|lynx)(\s|\+|\%20|%09) [NC,OR]
    RewriteCond %{QUERY_STRING} (nc|netcat|ncat|telnet)(\s|\+|\%20)+-[a-z] [NC,OR]
    RewriteCond %{QUERY_STRING} (python|perl|ruby|php|node|bash)(\s|\+|\%20)+-[cre] [NC,OR]
    RewriteCond %{QUERY_STRING} (\x00|\x0a|\x0d|\x1a|\x1b) [NC,OR]
    RewriteCond %{QUERY_STRING} (base64_decode|gzinflate|gzuncompress|str_rot13)(\s|\+|\%20)*\( [NC]
    RewriteRule .* - [F,L]
    
    # Block reverse shell patterns
    RewriteCond %{QUERY_STRING} (bash\s+-i|\/dev\/(tcp|udp)) [NC,OR]
    RewriteCond %{QUERY_STRING} (mkfifo|mknod)(\s|\+|\%20) [NC,OR]
    RewriteCond %{QUERY_STRING} (\||\%7C)(\s|\+|\%20)*(nc|netcat|bash|sh) [NC,OR]
    RewriteCond %{QUERY_STRING} (python.*socket|perl.*socket|ruby.*socket) [NC,OR]
    RewriteCond %{QUERY_STRING} (import\s+os|import\s+socket|import\s+subprocess) [NC]
    RewriteRule .* - [F,L]
</IfModule>

# ============================================================
# XSS (Cross-Site Scripting) PROTECTION - ENHANCED
# ============================================================

<IfModule mod_rewrite.c>
    RewriteEngine On
    
    # Block XSS in URI
    RewriteCond %{REQUEST_URI} (<|%3C)(\s)*script [NC,OR]
    RewriteCond %{REQUEST_URI} (<|%3C)(\s)*(img|iframe|object|embed|video|audio|svg|math|body|input|button|form|style|link|meta|base) [NC,OR]
    RewriteCond %{REQUEST_URI} (javascript|vbscript|livescript|expression)(\s)*: [NC,OR]
    RewriteCond %{REQUEST_URI} (on(error|load|click|mouse|focus|blur|change|submit|key|drag|drop|abort|scroll|resize|unload|beforeunload|hashchange|popstate|storage|message))(\s)*= [NC,OR]
    RewriteCond %{REQUEST_URI} (document\.(cookie|location|write|domain)|window\.(location|open|name)|eval\(|alert\(|prompt\(|confirm\() [NC,OR]
    RewriteCond %{REQUEST_URI} (innerHTML|outerHTML|insertAdjacentHTML|document\.write) [NC,OR]
    RewriteCond %{REQUEST_URI} (fromCharCode|String\.fromCharCode) [NC]
    RewriteRule .* - [F,L]
    
    # Block XSS in Query String
    RewriteCond %{QUERY_STRING} (<|%3C)(\s)*script [NC,OR]
    RewriteCond %{QUERY_STRING} (<|%3C)(\s)*(img|iframe|object|embed|video|audio|svg|math|body|input|button|form|style|link|meta|base)(\s|%20)[^>]*> [NC,OR]
    RewriteCond %{QUERY_STRING} (javascript|vbscript|livescript|expression)(\s)*: [NC,OR]
    RewriteCond %{QUERY_STRING} (on(error|load|click|mouse|focus|blur|change|submit|key|drag|drop|abort|scroll|resize|contextmenu|dblclick|wheel))(\s)*= [NC,OR]
    RewriteCond %{QUERY_STRING} (document\.(cookie|location|write|domain|body|forms|links|images)|window\.(location|open|name|frames)) [NC,OR]
    RewriteCond %{QUERY_STRING} (eval|alert|prompt|confirm|atob|btoa)(\s|\%20)*\( [NC,OR]
    RewriteCond %{QUERY_STRING} (innerHTML|outerHTML|textContent|insertAdjacentHTML|document\.write) [NC,OR]
    RewriteCond %{QUERY_STRING} (fromCharCode|String\.fromCharCode|unescape|decodeURI|decodeURIComponent) [NC,OR]
    RewriteCond %{QUERY_STRING} (data:text\/html|data:application\/javascript|data:text\/javascript) [NC]
    RewriteRule .* - [F,L]
    
    # Block XSS in User-Agent
    RewriteCond %{HTTP_USER_AGENT} (<|%3C)script [NC,OR]
    RewriteCond %{HTTP_USER_AGENT} (javascript|vbscript): [NC,OR]
    RewriteCond %{HTTP_USER_AGENT} on(error|load|click)= [NC]
    RewriteRule .* - [F,L]
    
    # Block XSS in Referer
    RewriteCond %{HTTP_REFERER} (<|%3C)script [NC,OR]
    RewriteCond %{HTTP_REFERER} (javascript|vbscript): [NC]
    RewriteRule .* - [F,L]
</IfModule>

# ============================================================
# PATH TRAVERSAL / LFI PROTECTION - ENHANCED
# ============================================================

<IfModule mod_rewrite.c>
    RewriteEngine On
    
    # Block path traversal attempts
    RewriteCond %{REQUEST_URI} (\.\./|\.\.\\|%2e%2e%2f|%2e%2e\/|\.%2e\/|%2e\.\/|\.\.%5c|%2e%2e%5c) [NC,OR]
    RewriteCond %{REQUEST_URI} (\/\.\.\/|\\\.\.\\) [NC,OR]
    RewriteCond %{QUERY_STRING} (\.\./|\.\.\\|%2e%2e%2f|%2e%2e\/|\.%2e\/|%2e\.\/|\.\.%5c|%2e%2e%5c) [NC]
    RewriteRule .* - [F,L]
    
    # Block access to sensitive files
    RewriteCond %{REQUEST_URI} (/etc/(passwd|shadow|group|hosts|resolv\.conf|fstab|issue|motd|crontab)) [NC,OR]
    RewriteCond %{REQUEST_URI} (/proc/(self|version|cmdline|mounts|net)) [NC,OR]
    RewriteCond %{REQUEST_URI} (/var/(log|mail|spool|www)) [NC,OR]
    RewriteCond %{REQUEST_URI} (boot\.ini|win\.ini|system\.ini|config\.sys|autoexec\.bat) [NC,OR]
    RewriteCond %{REQUEST_URI} (web\.config|applicationhost\.config|machine\.config) [NC,OR]
    RewriteCond %{REQUEST_URI} (\.htaccess|\.htpasswd|\.htgroups|\.bash_history|\.bash_profile|\.bashrc) [NC]
    RewriteRule .* - [F,L]
    
    # Block PHP wrappers for LFI
    RewriteCond %{QUERY_STRING} (php:\/\/|file:\/\/|glob:\/\/|data:\/\/|expect:\/\/|zip:\/\/|rar:\/\/|phar:\/\/|ogg:\/\/|zlib:\/\/) [NC,OR]
    RewriteCond %{QUERY_STRING} (input|filter|data|resource)(\%3A|:)\/\/ [NC,OR]
    RewriteCond %{QUERY_STRING} (convert\.base64-(encode|decode)|string\.(rot13|toupper|tolower|strip_tags)) [NC]
    RewriteRule .* - [F,L]
</IfModule>

# ============================================================
# SSRF (Server-Side Request Forgery) PROTECTION
# ============================================================

<IfModule mod_rewrite.c>
    RewriteEngine On
    
    # Block SSRF attempts
    RewriteCond %{QUERY_STRING} (url|uri|path|link|src|href|redirect|return|next|callback|fetch|proxy)(=|%3D)(http|https|ftp|file|gopher|dict|ldap|ssh|telnet)(\%3A|:) [NC,OR]
    RewriteCond %{QUERY_STRING} (127\.0\.0\.1|localhost|0\.0\.0\.0|::1|0177\.0\.0\.1|2130706433) [NC,OR]
    RewriteCond %{QUERY_STRING} (169\.254\.|10\.|172\.(1[6-9]|2[0-9]|3[01])\.|192\.168\.) [NC,OR]
    RewriteCond %{QUERY_STRING} (metadata\.google|169\.254\.169\.254) [NC,OR]
    RewriteCond %{QUERY_STRING} (@|%40)(localhost|127\.0\.0\.1) [NC]
    RewriteRule .* - [F,L]
</IfModule>

# ===== BLOCK IP ADDRESSES =====
Order Allow,Deny
Allow from all
# Deny from 1.2.3.4
# Deny from 5.6.7.0/24

# ===== ALLOW ONLY SPECIFIC IPS (for admin) =====
# <Files "admin.php">
#     Order Deny,Allow
#     Deny from all
#     Allow from 192.168.1.0/24
#     Allow from 10.0.0.1
# </Files>

# ===== RATE LIMITING (Anti-DDoS) =====
<IfModule mod_ratelimit.c>
    SetOutputFilter RATE_LIMIT
    SetEnv rate-limit 500
</IfModule>

# ===== PREVENT HOTLINKING =====
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{HTTP_REFERER} !^$
    RewriteCond %{HTTP_REFERER} !^https?://(www\.)?yourdomain\.com [NC]
    RewriteRule \.(jpg|jpeg|png|gif|webp|svg|css|js)$ - [F,NC]
</IfModule>

# ===== FORCE HTTPS =====
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{HTTPS} off
    RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
</IfModule>

# ===== REMOVE WWW =====
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{HTTP_HOST} ^www\.(.*)$ [NC]
    RewriteRule ^(.*)$ https://%1/$1 [R=301,L]
</IfModule>

# ===== COMPRESSION =====
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/html
    AddOutputFilterByType DEFLATE text/xml
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE text/javascript
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE application/xhtml+xml
    AddOutputFilterByType DEFLATE application/rss+xml
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/x-javascript
    AddOutputFilterByType DEFLATE application/json
</IfModule>

# ===== BROWSER CACHING =====
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType image/jpg "access plus 1 year"
    ExpiresByType image/jpeg "access plus 1 year"
    ExpiresByType image/gif "access plus 1 year"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType image/webp "access plus 1 year"
    ExpiresByType image/svg+xml "access plus 1 year"
    ExpiresByType text/css "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 month"
    ExpiresByType text/javascript "access plus 1 month"
    ExpiresByType application/pdf "access plus 1 month"
    ExpiresByType text/html "access plus 0 seconds"
</IfModule>

# ===== CUSTOM ERROR PAGES =====
ErrorDocument 400 /errors/400.html
ErrorDocument 401 /errors/401.html
ErrorDocument 403 /errors/403.html
ErrorDocument 404 /errors/404.html
ErrorDocument 500 /errors/500.html
ErrorDocument 502 /errors/502.html
ErrorDocument 503 /errors/503.html

# ===== PHP SETTINGS (if using PHP) =====
<IfModule mod_php.c>
    php_flag display_errors Off
    php_flag log_errors On
    php_flag expose_php Off
    php_value max_execution_time 30
    php_value max_input_time 60
    php_value memory_limit 128M
    php_value post_max_size 10M
    php_value upload_max_filesize 10M
    php_flag allow_url_fopen Off
    php_flag allow_url_include Off
    php_flag session.cookie_httponly On
    php_flag session.cookie_secure On
    php_value session.cookie_samesite Strict
</IfModule>
```

### 🔒 WordPress Specific .htaccess

```apache
# ===== WORDPRESS SECURITY .htaccess =====

# Block WordPress xmlrpc.php attacks
<Files xmlrpc.php>
    Order deny,allow
    Deny from all
</Files>

# Protect wp-config.php
<Files wp-config.php>
    Order allow,deny
    Deny from all
</Files>

# Protect wp-includes
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteBase /
    RewriteRule ^wp-admin/includes/ - [F,L]
    RewriteRule !^wp-includes/ - [S=3]
    RewriteRule ^wp-includes/[^/]+\.php$ - [F,L]
    RewriteRule ^wp-includes/js/tinymce/langs/.+\.php - [F,L]
    RewriteRule ^wp-includes/theme-compat/ - [F,L]
</IfModule>

# Block author enumeration
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{QUERY_STRING} ^author=([0-9]*)
    RewriteRule .* - [F,L]
</IfModule>

# Protect wp-login.php from brute force
<Files wp-login.php>
    Order deny,allow
    Deny from all
    # Allow your IP
    Allow from 192.168.1.0/24
</Files>

# Or use rate limiting
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{REQUEST_METHOD} POST
    RewriteCond %{REQUEST_URI} ^/wp-login\.php$
    RewriteCond %{HTTP_REFERER} !^https?://(www\.)?yourdomain\.com [NC]
    RewriteRule .* - [F,L]
</IfModule>

# Block PHP execution in uploads
<Directory /wp-content/uploads/>
    <Files *.php>
        deny from all
    </Files>
</Directory>

# Disable file editing
# Add to wp-config.php: define('DISALLOW_FILE_EDIT', true);
```

---

## ModSecurity WAF

### 🔧 Installation & Basic Setup

```bash
# Install ModSecurity
# Debian/Ubuntu
apt install libapache2-mod-security2
a2enmod security2

# RHEL/CentOS
yum install mod_security
```

### 📂 Configuration (/etc/modsecurity/modsecurity.conf)

```apache
# ===== MODSECURITY CONFIGURATION =====

# Enable ModSecurity
SecRuleEngine On

# Set default action
SecDefaultAction "phase:2,deny,log,status:403"

# Request body handling
SecRequestBodyAccess On
SecRequestBodyLimit 13107200
SecRequestBodyNoFilesLimit 131072
SecRequestBodyLimitAction Reject

# Response body handling
SecResponseBodyAccess On
SecResponseBodyMimeType text/plain text/html text/xml application/json
SecResponseBodyLimit 524288
SecResponseBodyLimitAction ProcessPartial

# Temporary directory
SecTmpDir /tmp/
SecDataDir /var/cache/modsecurity/

# Audit logging
SecAuditEngine RelevantOnly
SecAuditLogRelevantStatus "^(?:5|4(?!04))"
SecAuditLogParts ABCDEFHIJKZ
SecAuditLogType Serial
SecAuditLog /var/log/apache2/modsec_audit.log

# Debug log (disable in production)
SecDebugLog /var/log/apache2/modsec_debug.log
SecDebugLogLevel 0

# PCRE limits
SecPcreMatchLimit 100000
SecPcreMatchLimitRecursion 100000

# Server signature
SecServerSignature "Microsoft-IIS/10.0"

# ===== CUSTOM RULES =====

# Block SQL Injection
SecRule REQUEST_URI|ARGS|ARGS_NAMES "@rx (?i)(union.*select|select.*from|insert.*into|drop.*table|delete.*from|update.*set)" \
    "id:1000,phase:2,deny,log,msg:'SQL Injection Attempt'"

# Block XSS
SecRule REQUEST_URI|ARGS|ARGS_NAMES "@rx (?i)(<script|javascript:|vbscript:|onclick|onerror|onload)" \
    "id:1001,phase:2,deny,log,msg:'XSS Attack Attempt'"

# Block Path Traversal
SecRule REQUEST_URI|ARGS "@rx (\.\./|\.\.\\)" \
    "id:1002,phase:2,deny,log,msg:'Path Traversal Attempt'"

# Block Command Injection
SecRule REQUEST_URI|ARGS "@rx (?i)(;|\||`|\$\(|&&)" \
    "id:1003,phase:2,deny,log,msg:'Command Injection Attempt'"

# Block PHP injection
SecRule REQUEST_URI|ARGS "@rx (?i)(eval\(|base64_decode\(|gzinflate\(|shell_exec\(|exec\(|system\(|passthru\()" \
    "id:1004,phase:2,deny,log,msg:'PHP Injection Attempt'"

# Rate limiting
SecAction "id:1005,phase:1,nolog,pass,initcol:ip=%{REMOTE_ADDR},setvar:ip.requests=+1,expirevar:ip.requests=60"
SecRule IP:REQUESTS "@gt 100" "id:1006,phase:2,deny,log,msg:'Rate Limit Exceeded'"

# Block bad user agents
SecRule REQUEST_HEADERS:User-Agent "@rx (?i)(nikto|sqlmap|nmap|masscan|wget|curl)" \
    "id:1007,phase:1,deny,log,msg:'Bad User Agent Blocked'"

# Whitelist IP
SecRule REMOTE_ADDR "@ipMatch 192.168.1.0/24" "id:1008,phase:1,allow,nolog"
```

### 🛡️ OWASP CRS (Core Rule Set)

```bash
# Download OWASP CRS
cd /etc/modsecurity
git clone https://github.com/coreruleset/coreruleset.git
cp coreruleset/crs-setup.conf.example crs-setup.conf

# Enable in Apache
# Add to apache2.conf or security2.conf:
IncludeOptional /etc/modsecurity/coreruleset/crs-setup.conf
IncludeOptional /etc/modsecurity/coreruleset/rules/*.conf
```

---

# 2. NGINX HARDENING

## Nginx Main Configuration

### 📂 Configuration Files Location
```bash
/etc/nginx/nginx.conf
/etc/nginx/conf.d/
/etc/nginx/sites-available/
/etc/nginx/sites-enabled/
/etc/nginx/snippets/
```

### 🔧 Main Configuration (/etc/nginx/nginx.conf)

```nginx
# ===== NGINX HARDENING CONFIGURATION =====

user www-data;
worker_processes auto;
worker_rlimit_nofile 65535;
pid /run/nginx.pid;

events {
    worker_connections 65535;
    multi_accept on;
    use epoll;
}

http {
    # ===== BASIC SETTINGS =====
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;
    server_tokens off;  # Hide version
    
    # ===== BUFFER SIZES =====
    client_body_buffer_size 16k;
    client_header_buffer_size 1k;
    client_max_body_size 10m;
    large_client_header_buffers 4 8k;
    
    # ===== TIMEOUTS =====
    client_body_timeout 12;
    client_header_timeout 12;
    send_timeout 10;
    
    # ===== GZIP COMPRESSION =====
    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types text/plain text/css text/xml application/json application/javascript application/xml+rss application/atom+xml image/svg+xml;
    
    # ===== LOGGING =====
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';
    
    log_format security '$remote_addr - $remote_user [$time_local] "$request" '
                        '$status $body_bytes_sent "$http_referer" '
                        '"$http_user_agent" "$http_x_forwarded_for" '
                        '$request_time $upstream_response_time';
    
    access_log /var/log/nginx/access.log main;
    error_log /var/log/nginx/error.log warn;
    
    # ===== RATE LIMITING ZONES =====
    limit_req_zone $binary_remote_addr zone=general:10m rate=10r/s;
    limit_req_zone $binary_remote_addr zone=login:10m rate=1r/s;
    limit_req_zone $binary_remote_addr zone=api:10m rate=100r/s;
    limit_req_zone $binary_remote_addr zone=strict:10m rate=5r/m;
    
    # ===== CONNECTION LIMITING =====
    limit_conn_zone $binary_remote_addr zone=conn_limit:10m;
    limit_conn_zone $server_name zone=server_limit:10m;
    
    # ===== GEO BLOCKING =====
    # Create /etc/nginx/conf.d/geo-block.conf
    # geo $blocked_country {
    #     default 0;
    #     1.2.3.0/24 1;  # Block this range
    # }
    
    include /etc/nginx/mime.types;
    default_type application/octet-stream;
    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}
```

### 🛡️ Security Headers & Site Configuration

```nginx
# /etc/nginx/sites-available/secure-site.conf

server {
    listen 80;
    server_name example.com www.example.com;
    
    # Redirect to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name example.com www.example.com;
    
    root /var/www/html;
    index index.html index.php;
    
    # ===== SSL CONFIGURATION =====
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    ssl_session_timeout 1d;
    ssl_session_cache shared:SSL:50m;
    ssl_session_tickets off;
    
    # Modern SSL configuration
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;
    
    # OCSP Stapling
    ssl_stapling on;
    ssl_stapling_verify on;
    ssl_trusted_certificate /etc/letsencrypt/live/example.com/chain.pem;
    resolver 8.8.8.8 8.8.4.4 valid=300s;
    resolver_timeout 5s;
    
    # ===== SECURITY HEADERS =====
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self'; connect-src 'self'; frame-ancestors 'self'; base-uri 'self'; form-action 'self';" always;
    add_header Permissions-Policy "geolocation=(), microphone=(), camera=(), payment=(), usb=()" always;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
    add_header X-Permitted-Cross-Domain-Policies "none" always;
    add_header X-Download-Options "noopen" always;
    
    # Remove server header
    more_clear_headers Server;
    more_clear_headers X-Powered-By;
    
    # ===== RATE LIMITING =====
    limit_req zone=general burst=20 nodelay;
    limit_conn conn_limit 50;
    
    # ===== BLOCK BAD BOTS =====
    if ($http_user_agent ~* (bot|crawl|spider|wget|curl|nikto|sqlmap|nmap|masscan|scan|harvest|extract)) {
        return 403;
    }
    
    # Block empty user agents
    if ($http_user_agent = "") {
        return 403;
    }
    
    # ===== BLOCK BAD METHODS =====
    if ($request_method !~ ^(GET|HEAD|POST)$) {
        return 405;
    }
    
    # ===== DENY ACCESS TO HIDDEN FILES =====
    location ~ /\. {
        deny all;
        access_log off;
        log_not_found off;
    }
    
    # ===== DENY ACCESS TO SENSITIVE FILES =====
    location ~* \.(htaccess|htpasswd|ini|log|sh|sql|bak|config|env|git|svn)$ {
        deny all;
    }
    
    # ===== DENY ACCESS TO BACKUP FILES =====
    location ~* \.(bak|backup|old|orig|save|swp|tmp)$ {
        deny all;
    }
    
    # ===== STATIC FILES CACHING =====
    location ~* \.(jpg|jpeg|png|gif|ico|css|js|woff|woff2|ttf|svg|webp)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
        access_log off;
    }
    
    # ===== PHP CONFIGURATION =====
    location ~ \.php$ {
        fastcgi_pass unix:/var/run/php/php8.1-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
        
        # Security
        fastcgi_hide_header X-Powered-By;
        fastcgi_read_timeout 300;
    }
    
    # ===== UPLOADS DIRECTORY (No PHP execution) =====
    location /uploads/ {
        location ~ \.php$ {
            deny all;
        }
    }
    
    # ===== ADMIN AREA PROTECTION =====
    location /admin/ {
        # IP whitelist
        allow 192.168.1.0/24;
        allow 10.0.0.1;
        deny all;
        
        # Or with rate limiting
        limit_req zone=strict burst=3 nodelay;
        
        # Basic auth
        auth_basic "Admin Area";
        auth_basic_user_file /etc/nginx/.htpasswd;
    }
    
    # ===== LOGIN PAGE PROTECTION =====
    location /login {
        limit_req zone=login burst=3 nodelay;
    }
    
    # ===== API RATE LIMITING =====
    location /api/ {
        limit_req zone=api burst=50 nodelay;
        limit_conn conn_limit 20;
    }
}
```

## Nginx Rate Limiting

### 🛡️ Anti-DDoS Configuration

```nginx
# /etc/nginx/conf.d/rate-limiting.conf

# ===== RATE LIMIT ZONES =====
# General browsing
limit_req_zone $binary_remote_addr zone=general:10m rate=10r/s;

# Login/Auth pages
limit_req_zone $binary_remote_addr zone=login:10m rate=1r/s;

# API endpoints
limit_req_zone $binary_remote_addr zone=api:10m rate=50r/s;

# Strict (admin, sensitive pages)
limit_req_zone $binary_remote_addr zone=strict:10m rate=5r/m;

# Per server
limit_req_zone $server_name zone=perserver:10m rate=1000r/s;

# ===== CONNECTION LIMITS =====
limit_conn_zone $binary_remote_addr zone=conn_per_ip:10m;
limit_conn_zone $server_name zone=conn_per_server:10m;

# ===== RATE LIMIT STATUS =====
limit_req_status 429;
limit_conn_status 429;

# ===== LOGGING FOR RATE LIMITS =====
limit_req_log_level warn;
limit_conn_log_level warn;
```

### 🚫 Block Attacks

```nginx
# /etc/nginx/conf.d/security.conf

# ============================================================
# CSRF PROTECTION (Cross-Site Request Forgery)
# ============================================================

# Map valid origins
map $http_origin $cors_origin {
    default "";
    "https://yourdomain.com" "$http_origin";
    "https://www.yourdomain.com" "$http_origin";
    "https://subdomain.yourdomain.com" "$http_origin";
}

# Map valid referers for CSRF check
map $http_referer $invalid_referer {
    default 1;
    "~^https?://(www\.)?yourdomain\.com" 0;
    "" 0;  # Allow empty referer for direct access
}

# Block CSRF on POST/PUT/DELETE requests
map "$request_method:$invalid_referer" $csrf_block {
    default 0;
    "POST:1" 1;
    "PUT:1" 1;
    "DELETE:1" 1;
    "PATCH:1" 1;
}

# ============================================================
# SQL INJECTION PROTECTION
# ============================================================

map $request_uri $sql_injection {
    default 0;
    # Basic SQL keywords
    ~*union.*select 1;
    ~*select.*from 1;
    ~*insert.*into 1;
    ~*drop.*(table|database|column) 1;
    ~*delete.*from 1;
    ~*update.*set 1;
    ~*create.*(table|database|function|procedure) 1;
    ~*alter.*(table|database) 1;
    ~*truncate.*table 1;
    # SQL comments and special chars
    ~*(\-\-|#|\/\*|\*\/) 1;
    ~*(\%27|\'|\%22|\") 1;
    # SQL functions
    ~*(benchmark|sleep|waitfor|delay)\s*\( 1;
    ~*(load_file|into\s+(out|dump)file) 1;
    ~*(information_schema|mysql\.|sys\.|performance_schema) 1;
    ~*(concat|group_concat|char|chr|ascii|hex|unhex|ord|conv)\s*\( 1;
    ~*(exec|execute)\s*(xp_|sp_|master\.) 1;
    # SQL injection techniques
    ~*(having|order\s+by|group\s+by)\s+[0-9] 1;
    ~*(\|\||&&|;) 1;
    # Encoded variants
    ~*(%00|%0a|%0d|%27|%3c|%3e) 1;
}

# Also check query string
map $args $sql_injection_args {
    default 0;
    ~*union.*select 1;
    ~*select.*from 1;
    ~*insert.*into 1;
    ~*drop.*(table|database) 1;
    ~*delete.*from 1;
    ~*update.*set 1;
    ~*(\-\-|#|\/\*) 1;
    ~*(benchmark|sleep|waitfor)\s*\( 1;
    ~*(load_file|into\s+outfile) 1;
    ~*(information_schema|mysql\.) 1;
    ~*(concat|char|ascii|hex)\s*\( 1;
    ~*(%27|\'|%22|\") 1;
}

# ============================================================
# RCE (Remote Code Execution) PROTECTION
# ============================================================

map $request_uri $rce_attack {
    default 0;
    # Command separators
    ~*(;|\||`|\$\(|\$\{|&&|\|\|) 1;
    ~*(%3B|%7C|%60|%24%28|%26%26) 1;
    # Shell commands
    ~*(/bin/(bash|sh|csh|ksh|zsh|dash)) 1;
    ~*(/usr/(bin|sbin|local)/) 1;
    # PHP dangerous functions
    ~*(eval|exec|shell_exec|system|passthru|popen|proc_open|pcntl_exec)\s*\( 1;
    ~*(base64_decode|gzinflate|gzuncompress|str_rot13)\s*\( 1;
    # Download tools
    ~*(wget|curl|fetch|lwp-download)\s+ 1;
    # Network tools (reverse shell)
    ~*(nc|netcat|ncat|telnet)\s+-[a-z] 1;
    # Script interpreters with flags
    ~*(python|perl|ruby|php|node|bash)\s+-[cre] 1;
}

map $args $rce_attack_args {
    default 0;
    ~*(;|\||`|\$\(|\$\{|&&|\|\||\n|\r) 1;
    ~*(cmd|command|exec|execute|run)= 1;
    ~*(eval|exec|shell_exec|system|passthru)\s*\( 1;
    ~*(/bin/(bash|sh|zsh)) 1;
    ~*(/etc/(passwd|shadow|hosts)) 1;
    ~*(/proc/(self|version|cmdline)) 1;
    ~*(wget|curl|fetch)\s+ 1;
    ~*(nc|netcat|ncat)\s+-[a-z] 1;
    ~*(bash\s+-i|/dev/(tcp|udp)) 1;
    ~*(mkfifo|mknod)\s+ 1;
    ~*(import\s+os|import\s+socket|import\s+subprocess) 1;
}

# ============================================================
# XSS (Cross-Site Scripting) PROTECTION
# ============================================================

map $request_uri $xss_attack {
    default 0;
    ~*<\s*script 1;
    ~*javascript: 1;
    ~*vbscript: 1;
    ~*on(error|load|click|mouse|focus|blur|change|submit|key)\s*= 1;
    ~*(document\.(cookie|location|write)|window\.(location|open)) 1;
    ~*(eval|alert|prompt|confirm)\s*\( 1;
    ~*(innerHTML|outerHTML|document\.write) 1;
    ~*(<|%3C)\s*(img|iframe|object|embed|svg|body|form|input|style|link|meta) 1;
}

map $args $xss_attack_args {
    default 0;
    ~*<\s*script 1;
    ~*(javascript|vbscript): 1;
    ~*on(error|load|click|mouse|focus|blur)\s*= 1;
    ~*(document\.(cookie|location|write)|window\.(location|open)) 1;
    ~*(eval|alert|prompt|confirm|atob|btoa)\s*\( 1;
    ~*(innerHTML|outerHTML) 1;
    ~*(<|%3C)\s*(img|iframe|object|embed|svg) 1;
    ~*(data:text/html|data:application/javascript) 1;
}

# ============================================================
# PATH TRAVERSAL / LFI PROTECTION
# ============================================================

map $request_uri $path_traversal {
    default 0;
    ~*\.\./ 1;
    ~*\.\.\\  1;
    ~*%2e%2e%2f 1;
    ~*%2e%2e/ 1;
    ~*/etc/(passwd|shadow|group|hosts) 1;
    ~*/proc/(self|version|cmdline) 1;
    ~*boot\.ini 1;
    ~*win\.ini 1;
}

map $args $path_traversal_args {
    default 0;
    ~*\.\./ 1;
    ~*\.\.\\  1;
    ~*%2e%2e 1;
    ~*(php|file|glob|data|expect|zip|phar):// 1;
    ~*(filter|input|resource):// 1;
    ~*/etc/(passwd|shadow) 1;
    ~*/proc/self 1;
}

# ============================================================
# SSRF (Server-Side Request Forgery) PROTECTION
# ============================================================

map $args $ssrf_attack {
    default 0;
    ~*(url|uri|path|link|src|href|redirect|fetch|proxy)=(http|https|ftp|file|gopher): 1;
    ~*(127\.0\.0\.1|localhost|0\.0\.0\.0|::1) 1;
    ~*(169\.254\.|10\.|172\.(1[6-9]|2[0-9]|3[01])\.|192\.168\.) 1;
    ~*(metadata\.google|169\.254\.169\.254) 1;
}

# ===== BLOCK BAD BOTS =====
map $http_user_agent $bad_bot {
    default 0;
    ~*nikto 1;
    ~*sqlmap 1;
    ~*nmap 1;
    ~*masscan 1;
    ~*wget 1;
    ~*curl 1;
    ~*libwww 1;
    ~*HTTrack 1;
    ~*harvest 1;
    ~*scan 1;
    ~*grab 1;
    ~*extract 1;
    ~*ZmEu 1;
    ~*Morfeus 1;
    ~*acunetix 1;
    ~*nessus 1;
    ~*burp 1;
    ~*dirbuster 1;
    ~*gobuster 1;
    ~*wfuzz 1;
    ~*ffuf 1;
}

# ===== BLOCK BAD REFERRERS =====
map $http_referer $bad_referer {
    default 0;
    ~*semalt 1;
    ~*buttons-for-website 1;
    ~*sharebutton 1;
    ~*social-buttons 1;
}

# ===== COMBINED SECURITY CHECK =====
# Use this in server block to check all attacks
map "$sql_injection:$sql_injection_args:$rce_attack:$rce_attack_args:$xss_attack:$xss_attack_args:$path_traversal:$path_traversal_args:$ssrf_attack" $security_violation {
    default 0;
    ~*1 1;
}

# ===== USE IN SERVER BLOCK =====
server {
    # ===== CSRF Protection =====
    # Block if invalid referer on state-changing methods
    if ($csrf_block) {
        return 403;
    }
    
    # Set CORS headers for allowed origins
    add_header Access-Control-Allow-Origin $cors_origin always;
    add_header Access-Control-Allow-Methods "GET, POST, OPTIONS" always;
    add_header Access-Control-Allow-Headers "Content-Type, X-Requested-With, X-CSRF-Token, Authorization" always;
    add_header Access-Control-Allow-Credentials "true" always;
    
    # Handle preflight requests
    if ($request_method = 'OPTIONS') {
        add_header Access-Control-Allow-Origin $cors_origin;
        add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
        add_header Access-Control-Allow-Headers "Content-Type, X-Requested-With, X-CSRF-Token, Authorization";
        add_header Access-Control-Max-Age 86400;
        add_header Content-Length 0;
        add_header Content-Type text/plain;
        return 204;
    }
    
    # ===== Block All Security Violations =====
    if ($security_violation) {
        return 403;
    }
    
    # Block bad bots
    if ($bad_bot) {
        return 403;
    }
    
    # Block bad referrers
    if ($bad_referer) {
        return 403;
    }
    
    # Block empty user agents
    if ($http_user_agent = "") {
        return 403;
    }
    
    # ===== Additional CSRF for specific endpoints =====
    location ~ ^/(admin|api|login|checkout|payment|transfer) {
        # Strict referer check for sensitive endpoints
        if ($invalid_referer) {
            return 403;
        }
        
        # Rate limiting for sensitive endpoints
        limit_req zone=strict burst=5 nodelay;
        
        # Additional security headers
        add_header X-Frame-Options "DENY" always;
        add_header Content-Security-Policy "frame-ancestors 'none'" always;
    }
    
    # ===== Protect form submission endpoints =====
    location ~ ^/(contact|register|subscribe|newsletter) {
        if ($request_method = POST) {
            set $csrf_check 1;
        }
        if ($invalid_referer) {
            set $csrf_check "${csrf_check}1";
        }
        if ($csrf_check = "11") {
            return 403;
        }
    }
}
```

### 🌍 GeoIP Blocking

```nginx
# /etc/nginx/conf.d/geoip.conf

# Install geoip module first:
# apt install libnginx-mod-http-geoip geoip-database

# Load GeoIP database
geoip_country /usr/share/GeoIP/GeoIP.dat;

# Map countries to block
map $geoip_country_code $blocked_country {
    default 0;
    CN 1;      # China
    RU 1;      # Russia
    KP 1;      # North Korea
    IR 1;      # Iran
}

# Use in server block
server {
    if ($blocked_country) {
        return 403;
    }
}
```

### 🔐 Authentication

```nginx
# Create password file
# htpasswd -c /etc/nginx/.htpasswd admin

# Basic authentication
location /admin/ {
    auth_basic "Restricted Area";
    auth_basic_user_file /etc/nginx/.htpasswd;
}

# Combine with IP whitelist
location /admin/ {
    satisfy all;
    
    allow 192.168.1.0/24;
    deny all;
    
    auth_basic "Admin Area";
    auth_basic_user_file /etc/nginx/.htpasswd;
}

# Or satisfy any (IP OR password)
location /admin/ {
    satisfy any;
    
    allow 192.168.1.0/24;
    deny all;
    
    auth_basic "Admin Area";
    auth_basic_user_file /etc/nginx/.htpasswd;
}
```

### 📊 Logging & Monitoring

```nginx
# /etc/nginx/conf.d/logging.conf

# Detailed log format
log_format detailed '$remote_addr - $remote_user [$time_local] '
                    '"$request" $status $body_bytes_sent '
                    '"$http_referer" "$http_user_agent" '
                    '$request_time $upstream_response_time '
                    '$geoip_country_code';

# Security log format
log_format security '$remote_addr [$time_local] '
                    '"$request" $status '
                    '"$http_user_agent" '
                    'Rate:$limit_req_status Conn:$limit_conn_status';

# JSON format for log analysis
log_format json escape=json '{'
    '"time":"$time_iso8601",'
    '"remote_addr":"$remote_addr",'
    '"request":"$request",'
    '"status":"$status",'
    '"body_bytes_sent":"$body_bytes_sent",'
    '"referer":"$http_referer",'
    '"user_agent":"$http_user_agent",'
    '"request_time":"$request_time",'
    '"upstream_response_time":"$upstream_response_time"'
'}';

# Use in server block
server {
    access_log /var/log/nginx/access.json json;
    error_log /var/log/nginx/error.log warn;
    
    # Separate security log
    access_log /var/log/nginx/security.log security;
}
```

## 📜 Complete Nginx Hardening Script

```bash
#!/bin/bash
# nginx-hardening.sh

# Backup original config
cp /etc/nginx/nginx.conf /etc/nginx/nginx.conf.backup

# Create security snippet
cat > /etc/nginx/snippets/security.conf << 'EOF'
# Security Headers
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Permissions-Policy "geolocation=(), microphone=(), camera=()" always;

# Block bad methods
if ($request_method !~ ^(GET|HEAD|POST)$) {
    return 405;
}

# Block bad user agents
if ($http_user_agent ~* (nikto|sqlmap|nmap|masscan|wget|curl)) {
    return 403;
}

# Block empty user agents
if ($http_user_agent = "") {
    return 403;
}
EOF

# Create rate limiting config
cat > /etc/nginx/conf.d/rate-limiting.conf << 'EOF'
limit_req_zone $binary_remote_addr zone=general:10m rate=10r/s;
limit_req_zone $binary_remote_addr zone=login:10m rate=1r/s;
limit_conn_zone $binary_remote_addr zone=conn_limit:10m;
limit_req_status 429;
limit_conn_status 429;
EOF

# Test configuration
nginx -t

# Reload nginx
systemctl reload nginx

echo "Nginx hardening complete!"
```

---

# 3. SSL/TLS Configuration

## Apache SSL

```apache
# /etc/apache2/sites-available/ssl.conf

<VirtualHost *:443>
    ServerName example.com
    DocumentRoot /var/www/html
    
    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/example.com/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/example.com/privkey.pem
    
    # Modern configuration
    SSLProtocol all -SSLv3 -TLSv1 -TLSv1.1
    SSLCipherSuite ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384
    SSLHonorCipherOrder off
    SSLSessionTickets off
    
    # OCSP Stapling
    SSLUseStapling on
    SSLStaplingResponderTimeout 5
    SSLStaplingReturnResponderErrors off
    
    # HSTS
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
</VirtualHost>

# OCSP Stapling Cache
SSLStaplingCache shmcb:/var/run/ocsp(128000)
```

## Nginx SSL

```nginx
# /etc/nginx/snippets/ssl-params.conf

# Session settings
ssl_session_timeout 1d;
ssl_session_cache shared:SSL:50m;
ssl_session_tickets off;

# Modern configuration
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
ssl_prefer_server_ciphers off;

# OCSP Stapling
ssl_stapling on;
ssl_stapling_verify on;
resolver 8.8.8.8 8.8.4.4 valid=300s;
resolver_timeout 5s;

# DH parameters (generate: openssl dhparam -out /etc/nginx/dhparam.pem 4096)
ssl_dhparam /etc/nginx/dhparam.pem;

# Use in server block
server {
    listen 443 ssl http2;
    include snippets/ssl-params.conf;
    
    ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;
    
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
}
```

---

# 4. Comparison & Quick Reference

## Feature Comparison

| Feature | Apache | Nginx |
|---------|--------|-------|
| **Config Style** | Distributed (.htaccess) | Centralized |
| **Performance** | Good | Excellent |
| **Memory Usage** | Higher | Lower |
| **Concurrent Connections** | Thread-based | Event-based |
| **Rate Limiting** | mod_evasive, mod_ratelimit | Built-in |
| **WAF** | ModSecurity | ModSecurity, NAXSI |
| **Static Files** | Good | Excellent |
| **Dynamic Content** | Excellent (mod_php) | Via FastCGI |
| **.htaccess Support** | Yes | No |
| **Learning Curve** | Easy | Moderate |

## Quick Reference

### Security Headers
```bash
# Apache
Header always set X-Frame-Options "SAMEORIGIN"
Header always set X-XSS-Protection "1; mode=block"
Header always set X-Content-Type-Options "nosniff"

# Nginx
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header X-Content-Type-Options "nosniff" always;
```

### Rate Limiting
```bash
# Apache (mod_evasive)
DOSPageCount 5
DOSSiteCount 100
DOSBlockingPeriod 10

# Nginx
limit_req_zone $binary_remote_addr zone=one:10m rate=10r/s;
limit_req zone=one burst=20 nodelay;
```

### Block IP
```bash
# Apache .htaccess
Deny from 1.2.3.4
Deny from 5.6.7.0/24

# Apache 2.4+
Require not ip 1.2.3.4

# Nginx
deny 1.2.3.4;
deny 5.6.7.0/24;
```

### Allow IP Only
```bash
# Apache
Require ip 192.168.1.0/24

# Nginx
allow 192.168.1.0/24;
deny all;
```

### Basic Auth
```bash
# Create password file
htpasswd -c /etc/.htpasswd admin

# Apache
AuthType Basic
AuthName "Restricted"
AuthUserFile /etc/.htpasswd
Require valid-user

# Nginx
auth_basic "Restricted";
auth_basic_user_file /etc/nginx/.htpasswd;
```

### Block Files
```bash
# Apache
<FilesMatch "\.(sql|bak|log)$">
    Require all denied
</FilesMatch>

# Nginx
location ~* \.(sql|bak|log)$ {
    deny all;
}
```

### Disable Directory Listing
```bash
# Apache
Options -Indexes

# Nginx
autoindex off;
```

---

## 🔗 Useful Commands

```bash
# Apache
apachectl configtest          # Test config
systemctl reload apache2      # Reload
a2enmod headers              # Enable module
a2ensite secure              # Enable site

# Nginx
nginx -t                     # Test config
systemctl reload nginx       # Reload
```

## 📚 Additional Resources

- [Apache Security Tips](https://httpd.apache.org/docs/current/misc/security_tips.html)
- [Nginx Security Controls](https://docs.nginx.com/nginx/admin-guide/security-controls/)
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/)
- [OWASP ModSecurity Core Rule Set](https://coreruleset.org/)

---

# 5. STRESS TEST & LOAD TESTING CHEATSHEET

## 🔥 Web Server Stress Testing Tools

> ⚠️ **WARNING**: Hanya gunakan tools ini untuk testing server MILIK SENDIRI atau dengan izin tertulis!

---

## 5.1 Apache Benchmark (ab)

### 🔧 Installation
```bash
# Debian/Ubuntu
apt install apache2-utils

# RHEL/CentOS
yum install httpd-tools

# macOS
brew install httpd
```

### 📋 Basic Commands

```bash
# Basic test - 1000 requests, 10 concurrent
ab -n 1000 -c 10 http://example.com/

# With keep-alive
ab -n 1000 -c 100 -k http://example.com/

# POST request with data
ab -n 1000 -c 50 -p post_data.txt -T "application/x-www-form-urlencoded" http://example.com/login

# POST with JSON
ab -n 1000 -c 50 -p data.json -T "application/json" http://example.com/api/

# With custom headers
ab -n 1000 -c 50 -H "Authorization: Bearer token123" http://example.com/api/

# With cookies
ab -n 1000 -c 50 -C "session=abc123" http://example.com/

# HTTPS test
ab -n 1000 -c 50 https://example.com/

# Timeout setting (seconds)
ab -n 1000 -c 50 -s 30 http://example.com/

# Output to CSV
ab -n 1000 -c 50 -e results.csv http://example.com/

# Verbose output
ab -n 1000 -c 50 -v 2 http://example.com/
```

### 📊 Stress Test Scenarios

```bash
# Light load test
ab -n 5000 -c 50 -k http://example.com/

# Medium load test
ab -n 10000 -c 100 -k http://example.com/

# Heavy load test
ab -n 50000 -c 500 -k http://example.com/

# Extreme load test (DDoS simulation)
ab -n 100000 -c 1000 -k http://example.com/

# Login bruteforce simulation
ab -n 10000 -c 100 -p login.txt -T "application/x-www-form-urlencoded" http://example.com/login

# API stress test
ab -n 20000 -c 200 -k -H "Content-Type: application/json" http://example.com/api/users

# Test rate limiting
ab -n 1000 -c 500 -k http://example.com/api/
```

### 📝 Create POST Data Files

```bash
# login.txt (form data)
echo "username=admin&password=password123" > login.txt

# data.json (JSON)
echo '{"username":"admin","password":"password123"}' > data.json

# Multi-line POST data
cat > post_data.txt << 'EOF'
name=John&email=john@example.com&message=Hello+World
EOF
```

---

## 5.2 wrk - Modern HTTP Benchmarking

### 🔧 Installation
```bash
# Debian/Ubuntu
apt install wrk

# From source
git clone https://github.com/wg/wrk.git
cd wrk && make
sudo cp wrk /usr/local/bin/

# macOS
brew install wrk
```

### 📋 Basic Commands

```bash
# Basic test - 12 threads, 400 connections, 30 seconds
wrk -t12 -c400 -d30s http://example.com/

# Simple test
wrk -t4 -c100 -d10s http://example.com/

# With timeout
wrk -t8 -c200 -d30s --timeout 10s http://example.com/

# With latency statistics
wrk -t12 -c400 -d30s --latency http://example.com/

# HTTPS test
wrk -t8 -c200 -d30s https://example.com/
```

### 📊 Stress Test Scenarios

```bash
# Light load
wrk -t2 -c50 -d30s http://example.com/

# Medium load
wrk -t4 -c200 -d60s http://example.com/

# Heavy load
wrk -t8 -c500 -d60s http://example.com/

# Extreme load
wrk -t12 -c1000 -d120s http://example.com/

# Maximum connections test
wrk -t16 -c2000 -d60s --latency http://example.com/
```

### 📜 Lua Scripts for Advanced Testing

```bash
# Create POST script
cat > post.lua << 'EOF'
wrk.method = "POST"
wrk.body   = "username=admin&password=password123"
wrk.headers["Content-Type"] = "application/x-www-form-urlencoded"
EOF

# Use POST script
wrk -t4 -c100 -d30s -s post.lua http://example.com/login

# JSON POST script
cat > json_post.lua << 'EOF'
wrk.method = "POST"
wrk.body   = '{"username":"admin","password":"password123"}'
wrk.headers["Content-Type"] = "application/json"
EOF

wrk -t4 -c100 -d30s -s json_post.lua http://example.com/api/login

# Random data script
cat > random.lua << 'EOF'
request = function()
    local user_id = math.random(1, 10000)
    local path = "/api/users/" .. user_id
    return wrk.format("GET", path)
end
EOF

wrk -t4 -c100 -d30s -s random.lua http://example.com/

# Custom headers script
cat > headers.lua << 'EOF'
wrk.headers["Authorization"] = "Bearer your_token_here"
wrk.headers["X-Custom-Header"] = "CustomValue"
EOF

wrk -t4 -c100 -d30s -s headers.lua http://example.com/api/

# Bruteforce simulation script
cat > bruteforce.lua << 'EOF'
passwords = {"password", "123456", "admin", "root", "letmein", "qwerty", "password123"}
counter = 0

request = function()
    counter = counter + 1
    local idx = (counter % #passwords) + 1
    local body = "username=admin&password=" .. passwords[idx]
    return wrk.format("POST", "/login", {["Content-Type"] = "application/x-www-form-urlencoded"}, body)
end

response = function(status, headers, body)
    if status == 200 and string.find(body, "success") then
        print("Found valid password!")
    end
end
EOF

wrk -t4 -c50 -d60s -s bruteforce.lua http://example.com/
```

---

## 5.3 Siege - HTTP Load Testing

### 🔧 Installation
```bash
# Debian/Ubuntu
apt install siege

# RHEL/CentOS
yum install siege

# macOS
brew install siege

# From source
wget http://download.joedog.org/siege/siege-latest.tar.gz
tar -xzf siege-latest.tar.gz
cd siege-* && ./configure && make && make install
```

### 📋 Basic Commands

```bash
# Basic test - 25 concurrent users
siege -c25 http://example.com/

# Timed test - 60 seconds
siege -c50 -t60s http://example.com/

# Repetitions instead of time
siege -c50 -r100 http://example.com/

# With delay between requests (milliseconds)
siege -c25 -t60s -d1 http://example.com/

# Benchmark mode (no delay)
siege -c100 -t60s -b http://example.com/

# HTTPS
siege -c50 -t30s https://example.com/

# With custom User-Agent
siege -c50 -t30s -A "Mozilla/5.0 (Test)" http://example.com/

# With custom header
siege -c50 -t30s -H "Authorization: Bearer token" http://example.com/

# POST request
siege -c50 -t30s "http://example.com/login POST username=admin&password=test"

# JSON POST
siege -c50 -t30s -H "Content-Type: application/json" "http://example.com/api POST {\"user\":\"admin\"}"

# Verbose output
siege -c25 -t30s -v http://example.com/

# Log to file
siege -c50 -t60s --log=/var/log/siege.log http://example.com/
```

### 📊 Stress Test Scenarios

```bash
# Light load
siege -c10 -t60s -b http://example.com/

# Medium load
siege -c50 -t120s -b http://example.com/

# Heavy load
siege -c200 -t180s -b http://example.com/

# Extreme load
siege -c500 -t300s -b http://example.com/
```

### 📜 URL File Testing

```bash
# Create URLs file
cat > urls.txt << 'EOF'
http://example.com/
http://example.com/about
http://example.com/contact
http://example.com/products
http://example.com/api/users
http://example.com/login POST username=test&password=test
EOF

# Test multiple URLs
siege -c50 -t60s -f urls.txt

# Random URL selection
siege -c50 -t60s -i -f urls.txt
```

---

## 5.4 hey - HTTP Load Generator

### 🔧 Installation
```bash
# Go install
go install github.com/rakyll/hey@latest

# Download binary
wget https://hey-release.s3.us-east-2.amazonaws.com/hey_linux_amd64
chmod +x hey_linux_amd64
sudo mv hey_linux_amd64 /usr/local/bin/hey

# macOS
brew install hey
```

### 📋 Basic Commands

```bash
# Basic test - 200 requests, 50 concurrent
hey -n 200 -c 50 http://example.com/

# Duration based - 30 seconds
hey -z 30s -c 50 http://example.com/

# With rate limit (QPS)
hey -n 1000 -c 50 -q 100 http://example.com/

# POST request
hey -n 1000 -c 50 -m POST -d "username=admin&password=test" http://example.com/login

# JSON POST
hey -n 1000 -c 50 -m POST -H "Content-Type: application/json" -d '{"user":"admin"}' http://example.com/api/

# With headers
hey -n 1000 -c 50 -H "Authorization: Bearer token" http://example.com/api/

# Custom timeout
hey -n 1000 -c 50 -t 30 http://example.com/

# Disable keepalive
hey -n 1000 -c 50 --disable-keepalive http://example.com/

# HTTP/2
hey -n 1000 -c 50 -h2 https://example.com/

# Output as CSV
hey -n 1000 -c 50 -o csv http://example.com/

# CPU profiling
hey -n 1000 -c 50 --cpus 4 http://example.com/
```

### 📊 Stress Test Scenarios

```bash
# Quick test
hey -z 10s -c 50 http://example.com/

# Standard test
hey -z 60s -c 100 http://example.com/

# Heavy test
hey -z 120s -c 500 http://example.com/

# Sustained load
hey -z 300s -c 200 -q 1000 http://example.com/
```

---

## 5.5 Vegeta - HTTP Load Testing Tool

### 🔧 Installation
```bash
# Go install
go install github.com/tsenart/vegeta@latest

# Download binary
wget https://github.com/tsenart/vegeta/releases/download/v12.11.1/vegeta_12.11.1_linux_amd64.tar.gz
tar -xzf vegeta_12.11.1_linux_amd64.tar.gz
sudo mv vegeta /usr/local/bin/

# macOS
brew install vegeta
```

### 📋 Basic Commands

```bash
# Basic attack - 50 requests/sec for 10 seconds
echo "GET http://example.com/" | vegeta attack -duration=10s -rate=50 | vegeta report

# Custom rate
echo "GET http://example.com/" | vegeta attack -duration=30s -rate=100/s | vegeta report

# POST request
echo "POST http://example.com/login" | vegeta attack -duration=30s -rate=50 -body='{"user":"admin","pass":"test"}' -header="Content-Type: application/json" | vegeta report

# Multiple targets
cat > targets.txt << 'EOF'
GET http://example.com/
GET http://example.com/api/users
POST http://example.com/login
Content-Type: application/json
@login.json
EOF
vegeta attack -duration=30s -rate=100 -targets=targets.txt | vegeta report

# With headers
echo "GET http://example.com/api/" | vegeta attack -duration=30s -rate=50 -header="Authorization: Bearer token" | vegeta report

# Save results
echo "GET http://example.com/" | vegeta attack -duration=60s -rate=100 > results.bin
vegeta report results.bin
vegeta report -type=json results.bin

# Plot results
vegeta plot results.bin > plot.html

# Histogram
vegeta report -type=hist[0,10ms,50ms,100ms,500ms,1s] results.bin

# Encode results
vegeta encode results.bin | vegeta report -type=json
```

### 📊 Stress Test Scenarios

```bash
# Light load
echo "GET http://example.com/" | vegeta attack -duration=60s -rate=10 | vegeta report

# Medium load
echo "GET http://example.com/" | vegeta attack -duration=120s -rate=100 | vegeta report

# Heavy load
echo "GET http://example.com/" | vegeta attack -duration=180s -rate=500 | vegeta report

# Ramp up test
for rate in 10 50 100 200 500; do
    echo "Testing at $rate req/s"
    echo "GET http://example.com/" | vegeta attack -duration=30s -rate=$rate | vegeta report
    sleep 5
done
```

---

## 5.6 k6 - Modern Load Testing

### 🔧 Installation
```bash
# Debian/Ubuntu
sudo gpg -k
sudo gpg --no-default-keyring --keyring /usr/share/keyrings/k6-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D69
echo "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main" | sudo tee /etc/apt/sources.list.d/k6.list
sudo apt update && sudo apt install k6

# macOS
brew install k6

# Docker
docker run --rm -i grafana/k6 run - <script.js
```

### 📜 k6 Scripts

```javascript
// basic-test.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    vus: 50,           // Virtual Users
    duration: '30s',   // Duration
};

export default function () {
    const res = http.get('http://example.com/');
    check(res, {
        'status is 200': (r) => r.status === 200,
        'response time < 500ms': (r) => r.timings.duration < 500,
    });
    sleep(1);
}
```

```javascript
// stress-test.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
    stages: [
        { duration: '2m', target: 100 },   // Ramp up
        { duration: '5m', target: 100 },   // Stay at 100
        { duration: '2m', target: 200 },   // Ramp up more
        { duration: '5m', target: 200 },   // Stay at 200
        { duration: '2m', target: 0 },     // Ramp down
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'],  // 95% requests < 500ms
        http_req_failed: ['rate<0.01'],    // Error rate < 1%
    },
};

export default function () {
    const res = http.get('http://example.com/');
    check(res, {
        'status is 200': (r) => r.status === 200,
    });
    sleep(1);
}
```

```javascript
// bruteforce-test.js
import http from 'k6/http';
import { check } from 'k6';

export const options = {
    vus: 50,
    duration: '60s',
};

const passwords = ['password', '123456', 'admin', 'root', 'letmein', 'qwerty'];
let counter = 0;

export default function () {
    const password = passwords[counter % passwords.length];
    counter++;
    
    const payload = JSON.stringify({
        username: 'admin',
        password: password,
    });
    
    const params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };
    
    const res = http.post('http://example.com/api/login', payload, params);
    check(res, {
        'login blocked or failed': (r) => r.status === 429 || r.status === 401,
    });
}
```

```javascript
// api-test.js
import http from 'k6/http';
import { check, group, sleep } from 'k6';

export const options = {
    vus: 100,
    duration: '5m',
};

const BASE_URL = 'http://example.com/api';

export default function () {
    group('API Tests', function () {
        // GET users
        let res = http.get(`${BASE_URL}/users`);
        check(res, {
            'GET users status 200': (r) => r.status === 200,
        });
        
        // POST create user
        const payload = JSON.stringify({
            name: 'Test User',
            email: `user${__VU}@test.com`,
        });
        
        res = http.post(`${BASE_URL}/users`, payload, {
            headers: { 'Content-Type': 'application/json' },
        });
        check(res, {
            'POST user status 201': (r) => r.status === 201,
        });
        
        sleep(1);
    });
}
```

### 📋 Run k6 Tests

```bash
# Run basic test
k6 run basic-test.js

# With more VUs
k6 run --vus 100 --duration 60s basic-test.js

# Output to JSON
k6 run --out json=results.json basic-test.js

# Cloud run (k6 Cloud)
k6 cloud basic-test.js

# With environment variables
k6 run -e BASE_URL=http://example.com basic-test.js
```

---

## 5.7 slowhttptest - Slow HTTP Attack Testing

### 🔧 Installation
```bash
# Debian/Ubuntu
apt install slowhttptest

# From source
git clone https://github.com/shekyan/slowhttptest.git
cd slowhttptest && ./configure && make && make install

# macOS
brew install slowhttptest
```

### 📋 Attack Modes

```bash
# Slowloris attack (slow headers)
slowhttptest -c 1000 -H -g -o slowloris -i 10 -r 200 -t GET -u http://example.com/ -x 24 -p 3

# Slow POST attack (slow body)
slowhttptest -c 1000 -B -g -o slowpost -i 110 -r 200 -s 8192 -t POST -u http://example.com/login -x 10 -p 3

# Slow Read attack
slowhttptest -c 1000 -X -g -o slowread -r 200 -w 512 -y 1024 -n 5 -z 32 -k 3 -u http://example.com/ -p 3

# Range attack
slowhttptest -c 1000 -R -g -o range -r 200 -u http://example.com/bigfile.zip -p 3
```

### 📊 Parameters Explained

```bash
# Common parameters:
# -c : Number of connections
# -H : Slowloris mode
# -B : Slow POST mode
# -X : Slow Read mode
# -R : Range attack mode
# -g : Generate statistics in CSV/HTML
# -o : Output file prefix
# -i : Interval between follow-up data (seconds)
# -r : Connection rate (per second)
# -t : Request type (GET/POST)
# -u : Target URL
# -x : Max length of follow-up data
# -p : Timeout for probe connection
# -s : Content-Length header value
# -w : Range for advertised window size
# -y : Range for TCP window size
# -n : Interval between read operations
# -z : Bytes to read per operation

# Test Slowloris protection
slowhttptest -c 500 -H -i 10 -r 100 -t GET -u http://example.com/ -x 24 -p 5 -g -o test_slowloris

# Test Slow POST protection
slowhttptest -c 500 -B -i 110 -r 100 -s 65536 -t POST -u http://example.com/upload -x 10 -p 5 -g -o test_slowpost
```

---

## 5.8 hping3 - TCP/IP Packet Assembler

### 🔧 Installation
```bash
# Debian/Ubuntu
apt install hping3

# RHEL/CentOS
yum install hping3
```

### 📋 Attack Simulation

```bash
# SYN Flood test
hping3 -S --flood -V -p 80 example.com

# SYN Flood with random source
hping3 -S --flood --rand-source -p 80 example.com

# UDP Flood
hping3 --udp --flood -p 53 example.com

# ICMP Flood
hping3 --icmp --flood example.com

# Specific packet count
hping3 -S -c 10000 -p 80 example.com

# With specific rate
hping3 -S -i u10000 -p 80 example.com  # 100 packets/sec

# TCP ACK flood
hping3 -A --flood -p 80 example.com

# TCP RST flood
hping3 -R --flood -p 80 example.com

# FIN flood
hping3 -F --flood -p 80 example.com

# XMAS scan/flood
hping3 -FPU --flood -p 80 example.com

# Land attack simulation
hping3 -S -a TARGET_IP -p 80 TARGET_IP

# Smurf attack simulation
hping3 --icmp -a TARGET_IP BROADCAST_IP
```

### 📊 Parameters

```bash
# -S : Set SYN flag
# -A : Set ACK flag
# -R : Set RST flag
# -F : Set FIN flag
# -P : Set PSH flag
# -U : Set URG flag
# --flood : Send packets as fast as possible
# -V : Verbose
# -p : Destination port
# -c : Packet count
# -i : Interval (u = microseconds)
# --rand-source : Random source IP
# -a : Spoofed source IP
# --udp : UDP mode
# --icmp : ICMP mode
```

---

## 5.9 bombardier - Fast HTTP Benchmarking

### 🔧 Installation
```bash
# Go install
go install github.com/codesenberg/bombardier@latest

# Download binary
wget https://github.com/codesenberg/bombardier/releases/download/v1.2.6/bombardier-linux-amd64
chmod +x bombardier-linux-amd64
sudo mv bombardier-linux-amd64 /usr/local/bin/bombardier
```

### 📋 Basic Commands

```bash
# Basic test - 125 connections, 10 seconds
bombardier -c 125 -d 10s http://example.com/

# High connections
bombardier -c 500 -d 60s http://example.com/

# Requests per second limit
bombardier -c 100 -d 30s -r 1000 http://example.com/

# Total requests
bombardier -c 100 -n 10000 http://example.com/

# POST request
bombardier -c 100 -d 30s -m POST -b '{"user":"admin"}' -H "Content-Type: application/json" http://example.com/api/

# With headers
bombardier -c 100 -d 30s -H "Authorization: Bearer token" http://example.com/api/

# HTTP/2
bombardier -c 100 -d 30s --http2 https://example.com/

# Latency distribution
bombardier -c 100 -d 30s --latencies http://example.com/

# Print progress
bombardier -c 100 -d 60s --print=p http://example.com/

# Output format (json, plain-text)
bombardier -c 100 -d 30s -o json http://example.com/
```

---

## 5.10 Locust - Python Load Testing

### 🔧 Installation
```bash
pip install locust
```

### 📜 Locust Scripts

```python
# locustfile.py
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)
    
    @task(3)
    def index(self):
        self.client.get("/")
    
    @task(2)
    def about(self):
        self.client.get("/about")
    
    @task(1)
    def api_users(self):
        self.client.get("/api/users")
```

```python
# bruteforce_test.py
from locust import HttpUser, task, constant
import random

class BruteforceUser(HttpUser):
    wait_time = constant(0)  # No wait time
    
    passwords = ["password", "123456", "admin", "root", "letmein", "qwerty", "password123"]
    
    @task
    def login_attempt(self):
        password = random.choice(self.passwords)
        self.client.post("/login", {
            "username": "admin",
            "password": password
        })
```

```python
# api_test.py
from locust import HttpUser, task, between
import json

class APIUser(HttpUser):
    wait_time = between(0.5, 2)
    
    def on_start(self):
        # Login and get token
        response = self.client.post("/api/login", json={
            "username": "test",
            "password": "test123"
        })
        self.token = response.json().get("token", "")
    
    @task(5)
    def get_users(self):
        self.client.get("/api/users", headers={
            "Authorization": f"Bearer {self.token}"
        })
    
    @task(3)
    def create_user(self):
        self.client.post("/api/users", 
            json={"name": "Test", "email": "test@test.com"},
            headers={
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json"
            }
        )
    
    @task(1)
    def delete_user(self):
        user_id = random.randint(1, 1000)
        self.client.delete(f"/api/users/{user_id}", headers={
            "Authorization": f"Bearer {self.token}"
        })
```

### 📋 Run Locust

```bash
# Web UI mode
locust -f locustfile.py --host=http://example.com

# Headless mode
locust -f locustfile.py --host=http://example.com --headless -u 100 -r 10 -t 60s

# Parameters:
# -u : Number of users
# -r : Spawn rate (users per second)
# -t : Run time
# --headless : No web UI

# Distributed mode (master)
locust -f locustfile.py --master

# Distributed mode (worker)
locust -f locustfile.py --worker --master-host=MASTER_IP
```

---

## 5.11 curl-based Testing

### 📋 Simple Stress Testing with curl

```bash
# Basic loop test
for i in {1..1000}; do curl -s -o /dev/null -w "%{http_code}\n" http://example.com/; done

# Parallel requests with xargs
seq 1 100 | xargs -P 10 -I {} curl -s -o /dev/null -w "%{http_code}\n" http://example.com/

# With GNU parallel
parallel -j 50 curl -s -o /dev/null -w "%{http_code}\n" http://example.com/ ::: {1..1000}

# Time measurement
time (for i in {1..100}; do curl -s -o /dev/null http://example.com/; done)

# POST bruteforce simulation
for pass in password 123456 admin root; do
    curl -s -X POST -d "username=admin&password=$pass" http://example.com/login
done

# Rate limited requests
for i in {1..100}; do
    curl -s -o /dev/null http://example.com/
    sleep 0.1
done

# With response time
curl -w "Time: %{time_total}s\n" -o /dev/null -s http://example.com/
```

### 📜 Bash Stress Test Script

```bash
#!/bin/bash
# stress-test.sh

URL="${1:-http://example.com/}"
CONNECTIONS="${2:-100}"
REQUESTS="${3:-1000}"

echo "Stress Testing: $URL"
echo "Connections: $CONNECTIONS"
echo "Total Requests: $REQUESTS"
echo "---"

START=$(date +%s.%N)

# Run parallel requests
seq 1 $REQUESTS | xargs -P $CONNECTIONS -I {} sh -c \
    'curl -s -o /dev/null -w "%{http_code} %{time_total}\n" '"$URL"

END=$(date +%s.%N)
DURATION=$(echo "$END - $START" | bc)

echo "---"
echo "Total time: ${DURATION}s"
echo "Requests per second: $(echo "$REQUESTS / $DURATION" | bc)"
```

---

## 📊 Quick Reference - Stress Test Commands

| Tool | Light Load | Medium Load | Heavy Load | Extreme |
|------|-----------|-------------|------------|---------|
| **ab** | `-n 5000 -c 50` | `-n 10000 -c 100` | `-n 50000 -c 500` | `-n 100000 -c 1000` |
| **wrk** | `-t2 -c50 -d30s` | `-t4 -c200 -d60s` | `-t8 -c500 -d60s` | `-t12 -c1000 -d120s` |
| **siege** | `-c10 -t60s` | `-c50 -t120s` | `-c200 -t180s` | `-c500 -t300s` |
| **hey** | `-z 10s -c 50` | `-z 60s -c 100` | `-z 120s -c 500` | `-z 300s -c 1000` |
| **vegeta** | `-rate=10 -duration=60s` | `-rate=100 -duration=120s` | `-rate=500 -duration=180s` | `-rate=1000 -duration=300s` |
| **bombardier** | `-c 50 -d 30s` | `-c 200 -d 60s` | `-c 500 -d 120s` | `-c 1000 -d 300s` |

## 🎯 Test Rate Limiting Effectiveness

```bash
# Test if rate limiting is working
for i in {1..100}; do
    response=$(curl -s -o /dev/null -w "%{http_code}" http://example.com/api/)
    echo "Request $i: $response"
    if [ "$response" == "429" ]; then
        echo "Rate limit hit at request $i!"
        break
    fi
done

# Measure requests before rate limit
count=0
while true; do
    response=$(curl -s -o /dev/null -w "%{http_code}" http://example.com/)
    count=$((count + 1))
    if [ "$response" == "429" ]; then
        echo "Rate limited after $count requests"
        break
    fi
done
```

---

# 6. DOCKER COMMAND CHEATSHEET

## 📋 Table of Contents - Docker
- [Installation](#docker-installation)
- [Container Management](#container-management)
- [Image Management](#image-management)
- [Network Management](#network-management)
- [Volume Management](#volume-management)
- [Docker Compose](#docker-compose)
- [Dockerfile Reference](#dockerfile-reference)
- [Docker Swarm](#docker-swarm)
- [Security & Hardening](#docker-security--hardening)
- [Troubleshooting](#docker-troubleshooting)

---

## 🔧 DOCKER INSTALLATION

### Ubuntu/Debian
```bash
# Remove old versions
sudo apt remove docker docker-engine docker.io containerd runc

# Install prerequisites
sudo apt update
sudo apt install -y ca-certificates curl gnupg lsb-release

# Add Docker GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Add Docker repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Start and enable
sudo systemctl start docker
sudo systemctl enable docker

# Add user to docker group (logout required)
sudo usermod -aG docker $USER

# Verify installation
docker --version
docker compose version
```

### RHEL/CentOS/Rocky
```bash
# Remove old versions
sudo yum remove docker docker-client docker-client-latest docker-common \
    docker-latest docker-latest-logrotate docker-logrotate docker-engine

# Install prerequisites
sudo yum install -y yum-utils

# Add Docker repository
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

# Install Docker
sudo yum install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Start and enable
sudo systemctl start docker
sudo systemctl enable docker

# Add user to docker group
sudo usermod -aG docker $USER
```

### Windows (WSL2)
```powershell
# Install Docker Desktop
# Download from: https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe

# Or via winget
winget install Docker.DockerDesktop

# Enable WSL2 backend in Docker Desktop settings
```

---

## 📦 CONTAINER MANAGEMENT

### Basic Container Commands
```bash
# ===== RUN CONTAINERS =====
# Basic run
docker run IMAGE

# Run with name
docker run --name CONTAINER_NAME IMAGE

# Run in background (detached)
docker run -d IMAGE

# Run interactive with TTY
docker run -it IMAGE /bin/bash

# Run and remove after exit
docker run --rm IMAGE

# Run with port mapping
docker run -p HOST_PORT:CONTAINER_PORT IMAGE
docker run -p 8080:80 nginx

# Run with environment variables
docker run -e VAR=value IMAGE
docker run -e MYSQL_ROOT_PASSWORD=secret mysql

# Run with volume mount
docker run -v HOST_PATH:CONTAINER_PATH IMAGE
docker run -v /data:/app/data nginx

# Run with resource limits
docker run --memory=512m --cpus=1 IMAGE

# Run with restart policy
docker run --restart=always IMAGE
docker run --restart=unless-stopped IMAGE
docker run --restart=on-failure:5 IMAGE

# Run with network
docker run --network=NETWORK_NAME IMAGE

# Run with hostname
docker run --hostname=myhost IMAGE

# Complete example
docker run -d \
    --name web \
    -p 80:80 \
    -p 443:443 \
    -v /var/www:/usr/share/nginx/html:ro \
    -v /var/log/nginx:/var/log/nginx \
    -e TZ=Asia/Jakarta \
    --restart=unless-stopped \
    --memory=256m \
    --cpus=0.5 \
    nginx:alpine
```

### Container Lifecycle
```bash
# ===== START/STOP/RESTART =====
docker start CONTAINER
docker stop CONTAINER
docker restart CONTAINER

# Stop with timeout (seconds)
docker stop -t 30 CONTAINER

# Force stop (SIGKILL)
docker kill CONTAINER

# Pause/Unpause
docker pause CONTAINER
docker unpause CONTAINER

# ===== LIST CONTAINERS =====
# Running containers
docker ps

# All containers (including stopped)
docker ps -a

# Only container IDs
docker ps -q

# Latest created container
docker ps -l

# Filter containers
docker ps -f "status=exited"
docker ps -f "name=web"
docker ps -f "ancestor=nginx"

# Format output
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
docker ps --format "{{.ID}}: {{.Names}}"

# ===== REMOVE CONTAINERS =====
# Remove stopped container
docker rm CONTAINER

# Force remove running container
docker rm -f CONTAINER

# Remove all stopped containers
docker container prune
docker rm $(docker ps -aq -f "status=exited")

# Remove all containers
docker rm -f $(docker ps -aq)
```

### Container Inspection
```bash
# ===== INSPECT =====
# Full inspection (JSON)
docker inspect CONTAINER

# Get specific field
docker inspect -f '{{.State.Status}}' CONTAINER
docker inspect -f '{{.NetworkSettings.IPAddress}}' CONTAINER
docker inspect -f '{{.Config.Env}}' CONTAINER
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' CONTAINER

# ===== LOGS =====
# View logs
docker logs CONTAINER

# Follow logs (live)
docker logs -f CONTAINER

# Last N lines
docker logs --tail 100 CONTAINER

# With timestamps
docker logs -t CONTAINER

# Since time
docker logs --since 2h CONTAINER
docker logs --since "2026-01-14T10:00:00" CONTAINER

# Combined
docker logs -f --tail 50 -t CONTAINER

# ===== STATS =====
# Live resource usage
docker stats

# Specific container
docker stats CONTAINER

# No stream (snapshot)
docker stats --no-stream

# Format output
docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"

# ===== TOP =====
# Running processes in container
docker top CONTAINER
docker top CONTAINER aux
```

### Container Interaction
```bash
# ===== EXEC =====
# Run command in container
docker exec CONTAINER COMMAND
docker exec web ls -la

# Interactive shell
docker exec -it CONTAINER /bin/bash
docker exec -it CONTAINER /bin/sh

# As specific user
docker exec -u root CONTAINER whoami
docker exec -u 1000:1000 CONTAINER id

# With environment variable
docker exec -e VAR=value CONTAINER printenv VAR

# Working directory
docker exec -w /app CONTAINER pwd

# ===== ATTACH =====
# Attach to running container
docker attach CONTAINER
# Detach: Ctrl+P, Ctrl+Q

# ===== COPY =====
# Copy file to container
docker cp file.txt CONTAINER:/path/to/destination/

# Copy from container
docker cp CONTAINER:/path/to/file.txt ./local/

# Copy directory
docker cp ./mydir CONTAINER:/app/
docker cp CONTAINER:/app/logs ./backup/

# ===== DIFF =====
# Show filesystem changes
docker diff CONTAINER
# A = Added, C = Changed, D = Deleted

# ===== COMMIT =====
# Create image from container
docker commit CONTAINER new_image:tag
docker commit -m "Added config" -a "Author" CONTAINER myimage:v1

# ===== EXPORT/IMPORT =====
# Export container filesystem
docker export CONTAINER > container.tar
docker export CONTAINER -o container.tar

# Import as image
docker import container.tar myimage:latest
cat container.tar | docker import - myimage:latest
```

### Container Health
```bash
# ===== HEALTH CHECK =====
# Run with health check
docker run -d \
    --health-cmd="curl -f http://localhost/ || exit 1" \
    --health-interval=30s \
    --health-timeout=10s \
    --health-retries=3 \
    --health-start-period=40s \
    nginx

# Check health status
docker inspect --format='{{.State.Health.Status}}' CONTAINER
docker inspect --format='{{json .State.Health}}' CONTAINER | jq

# ===== WAIT =====
# Wait for container to stop
docker wait CONTAINER
```

---

## 🖼️ IMAGE MANAGEMENT

### Basic Image Commands
```bash
# ===== PULL IMAGES =====
docker pull IMAGE
docker pull nginx
docker pull nginx:alpine
docker pull nginx:1.25.3
docker pull mysql:8.0

# Pull from different registry
docker pull gcr.io/project/image:tag
docker pull ghcr.io/owner/image:tag

# Pull all tags
docker pull -a nginx

# ===== LIST IMAGES =====
docker images
docker image ls

# With specific name
docker images nginx

# All images (including intermediate)
docker images -a

# Only IDs
docker images -q

# Filter
docker images -f "dangling=true"
docker images -f "reference=nginx*"

# Format
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"

# ===== SEARCH IMAGES =====
docker search nginx
docker search --limit 5 nginx
docker search -f "is-official=true" nginx
docker search -f "stars=100" nginx

# ===== REMOVE IMAGES =====
docker rmi IMAGE
docker rmi nginx:latest
docker rmi IMAGE_ID

# Force remove
docker rmi -f IMAGE

# Remove unused images
docker image prune

# Remove ALL unused images
docker image prune -a

# Remove images older than 24h
docker image prune -a --filter "until=24h"

# Remove all images
docker rmi $(docker images -q)
```

### Building Images
```bash
# ===== BUILD =====
# Build from Dockerfile in current directory
docker build .

# Build with tag
docker build -t myimage:latest .
docker build -t myimage:v1.0 .

# Build with multiple tags
docker build -t myimage:latest -t myimage:v1.0 .

# Build from specific Dockerfile
docker build -f Dockerfile.prod .
docker build -f docker/Dockerfile.dev .

# Build with build arguments
docker build --build-arg VERSION=1.0 .
docker build --build-arg HTTP_PROXY=http://proxy:8080 .

# Build without cache
docker build --no-cache .

# Build with target stage
docker build --target production .

# Build and squash layers
docker build --squash .

# Build with platform
docker build --platform linux/amd64 .
docker build --platform linux/arm64 .

# Complete example
docker build \
    -t myapp:latest \
    -t myapp:v1.0 \
    -f Dockerfile.prod \
    --build-arg APP_VERSION=1.0 \
    --build-arg BUILD_DATE=$(date -u +"%Y-%m-%dT%H:%M:%SZ") \
    --no-cache \
    .

# ===== BUILDX (Multi-platform) =====
# Create builder
docker buildx create --name mybuilder --use

# Build multi-platform
docker buildx build --platform linux/amd64,linux/arm64 -t myimage:latest .

# Build and push
docker buildx build --platform linux/amd64,linux/arm64 -t user/myimage:latest --push .

# ===== TAG =====
docker tag SOURCE_IMAGE TARGET_IMAGE
docker tag myimage:latest myimage:v1.0
docker tag myimage:latest registry.example.com/myimage:latest

# ===== PUSH =====
# Login to registry
docker login
docker login registry.example.com

# Push image
docker push IMAGE
docker push myimage:latest
docker push registry.example.com/myimage:latest

# ===== SAVE/LOAD =====
# Save image to file
docker save IMAGE > image.tar
docker save -o image.tar IMAGE
docker save -o images.tar image1:tag image2:tag

# Load image from file
docker load < image.tar
docker load -i image.tar

# ===== HISTORY =====
# Show image layers
docker history IMAGE
docker history --no-trunc IMAGE
docker history --format "table {{.CreatedBy}}\t{{.Size}}" IMAGE
```

---

## 🌐 NETWORK MANAGEMENT

### Network Commands
```bash
# ===== LIST NETWORKS =====
docker network ls

# Filter
docker network ls -f "driver=bridge"
docker network ls -f "name=my"

# ===== CREATE NETWORK =====
# Bridge network (default)
docker network create NETWORK_NAME
docker network create mynetwork

# With specific driver
docker network create -d bridge mynetwork
docker network create -d overlay myoverlay
docker network create -d macvlan mymacvlan

# With subnet
docker network create --subnet=172.20.0.0/16 mynetwork
docker network create --subnet=172.20.0.0/16 --gateway=172.20.0.1 mynetwork

# With IP range
docker network create \
    --subnet=172.20.0.0/16 \
    --ip-range=172.20.240.0/20 \
    --gateway=172.20.0.1 \
    mynetwork

# Internal network (no external access)
docker network create --internal myinternal

# With options
docker network create \
    -d bridge \
    --opt com.docker.network.bridge.name=br-custom \
    --opt com.docker.network.bridge.enable_ip_masquerade=true \
    mynetwork

# ===== INSPECT NETWORK =====
docker network inspect NETWORK
docker network inspect bridge
docker network inspect -f '{{range .Containers}}{{.Name}}{{end}}' NETWORK

# ===== CONNECT/DISCONNECT =====
# Connect container to network
docker network connect NETWORK CONTAINER
docker network connect mynetwork web

# With specific IP
docker network connect --ip 172.20.0.10 mynetwork web

# With alias
docker network connect --alias webserver mynetwork web

# Disconnect
docker network disconnect NETWORK CONTAINER

# ===== REMOVE NETWORK =====
docker network rm NETWORK
docker network rm mynetwork

# Remove unused networks
docker network prune
```

### Network Types
```bash
# ===== BRIDGE (Default) =====
# Isolated network on host
docker network create -d bridge mybridge
docker run --network mybridge nginx

# ===== HOST =====
# Use host network directly
docker run --network host nginx
# Container uses host's IP, no port mapping needed

# ===== NONE =====
# No networking
docker run --network none alpine

# ===== OVERLAY =====
# Multi-host networking (Swarm)
docker network create -d overlay --attachable myoverlay

# ===== MACVLAN =====
# Assign MAC address to container
docker network create -d macvlan \
    --subnet=192.168.1.0/24 \
    --gateway=192.168.1.1 \
    -o parent=eth0 \
    mymacvlan
```

### DNS & Links
```bash
# ===== CONTAINER DNS =====
# Custom DNS
docker run --dns 8.8.8.8 nginx
docker run --dns 8.8.8.8 --dns 8.8.4.4 nginx

# DNS search domain
docker run --dns-search example.com nginx

# ===== HOSTS FILE =====
docker run --add-host=myhost:192.168.1.100 nginx
docker run --add-host=host.docker.internal:host-gateway nginx

# ===== LINKS (Legacy) =====
docker run --link db:database web
# Creates /etc/hosts entry and environment variables
```

---

## 💾 VOLUME MANAGEMENT

### Volume Commands
```bash
# ===== CREATE VOLUME =====
docker volume create VOLUME_NAME
docker volume create mydata

# With driver options
docker volume create --driver local \
    --opt type=nfs \
    --opt o=addr=192.168.1.100,rw \
    --opt device=:/path/to/dir \
    nfsvolume

# ===== LIST VOLUMES =====
docker volume ls

# Filter
docker volume ls -f "dangling=true"
docker volume ls -f "name=my"

# ===== INSPECT VOLUME =====
docker volume inspect VOLUME
docker volume inspect mydata

# ===== REMOVE VOLUME =====
docker volume rm VOLUME
docker volume rm mydata

# Remove unused volumes
docker volume prune

# ===== USE VOLUMES =====
# Named volume
docker run -v mydata:/app/data nginx

# Bind mount
docker run -v /host/path:/container/path nginx
docker run -v $(pwd):/app nginx

# Read-only
docker run -v mydata:/app/data:ro nginx

# tmpfs mount
docker run --tmpfs /app/tmp nginx

# Mount syntax (preferred)
docker run --mount source=mydata,target=/app/data nginx
docker run --mount type=bind,source=/host/path,target=/container/path nginx
docker run --mount type=tmpfs,destination=/app/tmp,tmpfs-size=100m nginx

# Complete example
docker run -d \
    --name db \
    --mount source=mysql-data,target=/var/lib/mysql \
    --mount type=bind,source=/backup,target=/backup,readonly \
    -e MYSQL_ROOT_PASSWORD=secret \
    mysql:8.0
```

### Volume Backup
```bash
# ===== BACKUP VOLUME =====
# Backup to tar
docker run --rm \
    -v VOLUME_NAME:/data \
    -v $(pwd):/backup \
    alpine tar cvf /backup/backup.tar /data

# ===== RESTORE VOLUME =====
# Restore from tar
docker run --rm \
    -v VOLUME_NAME:/data \
    -v $(pwd):/backup \
    alpine sh -c "cd /data && tar xvf /backup/backup.tar --strip 1"

# ===== COPY BETWEEN VOLUMES =====
docker run --rm \
    -v source_vol:/source:ro \
    -v dest_vol:/dest \
    alpine cp -r /source/. /dest/
```

---

## 🐙 DOCKER COMPOSE

### Basic Commands
```bash
# ===== START SERVICES =====
docker compose up
docker compose up -d                    # Detached
docker compose up --build              # Rebuild images
docker compose up --force-recreate     # Recreate containers
docker compose up -d --scale web=3     # Scale service
docker compose up SERVICE              # Specific service

# ===== STOP SERVICES =====
docker compose down
docker compose down -v                 # Remove volumes
docker compose down --rmi all          # Remove images
docker compose down --remove-orphans   # Remove orphan containers

docker compose stop                    # Stop without removing
docker compose start                   # Start stopped services
docker compose restart                 # Restart services

# ===== LOGS =====
docker compose logs
docker compose logs -f                 # Follow
docker compose logs SERVICE            # Specific service
docker compose logs --tail 100 SERVICE

# ===== STATUS =====
docker compose ps
docker compose top
docker compose images

# ===== EXEC =====
docker compose exec SERVICE COMMAND
docker compose exec web bash
docker compose exec -u root db mysql -u root -p

# ===== CONFIG =====
docker compose config                  # Validate and view
docker compose config --services       # List services
docker compose config --volumes        # List volumes

# ===== BUILD =====
docker compose build
docker compose build --no-cache
docker compose build SERVICE

# ===== PULL/PUSH =====
docker compose pull
docker compose push
```

### Docker Compose File Examples

#### Basic Web + Database
```yaml
# docker-compose.yml
version: '3.9'

services:
  web:
    image: nginx:alpine
    container_name: web
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./html:/usr/share/nginx/html:ro
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - app
    restart: unless-stopped
    networks:
      - frontend

  app:
    build:
      context: ./app
      dockerfile: Dockerfile
    container_name: app
    environment:
      - NODE_ENV=production
      - DB_HOST=db
      - DB_USER=app
      - DB_PASS=${DB_PASSWORD}
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped
    networks:
      - frontend
      - backend

  db:
    image: mysql:8.0
    container_name: db
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: appdb
      MYSQL_USER: app
      MYSQL_PASSWORD: ${DB_PASSWORD}
    volumes:
      - mysql-data:/var/lib/mysql
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped
    networks:
      - backend

  redis:
    image: redis:alpine
    container_name: redis
    command: redis-server --requirepass ${REDIS_PASSWORD}
    volumes:
      - redis-data:/data
    restart: unless-stopped
    networks:
      - backend

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true

volumes:
  mysql-data:
  redis-data:
```

#### WordPress Complete Stack
```yaml
# docker-compose.wordpress.yml
version: '3.9'

services:
  wordpress:
    image: wordpress:latest
    container_name: wordpress
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: ${WP_DB_PASSWORD}
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - wordpress-data:/var/www/html
      - ./uploads.ini:/usr/local/etc/php/conf.d/uploads.ini
    depends_on:
      - db
    restart: unless-stopped
    networks:
      - wp-network

  db:
    image: mariadb:10.11
    container_name: wordpress-db
    environment:
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: ${WP_DB_PASSWORD}
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
    volumes:
      - db-data:/var/lib/mysql
    restart: unless-stopped
    networks:
      - wp-network

  phpmyadmin:
    image: phpmyadmin:latest
    container_name: phpmyadmin
    ports:
      - "8081:80"
    environment:
      PMA_HOST: db
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
    depends_on:
      - db
    restart: unless-stopped
    networks:
      - wp-network

networks:
  wp-network:
    driver: bridge

volumes:
  wordpress-data:
  db-data:
```

#### LEMP Stack (Nginx + PHP + MySQL)
```yaml
# docker-compose.lemp.yml
version: '3.9'

services:
  nginx:
    image: nginx:alpine
    container_name: nginx
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./src:/var/www/html
      - ./nginx/conf.d:/etc/nginx/conf.d
      - ./nginx/ssl:/etc/nginx/ssl
    depends_on:
      - php
    restart: unless-stopped
    networks:
      - lemp

  php:
    build:
      context: ./php
      dockerfile: Dockerfile
    container_name: php
    volumes:
      - ./src:/var/www/html
      - ./php/php.ini:/usr/local/etc/php/php.ini
    environment:
      - DB_HOST=mysql
      - DB_NAME=app
      - DB_USER=app
      - DB_PASS=${DB_PASSWORD}
    restart: unless-stopped
    networks:
      - lemp

  mysql:
    image: mysql:8.0
    container_name: mysql
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: app
      MYSQL_USER: app
      MYSQL_PASSWORD: ${DB_PASSWORD}
    volumes:
      - mysql-data:/var/lib/mysql
    restart: unless-stopped
    networks:
      - lemp

networks:
  lemp:
    driver: bridge

volumes:
  mysql-data:
```

---

## 📄 DOCKERFILE REFERENCE

### Complete Dockerfile Example
```dockerfile
# ===== BUILD STAGE =====
FROM node:20-alpine AS builder

# Set working directory
WORKDIR /app

# Install dependencies first (cache optimization)
COPY package*.json ./
RUN npm ci --only=production

# Copy source code
COPY . .

# Build application
RUN npm run build

# ===== PRODUCTION STAGE =====
FROM node:20-alpine AS production

# Labels
LABEL maintainer="admin@example.com"
LABEL version="1.0"
LABEL description="Production Node.js Application"

# Create non-root user
RUN addgroup -g 1001 -S nodejs && \
    adduser -S nodejs -u 1001

# Set working directory
WORKDIR /app

# Copy from builder
COPY --from=builder --chown=nodejs:nodejs /app/dist ./dist
COPY --from=builder --chown=nodejs:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=nodejs:nodejs /app/package.json ./

# Environment variables
ENV NODE_ENV=production
ENV PORT=3000

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost:3000/health || exit 1

# Switch to non-root user
USER nodejs

# Start command
CMD ["node", "dist/index.js"]
```

### PHP Application Dockerfile
```dockerfile
FROM php:8.2-fpm-alpine

# Install extensions
RUN apk add --no-cache \
    freetype-dev \
    libjpeg-turbo-dev \
    libpng-dev \
    libzip-dev \
    icu-dev \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install -j$(nproc) \
        gd \
        mysqli \
        pdo_mysql \
        zip \
        intl \
        opcache

# Install Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# PHP configuration
COPY php.ini /usr/local/etc/php/conf.d/custom.ini

# Set working directory
WORKDIR /var/www/html

# Copy application
COPY --chown=www-data:www-data . .

# Install dependencies
RUN composer install --no-dev --optimize-autoloader

USER www-data

EXPOSE 9000
CMD ["php-fpm"]
```

### Python Application Dockerfile
```dockerfile
FROM python:3.12-slim

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create non-root user
RUN useradd --create-home --shell /bin/bash appuser

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY --chown=appuser:appuser . .

# Switch to non-root user
USER appuser

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]
```

### Dockerfile Instructions Reference
```dockerfile
# ===== BASE IMAGE =====
FROM image:tag
FROM image:tag AS stage_name

# ===== METADATA =====
LABEL key="value"
LABEL maintainer="email@example.com"

# ===== ENVIRONMENT =====
ENV KEY=value
ENV KEY1=value1 KEY2=value2
ARG BUILD_ARG=default

# ===== WORKING DIRECTORY =====
WORKDIR /path/to/dir

# ===== COPY FILES =====
COPY source dest
COPY --chown=user:group source dest
COPY --from=stage /source /dest

# ===== ADD FILES =====
ADD source dest
ADD https://url/file.tar.gz /dest/
# ADD extracts tar automatically

# ===== RUN COMMANDS =====
RUN command
RUN command1 && command2
RUN ["executable", "param1", "param2"]

# ===== EXPOSE PORTS =====
EXPOSE 80
EXPOSE 80/tcp 443/tcp

# ===== VOLUMES =====
VOLUME /data
VOLUME ["/data", "/logs"]

# ===== USER =====
USER username
USER uid:gid

# ===== ENTRYPOINT & CMD =====
# ENTRYPOINT - always executed
ENTRYPOINT ["executable"]
ENTRYPOINT ["executable", "param1"]

# CMD - default arguments (overridable)
CMD ["param1", "param2"]
CMD ["executable", "param1"]
CMD command param1 param2

# Combined:
ENTRYPOINT ["python"]
CMD ["app.py"]  # docker run image script.py -> runs python script.py

# ===== HEALTH CHECK =====
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost/ || exit 1
HEALTHCHECK NONE

# ===== SHELL =====
SHELL ["/bin/bash", "-c"]

# ===== STOPSIGNAL =====
STOPSIGNAL SIGTERM

# ===== ONBUILD =====
ONBUILD COPY . /app
ONBUILD RUN npm install
```

---

## 🐝 DOCKER SWARM

### Swarm Management
```bash
# ===== INITIALIZE SWARM =====
docker swarm init
docker swarm init --advertise-addr 192.168.1.100

# Get join token
docker swarm join-token worker
docker swarm join-token manager

# Join as worker
docker swarm join --token TOKEN MANAGER_IP:2377

# Join as manager
docker swarm join --token TOKEN MANAGER_IP:2377

# Leave swarm
docker swarm leave
docker swarm leave --force  # For managers

# ===== NODE MANAGEMENT =====
docker node ls
docker node inspect NODE_ID
docker node update --availability drain NODE_ID
docker node update --availability active NODE_ID
docker node promote NODE_ID    # Worker to manager
docker node demote NODE_ID     # Manager to worker
docker node rm NODE_ID

# ===== SERVICE MANAGEMENT =====
# Create service
docker service create --name web -p 80:80 nginx
docker service create \
    --name web \
    --replicas 3 \
    --publish 80:80 \
    --mount type=volume,source=webdata,target=/usr/share/nginx/html \
    --env NGINX_HOST=example.com \
    --constraint 'node.role==worker' \
    nginx:alpine

# List services
docker service ls

# Inspect service
docker service inspect web
docker service inspect --pretty web

# Service logs
docker service logs web
docker service logs -f web

# Scale service
docker service scale web=5
docker service update --replicas 5 web

# Update service
docker service update --image nginx:1.25 web
docker service update --env-add NEW_VAR=value web
docker service update --publish-rm 80 web
docker service update --publish-add 8080:80 web

# Rollback
docker service rollback web

# Remove service
docker service rm web

# ===== STACK (Compose for Swarm) =====
# Deploy stack
docker stack deploy -c docker-compose.yml mystack

# List stacks
docker stack ls

# List stack services
docker stack services mystack

# List stack tasks
docker stack ps mystack

# Remove stack
docker stack rm mystack
```

---

## 🔒 DOCKER SECURITY & HARDENING

### Secure Docker Daemon
```bash
# /etc/docker/daemon.json
{
    "icc": false,
    "no-new-privileges": true,
    "userland-proxy": false,
    "live-restore": true,
    "log-driver": "json-file",
    "log-opts": {
        "max-size": "10m",
        "max-file": "3"
    },
    "storage-driver": "overlay2",
    "default-ulimits": {
        "nofile": {
            "Name": "nofile",
            "Hard": 64000,
            "Soft": 64000
        }
    }
}

# Restart Docker
sudo systemctl restart docker
```

### Container Security
```bash
# ===== RUN AS NON-ROOT =====
docker run --user 1000:1000 IMAGE
docker run --user nobody IMAGE

# ===== READ-ONLY FILESYSTEM =====
docker run --read-only IMAGE
docker run --read-only --tmpfs /tmp IMAGE

# ===== DROP CAPABILITIES =====
docker run --cap-drop ALL IMAGE
docker run --cap-drop ALL --cap-add NET_BIND_SERVICE IMAGE

# ===== SECURITY OPTIONS =====
docker run --security-opt no-new-privileges IMAGE
docker run --security-opt seccomp=profile.json IMAGE
docker run --security-opt apparmor=docker-default IMAGE

# ===== RESOURCE LIMITS =====
docker run --memory=512m --memory-swap=512m IMAGE
docker run --cpus=0.5 IMAGE
docker run --pids-limit 100 IMAGE
docker run --ulimit nofile=1024:1024 IMAGE

# ===== NETWORK SECURITY =====
docker run --network none IMAGE  # No network
docker run --network=host IMAGE  # Host network (careful!)

# Complete secure container
docker run -d \
    --name secure-app \
    --user 1000:1000 \
    --read-only \
    --tmpfs /tmp:rw,noexec,nosuid \
    --cap-drop ALL \
    --security-opt no-new-privileges:true \
    --memory=256m \
    --cpus=0.5 \
    --pids-limit=50 \
    --restart=unless-stopped \
    myapp:latest
```

### Docker Content Trust
```bash
# Enable content trust
export DOCKER_CONTENT_TRUST=1

# Sign images
docker trust sign myregistry/myimage:latest

# View signatures
docker trust inspect myregistry/myimage:latest

# Revoke trust
docker trust revoke myregistry/myimage:latest
```

### Security Scanning
```bash
# Docker Scout (built-in)
docker scout cves IMAGE
docker scout recommendations IMAGE

# Trivy
trivy image IMAGE
trivy image --severity HIGH,CRITICAL nginx:latest

# Anchore/Grype
grype IMAGE
```

---

## 🔧 DOCKER TROUBLESHOOTING

### Debug Commands
```bash
# ===== CONTAINER DEBUGGING =====
# View all logs
docker logs CONTAINER 2>&1

# Enter failed container
docker commit CONTAINER debug-image
docker run -it debug-image /bin/sh

# Debug networking
docker run --rm --net container:CONTAINER nicolaka/netshoot

# Check container events
docker events --filter container=CONTAINER

# ===== SYSTEM DEBUGGING =====
# Docker system info
docker info
docker version

# Disk usage
docker system df
docker system df -v

# Events
docker events
docker events --since '2026-01-14T00:00:00'

# ===== CLEANUP =====
# Remove everything unused
docker system prune -a

# Remove with volumes
docker system prune -a --volumes

# Remove builder cache
docker builder prune -a

# ===== LOGS =====
# Docker daemon logs
sudo journalctl -u docker.service
sudo tail -f /var/log/docker.log

# Container logs location
/var/lib/docker/containers/[container-id]/[container-id]-json.log
```

### Common Issues
```bash
# ===== PERMISSION DENIED =====
# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker

# ===== DISK SPACE =====
# Check disk usage
docker system df

# Cleanup
docker system prune -a --volumes

# ===== NETWORK ISSUES =====
# Restart Docker networking
sudo systemctl restart docker

# Check DNS
docker run --rm busybox nslookup google.com

# ===== CONTAINER WON'T START =====
# Check logs
docker logs CONTAINER

# Inspect
docker inspect CONTAINER

# Check events
docker events --filter container=CONTAINER

# ===== IMAGE PULL FAILED =====
# Check registry
docker login REGISTRY

# Pull with debug
docker pull IMAGE 2>&1 | tee pull.log

# ===== CANNOT CONNECT TO DAEMON =====
# Check Docker service
sudo systemctl status docker
sudo systemctl restart docker

# Check socket
ls -la /var/run/docker.sock
```

---

## 📊 DOCKER QUICK REFERENCE

### Most Used Commands
| Command | Description |
|---------|-------------|
| `docker run -d -p 80:80 nginx` | Run container detached with port |
| `docker ps -a` | List all containers |
| `docker logs -f CONTAINER` | Follow container logs |
| `docker exec -it CONTAINER bash` | Enter container shell |
| `docker stop CONTAINER` | Stop container |
| `docker rm CONTAINER` | Remove container |
| `docker images` | List images |
| `docker rmi IMAGE` | Remove image |
| `docker pull IMAGE` | Pull image |
| `docker build -t name .` | Build image |
| `docker compose up -d` | Start compose stack |
| `docker compose down` | Stop compose stack |
| `docker system prune -a` | Cleanup everything |

### Environment File (.env)
```bash
# .env file for docker-compose
MYSQL_ROOT_PASSWORD=supersecret
DB_PASSWORD=dbpass123
REDIS_PASSWORD=redispass
APP_ENV=production
APP_DEBUG=false
```

### Docker Ignore (.dockerignore)
```
# .dockerignore
.git
.gitignore
.env
.env.*
node_modules
npm-debug.log
Dockerfile*
docker-compose*
.dockerignore
README.md
.vscode
.idea
*.md
tests
coverage
.nyc_output
```

---

# 7. GIT COMPLETE CHEATSHEET & TEAM WORKFLOW

## 📋 Table of Contents - Git
- [Git Configuration](#git-configuration)
- [Basic Commands](#git-basic-commands)
- [Branching & Merging](#branching--merging)
- [Git Stash](#git-stash)
- [Remote Operations](#remote-operations)
- [Git Log & History](#git-log--history)
- [Undoing Changes](#undoing-changes)
- [Git Rebase](#git-rebase)
- [Git Tags](#git-tags)
- [Git Submodules](#git-submodules)
- [Git Hooks](#git-hooks)
- [Git Flow (Team Workflow)](#git-flow-team-workflow)
- [Team Collaboration (4+ Developers)](#team-collaboration-4-developers)
- [Conflict Resolution](#conflict-resolution)
- [Best Practices](#git-best-practices)

---

## 🔧 GIT CONFIGURATION

### Initial Setup
```bash
# ===== IDENTITY =====
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Per-repository config
git config user.name "Work Name"
git config user.email "work@company.com"

# ===== EDITOR =====
git config --global core.editor "code --wait"    # VS Code
git config --global core.editor "vim"            # Vim
git config --global core.editor "nano"           # Nano

# ===== DEFAULT BRANCH =====
git config --global init.defaultBranch main

# ===== LINE ENDINGS =====
# Windows
git config --global core.autocrlf true
# Linux/Mac
git config --global core.autocrlf input

# ===== ALIASES =====
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual '!gitk'
git config --global alias.lg "log --oneline --graph --decorate --all"
git config --global alias.amend 'commit --amend --no-edit'

# ===== CREDENTIAL STORAGE =====
git config --global credential.helper store      # Plain text (not secure)
git config --global credential.helper cache      # Memory (15 min default)
git config --global credential.helper 'cache --timeout=3600'  # 1 hour

# Windows Credential Manager
git config --global credential.helper manager

# ===== DIFF & MERGE TOOLS =====
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'
git config --global diff.tool vscode
git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'

# ===== COLORS =====
git config --global color.ui auto
git config --global color.branch.current "yellow bold"
git config --global color.branch.remote "green"
git config --global color.status.added "green"
git config --global color.status.changed "yellow"
git config --global color.status.untracked "red"

# ===== VIEW CONFIG =====
git config --list
git config --list --global
git config --list --local
git config user.name
```

### SSH Key Setup
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"
# or RSA
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

# Start SSH agent
eval "$(ssh-agent -s)"

# Add key to agent
ssh-add ~/.ssh/id_ed25519

# Copy public key
cat ~/.ssh/id_ed25519.pub
# Add to GitHub/GitLab/Bitbucket

# Test connection
ssh -T git@github.com
ssh -T git@gitlab.com
```

---

## 📝 GIT BASIC COMMANDS

### Initialize & Clone
```bash
# ===== INITIALIZE =====
git init
git init project-name
git init --bare repo.git    # Bare repository (server)

# ===== CLONE =====
git clone URL
git clone URL directory-name
git clone --depth 1 URL                    # Shallow clone (latest only)
git clone --branch branch-name URL         # Clone specific branch
git clone --single-branch --branch dev URL # Only one branch
git clone --recursive URL                  # With submodules

# Clone with SSH
git clone git@github.com:user/repo.git

# Clone with HTTPS
git clone https://github.com/user/repo.git
```

### Staging & Committing
```bash
# ===== STATUS =====
git status
git status -s              # Short format
git status -sb             # Short with branch

# ===== ADD (STAGING) =====
git add file.txt           # Single file
git add file1.txt file2.txt
git add *.js               # Pattern
git add .                  # All files
git add -A                 # All files (including deletions)
git add -u                 # Only modified/deleted (not new)
git add -p                 # Interactive/patch mode
git add -N file.txt        # Intent to add (track without staging)

# ===== COMMIT =====
git commit -m "Commit message"
git commit -am "Message"   # Add all modified + commit
git commit --amend         # Modify last commit
git commit --amend -m "New message"
git commit --amend --no-edit  # Amend without changing message
git commit --allow-empty -m "Empty commit"
git commit -v              # Show diff in editor

# Commit with signature
git commit -S -m "Signed commit"

# ===== DIFF =====
git diff                   # Unstaged changes
git diff --staged          # Staged changes
git diff HEAD              # All changes since last commit
git diff branch1..branch2  # Between branches
git diff commit1..commit2  # Between commits
git diff --stat            # Summary only
git diff --name-only       # File names only
git diff --name-status     # Names with status
git diff file.txt          # Specific file

# ===== REMOVE =====
git rm file.txt            # Remove from working dir & stage
git rm --cached file.txt   # Remove from staging only (keep file)
git rm -r directory/       # Remove directory
git rm -f file.txt         # Force remove modified file

# ===== MOVE/RENAME =====
git mv old-name.txt new-name.txt
git mv file.txt directory/
```

---

## 🌿 BRANCHING & MERGING

### Branch Operations
```bash
# ===== LIST BRANCHES =====
git branch                 # Local branches
git branch -r              # Remote branches
git branch -a              # All branches
git branch -v              # With last commit
git branch -vv             # With upstream info
git branch --merged        # Merged into current
git branch --no-merged     # Not merged
git branch --contains commit  # Branches containing commit

# ===== CREATE BRANCH =====
git branch branch-name
git branch branch-name commit   # From specific commit
git branch branch-name origin/branch  # From remote

# ===== SWITCH/CHECKOUT =====
git checkout branch-name
git checkout -b new-branch      # Create and switch
git checkout -b new-branch origin/branch  # From remote
git checkout -                  # Previous branch
git checkout --track origin/branch  # Track remote

# Git 2.23+ (preferred)
git switch branch-name
git switch -c new-branch        # Create and switch
git switch -c new-branch origin/branch
git switch -                    # Previous branch

# ===== RENAME BRANCH =====
git branch -m new-name          # Rename current
git branch -m old-name new-name # Rename specific

# ===== DELETE BRANCH =====
git branch -d branch-name       # Safe delete (must be merged)
git branch -D branch-name       # Force delete
git push origin --delete branch-name  # Delete remote

# ===== SET UPSTREAM =====
git branch --set-upstream-to=origin/branch
git branch -u origin/branch
git push -u origin branch-name  # Push and set upstream
```

### Merge Operations
```bash
# ===== BASIC MERGE =====
git checkout main
git merge feature-branch

# ===== MERGE OPTIONS =====
git merge --no-ff branch   # No fast-forward (always create merge commit)
git merge --ff-only branch # Only fast-forward (fail if not possible)
git merge --squash branch  # Squash all commits into one
git merge -m "Custom message" branch

# ===== ABORT MERGE =====
git merge --abort

# ===== MERGE STRATEGIES =====
git merge -s recursive branch      # Default
git merge -s ours branch           # Keep ours, discard theirs
git merge -s theirs branch         # Keep theirs (not available directly)
git merge -X ours branch           # Recursive with ours preference
git merge -X theirs branch         # Recursive with theirs preference

# ===== THREE-WAY MERGE =====
# Git automatically uses 3-way merge with common ancestor

# Visual merge tool
git mergetool
```

### Merge Strategies Explained
```
┌─────────────────────────────────────────────────────────────────┐
│                    MERGE STRATEGIES                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  FAST-FORWARD (--ff)                                           │
│  ─────────────────────                                         │
│  main:    A───B───C                                            │
│                    ↘                                           │
│  feature:          D───E───F                                   │
│                                                                 │
│  After merge:                                                  │
│  main:    A───B───C───D───E───F                                │
│                                                                 │
│  * Linear history, no merge commit                             │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  NO FAST-FORWARD (--no-ff)                                     │
│  ─────────────────────────                                     │
│  main:    A───B───C───────────M                                │
│                    ↘         ↗                                 │
│  feature:          D───E───F                                   │
│                                                                 │
│  * Always creates merge commit                                 │
│  * Preserves branch history                                    │
│  * Recommended for feature branches                            │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  SQUASH MERGE (--squash)                                       │
│  ──────────────────────                                        │
│  main:    A───B───C───S                                        │
│                    ↘                                           │
│  feature:          D───E───F (not connected)                   │
│                                                                 │
│  * Combines all commits into one                               │
│  * Clean main history                                          │
│  * Loses individual commit history                             │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  THREE-WAY MERGE                                                │
│  ───────────────                                               │
│              G───H (feature)                                   │
│             ↗     ↘                                            │
│  main: A───B───C───D───M                                       │
│            (base)                                               │
│                                                                 │
│  * Uses common ancestor (B) as base                            │
│  * Compares both branches to base                              │
│  * Automatic conflict detection                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📦 GIT STASH

### Basic Stash Operations
```bash
# ===== SAVE TO STASH =====
git stash                      # Stash tracked changes
git stash push                 # Same as above
git stash push -m "Message"    # With description
git stash push -u              # Include untracked files
git stash push -a              # Include all (untracked + ignored)
git stash push file.txt        # Specific file(s)
git stash push -p              # Interactive (partial stash)
git stash push --keep-index    # Keep staged files

# ===== LIST STASHES =====
git stash list
# Output: stash@{0}: WIP on main: abc1234 Last commit message

# ===== SHOW STASH CONTENT =====
git stash show                 # Summary of latest
git stash show -p              # Full diff of latest
git stash show stash@{1}       # Specific stash
git stash show -p stash@{2}    # Full diff of specific

# ===== APPLY STASH =====
git stash apply                # Apply latest, keep in stash
git stash apply stash@{1}      # Apply specific
git stash apply --index        # Restore staged state too

# ===== POP STASH =====
git stash pop                  # Apply and remove latest
git stash pop stash@{1}        # Pop specific
git stash pop --index          # Restore staged state

# ===== DROP STASH =====
git stash drop                 # Remove latest
git stash drop stash@{1}       # Remove specific

# ===== CLEAR ALL STASHES =====
git stash clear

# ===== CREATE BRANCH FROM STASH =====
git stash branch new-branch              # Latest stash
git stash branch new-branch stash@{1}    # Specific stash
```

### Advanced Stash
```bash
# ===== STASH UNTRACKED FILES =====
git stash push -u -m "With untracked"

# ===== STASH SPECIFIC FILES =====
git stash push -m "Partial" -- file1.txt file2.txt

# ===== STASH WITH PATHSPEC =====
git stash push -m "Only src" -- src/

# ===== CHECK IF STASH EXISTS =====
git stash list | grep -q "stash@{0}" && echo "Has stash"

# ===== APPLY STASH TO DIFFERENT BRANCH =====
git checkout other-branch
git stash apply

# ===== VIEW STASH DIFF AGAINST CURRENT =====
git diff stash@{0}

# ===== RECOVER DROPPED STASH =====
# Find dangling commits
git fsck --unreachable | grep commit
# Apply recovered stash
git stash apply COMMIT_HASH
```

### Stash Workflow Examples
```bash
# ===== QUICK CONTEXT SWITCH =====
# Working on feature, need to fix bug
git stash push -m "Feature WIP"
git checkout main
git checkout -b hotfix/bug-123
# ... fix bug ...
git commit -am "Fix bug #123"
git checkout main
git merge hotfix/bug-123
git checkout feature-branch
git stash pop

# ===== STASH BEFORE PULL =====
git stash
git pull
git stash pop

# ===== PARTIAL STASH =====
# Stash only some changes interactively
git stash push -p
# Answer y/n for each hunk
```

---

## 🌐 REMOTE OPERATIONS

### Remote Management
```bash
# ===== LIST REMOTES =====
git remote
git remote -v              # With URLs

# ===== ADD REMOTE =====
git remote add origin URL
git remote add upstream URL

# ===== CHANGE REMOTE URL =====
git remote set-url origin NEW_URL

# ===== REMOVE REMOTE =====
git remote remove origin
git remote rm origin

# ===== RENAME REMOTE =====
git remote rename origin upstream

# ===== SHOW REMOTE INFO =====
git remote show origin
```

### Fetch, Pull, Push
```bash
# ===== FETCH =====
git fetch                  # Fetch all remotes
git fetch origin           # Specific remote
git fetch origin branch    # Specific branch
git fetch --all            # All remotes
git fetch --prune          # Remove deleted remote branches
git fetch --tags           # Fetch tags
git fetch --depth=1        # Shallow fetch

# ===== PULL =====
git pull                   # Fetch + merge
git pull origin main
git pull --rebase          # Fetch + rebase
git pull --rebase=interactive
git pull --ff-only         # Only fast-forward
git pull --no-commit       # Don't auto-commit merge
git pull --autostash       # Auto stash/unstash

# ===== PUSH =====
git push
git push origin main
git push -u origin branch  # Set upstream
git push --all             # All branches
git push --tags            # Push tags
git push --force           # Force push (DANGEROUS!)
git push --force-with-lease  # Safer force push
git push --delete origin branch  # Delete remote branch
git push origin :branch    # Delete remote branch (old syntax)

# ===== PUSH SPECIFIC COMMITS =====
git push origin commit:branch

# ===== SET UPSTREAM =====
git push --set-upstream origin branch
git branch --set-upstream-to=origin/branch
```

### Working with Multiple Remotes
```bash
# ===== FORK WORKFLOW =====
# Clone your fork
git clone git@github.com:YOUR_USER/repo.git
cd repo

# Add upstream (original repo)
git remote add upstream git@github.com:ORIGINAL_OWNER/repo.git

# Fetch upstream
git fetch upstream

# Merge upstream changes
git checkout main
git merge upstream/main

# Push to your fork
git push origin main

# ===== SYNC FORK =====
git fetch upstream
git checkout main
git rebase upstream/main
git push origin main --force-with-lease
```

---

## 📜 GIT LOG & HISTORY

### Log Commands
```bash
# ===== BASIC LOG =====
git log
git log -n 10              # Last 10 commits
git log --oneline          # One line per commit
git log --graph            # ASCII graph
git log --decorate         # Show refs
git log --all              # All branches

# ===== COMBINED OPTIONS =====
git log --oneline --graph --decorate --all
git log --oneline --graph --all -20

# ===== FORMAT LOG =====
git log --pretty=format:"%h - %an, %ar : %s"
git log --pretty=format:"%H%n%an%n%ae%n%s%n"

# Format placeholders:
# %H  - Full hash
# %h  - Short hash
# %an - Author name
# %ae - Author email
# %ad - Author date
# %ar - Author date (relative)
# %cn - Committer name
# %s  - Subject
# %b  - Body
# %d  - Ref names

# ===== FILTER LOG =====
git log --author="Name"
git log --author="name@email.com"
git log --since="2024-01-01"
git log --until="2024-12-31"
git log --after="2 weeks ago"
git log --before="yesterday"
git log --grep="bug fix"
git log -S "function_name"        # Search content changes
git log -G "regex"                # Search with regex
git log -- file.txt               # Specific file
git log -- path/to/dir/           # Specific directory

# ===== COMBINED FILTERS =====
git log --author="John" --since="2024-01-01" --oneline

# ===== FILE HISTORY =====
git log -- file.txt
git log -p -- file.txt            # With diff
git log --follow -- file.txt      # Follow renames

# ===== BRANCH COMPARISON =====
git log main..feature             # Commits in feature not in main
git log feature..main             # Commits in main not in feature
git log main...feature            # Commits in either, not both

# ===== SHOW SPECIFIC COMMIT =====
git show COMMIT_HASH
git show HEAD
git show HEAD~1                   # Previous commit
git show HEAD~3:file.txt          # File at specific commit
git show --stat COMMIT            # With file stats
```

### Other History Commands
```bash
# ===== BLAME =====
git blame file.txt
git blame -L 10,20 file.txt       # Lines 10-20
git blame -e file.txt             # Show email
git blame -w file.txt             # Ignore whitespace
git blame --date=short file.txt

# ===== SHORTLOG =====
git shortlog                      # Commits grouped by author
git shortlog -sn                  # Summary: count, name
git shortlog -sne                 # With email

# ===== REFLOG =====
git reflog                        # All HEAD changes
git reflog show branch            # Specific branch
git reflog --date=relative
git reflog expire --expire=30.days.ago --all

# ===== BISECT (Find bug) =====
git bisect start
git bisect bad                    # Current commit is bad
git bisect good v1.0              # This commit was good
# Git will checkout middle commit
# Test and mark:
git bisect good                   # or
git bisect bad
# Repeat until found
git bisect reset                  # End bisect

# Automated bisect
git bisect start HEAD v1.0
git bisect run ./test.sh
```

---

## ↩️ UNDOING CHANGES

### Reset Operations
```bash
# ===== RESET MODES =====
# --soft: Keep changes staged
git reset --soft HEAD~1

# --mixed (default): Keep changes unstaged
git reset HEAD~1
git reset --mixed HEAD~1

# --hard: Discard all changes (DANGEROUS!)
git reset --hard HEAD~1

# ===== RESET TO SPECIFIC COMMIT =====
git reset --hard COMMIT_HASH

# ===== RESET SPECIFIC FILE =====
git reset HEAD file.txt          # Unstage file
git reset COMMIT file.txt        # Reset file to commit version

# ===== RESET TO REMOTE =====
git reset --hard origin/main

# ===== UNDO LAST COMMIT (keep changes) =====
git reset --soft HEAD~1

# ===== UNDO LAST COMMIT (discard changes) =====
git reset --hard HEAD~1
```

### Revert (Safe Undo)
```bash
# ===== REVERT COMMIT =====
git revert COMMIT_HASH
git revert HEAD                  # Revert last commit

# ===== REVERT OPTIONS =====
git revert -n COMMIT             # No auto-commit
git revert --no-commit COMMIT    # Same as above
git revert -m 1 MERGE_COMMIT     # Revert merge commit

# ===== REVERT MULTIPLE COMMITS =====
git revert OLDEST..NEWEST
git revert HEAD~3..HEAD          # Last 3 commits
```

### Restore & Checkout
```bash
# ===== RESTORE (Git 2.23+) =====
git restore file.txt             # Discard working directory changes
git restore --staged file.txt    # Unstage file
git restore --source=HEAD~1 file.txt  # Restore from commit
git restore --source=COMMIT file.txt
git restore .                    # Restore all files

# ===== CHECKOUT (older method) =====
git checkout -- file.txt         # Discard changes
git checkout HEAD file.txt
git checkout COMMIT -- file.txt  # Get file from commit

# ===== CLEAN (Remove untracked) =====
git clean -n                     # Dry run
git clean -f                     # Remove untracked files
git clean -fd                    # Remove files and directories
git clean -fx                    # Remove ignored files too
git clean -i                     # Interactive
```

### Recovery
```bash
# ===== RECOVER DELETED BRANCH =====
git reflog
git checkout -b recovered-branch COMMIT_HASH

# ===== RECOVER RESET COMMITS =====
git reflog
git reset --hard HEAD@{2}

# ===== RECOVER DROPPED STASH =====
git fsck --unreachable | grep commit
git show COMMIT_HASH
git stash apply COMMIT_HASH

# ===== RECOVER DELETED FILE =====
git checkout HEAD~1 -- file.txt
```

---

## 🔄 GIT REBASE

### Basic Rebase
```bash
# ===== REBASE ONTO BRANCH =====
git checkout feature
git rebase main

# ===== REBASE INTERACTIVELY =====
git rebase -i HEAD~5             # Last 5 commits
git rebase -i main               # Since branching from main
git rebase -i --root             # All commits

# Interactive commands:
# pick   = use commit
# reword = use commit, edit message
# edit   = use commit, stop for amending
# squash = meld into previous commit
# fixup  = like squash, discard message
# drop   = remove commit
# exec   = run command

# ===== REBASE OPTIONS =====
git rebase --onto main feature branch
git rebase --continue           # After resolving conflicts
git rebase --abort              # Cancel rebase
git rebase --skip               # Skip current commit

# ===== REBASE WITH AUTOSQUASH =====
git commit --fixup=COMMIT_HASH
git commit --squash=COMMIT_HASH
git rebase -i --autosquash HEAD~5

# ===== PRESERVE MERGE COMMITS =====
git rebase -r main              # --rebase-merges
```

### Rebase vs Merge
```
┌─────────────────────────────────────────────────────────────────┐
│                    MERGE vs REBASE                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  BEFORE:                                                        │
│  main:     A───B───C───D                                        │
│                 ↘                                               │
│  feature:       E───F───G                                       │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  AFTER MERGE:                                                   │
│  main:     A───B───C───D───────M                                │
│                 ↘             ↗                                 │
│  feature:       E───F───G────                                   │
│                                                                 │
│  ✓ Preserves history                                           │
│  ✓ Safe for shared branches                                    │
│  ✗ Creates merge commit                                        │
│  ✗ Non-linear history                                          │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  AFTER REBASE:                                                  │
│  main:     A───B───C───D                                        │
│                         ↘                                       │
│  feature:               E'──F'──G'                              │
│                                                                 │
│  ✓ Linear history                                              │
│  ✓ Clean commit graph                                          │
│  ✗ Rewrites history                                            │
│  ✗ Don't use on shared branches!                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

GOLDEN RULE: Never rebase public/shared branches!
```

### Interactive Rebase Examples
```bash
# ===== SQUASH COMMITS =====
git rebase -i HEAD~4
# Change 'pick' to 'squash' for commits to combine
# Save and edit combined message

# ===== REORDER COMMITS =====
git rebase -i HEAD~4
# Reorder lines in editor
# Save

# ===== EDIT COMMIT MESSAGE =====
git rebase -i HEAD~3
# Change 'pick' to 'reword'
# Save, then edit message when prompted

# ===== SPLIT COMMIT =====
git rebase -i HEAD~3
# Change 'pick' to 'edit'
# Save
git reset HEAD~1
git add file1.txt
git commit -m "First part"
git add file2.txt
git commit -m "Second part"
git rebase --continue

# ===== DELETE COMMIT =====
git rebase -i HEAD~4
# Change 'pick' to 'drop' or delete line
# Save
```

---

## 🏷️ GIT TAGS

### Tag Operations
```bash
# ===== LIST TAGS =====
git tag
git tag -l "v1.*"             # Pattern matching
git tag -n                    # With messages
git tag --sort=-version:refname  # Sort by version

# ===== CREATE TAGS =====
# Lightweight tag
git tag v1.0.0
git tag v1.0.0 COMMIT_HASH

# Annotated tag (recommended)
git tag -a v1.0.0 -m "Release version 1.0.0"
git tag -a v1.0.0 -m "Message" COMMIT_HASH

# Signed tag
git tag -s v1.0.0 -m "Signed release"

# ===== SHOW TAG =====
git show v1.0.0

# ===== PUSH TAGS =====
git push origin v1.0.0        # Single tag
git push origin --tags        # All tags
git push --follow-tags        # Annotated tags with commits

# ===== DELETE TAGS =====
git tag -d v1.0.0             # Local
git push origin --delete v1.0.0  # Remote
git push origin :refs/tags/v1.0.0  # Remote (old syntax)

# ===== CHECKOUT TAG =====
git checkout v1.0.0
git checkout -b hotfix v1.0.0    # Create branch from tag
```

### Semantic Versioning
```
VERSION FORMAT: MAJOR.MINOR.PATCH

MAJOR - Breaking changes (incompatible API changes)
MINOR - New features (backward compatible)
PATCH - Bug fixes (backward compatible)

Examples:
v1.0.0 - Initial release
v1.0.1 - Bug fix
v1.1.0 - New feature
v2.0.0 - Breaking change

Pre-release: v1.0.0-alpha, v1.0.0-beta.1, v1.0.0-rc.1
Build metadata: v1.0.0+build.123
```

---

## 📁 GIT SUBMODULES

### Submodule Commands
```bash
# ===== ADD SUBMODULE =====
git submodule add URL path/to/submodule
git submodule add -b main URL path/to/submodule

# ===== CLONE WITH SUBMODULES =====
git clone --recursive URL
git clone --recurse-submodules URL

# ===== INITIALIZE SUBMODULES =====
git submodule init
git submodule update
git submodule update --init
git submodule update --init --recursive

# ===== UPDATE SUBMODULES =====
git submodule update --remote
git submodule update --remote --merge
git submodule update --remote --rebase

# ===== LIST SUBMODULES =====
git submodule status
git submodule foreach 'echo $name'

# ===== REMOVE SUBMODULE =====
git submodule deinit path/to/submodule
git rm path/to/submodule
rm -rf .git/modules/path/to/submodule

# ===== RUN COMMAND IN ALL SUBMODULES =====
git submodule foreach 'git pull origin main'
git submodule foreach 'git checkout main'
```

---

## 🪝 GIT HOOKS

### Available Hooks
```bash
# Location: .git/hooks/

# CLIENT-SIDE HOOKS
pre-commit       # Before commit message prompt
prepare-commit-msg  # Before commit message editor
commit-msg       # After commit message entered
post-commit      # After commit completed
pre-rebase       # Before rebase
post-rewrite     # After commit-changing commands
post-checkout    # After checkout
post-merge       # After merge
pre-push         # Before push

# SERVER-SIDE HOOKS
pre-receive      # Before refs updated
update           # Per-branch before update
post-receive     # After refs updated
```

### Hook Examples
```bash
# ===== PRE-COMMIT HOOK =====
# .git/hooks/pre-commit
#!/bin/bash

# Run linter
npm run lint
if [ $? -ne 0 ]; then
    echo "Lint failed! Fix errors before committing."
    exit 1
fi

# Run tests
npm test
if [ $? -ne 0 ]; then
    echo "Tests failed! Fix tests before committing."
    exit 1
fi

# Check for debug statements
if grep -rn "console.log\|debugger" --include="*.js" src/; then
    echo "Remove debug statements before committing!"
    exit 1
fi

exit 0

# ===== COMMIT-MSG HOOK =====
# .git/hooks/commit-msg
#!/bin/bash

# Enforce conventional commits
commit_regex='^(feat|fix|docs|style|refactor|test|chore|perf|ci|build|revert)(\(.+\))?: .{1,50}'

if ! grep -qE "$commit_regex" "$1"; then
    echo "Invalid commit message format!"
    echo "Use: type(scope): description"
    echo "Types: feat, fix, docs, style, refactor, test, chore, perf, ci, build, revert"
    exit 1
fi

exit 0

# ===== PRE-PUSH HOOK =====
# .git/hooks/pre-push
#!/bin/bash

# Prevent push to main
protected_branch='main'
current_branch=$(git symbolic-ref HEAD | sed -e 's,.*/\(.*\),\1,')

if [ $current_branch = $protected_branch ]; then
    echo "Direct push to main is not allowed!"
    echo "Create a pull request instead."
    exit 1
fi

# Run full test suite
npm run test:full
exit $?
```

### Husky (Git Hooks Made Easy)
```bash
# Install Husky
npm install husky --save-dev
npx husky install

# Add to package.json
# "prepare": "husky install"

# Add hook
npx husky add .husky/pre-commit "npm run lint"
npx husky add .husky/commit-msg 'npx commitlint --edit $1'

# .husky/pre-commit
#!/bin/sh
. "$(dirname "$0")/_/husky.sh"

npm run lint-staged
```

---

## 🌊 GIT FLOW (TEAM WORKFLOW)

### Git Flow Model
```
┌─────────────────────────────────────────────────────────────────────────┐
│                         GIT FLOW BRANCHING MODEL                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  main (production)                                                      │
│  ════════════════════════════●═══════●═══════════●═══════════════►     │
│                              ↑       ↑           ↑                      │
│                              │       │           │                      │
│  hotfix/*                    │   ●───●           │                      │
│                              │   ↑   ↓           │                      │
│  release/*              ●────●───┘   └───●───────●                      │
│                         ↑                ↓                              │
│  develop                                                                │
│  ═══════════●═══●═══════●════════●═══════●═══════●══════════════►      │
│             ↑   ↑       ↑        ↑       ↑       ↑                      │
│             │   │       │        │       │       │                      │
│  feature/*  ●───●       │    ●───●───●   │       │                      │
│                         │                │       │                      │
│  feature/*              ●────────────────●       │                      │
│                                                  │                      │
│  feature/*                                   ●───●                      │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│ BRANCH TYPES:                                                           │
│ • main     - Production-ready code (tagged releases)                    │
│ • develop  - Integration branch for features                            │
│ • feature/ - New features (from develop)                                │
│ • release/ - Release preparation (from develop)                         │
│ • hotfix/  - Emergency fixes (from main)                                │
└─────────────────────────────────────────────────────────────────────────┘
```

### Git Flow Commands
```bash
# ===== INSTALL GIT FLOW =====
# Ubuntu/Debian
apt install git-flow

# Mac
brew install git-flow-avh

# Windows (Git Bash)
# Included in Git for Windows

# ===== INITIALIZE =====
git flow init
# Accept defaults or customize branch names

# ===== FEATURE BRANCHES =====
# Start feature
git flow feature start feature-name
# Creates: feature/feature-name from develop

# Finish feature
git flow feature finish feature-name
# Merges into develop, deletes feature branch

# Publish feature (share with team)
git flow feature publish feature-name

# Pull feature
git flow feature pull origin feature-name
git flow feature track feature-name

# ===== RELEASE BRANCHES =====
# Start release
git flow release start 1.0.0
# Creates: release/1.0.0 from develop

# Finish release
git flow release finish 1.0.0
# Merges into main AND develop
# Tags main with version
# Deletes release branch

# Publish release
git flow release publish 1.0.0

# ===== HOTFIX BRANCHES =====
# Start hotfix
git flow hotfix start 1.0.1
# Creates: hotfix/1.0.1 from main

# Finish hotfix
git flow hotfix finish 1.0.1
# Merges into main AND develop
# Tags main with version
# Deletes hotfix branch
```

### Manual Git Flow (Without git-flow tool)
```bash
# ===== FEATURE WORKFLOW =====
# Start feature
git checkout develop
git checkout -b feature/user-authentication

# Work on feature
git add .
git commit -m "feat(auth): add login form"
git commit -m "feat(auth): implement JWT authentication"

# Update from develop
git checkout develop
git pull origin develop
git checkout feature/user-authentication
git merge develop  # or rebase

# Finish feature
git checkout develop
git merge --no-ff feature/user-authentication -m "Merge feature/user-authentication"
git push origin develop
git branch -d feature/user-authentication
git push origin --delete feature/user-authentication

# ===== RELEASE WORKFLOW =====
# Start release
git checkout develop
git checkout -b release/1.0.0

# Prepare release (version bumps, changelog)
git commit -am "chore(release): bump version to 1.0.0"

# Finish release
git checkout main
git merge --no-ff release/1.0.0 -m "Release v1.0.0"
git tag -a v1.0.0 -m "Version 1.0.0"
git push origin main --tags

git checkout develop
git merge --no-ff release/1.0.0 -m "Merge release/1.0.0 into develop"
git push origin develop

git branch -d release/1.0.0

# ===== HOTFIX WORKFLOW =====
# Start hotfix
git checkout main
git checkout -b hotfix/1.0.1

# Fix bug
git commit -am "fix(auth): resolve login timeout issue"

# Finish hotfix
git checkout main
git merge --no-ff hotfix/1.0.1 -m "Hotfix v1.0.1"
git tag -a v1.0.1 -m "Hotfix 1.0.1"
git push origin main --tags

git checkout develop
git merge --no-ff hotfix/1.0.1 -m "Merge hotfix/1.0.1 into develop"
git push origin develop

git branch -d hotfix/1.0.1
```

---

## 👥 TEAM COLLABORATION (4+ DEVELOPERS)

### Branch Naming Convention
```
┌─────────────────────────────────────────────────────────────────┐
│                    BRANCH NAMING CONVENTION                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  FORMAT: type/ticket-description                                │
│                                                                 │
│  EXAMPLES:                                                      │
│  feature/AUTH-123-user-login                                    │
│  feature/SHOP-456-checkout-page                                 │
│  bugfix/BUG-789-fix-cart-calculation                           │
│  hotfix/CRITICAL-001-security-patch                            │
│  release/v1.2.0                                                │
│  refactor/TECH-100-optimize-database                           │
│  docs/DOC-50-api-documentation                                 │
│  test/TEST-30-add-unit-tests                                   │
│                                                                 │
│  PREFIXES:                                                      │
│  feature/  - New functionality                                  │
│  bugfix/   - Bug fixes (non-critical)                          │
│  hotfix/   - Critical production fixes                         │
│  release/  - Release preparation                               │
│  refactor/ - Code refactoring                                  │
│  docs/     - Documentation only                                │
│  test/     - Adding/fixing tests                               │
│  chore/    - Maintenance tasks                                 │
│  experiment/ - Experimental features                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Commit Message Convention (Conventional Commits)
```bash
# FORMAT
<type>(<scope>): <description>

[optional body]

[optional footer(s)]

# TYPES
feat     - New feature
fix      - Bug fix
docs     - Documentation only
style    - Formatting (no code change)
refactor - Code change (no feature/fix)
perf     - Performance improvement
test     - Adding tests
chore    - Maintenance
ci       - CI/CD changes
build    - Build system changes
revert   - Revert previous commit

# EXAMPLES
feat(auth): add Google OAuth login
fix(cart): resolve quantity calculation bug
docs(api): update endpoint documentation
style(ui): format button components
refactor(db): optimize user queries
perf(images): implement lazy loading
test(auth): add login unit tests
chore(deps): update dependencies
ci(github): add automated testing workflow
build(docker): optimize image size

# WITH BODY AND FOOTER
feat(payment): integrate Stripe payment gateway

Implement Stripe checkout flow with:
- Card payment support
- Saved payment methods
- Webhook handling

Closes #123
BREAKING CHANGE: Payment API response format changed
```

### Pull Request Workflow
```bash
# ===== DEVELOPER WORKFLOW =====

# 1. Update local develop
git checkout develop
git pull origin develop

# 2. Create feature branch
git checkout -b feature/AUTH-123-user-login

# 3. Work on feature (multiple commits)
git add .
git commit -m "feat(auth): create login form component"
git commit -m "feat(auth): implement login API"
git commit -m "feat(auth): add form validation"
git commit -m "test(auth): add login unit tests"

# 4. Push to remote
git push -u origin feature/AUTH-123-user-login

# 5. Create Pull Request (GitHub/GitLab/Bitbucket)
# - Title: [AUTH-123] Implement user login
# - Description: Feature details, screenshots
# - Reviewers: Assign team members
# - Labels: feature, needs-review

# 6. Address review comments
git add .
git commit -m "fix(auth): address review feedback"
git push

# 7. After approval, merge (via UI or command)
# Squash merge recommended for clean history

# 8. Delete feature branch
git checkout develop
git pull origin develop
git branch -d feature/AUTH-123-user-login
```

### Code Review Process
```
┌─────────────────────────────────────────────────────────────────┐
│                    CODE REVIEW CHECKLIST                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ☐ FUNCTIONALITY                                               │
│    • Does it work as expected?                                 │
│    • Are edge cases handled?                                   │
│    • Is error handling appropriate?                            │
│                                                                 │
│  ☐ CODE QUALITY                                                │
│    • Is code readable and maintainable?                        │
│    • Are naming conventions followed?                          │
│    • Is there code duplication?                                │
│    • Are functions/methods too long?                           │
│                                                                 │
│  ☐ TESTING                                                     │
│    • Are there adequate tests?                                 │
│    • Do all tests pass?                                        │
│    • Is test coverage sufficient?                              │
│                                                                 │
│  ☐ SECURITY                                                    │
│    • Are there security vulnerabilities?                       │
│    • Is input validated?                                       │
│    • Are sensitive data handled properly?                      │
│                                                                 │
│  ☐ PERFORMANCE                                                 │
│    • Are there performance issues?                             │
│    • Are database queries optimized?                           │
│    • Is caching implemented where needed?                      │
│                                                                 │
│  ☐ DOCUMENTATION                                               │
│    • Is code documented where necessary?                       │
│    • Is README updated?                                        │
│    • Are API changes documented?                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Team Workflow for 4+ Developers
```
┌─────────────────────────────────────────────────────────────────────────┐
│               TEAM WORKFLOW (4+ DEVELOPERS)                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ROLES:                                                                 │
│  • Tech Lead        - Merge to main, release management                │
│  • Senior Dev (2+)  - Code review, merge to develop                    │
│  • Junior Dev (2+)  - Feature development, bugfixes                    │
│                                                                         │
│  BRANCH PROTECTION RULES:                                               │
│  ─────────────────────                                                  │
│  main:                                                                  │
│    • Require PR with 2 approvals                                       │
│    • Require status checks (CI/CD)                                     │
│    • No direct push                                                    │
│    • Only Tech Lead can merge                                          │
│                                                                         │
│  develop:                                                               │
│    • Require PR with 1 approval                                        │
│    • Require status checks                                             │
│    • No direct push                                                    │
│    • Senior+ can merge                                                 │
│                                                                         │
│  WORKFLOW:                                                              │
│  ──────────                                                             │
│                                                                         │
│  1. PLANNING                                                            │
│     └── Sprint planning → Create tickets → Assign developers           │
│                                                                         │
│  2. DEVELOPMENT                                                         │
│     └── Create branch → Develop → Push → Create PR                     │
│                                                                         │
│  3. CODE REVIEW                                                         │
│     └── Assign reviewers → Review → Request changes/Approve            │
│                                                                         │
│  4. MERGE TO DEVELOP                                                    │
│     └── Squash merge → Delete branch → Deploy to staging               │
│                                                                         │
│  5. TESTING                                                             │
│     └── QA testing on staging → Report bugs → Fix                      │
│                                                                         │
│  6. RELEASE                                                             │
│     └── Create release branch → Final testing → Merge to main          │
│                                                                         │
│  7. DEPLOYMENT                                                          │
│     └── Tag release → Deploy to production → Monitor                   │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  DAILY WORKFLOW:                                                        │
│  ───────────────                                                        │
│                                                                         │
│  Morning:                                                               │
│    git checkout develop                                                 │
│    git pull origin develop                                              │
│    git checkout feature/my-feature                                      │
│    git merge develop (or rebase)                                        │
│                                                                         │
│  During work:                                                           │
│    git add .                                                            │
│    git commit -m "feat(scope): description"                             │
│    git push origin feature/my-feature                                   │
│                                                                         │
│  End of day:                                                            │
│    git push origin feature/my-feature                                   │
│    Update PR status                                                     │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Trunk-Based Development (Alternative)
```
┌─────────────────────────────────────────────────────────────────┐
│               TRUNK-BASED DEVELOPMENT                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  main (trunk)                                                   │
│  ══════●═══●═══●═══●═══●═══●═══●═══●═══●═══●═══►              │
│        ↑   ↑   ↑   ↑   ↑   ↑   ↑   ↑   ↑   ↑                   │
│        │   │   │   │   │   │   │   │   │   │                   │
│        ●   ●   │   ●   │   ●   │   ●───●   │                   │
│       (1) (2)  │  (3)  │  (4)  │  (5)      │                   │
│                │       │       │           │                   │
│                ●───●   ●       ●───●───●   │                   │
│               (6)     (7)    (8)           │                   │
│                                            │                   │
│  release/v1.0 ─────────────────────────────●───►               │
│                                                                 │
│  RULES:                                                        │
│  • Small, frequent commits to main                             │
│  • Feature flags for incomplete features                       │
│  • Short-lived branches (< 1 day)                             │
│  • Strong CI/CD pipeline                                       │
│  • Release branches cut from main                              │
│                                                                 │
│  BENEFITS:                                                     │
│  ✓ Faster integration                                         │
│  ✓ Fewer merge conflicts                                      │
│  ✓ Continuous deployment ready                                │
│  ✓ Better code visibility                                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⚔️ CONFLICT RESOLUTION

### Understanding Conflicts
```bash
# Conflict markers in files:
<<<<<<< HEAD
Your changes (current branch)
=======
Their changes (incoming branch)
>>>>>>> feature-branch

# Sometimes with ancestor:
<<<<<<< HEAD
Your changes
||||||| merged common ancestor
Original code
=======
Their changes
>>>>>>> feature-branch
```

### Resolving Conflicts
```bash
# ===== DURING MERGE =====
git merge feature-branch
# CONFLICT message appears

# View conflicted files
git status
git diff --name-only --diff-filter=U

# Option 1: Edit manually
vim conflicted-file.txt
# Remove conflict markers, keep desired code
git add conflicted-file.txt
git commit

# Option 2: Use merge tool
git mergetool
# Opens configured tool (VS Code, vim, etc.)

# Option 3: Accept one side completely
git checkout --ours file.txt    # Keep current branch version
git checkout --theirs file.txt  # Keep incoming branch version

# Abort merge
git merge --abort

# ===== DURING REBASE =====
git rebase main
# CONFLICT message appears

# Fix conflicts
vim conflicted-file.txt
git add conflicted-file.txt
git rebase --continue

# Skip this commit
git rebase --skip

# Abort rebase
git rebase --abort

# ===== DURING CHERRY-PICK =====
git cherry-pick COMMIT
# CONFLICT message appears

git add conflicted-file.txt
git cherry-pick --continue

# Abort
git cherry-pick --abort
```

### Conflict Prevention
```bash
# ===== REGULAR SYNC =====
# Sync feature branch with develop frequently
git checkout feature/my-feature
git fetch origin
git merge origin/develop  # or rebase

# ===== BEFORE MERGE =====
# Preview merge conflicts
git merge --no-commit --no-ff branch
git diff --cached
git merge --abort  # If conflicts exist, fix first

# ===== COMMUNICATION =====
# Let team know which files you're working on
# Break large features into smaller PRs
# Use feature flags for long-running features
```

### Complex Conflict Scenarios
```bash
# ===== RERERE (Reuse Recorded Resolution) =====
# Enable rerere
git config --global rerere.enabled true

# Git remembers how you resolved conflicts
# and applies same resolution automatically

# View recorded resolutions
ls .git/rr-cache/

# Forget resolution
git rerere forget file.txt

# ===== THREE-WAY MERGE WITH DIFF3 =====
git config --global merge.conflictStyle diff3

# Shows:
# <<<<<<< HEAD
# your changes
# ||||||| ancestor
# original
# =======
# their changes
# >>>>>>> branch

# ===== OURS/THEIRS STRATEGY =====
# For merge
git merge -X ours branch     # Prefer our changes
git merge -X theirs branch   # Prefer their changes

# For specific file during conflict
git checkout --ours path/to/file
git checkout --theirs path/to/file
```

---

## 📚 GIT BEST PRACTICES

### Commit Best Practices
```bash
# ✓ DO
- Commit early and often
- Write meaningful commit messages
- Keep commits focused (one logical change)
- Test before committing
- Use present tense ("Add feature" not "Added feature")

# ✗ DON'T
- Commit generated files (build, node_modules)
- Commit sensitive data (passwords, keys)
- Make huge commits
- Commit broken code
- Use vague messages ("fix", "update", "changes")
```

### Branching Best Practices
```bash
# ✓ DO
- Keep branches short-lived
- Delete merged branches
- Use descriptive branch names
- Sync with base branch regularly
- Protect main/develop branches

# ✗ DON'T
- Work directly on main
- Keep stale branches
- Use personal names as branch names
- Let branches diverge too much
```

### .gitignore Template
```gitignore
# ===== DEPENDENCIES =====
node_modules/
vendor/
bower_components/
.pnp/
.pnp.js

# ===== BUILD =====
dist/
build/
out/
target/
*.class
*.jar
*.war

# ===== IDE =====
.idea/
.vscode/
*.swp
*.swo
*.sublime-*
.project
.settings/

# ===== OS =====
.DS_Store
Thumbs.db
*.log

# ===== ENVIRONMENT =====
.env
.env.local
.env.*.local
*.local

# ===== SECRETS =====
*.pem
*.key
*.p12
secrets/
credentials/

# ===== CACHE =====
.cache/
.tmp/
*.cache
__pycache__/
*.py[cod]

# ===== TESTING =====
coverage/
.nyc_output/
*.lcov

# ===== MISC =====
*.bak
*.backup
*.temp
*.tmp
```

### Git Aliases (Productivity)
```bash
# ~/.gitconfig

[alias]
    # Basic shortcuts
    co = checkout
    ci = commit
    br = branch
    st = status
    
    # Logging
    lg = log --oneline --graph --decorate --all
    ll = log --pretty=format:'%C(yellow)%h%Creset %s %C(cyan)(%cr)%Creset %C(green)<%an>%Creset' --abbrev-commit
    last = log -1 HEAD
    
    # Branch management
    branches = branch -a
    remotes = remote -v
    contributors = shortlog -sn
    
    # Diff
    df = diff
    dc = diff --cached
    
    # Undo
    unstage = reset HEAD --
    undo = reset --soft HEAD~1
    amend = commit --amend --no-edit
    
    # Cleanup
    cleanup = !git branch --merged | grep -v '\\*\\|main\\|develop' | xargs -n 1 git branch -d
    
    # Stash
    sl = stash list
    sp = stash pop
    ss = stash save
    
    # Work in progress
    wip = !git add -A && git commit -m 'WIP'
    unwip = reset HEAD~1
    
    # Sync
    sync = !git fetch --all --prune && git pull --rebase
    
    # Aliases list
    aliases = config --get-regexp alias
```

---

## 📊 GIT QUICK REFERENCE

### Most Used Commands
| Command | Description |
|---------|-------------|
| `git clone URL` | Clone repository |
| `git status` | Check status |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Commit with message |
| `git push` | Push to remote |
| `git pull` | Fetch and merge |
| `git checkout -b branch` | Create and switch branch |
| `git merge branch` | Merge branch |
| `git stash` | Stash changes |
| `git stash pop` | Apply stashed changes |
| `git log --oneline` | View commit history |
| `git diff` | View changes |
| `git reset --hard HEAD` | Discard all changes |
| `git rebase main` | Rebase onto main |

### Git Flow Quick Reference
| Action | Command |
|--------|---------|
| Start feature | `git checkout -b feature/name develop` |
| Finish feature | `git checkout develop && git merge --no-ff feature/name` |
| Start release | `git checkout -b release/v1.0 develop` |
| Finish release | Merge to main + develop, tag |
| Start hotfix | `git checkout -b hotfix/v1.0.1 main` |
| Finish hotfix | Merge to main + develop, tag |

### Conflict Resolution Quick Reference
| Situation | Command |
|-----------|---------|
| View conflicts | `git status` |
| Accept ours | `git checkout --ours file` |
| Accept theirs | `git checkout --theirs file` |
| Use merge tool | `git mergetool` |
| Abort merge | `git merge --abort` |
| Continue after fix | `git add file && git commit` |

---

**Author:** TangselSecTeam  
**Version:** 1.2  
**Last Updated:** January 2026

