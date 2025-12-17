# TangselSecTeam Project

![Screenshot of the app](./images/roadmap.jpg)

# KURIKULUM CYBER SECURITY TRAINING

---

## BATCH KE 1

### Pertemuan 1 – Fondasi Cyber Security & Lab Setup

**Fokus:**
- Konsep dasar: Ethical hacking, threat, vulnerability, risk
- Perbedaan defensive vs offensive

**Tools:**
- VirtualBox / VMware
- Linux (misal: Kali Linux / Ubuntu)

**Praktek:**
- Menginstall Kali Linux di VMware
- Pengenalan tools yang ada di Kali Linux, dasar-dasar Linux

---

### Pertemuan 2 – Dasar Networking untuk Security

**Fokus:**
- TCP/IP, port, service
- HTTP vs HTTPS
- Konsep firewall & segmentasi
- Pengenalan spoofing dan sniffing traffic network

**Tools:**
- `nmap`
- `netstat`, `ss`
- Wireshark / tcpdump
- Aircrack-ng, airdump

**Praktek:**
- Scan port VM target dengan nmap
- Capture traffic HTTP dengan Wireshark (akses web sederhana)
- Bedakan paket HTTP dan HTTPS di capture

---

### Pertemuan 3 – Linux & Server Hardening Dasar

**Fokus:**
- Permission, service, user, sudo
- Konsep hardening dasar (disable service, update, firewall)

**Tools:**
- Linux CLI: `ps`, `top`, `systemctl`, `ufw`/`firewalld`, `chmod`, `chown`
- SSH

**Praktek:**
- Buat user baru khusus service
- Konfigurasi firewall sederhana (hanya buka SSH + HTTP)
- Tunjukkan perbedaan permission file sensitif (contoh: `.env` aplikasi)

---

### Pertemuan 4 – Web Security & OWASP Top 10 Overview

**Fokus:**
- Gambaran OWASP Top 10 (auth, injection, XSS, IDOR)
- Cara pikir attacker vs developer

**Tools:**
- DVWA atau OWASP Juice Shop
- Browser dev tools
- Burp Suite

**Praktek:**
- Deploy DVWA/Juice Shop di VM target
- Coba login default / brute password lemah
- Tunjukkan contoh input tidak tervalidasi (form, URL)

---

### Pertemuan 5 – Offensive: Recon & Scanning

**Fokus:**
- Information gathering sebelum serang
- Active vs passive recon

**Tools:**
- `nmap` (service detection, OS detection)
- `whatweb`, `nikto`, `nuclei`
- `dig`, `nslookup`

**Praktek:**
- Identifikasi service yang berjalan di target: web, SSH, DB
- Scan versi service dan catat potensi vuln
- Buat laporan sederhana: "asset + service + port + kemungkinan risiko"

---

### Pertemuan 6 – Offensive: Web Exploitation (SQL Injection)

**Fokus:**
- Konsep SQL injection
- Input tidak di-sanitize / tidak pakai prepared statements

**Tools:**
- DVWA (SQLi module)
- Burp Suite (Community)
- Browser

**Praktek:**
- Eksploitasi SQLi di DVWA (level low/medium)
- Dump sebagian data user dari database via SQLi
- Diskusi: cara mencegah (prepared statement, parameterized query)

---

### Pertemuan 7 – Offensive: XSS & Session Hijacking Sederhana

**Fokus:**
- Reflected & Stored XSS
- Risiko: pencurian cookie, deface, phishing

**Tools:**
- DVWA / Juice Shop (XSS challenge)
- Burp Suite (repeater)

**Praktek:**
- Tanam payload XSS di form komentar
- Tunjukkan eksekusi script di browser korban
- Diskusi mitigasi: output encoding, CSP, sanitize

---

### Pertemuan 8 – Defensive: Logging & Monitoring Dasar

**Fokus:**
- Pentingnya log untuk incident response
- Apa yang harus di-log (auth, error, access log, admin action)

**Tools:**
- Linux log: `/var/log/*`
- Web server log (Apache/Nginx)
- Simple log viewer / grep

**Praktek:**
- Tunjukkan jejak serangan (scan, login gagal, request aneh) di access log dari VM DVWA/Juice Shop
- Filter log pakai `grep`/`awk` (misal IP attacker)
- Buat mini "incident report" dari log (jam berapa, IP mana, apa aksinya)

---

### Pertemuan 9 – Defensive: Web Server Hardening

**Fokus:**
- Konfigurasi aman untuk Nginx/Apache
- Disable directory listing, limit method, header security

**Tools:**
- Nginx/Apache config
- `curl -v` / browser dev tools (cek header)

