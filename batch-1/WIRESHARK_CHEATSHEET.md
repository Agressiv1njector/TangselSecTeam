# 🦈 Wireshark Cheat Sheet - Lengkap & Komprehensif

## 📑 Daftar Isi
1. [Pengenalan Wireshark](#pengenalan-wireshark)
2. [Interface & Menu](#interface--menu)
3. [Display Filters](#display-filters)
4. [Capture Filters](#capture-filters)
5. [Teknik Analisis](#teknik-analisis)
6. [Command Line (TShark)](#command-line-tshark)
7. [Tips & Tricks](#tips--tricks)

---

## 🔍 Pengenalan Wireshark

### Apa itu Wireshark?
Wireshark adalah network protocol analyzer yang digunakan untuk:
- Troubleshooting jaringan
- Analisis keamanan
- Pengembangan protokol
- Pembelajaran networking
- Forensik digital

### Instalasi
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install wireshark

# Fedora/RHEL
sudo dnf install wireshark

# Windows
# Download dari https://www.wireshark.org/download.html

# macOS
brew install --cask wireshark
```

---

## 🖥️ Interface & Menu

### 1. **Main Toolbar**
```
File → Edit → View → Go → Capture → Analyze → Statistics → Telephony → Wireless → Tools → Help
```

#### **File Menu**
- `Open` (Ctrl+O) - Buka file capture
- `Save` (Ctrl+S) - Simpan capture
- `Export Packet Dissections` - Export ke berbagai format (CSV, JSON, XML)
- `Export Objects` - Extract file dari traffic (HTTP, SMB, etc)
- `Print` - Print packet details

#### **Edit Menu**
- `Find Packet` (Ctrl+F) - Cari packet
- `Mark Packet` (Ctrl+M) - Tandai packet
- `Time Reference` - Set time reference
- `Configuration Profiles` - Manage profiles

#### **View Menu**
- `Zoom In/Out` (Ctrl++/Ctrl+-) - Zoom display
- `Coloring Rules` - Atur warna packet
- `Show Packet in New Window` - Buka packet di window baru
- `Reload` (Ctrl+R) - Reload capture file

#### **Go Menu**
- `Go to Packet` (Ctrl+G) - Jump ke packet number
- `Go to Corresponding Packet` - Jump ke packet terkait
- `Next/Previous Packet` (↓/↑) - Navigasi packet

#### **Capture Menu**
- `Interfaces` (Ctrl+I) - Pilih interface
- `Start` (Ctrl+E) - Mulai capture
- `Stop` (Ctrl+E) - Stop capture
- `Restart` (Ctrl+R) - Restart capture
- `Capture Filters` - Set capture filter

#### **Analyze Menu**
- `Display Filters` - Manage display filters
- `Apply as Filter` - Terapkan filter dari packet
- `Follow TCP/UDP/HTTP Stream` - Ikuti conversation
- `Expert Information` - Lihat warning/error
- `Conversation Filter` - Filter conversation specific

#### **Statistics Menu**
- `Capture File Properties` - Info file
- `Protocol Hierarchy` - Statistik protokol
- `Conversations` - Daftar percakapan
- `Endpoints` - Daftar endpoint
- `I/O Graph` - Grafik traffic
- `Flow Graph` - Visualisasi alur packet

---

### 2. **Packet List Pane** (Atas)
Menampilkan daftar packet yang di-capture dengan kolom:

| Kolom | Deskripsi |
|-------|-----------|
| **No.** | Nomor packet |
| **Time** | Waktu capture (relative/absolute) |
| **Source** | IP/MAC address sumber |
| **Destination** | IP/MAC address tujuan |
| **Protocol** | Protokol yang digunakan |
| **Length** | Panjang packet (bytes) |
| **Info** | Informasi singkat packet |

**Warna Default:**
- 🟣 **Ungu** - TCP (SYN, SYN-ACK)
- 🔵 **Biru** - UDP
- ⚫ **Hitam** - TCP (error/retransmission)
- 🟢 **Hijau** - HTTP
- 🟡 **Kuning** - Routing protocols
- 🔴 **Merah** - Error/Problem

---

### 3. **Packet Details Pane** (Tengah)
Menampilkan detail protokol berlapis (expandable tree):

```
▼ Frame 1: 74 bytes on wire
▼ Ethernet II, Src: 00:11:22:33:44:55, Dst: aa:bb:cc:dd:ee:ff
▼ Internet Protocol Version 4, Src: 192.168.1.100, Dst: 8.8.8.8
▼ Transmission Control Protocol, Src Port: 54321, Dst Port: 443
▼ Transport Layer Security
```

**Klik kanan pada field:**
- `Apply as Filter` - Gunakan sebagai filter
- `Prepare a Filter` - Siapkan filter
- `Colorize Conversation` - Beri warna percakapan
- `Follow Stream` - Ikuti stream
- `Copy` - Copy value

---

### 4. **Packet Bytes Pane** (Bawah)
Menampilkan raw data packet dalam format:
- **Hexadecimal** (kiri)
- **ASCII** (kanan)

```
0000  00 11 22 33 44 55 aa bb cc dd ee ff 08 00 45 00   .."3DU........E.
0010  00 3c 1c 46 40 00 40 06 b1 e6 c0 a8 01 64 08 08   .<.F@.@......d..
```

---

### 5. **Status Bar** (Paling Bawah)
Menampilkan:
- Jumlah packet yang di-capture
- Jumlah packet yang ditampilkan
- Jumlah packet yang di-mark
- Profile yang aktif

---

### 6. **Toolbar Buttons**

| Icon | Fungsi | Shortcut |
|------|--------|----------|
| 📂 | Open file | Ctrl+O |
| 💾 | Save | Ctrl+S |
| 🔄 | Reload | Ctrl+R |
| ▶️ | Start capture | Ctrl+E |
| ⏹️ | Stop capture | Ctrl+E |
| 🔄 | Restart capture | Ctrl+R |
| ⚙️ | Capture options | Ctrl+K |
| 🔍 | Find packet | Ctrl+F |
| ⬅️➡️ | Go back/forward | Alt+← / Alt+→ |
| 🔼🔽 | Go to packet | Ctrl+G |
| 🎨 | Colorize | View → Coloring Rules |
| 📊 | Auto scroll | View → Auto Scroll |
| 🔍+ | Zoom in | Ctrl++ |
| 🔍- | Zoom out | Ctrl+- |

---

## 🎯 Display Filters

### Syntax Dasar
```
[protocol].[field] [operator] [value]
```

### Operators

| Operator | Deskripsi | Contoh |
|----------|-----------|---------|
| `==` | Equal | `ip.addr == 192.168.1.1` |
| `!=` | Not equal | `tcp.port != 80` |
| `>` | Greater than | `frame.len > 1000` |
| `<` | Less than | `tcp.window_size < 1000` |
| `>=` | Greater or equal | `frame.time_relative >= 10` |
| `<=` | Less or equal | `ip.ttl <= 64` |
| `contains` | Contains string | `http.request.uri contains "admin"` |
| `matches` | Regex match | `http.host matches ".*\\.com"` |
| `&&` atau `and` | Logical AND | `ip.src == 192.168.1.1 && tcp.port == 80` |
| `\|\|` atau `or` | Logical OR | `tcp.port == 80 \|\| tcp.port == 443` |
| `!` atau `not` | Logical NOT | `!(arp or icmp)` |
| `in` | In range/set | `tcp.port in {80 443 8080}` |

---

### Filter Berdasarkan Protokol

#### **HTTP/HTTPS**
```bash
# Semua traffic HTTP
http

# HTTP GET requests
http.request.method == "GET"

# HTTP POST requests
http.request.method == "POST"

# HTTP responses dengan status code 200
http.response.code == 200

# HTTP 404 Not Found
http.response.code == 404

# HTTP 500 Internal Server Error
http.response.code >= 500

# Filter berdasarkan host
http.host == "example.com"

# Filter berdasarkan URI
http.request.uri contains "/admin"

# Filter User-Agent
http.user_agent contains "Mozilla"

# HTTP dengan cookie
http.cookie

# HTTPS (TLS)
tls || ssl
```

#### **TCP**
```bash
# Semua traffic TCP
tcp

# TCP port 80
tcp.port == 80

# TCP source port
tcp.srcport == 54321

# TCP destination port
tcp.dstport == 443

# TCP SYN flag (connection initiation)
tcp.flags.syn == 1

# TCP SYN-ACK (connection acknowledgment)
tcp.flags.syn == 1 && tcp.flags.ack == 1

# TCP FIN (connection termination)
tcp.flags.fin == 1

# TCP RST (reset connection)
tcp.flags.reset == 1

# TCP retransmission
tcp.analysis.retransmission

# TCP duplicate ACK
tcp.analysis.duplicate_ack

# TCP zero window (buffer penuh)
tcp.analysis.zero_window

# TCP out of order
tcp.analysis.out_of_order

# TCP connection bermasalah
tcp.analysis.flags
```

#### **UDP**
```bash
# Semua traffic UDP
udp

# UDP port specific
udp.port == 53

# UDP source port
udp.srcport == 12345

# UDP destination port
udp.dstport == 161

# UDP payload length
udp.length > 1000
```

#### **DNS**
```bash
# Semua traffic DNS
dns

# DNS query
dns.flags.response == 0

# DNS response
dns.flags.response == 1

# DNS A record query
dns.qry.type == 1

# DNS AAAA record (IPv6)
dns.qry.type == 28

# DNS MX record
dns.qry.type == 15

# DNS TXT record
dns.qry.type == 16

# DNS query untuk domain tertentu
dns.qry.name == "example.com"

# DNS query mengandung string
dns.qry.name contains "google"

# DNS response code (NXDOMAIN)
dns.flags.rcode == 3
```

#### **ICMP**
```bash
# Semua traffic ICMP
icmp

# ICMP Echo Request (ping)
icmp.type == 8

# ICMP Echo Reply (ping response)
icmp.type == 0

# ICMP Destination Unreachable
icmp.type == 3

# ICMP Time Exceeded
icmp.type == 11

# ICMPv6
icmpv6
```

#### **ARP**
```bash
# Semua traffic ARP
arp

# ARP request
arp.opcode == 1

# ARP reply
arp.opcode == 2

# ARP untuk IP tertentu
arp.dst.proto_ipv4 == 192.168.1.1

# ARP gratuitous (duplicate IP detection)
arp.isgratuitous == 1
```

#### **DHCP**
```bash
# Semua traffic DHCP
dhcp

# DHCP Discover
dhcp.option.dhcp == 1

# DHCP Offer
dhcp.option.dhcp == 2

# DHCP Request
dhcp.option.dhcp == 3

# DHCP ACK
dhcp.option.dhcp == 5

# DHCP NAK
dhcp.option.dhcp == 6

# DHCP Release
dhcp.option.dhcp == 7
```

#### **FTP**
```bash
# Semua traffic FTP
ftp

# FTP commands
ftp.request.command

# FTP USER command
ftp.request.command == "USER"

# FTP PASS command
ftp.request.command == "PASS"

# FTP responses
ftp.response.code

# FTP data transfer
ftp-data
```

#### **SSH**
```bash
# Semua traffic SSH
ssh

# SSH version exchange
ssh.protocol

# SSH port
tcp.port == 22
```

#### **Telnet**
```bash
# Semua traffic Telnet
telnet

# Telnet port
tcp.port == 23
```

#### **SMB/CIFS**
```bash
# Semua traffic SMB
smb || smb2

# SMB commands
smb.cmd

# SMB file operations
smb2.cmd == 5

# SMB tree connect
smb2.cmd == 3
```

#### **SMTP**
```bash
# Semua traffic SMTP
smtp

# SMTP commands
smtp.req.command

# SMTP MAIL FROM
smtp.req.command == "MAIL"

# SMTP RCPT TO
smtp.req.command == "RCPT"

# SMTP DATA
smtp.req.command == "DATA"
```

#### **POP3**
```bash
# Semua traffic POP3
pop

# POP3 USER command
pop.request.command == "USER"

# POP3 PASS command
pop.request.command == "PASS"
```

#### **IMAP**
```bash
# Semua traffic IMAP
imap

# IMAP LOGIN
imap.request contains "LOGIN"
```

---

### Filter Berdasarkan IP Address

```bash
# IP address tertentu (source atau destination)
ip.addr == 192.168.1.100

# IP source
ip.src == 192.168.1.100

# IP destination
ip.dst == 8.8.8.8

# IP range (subnet)
ip.addr == 192.168.1.0/24

# Multiple IP addresses
ip.addr == 192.168.1.100 || ip.addr == 192.168.1.101

# Exclude IP address
!(ip.addr == 192.168.1.1)

# Private IP addresses
ip.src == 10.0.0.0/8 || ip.src == 172.16.0.0/12 || ip.src == 192.168.0.0/16

# IPv6
ipv6.addr == 2001:db8::1
```

---

### Filter Berdasarkan MAC Address

```bash
# MAC address tertentu
eth.addr == 00:11:22:33:44:55

# MAC source
eth.src == 00:11:22:33:44:55

# MAC destination
eth.dst == aa:bb:cc:dd:ee:ff

# Broadcast MAC
eth.dst == ff:ff:ff:ff:ff:ff

# Multicast MAC
eth.dst[0] & 1
```

---

### Filter Berdasarkan Port

```bash
# Port tertentu (TCP atau UDP)
tcp.port == 80 || udp.port == 80

# Multiple ports
tcp.port in {80 443 8080 8443}

# Port range
tcp.port >= 1024 && tcp.port <= 65535

# Well-known ports (0-1023)
tcp.port < 1024

# Registered ports (1024-49151)
tcp.port >= 1024 && tcp.port <= 49151

# Dynamic/private ports (49152-65535)
tcp.port >= 49152
```

---

### Filter Berdasarkan Packet Size

```bash
# Frame length greater than 1000 bytes
frame.len > 1000

# Frame length less than 64 bytes (runt packet)
frame.len < 64

# Frame length equal to 1514 bytes (max Ethernet frame)
frame.len == 1514

# Jumbo frames
frame.len > 1514
```

---

### Filter Berdasarkan Time

```bash
# Packets dalam 5 detik pertama
frame.time_relative < 5

# Packets setelah 10 detik
frame.time_relative > 10

# Packets dalam time range
frame.time >= "2026-01-12 10:00:00" && frame.time <= "2026-01-12 11:00:00"
```

---

### Filter Advanced & Kombinasi

```bash
# HTTP traffic dari IP tertentu
ip.src == 192.168.1.100 && http

# HTTP POST dengan payload besar
http.request.method == "POST" && http.content_length > 1000

# TCP retransmission dari IP tertentu
ip.src == 192.168.1.100 && tcp.analysis.retransmission

# DNS queries kecuali ke 8.8.8.8
dns && !(ip.dst == 8.8.8.8)

# Suspicious traffic (non-standard ports)
(tcp.port == 4444 || tcp.port == 5555 || tcp.port == 31337)

# Large TCP sessions
tcp.len > 1400

# Fragmented IP packets
ip.flags.mf == 1 || ip.frag_offset > 0

# Broadcast dan multicast
eth.dst[0] & 1

# ARP scan detection
arp.opcode == 1 && frame.time_delta < 0.1

# SYN flood detection
tcp.flags.syn == 1 && tcp.flags.ack == 0

# HTTP dengan credentials
http.authorization

# HTTP redirect
http.response.code >= 300 && http.response.code < 400

# TLS handshake
tls.handshake.type == 1

# TLS alerts
tls.alert_message

# Packets dengan errors
tcp.analysis.flags || ip.checksum_bad || tcp.checksum_bad
```

---

### Filter untuk Security Analysis

```bash
# SQL Injection attempts
http.request.uri contains "union" || http.request.uri contains "select"

# XSS attempts
http.request.uri contains "<script>" || http.request.uri contains "javascript:"

# Path traversal
http.request.uri contains "../" || http.request.uri contains "..\\"

# Command injection
http.request.uri contains ";" || http.request.uri contains "|" || http.request.uri contains "&"

# Suspicious User-Agents
http.user_agent contains "sqlmap" || http.user_agent contains "nikto" || http.user_agent contains "nmap"

# Possible data exfiltration (large uploads)
http.request.method == "POST" && http.content_length > 10000000

# Port scanning (banyak SYN ke berbagai port)
tcp.flags.syn == 1 && tcp.flags.ack == 0

# Failed login attempts
http.response.code == 401 || http.response.code == 403

# Suspicious DNS queries
dns.qry.name contains "pastebin" || dns.qry.name contains "raw.githubusercontent"
```

---

## 🎣 Capture Filters

Capture filters menggunakan **BPF (Berkeley Packet Filter)** syntax - berbeda dengan display filters!

### Syntax Dasar
```
[protocol] [direction] [type] [value]
```

### Capture Filters vs Display Filters

| Aspect | Capture Filter | Display Filter |
|--------|----------------|----------------|
| **Timing** | Saat capturing | Setelah capture |
| **Syntax** | BPF syntax | Wireshark syntax |
| **Performance** | Lebih cepat | Lebih lambat |
| **Flexibility** | Terbatas | Sangat flexible |

---

### Common Capture Filters

#### **Protocol Filters**
```bash
# TCP only
tcp

# UDP only
udp

# ICMP only
icmp

# ARP only
arp

# No ARP
not arp

# DNS only
port 53
```

#### **IP Address Filters**
```bash
# Specific IP address
host 192.168.1.100

# Source IP
src host 192.168.1.100

# Destination IP
dst host 8.8.8.8

# IP range (subnet)
net 192.168.1.0/24

# Exclude IP
not host 192.168.1.1

# Multiple IPs
host 192.168.1.100 or host 192.168.1.101
```

#### **Port Filters**
```bash
# Specific port
port 80

# Source port
src port 54321

# Destination port
dst port 443

# Port range
portrange 80-443

# Multiple ports
port 80 or port 443 or port 8080

# Exclude port
not port 22
```

#### **Combined Filters**
```bash
# HTTP traffic from specific IP
host 192.168.1.100 and port 80

# DNS queries only
udp port 53 and src host 192.168.1.100

# SSH traffic except from specific IP
port 22 and not host 192.168.1.50

# Large packets
greater 1000

# Small packets
less 128

# TCP SYN packets
tcp[tcpflags] & tcp-syn != 0

# TCP connections to web servers
tcp dst port 80 or tcp dst port 443
```

---

### Advanced Capture Filters

```bash
# TCP SYN only
tcp[13] == 2

# TCP SYN-ACK
tcp[13] == 18

# TCP RST
tcp[13] & 4 != 0

# TCP FIN
tcp[13] & 1 != 0

# IPv4 only
ip

# IPv6 only
ip6

# Multicast
multicast

# Broadcast
broadcast

# VLAN traffic
vlan

# PPPoE traffic
pppoes

# Ether type
ether proto 0x0800

# MAC address
ether host 00:11:22:33:44:55

# Exclude local traffic
not net 192.168.1.0/24

# Capture everything except SSH and DNS
not (port 22 or port 53)
```

---

## 🔬 Teknik Analisis

### 1. **Follow Stream**

Follow stream memungkinkan melihat keseluruhan percakapan dalam format yang mudah dibaca.

**Cara:**
1. Klik kanan pada packet
2. Pilih `Follow` → `TCP Stream` / `UDP Stream` / `HTTP Stream` / `TLS Stream`

**Shortcut:**
- TCP Stream: Klik kanan → Follow → TCP Stream
- Filter otomatis: `tcp.stream eq 0`

**Use Cases:**
- Membaca HTTP request/response lengkap
- Melihat FTP credentials
- Analisis protokol plaintext
- Debugging aplikasi

---

### 2. **Expert Information**

Menampilkan warning, error, dan catatan dari Wireshark.

**Cara:**
- Menu: `Analyze` → `Expert Information`
- Shortcut: Lihat icon di status bar

**Kategori:**
- 🔴 **Error** - Masalah serius (checksum errors, malformed packets)
- 🟡 **Warning** - Potensi masalah (retransmissions, duplicate ACKs)
- 🔵 **Note** - Informasi (connection setup/teardown)
- 🟢 **Chat** - Informasi protokol normal

**Use Cases:**
- Troubleshooting koneksi lambat
- Menemukan packet corruption
- Identifikasi network issues

---

### 3. **Protocol Hierarchy**

Melihat distribusi protokol dalam capture.

**Cara:**
- Menu: `Statistics` → `Protocol Hierarchy`

**Informasi yang ditampilkan:**
- Persentase packet per protokol
- Bytes per protokol
- End packets

**Use Cases:**
- Mengetahui protokol dominan
- Identifikasi traffic abnormal
- Baseline network behavior

---

### 4. **Conversations**

Melihat daftar percakapan antara endpoints.

**Cara:**
- Menu: `Statistics` → `Conversations`

**Tabs:**
- Ethernet
- IPv4 / IPv6
- TCP
- UDP

**Kolom:**
- Address A ↔ Address B
- Packets
- Bytes
- Duration

**Use Cases:**
- Identifikasi top talkers
- Menemukan heavy users
- Analisis bandwidth usage

---

### 5. **Endpoints**

Melihat daftar semua endpoints dalam capture.

**Cara:**
- Menu: `Statistics` → `Endpoints`

**Informasi:**
- IP/MAC address
- Packets sent/received
- Bytes sent/received
- GeoIP (jika dikonfigurasi)

**Use Cases:**
- Identifikasi devices dalam network
- Traffic analysis per host
- Geolocation analysis

---

### 6. **I/O Graph**

Visualisasi traffic dalam bentuk grafik.

**Cara:**
- Menu: `Statistics` → `I/O Graph`

**Konfigurasi:**
- X-axis: Time
- Y-axis: Packets/bytes per interval
- Multiple graphs dengan filters berbeda

**Use Cases:**
- Visualisasi traffic patterns
- Identifikasi traffic spikes
- Perbandingan protokol

---

### 7. **Flow Graph**

Visualisasi alur packet secara sekuensial.

**Cara:**
- Menu: `Statistics` → `Flow Graph`

**Options:**
- General flow
- TCP flow
- All flows / Displayed flows

**Use Cases:**
- Memahami sequence komunikasi
- Analisis handshake
- Debugging timing issues

---

### 8. **Extract Objects**

Extract file dari traffic HTTP, SMB, TFTP, dll.

**Cara:**
- Menu: `File` → `Export Objects` → `HTTP` / `SMB` / etc

**Protokol yang didukung:**
- HTTP
- SMB/SMB2
- TFTP
- IMF (Email)

**Use Cases:**
- Forensik - extract malware
- Recovery - mendapatkan file yang di-download
- Analisis - melihat content yang dikirim

---

### 9. **Time Display Format**

Mengubah format tampilan waktu.

**Cara:**
- Menu: `View` → `Time Display Format`

**Options:**
- Date and Time of Day
- Time of Day
- Seconds Since Beginning of Capture (default)
- Seconds Since Previous Captured Packet
- Seconds Since Previous Displayed Packet

**Use Cases:**
- Analisis timing
- Korelasi dengan log lain
- Performance measurement

---

### 10. **Packet Coloring**

Menggunakan warna untuk mengidentifikasi packet types.

**Cara:**
- Menu: `View` → `Coloring Rules`

**Default colors:**
- Light purple: TCP
- Light blue: UDP
- Black background: TCP errors
- Light green: HTTP
- Yellow: Routing protocols
- Dark gray: TCP issues (retransmission, etc)

**Custom coloring:**
1. Buat filter
2. Klik `Colorize` button
3. Pilih warna

---

### 11. **Packet Marking**

Menandai packet penting untuk referensi.

**Cara:**
- Klik packet → Ctrl+M
- Atau klik kanan → Mark/Unmark Packet

**Navigation:**
- `Shift+Ctrl+N` - Next marked packet
- `Shift+Ctrl+B` - Previous marked packet

---

### 12. **Time Reference**

Set referensi waktu untuk measurement.

**Cara:**
- Klik packet → Ctrl+T
- Atau klik kanan → Set/Unset Time Reference

**Use Cases:**
- Mengukur response time
- Analisis latency
- Perbandingan timing

---

### 13. **Name Resolution**

Resolve IP/MAC address ke hostname.

**Cara:**
- Menu: `View` → `Name Resolution`

**Options:**
- Resolve MAC addresses
- Resolve network (IP) addresses
- Resolve transport addresses

**Settings:**
- Edit → Preferences → Name Resolution

---

## 💻 Command Line (TShark)

TShark adalah versi command-line dari Wireshark.

### Instalasi
```bash
# Biasanya terinstall bersamaan dengan Wireshark
tshark --version
```

---

### Basic Commands

#### **List Interfaces**
```bash
tshark -D
```

#### **Capture Packets**
```bash
# Capture pada interface eth0
tshark -i eth0

# Capture 100 packets
tshark -i eth0 -c 100

# Capture dan simpan ke file
tshark -i eth0 -w capture.pcap

# Capture dengan timeout
tshark -i eth0 -a duration:60 -w capture.pcap
```

#### **Read Capture File**
```bash
# Baca file
tshark -r capture.pcap

# Dengan display filter
tshark -r capture.pcap -Y "http"

# Export ke text
tshark -r capture.pcap > output.txt
```

---

### Display Filters
```bash
# HTTP traffic
tshark -r capture.pcap -Y "http"

# Specific IP
tshark -r capture.pcap -Y "ip.addr == 192.168.1.100"

# TCP port 443
tshark -r capture.pcap -Y "tcp.port == 443"

# Combined filters
tshark -r capture.pcap -Y "http and ip.src == 192.168.1.100"
```

---

### Capture Filters
```bash
# Gunakan -f untuk capture filter
tshark -i eth0 -f "port 80"

# Multiple filters
tshark -i eth0 -f "port 80 or port 443"

# Specific host
tshark -i eth0 -f "host 192.168.1.100"
```

---

### Field Extraction
```bash
# Extract specific fields
tshark -r capture.pcap -T fields -e ip.src -e ip.dst -e tcp.port

# Dengan separator
tshark -r capture.pcap -T fields -e ip.src -e ip.dst -E separator=,

# HTTP requests only
tshark -r capture.pcap -Y "http.request" -T fields -e http.request.method -e http.host -e http.request.uri
```

---

### Statistics
```bash
# Protocol hierarchy
tshark -r capture.pcap -q -z io,phs

# Conversations
tshark -r capture.pcap -q -z conv,tcp

# Endpoints
tshark -r capture.pcap -q -z endpoints,ip

# HTTP requests
tshark -r capture.pcap -q -z http,tree

# DNS statistics
tshark -r capture.pcap -q -z dns,tree
```

---

### Output Formats
```bash
# JSON output
tshark -r capture.pcap -T json

# PDML (XML) output
tshark -r capture.pcap -T pdml

# PS (PostScript) output
tshark -r capture.pcap -T ps

# CSV-like output
tshark -r capture.pcap -T fields -e ip.src -e ip.dst -E separator=, -E quote=d
```

---

### Advanced Usage

#### **Extract HTTP Objects**
```bash
tshark -r capture.pcap --export-objects http,./extracted_http_objects
```

#### **Follow TCP Stream**
```bash
tshark -r capture.pcap -q -z follow,tcp,ascii,0
```

#### **Decrypt HTTPS (dengan key)**
```bash
tshark -r capture.pcap -o "tls.keylog_file:sslkeylog.txt" -Y "http"
```

#### **Live Capture dengan Display**
```bash
tshark -i eth0 -Y "http" -T fields -e http.request.method -e http.host -e http.request.uri
```

#### **Capture dan Rotate Files**
```bash
# Rotate setiap 10MB atau 60 detik
tshark -i eth0 -b filesize:10240 -b duration:60 -w capture.pcap
```

#### **Real-time Statistics**
```bash
# Packet count per second
tshark -i eth0 -q -z io,stat,1
```

---

### Scripting Examples

#### **Monitor HTTP Traffic**
```bash
#!/bin/bash
tshark -i eth0 -Y "http.request" -T fields \
  -e frame.time \
  -e ip.src \
  -e http.request.method \
  -e http.host \
  -e http.request.uri \
  -E separator=, \
  -E quote=d
```

#### **Extract All URLs**
```bash
#!/bin/bash
tshark -r capture.pcap -Y "http.request" -T fields \
  -e http.host \
  -e http.request.uri | \
  awk '{print "http://"$1$2}' | sort | uniq
```

#### **Find Suspicious Traffic**
```bash
#!/bin/bash
# Mencari port scan
tshark -r capture.pcap -Y "tcp.flags.syn==1 and tcp.flags.ack==0" \
  -T fields -e ip.src | sort | uniq -c | sort -nr
```

#### **DNS Query Analysis**
```bash
#!/bin/bash
tshark -r capture.pcap -Y "dns.flags.response == 0" \
  -T fields -e dns.qry.name | sort | uniq -c | sort -nr
```

---

## 🎓 Tips & Tricks

### 1. **Keyboard Shortcuts**

| Shortcut | Fungsi |
|----------|--------|
| `Ctrl+E` | Start/Stop capture |
| `Ctrl+R` | Restart capture |
| `Ctrl+K` | Capture options |
| `Ctrl+O` | Open file |
| `Ctrl+S` | Save file |
| `Ctrl+W` | Close file |
| `Ctrl+F` | Find packet |
| `Ctrl+N` | Next packet |
| `Ctrl+B` | Previous packet |
| `Ctrl+G` | Go to packet |
| `Ctrl+M` | Mark/unmark packet |
| `Ctrl+T` | Set time reference |
| `Ctrl+/` | Apply display filter |
| `Alt+Shift+F` | Follow TCP stream |
| `Ctrl++` | Zoom in |
| `Ctrl+-` | Zoom out |
| `↓` / `↑` | Navigate packets |
| `→` / `←` | Expand/collapse tree |
| `Tab` | Move between panes |

---

### 2. **Quick Filters**

**Apply as Filter (klik kanan):**
- `Selected` - Filter packet yang selected
- `Not Selected` - Exclude packet yang selected
- `...and Selected` - AND dengan filter existing
- `...or Selected` - OR dengan filter existing
- `...and not Selected` - AND NOT dengan filter existing
- `...or not Selected` - OR NOT dengan filter existing

**Prepare as Filter:**
Sama seperti di atas tapi tidak langsung apply (muncul di filter bar untuk diedit dulu)

---

### 3. **Profile Management**

Create profiles untuk berbagai use cases:
- Security Analysis
- Web Development
- Network Troubleshooting
- VoIP Analysis

**Cara:**
1. Edit → Configuration Profiles
2. New profile
3. Atur coloring rules, columns, filters sesuai kebutuhan

---

### 4. **GeoIP Database**

Install GeoIP database untuk melihat lokasi geografis IP addresses:

**Download:**
- MaxMind GeoLite2 databases (gratis)

**Configure:**
1. Edit → Preferences → Name Resolution
2. MaxMind database directories
3. Add path ke GeoIP database

**Usage:**
- Lihat di Endpoints statistics
- Filter: `ip.geoip.country == "US"`

---

### 5. **Decrypting HTTPS Traffic**

**Method 1: SSL Key Log File**
```bash
# Set environment variable
export SSLKEYLOGFILE=/path/to/sslkeylog.txt

# Chrome/Firefox akan menulis keys ke file ini
# Kemudian load di Wireshark
```

**Wireshark Configuration:**
1. Edit → Preferences → Protocols → TLS
2. (Pre)-Master-Secret log filename: browse ke sslkeylog.txt

**Method 2: Private Key**
1. Edit → Preferences → Protocols → TLS
2. RSA keys list: tambah IP, port, protocol, key file

---

### 6. **Performance Optimization**

**Untuk capture besar:**
```bash
# Gunakan ring buffer
tshark -i eth0 -b filesize:100000 -b files:10 -w capture.pcap

# Capture hanya yang diperlukan
tshark -i eth0 -f "port 80 or port 443" -w capture.pcap

# Jangan resolve names saat capture
tshark -i eth0 -n -w capture.pcap
```

**Di Wireshark:**
- Disable name resolution saat capture
- Gunakan capture filter untuk mengurangi data
- Close unutilized protocol dissectors
- Edit → Preferences → Protocols → disable yang tidak perlu

---

### 7. **Custom Columns**

Tambah kolom custom untuk informasi yang sering dilihat:

**Cara:**
1. Klik kanan pada packet detail field
2. Apply as Column

**Contoh kolom berguna:**
- HTTP Request Method: `http.request.method`
- HTTP Host: `http.host`
- HTTP URI: `http.request.uri`
- HTTP Response Code: `http.response.code`
- DNS Query Name: `dns.qry.name`
- TCP Stream: `tcp.stream`

---

### 8. **Comparing Captures**

**Method 1: Using editcap**
```bash
# Merge multiple captures
mergecap -w merged.pcap capture1.pcap capture2.pcap

# Split capture by time
editcap -A "2026-01-12 10:00:00" -B "2026-01-12 11:00:00" capture.pcap filtered.pcap
```

**Method 2: Manual comparison**
- Open kedua file di Wireshark instances berbeda
- Gunakan identical filters
- Compare statistics

---

### 9. **Remote Capture**

**Menggunakan SSH:**
```bash
# Capture di remote server
ssh user@remote-host "tcpdump -i eth0 -w - 'port 80'" | wireshark -k -i -
```

**Menggunakan TShark:**
```bash
# Capture remote dan save local
ssh user@remote-host "tshark -i eth0 -w -" > local_capture.pcap
```

---

### 10. **Baseline Normal Traffic**

1. Capture traffic saat kondisi normal
2. Analisis:
   - Protocol Hierarchy
   - Conversations
   - Endpoints
   - I/O Graph
3. Save sebagai reference
4. Compare dengan traffic saat masalah terjadi

---

### 11. **Security Analysis Workflow**

```
1. Capture Traffic
   ↓
2. Quick Analysis
   - Expert Information (cari errors/warnings)
   - Protocol Hierarchy (cari anomali)
   ↓
3. Filter Suspicious
   - Non-standard ports
   - Failed connections
   - Large data transfers
   ↓
4. Deep Dive
   - Follow streams
   - Extract objects
   - Analyze payloads
   ↓
5. Document Findings
```

---

### 12. **Common Issues & Solutions**

#### **"No interfaces found"**
```bash
# Linux - jalankan dengan sudo
sudo wireshark

# Atau tambah user ke wireshark group
sudo usermod -a -G wireshark $USER
sudo chmod +x /usr/bin/dumpcap

# Windows - run as Administrator
```

#### **"Dropped packets"**
- Gunakan capture filter
- Increase buffer size
- Capture ke SSD/RAM disk
- Disable nama resolution
- Use multiple interfaces dengan mergecap

#### **"Checksum errors"**
- Biasanya false positive dari offloading
- Disable: Edit → Preferences → Protocols → TCP/UDP → Validate checksums

---

### 13. **Best Practices**

1. **Always use capture filters untuk production networks**
2. **Save raw captures** - analisis bisa dilakukan nanti
3. **Document filter expression** yang sering digunakan
4. **Use profiles** untuk use cases berbeda
5. **Regular updates** - protokol baru terus ditambahkan
6. **Practice dengan pcap samples** sebelum production
7. **Combine dengan tools lain** (nmap, netstat, iptables)
8. **Understand network architecture** sebelum capture
9. **Check legal/policy** sebelum capture di production
10. **Anonymize sensitive data** sebelum share captures

---

## 📚 Resources & Learning

### Official Documentation
- [Wireshark User's Guide](https://www.wireshark.org/docs/wsug_html_chunked/)
- [Wireshark Wiki](https://wiki.wireshark.org/)
- [Display Filter Reference](https://www.wireshark.org/docs/dfref/)

### Practice Captures
- [Wireshark Sample Captures](https://wiki.wireshark.org/SampleCaptures)
- [Malware Traffic Analysis](https://www.malware-traffic-analysis.net/)
- [PacketLife Captures](http://packetlife.net/captures/)

### Books
- "Wireshark Network Analysis" - Laura Chappell
- "Practical Packet Analysis" - Chris Sanders
- "Network Analysis Using Wireshark 2 Cookbook" - Nagendra Kumar

### Online Courses
- Wireshark Certified Network Analyst (WCNA)
- Udemy Wireshark courses
- Cybrary network analysis courses

---

## 🎯 Quick Reference Card

### Most Used Display Filters
```bash
ip.addr == 192.168.1.100          # Specific IP
tcp.port == 80                     # HTTP traffic
http.request.method == "POST"     # HTTP POST
dns                                # DNS traffic
tcp.analysis.retransmission       # TCP issues
!(arp or icmp or dns)             # Exclude noise
http.response.code >= 400         # HTTP errors
tcp.flags.syn==1 && tcp.flags.ack==0  # SYN packets
```

### Most Used Capture Filters
```bash
host 192.168.1.100                # Specific IP
port 80                           # Port 80
tcp port 443                      # HTTPS
not port 22                       # Exclude SSH
net 192.168.1.0/24                # Subnet
port 80 or port 443               # Multiple ports
```

### Keyboard Shortcuts Quick List
```
Ctrl+E    Start/Stop
Ctrl+K    Options
Ctrl+F    Find
Ctrl+G    Go to packet
Ctrl+M    Mark packet
Ctrl+/    Apply filter
```

---

## ⚠️ Legal & Ethical Considerations

**PENTING:**
1. ✅ Capture hanya di network yang anda miliki atau punya izin
2. ✅ Follow company policy dan local laws
3. ✅ Protect privacy - jangan capture kredensial orang lain
4. ✅ Anonymize data sebelum share
5. ❌ Jangan gunakan untuk tujuan ilegal
6. ❌ Jangan capture tanpa izin di network publik/orang lain

---

## 🏆 Kesimpulan

Wireshark adalah tool yang sangat powerful untuk:
- **Network troubleshooting** - diagnosa masalah koneksi
- **Security analysis** - deteksi intrusi dan malware
- **Performance optimization** - identifikasi bottleneck
- **Protocol development** - debugging protokol baru
- **Education** - belajar bagaimana network bekerja

**Mastery membutuhkan:**
1. Pemahaman protocol fundamentals (TCP/IP, HTTP, DNS, dll)
2. Practice dengan berbagai scenarios
3. Understanding network architecture
4. Kombinasi dengan tools lain

**Next Steps:**
1. Install Wireshark dan explore interface
2. Capture traffic dari browsing anda sendiri
3. Practice dengan sample captures
4. Pelajari satu protokol dalam sekaligus
5. Build filter library untuk use cases anda
6. Join community dan terus belajar

---

**Happy Packet Hunting! 🦈📡**

---

*Cheat sheet ini dibuat untuk tujuan edukasi. Gunakan dengan bertanggung jawab dan legal.*

**Version:** 2.0  
**Last Updated:** January 12, 2026  
**Author:** TangselSecTeam - Batch 1
