# Burp Suite Wireless Proxy - Complete Cheat Sheet

## Daftar Isi
1. [Konsep & Arsitektur](#konsep--arsitektur)
2. [Hardware Setup - TP-Link TL-WN722N v1](#hardware-setup)
3. [Prerequisites & Installation](#prerequisites--installation)
4. [Setup Access Point (hostapd)](#setup-access-point-hostapd)
5. [DHCP Server (dnsmasq)](#dhcp-server-dnsmasq)
6. [IP Forwarding & NAT](#ip-forwarding--nat)
7. [Burp Suite Configuration](#burp-suite-configuration)
8. [iptables Redirect Rules](#iptables-redirect-rules)
9. [Complete Setup Script](#complete-setup-script)
10. [Testing & Verification](#testing--verification)
11. [Troubleshooting](#troubleshooting)
12. [SSL/TLS Certificate](#ssltls-certificate)
13. [Protocol Differences (HTTP vs HTTPS vs QUIC)](#protocol-differences)
14. [Android Chrome Limitations](#android-chrome-limitations)
15. [Cleanup & Reset](#cleanup--reset)

---

## Konsep & Arsitektur

### Network Flow

```
┌─────────────────┐
│  Client Device  │
│ (Phone/Laptop)  │
│  10.10.0.x      │
└────────┬────────┘
         │ Wi-Fi
         ↓
┌─────────────────────────────────┐
│      Kali Linux                 │
│                                 │
│  ┌──────────┐  wlan0            │
│  │ hostapd  │  10.10.0.1        │
│  └─────┬────┘                   │
│        │                        │
│  ┌─────▼────┐                   │
│  │ dnsmasq  │ DHCP Server       │
│  └─────┬────┘                   │
│        │                        │
│  ┌─────▼──────────┐             │
│  │   iptables     │             │
│  │   REDIRECT     │             │
│  │   :80  → :8080 │             │
│  │   :443 → :8080 │             │
│  └─────┬──────────┘             │
│        │                        │
│  ┌─────▼────────┐               │
│  │ Burp Suite   │               │
│  │ 0.0.0.0:8080 │               │
│  │ Transparent  │               │
│  └─────┬────────┘               │
│        │                        │
│  ┌─────▼────┐                   │
│  │   NAT    │ eth0              │
│  │MASQUERADE│ (Internet)        │
│  └──────────┘                   │
└─────────────────────────────────┘
         │
         ↓
    🌐 Internet
```

### What Happens?

1. **Client connects** ke Wi-Fi AP "LAB-PROXY"
2. **dnsmasq** memberikan IP (10.10.0.10-100)
3. **Client browsing** HTTP/HTTPS
4. **iptables REDIRECT** ke Burp :8080
5. **Burp Suite** intercept & modify traffic
6. **Burp forward** ke internet via eth0
7. **NAT (MASQUERADE)** share internet ke client

---

## 🔌 Hardware Setup - TP-Link TL-WN722N v1

### Identifikasi Chipset di Windows

#### Method 1: Device Manager (PALING AKURAT)

```
1. Colokkan TL-WN722N ke USB
2. Klik kanan Start → Device Manager
3. Buka "Network adapters"
4. Cari "TP-Link" / "Wireless USB"
5. Klik kanan → Properties
6. Tab "Details"
7. Pada "Property", pilih "Hardware Ids"

Version 1 (BAGUS):
   USB\VID_0CF3&PID_9271
   Chipset: Atheros AR9271

❌ Version 2/3 (TIDAK BAGUS untuk AP mode):
   USB\VID_2357&PID_010C
   Chipset: Realtek RTL8188EUS
```

#### Method 2: USBDeview (Free Tool)

```
1. Download USBDeview dari NirSoft
2. Jalankan USBDeview.exe
3. Cari TP-Link TL-WN722N
4. Check kolom "VendorID" dan "ProductID"

v1: VID=0CF3, PID=9271
❌ v2: VID=2357, PID=010C
```

---

### Identifikasi di Kali Linux

#### VMware Workstation USB Passthrough

```bash
# Di VMware menu:
VM → Removable Devices → 

Cari:
  TP-Link TL-WN722N
  Atheros AR9271

Klik:
  Connect (Disconnect from Host)

Jika masih "Connect to Host" = USB BELUM masuk VM!
```

#### Verify di Kali Linux

```bash
# Check USB device
lsusb | grep -i "atheros\|0cf3:9271"

# Expected output:
# Bus 001 Device 003: ID 0cf3:9271 Atheros Communications, Inc. AR9271 802.11n

# Check kernel module loaded
lsmod | grep ath9k

# Expected:
# ath9k_htc              81920  0
# ath9k_common           20480  1 ath9k_htc
# ath9k_hw              495616  2 ath9k_htc,ath9k_common

# Load module jika belum
sudo modprobe ath9k_htc

# Check dmesg
dmesg | tail -20 | grep -i "ath\|usb"

# Expected:
# usb 1-1: Atheros AR9271 Rev:1
# ath9k_htc: USB layer initialized

# Check wireless interface
iwconfig

# Expected:
# wlan0     IEEE 802.11  ESSID:off/any
#           Mode:Managed  Access Point: Not-Associated

# Check dengan iw
iw dev

# Check supported modes
iw list | grep -A 10 "Supported interface modes"

# Should show:
# * managed
# * AP         <--- IMPORTANT!
# * monitor
```

---

## 📦 Prerequisites & Installation

### Stop Monitor Mode (jika aktif)

```bash
# Check current status
iw dev
airmon-ng

# Stop monitor mode
sudo airmon-ng stop wlan0mon

# Or manually
sudo ip link set wlan0mon down
sudo iw dev wlan0mon set type managed
sudo ip link set wlan0mon up
sudo ip link set wlan0mon name wlan0
```

### Install Required Packages

```bash
# Update system
sudo apt update

# Install required packages
sudo apt install -y \
    hostapd \
    dnsmasq \
    iptables \
    iptables-persistent \
    net-tools \
    wireless-tools \
    iw

# Optional but useful
sudo apt install -y \
    tcpdump \
    wireshark \
    burpsuite
```

### Stop Conflicting Services

```bash
# Stop NetworkManager dari manage wlan0
sudo systemctl stop NetworkManager

# Or keep NM running tapi unmanage wlan0
sudo nmcli device set wlan0 managed no

# Stop conflicting services
sudo systemctl stop wpa_supplicant
sudo systemctl stop ModemManager

# Kill processes yang bisa interfere
sudo airmon-ng check kill
```

---

## 📡 Setup Access Point (hostapd)

### Prepare Interface

```bash
# Set interface down
sudo ip link set wlan0 down

# Set type to AP mode
sudo iw dev wlan0 set type __ap

# Bring interface up
sudo ip link set wlan0 up

# Verify
iw dev wlan0 info

# Should show:
# type AP

# Unmanage dari NetworkManager (jika running)
sudo nmcli device set wlan0 managed no
```

### Create hostapd Configuration

```bash
# Backup default config (if exists)
sudo cp /etc/hostapd/hostapd.conf /etc/hostapd/hostapd.conf.backup 2>/dev/null

# Create new config
sudo nano /etc/hostapd/hostapd.conf
```

**Paste this configuration:**

```ini
# Interface configuration
interface=wlan0
driver=nl80211

# Network name
ssid=LAB-PROXY

# Hardware mode (a=5GHz, b=2.4GHz, g=2.4GHz with higher rates)
hw_mode=g

# Channel (1-14 for 2.4GHz)
channel=1

# Country code (regulatory domain)
country_code=US
ieee80211d=1

# 802.11n (disable untuk compatibility)
ieee80211n=0

# WMM (Quality of Service)
wmm_enabled=0

# Authentication algorithm (1=Open, 2=Shared, 3=Both)
auth_algs=1

# Hide SSID (0=broadcast, 1=hidden)
ignore_broadcast_ssid=0

# No encryption (untuk testing)
# Tambahkan jika mau WPA2:
# wpa=2
# wpa_passphrase=YourPassword123
# wpa_key_mgmt=WPA-PSK
# rsn_pairwise=CCMP
```

### Alternative: WPA2 Configuration

```ini
# Same as above, plus:
wpa=2
wpa_passphrase=YourStrongPassword123
wpa_key_mgmt=WPA-PSK
wpa_pairwise=CCMP
rsn_pairwise=CCMP
```

### Set hostapd Daemon Config Path

```bash
# Edit default file
sudo nano /etc/default/hostapd

# Uncomment and set:
DAEMON_CONF="/etc/hostapd/hostapd.conf"

# Save and exit (Ctrl+X, Y, Enter)
```

### Test hostapd Configuration

```bash
# Test config (dry run)
sudo hostapd -dd /etc/hostapd/hostapd.conf

# Expected output:
# wlan0: interface state UNINITIALIZED->ENABLED
# wlan0: AP-ENABLED

# Ctrl+C to stop

# If successful, enable service
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
```

---

## 🌐 DHCP Server (dnsmasq)

### Backup Original Config

```bash
# Backup
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.backup
```

### Create New dnsmasq Config

```bash
sudo nano /etc/dnsmasq.conf
```

**Paste this:**

```ini
# Interface to listen on
interface=wlan0

# Don't listen on other interfaces
bind-interfaces

# DHCP range
dhcp-range=10.10.0.10,10.10.0.100,255.255.255.0,12h

# Gateway (router)
dhcp-option=3,10.10.0.1

# DNS servers (Google & Cloudflare)
dhcp-option=6,8.8.8.8,1.1.1.1

# Authoritative DHCP server
dhcp-authoritative

# Log queries (debugging)
log-queries
log-dhcp

# Log file
log-facility=/var/log/dnsmasq.log
```

### Alternative: More Verbose Config

```ini
interface=wlan0
bind-interfaces

# DHCP
dhcp-range=10.10.0.10,10.10.0.100,255.255.255.0,12h
dhcp-option=option:router,10.10.0.1
dhcp-option=option:dns-server,8.8.8.8,1.1.1.1
dhcp-option=option:netmask,255.255.255.0

# DNS
server=8.8.8.8
server=1.1.1.1

# DHCP settings
dhcp-authoritative
dhcp-leasefile=/var/lib/dnsmasq/dnsmasq.leases

# Logging
log-queries
log-dhcp
log-facility=/var/log/dnsmasq.log

# Performance
cache-size=1000
```

### Enable dnsmasq

```bash
# Enable service
sudo systemctl enable dnsmasq

# Don't start yet (will start after IP configured)
```

---

## 🔀 IP Forwarding & NAT

### Assign IP to wlan0

```bash
# Add IP address
sudo ip addr add 10.10.0.1/24 dev wlan0

# Bring interface up
sudo ip link set wlan0 up

# Verify
ip addr show wlan0

# Expected:
# inet 10.10.0.1/24 scope global wlan0
```

### Enable IP Forwarding

```bash
# Temporary (until reboot)
sudo sysctl -w net.ipv4.ip_forward=1

# Permanent
echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf

# Verify
cat /proc/sys/net/ipv4/ip_forward
# Should output: 1
```

### Flush Existing iptables Rules

```bash
# Flush all rules
sudo iptables -F
sudo iptables -t nat -F
sudo iptables -t mangle -F
sudo iptables -X

# Set default policies
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT
```

---

## 🎭 Burp Suite Configuration

### Install/Update Burp Suite

```bash
# Kali Linux biasanya sudah ada
which burpsuite

# Update jika perlu
sudo apt update
sudo apt install burpsuite

# Or download Community/Pro dari:
# https://portswigger.net/burp/releases
```

### Start Burp Suite

```bash
# Start Burp
burpsuite &

# Or dari menu: Applications → Web Application Analysis → burpsuite
```

### Configure Proxy Listener

```
1. Go to: Proxy → Options → Proxy Listeners

2. Add new listener:
   - Bind to port: 8080
   - Bind to address: All interfaces (0.0.0.0)

3. Check: "Support invisible proxying"
   PENTING untuk transparent proxy!

4. Running: Pastikan checkbox "Running" checked

5. Request handling (optional):
   - Redirect to host: (leave empty)
   - Redirect to port: (leave empty)
   - Force use of SSL: (uncheck)
   - Support invisible proxying: CHECK THIS!
```

**Screenshot reference:**
```
┌─────────────────────────────────────┐
│ Proxy Listener                      │
├─────────────────────────────────────┤
│ Bind to port: 8080                  │
│ Bind to address: ○ Loopback only    │
│                  ● All interfaces   │
│                  ○ Specific address │
│                                     │
│ Request handling:                   │
│ ☐ Redirect to host: [         ]    │
│ ☐ Redirect to port: [         ]    │
│ ☐ Force use of SSL                  │
│ ☑ Support invisible proxying        │ ← IMPORTANT!
└─────────────────────────────────────┘
```

### Verify Burp Listening

```bash
# Check if Burp listening on 8080
sudo netstat -tlnp | grep 8080

# Expected:
# tcp6  0  0 :::8080  :::*  LISTEN  12345/java

# Or with ss
sudo ss -tlnp | grep 8080

# Or with lsof
sudo lsof -i :8080
```

### Configure SSL/TLS (for HTTPS)

```
1. Go to: Proxy → Options → Proxy Listeners → Edit

2. Certificate tab:
   - ● Generate CA-signed per-host certificates
   - Certificate: Use Burp defaults

3. Install CA certificate on client devices (see below)
```

---

## 🔥 iptables Redirect Rules

### Complete iptables Setup

```bash
# ============================================
# 1. SSH PROTECTION (jika remote access)
# ============================================
sudo iptables -I INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -I OUTPUT -p tcp --sport 22 -j ACCEPT

# ============================================
# 2. NAT - INTERNET SHARING
# ============================================
# Replace eth0 dengan interface internet Anda
# Check dengan: ip route | grep default

sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# ============================================
# 3. FORWARD - Allow traffic flow
# ============================================
sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT

# ============================================
# 4. REDIRECT to Burp Suite (TRANSPARENT PROXY)
# ============================================
# HTTP (port 80) → Burp :8080
sudo iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 80 -j REDIRECT --to-port 8080

# HTTPS (port 443) → Burp :8080
sudo iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j REDIRECT --to-port 8080

# ============================================
# 5. ALLOW local traffic (Kali → Internet)
# ============================================
sudo iptables -t nat -I OUTPUT -o lo -j RETURN
sudo iptables -t nat -I OUTPUT -m owner --uid-owner $(id -u) -j RETURN
```

### Exclude Kali's Own Traffic

```bash
# Agar Kali sendiri tidak di-redirect ke Burp
# (supaya bisa browsing normal)

# Get Kali user UID
echo $UID
# Example: 1000

# Exclude based on UID
sudo iptables -t nat -I PREROUTING -m owner --uid-owner 1000 -j RETURN

# Or exclude based on source IP (Kali itself)
sudo iptables -t nat -I PREROUTING -s 10.10.0.1 -j RETURN
```

### Verify iptables Rules

```bash
# View NAT table
sudo iptables -t nat -L -n -v

# Expected output should include:
# PREROUTING chain:
#   - REDIRECT tcp dpt:80 redir ports 8080
#   - REDIRECT tcp dpt:443 redir ports 8080

# POSTROUTING chain:
#   - MASQUERADE all -- * eth0 0.0.0.0/0 0.0.0.0/0

# View FORWARD chain
sudo iptables -L FORWARD -n -v

# Should show:
#   - ACCEPT all -- wlan0 eth0 0.0.0.0/0 0.0.0.0/0
#   - ACCEPT all -- eth0 wlan0 0.0.0.0/0 0.0.0.0/0 state RELATED,ESTABLISHED
```

### Save iptables Rules

```bash
# Save current rules
sudo iptables-save | sudo tee /etc/iptables/rules.v4

# Or use iptables-persistent
sudo netfilter-persistent save

# Verify saved
cat /etc/iptables/rules.v4
```

---

## 🚀 Complete Setup Script

### All-in-One Setup Script

```bash
#!/bin/bash
# Burp Suite Wireless Proxy Setup
# Save as: setup-burp-proxy.sh

set -e  # Exit on error

echo "==================================="
echo "Burp Suite Wireless Proxy Setup"
echo "==================================="

# Variables
INTERFACE="wlan0"
INET_INTERFACE="eth0"  # Change if different
AP_IP="10.10.0.1"
AP_SUBNET="10.10.0.0/24"
DHCP_START="10.10.0.10"
DHCP_END="10.10.0.100"
BURP_PORT="8080"

# Check if running as root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root (sudo)"
   exit 1
fi

echo "[*] Step 1: Stop conflicting services"
systemctl stop NetworkManager 2>/dev/null || true
nmcli device set $INTERFACE managed no 2>/dev/null || true
killall wpa_supplicant 2>/dev/null || true

echo "[*] Step 2: Setup wireless interface"
ip link set $INTERFACE down
iw dev $INTERFACE set type __ap
ip link set $INTERFACE up
ip addr flush dev $INTERFACE
ip addr add ${AP_IP}/24 dev $INTERFACE

echo "[*] Step 3: Enable IP forwarding"
sysctl -w net.ipv4.ip_forward=1

echo "[*] Step 4: Flush iptables"
iptables -F
iptables -t nat -F
iptables -t mangle -F
iptables -X

echo "[*] Step 5: Setup iptables rules"
# SSH protection
iptables -I INPUT -p tcp --dport 22 -j ACCEPT
iptables -I OUTPUT -p tcp --sport 22 -j ACCEPT

# NAT
iptables -t nat -A POSTROUTING -o $INET_INTERFACE -j MASQUERADE

# Forward
iptables -A FORWARD -i $INTERFACE -o $INET_INTERFACE -j ACCEPT
iptables -A FORWARD -i $INET_INTERFACE -o $INTERFACE -m state --state RELATED,ESTABLISHED -j ACCEPT

# Redirect to Burp
iptables -t nat -A PREROUTING -i $INTERFACE -p tcp --dport 80 -j REDIRECT --to-port $BURP_PORT
iptables -t nat -A PREROUTING -i $INTERFACE -p tcp --dport 443 -j REDIRECT --to-port $BURP_PORT

# Exclude Kali's own traffic
iptables -t nat -I PREROUTING -s $AP_IP -j RETURN

echo "[*] Step 6: Start hostapd"
systemctl start hostapd

echo "[*] Step 7: Start dnsmasq"
systemctl start dnsmasq

echo ""
echo "==================================="
echo "Setup Complete!"
echo "==================================="
echo ""
echo "AP SSID: LAB-PROXY"
echo "AP IP: $AP_IP"
echo "DHCP Range: $DHCP_START - $DHCP_END"
echo ""
echo "Next steps:"
echo "1. Start Burp Suite"
echo "2. Configure listener: 0.0.0.0:$BURP_PORT"
echo "3. Enable 'Support invisible proxying'"
echo "4. Connect client to LAB-PROXY"
echo "5. Browse to http://neverssl.com to test"
echo ""
echo "View logs:"
echo "  hostapd: journalctl -u hostapd -f"
echo "  dnsmasq: tail -f /var/log/dnsmasq.log"
echo ""
```

### Make Script Executable

```bash
# Save script
nano setup-burp-proxy.sh
# Paste script above

# Make executable
chmod +x setup-burp-proxy.sh

# Run
sudo ./setup-burp-proxy.sh
```

---

## Testing & Verification

### Check Services Status

```bash
# Check hostapd
sudo systemctl status hostapd --no-pager -l

# Check dnsmasq
sudo systemctl status dnsmasq --no-pager -l

# Check if services running
ps aux | grep -E 'hostapd|dnsmasq' | grep -v grep
```

### Check Interface

```bash
# Check IP address
ip addr show wlan0

# Should show:
# inet 10.10.0.1/24 scope global wlan0

# Check interface type
iw dev wlan0 info

# Should show:
# type AP
```

### Check IP Forwarding

```bash
cat /proc/sys/net/ipv4/ip_forward
# Output: 1
```

### Check iptables

```bash
# NAT rules
sudo iptables -t nat -L PREROUTING -n -v

# Should show REDIRECT rules for port 80 and 443

# Forward rules
sudo iptables -L FORWARD -n -v
```

### Check Burp Listening

```bash
sudo netstat -tlnp | grep 8080
# tcp6  0  0 :::8080  :::*  LISTEN  xxx/java

# Or
sudo ss -tlnp | grep 8080
```

### Monitor Logs Real-time

```bash
# Terminal 1: hostapd logs
sudo journalctl -u hostapd -f

# Terminal 2: dnsmasq logs
sudo tail -f /var/log/dnsmasq.log

# Terminal 3: tcpdump on wlan0
sudo tcpdump -i wlan0 -n

# Terminal 4: iptables trace (optional)
sudo iptables -t nat -L PREROUTING -n -v
watch -n 1 'sudo iptables -t nat -L PREROUTING -n -v'
```

---

## 📱 Client Testing

### Connect Client to AP

```
1. On client device (phone/laptop):
   - Scan WiFi
   - Find "LAB-PROXY"
   - Connect (no password)

2. Check IP received:
   - Should be 10.10.0.x (between .10-.100)
   - Gateway: 10.10.0.1
   - DNS: 8.8.8.8
```

### Test HTTP (should work immediately)

```
Open browser on client:
http://neverssl.com

Should show in Burp:
   - Proxy → HTTP history
   - Request from 10.10.0.x
   - Host: neverssl.com
```

### Test HTTPS (needs certificate)

```
Open browser on client:
https://example.com

Will show certificate warning!

To fix:
1. Install Burp CA certificate (see below)
2. Or ignore warning for testing
```

---

## 🔒 SSL/TLS Certificate

### Download Burp CA Certificate

#### From Client Device

```
1. Connect to LAB-PROXY
2. Open browser
3. Go to: http://burp
   (or http://10.10.0.1:8080)
4. Click "CA Certificate"
5. Save as: cacert.der
```

#### From Kali (copy to client)

```bash
# Burp generates cert automatically
# Default location (varies by installation):
~/.java/.userPrefs/burp/
~/.BurpSuite/
```

### Install on Android

```
1. Download cacert.der from http://burp
2. Settings → Security → Install from storage
3. Choose "CA Certificate"
4. Select cacert.der
5. Name: "Burp Suite CA"
6. Restart browser
```

### Install on iOS

```
1. Download cacert.der from http://burp via Safari
2. Settings → Profile Downloaded → Install
3. Settings → General → About → Certificate Trust Settings
4. Enable trust for Burp CA
```

### Install on Linux

```bash
# Copy to certificates directory
sudo cp cacert.der /usr/local/share/ca-certificates/burp.crt

# Update certificates
sudo update-ca-certificates

# Verify
ls /etc/ssl/certs/ | grep -i burp
```

### Install on Windows

```
1. Double-click cacert.der
2. Install Certificate
3. Store Location: Current User
4. Place in: Trusted Root Certification Authorities
5. Finish
```

---

## 🌐 Protocol Differences

### HTTP vs HTTPS vs QUIC

#### HTTP (Port 80)

```
Protocol: Plaintext
Interception: EASY
Certificate: ❌ Not needed

Flow:
Client → iptables REDIRECT → Burp :8080 → Internet

Burp can:
Read all data
Modify requests/responses
Fully transparent
```

#### HTTPS (Port 443)

```
Protocol: TLS encrypted
Interception: POSSIBLE with certificate
Certificate: REQUIRED (install Burp CA)

Flow:
Client → iptables REDIRECT → Burp :8080 → Internet
         TLS handshake    Burp MITM     TLS to server

Burp can:
Read encrypted data (after MITM)
Modify requests/responses
Requires CA certificate installed
❌ Client shows warning without cert
```

**SSL/TLS MITM Process:**

```
1. Client initiates HTTPS to example.com
2. iptables redirects to Burp :8080
3. Burp creates fake certificate for example.com
   - Signed by Burp CA
4. Client verifies certificate
   If Burp CA installed: OK
   ❌ If not: Certificate warning
5. Burp establishes real connection to example.com
6. Burp decrypts & logs all traffic
```

#### QUIC (UDP Port 443)

```
Protocol: UDP-based, TLS 1.3 built-in
Interception: ❌ VERY DIFFICULT
Certificate: ❌ Won't help

Flow:
Client → ??? → Internet (bypasses iptables TCP rules)

Burp can:
❌ Cannot intercept (iptables only handles TCP)
❌ Cannot decrypt (no MITM possible)
❌ Traffic bypasses proxy

Used by:
- Chrome (Google services)
- YouTube
- Gmail
- Google Search
- Many modern apps
```

**QUIC Characteristics:**

```
Faster than TCP
Less latency
Encrypted by default
❌ Harder to intercept/proxy
❌ Bypasses traditional proxies
```

### Protocol Summary Table

| Feature | HTTP | HTTPS | QUIC |
|---------|------|-------|------|
| **Protocol** | TCP | TCP + TLS | UDP + TLS |
| **Port** | 80 | 443 | 443 |
| **Encryption** | None | TLS | Built-in TLS 1.3 |
| **Burp Intercept** | Easy | Needs cert | ❌ Very hard |
| **Certificate Needed** | ❌ No | Yes | ❌ Won't help |
| **iptables REDIRECT** | Works | Works | ❌ Doesn't work |
| **Modify Traffic** | Full control | With cert | ❌ Not possible |

---

## 📱 Android Chrome Limitations

### Why Android Chrome is Problematic

#### 1. Certificate Pinning

```
Chrome menggunakan certificate pinning untuk:
- Google services (Gmail, YouTube, Search)
- Banking apps
- Security-conscious apps

Result:
❌ Tidak bisa di-intercept walaupun Burp CA installed
❌ Connection fails atau bypass proxy
```

#### 2. QUIC Protocol

```
Chrome/Android prefer QUIC (UDP) over HTTPS (TCP)

Why problematic:
- QUIC uses UDP port 443
- iptables REDIRECT hanya work untuk TCP
- Traffic BYPASSES proxy sepenuhnya

Sites using QUIC:
- google.com
- youtube.com
- gmail.com
- facebook.com (partial)
- cloudflare sites
```

#### 3. DNS over HTTPS (DoH)

```
Chrome menggunakan DoH secara default

Result:
- DNS queries bypass dnsmasq
- DNS queries di-encrypt
- Harder to redirect/monitor
```

#### 4. Security Features

```
Android 7.0+ (Nougat):
- Tidak trust user-installed certificates untuk apps
- Hanya system certificates di-trust
- Apps menggunakan network_security_config

Result:
❌ Many apps ignore Burp certificate
❌ SSL errors atau connection failures
```

---

### Workarounds for Android Chrome

#### Method 1: Disable QUIC

**Chrome Flags:**

```
1. Open Chrome
2. Go to: chrome://flags
3. Search: "QUIC"
4. Find: "Experimental QUIC protocol"
5. Set to: Disabled
6. Restart Chrome

Result:
Chrome will use HTTPS (TCP) instead of QUIC
iptables redirect will work
Burp can intercept
```

#### Method 2: Disable Chrome on Android

```bash
# Use different browser:
Firefox (best for pentesting)
Edge
Opera Mini
Samsung Internet

Why Firefox is better:
- Respects system certificates
- No certificate pinning
- No forced QUIC
- Better proxy support
```

#### Method 3: Root + Magisk

```
For rooted Android:

1. Install Magisk
2. Install "Move Certificates" module
3. Moves user certificates to system
4. Apps will trust Burp CA

Pros:
Works with all apps
Bypass certificate pinning

Cons:
❌ Requires root
❌ Voids warranty
❌ Security implications
```

#### Method 4: Use HTTP Toolkit

```bash
# Alternative to Burp for Android
# https://httptoolkit.tech/

Features:
Automatic certificate installation
Handles QUIC
No root required
One-click setup

Download:
wget https://github.com/httptoolkit/httptoolkit-desktop/releases/latest

# Can work alongside Burp
```

#### Method 5: Block QUIC at Firewall

```bash
# Add iptables rule to block UDP 443
sudo iptables -A FORWARD -i wlan0 -p udp --dport 443 -j REJECT
sudo iptables -A FORWARD -i wlan0 -p udp --dport 80 -j REJECT

# Force fallback to TCP
# Chrome will automatically use HTTPS instead

# Test:
# Chrome should now show traffic in Burp
```

#### Method 6: DNS Blackhole for QUIC

```bash
# Add to /etc/dnsmasq.conf
address=/google.com/0.0.0.0
address=/youtube.com/0.0.0.0

# Force Chrome to use HTTPS
# (tidak recommended untuk production)
```

---

### Testing Chrome Interception

#### Test 1: HTTP (should always work)

```
URL: http://neverssl.com

Expected:
Appears in Burp
No certificate errors
Modifiable
```

#### Test 2: HTTPS (standard site)

```
URL: https://example.com

Expected:
Appears in Burp (with cert installed)
Can read/modify traffic
Certificate warning (without cert)
```

#### Test 3: HTTPS (Google/QUIC site)

```
URL: https://google.com

Result WITHOUT blocking QUIC:
❌ May not appear in Burp
❌ Bypasses proxy via QUIC
❌ Falls back to HTTPS after QUIC blocked

Result AFTER blocking UDP 443:
Appears in Burp
Uses HTTPS fallback
```

#### Test 4: Certificate Pinned Site

```
URL: https://gmail.com (in Chrome)

Result:
❌ Connection fails
❌ Certificate pinning prevents MITM
❌ Cannot intercept

Alternative:
Use Firefox instead
Or dedicated app pentesting tools
```

---

## 🐛 Troubleshooting

### Issue 1: AP tidak muncul

**Symptoms:**
- Client tidak melihat "LAB-PROXY"
- No SSID broadcast

**Debug:**

```bash
# Check hostapd status
sudo systemctl status hostapd

# Check hostapd logs
sudo journalctl -u hostapd -n 50

# Test hostapd manually
sudo killall hostapd
sudo hostapd -dd /etc/hostapd/hostapd.conf

# Common errors:
# - "Could not configure driver mode"
#   → Check interface type: iw dev wlan0 info (should be AP)
# - "Channel X not allowed"
#   → Change channel in hostapd.conf
# - "Device or resource busy"
#   → Stop NetworkManager: systemctl stop NetworkManager
```

**Fix:**

```bash
# Reset interface
sudo ip link set wlan0 down
sudo iw dev wlan0 set type __ap
sudo ip link set wlan0 up
sudo ip addr add 10.10.0.1/24 dev wlan0

# Restart hostapd
sudo systemctl restart hostapd
```

---

### Issue 2: Client connect tapi tidak dapat IP

**Symptoms:**
- Client connects to LAB-PROXY
- Stuck on "Obtaining IP address"
- No DHCP lease

**Debug:**

```bash
# Check dnsmasq status
sudo systemctl status dnsmasq

# Check dnsmasq logs
sudo tail -f /var/log/dnsmasq.log

# Check if IP assigned to wlan0
ip addr show wlan0
# Should show: inet 10.10.0.1/24

# Check dnsmasq process
ps aux | grep dnsmasq

# Test dnsmasq config
sudo dnsmasq --test -C /etc/dnsmasq.conf
```

**Fix:**

```bash
# Ensure IP assigned
sudo ip addr add 10.10.0.1/24 dev wlan0

# Restart dnsmasq
sudo systemctl restart dnsmasq

# Check leases
cat /var/lib/dnsmasq/dnsmasq.leases
```

---

### Issue 3: Client dapat IP tapi tidak ada internet

**Symptoms:**
- Client IP: 10.10.0.x
- Can ping 10.10.0.1
- Cannot ping 8.8.8.8 atau google.com

**Debug:**

```bash
# Check IP forwarding
cat /proc/sys/net/ipv4/ip_forward
# Should be: 1

# Check NAT rule
sudo iptables -t nat -L POSTROUTING -n -v
# Should show MASQUERADE rule

# Check forward rules
sudo iptables -L FORWARD -n -v

# Test from Kali
ping -I wlan0 8.8.8.8

# Check eth0 has internet
ping -I eth0 8.8.8.8
```

**Fix:**

```bash
# Enable IP forwarding
sudo sysctl -w net.ipv4.ip_forward=1

# Add NAT rule
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

# Add forward rules
sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT

# Verify eth0 interface name
ip route | grep default
# If not eth0, replace in iptables rules
```

---

### Issue 4: Burp tidak menerima traffic

**Symptoms:**
- Client has internet
- Browsing works
- But Burp HTTP history empty

**Debug:**

```bash
# Check if Burp listening
sudo netstat -tlnp | grep 8080
sudo ss -tlnp | grep 8080

# Check iptables redirect rules
sudo iptables -t nat -L PREROUTING -n -v
# Should show REDIRECT rules with packet count increasing

# Check packets hitting rules
watch -n 1 'sudo iptables -t nat -L PREROUTING -n -v'
# Browse from client, watch pkts column

# Test redirect manually
# On Kali:
curl -v http://example.com
# Should fail or show Burp response

# Check Burp listener settings
# - Should be 0.0.0.0:8080
# - "Support invisible proxying" should be CHECKED
```

**Fix:**

```bash
# Add redirect rules
sudo iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 80 -j REDIRECT --to-port 8080
sudo iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j REDIRECT --to-port 8080

# Exclude Kali's own traffic
sudo iptables -t nat -I PREROUTING -s 10.10.0.1 -j RETURN

# Restart Burp with correct settings:
# 1. Listener: 0.0.0.0:8080
# 2. Support invisible proxying
# 3. Running
```

---

### Issue 5: HTTPS tidak bekerja

**Symptoms:**
- HTTP works (http://neverssl.com)
- HTTPS shows "ERR_CONNECTION_REFUSED" atau timeout

**Debug:**

```bash
# Check if HTTPS redirect rule exists
sudo iptables -t nat -L PREROUTING -n -v | grep 443

# Check Burp handling HTTPS
# In Burp: Proxy → Options → Listener → Edit
# Verify: "Support invisible proxying" checked

# Test from client
curl -v -k https://example.com
```

**Fix:**

```bash
# Ensure HTTPS redirect rule
sudo iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j REDIRECT --to-port 8080

# Configure Burp:
# 1. Proxy → Options → Listener
# 2. Edit listener
# 3. Request handling:
#    Support invisible proxying
# 4. Certificate:
#    ● Generate CA-signed per-host certificates
```

---

### Issue 6: Certificate warnings

**Symptoms:**
- HTTPS sites show "Your connection is not private"
- NET::ERR_CERT_AUTHORITY_INVALID

**Fix:**

```
1. Download Burp CA certificate:
   - Browse to: http://burp
   - Click "CA Certificate"
   - Save cacert.der

2. Install on device:
   - Android: Settings → Security → Install from storage
   - iOS: Settings → Profile → Install + Trust
   - Linux: Copy to /usr/local/share/ca-certificates/
   - Windows: Double-click → Install to Trusted Root

3. Restart browser

4. Test: https://example.com
   - Should work without warning
```

---

### Issue 7: Chrome/Android tidak bekerja

**Symptoms:**
- Firefox works
- Chrome tidak muncul di Burp
- Chrome has internet but bypasses proxy

**Reason:**
- Chrome menggunakan QUIC (UDP)
- iptables redirect hanya TCP
- Traffic bypasses proxy

**Fix:**

```bash
# Method 1: Block QUIC
sudo iptables -A FORWARD -i wlan0 -p udp --dport 443 -j REJECT

# Method 2: Disable QUIC di Chrome
# chrome://flags → Search "QUIC" → Disable

# Method 3: Use Firefox instead
# Firefox respects system proxy better

# Test
# After blocking QUIC, Chrome should fallback to HTTPS (TCP)
```

---

### Issue 8: DNS tidak resolve

**Symptoms:**
- Can ping 8.8.8.8
- Cannot ping google.com
- DNS resolution fails

**Debug:**

```bash
# Check dnsmasq running
sudo systemctl status dnsmasq

# Check dnsmasq config
cat /etc/dnsmasq.conf | grep -v ^# | grep -v ^$

# Check DNS in DHCP response
sudo tail -f /var/log/dnsmasq.log
# Should show: DHCPOFFER ... opt:6 = 8.8.8.8

# Test DNS from Kali
dig @10.10.0.1 google.com

# Check client DNS settings
# On client: Should be 8.8.8.8, 1.1.1.1
```

**Fix:**

```bash
# Edit dnsmasq.conf
sudo nano /etc/dnsmasq.conf

# Ensure these lines:
dhcp-option=6,8.8.8.8,1.1.1.1
server=8.8.8.8
server=1.1.1.1

# Restart
sudo systemctl restart dnsmasq

# Reconnect client
```

---

### Issue 9: Interface keeps resetting

**Symptoms:**
- wlan0 loses IP
- AP disappears
- NetworkManager takes over

**Fix:**

```bash
# Permanently unmanage wlan0
sudo nmcli device set wlan0 managed no

# Or edit NetworkManager config
sudo nano /etc/NetworkManager/NetworkManager.conf

# Add:
[keyfile]
unmanaged-devices=interface-name:wlan0

# Restart NetworkManager
sudo systemctl restart NetworkManager

# Or stop NetworkManager completely
sudo systemctl stop NetworkManager
sudo systemctl disable NetworkManager
```

---

### Issue 10: Performance issues (slow)

**Symptoms:**
- Internet very slow
- High latency
- Packet loss

**Debug:**

```bash
# Check CPU usage
top
# Look for high CPU process

# Check Burp heap size
# Burp → Project options → Performance

# Check iptables packet count
sudo iptables -t nat -L -n -v

# Check interface errors
ip -s link show wlan0
```

**Fix:**

```bash
# Increase Burp heap size
# Edit burpsuite launch script
# Add: -Xmx2G (for 2GB heap)

# Disable unnecessary Burp features:
# - Burp → Project options → Misc
# - Uncheck "Log proxy traffic to file"

# Reduce iptables logging (if enabled)
sudo iptables -t nat -D PREROUTING -j LOG 2>/dev/null

# Use better hardware or bare-metal instead of VM
```

---

## 🔄 Cleanup & Reset

### Stop All Services

```bash
#!/bin/bash
# Save as: stop-burp-proxy.sh

echo "[*] Stopping services..."
sudo systemctl stop hostapd
sudo systemctl stop dnsmasq

echo "[*] Flushing iptables..."
sudo iptables -F
sudo iptables -t nat -F
sudo iptables -t mangle -F
sudo iptables -X

echo "[*] Disable IP forwarding"
sudo sysctl -w net.ipv4.ip_forward=0

echo "[*] Reset wlan0 interface..."
sudo ip addr flush dev wlan0
sudo ip link set wlan0 down
sudo iw dev wlan0 set type managed
sudo ip link set wlan0 up

echo "[*] Re-enable NetworkManager..."
sudo nmcli device set wlan0 managed yes
sudo systemctl start NetworkManager

echo ""
echo "Cleanup complete!"
echo "wlan0 is now back to normal Wi-Fi client mode"
```

### Make Executable & Run

```bash
chmod +x stop-burp-proxy.sh
sudo ./stop-burp-proxy.sh
```

---

### Full Reset (if needed)

```bash
# Nuclear option - reset everything

# 1. Stop all services
sudo systemctl stop hostapd dnsmasq NetworkManager

# 2. Kill processes
sudo killall hostapd dnsmasq wpa_supplicant

# 3. Flush iptables
sudo iptables -F
sudo iptables -t nat -F
sudo iptables -t mangle -F
sudo iptables -X
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT

# 4. Disable IP forwarding
sudo sysctl -w net.ipv4.ip_forward=0

# 5. Reset wlan0
sudo ip addr flush dev wlan0
sudo ip link set wlan0 down
sudo iw dev wlan0 set type managed
sudo ip link set wlan0 up

# 6. Unblock RF
sudo rfkill unblock all

# 7. Restart NetworkManager
sudo systemctl start NetworkManager

# 8. Reboot (if still issues)
sudo reboot
```

---

## 📚 Quick Reference

### Essential Commands

```bash
# Setup (in order)
sudo ip link set wlan0 down
sudo iw dev wlan0 set type __ap
sudo ip link set wlan0 up
sudo ip addr add 10.10.0.1/24 dev wlan0
sudo nmcli device set wlan0 managed no
sudo sysctl -w net.ipv4.ip_forward=1
sudo systemctl start hostapd
sudo systemctl start dnsmasq

# iptables
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 80 -j REDIRECT --to-port 8080
sudo iptables -t nat -A PREROUTING -i wlan0 -p tcp --dport 443 -j REDIRECT --to-port 8080

# Verify
sudo systemctl status hostapd dnsmasq
sudo netstat -tlnp | grep 8080
sudo iptables -t nat -L PREROUTING -n -v
ip addr show wlan0
cat /proc/sys/net/ipv4/ip_forward
```

### Burp Settings Checklist

```
Proxy → Options → Proxy Listeners
Add listener: 0.0.0.0:8080
Running: checked
Request handling:
   Support invisible proxying: CHECKED
```

### Client Testing Steps

```
1. Connect to LAB-PROXY
2. Check IP: 10.10.0.x
3. Test HTTP: http://neverssl.com
4. Download cert: http://burp
5. Install certificate on device
6. Test HTTPS: https://example.com
7. Check Burp HTTP history
```

---

## 🎓 Use Cases & Scenarios

### Penetration Testing

```
Intercept mobile app traffic
Test API endpoints
Capture authentication tokens
Analyze encrypted traffic
Test session management
Find sensitive data leaks
```

### Security Research

```
Reverse engineer app protocols
Discover hidden API endpoints
Analyze encryption implementations
Test certificate validation
Research security vulnerabilities
```

### Development & Debugging

```
Debug mobile app HTTP issues
Monitor API calls
Test error handling
Inspect request/response headers
Validate data formatting
```

---

## Legal & Ethical Warning

### 🚨 PENTING - BACA INI

```
❌ JANGAN gunakan untuk:
   - Intercept traffic orang lain tanpa izin
   - Steal credentials/data
   - Man-in-the-Middle attack di network publik
   - Violate privacy laws

HANYA gunakan untuk:
   - YOUR OWN devices
   - Authorized penetration testing
   - Research lab environment
   - Educational purposes dengan izin

⚖️ HUKUM:
   - UU ITE Pasal 30, 32, 46 (Indonesia)
   - Computer Fraud and Abuse Act (USA)
   - Computer Misuse Act (UK)
   - Hukuman: PENJARA + DENDA

📝 ALWAYS:
   - Get written authorization
   - Document testing scope
   - Protect intercepted data
   - Follow responsible disclosure
```

---

## 🏆 Best Practices

### Security

1. **Use WPA2** untuk lab AP (jangan open)
2. **Change default SSID** (jangan "LAB-PROXY" di production)
3. **Isolate lab network** dari production
4. **Encrypt captured data** (Burp project files)
5. **Delete sensitive data** after testing

### Performance

1. **Use Kali bare-metal** (bukan VM jika possible)
2. **Increase Burp heap** (-Xmx2G atau lebih)
3. **Disable Burp logging** jika tidak perlu
4. **Use SSD** untuk better I/O
5. **Close unnecessary apps**

### Testing

1. **Test dengan HTTP dulu** (simpler)
2. **Install certificate** sebelum HTTPS testing
3. **Test dengan Firefox** dulu (lebih mudah)
4. **Document findings** systematically
5. **Verify results** dengan multiple tools

---

## 📖 Additional Resources

### Official Documentation

- **Burp Suite:** https://portswigger.net/burp/documentation
- **hostapd:** https://w1.fi/hostapd/
- **dnsmasq:** https://thekelleys.org.uk/dnsmasq/doc.html
- **iptables:** https://netfilter.org/documentation/

### Learning

- **PortSwigger Academy:** https://portswigger.net/web-security
- **Burp Suite Certified Practitioner (BSCP)**
- **OWASP Mobile Security:** https://owasp.org/www-project-mobile-security/

### Tools

- **mitmproxy:** Alternative transparent proxy
- **Charles Proxy:** Cross-platform proxy
- **Fiddler:** Windows proxy tool
- **HTTP Toolkit:** Modern HTTP(S) debugging

---

## 🎯 Summary Checklist

### Pre-Setup

- [ ] TP-Link TL-WN722N v1 (Atheros AR9271)
- [ ] Kali Linux (bare-metal recommended)
- [ ] Internet connection (eth0)
- [ ] Burp Suite installed
- [ ] All packages installed (hostapd, dnsmasq, etc)

### Setup Steps

- [ ] Stop NetworkManager / unmanage wlan0
- [ ] Set wlan0 to AP mode
- [ ] Assign IP 10.10.0.1/24 to wlan0
- [ ] Configure hostapd.conf
- [ ] Configure dnsmasq.conf
- [ ] Enable IP forwarding
- [ ] Setup iptables NAT
- [ ] Setup iptables REDIRECT
- [ ] Start hostapd
- [ ] Start dnsmasq
- [ ] Start Burp with correct settings
- [ ] Verify all services running

### Testing

- [ ] AP visible on client
- [ ] Client gets IP via DHCP
- [ ] Client has internet access
- [ ] HTTP traffic appears in Burp
- [ ] Install Burp CA certificate
- [ ] HTTPS traffic appears in Burp
- [ ] Can modify requests/responses

### Cleanup

- [ ] Stop hostapd & dnsmasq
- [ ] Flush iptables
- [ ] Reset wlan0 to managed mode
- [ ] Re-enable NetworkManager
- [ ] Delete sensitive captured data

---

**Happy Hunting! 🔥🔓 (Legally & Responsibly)**

---

*Cheat sheet ini untuk **AUTHORIZED TESTING ONLY**.*  
*Gunakan dengan **BIJAKSANA** dan **BERTANGGUNG JAWAB**.*

**Version:** 1.0  
**Last Updated:** January 12, 2026  
**Author:** TangselSecTeam - Batch 1  
**Device:** TP-Link TL-WN722N v1 (Atheros AR9271)  
**Platform:** Kali Linux + Burp Suite