**Praktek:**
- Tambahkan security header: `X-Frame-Options`, `X-Content-Type-Options`, `Content-Security-Policy` sederhana
- Matikan server tokens (jangan bocorkan versi server)
- Test sebelum & sesudah pakai `curl -I` / dev tools

---

### Pertemuan 10 – Defensive: Secure Coding (Backend/Web API)

**Fokus:**
- Validasi input & output
- Auth & authorization (role, access control)
- Secure file upload & path

**Tools:**
- Bahasa yang dipakai tim (misal: PHP)
- Simple code example vulnerable + versi yang sudah diperbaiki

**Praktek:**
- Review snippet kode yang vuln (SQLi, XSS, file upload)
- Refactor jadi versi aman (prepared statement, filter, limit extension)
- Unit test / manual test: serang lagi dan buktikan sudah aman

---

### Pertemuan 11 – SIEM Sederhana & Alerting (Simulasi)

**Fokus:**
- Konsep SIEM (gabung log, korelasi, alert)
- Deteksi pola aneh (bruteforce, scan, login gagal banyak)

**Tools:**
- Simulasikan SIEM pakai:
  - ELK stack (Elasticsearch + Logstash + Kibana), atau
  - Minimal: GoAccess / Wazuh / parse log dan visualisasi
  - Atau pakai layanan free-tier kalau memungkinkan

**Praktek:**
- Kirim access log web ke tool (ELK/GoAccess)
- Buat filter: IP dengan > X request/menit, atau login gagal berulang
- Tunjukkan dashboard / grafik pattern "serangan"

---

### Pertemuan 12 – Password, Auth & Session Security

**Fokus:**
- Hashing (bcrypt/argon2), bukan simpan plain text
- Session management, cookie, JWT
- Multi-factor Authentication (konsep)

**Tools:**
- Demo kecil app login
- Hash function (PHP, Python, dsb)

**Praktek:**
- Tunjukkan perbedaan simpan password plain vs hash
- Simulasikan bruteforce terhadap password lemah
- Tambah limit login attempt + delay + lockout

---

### Pertemuan 13 – Mini Red Team vs Blue Team Simulation

**Fokus:**
- Menggabungkan semua skill: serang & bertahan
- Satu tim jadi attacker, satu defender

**Tools:**
- Semua yang sudah dipakai: nmap, Burp, log, server config, DVWA, dsb

**Praktek:**
- **Skenario:**
  - **Attacker:** coba recon + exploit web/app
  - **Defender:** monitoring log, block IP, perbaiki config, patch vuln
- **Setelah sesi, lakukan debrief:**
  - Serangan apa yang berhasil?
  - Apa yang kurang dari sisi defense?
  - Apa yang harus diperbaiki di proses?

---

### Pertemuan 14 – Capture The Flag (CTF) Mini + Review & Rencana Lanjut

**Fokus:**
- Menyatukan semua materi dalam bentuk challenge
- Evaluasi pemahaman & skill

**Tools:**
- CTF internal sederhana (bisa pakai):
  - Beberapa vuln di DVWA/Juice Shop
  - Server dengan beberapa misconfig
  - Log yang sudah disiapkan, dll

**Praktek:**
- **Buat 5–10 challenge:**
  - Temukan SQLi & ambil 1 data
  - Temukan XSS & buat alert
  - Cari password lemah di log / config
  - Hardening server sampai scan jadi "lebih bersih"
- **Tutup dengan:**
  - Review materi 14 pertemuan
  - Saran roadmap lanjutan (OSCP path, Blue Team path, AppSec path)

---

## BATCH KE 2

### 1. OSINT (Open Source Intelligence) untuk Recon

**Fokus:**
Mengumpulkan informasi target dari sumber terbuka, sebelum serangan / assessment.

**Tools:**
- Browser, Google dorks
- `whois`, `nslookup`, `dig`
- hunter.io / email-finder sejenis (kalau ada)
- Shodan/Censys (kalau bisa akses, di lab)

**Praktik:**
- Pilih target simulasi (bisa domain dummy / lingkungan lab organisasi sendiri)
- **Cari:**
  - Subdomain, IP, DNS info
  - Teknologi yang dipakai (server, framework, dll)
  - Email publik / pola username
- Dokumentasikan hasil OSINT dalam 1 report singkat (yang nanti bisa dipakai untuk pentest lab)

---

### 2. Linux & Web Server Forensics (Post-Hack Investigation)

**Fokus:**
Investigasi server Linux yang sudah diacak-acak attacker (web shell, brute force, dll).

**Tools:**
- Linux server lab + web app (DVWA/Juice Shop)
- `grep`, `journalctl`, `less`
- Log web (access/error)

