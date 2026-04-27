# 🔥 Complete Firewall Hardening Cheatsheet
## firewalld, UFW, CSF, iptables - Full Security Commands

---

## 📋 Table of Contents
1. [IPTABLES](#1-iptables)
2. [FIREWALLD](#2-firewalld)
3. [UFW (Uncomplicated Firewall)](#3-ufw-uncomplicated-firewall)
4. [CSF (ConfigServer Security & Firewall)](#4-csf-configserver-security--firewall)
5. [Comparison Table](#5-comparison-table)

---

# 1. IPTABLES

## 🔧 Basic Commands

```bash
# Lihat semua rules
iptables -L -v -n
iptables -L -v -n --line-numbers

# Simpan rules
iptables-save > /etc/iptables/rules.v4
ip6tables-save > /etc/iptables/rules.v6

# Restore rules
iptables-restore < /etc/iptables/rules.v4

# Flush semua rules (HATI-HATI!)
iptables -F
iptables -X
iptables -t nat -F
iptables -t mangle -F

# Set default policy
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT
```

## 🛡️ Anti-DDoS Protection

### SYN Flood Protection
```bash
# Limit SYN packets
iptables -A INPUT -p tcp --syn -m limit --limit 1/s --limit-burst 3 -j ACCEPT
iptables -A INPUT -p tcp --syn -j DROP

# SYN cookies (kernel level)
echo 1 > /proc/sys/net/ipv4/tcp_syncookies
echo "net.ipv4.tcp_syncookies = 1" >> /etc/sysctl.conf

# Limit new connections per IP
iptables -A INPUT -p tcp --dport 80 --syn -m connlimit --connlimit-above 20 -j DROP
iptables -A INPUT -p tcp --dport 443 --syn -m connlimit --connlimit-above 20 -j DROP
```

### UDP Flood Protection
```bash
# Limit UDP packets
iptables -A INPUT -p udp -m limit --limit 10/s --limit-burst 20 -j ACCEPT
iptables -A INPUT -p udp -j DROP

# Block UDP pada port tertentu (jika tidak digunakan)
iptables -A INPUT -p udp --dport 0:1024 -j DROP
```

### ICMP Flood Protection (Ping of Death)
```bash
# Limit ICMP
iptables -A INPUT -p icmp --icmp-type echo-request -m limit --limit 1/s --limit-burst 4 -j ACCEPT
iptables -A INPUT -p icmp --icmp-type echo-request -j DROP

# Block semua ICMP (optional)
iptables -A INPUT -p icmp -j DROP

# Allow essential ICMP types only
iptables -A INPUT -p icmp --icmp-type destination-unreachable -j ACCEPT
iptables -A INPUT -p icmp --icmp-type time-exceeded -j ACCEPT
iptables -A INPUT -p icmp --icmp-type echo-reply -j ACCEPT
```

### HTTP/HTTPS Rate Limiting
```bash
# Rate limit HTTP
iptables -A INPUT -p tcp --dport 80 -m state --state NEW -m recent --set
iptables -A INPUT -p tcp --dport 80 -m state --state NEW -m recent --update --seconds 60 --hitcount 20 -j DROP

# Rate limit HTTPS
iptables -A INPUT -p tcp --dport 443 -m state --state NEW -m recent --set
iptables -A INPUT -p tcp --dport 443 -m state --state NEW -m recent --update --seconds 60 --hitcount 20 -j DROP

# Limit connections per second
iptables -A INPUT -p tcp --dport 80 -m hashlimit --hashlimit-name http --hashlimit 50/sec --hashlimit-burst 100 --hashlimit-mode srcip -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j DROP
```

### Slowloris Protection
```bash
# Limit concurrent connections per IP
iptables -A INPUT -p tcp --dport 80 -m connlimit --connlimit-above 50 --connlimit-mask 32 -j REJECT

# Connection timeout
iptables -A INPUT -p tcp --dport 80 -m state --state NEW -m recent --set --name slowloris
iptables -A INPUT -p tcp --dport 80 -m state --state NEW -m recent --update --seconds 60 --hitcount 10 --name slowloris -j DROP
```

## 🚫 Block Invalid Packets

```bash
# Drop invalid packets
iptables -A INPUT -m state --state INVALID -j DROP

# Drop NULL packets
iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP

# Drop XMAS packets
iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP

# Drop FIN scan
iptables -A INPUT -p tcp --tcp-flags ALL FIN -j DROP

# Drop SYN-FIN attack
iptables -A INPUT -p tcp --tcp-flags SYN,FIN SYN,FIN -j DROP

# Drop SYN-RST attack
iptables -A INPUT -p tcp --tcp-flags SYN,RST SYN,RST -j DROP

# Drop fragments
iptables -A INPUT -f -j DROP

# Block bogus TCP flags
iptables -A INPUT -p tcp --tcp-flags FIN,SYN FIN,SYN -j DROP
iptables -A INPUT -p tcp --tcp-flags FIN,RST FIN,RST -j DROP
iptables -A INPUT -p tcp --tcp-flags FIN,ACK FIN -j DROP
iptables -A INPUT -p tcp --tcp-flags ACK,URG URG -j DROP
iptables -A INPUT -p tcp --tcp-flags PSH,ACK PSH -j DROP
```

## 🔒 Port Knocking
```bash
# Buat chain untuk port knocking
iptables -N KNOCKING
iptables -N GATE1
iptables -N GATE2
iptables -N GATE3
iptables -N PASSED

# Knock sequence: 7000 -> 8000 -> 9000 -> SSH opens
iptables -A GATE1 -p tcp --dport 7000 -m recent --name AUTH1 --set -j DROP
iptables -A GATE1 -j DROP

iptables -A GATE2 -m recent --name AUTH1 --remove
iptables -A GATE2 -p tcp --dport 8000 -m recent --name AUTH2 --set -j DROP
iptables -A GATE2 -j GATE1

iptables -A GATE3 -m recent --name AUTH2 --remove
iptables -A GATE3 -p tcp --dport 9000 -m recent --name AUTH3 --set -j DROP
iptables -A GATE3 -j GATE1

iptables -A PASSED -m recent --name AUTH3 --remove
iptables -A PASSED -p tcp --dport 22 -j ACCEPT
iptables -A PASSED -j GATE1

iptables -A KNOCKING -m recent --rcheck --seconds 30 --name AUTH3 -j PASSED
iptables -A KNOCKING -m recent --rcheck --seconds 10 --name AUTH2 -j GATE3
iptables -A KNOCKING -m recent --rcheck --seconds 10 --name AUTH1 -j GATE2
iptables -A KNOCKING -j GATE1

iptables -A INPUT -p tcp --dport 22 -j KNOCKING
```

## 🔐 SSH Brute Force Protection
```bash
# Limit SSH connections
iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set --name SSH
iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --update --seconds 60 --hitcount 4 --name SSH -j DROP

# Alternative: hashlimit
iptables -A INPUT -p tcp --dport 22 -m hashlimit --hashlimit 3/min --hashlimit-burst 3 --hashlimit-mode srcip --hashlimit-name ssh -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j DROP

# Block after 3 failed attempts
iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set --name sshattack
iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --rcheck --seconds 180 --hitcount 3 --name sshattack -j LOG --log-prefix "SSH Attack: "
iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --rcheck --seconds 180 --hitcount 3 --name sshattack -j DROP
```

## 🌍 GeoIP Blocking
```bash
# Install xtables-addons untuk geoip
apt install xtables-addons-common libtext-csv-xs-perl

# Download GeoIP database
/usr/lib/xtables-addons/xt_geoip_dl
/usr/lib/xtables-addons/xt_geoip_build -D /usr/share/xt_geoip *.csv

# Block specific countries
iptables -A INPUT -m geoip --src-cc CN,RU,KP -j DROP

# Allow only specific countries
iptables -A INPUT -m geoip ! --src-cc ID,SG,US -j DROP
```

## 📊 Logging
```bash
# Log dropped packets
iptables -A INPUT -j LOG --log-prefix "IPTables-Dropped: " --log-level 4
iptables -A INPUT -j DROP

# Log specific attacks
iptables -A INPUT -p tcp --dport 22 -m limit --limit 5/min -j LOG --log-prefix "SSH attempt: "

# Log rate limited to prevent log flooding
iptables -A INPUT -m limit --limit 3/min --limit-burst 10 -j LOG --log-prefix "Firewall: "
```

## 📜 Complete Hardening Script

```bash
#!/bin/bash
# iptables-hardening.sh

# Flush existing rules
iptables -F
iptables -X
iptables -t nat -F
iptables -t mangle -F

# Default policies
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Allow loopback
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# Allow established connections
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Drop invalid packets
iptables -A INPUT -m state --state INVALID -j DROP
iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP
iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP
iptables -A INPUT -p tcp --tcp-flags SYN,FIN SYN,FIN -j DROP
iptables -A INPUT -p tcp --tcp-flags SYN,RST SYN,RST -j DROP
iptables -A INPUT -f -j DROP

# Anti-DDoS
iptables -A INPUT -p tcp --syn -m limit --limit 1/s --limit-burst 3 -j ACCEPT
iptables -A INPUT -p udp -m limit --limit 10/s --limit-burst 20 -j ACCEPT
iptables -A INPUT -p icmp --icmp-type echo-request -m limit --limit 1/s --limit-burst 4 -j ACCEPT

# SSH with rate limiting
iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --set --name SSH
iptables -A INPUT -p tcp --dport 22 -m state --state NEW -m recent --update --seconds 60 --hitcount 4 --name SSH -j DROP
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# HTTP/HTTPS with rate limiting
iptables -A INPUT -p tcp --dport 80 -m connlimit --connlimit-above 50 -j DROP
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -m connlimit --connlimit-above 50 -j DROP
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Log and drop everything else
iptables -A INPUT -m limit --limit 3/min -j LOG --log-prefix "IPTables-Dropped: "
iptables -A INPUT -j DROP

# Save rules
iptables-save > /etc/iptables/rules.v4

echo "Firewall hardening complete!"
```

---

# 2. FIREWALLD

## 🔧 Basic Commands

```bash
# Status dan info
systemctl status firewalld
firewall-cmd --state
firewall-cmd --get-active-zones
firewall-cmd --get-default-zone
firewall-cmd --list-all
firewall-cmd --list-all-zones

# Start/Stop/Enable
systemctl start firewalld
systemctl stop firewalld
systemctl enable firewalld
systemctl restart firewalld

# Reload tanpa kehilangan state
firewall-cmd --reload
firewall-cmd --complete-reload

# Set default zone
firewall-cmd --set-default-zone=drop
```

## 🛡️ Anti-DDoS Protection

### Rate Limiting dengan Rich Rules
```bash
# Rate limit SSH (max 3 connections per minute)
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" service name="ssh" limit value="3/m" accept'

# Rate limit HTTP (max 25 connections per second)
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" port port="80" protocol="tcp" limit value="25/s" accept'

# Rate limit HTTPS
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" port port="443" protocol="tcp" limit value="25/s" accept'

# Limit new connections
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" port port="80" protocol="tcp" limit value="100/m" accept'

# Apply changes
firewall-cmd --reload
```

### Block Specific Attacks
```bash
# Drop ICMP flood
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" protocol value="icmp" limit value="1/s" accept'
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" protocol value="icmp" drop'

# Block ping completely (optional)
firewall-cmd --permanent --add-icmp-block=echo-request
firewall-cmd --permanent --add-icmp-block=echo-reply

# Drop all traffic from suspicious IP
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="1.2.3.4" drop'

# Drop traffic from IP range
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.1.0/24" drop'

# Limit connections per source IP
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" service name="http" limit value="10/s" burst="50" accept'
```

### SYN Flood Protection
```bash
# Create custom zone for DDoS protection
firewall-cmd --permanent --new-zone=antiddos

# Set drop as default
firewall-cmd --permanent --zone=antiddos --set-target=DROP

# Add rate-limited services
firewall-cmd --permanent --zone=antiddos --add-rich-rule='rule family="ipv4" port port="80" protocol="tcp" limit value="50/s" accept'
firewall-cmd --permanent --zone=antiddos --add-rich-rule='rule family="ipv4" port port="443" protocol="tcp" limit value="50/s" accept'
firewall-cmd --permanent --zone=antiddos --add-rich-rule='rule family="ipv4" port port="22" protocol="tcp" limit value="3/m" accept'

# Activate zone
firewall-cmd --reload
firewall-cmd --zone=antiddos --change-interface=eth0
```

## 🔐 SSH Brute Force Protection

```bash
# Limit SSH connections
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" service name="ssh" limit value="3/m" accept'

# Allow SSH only from specific IP
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.1.100" service name="ssh" accept'

# Block SSH from everyone else
firewall-cmd --permanent --remove-service=ssh

# Log SSH attempts
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" service name="ssh" log prefix="SSH-Access: " level="info" limit value="3/m"'
```

## 🚫 Block IPs & Networks

```bash
# Block single IP
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="10.0.0.1" reject'
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="10.0.0.1" drop'

# Block network range
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="10.0.0.0/8" drop'

# Block country using ipset (requires ipset)
firewall-cmd --permanent --new-ipset=blacklist --type=hash:net
firewall-cmd --permanent --ipset=blacklist --add-entry=1.2.3.0/24
firewall-cmd --permanent --add-rich-rule='rule source ipset="blacklist" drop'

# Whitelist IP (allow before drop)
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.1.0/24" accept' --priority=-100
```

## 🔒 Port Management

```bash
# Allow specific ports
firewall-cmd --permanent --add-port=80/tcp
firewall-cmd --permanent --add-port=443/tcp
firewall-cmd --permanent --add-port=8080-8090/tcp

# Remove ports
firewall-cmd --permanent --remove-port=80/tcp

# Allow service
firewall-cmd --permanent --add-service=http
firewall-cmd --permanent --add-service=https
firewall-cmd --permanent --add-service=ssh

# List available services
firewall-cmd --get-services
```

## 📊 Logging

```bash
# Enable logging for dropped packets
firewall-cmd --set-log-denied=all
firewall-cmd --set-log-denied=unicast
firewall-cmd --set-log-denied=broadcast
firewall-cmd --set-log-denied=multicast
firewall-cmd --set-log-denied=off

# Log specific rules
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" port port="22" protocol="tcp" log prefix="SSH: " level="warning" limit value="3/m" accept'

# View logs
journalctl -f -u firewalld
tail -f /var/log/firewalld
```

## 📜 Complete Hardening Script

```bash
#!/bin/bash
# firewalld-hardening.sh

# Ensure firewalld is running
systemctl start firewalld
systemctl enable firewalld

# Set default zone to drop
firewall-cmd --set-default-zone=drop

# Allow loopback
firewall-cmd --permanent --zone=trusted --add-interface=lo

# Allow established connections (automatic in firewalld)

# Rate limited SSH
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" service name="ssh" limit value="3/m" accept'

# Rate limited HTTP/HTTPS
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" port port="80" protocol="tcp" limit value="25/s" accept'
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" port port="443" protocol="tcp" limit value="25/s" accept'

# ICMP rate limiting
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" protocol value="icmp" limit value="1/s" accept'

# Enable logging for dropped packets
firewall-cmd --set-log-denied=all

# Reload
firewall-cmd --reload

echo "Firewalld hardening complete!"
firewall-cmd --list-all
```

---

# 3. UFW (Uncomplicated Firewall)

## 🔧 Basic Commands

```bash
# Status
ufw status
ufw status verbose
ufw status numbered

# Enable/Disable
ufw enable
ufw disable
ufw reload

# Reset semua rules
ufw reset

# Default policies
ufw default deny incoming
ufw default allow outgoing
ufw default deny forward

# Logging
ufw logging on
ufw logging medium
ufw logging high
ufw logging full
```

## 🛡️ Anti-DDoS Protection

### Rate Limiting
```bash
# Rate limit SSH (6 connections per 30 seconds)
ufw limit ssh
ufw limit 22/tcp

# Rate limit specific port
ufw limit 80/tcp
ufw limit 443/tcp

# Custom rate limit dengan iptables (UFW uses iptables backend)
# Edit /etc/ufw/before.rules - add before *filter:

# Rate limit HTTP
-A ufw-before-input -p tcp --dport 80 -m state --state NEW -m recent --set --name HTTP
-A ufw-before-input -p tcp --dport 80 -m state --state NEW -m recent --update --seconds 60 --hitcount 20 --name HTTP -j DROP

# Rate limit HTTPS
-A ufw-before-input -p tcp --dport 443 -m state --state NEW -m recent --set --name HTTPS
-A ufw-before-input -p tcp --dport 443 -m state --state NEW -m recent --update --seconds 60 --hitcount 20 --name HTTPS -j DROP
```

### SYN Flood Protection
Edit `/etc/ufw/before.rules` - add after `*filter`:

```bash
# SYN flood protection
-A ufw-before-input -p tcp --syn -m limit --limit 1/s --limit-burst 3 -j ACCEPT
-A ufw-before-input -p tcp --syn -j DROP

# Connection limit per IP
-A ufw-before-input -p tcp --dport 80 -m connlimit --connlimit-above 50 -j DROP
-A ufw-before-input -p tcp --dport 443 -m connlimit --connlimit-above 50 -j DROP

# Drop invalid packets
-A ufw-before-input -m state --state INVALID -j DROP

# Drop NULL packets
-A ufw-before-input -p tcp --tcp-flags ALL NONE -j DROP

# Drop XMAS packets
-A ufw-before-input -p tcp --tcp-flags ALL ALL -j DROP
```

### ICMP Protection
Edit `/etc/ufw/before.rules`:

```bash
# Rate limit ICMP
-A ufw-before-input -p icmp --icmp-type echo-request -m limit --limit 1/s --limit-burst 4 -j ACCEPT
-A ufw-before-input -p icmp --icmp-type echo-request -j DROP

# Or block ICMP completely
-A ufw-before-input -p icmp --icmp-type echo-request -j DROP
```

## 🔐 SSH Brute Force Protection

```bash
# Basic rate limiting
ufw limit ssh

# Allow SSH from specific IP only
ufw allow from 192.168.1.100 to any port 22

# Deny SSH from all others
ufw deny 22

# Allow SSH from subnet
ufw allow from 192.168.1.0/24 to any port 22

# Log SSH attempts - add to /etc/ufw/before.rules:
-A ufw-before-input -p tcp --dport 22 -m limit --limit 3/min -j LOG --log-prefix "UFW-SSH: "
```

## 🚫 Block IPs & Networks

```bash
# Block single IP
ufw deny from 1.2.3.4
ufw deny from 1.2.3.4 to any

# Block network
ufw deny from 10.0.0.0/8

# Block IP on specific port
ufw deny from 1.2.3.4 to any port 80

# Insert rule at specific position (higher priority)
ufw insert 1 deny from 1.2.3.4

# Block outgoing to IP
ufw deny out to 1.2.3.4

# Block with reject (sends ICMP unreachable)
ufw reject from 1.2.3.4
```

## 🔒 Port Management

```bash
# Allow ports
ufw allow 80/tcp
ufw allow 443/tcp
ufw allow 22/tcp

# Allow port range
ufw allow 8000:8100/tcp

# Allow service by name
ufw allow http
ufw allow https
ufw allow ssh

# Allow from specific IP to port
ufw allow from 192.168.1.0/24 to any port 22

# Delete rules
ufw delete allow 80/tcp
ufw delete 3  # by number

# Deny ports
ufw deny 23/tcp  # telnet
ufw deny 21/tcp  # ftp
```

## 📊 Application Profiles

```bash
# List app profiles
ufw app list

# Show app info
ufw app info "Apache Full"
ufw app info "Nginx Full"
ufw app info "OpenSSH"

# Allow application
ufw allow "Nginx Full"
ufw allow "Apache Full"
ufw allow "OpenSSH"

# Create custom app profile
# /etc/ufw/applications.d/myapp
[MyApp]
title=My Application
description=My custom application
ports=8080/tcp|8443/tcp
```

## 📜 Complete Hardening Script

```bash
#!/bin/bash
# ufw-hardening.sh

# Reset UFW
ufw --force reset

# Default policies
ufw default deny incoming
ufw default deny forward
ufw default allow outgoing

# Enable logging
ufw logging high

# Allow loopback
ufw allow in on lo
ufw allow out on lo

# Rate limited SSH
ufw limit ssh

# Allow HTTP/HTTPS
ufw allow 80/tcp
ufw allow 443/tcp

# Add anti-DDoS rules to before.rules
cat >> /etc/ufw/before.rules << 'EOF'
# Anti-DDoS rules
-A ufw-before-input -p tcp --syn -m limit --limit 1/s --limit-burst 3 -j ACCEPT
-A ufw-before-input -p tcp --dport 80 -m connlimit --connlimit-above 50 -j DROP
-A ufw-before-input -p tcp --dport 443 -m connlimit --connlimit-above 50 -j DROP
-A ufw-before-input -p icmp --icmp-type echo-request -m limit --limit 1/s -j ACCEPT
-A ufw-before-input -m state --state INVALID -j DROP
-A ufw-before-input -p tcp --tcp-flags ALL NONE -j DROP
-A ufw-before-input -p tcp --tcp-flags ALL ALL -j DROP
EOF

# Enable UFW
ufw --force enable

echo "UFW hardening complete!"
ufw status verbose
```

### Kernel Parameters untuk UFW
Edit `/etc/sysctl.conf`:

```bash
# Add these lines
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_max_syn_backlog = 2048
net.ipv4.tcp_synack_retries = 2
net.ipv4.tcp_syn_retries = 5
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1
net.ipv4.icmp_echo_ignore_broadcasts = 1
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.default.accept_source_route = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.default.send_redirects = 0
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv4.conf.all.log_martians = 1

# Apply
sysctl -p
```

---

# 4. CSF (ConfigServer Security & Firewall)

## 🔧 Installation

```bash
# Download dan install
cd /usr/src
wget https://download.configserver.com/csf.tgz
tar -xzf csf.tgz
cd csf
sh install.sh

# Check dependencies
perl /usr/local/csf/bin/csftest.pl

# Disable testing mode (WAJIB sebelum production)
sed -i 's/TESTING = "1"/TESTING = "0"/' /etc/csf/csf.conf
csf -r
```

## 🔧 Basic Commands

```bash
# Status
csf -s           # Start
csf -f           # Stop (flush)
csf -r           # Restart
csf -x           # Disable CSF
csf -e           # Enable CSF

# List rules
csf -l           # List all rules
csf -g IP        # Check if IP is blocked

# Version
csf -v

# Config test
csf -c
```

## 🛡️ Anti-DDoS Protection

### CSF Configuration (`/etc/csf/csf.conf`)

```bash
# ===== CONNLIMIT - Limit connections per IP =====
CONNLIMIT = "22;5,80;50,443;50"
# Format: port;limit
# SSH: 5 connections, HTTP/HTTPS: 50 connections per IP

# ===== PORTFLOOD - Rate limit connections =====
PORTFLOOD = "22;tcp;5;300,80;tcp;50;5,443;tcp;50;5"
# Format: port;protocol;hitcount;seconds
# SSH: 5 hits per 300 seconds
# HTTP/HTTPS: 50 hits per 5 seconds

# ===== SYNFLOOD Protection =====
SYNFLOOD = "1"
SYNFLOOD_RATE = "100/s"
SYNFLOOD_BURST = "150"

# ===== SYN Cookies =====
SYSCTL_CONF = "1"

# ===== Connection Tracking =====
CT_LIMIT = "300"
CT_INTERVAL = "30"
CT_BLOCK_TIME = "1800"
CT_SKIP_TIME_WAIT = "1"
CT_STATES = "SYN_RECV"

# ===== Port Scan Detection =====
PS_INTERVAL = "300"
PS_LIMIT = "10"
PS_PERMANENT = "0"
PS_BLOCK_TIME = "3600"

# ===== PACKET_FILTER - Drop invalid packets =====
PACKET_FILTER = "1"

# ===== DROP_NOLOG - Silently drop =====
DROP_NOLOG = "67,68,111,113,135:139,445,500,513,520"

# ===== ICMP Rate Limit =====
ICMP_IN = "1"
ICMP_IN_RATE = "1/s"
ICMP_OUT = "1"
ICMP_OUT_RATE = "0"

# ===== UDP Flood Protection =====
UDPFLOOD = "1"
UDPFLOOD_LIMIT = "100/s"
UDPFLOOD_BURST = "500"
UDPFLOOD_ALLOWUSER = "named"

# ===== Block Specific Countries =====
CC_DENY = "CN,RU,KP,IR"
CC_ALLOW = ""
CC_ALLOW_FILTER = ""
CC_DENY_PORTS = "22,25,80,443"
CC_ALLOW_PORTS = ""

# ===== LF_TRIGGER - Login Failure Daemon =====
LF_TRIGGER = "1"
LF_TRIGGER_PERM = "0"
LF_SELECT = "0"

# ===== Account Protection =====
LF_SSHD = "5"          # SSH failures before block
LF_SSHD_PERM = "1"     # Permanent block
LF_FTPD = "10"         # FTP failures
LF_SMTPAUTH = "5"      # SMTP auth failures
LF_POP3D = "10"        # POP3 failures
LF_IMAPD = "10"        # IMAP failures
LF_HTACCESS = "5"      # htaccess failures

# ===== Block Time =====
LF_PERMBLOCK = "1"
LF_PERMBLOCK_INTERVAL = "86400"
LF_PERMBLOCK_COUNT = "4"
LF_PERMBLOCK_ALERT = "1"

# ===== CLUSTER - Distributed blocking =====
CLUSTER_SENDTO = ""
CLUSTER_RECVFROM = ""
CLUSTER_KEY = "your_secret_key"
```

## 🔐 SSH Brute Force Protection

```bash
# Set in csf.conf
LF_SSHD = "3"              # Block after 3 failures
LF_SSHD_PERM = "1"         # Permanent block (1) or temporary (0)

# Temporary block settings
LF_SSHD_PERM = "0"
LF_TRIGGER_PERM = "300"    # Block for 300 seconds

# Change SSH port (recommended)
TCP_IN = "2222,80,443"     # Use custom SSH port
TCP_OUT = "2222,80,443,53"
```

## 🚫 Block/Allow IPs

```bash
# Block IP permanently
csf -d 1.2.3.4
csf -d 1.2.3.4 "Reason for blocking"

# Block temporarily (seconds)
csf -td 1.2.3.4 3600
csf -td 1.2.3.4 3600 "Blocked for 1 hour"

# Unblock IP
csf -dr 1.2.3.4

# Allow IP (whitelist)
csf -a 1.2.3.4
csf -a 1.2.3.4 "Trusted IP"

# Remove from allow list
csf -ar 1.2.3.4

# Temporary allow
csf -ta 1.2.3.4 3600 "Temporary access"

# Ignore IP (never block)
# Add to /etc/csf/csf.ignore
echo "1.2.3.4" >> /etc/csf/csf.ignore
csf -r

# Check IP status
csf -g 1.2.3.4
```

## 📂 Important CSF Files

```bash
/etc/csf/csf.conf        # Main configuration
/etc/csf/csf.allow       # Whitelist IPs
/etc/csf/csf.deny        # Blacklist IPs
/etc/csf/csf.ignore      # Ignored IPs (won't be blocked)
/etc/csf/csf.tempallow   # Temporary whitelist
/etc/csf/csf.tempdeny    # Temporary blacklist
/etc/csf/csf.syslogs     # Log files to watch
/etc/csf/csf.dirwatch    # Directories to monitor
/etc/csf/csf.pignore     # Process ignore list
/etc/csf/csf.fignore     # File ignore list
```

## 📊 Monitoring & Alerts

```bash
# Enable email alerts
LF_ALERT_TO = "admin@example.com"
LF_ALERT_FROM = "csf@example.com"

# Alert on SSH login
LF_SSH_EMAIL_ALERT = "1"

# Alert on blocked IPs
LF_EMAIL_ALERT = "1"

# View statistics
csf -t              # Show temporary blocks
csf -l              # List all rules

# Watch logs
tail -f /var/log/lfd.log
tail -f /var/log/messages | grep csf
```

## 📜 Complete CSF Configuration

```bash
#!/bin/bash
# csf-hardening.sh

# Backup original config
cp /etc/csf/csf.conf /etc/csf/csf.conf.backup

# Edit configuration
cat > /tmp/csf_settings.txt << 'EOF'
TESTING = "0"
TCP_IN = "22,80,443"
TCP_OUT = "20,21,22,25,53,80,110,113,443,587,993,995"
UDP_IN = ""
UDP_OUT = "20,21,53,113,123"

# Anti-DDoS
SYNFLOOD = "1"
SYNFLOOD_RATE = "100/s"
SYNFLOOD_BURST = "150"
CONNLIMIT = "22;5,80;50,443;50"
PORTFLOOD = "22;tcp;5;300,80;tcp;50;5,443;tcp;50;5"

# Login Failure
LF_SSHD = "3"
LF_SSHD_PERM = "1"
LF_FTPD = "5"
LF_SMTPAUTH = "5"

# ICMP
ICMP_IN = "1"
ICMP_IN_RATE = "1/s"

# Port Scan
PS_INTERVAL = "300"
PS_LIMIT = "10"

# Connection Tracking
CT_LIMIT = "300"
CT_INTERVAL = "30"
CT_BLOCK_TIME = "1800"

# Packet Filter
PACKET_FILTER = "1"

# Country Blocking (example)
CC_DENY = ""
CC_ALLOW = ""
EOF

echo "CSF Settings prepared. Edit /etc/csf/csf.conf manually or use:"
echo "Review settings and apply with: csf -r"

# Restart CSF
csf -r

echo "CSF hardening configured!"
```

## 🔧 CSF Integration dengan cPanel/WHM

```bash
# Access via WHM
WHM > Plugins > ConfigServer Security & Firewall

# Quick Commands via WHM
# - Firewall Allow/Deny
# - Quick Allow
# - Quick Deny
# - Temporary Allow/Deny

# Enable CSF UI
CSF_UI = "1"
CSF_UI_IP = ""
CSF_UI_PORT = "6666"
CSF_UI_USER = "admin"
CSF_UI_PASS = "strongpassword"
```

---

# 5. Comparison Table

## Feature Comparison

| Feature | iptables | firewalld | UFW | CSF |
|---------|----------|-----------|-----|-----|
| **Complexity** | High | Medium | Low | Medium |
| **Learning Curve** | Steep | Moderate | Easy | Moderate |
| **Dynamic Rules** | Manual | Yes | Limited | Yes |
| **Zones Support** | No | Yes | No | Limited |
| **Rate Limiting** | Yes | Yes (rich rules) | Yes | Yes |
| **GeoIP Blocking** | With modules | With ipset | Manual | Built-in |
| **Brute Force Detection** | Manual | Manual | Manual | Built-in (lfd) |
| **Email Alerts** | External | External | External | Built-in |
| **Web UI** | No | Cockpit | No | Yes |
| **Best For** | Advanced users | RHEL/CentOS | Ubuntu/Debian | cPanel servers |

## Quick Reference Commands

| Action | iptables | firewalld | UFW | CSF |
|--------|----------|-----------|-----|-----|
| **Start** | `systemctl start iptables` | `systemctl start firewalld` | `ufw enable` | `csf -s` |
| **Stop** | `systemctl stop iptables` | `systemctl stop firewalld` | `ufw disable` | `csf -f` |
| **Status** | `iptables -L` | `firewall-cmd --list-all` | `ufw status` | `csf -l` |
| **Allow Port** | `iptables -A INPUT -p tcp --dport 80 -j ACCEPT` | `firewall-cmd --add-port=80/tcp` | `ufw allow 80` | Edit csf.conf |
| **Block IP** | `iptables -A INPUT -s 1.2.3.4 -j DROP` | `firewall-cmd --add-rich-rule='...'` | `ufw deny from 1.2.3.4` | `csf -d 1.2.3.4` |
| **Allow IP** | `iptables -A INPUT -s 1.2.3.4 -j ACCEPT` | `firewall-cmd --add-rich-rule='...'` | `ufw allow from 1.2.3.4` | `csf -a 1.2.3.4` |
| **Reload** | `iptables-restore` | `firewall-cmd --reload` | `ufw reload` | `csf -r` |

---

# 🔗 Quick Anti-DDoS Commands Summary

## iptables
```bash
# SYN Flood
iptables -A INPUT -p tcp --syn -m limit --limit 1/s --limit-burst 3 -j ACCEPT

# Connection Limit
iptables -A INPUT -p tcp --dport 80 -m connlimit --connlimit-above 50 -j DROP

# Rate Limit
iptables -A INPUT -p tcp --dport 80 -m hashlimit --hashlimit 50/sec --hashlimit-mode srcip -j ACCEPT
```

## firewalld
```bash
# Rate Limit
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" port port="80" protocol="tcp" limit value="25/s" accept'

# Block IP
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="1.2.3.4" drop'
```

## UFW
```bash
# Rate Limit
ufw limit 80/tcp

# Block IP
ufw deny from 1.2.3.4
```

## CSF
```bash
# In csf.conf
CONNLIMIT = "80;50,443;50"
PORTFLOOD = "80;tcp;50;5,443;tcp;50;5"
SYNFLOOD = "1"

# Block IP
csf -d 1.2.3.4
```

---

# 📚 Additional Resources

- [iptables manual](https://linux.die.net/man/8/iptables)
- [firewalld documentation](https://firewalld.org/documentation/)
- [UFW documentation](https://help.ubuntu.com/community/UFW)
- [CSF documentation](https://configserver.com/cp/csf.html)

---

**Author:** TangselSecTeam  
**Version:** 1.0  
**Last Updated:** January 2026