**Praktik:**
- Serang web lab (misal brute login / coba upload file)
- **Dari sisi server:**
  - Cek `/var/log/auth.log` / `secure`
  - Cek access log web
- Temukan: IP attacker, path/URL yang diserang, waktu serangan
- Susun timeline insiden dari log

---

### 3. Memory Forensics (Volatility) – Jejak Malware & RAT

**Fokus:**
Mencari proses jahat, koneksi aneh, injeksi proses di RAM.

**Tools:**
- Sample memory dump (image training)
- Volatility / Volatility3

**Praktik:**
- Load memory dump
- **Jalankan:**
  - `pslist` / `psscan`
  - `netscan`
  - (kalau ada) `malfind`
- **Identifikasi:**
  - Proses mencurigakan (nama, path, PID)
  - Koneksi keluar ke IP tidak dikenal
- Buat ringkasan: proses mana yang mencurigakan & kenapa

---

### 4. Network Forensics & Analisa PCAP Serangan

**Fokus:**
Melihat serangan lewat paket (network evidence).

**Tools:**
- Wireshark / tshark
- PCAP yang berisi serangan (scan, brute, download file)

**Praktik:**
- **Buka PCAP berisi:**
  - Port scan
  - Login brute force
  - Mungkin download file
- **Filter:**
  - Berdasarkan IP attacker
  - Berdasarkan protokol (HTTP/SSH, dsb)
- **Temukan:**
  - Jenis serangan
  - Target port
  - Apakah ada data sensitif lewat
- Buat mini incident report dari PCAP

---

### 5. Threat Intel & CVE Hunting (Operational)

**Fokus:**
Menghubungkan CVE & exploit dengan sistem nyata.

**Tools:**
- `nmap -sV`
- Browser (NVD, Mitre, vendor advisory)

**Praktik:**
- Scan service di server lab (`nmap -sV <ip>`)
- Pilih beberapa service (Apache, PHP, SSH, DB)
- **Cari CVE terkait versi itu:**
  - Catat ID CVE
  - Severity (CVSS)
  - Dampak singkat
- Buat list prioritas patching untuk environment lab

---

### 6. Phishing, Logger & Spoofing Attack (Lab)

**Fokus:**
Memahami chain: phishing → credential harvesting / logger → spoofing identitas (di lab & etis).

**Tools:**
- Mail server lab / simulasi email spoof (bisa juga pakai tool offline)
- Simple web phishing page (HTML form)
- Burp Suite (untuk lihat request)
- DNS/spoofing konsep (tanpa menyerang publik)

**Praktik:**
- Buat halaman login palsu (lab) yang mirip layanan tertentu
- Simulasikan email phishing (ditulis, tapi dikirim hanya di lingkungan latihan)
- **Kirim "korban" (peserta lain) ke halaman itu:**
  - Capture credential di server (di log)
- **Tampilkan:**
  - Request HTTP (username/password)
  - Bahas cara mitigasi: awareness, SPF/DKIM, 2FA, URL check
- **Ditekankan:** hanya di lab / environment training, bukan ke user real

---

### 7. Cloud Security: IAM & Network (Security-First)

**Fokus:**
Keamanan akses & jaringan di cloud (bukan cuma "bisa jalan").

**Tools:**
- Proxmox
- Console/CLI

**Praktik:**
- Buat 1 VM instance + security group
- **Konfigurasi:**
  - Firewall Proxmox agar dari VM tidak bisa ping hypervisor
  - Menggunakan firewall Proxmox dan iptables
- Melakukan backup dan restore

---

### 8. Cloud Misconfiguration (Attack & Fix)

**Fokus:**
Bagaimana misconfig cloud (bucket public, dsb) dipakai attacker, dan cara memperbaikinya.

**Tools:**
- Cloud storage: NFS, CEPH, SAMBA, SFTP
- Browser/CLI
- (Opsional) menggunakan tool audit ScoutSuite/Prowler

**Praktik:**
- Buat bucket dan upload file "sensitif" dummy (e.g. `config_backup.txt`)
- Set bucket/object public, akses dari browser tanpa login
- Perbaiki policy (private / only specific identity) → test lagi
- **Tuliskan:**
  - Risiko kalau setting awal dipakai di production
  - Checklist misconfig yang harus dicek rutin

---

### 9. DevSecOps & Secure SDLC (Desain + Implementasi Minimum)

**Fokus:**
Menyusun SDLC yang ada kontrol security di setiap tahap.

**Tools:**
- Diagram tool, Git repo, CI basic (GitLab/GitHub/Jenkins)

**Praktik:**
- **Gambar flow SDLC:**
  - Plan → Code → Build → Test → Deploy → Monitor
- **Di tiap step, tentukan:**
  - Kontrol security apa: code review, SAST, DAST, approval, logging, dsb
- **Implementasi minimal:**
  - Repositori + minimal 1 branch protection rule (misal: wajib review sebelum merge)
- Presentasi desain secure SDLC tiap kelompok

---

### 10. CI/CD Security: SAST & Dependency Scan di Pipeline

**Fokus:**
DevSecOps "beneran jalan", bukan cuma di gambar.

**Tools:**
- GitLab CI / GitHub Actions / Jenkins
- Semgrep (SAST)
- Trivy / Dependency-Check (SCA)

**Praktik:**
- Ambil app web dummy (PHP/Node/Go sesuai tim)
- **Setup pipeline:**
  - Stage build/test
  - Stage security: Semgrep + dependency scan
- **Konfigurasi rule:**
  - Kalau ada vuln HIGH → job fail
- **Tunjukkan:**
  - Pipeline merah dulu (karena ada masalah)
  - Setelah kode diperbaiki → pipeline hijau

---

### 11. Proxy, VPN & Tunneling (Offense & Defense)

**Fokus:**
Bagaimana attacker pakai proxy/VPN/tunneling untuk menyembunyikan jejak, dan apa impact ke defender.

**Tools:**
- Burp Suite (proxy)
- SSH tunneling (`ssh -L`, `ssh -D`)
- VPN (lab / Proton/WireGuard lokal)
- Browser setting proxy

**Praktik:**
- Set Burp sebagai proxy di browser → lihat seluruh request ketika akses web lab
- **Buat SSH tunnel:**
  - Contoh `ssh -D` sebagai SOCKS proxy, test lewat browser
- **Diskusi/lihat:**
  - IP di server log (cuma lihat IP proxy/VPN)
  - Gimana sulitnya blocking user yang pakai tunneling
- **Bahas strategi defensif:**
  - GeoIP block (terbatas)
  - Anomaly detection
  - Multi-factor auth

---

### 12. Security Automation: Membangun Tools Sendiri

**Fokus:**
Bikin automation yang benar-benar membantu kerja security sehari-hari.

**Tools:**
- Python (requests, subprocess, json)
- nmap / scanner lain
- (Opsional) API CVE / API chat/Slack/Telegram

**Praktik:**
- **Buat script Python:**
  - Input: list IP / range
  - Jalankan scan (nmap atau lainnya)
  - Parse hasil (port terbuka + service)
- **Export hasil ke:**
  - JSON/CSV
  - Tandai port "risk tinggi"
- (Opsional) Kirim summary ke webhook (Slack/Telegram) kalau ditemukan port kritikal

---

### 13. Lab Exploit CVE (Terkini) di Lingkungan Aman

**Fokus:**
Mempraktikkan CVE/exploit terbaru secara aman dan terkontrol.

**Tools:**
- Vuln images (Vulhub / Docker vuln lab / VM Metasploitable)
- Browser/Burp/Metasploit (kalau perlu)

**Praktik:**
- Pilih 1–2 image vulnerable sesuai CVE (yang ada PoC resmi/di lab)
- Jalankan service vuln di host lab
- **Jalankan exploit:**
  - Baca langkah PoC, jalankan step-by-step
  - Lihat hasil (RCE, info leak, auth bypass)
- **Diskusi:**
  - Log apa yang terekam
  - Mitigasi: patch, config, rule tambahan

---

### 14. Recovery & Hardening: Menyelamatkan Server/OS Setelah Crash / Hack

**Fokus:**
Bagaimana menyelamatkan sistem & data setelah:
- Crash (hardware/software)
- Dan/atau diacak-acak hacker, terkena ransomware, penuh malware dan virus
- Lalu melakukan hardening (hardener)

**Tools:**
- VM server lab (Linux), backup image/snapshot
- Tools backup: `rsync`, `tar`, snapshot VM
- Hardening: firewall, user/permission, service minimal

**Praktik:**
- **Simulasikan:**
  - Server rusak: misal config web dihapus, service gagal start
  - Atau data penting diubah (di-log saja untuk demo, jangan benar-benar rusak permanen)
- **Lakukan recovery:**
  - Dari backup file / snapshot
  - Restore config dan data penting
- **Setelah "pulih", lakukan hardening:**
  - Matikan service tidak perlu
  - Perbaiki permission file sensitif
  - Pasang firewall basic (hanya port tertentu)
- **Buat checklist:**
  - Langkah recovery
  - Langkah hardening yang dilakukan
  - Rekomendasi untuk mencegah kejadian serupa

---

**END OF CURRICULUM**
