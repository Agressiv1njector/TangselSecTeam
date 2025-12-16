# PERTEMUAN 1 - FONDASI CYBER SECURITY & LAB SETUP

##  A. TEORI DASAR CYBER SECURITY

### 1.1 Pengertian Cyber Security

**Definisi Utama:**
Cyber Security adalah praktik, proses, dan teknologi yang dirancang untuk melindungi jaringan, sistem komputer, dan data digital dari serangan, kerusakan, atau akses tidak sah.

**Perspektif Alternatif:**

1. **Perspektif Teknis:**
   Cyber Security adalah implementasi kontrol teknologi (firewall, encryption, IDS/IPS, antivirus) untuk mencegah, mendeteksi, dan merespons ancaman cyber.

2. **Perspektif Manajemen Risiko:**
   Cyber Security adalah proses identifikasi, analisis, dan mitigasi risiko terkait aset digital dan informasi organisasi.

3. **Perspektif Hukum & Compliance:**
   Cyber Security adalah penerapan kebijakan, prosedur, dan teknologi untuk mematuhi regulasi perlindungan data (GDPR, UU ITE, HIPAA, PCI-DSS, dll).

4. **Perspektif Operasional:**
   Cyber Security adalah sekumpulan praktik operasional yang terus-menerus untuk memastikan confidentiality, integrity, dan availability (CIA) dari sistem informasi.

---

**Prinsip Utama Cyber Security:**

**1. Confidentiality (Kerahasiaan)**
- Memastikan data hanya diakses oleh pihak yang berwenang
- Teknik: Enkripsi, access control, authentication
- Contoh: Database customer tidak boleh diakses oleh semua karyawan

**2. Integrity (Integritas)**
- Memastikan data tidak diubah tanpa izin atau tidak diubah secara tidak sengaja
- Teknik: Checksum, digital signature, version control
- Contoh: Transaksi keuangan harus akurat dan tidak boleh dimanipulasi

**3. Availability (Ketersediaan)**
- Memastikan sistem & data dapat diakses oleh pengguna yang berwenang kapan dibutuhkan
- Teknik: Redundancy, backup, disaster recovery
- Contoh: Website layanan publik harus online 24/7

**4. Authenticity (Keaslian)**
- Memastikan bahwa data/komunikasi berasal dari sumber yang tepat
- Teknik: Digital certificate, digital signature, multi-factor authentication
- Contoh: Verifikasi bahwa email dari bank benar-benar dari bank

**5. Non-repudiation (Tanpa Penyangkalan)**
- Memastikan bahwa pengirim tidak bisa menyangkal telah mengirim data
- Teknik: Digital signature, audit log, tamper-proof logging
- Contoh: Bukti digital bahwa karyawan telah menandatangani perjanjian

---

**Scope & Domain Cyber Security:**

| Domain | Penjelasan | Contoh |
|--------|-----------|---------|
| **Network Security** | Perlindungan jaringan dari akses/modifikasi tidak sah | Firewall, VPN, IDS/IPS |
| **Application Security** | Perlindungan aplikasi dari vulnerability & exploit | Code review, penetration testing, WAF |
| **Data Security** | Perlindungan data saat disimpan & transit | Encryption, access control, DLP |
| **Endpoint Security** | Perlindungan perangkat (laptop, PC, mobile) | Antivirus, MDM, EDR |
| **Cloud Security** | Perlindungan data & layanan di cloud | Cloud access security brokers, encryption |
| **Identity & Access Mgmt** | Manajemen identitas & otorizasi akses | SSO, MFA, RBAC, PAM |
| **Incident Response** | Respons terhadap serangan/insiden keamanan | Forensik, containment, recovery |
| **Compliance & Governance** | Penerapan regulasi & standar keamanan | GDPR, ISO 27001, SOC 2 |
| **Security Awareness** | Pelatihan karyawan tentang keamanan siber | Phishing simulation, training, policies |

---

**Definisi Aktor dalam Cyber Security:**

**1. Threat Actor (Pelaku Ancaman):**
- **Cybercriminal**: Mencari keuntungan finansial (fraud, ransomware, data theft)
- **Hacker/Attacker**: Memiliki motivasi ideologi atau personal
- **Nation-State**: Aktor negara dengan tujuan geopolitik/intelijen
- **Insider Threat**: Karyawan/pihak dalam dengan akses yang menyalahgunakan privilege
- **Script Kiddie**: Pemula yang menggunakan tools/exploit yang sudah ada

**2. Defender (Pihak Pertahanan):**
- **Security Operations Center (SOC)**: Tim 24/7 untuk monitoring & response
- **Incident Response Team (IRT)**: Respons cepat terhadap insiden keamanan
- **Security Architect**: Merancang arsitektur keamanan sistem
- **Penetration Tester**: Mengidentifikasi vulnerability dengan simulasi serangan
- **Security Analyst**: Menganalisis log, threat intel, dan vulnerability

**3. Ethical Hacker:**
- Profesional yang melakukan penetration testing dengan izin
- Tujuan konstruktif: menemukan dan memperbaiki vulnerability
- Mematuhi hukum, etika, dan kontrak legal

---

**Tujuan Cyber Security:**

✓ **Melindungi aset digital** dari pencurian, modifikasi, atau penghancuran  
✓ **Memastikan business continuity** tanpa gangguan dari serangan cyber  
✓ **Mematuhi regulasi & standar** perlindungan data yang berlaku  
✓ **Meminimalkan risiko & dampak** jika serangan terjadi  
✓ **Membangun kepercayaan** pelanggan & stakeholder  
✓ **Merespons cepat** terhadap insiden keamanan  
✓ **Edukasi & awareness** karyawan tentang pentingnya keamanan  

---

**Mengapa Cyber Security Penting?**

```
STATISTIK SERANGAN CYBER:
- Rata-rata organisasi mengalami 120 serangan per hari
- Data breach rata-rata memicu kerugian $4.29 juta USD
- Waktu deteksi serangan: rata-rata 287 hari
- 60% organisasi mengalami ransomware attack tahun ini
- 45% data breach melibatkan human error

DAMPAK SERANGAN CYBER:
- **Finansial**: Kerugian uang, biaya recovery, denda regulasi
- **Reputasi**: Hilang kepercayaan pelanggan, penurunan brand value
- **Operasional**: Downtime sistem, gangguan layanan, produktivitas turun
- **Hukum**: Tanggung jawab hukum, tuntutan, kriminal charges
- **Strategis**: Kehilangan competitive advantage, data kompetitor dicuri
```

---

**Evolution Cyber Security:**

| Era | Fokus | Tools/Metode | Challenge |
|-----|-------|-------------|-----------|
| **2000s** | Virus & Worm | Antivirus, firewall stateless | Single layer defense |
| **2010s** | Advanced APT | SIEM, IDS/IPS, threat intel | Multi-vector attacks |
| **2020s** | Cloud & Mobile | EDR, SOAR, AI/ML detection | Ransomware, supply chain |
| **2030s** | AI-driven** | Zero Trust, behavioral analytics, quantum-safe | AI-powered attacks |

---

***Q: bagaimana jika semua orang menjadi cyber security aja biar ga usah ada hacker ?***
**Answer:**
Jika semua orang menjadi cybersecurity expert, tentunya itu akan sangat mengurangi jumlah atau bahkan menghilangkan keberadaan hacker yang jahat. Namun, ada beberapa hal yang perlu dipertimbangkan untuk memahami bagaimana situasi tersebut bisa berpengaruh pada dunia digital:

1. Peningkatan Keamanan Secara Global

Jika semua orang memiliki pengetahuan tentang cybersecurity, maka tingkat kesadaran dan pemahaman tentang ancaman digital akan sangat meningkat. Ini berarti banyak orang yang lebih berhati-hati dalam melindungi data pribadi mereka, menghindari serangan phishing, dan tidak sembarangan menggunakan perangkat atau jaringan yang tidak aman.

Keamanan sistem juga akan menjadi prioritas utama dalam setiap organisasi, memperkecil kemungkinan kebocoran data, serangan DDoS, atau peretasan.

2. Pengurangan Kerentanannya

Banyaknya individu yang memiliki keahlian dalam cybersecurity akan membantu mengidentifikasi dan mengatasi kerentanannya sebelum mereka bisa dimanfaatkan oleh pihak yang berniat jahat. Misalnya, lebih banyak orang yang akan memperhatikan pengaturan password yang kuat, enkripsi data, dan firewall yang lebih canggih.

Keamanan data pribadi juga akan lebih terlindungi, karena lebih banyak orang yang sadar tentang pentingnya menjaga informasi sensitif.

3. Tantangan dalam Menjaga Inovasi

Meskipun kita bisa membayangkan dunia yang lebih aman, ada sisi lain yang harus dipertimbangkan: keamanan yang terlalu ketat bisa menghambat beberapa inovasi. Jika semua orang memiliki keterampilan tingkat tinggi dalam cybersecurity, mereka mungkin menjadi terlalu fokus pada proteksi dan kehilangan rasa fleksibilitas atau kreativitas dalam pengembangan aplikasi dan teknologi baru.

Selain itu, beberapa individu mungkin menyalahgunakan pengetahuan mereka untuk memata-matai atau mencoba untuk menyusup ke sistem yang lebih aman untuk "bermain-main" atau menguji keterampilan mereka.

4. Hacker yang Lebih Canggih

Meskipun banyak orang terlatih dalam cybersecurity, itu juga berpotensi melahirkan lebih banyak hacker yang lebih pintar. Hacker yang terlatih bisa lebih canggih dalam menghindari deteksi dan mengeksploitasi celah yang lebih kompleks dalam sistem.

Keahlian cybersecurity yang tersebar luas mungkin justru memperburuk keadaan bagi organisasi atau individu yang tidak memiliki tingkat keahlian yang cukup tinggi. Hacker yang terlatih dan berpengalaman mungkin menjadi lebih sulit untuk dideteksi.

5. Masalah Keamanan Etis dan Privasi

Jika banyak orang tahu cara melindungi diri mereka dari hacker, pertanyaannya adalah bagaimana kita mengelola keamanan etis? Ada perbedaan besar antara pengujian penetrasi yang sah (ethical hacking) dan serangan berbahaya yang bertujuan merusak atau mencuri informasi. Semua orang yang memiliki keterampilan ini perlu memiliki prinsip moral dan etika yang sangat kuat untuk membedakan antara yang benar dan salah dalam dunia maya.

Privasi juga bisa menjadi masalah. Beberapa orang mungkin menggunakan keterampilan mereka untuk memata-matai orang lain atau melanggar privasi individu dengan alasan yang tidak sah.

6. Masih Ada Peran Spesialis

Walaupun banyak orang bisa belajar dasar-dasar dan keterampilan cybersecurity, akan selalu ada spesialis di bidang ini yang lebih mendalam dan terfokus pada aspek-aspek tertentu dari keamanan dunia maya, seperti forensik digital, keamanan aplikasi, atau analisis ancaman.

Tim cybersecurity yang lebih besar dan beragam diperlukan untuk menangani ancaman yang sangat canggih dan beragam.

---

## 📋 STUDI KASUS: CYBER ATTACKS FATAL DI INDUSTRI NYATA (2022-2025)

Untuk memberikan gambaran **nyata dan konkret** bagaimana cyber security bukan hanya teori tetapi ancaman yang sangat **real, fatal, dan expensive**, berikut adalah 5 studi kasus perusahaan/organisasi besar yang terkena cyber attack yang sangat mengguncang dalam 3 tahun terakhir:

---

### **Studi Kasus 1: MGM Resorts International (September 2023) - Ransomware Attack**

**Organisasi:** MGM Resorts (Las Vegas - Salah satu kasino & hotel terbesar dunia)

**Tipe Serangan:** Ransomware Attack via Social Engineering + Data Breach

**Dampak:**
- ❌ **Sistem Down**: 60+ hotel & kasino di seluruh dunia tidak bisa operate
- ❌ **Keuangan**: Kehilangan ~$100 juta+ per hari (3 minggu downtime)
- ❌ **Operasional**: Guest tidak bisa check-in, ATM tidak bisa diakses, semua transaksi manual
- ❌ **Reputasi**: Jutaan guest kecewa, booking cancel, trust merosot
- ❌ **Ransom**: Attacker minta $15 juta (tidak dibayar)

**Kronologi Attack:**
```
Phase 1 (3 bulan SEBELUM serangan):
→ Attacker identifikasi MGM employee via LinkedIn
→ Social engineer: Contact employee via call, pretend jadi IT support
→ Tricke employee untuk share credential (password reset verification)

Phase 2 (Initial Access):
→ Attacker login dengan credential employee via VPN
→ Explore network secara perlahan tanpa terdeteksi
→ Mapping sistem, identifikasi sistem kritis

Phase 3 (Lateral Movement & Privilege Escalation):
→ Escalate privilege dari user → admin/system
→ Install backdoor untuk persistence jika ketahuan
→ Disable security monitoring tools

Phase 4 (Eksploitasi & Ransomware Deployment):
→ Encrypt semua file kritis & database sekaligus
→ Ransom note: "Bayar $15M atau data dijual/dihapus/destroyed"

Phase 5 (Impact):
→ SEMUA SISTEM DOWN - tidak bisa book hotel
→ TIDAK BISA PROCESS transaksi apapun
→ Manual operations everywhere = chaos
→ Tidak ada automation, semuanya stall
```

**Penyebab Root:**
- 🔴 **Weak Credential Management** - Password reused/shared
- 🔴 **Poor Employee Training** - Vulnerable to social engineering
- 🔴 **No MFA (Multi-Factor Authentication)** - Attacker tidak perlu token, hanya password
- 🔴 **No Network Segmentation** - Attacker bisa lateral move freely
- 🔴 **Delayed Detection** - Attacker di network 3 bulan, baru terdeteksi saat ransomware deployed

**Pembelajaran Kunci:**
```
✓ SOCIAL ENGINEERING ADALAH ENTRY POINT #1
  → Human adalah weakest link, bukan sistem
  → $100M+ loss bukan karena unpatched software, tapi karena employee tertipu

✓ MFA BISA PREVENT INI
  → Bahkan dengan credential yang dicuri, MFA block attacker
  → Lesson: Deploy MFA everywhere, terutama untuk admin/VPN access

✓ NETWORK SEGMENTATION PENTING
  → Jika database server isolated, attacker tidak bisa encrypt semuanya
  → Limit lateral movement = limit damage

✓ MONITORING & DETECTION CRITICAL
  → 3 bulan undetected = attacker bisa setup semuanya
  → Need 24/7 monitoring, anomaly detection, behavioral analytics
```

**Referensi Official:**
- https://www.reuters.com/technology/mgm-resorts-confirms-cyberattack-2023-09-11/
- https://www.bbc.com/news/technology-66747014
- https://www.securityweek.com/mgm-resorts-hit-by-alphv-ransomware-attack/
- https://krebsonsecurity.com/2023/09/mgm-resorts-hit-by-alphv-ransomware-gang/

---

### **Studi Kasus 2: Caesars Entertainment (June 2023) - Ransomware + Data Breach**

**Organisasi:** Caesars Entertainment (Kasino & hotel chain, salah satu terbesar di dunia)

**Tipe Serangan:** Ransomware Attack + Customer Data Breach (Unpatched Vulnerability)

**Dampak:**
- ❌ **Data Stolen**: 50,000+ customer credit cards & personal information
- ❌ **Ransom**: Attacker minta $30 juta → Caesars bayar $15 juta
- ❌ **Operational**: Sistem reservation & payment terganggu berhari-hari
- ❌ **Legal**: GDPR investigation, PCI-DSS fines, class action lawsuits
- ❌ **Trust**: Customer percaya berkurang, loyalty program ditinggalkan

**Cara Masuk:**
```
Attacker exploit:
1. CITRIX vulnerability (sudah diketahui, tapi belum dipatch)
   → Citrix adalah remote access sistem, attacker bisa masuk dari internet
   → Known vulnerability yang bisa discan & exploited
   → Patch sudah available, tapi Caesars belum apply

2. Weak VPN Credential
   → Setelah exploit Citrix, cari user credentials
   → Default passwords / weak passwords
   → No MFA protection

3. No Active Monitoring
   → Breach terjadi, tapi tidak terdeteksi berbulan-bulan
   → Ransomware deployed tanpa alert

Timeline:
- March 2023: Initial breach via unpatched Citrix
- June 2023: Ransomware deployed & data exfiltrated sekaligus
- June 2023: Ransom demand $30 juta
- July 2023: Settlement $15 juta (+ insurance cover paling gede)
- Ongoing: Regulatory investigations, lawsuits
```

**Penyebab Root:**
- 🔴 **Unpatched Vulnerability** - Citrix bug known, patch available, tapi tidak diapply
- 🔴 **Weak Access Control** - VPN credential reused/shared
- 🔴 **No Network Monitoring** - Breach terjadi berbulan-bulan tidak terdeteksi
- 🔴 **Insufficient Backup** - Data tidak bisa di-recover dari clean backup, jadi perlu decrypt

**Pembelajaran Kunci:**
```
✓ PATCH MANAGEMENT ADALAH PRIORITAS
  → Unpatched systems = low-hanging fruit untuk attacker
  → CIS Control #2: Inventory & Control of Software Assets
  → CIS Control #3: Continuous Vulnerability Management

✓ DATA EXFILTRATION DETECTION PENTING
  → Monitor unusual data movement (large file transfers, bulk exports)
  → Data leakage prevention (DLP) tools dapat detect ini

✓ RANSOMWARE INSURANCE HELPFUL TAPI BUKAN SOLUSI
  → Insurance cover sebagian loss, tapi tidak cover semua
  → Preventive security lebih baik & lebih murah daripada insurance claim

✓ CREDIT CARD DATA = COMPLIANCE NIGHTMARE
  → PCI-DSS compliance mandatory
  → Breach = investigation, audit, fines, lawsuits
  → Customer notification requirements, potential identity theft
```

**Referensi Official:**
- https://www.reuters.com/technology/caesars-entertainment-confirms-ransomware-attack-2023-06-16/
- https://www.bleepingcomputer.com/news/security/caesars-entertainment-confirms-ransomware-attack-ransom-demand/
- https://krebsonsecurity.com/2023/06/caesars-entertainment-hit-with-ransom-demand/
- https://www.securityweek.com/caesars-ransom-attack-what-we-know-so-far/

---

### **Studi Kasus 3: Okta - Identity & Access Management Breach (January 2023)**

**Organisasi:** Okta (Penyedia Identity Management untuk ribuan perusahaan global)

**Tipe Serangan:** Supply Chain Attack + Zero-Day Vulnerability

**Dampak Massive:**
- ❌ **Scale HUGE**: Okta provide authentication untuk ribuan perusahaan
  - Jika Okta compromise, SEMUA customer potentially affected
  - Estimated 10,000+ organizations depend on Okta
  - Cascade effect: 1 vendor breach = 1000s of customer breaches

- ❌ **Data Breached**: Customer identity data, API tokens, session cookies
- ❌ **Privilege Access Granted**: Attacker bisa access customer accounts melalui Okta platform
- ❌ **Regulatory Nightmare**: Massive compliance breach, investigations, penalties
- ❌ **Trust Crisis**: Okta adalah "TRUSTED IDENTITY PROVIDER"
  - Breach shakes confidence di seluruh customer base
  - Competitors capitalize, customers consider switching

**Cara Masuk:**
```
Attacker exploit:
1. ZERO-DAY vulnerability di Okta support system
   → Previously unknown bug, tidak ada patch
   → Sulit untuk di-prevent karena tidak diketahui exploit-nya

2. No detection system menangkap anomali
   → Attacker bertindak sekecil mungkin untuk avoid detection
   → Support system tidak closely monitored

3. Extended dwell time (lama undetected)
   → Attacker bisa explore system perlahan
   → Setup backdoor, establish persistence

4. Lateral movement ke customer data
   → Dari support system → production environment
   → Access customer identity information
```

**Timeline:**
```
- September 2022: Breach terjadi (unknown saat itu)
- January 2023: Breach formally discovered
- Investigation: Attacker dalam system sejak September 2022 (4 BULAN UNDETECTED!)
- Data: Customer identity information, support case data, potentially more
- Attacker: Group called "LAPSUS$" (known untuk supply chain attacks)

Catatan penting: 4 bulan adalah LONG TIME
→ Attacker bisa:
  - Thoroughly explore infrastructure
  - Steal data gradually tanpa alert
  - Setup multiple backdoors
  - Escalate privilege
  - Access banyak customer data
```

**Penyebab Root:**
- 🔴 **Zero-Day Vulnerability** - Unknown bug, tidak bisa di-predict atau di-patch sebelumnya
- 🔴 **Insufficient Logging & Monitoring** - 4 bulan tidak terdeteksi
- 🔴 **Access Control Not Tight** - Attacker bisa lateral move ke banyak tempat
- 🔴 **Incident Response Delay** - Terlambat detect & respond

**Pembelajaran Kunci:**
```
✓ SUPPLY CHAIN ATTACKS SANGAT DANGEROUS
  → 1 vendor compromise = 1000s of customers affected (cascade)
  → Need vendor security requirements in contracts
  → Continuous vendor security monitoring necessary

✓ ZERO-DAY CANNOT BE PREVENTED, TAPI CAN BE DETECTED
  → Preventive measures alone tidak cukup
  → Need detection-focused strategies: behavioral analysis, anomaly detection
  → Look for suspicious patterns: unusual data access, lateral movement, etc.

✓ CONTINUOUS MONITORING & LOGGING CRITICAL
  → Semakin cepat detect, semakin limit damage
  → 4 bulan undetected vs 1 hari undetected = massive difference in impact
  → SIEM (Security Information Event Management) tools help correlate events

✓ IDENTITY & ACCESS MANAGEMENT = CROWN JEWEL
  → If IAM compromised, everything downstream compromised
  → Protect dengan highest priority: MFA, encryption, monitoring

✓ VENDOR SECURITY = YOUR SECURITY
  → Vet vendors before using
  - Ask about security practices, certifications (SOC 2, ISO 27001, etc.)
  - Contractual security requirements
  - Regular security assessments
  - Incident notification requirements
```

**Referensi Official:**
- https://www.reuters.com/technology/okta-says-customer-data-compromised-january-cyberattack-2023-02-02/
- https://www.securityweek.com/okta-breach-details-what-we-know/
- https://blog.okta.com/okta-security-incident/ (official Okta security blog)
- https://www.bleepingcomputer.com/news/security/okta-says-attacker-accessed-customer-data-in-january-breach/

---

### **Studi Kasus 4: MOVEit - Zero-Day Exploitation (May 2023)**

**Organisasi:** Moveit (Managed file transfer software, digunakan oleh Fortune 500 companies worldwide)

**Tipe Serangan:** Zero-Day Vulnerability Exploitation + Mass Compromise (48-hour window)

**Dampak Massive:**
- ❌ **Scale UNPRECEDENTED**: 2,000+ organizations affected globally within 48 hours
- ❌ **Data**: Millions of records stolen (healthcare, finance, government data)
- ❌ **Duration**: Vulnerability unknown & exploited SEBELUM patch available
- ❌ **Industries Affected**: 
  - Hospitals & healthcare providers (patient data at risk)
  - Banks & financial institutions (financial data)
  - Government agencies (national security data)
  - Airlines & travel companies (traveler information)
  - Fortune 500 companies (trade secrets, business data)

**Contoh Organisasi Terkena:**
- US Department of Energy
- US Department of Labor
- US Treasury Department
- Multiple hospital chains & healthcare providers
- Airlines (Southwest, others)
- Financial institutions

**Cronology:**
```
Timeline (EXTREMELY FAST):
- May 27, 2023: Vulnerability discovered (ZERO-DAY)
- May 28, 2023: Patch released by Moveit team (48 jam kemudian)
- Between May 27-28: Attacker actively exploit sebelum patch available
- Result: 2,000+ organizations breached dalam 48-hour window

Mengapa 48 jam FATAL?
→ Software sudah deployed di ribuan system worldwide
→ Tidak semua organization patching immediately
→ Takes days/weeks untuk patch deployment (testing, rollout)
→ During 48-hour gap, attacker bisa exploit di 2,000+ systems

Pattern:
- Day 1: Vulnerability announced (0-24 hours)
- Day 1-2: Attacker scanning & exploiting unpatched systems
- Day 2: Patch released (too late, thousands already breached)
- Days 3+: Organizations patching (but data already stolen)
```

**Cara Masuk:**
```
Attack chain:
1. Zero-day vulnerability di MOVEit file transfer mechanism
   → Known file upload/download handling flaw
   → Attacker dapat bypass authentication

2. Exploit selama 48-hour window (before patch)
   → Exploit code dirilis/discovered
   → Attacker scan & compromise unpatched instances

3. Data extraction
   → MOVEit berisi transfer history, files, credentials
   → Attacker bisa extract & steal data

4. Impact
   → Organizations realize mereka compromised AFTER patch
   → Data already stolen & exfiltrated
```

**Penyebab Root:**
- 🔴 **Zero-Day Vulnerability** - Previously unknown, tidak bisa dicegah sebelumnya
- 🔴 **Time-to-Patch Gap** - 48 jam antara discovery & patch terlalu lama untuk mass deployment
- 🔴 **Delayed Patching by Customers** - Takes weeks/months untuk deploy critical patch (testing cycle)
- 🔴 **No Intrusion Detection** - Tidak ada alert sistem sampai terlambat

**Pembelajaran Kunci:**
```
✓ ZERO-DAY ADALAH REALITY, BUKAN IF-THEN-WHEN
  → Unknown vulnerabilities exist everywhere
  → Cannot be prevented (by definition, unknown)
  → Must prepare for zero-day exploitation

✓ PATCH MANAGEMENT PROCESS HARUS AGILE
  → Critical patches harus di-deploy dalam jam/hari, bukan minggu/bulan
  → Test & validate quickly
  → Emergency patching procedures untuk zero-day scenarios
  → CIS Control #3: Continuous Vulnerability Management (prioritize critical)

✓ INTRUSION DETECTION DAPAT MENDETEKSI EXPLOITATION
  → Even jika zero-day, attack pattern bisa suspicious
  → Anomaly detection: unusual file access/transfer patterns
  → Behavioral analysis: compare dengan normal baseline
  → IDS/IPS systems dapat alert pada suspicious activity

✓ FILE TRANSFER SYSTEMS = HIGH-VALUE TARGET
  → Usually berisi sensitive/valuable data
  → Critical untuk business operations
  → More likely untuk di-target oleh attackers

✓ INCIDENT RESPONSE PLAYBOOK ESSENTIAL
  → Pre-planned response untuk breach scenario
  → Know what to do, who to notify, when to escalate
  → Faster response = limit damage & data exfiltration
```

**Referensi Official:**
- https://www.cisa.gov/news-events/alerts/2023/05/31/cisa-adds-one-known-exploited-vulnerability-catalog (US government alert)
- https://www.bleepingcomputer.com/news/security/moveit-transfer-zero-day-exploited-in-mass-breaches/
- https://www.reuters.com/technology/moveit-hack-exposes-sensitive-us-data-2023-06-01/
- https://www.securityweek.com/moveit-zero-day-exploited-mass-compromise/

---

### **Studi Kasus 5: LastPass - Credential Vault Breach (December 2022)**

**Organisasi:** LastPass (Password manager dengan 30 juta users worldwide)

**Tipe Serangan:** Supply Chain + Insider Compromise + Multi-Stage Sophisticated Attack

**Dampak CRITICAL:**
- ❌ **Trust Crisis**: LastPass supposed to PROTECT passwords
  - Paradoxically: credential manager yang protect credentials COMPROMISED
  - Irony: 30 juta users yang trust LastPass sekarang worried tentang semua credentials

- ❌ **Credential Exposure**: 
  - Customer master passwords (hopefully hashed & protected)
  - Encrypted vaults (if encryption strong, harder to break)
  - API keys, SSH keys, database credentials stored in vaults

- ❌ **Downstream Impact**: 
  - If customers reuse passwords across sites, other accounts at risk
  - API keys dapat used untuk breach customer systems
  - SSH keys dapat used untuk unauthorized access ke servers

- ❌ **Sensitive Data**: LastPass vaults store bukan hanya passwords:
  - API credentials untuk cloud services
  - Database passwords untuk production systems
  - SSH keys untuk server access
  - Credit card & financial information
  - Personal notes & sensitive information

- ❌ **Attribution**: Attack traced to Russian-speaking threat actor
  - Geopolitical implications
  - Likely advanced, well-resourced attacker

**Cara Masuk (Multi-Stage):**
```
Stage 1: Initial breach (August 2022)
→ Attacker identify LastPass developer via job posting/LinkedIn
→ Social engineer developer dengan job offer / phishing
→ Trick developer untuk click link, download trojan
→ Steal developer credential dari developer machine
→ Alternative: Credential stuffing attack (reused password from another breach)

Stage 2: Internal reconnaissance (November 2022)
→ Attacker login sebagai developer
→ Explore LastPass internal systems
→ Access source code repository (GitHub, internal SCM)
→ Access production data/database
→ Find API keys untuk cloud infrastructure (AWS, Google Cloud)

Stage 3: Data exfiltration & public disclosure (December 2022)
→ Customer vault data exfiltrated
→ Some encrypted (harder to use), some not
→ LastPass publicly disclosed breach
→ Attacker release data publicly atau sell darknet

Timeline: Sophisticated, multi-month attack
→ Takes time to infiltrate, explore, escalate, exfiltrate
→ Not opportunistic one-day exploit
→ Planned, targeted, well-resourced attack
```

**Penyebab Root:**
- 🔴 **Weak Credential Management** - Developer credential compromised
- 🔴 **No MFA on Developer Accounts** - Or not enforced everywhere
- 🔴 **Insufficient Internal Network Segmentation** - Developer bisa access production
- 🔴 **Delayed Detection** - Breach terjadi berbulan-bulan sebelum discovery
- 🔴 **Insider Threat Not Fully Mitigated** - Or social engineering worked too well

**Pembelajaran Kunci:**
```
✓ PASSWORD MANAGER BREACH = WORST CASE SCENARIO
  → If master password compromised, SEMUA secrets compromised
  → 30 juta users potentially affected
  → Cascading impact: customer APIs, databases, other systems
  → Choose password manager dengan strong reputation & security track record

✓ DEVELOPER ACCESS = HIGHEST VALUE TARGET
  → Developers usually have admin/production access
  → Source code access
  → API keys untuk infrastructure
  → Database credentials
  → Why attackers specifically target developers

✓ SUPPLY CHAIN ATTACKS BISA MULTI-STAGE & VERY SOPHISTICATED
  → Not always "smash & grab"
  → Can be months of infiltration, exploration, escalation
  → Plan untuk long-term compromise

✓ EVEN SECURITY-FIRST COMPANIES NOT IMMUNE
  → LastPass adalah security-focused company
  → Yet still compromised
  → Lesson: no system 100% secure, prepare untuk worst case

✓ DEFENSE-IN-DEPTH CRITICAL
  → Multiple security layers so breach at 1 layer ≠ total compromise
  → If attacker bypass developer authentication, MFA would block
  → If no MFA, internal network segmentation would limit access
  → If no segmentation, detection system would alert
  → Multiple layers mean harder to fully compromise

✓ TRANSPARENCY & INCIDENT COMMUNICATION MATTER
  → How LastPass handled disclosure was criticized
  → Poor communication erodes customer trust further
  → Lessons learned: communicate clearly & quickly
```

**Referensi Official:**
- https://www.reuters.com/technology/lastpass-parent-company-warns-of-december-cyber-incident-2022-12-22/
- https://krebsonsecurity.com/2023/01/lastpass-suffered-a-breach-security-holes-remain-unpatched-since-2018/
- https://www.bleepingcomputer.com/news/security/lastpass-says-accounts-and-vaults-encrypted-in-breach/
- https://www.securityweek.com/lastpass-breach-deep-dive/

---

## 🔍 ANALISIS PERBANDINGAN KASUS-KASUS

Perhatikan pola & kesamaan di antara 5 studi kasus:

| Kasus | Tipe Attack | Entry Point | Impact | Duration |
|-------|-------------|------------|--------|----------|
| MGM | Ransomware (Human) | Social Engineering + weak credentials | $100M+/day + ransom | 3 minggu downtime |
| Caesars | Ransomware + Data Breach | Unpatched Citrix | $15M+ ransom | Ransom + regulatory |
| Okta | Supply Chain Zero-day | Zero-day vulnerability | 10,000+ orgs at risk | 4 months undetected (massive!) |
| MOVEit | Zero-day Exploitation | Zero-day vulnerability (48hr window) | 2,000+ orgs affected | 48 hours (1-2 day window) |
| LastPass | Multi-stage Supply Chain | Weak credentials + Insider/Social Engineering | 30M users at risk | Months undetected (sophisticated) |

**Pola Umum yang Terlihat:**

**1. Social Engineering / Weak Credential = #1 Entry Point**
```
MGM: Masuk via social engineering (employee tertipu)
LastPass: Masuk via weak/reused developer credential
Caesars: Weak VPN credential (supporting factor)

Lesson: Human adalah weakest link, training penting
→ Even dengan teknologi terbaik, social engineering works
→ Security awareness training bukan optional, REQUIRED
```

**2. Unpatched Systems = Fatal Vulnerability**
```
Caesars: Unpatched Citrix (3-month window)
MOVEit: Unpatched zero-day (48-hour window)

Lesson: Patch management critical & urgent
→ CIS Control #3: Continuous Vulnerability Management
→ Prioritize critical patches: deploy dalam jam/hari
→ Auto-patching untuk non-critical updates
```

**3. Extended Dwell Time = Worse Damage**
```
Okta: 4 months undetected (massively worse)
LastPass: Months undetected
MGM: 3 months before ransomware deployment
MOVEit: 48 hours (fastest, but still time to damage)

Lesson: Early detection dapat drastically limit damage
→ 4 months undetected = attacker setup everything, exfiltrate everything
→ 1 day undetected = minimal damage
→ Need 24/7 monitoring, SIEM, anomaly detection
```

**4. Zero-Day Impossible to Prevent, But Detectable**
```
MOVEit: Zero-day exploitation (cannot prevent unknown vuln)
Okta: Zero-day exploitation (cannot prevent)

TAPI: Tidak berarti undectable
→ Behavioral analysis: suspicious data access patterns
→ Anomaly detection: unusual network traffic
→ IDS/IPS: signature-based detection setelah exploitation known
→ Response: once detected, can be stopped & contained

Lesson: Shift perspective dari prevention-only → detection & response
```

**5. Supply Chain Impact is Catastrophic**
```
Okta: 10,000+ organizations affected (1 vendor breach = mass impact)
MOVEit: 2,000+ organizations affected (48-hour mass compromise)
LastPass: 30M users affected (massive downstream impact)

Lesson: Vendor security = your security
→ Vet third-party providers: ask tentang security practices
→ Include security requirements dalam contracts
→ Monitor vendors continuously
→ Have incident response plan untuk vendor breach scenario
```

---

## 💡 KEY TAKEAWAYS DARI STUDI KASUS

Berdasarkan 5 studi kasus nyata di atas, berikut adalah insight yang paling penting untuk dipahami oleh setiap mahasiswa cybersecurity:

## 💡 KEY TAKEAWAYS DARI STUDI KASUS

Berdasarkan 5 studi kasus nyata, berikut adalah insight yang paling penting:

**1. TIDAK ADA ORGANISASI YANG KEBAL**
- Baik Fortune 500, government agencies, atau security-focused companies SEMUA bisa terkena
- Size, resources, brand reputation BUKAN guarantee
- Sebesar apapun, yang penting adalah ada vulnerability

**2. FINANCIAL IMPACT ADALAH MASSIVE**
- MGM Resorts: $100M+ per hari downtime (3 minggu)
- Caesars: $15M ransom + investigation costs
- MOVEit: Investigation costs, legal fees, reputation
- LastPass: Ongoing security incident costs, trust loss
- Money di-spend untuk remediation, investigation, lawsuits, compliance, insurance

**3. HUMAN STILL THE WEAKEST LINK**
- Social engineering works (MGM, LastPass)
- Weak credentials common (Caesars, LastPass)
- Employee training = critical defense layer
- Technology alone tidak cukup

**4. DETECTION & RESPONSE CRITICAL**
- Early detection dapat drastically limit damage
- 1 day undetected ≠ 4 months undetected
- Incident response playbook saves money & time
- 24/7 monitoring necessary untuk critical systems
- SIEM, anomaly detection, behavioral analysis tools

**5. VENDOR SECURITY = YOUR SECURITY**
- 1 vendor breach = 1000s of customer breaches
- Okta breach affected 10,000+ orgs
- MOVEit breach affected 2,000+ orgs
- Vet & monitor third-party providers
- Include security requirements dalam contracts

**6. COMPLIANCE & LEGAL CONSEQUENCES SEVERE**
- GDPR fines: up to 4% of annual revenue (massive)
- HIPAA fines untuk healthcare breach
- PCI-DSS compliance untuk credit card data
- Class action lawsuits from customers
- Regulatory investigations & penalties
- Reputational damage lasting years

**7. ZERO-DAY CANNOT BE PREVENTED, TAPI DAPAT DIPERSIAPKAN**
- Unknown vulnerabilities akan selalu ada
- Focus pada detection, containment, recovery
- Disaster recovery plan essential
- Backup systems & redundancy critical
- Insurance dapat membantu (tapi expensive)
- Shift dari "prevent all" → "detect early, respond fast"

**Kesimpulan:** Cyber security bukan pilihan, tapi **necessity**. Organisasi apapun, seberapa besarpun, bisa terkena attack yang sangat fatal & expensive. Oleh karena itu, **understanding & prevention adalah critical skills** yang harus dipelajari setiap IT professional.

#### **Apa itu Cyber Security Framework?**

**Definisi Sederhana:**
Cyber Security Framework adalah seperti **"arah peta & kompas"** bagi seorang cybersecurity professional. Framework memberikan:
- **Struktur** = Bagaimana cara mengorganisir keamanan
- **Pedoman** = Apa yang harus dilakukan dan kapan
- **Best practices** = Cara terbaik yang sudah terbukti berhasil
- **Standar** = Acuan minimum untuk compliance & regulasi

**Analogi yang Tepat:**
```
Ibaratnya cybersecurity professional seperti pilot pesawat:
- Framework adalah "flight manual" yang menjelaskan semua prosedur
- Threat adalah "cuaca buruk" yang bisa membahayakan
- Controls adalah "instrument & sistem keselamatan" di pesawat

Tanpa framework:
❌ Pilot terbang dengan improvisasi, tidak punya checklist
❌ Tidak tahu prosedur emergency, action plan chaos
❌ Tidak bisa communicate dengan team, operasi berantakan
❌ Jika terjadi incident, tidak tahu apa yang harus dilakukan

Dengan framework:
✅ Pilot punya pre-flight checklist yang jelas
✅ Tahu prosedur exact untuk setiap situasi
✅ Bisa communicate dengan tower & team dengan bahasa yang sama
✅ Jika terjadi masalah, ada playbook yang siap pakai
✅ Operasi berjalan systematically & safely
```

**Mengapa Framework Penting?**

| Aspek | Tanpa Framework | Dengan Framework |
|-------|-----------------|------------------|
| **Consistency** | Setiap team berbeda-beda | Semua team mengikuti standard |
| **Efficiency** | Coba-coba, buang waktu | Langkah-langkah sudah proven |
| **Compliance** | Tidak jelas apa requirement | Jelas apa yang harus dipenuhi |
| **Communication** | Miscommunication antar team | Bahasa & terminology sama |
| **Scalability** | Susah grow, chaos bertambah | Mudah scale dengan consistent process |
| **Benchmarking** | Tidak tahu performance kita | Bisa compare dengan industry standard |
| **Risk Management** | Ad-hoc, tidak terstruktur | Systematic risk assessment & mitigation |

---

#### **4 FRAMEWORK UTAMA CYBER SECURITY**

---

### **1️⃣ NIST Cybersecurity Framework (US)**

**Asal Usul:**
- Dikembangkan oleh **NIST (National Institute of Standards & Technology)** - badan US
- Dipublikasikan tahun 2014, updated 2022
- Awalnya untuk critical infrastructure protection
- Sekarang digunakan globally di berbagai industri

**Struktur NIST CSF (5 Core Functions):**

1. **IDENTIFY**
   - Understand assets & environment
   - Identify risks & threats
   - Baseline security posture

2. **PROTECT**
   - Access control (who can access what)
   - Encryption (protect data)
   - Training (awareness program)
   - Infrastructure security (firewall, etc)

3. **DETECT**
   - Monitoring & logging (24/7 watch)
   - Anomaly detection (unusual activity)
   - Security testing (vulnerability scan)
   - Threat intelligence (know enemy)

4. **RESPOND**
   - Incident response plan (action playbook)
   - Communication (notify stakeholders)
   - Containment (stop spread of attack)
   - Recovery (restore systems to normal)

5. **RECOVER**
   - Restore systems & data
   - Lessons learned (improve future)
   - Business continuity (minimize downtime)
   - Resilience (stronger untuk next attack)

**Contoh Implementasi NIST CSF - Hospital Health System:**

```
IDENTIFY:
→ Mapping: Database pasien, sistem medical device, server pharmacy
→ Risk: Medical data breach bisa fatal (patient health risk)
→ Baseline: Current security maturity level

PROTECT:
→ Encryption: Encrypt patient data di database & transit
→ Access Control: Hanya doctor/nurse authorized bisa access patient records
→ Training: Staff training tentang HIPAA compliance
→ Network Security: Firewall antara patient system & public internet

DETECT:
→ SIEM: Monitor semua login & data access attempts
→ Alert: Anomaly jika ada unusual bulk download of patient data
→ Scanning: Regular vulnerability scan di sistem medis

RESPOND:
→ Incident: Jika ada suspicious activity, immediate isolation
→ Communication: Notify hospital management & regulatory body
→ Containment: Shutdown compromised system untuk prevent spread

RECOVER:
→ Restore: Restore patient data dari clean backup
→ Investigation: Forensik untuk determine root cause
→ Improvement: Implement additional controls berdasarkan incident
```

**Kapan Gunakan NIST CSF?**
- ✅ Critical infrastructure (healthcare, power grid, banking)
- ✅ Organizations yang perlu lifecycle approach
- ✅ Need structured risk management
- ✅ US government contracts (often requirement)

---

### **2️⃣ ISO/IEC 27001 (International)**

**Asal Usul:**
- Dikembangkan oleh **ISO (International Organization for Standardization)**
- Standard internasional untuk Information Security Management Systems (ISMS)
- Dapat di-certify (audit & tercapai ISO certification)
- Digunakan di 170+ negara

**Struktur ISO 27001 (14 Sections - Plan, Do, Check, Act):**

**CONTEXT & LEADERSHIP (Planning Phase)**
- Section 4: Understanding the organization
- Section 5: Leadership commitment
- Section 6: Planning untuk ISMS

**SUPPORT (Enablement Phase)**
- Section 7: Resources (people, budget, tools)
- Section 8: Competence (training & capability)

**OPERATION (Doing Phase)**
- Section 9: Operational planning & control
- Section 10: Information security controls
  - A.5: Organizational controls
  - A.6: People controls (HR security)
  - A.7: Physical controls (building, datacenter)
  - A.8: Tech controls (crypto, access, logging)
  - A.14: System acquisition & development

**PERFORMANCE EVALUATION (Checking Phase)**
- Section 11: Performance evaluation (metrics)
- Section 12: Internal audit (compliance check)
- Section 13: Management review (quarterly/yearly)

**IMPROVEMENT (Acting Phase)**
- Section 14: Corrective action (fix non-compliance)
- Continuous improvement cycle

**14 Categories ISO 27001 Controls:**

| Category | Fokus | Contoh Control |
|----------|-------|-----------------|
| **5. Organizational** | Policies & governance | Information security policy, responsibility |
| **6. People** | HR & staff security | Background check, termination procedure |
| **7. Physical** | Building & facility | Secure datacenter, visitor management |
| **8. Technology** | Tech infrastructure | Firewall, encryption, access control |
| **9. Cryptography** | Encryption standards | Algorithm strength, key management |
| **10. Physical/Tech** | Backup & recovery | Regular backup, disaster recovery plan |
| **11. Comms Security** | Network security | Network segregation, VPN, secure protocols |
| **12. Systems Acq** | Software development | Secure coding, vulnerability testing |
| **13. Supplier Mgmt** | Third-party risk | Vendor assessment, SLA requirements |
| **14. Information** | Data classification | Data handling, retention, disposal |
| **15. Relationships** | Compliance tracking | Incident reporting, audit log retention |
| **16. Incident Mgmt** | Response procedures | Incident response, forensics, communication |

**Contoh Implementasi ISO 27001 - E-Commerce Company:**

```
SECTION 7 (PEOPLE CONTROLS):
→ Hire policy: Background check untuk semua IT staff
→ Training: Mandatory security awareness training/year
→ Termination: Revoke access immediately saat employee resign

SECTION 8 (TECHNICAL CONTROLS):
→ Access Control: Role-based access (normal user ≠ admin)
→ Encryption: HTTPS untuk website, AES-256 untuk database
→ Logging: Audit log semua login & data access
→ Firewall: WAF (Web Application Firewall) untuk website

SECTION 10 (PHYSICAL CONTROLS):
→ Datacenter: Access card controlled, CCTV monitoring
→ Visitor: Visitor log, escorted jika masuk server room
→ Clean desk: Confidential documents must be locked/destroyed

SECTION 11 (INCIDENT MANAGEMENT):
→ Response: 24/7 incident response team on-call
→ Communication: Notify affected customers within 72 hours (GDPR)
→ Investigation: Forensic analysis untuk determine root cause

ANNUAL AUDIT:
→ External auditor check compliance terhadap 127 controls
→ If compliant → ISO 27001 certification (valid 3 years)
→ Certification = proof untuk customers bahwa security serius
```

**Kapan Gunakan ISO 27001?**
- ✅ Need international recognition & certification
- ✅ Regulated industries (finance, healthcare, data processing)
- ✅ B2B companies (customers trust certification)
- ✅ Global operations (same standard di semua negara)

---

### **3️⃣ CIS Controls (Center for Internet Security)**

**Asal Usul:**
- Dikembangkan oleh **Center for Internet Security** - non-profit organization
- Focus: "Most effective defensive actions" against real attacks
- Updated regularly based on attack data
- Version 8 (2021) memiliki 18 controls + sub-controls

**Struktur CIS Controls (18 Critical Controls):**

**ASSET MANAGEMENT (What do you have?)**
- 1. Inventory of Enterprise Assets
- 2. Inventory of Software Assets

**ACCESS CONTROL (Who can access what?)**
- 3. Data Protection & Privacy
- 4. Secure Configuration Management
- 5. Account Management
- 6. Access Control Management
- 7. Security Awareness & Skills Training
- 8. Audit Log Management

**DEFENSE (Prevent attacks)**
- 9. Email & Web Browser Protections
- 10. Malware Defense
- 11. Data Recovery (Backup & Restore)
- 12. Network Infrastructure Management
- 13. Network Monitoring & Defense
- 14. Security Awareness Program

**DETECTION (Find attacks early)**
- 15. Service Provider Management
- 16. Application Software Security
- 17. Incident Response Management
- 18. Penetration Testing

**Tingkatan Implementasi:**

```
IMPLEMENTATION GROUPS:

IG1 (Small Business):
- Budget terbatas, staff minimal
- Focus: Basic protection (antivirus, firewall, passwords)
- Effort: Low
- Benefit: Cover 70% of common attacks

IG2 (Medium Business):
- Dedicated security team, moderate budget
- Focus: Advanced controls (monitoring, access control, incident response)
- Effort: Medium
- Benefit: Cover 90% of sophisticated attacks

IG3 (Large Enterprise):
- Large security team, substantial budget
- Focus: Advanced detection, threat hunting, zero-trust
- Effort: High
- Benefit: Cover 99% of advanced threats
```

**Contoh Implementasi CIS Controls - Manufacturing Company:**

```
CONTROL 1 (Asset Inventory):
→ Scan: Automated asset discovery tool scan network
→ List: Database of semua servers, PCs, printers, IoT devices
→ Tracking: Update real-time saat ada device baru/removed

CONTROL 3 (Data Protection):
→ Identify: Data classification (public, internal, confidential, restricted)
→ Encrypt: Confidential data encrypted both at-rest & in-transit
→ Access: Only authorized personnel dapat access restricted data

CONTROL 6 (Access Control):
→ Principle: Least privilege (give minimum access needed)
→ Admin accounts: Separate admin account untuk elevated access
→ Review: Quarterly review of who has access to what

CONTROL 10 (Malware Defense):
→ Antivirus: Deploy antivirus di semua endpoints
→ Updates: Auto-update signatures daily
→ Scanning: Weekly full system scan untuk detect malware

CONTROL 13 (Network Monitoring):
→ SIEM: Centralized logging dari firewall & servers
→ Alert: Auto-alert untuk suspicious patterns
→ Response: Security team investigate alerts dalam 1 hour

CONTROL 17 (Incident Response):
→ Plan: Written incident response playbook
→ Team: Designated incident response team
→ Drill: Monthly tabletop exercise untuk practice response
```

**Kapan Gunakan CIS Controls?**
- ✅ Want practical, action-oriented controls
- ✅ Based on real attack data (not theoretical)
- ✅ Limited budget (CIS IG1 for small companies)
- ✅ Quick implementation dengan high impact

---

### **4️⃣ COBIT (ISACA - IT Governance)**

**Asal Usul:**
- Dikembangkan oleh **ISACA (Information Systems Audit & Control Association)**
- Focus: IT governance & risk management
- Comprehensive framework (mencakup security, compliance, performance)
- Used untuk internal audit & compliance

**Struktur COBIT 2019 (Governance & Management):**

**GOVERNANCE (Board/Executive level)**
- Evaluated, Directed, Monitored
- Strategic alignment
- Stakeholder value realization
- Risk optimization
- Resource optimization

**MANAGEMENT (Operational level)**
- Plan, Build, Run, Monitor (PBRM)
- Domain 1: Plan & Organize
- Domain 2: Acquire & Implement
- Domain 3: Deliver & Support
- Domain 4: Monitor & Evaluate
- Domain 5: Information & Communication

**4 Domains of COBIT Management:**

| Domain | Focus | Contoh Activities |
|--------|-------|-------------------|
| **1. Plan & Organize** | Strategic planning | IT strategy, governance structure, risk framework |
| **2. Acquire & Implement** | Technology acquisition | System selection, project management, implementation |
| **3. Deliver & Support** | Operational delivery | Service management, incident management, support |
| **4. Monitor & Evaluate** | Performance tracking | Audit, compliance, performance metrics, review |

**Contoh Implementasi COBIT - Bank:**

```
GOVERNANCE (Board level):
→ Risk Committee: Quarterly review IT risk posture
→ Budget: Allocate security budget based on risk assessment
→ Strategy: Align IT security strategy dengan business goals

MANAGEMENT - Domain 1 (Plan & Organize):
→ IT Policy: Document IT governance policies
→ Risk Framework: Implement ISO 31000 risk management
→ Roles: Define clear CISO, security team roles

MANAGEMENT - Domain 2 (Acquire & Implement):
→ Selection: Evaluate & select security tools
→ Implement: Roll-out systems dengan testing & quality check
→ Training: Staff training untuk new systems

MANAGEMENT - Domain 3 (Deliver & Support):
→ Service: Ensure security operations run 24/7
→ Incident: Respond to incidents within SLA
→ Support: Technical support untuk users

MANAGEMENT - Domain 4 (Monitor & Evaluate):
→ Audit: Internal audit untuk compliance check
→ Metrics: KPI tracking (mean time to detect, response time, etc)
→ Review: Management review quarterly

COMMUNICATION (Cross-domain):
→ Reporting: Risk dashboard untuk executives
→ Notification: Alert untuk security incidents
→ Learning: Lesson learned dari incidents
```

**Kapan Gunakan COBIT?**
- ✅ Large enterprises dengan complex IT operations
- ✅ Internal audit & governance requirements
- ✅ Multiple domains (security, compliance, performance)
- ✅ C-suite / board level governance needs

---

#### **PERBANDINGAN 4 FRAMEWORK**

| Aspek | NIST CSF | ISO 27001 | CIS Controls | COBIT |
|-------|----------|-----------|--------------|-------|
| **Asal** | US (NIST) | Intl (ISO) | Non-profit | ISACA |
| **Focus** | Lifecycle | Mgmt System | Practical | Governance |
| **Structure** | 5 functions | 14 sections | 18 controls | 5 domains |
| **Certification** | No | Yes (audit) | No (guideline) | No |
| **Complexity** | Medium | High | Low-Medium | High |
| **Cost** | Free | Medium | Low (free) | Medium |
| **Update** | Regularly | Every 3 yrs | Regularly | Every 3 yrs |
| **Best for** | Strategy | Compliance | Quick start | Enterprise |
| **Industry** | Critical infra | All | All | All |
| **Implementation** | Months | 6-12 months | Weeks-months | 6-24 months |

**USE CASE 1: Startup**

| Aspek | NIST CSF | ISO 27001 | CIS Controls | COBIT |
|-------|----------|-----------|--------------|-------|
| **Recommend** | ✅ CIS IG1 | ❌ Overkill | ✅ CIS IG1 | ❌ Too heavy |
| **Reason** | Low cost, practical | Too complex, expensive | Practical, low cost | Complex, too heavy |

**USE CASE 2: Healthcare**

| Aspek | NIST CSF | ISO 27001 | CIS Controls | COBIT |
|-------|----------|-----------|--------------|-------|
| **Recommend** | ✅ Good | ✅ HIPAA req | ✅ Practical | ✅ Governance |
| **Reason** | Structured | Must comply | For controls | For oversight |

**USE CASE 3: Banking**

| Aspek | NIST CSF | ISO 27001 | CIS Controls | COBIT |
|-------|----------|-----------|--------------|-------|
| **Recommend** | ✅ Good | ✅ Best | ✅ Baseline | ✅ Best |
| **Reason** | Structured | Regulatory requirement | For security | For governance |

**USE CASE 4: Manufacturing**

| Aspek | NIST CSF | ISO 27001 | CIS Controls | COBIT |
|-------|----------|-----------|--------------|-------|
| **Recommend** | ✅ Good | ✅ ISO lead | ✅ Practical | ✅ IT overview |
| **Reason** | Structured approach | ISO culture | Quick win | Governance |

---

#### **PERJALANAN CYBERSECURITY PROFESSIONAL - MENGGUNAKAN FRAMEWORKS**

**Tahap 1: Junior Security Analyst**
```
Framework Usage:
- Belajar: NIST 5 functions (foundation)
- Praktik: CIS Controls (hands-on, practical)
- Focus: Execution level (implement controls)

Task:
✓ Scan vulnerability mengikuti CIS Control #3
✓ Configure firewall sesuai NIST Protect function
✓ Monitor logs per NIST Detect function
```

**Tahap 2: Security Engineer**
```
Framework Usage:
- Deep dive: CIS Controls (all 18)
- Apply: NIST CSF (holistic)
- Reference: ISO 27001 technical controls

Task:
✓ Design security architecture per NIST
✓ Implement monitoring per CIS Control #13
✓ Document controls per ISO 27001 Section 10
```

**Tahap 3: Security Manager**
```
Framework Usage:
- Oversight: NIST + ISO 27001
- Risk Management: COBIT domains
- Strategic: Align frameworks to business

Task:
✓ Manage team against NIST lifecycle
✓ Prepare audit evidence untuk ISO 27001
✓ Report metrics ke executives per COBIT
```

**Tahap 4: Chief Information Security Officer (CISO)**
```
Framework Usage:
- Enterprise: COBIT (governance)
- Compliance: ISO 27001 certification
- Strategy: NIST CSF roadmap
- Metrics: CIS Controls maturity levels

Task:
✓ Present security posture to board per COBIT
✓ Plan ISO 27001 audit
✓ Develop 3-year NIST CSF maturity roadmap
✓ Benchmark against CIS Controls
```

---

#### **APA LAGI YANG PERLU DITAMBAHKAN UNTUK LAYAK DISEBUT CYBERSECURITY PROFESSIONAL?**

Selain mengerti framework, seorang cybersecurity professional perlu memahami:

**1. TECHNICAL SKILLS (Hands-on)**
- Linux/Windows administration
- Networking (TCP/IP, firewall, VPN)
- Application security (OWASP, secure coding)
- Penetration testing (tools, methodology)
- Incident response & forensics

**2. SOFT SKILLS (People & Communication)**
- Risk communication (explain risk to non-technical people)
- Project management (deliver security projects on time)
- Negotiation (balance security vs business needs)
- Leadership (manage security team)
- Presentation (present to C-suite executives)

**3. CERTIFICATIONS (Proof of Expertise)**
- Security+: Foundation security knowledge
- CEH (Certified Ethical Hacker): Penetration testing
- CISSP: Enterprise security architecture
- CISM: Security management & governance
- OSCP: Advanced offensive security

**4. BUSINESS ACUMEN (Strategic Thinking)**
- Understand business goals & how security enables/hinders
- ROI calculation (how much security costs vs benefit)
- Risk appetite (what level of risk business can tolerate)
- Compliance requirements (GDPR, HIPAA, PCI-DSS applicable)
- Industry trends (emerging threats, new technologies)

**5. CONTINUOUS LEARNING (Staying Current)**
- Threat landscape changing rapidly
- New vulnerabilities discovered daily
- Attacks becoming more sophisticated
- Must stay updated with industry news, vendor updates, threat reports
- Recommended: Blogs (Krebs on Security), podcasts, conferences, training

**6. ETHICS & JUDGMENT CALL (Integrity)**
- Know legal boundaries (what's legal vs illegal hacking)
- Make difficult trade-off decisions (security vs convenience)
- Maintain confidentiality of sensitive information
- Admit mistakes & learn from them
- Follow organizational code of conduct

**7. SPECIFIC DOMAIN EXPERTISE (Specialization)**

Choose 1-2 specializations:

- **Network Security**
  - Firewall, IDS/IPS, DDoS mitigation, VPN, routing

- **Application Security**
  - Secure coding, OWASP, web app testing, API security

- **Cloud Security**
  - AWS/Azure/GCP security, serverless, containers

- **Incident Response**
  - Forensics, malware analysis, root cause, recovery

- **Risk & Compliance**
  - Audit, compliance, risk assessment, policy

- **Threat Intelligence**
  - Threat hunting, APT analysis, malware research

- **Identity & Access Management**
  - SSO, MFA, directory services, PAM, zero-trust

---

**KESIMPULAN: Framework adalah COMPASS dalam Cybersecurity Journey**

**Tanpa framework:**
- ❌ Ad-hoc security, tidak terstruktur
- ❌ Inkonsisten antar team, waste effort
- ❌ Tidak tahu progress, compliance unclear
- ❌ Business tidak percaya, sulit justify budget
- ❌ Jika breach, tidak ada playbook to follow

**Dengan framework:**
- ✅ Systematic approach, terstruktur & consistent
- ✅ Clear roadmap, semua team aligned
- ✅ Measurable progress, audit trail clear
- ✅ Business confidence, security justifiable
- ✅ Proven incident response, faster recovery

**Framework yang tepat = successful cybersecurity program**

---

### 1.2 Konsep Fundamental

#### **A. Ethical Hacking (Hacking Etis)**
Ethical hacking adalah proses penetrasi terhadap sistem IT dengan izin pemilik sistem untuk mengidentifikasi dan memperbaiki kerentanan sebelum attacker jahat melakukannya.

**Karakteristik:**
-  Ada izin tertulis dari pemilik sistem
-  Memiliki tujuan konstruktif (melindungi)
-  Mematuhi hukum dan etika profesional
-  Melaporkan findings secara rahasia

**Contoh Profesi:**
- Penetration Tester
- Security Researcher
- Bug Bounty Hunter
- Security Consultant

**Prinsip Etika & Tanggung Jawab dalam Ethical Hacking:**

Ethical hacking bukanlah sekadar teknik, melainkan **komitmen moral** terhadap integritas dan tanggung jawab. Seorang ethical hacker harus mematuhi prinsip-prinsip berikut:

**1. Tidak Menyalahgunakan Akses:**
- ✅ **Boleh**: Mengakses sistem sesuai scope yang disetujui untuk identifikasi vulnerability
- ❌ **Tidak boleh**: 
  - Menyalin atau mengambil data pribadi/sensitif
  - Memodifikasi atau menghapus data tanpa izin
  - Menggunakan akses untuk kepentingan pribadi
  - Menjual informasi yang ditemukan

**Contoh Nyata:**
```
Scenario 1 (SALAH):
- Ethical hacker menemukan database customer
- Melihat ada nomor kartu kredit
- Mencatat nomor tersebut untuk penggunaan pribadi
→ Ini PELANGGARAN HUKUM (fraud, pencurian data)

Scenario 2 (BENAR):
- Ethical hacker menemukan database customer
- Melaporkan ke owner: "Database terbuka tanpa enkripsi"
- Tidak menyalin atau menyimpan data apapun
- Mendokumentasikan hanya vulnerability-nya
→ Ini ETHICAL HACKING yang BENAR
```

**2. Berbuat Bijak & Bertanggung Jawab:**

**Sebelum Melakukan Testing:**
- ✓ Dapatkan **izin tertulis** (signed Rules of Engagement/RoE)
- ✓ Definisikan **scope dengan jelas** (IP range, aplikasi, metode yang diizinkan)
- ✓ Set **waktu testing** yang tidak mengganggu operasional
- ✓ Identifikasi **sistem kritis** yang harus dihindari
- ✓ Siapkan **kontak emergency** untuk rollback jika terjadi masalah

**Selama Testing:**
- ✓ Dokumentasikan **setiap aktivitas** (log, timestamp, bukti)
- ✓ **Minimal invasive**: Gunakan teknik yang paling tidak merusak
- ✓ **Test non-destructively dulu**: Informasi gathering sebelum eksploitasi
- ✓ **Hati-hati dengan production systems**: Jangan test di jam prime-time
- ✓ **Inform stakeholders**: Jika ada impact, komunikasikan segera

**Setelah Testing:**
- ✓ Buat laporan **professional & detailed**:
  - Vulnerability yang ditemukan
  - Langkah reproduksi yang jelas
  - Risk level & impact
  - Rekomendasi mitigasi
  - Evidence (screenshot, log)
- ✓ Presentasikan findings **confidentially** kepada authorized personnel saja
- ✓ **Tidak share** vulnerability details di public/social media
- ✓ Set **timeline** untuk client melakukan patching
- ✓ Follow-up untuk verifikasi bahwa vulnerability sudah di-fix

**3. Kepatuhan Hukum & Etika Profesional:**

**Hukum yang Relevan:**
| Hukum | Penjelasan |
|------|-----------|
| **CFAA (Computer Fraud & Abuse Act)** | US law - unauthorized access adalah crime |
| **GDPR** | EU - perlindungan data pribadi |
| **UU ITE (Indonesia)** | Pasal 30 tentang unauthorized access |
| **Hak Kekayaan Intelektual** | Jangan share exploit/technique tanpa permission |

**Etika Profesional:**
```
1. Integritas
   - Jujur dalam melaporkan findings
   - Tidak berdusta tentang kemampuan
   - Akui keterbatasan skill

2. Confidentiality
   - Jaga kerahasiaan informasi sensitif
   - Tidak discuss findings di public
   - Secure storage untuk reports

3. Competence
   - Terus belajar & update skills
   - Jangan test technique yang belum dipahami
   - Know the limitations

4. Objectivity
   - Report findings secara factual
   - Tidak bias atau berlebihan
   - Berikan konteks yang jelas
```

**4. Contoh Skenario Etika dalam Praktik:**

**Skenario A: Ditemukan Directory Traversal Vulnerability**
```
TAHAPAN BIJAK:
1. Dokumentasi: Screenshot path traversal
2. Laporan: "Directory traversal memungkinkan akses file sensitif"
3. Proof: Tunjukkan file yang bisa diakses (misal: /etc/passwd)
4. STOP di sini - jangan copy file atau explore lebih dalam
5. Rekomendasikan: Implement proper access control
6. Verifikasi: Konfirmasikan bahwa fix sudah diaplikasikan

TINDAKAN TIDAK ETIS:
❌ Download semua file dari server
❌ Modify file untuk "test" tanpa izin
❌ Share vulnerability di forum hacker
❌ Jual informasi ke pihak ketiga
```

**Skenario B: Akses Root/Admin Berhasil Didapat**
```
LANGKAH ETIS:
1. Catat bukti akses (screenshot prompt, timestamp)
2. Dokumentasi: Path eksploitasi yang digunakan
3. SEGERA LOGOUT - jangan mengeksplorasi lebih jauh
4. Laporkan: "Privilege escalation from user to root possible"
5. Rekomendasi: Update kernel, restrict sudo privileges
6. Jangan modifikasi sistem atau data apapun

JANGAN:
❌ Buat backdoor untuk akses nanti
❌ Modify log files untuk cover tracks
❌ Install tools atau software tanpa izin
❌ Change password atau konfigurasi
```

**Skenario C: Menemukan Sensitive Data (Customer Info, Passwords, Keys)**
```
TINDAKAN ETIS:
1. Foto/screenshot file path (bukti keberadaannya)
2. Laporkan: "Sensitive data ditemukan di lokasi Y tanpa enkripsi"
3. Highlight risk: "Data ini bisa diakses oleh attacker"
4. Rekomendasi: 
   - Encrypt data at rest
   - Implement access controls
   - Audit log access
5. JANGAN PERNAH menyalin atau membuka data tersebut

LARANGAN ABSOLUT:
❌ Download atau copy data
❌ Share dengan siapapun
❌ Use data untuk kepentingan pribadi
❌ Jual atau trade data
```

**5. Kode Etik untuk Ethical Hacker:**

1. Saya memiliki izin sebelum melakukan testing
2. Saya tidak akan mengungkap vulnerability tanpa izin
3. Saya tidak akan memodifikasi, menyalin, atau mencuri
4. Saya akan mendokumentasikan semuanya dengan akurat
5. Saya akan melindungi privasi organisasi
6. Saya akan mematuhi semua hukum yang berlaku
7. Saya akan bertindak dengan profesionalisme & etika
8. Saya akan terus meningkatkan skill dengan etis
9. Saya akan mendukung komunitas keamanan siber
10. Saya memahami dampak dari tindakan saya

---

#### **B. Threat (Ancaman)**

**Pengertian:**
Hal atau kondisi yang memiliki potensi untuk merusak, mencuri, atau mengganggu sistem/data.

**Penjelasan:**

Threat atau ancaman dalam konteks keamanan siber adalah segala sesuatu yang dapat menyebabkan kerugian pada organisasi. Bayangkan sistem informasi Anda sebagai sebuah benteng - threat adalah setiap kekuatan eksternal atau internal yang berusaha untuk menembus pertahanan tersebut. Threat tidak selalu aktif melakukan serangan, tetapi merupakan potensi yang ada.

Sebagai contoh konkret: Seorang hacker di internet adalah sebuah threat karena memiliki kemampuan dan niat untuk menyerang sistem Anda. Demikian juga disgruntled employee (karyawan yang tidak puas) adalah threat karena mereka memiliki akses internal dan motivasi untuk merusak. Bahkan, human error (kesalahan manusia) dapat dianggap sebagai threat karena dapat menyebabkan kerusakan meskipun tidak disengaja.

Penting untuk memahami bahwa threat bukan sekadar tentang hacker berbakat di film-film. Threat mencakup berbagai aktor dengan tingkat keahlian berbeda - mulai dari cybercriminal profesional yang mencari keuntungan finansial, hingga pemula (script kiddie) yang hanya menggunakan tools yang sudah ada, hingga nation-state yang memiliki sumber daya tidak terbatas untuk espionase cyber.

**Jenis-jenis Threat:**

1. **External Threat** - Dari luar organisasi (hacker, cybercriminal, competitor)
   - Datang dari pihak yang tidak memiliki akses resmi ke sistem
   - Contoh: Hacker dari luar negara yang mencoba penetrasi jaringan publik
   - Biasanya memerlukan teknik sophisticated untuk mendapatkan akses awal

2. **Internal Threat** - Dari dalam organisasi (disgruntled employee, akses privilege salah)
   - Datang dari pihak yang sudah memiliki akses ke sistem (karyawan, vendor, partner)
   - Contoh: Admin IT yang marah meninggalkan backdoor sebelum resign
   - Lebih berbahaya karena sudah memiliki kepercayaan dan akses

3. **Accidental Threat** - Karena kelalaian (human error, misconfiguration)
   - Tidak disengaja tetapi dapat menyebabkan kerusakan besar
   - Contoh: Admin secara tidak sengaja membagikan password di email
   - Sering diabaikan tetapi merupakan salah satu penyebab terbanyak insiden

**Contoh Threat Konkret:**

- **Malware & Virus**: Program berbahaya yang dapat merusak file, mencuri data, atau memberikan akses tidak sah
  - Narasi: Malware sering menyebar melalui email attachment atau download website tercemar
  
- **Phishing Attacks**: Email/message tipu yang meminta pengguna memberikan informasi sensitif
  - Narasi: Attacker menyamar sebagai bank atau perusahaan kepercayaan untuk menipu korban
  
- **DDoS Attacks**: Penyerangan dengan membanjiri server dengan traffic palsu
  - Narasi: Seperti pengguna membanjiri toko dengan orang-orang palsu hingga pelanggan sejati tidak bisa masuk
  
- **Data Breach**: Pencurian data sensitif dari sistem
  - Narasi: Data pribadi, finansial, atau intelektual curian dan dijual di dark web
  
- **Ransomware**: Malware yang mengenkripsi file dan meminta pembayaran
  - Narasi: Attacker mengunci data penting Anda dan mengatakan "bayar atau data hilang selamanya"
  
- **Zero-day Exploits**: Exploit untuk vulnerability yang belum diketahui developer
  - Narasi: Seperti serangan menggunakan celah rahasia di benteng sebelum pemilik mengetahuinya

---

#### **C. Vulnerability (Kerentanan)**

**Pengertian:**
Kelemahan atau celah dalam sistem yang dapat dieksploitasi oleh threat untuk menyebabkan kerusakan.

**Penjelasan:**

Vulnerability adalah celah atau kelemahan di dalam sistem yang dapat dimanfaatkan oleh threat untuk mencapai tujuan mereka. Jika threat adalah "musuh yang ingin menyerang", maka vulnerability adalah "pintu yang tidak terkunci" yang memungkinkan musuh itu masuk.

Penting dipahami bahwa vulnerability TIDAK sama dengan threat. Vulnerability hanya akan menjadi masalah jika ada threat yang memanfaatkannya. Analogi sederhana: Sebuah rumah dengan pintu yang tidak terkunci adalah vulnerability, tetapi jika tidak ada pencuri yang melewati, maka tidak ada masalah. Namun, kehadiran pencuri + pintu tidak terkunci = disaster.

Vulnerability dapat berada di berbagai lapisan sistem:
- **Level Software**: Bug dalam kode aplikasi, library yang outdated, default configuration
- **Level Hardware**: Fisik yang mudah diakses, komponen yang tidak dienkripsi
- **Level Manusia**: Pengguna yang tidak terlatih, password yang lemah, social engineering yang mudah terjebak
- **Level Organisasi**: Proses keamanan yang tidak jelas, monitoring yang tidak memadai

Vulnerability bisa ada selama berbulan-bulan atau bahkan bertahun-tahun tanpa diketahui. Inilah mengapa penetration testing (ethical hacking) penting - untuk menemukan vulnerability sebelum threat menemukan dan mengeksploitasinya terlebih dahulu.

**Sumber-Sumber Vulnerability:**

1. **Design Flaw** - Kesalahan dalam desain sistem
   - Narasi: Aplikasi dirancang tanpa mempertimbangkan keamanan sejak awal
   - Contoh: Aplikasi yang tidak pernah direncanakan untuk enkripsi data dari awal
   - Dampak: Sulit diperbaiki karena memerlukan redesign ulang

2. **Implementation Bug** - Bug dalam kode programming
   - Narasi: Developer menulis kode yang tidak aman atau memiliki bug
   - Contoh: SQL Injection karena input tidak di-sanitasi dengan benar
   - Dampak: Dapat diperbaiki dengan patch atau update

3. **Configuration Mistake** - Konfigurasi yang salah
   - Narasi: System administrator mengkonfigurasi sistem dengan setting yang tidak aman
   - Contoh: Database server yang dapat diakses dari internet tanpa password
   - Dampak: Biasanya cepat diperbaiki dengan mengubah konfigurasi

4. **Missing Patch** - Software tidak di-update
   - Narasi: Developer merilis patch keamanan tetapi organisasi belum mengaplikasikannya
   - Contoh: Windows yang belum diupdate selama 1 tahun
   - Dampak: Vulnerability yang sudah diketahui public tetapi masih berada di sistem

**Contoh Vulnerability Konkret:**

- **SQL Injection di Web Application**
  - Deskripsi: Attacker memasukkan SQL command berbahaya di input field
  - Dampak: Dapat mengakses atau menghapus seluruh database
  - Mitigasi: Input validation dan parameterized queries

- **Weak Password Policy**
  - Deskripsi: Sistem mengizinkan password pendek atau mudah ditebak
  - Dampak: Account dapat di-brute force atau di-guess
  - Mitigasi: Enforce strong password requirements dan MFA

- **Open Port yang Tidak Perlu**
  - Deskripsi: Server membuka port untuk service yang tidak digunakan
  - Dampak: Attacker dapat scan dan exploit service tersebut
  - Mitigasi: Close unnecessary ports dan disable unused services

- **Unencrypted Sensitive Data**
  - Deskripsi: Data sensitif disimpan atau dikirim tanpa enkripsi
  - Dampak: Jika data dicuri, dapat langsung dibaca
  - Mitigasi: Encrypt data at rest dan in transit

- **Missing Authentication/Authorization**
  - Deskripsi: Aplikasi tidak memeriksa siapa user dan apa yang boleh mereka lakukan
  - Dampak: Siapapun dapat mengakses resource apapun
  - Mitigasi: Implement proper authentication dan authorization controls

- **Outdated Software Version**
  - Deskripsi: Sistem menjalankan versi lama software yang sudah memiliki known CVE
  - Dampak: Public exploit tersedia dan dapat langsung digunakan attacker
  - Mitigasi: Keep software updated dengan latest security patches

---

#### **D. Risk (Risiko)**

**Pengertian:**
Probabilitas bahwa threat akan memanfaatkan vulnerability dan menyebabkan dampak negatif terhadap organisasi.

**Penjelasan Naratif Deskriptif:**

Risk adalah hasil dari kombinasi tiga faktor: threat, vulnerability, dan nilai aset. Ini adalah konsep paling penting dalam manajemen keamanan informasi. Risk bukan hanya tentang keberadaan threat atau vulnerability, tetapi tentang kemungkinan terjadinya serangan dan dampak yang ditimbulkan.

Bayangkan skenario: Anda memiliki data customer yang sangat berharga (high asset value). Ada vulnerability di sistem database Anda (unencrypted, weak password). Ada juga threat yang aktif mencari target (hacker cybercriminal). Kombinasi ketiga hal ini menciptakan HIGH RISK yang harus segera ditangani.

Rumus Risk = Threat × Vulnerability × Asset Value menggambarkan bahwa:
- Jika salah satu faktor adalah nol, maka risk akan nol
- Semakin besar ketiga faktor, semakin besar risknya
- Untuk mengurangi risk, kita bisa mengurangi salah satu atau ketiga faktor tersebut

Risk TIDAK pernah bisa dieliminasi 100%, tetapi dapat diminimalkan dan dikelola. Strategi mengelola risk adalah inti dari cybersecurity.

**Rumus Risk:**
```
RISK = THREAT × VULNERABILITY × ASSET VALUE
```

**Contoh Perhitungan:**

```
SKENARIO 1: Database Customer (HIGH RISK)
- Threat: Hacker (probability: HIGH = 3)
  → Banyak hacker aktif mencari database customer
  
- Vulnerability: Database terbuka (severity: CRITICAL = 4)
  → Database dapat diakses dari internet tanpa autentikasi
  
- Asset Value: Customer data (value: VERY HIGH = 4)
  → Data ini sangat berharga untuk bisnis dan harus dilindungi

Risk Score = 3 × 4 × 4 = 48 (CRITICAL)
→ Harus ditangani SEGERA, tidak boleh ditunda

AKSI MITIGASI:
1. Immediately: Batasi akses database dari internet
2. Urgent: Implementasikan encryption & strong authentication
3. Follow-up: Monitor akses dan audit log database


SKENARIO 2: Testing Server Internal (LOW RISK)
- Threat: Internal employee (probability: LOW = 1)
  → Biasanya tidak ada niat untuk merusak test environment
  
- Vulnerability: Default credentials (severity: MEDIUM = 2)
  → Testing server dengan default password
  
- Asset Value: Test data (value: LOW = 1)
  → Data test tidak ada nilai bisnis, hanya untuk pengujian

Risk Score = 1 × 2 × 1 = 2 (LOW)
→ Dapat ditangani dengan scheduling regular patching


SKENARIO 3: Outdated Webserver (MEDIUM RISK)
- Threat: Script kiddie (probability: MEDIUM = 2)
  → Ada banyak script kiddies yang menggunakan public exploit
  
- Vulnerability: Apache 2.4.25 dengan CVE terkenal (severity: HIGH = 3)
  → Public exploit sudah tersedia di internet
  
- Asset Value: Website company profile (value: MEDIUM = 2)
  → Bukan critical tapi penting untuk reputasi

Risk Score = 2 × 3 × 2 = 12 (MEDIUM)
→ Perlu diupdate dalam waktu dekat
```

**Risk Management Framework:**

Risk management bukanlah proses sekali jadi, tetapi siklus berkelanjutan:

1. **Identify** - Identifikasi asset & threats
   - Deskripsi: Cari tahu apa saja aset berharga yang perlu dilindungi dan apa threat yang potensial
   - Contoh: Melakukan asset inventory dan threat landscape analysis
   - Hasil: List lengkap aset dan potential threats

2. **Analyze** - Analisa probability & impact
   - Deskripsi: Tentukan seberapa mungkin threat terjadi dan apa dampaknya jika terjadi
   - Contoh: Quantitative risk analysis menggunakan historical data
   - Hasil: Risk score dan prioritas penanganan

3. **Treat** - Mitigasi, accept, avoid, transfer risk
   - Deskripsi: Ambil aksi untuk mengurangi, menerima, menghindari, atau transfer risk
   - Contoh:
     * Mitigate: Install patch untuk fix vulnerability
     * Accept: Accept low risk yang tidak perlu banyak biaya untuk mitigasi
     * Avoid: Tidak menggunakan teknologi/service tertentu yang terlalu risky
     * Transfer: Beli insurance atau outsource ke vendor yang lebih aman
   - Hasil: Risk berkurang dari level tinggi ke level terkelola

4. **Monitor** - Monitoring berkelanjutan
   - Deskripsi: Terus pantau untuk memastikan risk tetap dalam level acceptable
   - Contoh: SIEM monitoring, vulnerability scan rutin, audit log
   - Hasil: Deteksi dini jika ada threat baru atau vulnerability baru

---

### 1.3 Pilar Cyber Security (CIA Triad)

---

#### **Pengantar: Mengapa CIA Triad Penting?**

Ketika membangun rumah, kita tidak hanya fokus pada satu aspek. Kita perlu:
- **Kunci & alarm** → agar pencuri tidak masuk (Confidentiality)
- **Konstruksi kuat** → agar rumah tidak roboh atau dirusak (Integrity)
- **Listrik & air 24/7** → agar kita bisa hidup nyaman (Availability)

Sama halnya dengan keamanan sistem informasi. Kita tidak bisa hanya fokus pada satu aspek keamanan. Kita perlu menjaga **Confidentiality (Kerahasiaan)**, **Integrity (Integritas)**, dan **Availability (Ketersediaan)** secara bersamaan. Inilah yang disebut **CIA Triad**.

**Pertanyaan Kunci:**
- **Confidentiality**: "Siapa saja yang bisa akses data ini?"
- **Integrity**: "Apakah data ini masih original dan belum diubah?"
- **Availability**: "Apakah sistem ini bisa diakses ketika dibutuhkan?"

Jika salah satu dari ketiga pilar ini lemah, maka seluruh keamanan sistem akan terancam.

---

#### **Visualisasi CIA Triad**

```
                         CONFIDENTIALITY
                          (Kerahasiaan)
                    
                         Siapa saja yang
                         bisa akses data?
                         
                      Data hanya boleh
                      diakses oleh yang
                         berwenang
                              |
                    +---------|----------+
                    |                    |
                INTEGRITY           AVAILABILITY
              (Integritas)        (Ketersediaan)
              
          Apakah data masih    Apakah sistem
          original & belum     bisa diakses ketika
          diubah?              dibutuhkan?
          
          Data hanya boleh     Sistem harus online
          diubah oleh yang     24/7 & reliable
          berwenang                   |
                    |                    |
                    +---------|----------+
                              |
                         CIA TRIAD
                          SEIMBANG
                         
                       Keamanan &
                       Keandalan OK
```

---

#### **1. CONFIDENTIALITY (Kerahasiaan) - Privasi Data**

**Definisi Sederhana:**
Memastikan bahwa **HANYA orang yang berhak** yang bisa melihat atau mengakses data.

**Analogi Kehidupan Nyata:**

Bayangkan Anda memiliki **buku diary pribadi** yang berisi:
- Kisah cinta Anda
- Rencana bisnis rahasia
- Catatan kesehatan pribadi

Apa yang akan Anda lakukan?
- ✅ **Confidential**: Kunci buku itu di lemari, kunci dibuang, tidak ada yang boleh baca
- ❌ **Tidak Confidential**: Letakkan di meja terbuka, siapa saja bisa baca

Dalam dunia digital, data confidential adalah:
- **Password** → Jangan pernah share atau simpan di tempat terbuka
- **Nomor kartu kredit** → Hanya bank yang boleh tahu
- **Data medis pasien** → Hanya dokter & pasien yang boleh akses
- **Formula rahasia perusahaan** → Hanya karyawan tertentu yang boleh tahu

**Cara Menjaga Confidentiality:**

**TEKNIK MENJAGA CONFIDENTIALITY:**

1. **ENCRYPTION (Enkripsi)**
   - Ubah data jadi kode yang tidak bisa dibaca tanpa kunci
   - Contoh: Password di-hash, pesan WhatsApp encrypted

2. **ACCESS CONTROL (Kontrol Akses)**
   - Siapa saja yang bisa akses data
   - Contoh: Login dengan username & password, permission file 600

3. **AUTHENTICATION (Autentikasi)**
   - Verifikasi bahwa user benar-benar adalah siapa yang mereka klaim
   - Contoh: Password, biometric, 2FA

4. **DATA MASKING (Menyembunyikan Data)**
   - Tampilkan hanya sebagian data
   - Contoh: Nomor kartu 1234-****-****-5678 (hanya 4 digit terakhir)

5. **SECURE DELETION (Penghapusan Aman)**
   - Hapus data sampai benar-benar tidak bisa di-recover
   - Contoh: Overwrite file 3x dengan random data sebelum delete

---

**Skenario Real-world Breach Confidentiality:**

**❌ BREACHED (Data Terbuka):**

Database Customer Bank AMAN JAYA (Tidak ter-enkripsi, terbuka publik):

| ID | Nama | No. Kartu |
|----|------|-----------|
| 001 | Budi Santoso | 1234-5678-... |
| 002 | Siti Nurhal | 5432-1098-... |
| 003 | Agus Rahman | 9876-5432-... |

**Hasil:**
- Hacker akses database
- Curi 100,000+ nomor kartu kredit
- Jual di dark web dengan harga $10/kartu
- Kerugian bank: $1 juta + reputasi hancur

**Penyebab:**
- Database tidak ter-enkripsi
- Akses terbuka dari internet tanpa password
- Tidak ada monitoring akses

✅ **PROTECTED (Data Aman):**

**Database Customer Bank AMAN JAYA** (Encrypted, Access Control ON)

| ID | Nama | No. Kartu |
|----|------|-----------|
| 001 | Budi Santoso | [ENCRYPTED:***] |
| 002 | Siti Nurhal | [ENCRYPTED:***] |
| 003 | Agus Rahman | [ENCRYPTED:***] |

**Access Log:**
- 2025-01-15 10:30:05 admin1 LOGIN
- 2025-01-15 10:31:22 admin1 QUERY
- 2025-01-15 10:32:45 admin1 LOGOUT

**Perlindungan:**
- ✓ Data ter-enkripsi → Tidak bisa dibaca meski dicuri
- ✓ Access Control → Hanya admin berwenang login
- ✓ Authentication → Login dengan password + 2FA
- ✓ Audit Log → Setiap akses dimonitor & dicatat
- ✓ Firewall → Database hanya boleh diakses dari jaringan internal

**Hasil:**
- Bahkan jika hacker masuk, data yang dicuri hanya encrypted blobs
- Tidak bisa digunakan
- Audit log menunjukkan siapa & kapan akses terjadi
- Cepat terdeteksi & response team activated

---

#### **2. INTEGRITY (Integritas) - Keaslian & Keakuratan Data**

**Definisi Sederhana:**
Memastikan bahwa data **tidak berubah secara tidak sah** dan tetap **original & akurat**.

**Analogi Kehidupan Nyata:**

Bayangkan Anda menerima **surat resmi dari universitas** yang berisi:
- Nilai ujian Anda: **A (outstanding)**
- Status kelulusan: **Passed**

Apa yang bisa terjadi jika tidak ada integritas?

❌ **Integrity Breach:**
- Hacker akses server universitas
- Ubah nilai dari A → F
- Ubah status dari "Passed" → "Failed"
- Tidak ada yang tahu kalo surat sudah dimanipulasi
- Anda kehilangan beasiswa, ditolak kerja

✅ **Integrity Protected:**
- Surat dilengkapi signature digital & seal dari rektor
- Jika ada yang coba ubah, signature tidak valid
- Sistem bisa deteksi "surat ini sudah dimanipulasi"
- Surat original tersimpan dengan checksum/hash

**Cara Menjaga Integrity:**

**TEKNIK MENJAGA INTEGRITY**

1. **DIGITAL SIGNATURE**
   - Tanda tangan digital untuk verifikasi keaslian dokumen
   - Seperti seal dari institusi

2. **CHECKSUM / HASH**
   - Fingerprint unik dari data
   - Jika data berubah 1 bit saja, checksum berubah total
   - Contoh: SHA256 hash

3. **VERSION CONTROL**
   - Simpan history perubahan
   - Siapa mengubah apa kapan
   - Bisa rollback ke versi sebelumnya

4. **READ-ONLY MODE**
   - Data tidak boleh diubah setelah tertentu (immutable)
   - Contoh: Log files di append-only

5. **PERMISSION & ACCESS CONTROL**
   - Siapa saja yang boleh ubah data
   - Contoh: hanya admin yang bisa edit konfigurasi

6. **AUDIT LOG & MONITORING**
   - Catat setiap perubahan data
   - Monitor aktivitas mencurigakan
   - Alert jika ada anomali

---

**Skenario Real-world Breach Integrity:**

**❌ INTEGRITY COMPROMISED (Data Berubah):**

**Transaksi Bank Normal:**

| Waktu | Dari | Ke | Jumlah | Status | Hash |
|-------|------|----|---------| -------|------|
| 2025-01-15 14:30:00 | Agus (Rp 1,000,000) | Budi | Rp 100,000 | COMPLETED | a3c8f9d2e1b4c5f6... |

**Hacker Ubah Data:**

**Transaksi Bank (Sudah dimanipulasi):**

| Waktu | Dari | Ke | Jumlah | Status | Hash |
|-------|------|----|---------| -------|------|
| 2025-01-15 14:30:00 | Agus (Rp 1,000,000) ← DIUBAH | Budi | Rp 1,000,000 | COMPLETED | MISMATCH! |

**Dampak:**
- Agus pikir transfer Rp 100,000 tapi ternyata Rp 1 juta
- Budi dapat Rp 1 juta bukannya Rp 100,000
- Bank tidak tahu transaksi sudah dimanipulasi
- Kerugian finansial & kepercayaan rusak

---

✅ **INTEGRITY PROTECTED (Data Aman):**

**Transaksi dengan Digital Signature & Checksum:**

| Waktu | Dari | Ke | Jumlah | Status | Hash | Digital Sig |
|-------|------|----|---------| -------|------| ------------|
| 2025-01-15 14:30:00 | Agus (Rp 1,000,000) | Budi | Rp 100,000 | COMPLETED | a3c8f9d2e1b4c5f6... | 🔒 Bank (verified) |

**Jika Hacker Coba Ubah:**

| Waktu | Dari | Ke | Jumlah | Status | Hash | Digital Sig |
|-------|------|----|---------| -------|------| ------------|
| 2025-01-15 14:30:00 | Agus (Rp 1,000,000) ← DIUBAH ❌ | Budi | Rp 1,000,000 ← DIUBAH ❌ | COMPLETED | MISMATCH ❌ | ❌ INVALID |

**Sistem Mendeteksi:**
- ✓ Hash tidak cocok → Data berubah
- ✓ Digital signature rusak → Manipulasi terdeteksi
- ✓ Timestamp berubah → Alert sistem
- ✓ Transaksi ditolak & investigasi dimulai
✓ Digital signature invalid → Bukan dari bank
✓ Timestamp berubah → Pesan original dimanipulasi
✓ Alert: "FRAUD DETECTED - Transaksi ini sudah diubah!"
✓ Transaksi ditolak, investigasi dimulai

---



#### **3. AVAILABILITY (Ketersediaan) - Akses & Keandalan**

**Definisi Sederhana:**
Memastikan bahwa **sistem & data dapat diakses oleh yang berhak kapanpun dibutuhkan**.

**Analogi Kehidupan Nyata:**

Bayangkan Anda memiliki **toko online 24 jam**:
- Customer bisa belanja kapan saja
- Stok barang selalu tersedia
- Website tidak pernah down

Apa yang bisa terjadi jika tidak ada availability?

❌ **Availability Breach:**
- Website tiba-tiba down saat promo besar-besaran
- Customer tidak bisa order
- Competitor mulai terima orderan
- Penjualan drop 90%, kerugian jutaan
- Reputasi rusak (website tidak reliable)

✅ **Availability Protected:**
- Website di-backup di multiple servers
- Jika 1 server down, traffic diswitch ke server lain (auto-failover)
- Load balancer distribusi traffic evenly
- Monitoring 24/7 untuk deteksi masalah
- DDoS protection untuk mencegah serangan
- Uptime guarantee 99.99% (hanya down ~45 menit per tahun)

**Cara Menjaga Availability:**

**TEKNIK MENJAGA AVAILABILITY**

1. **REDUNDANCY (Backup System)**
   - Buat duplikat sistem/data
   - Jika yang utama down, ada backup yang siap ambil alih
   - Contoh: 2 server untuk website

2. **LOAD BALANCING**
   - Distribusi traffic ke multiple server agar tidak overload
   - Meningkatkan capacity & speed

3. **AUTO-FAILOVER**
   - Automatic switch ke backup jika primary server down
   - Tidak ada manual intervention diperlukan

4. **BACKUP & DISASTER RECOVERY**
   - Regular backup data (daily)
   - Bisa restore jika terjadi data loss atau disaster

5. **MONITORING & ALERTING**
   - Monitor system health 24/7
   - Alert jika ada issue
   - Quick response & resolution

6. **DDoS PROTECTION**
   - Proteksi dari DDoS attack
   - Filter malicious traffic
   - Keep website accessible

7. **CAPACITY PLANNING**
   - Pastikan resource cukup
   - Scale up sebelum bottleneck
   - Prevent performance degradation

---

**Skenario Real-world Breach Availability:**

**❌ AVAILABILITY COMPROMISED (Sistem Down):**

**Serangan DDoS ke Website Tokopedia:**

| Metrik | Nilai | Status |
|--------|-------|--------|
| Normal Traffic | 1,000 req/sec | ✅ OK |
| DDoS Attack | 1,000,000 req/sec | ❌ OVERLOAD |
| Server CPU | 100% | ❌ Maksimal |
| Response Time | 30+ detik | ❌ Sangat lambat |
| Customer bisa akses | NO | ❌ TIDAK |

**Dampak:**
- Tidak bisa order selama 2 jam
- Revenue loss jutaan rupiah
- Kehilangan Rp 100 miliar transaksi
- Customer kecewa, switch ke Shopee
- Media headlines: Tokopedia Down
- Reputasi & kepercayaan merosot

---

✅ **AVAILABILITY PROTECTED (Sistem Robust):**

**Tokopedia dengan Availability Protection:**

| Aspek | Status | Hasil |
|-------|--------|-------|
| Normal Traffic | 1,000 req/sec | ✅ OK |
| DDoS Attack | 1,000,000 req/sec | ✅ DETECTED |
| DDoS Detection | ✓ Activated | ✓ Filtering malicious IPs |
| Primary Server 1 | 50% CPU | ✓ Healthy |
| Primary Server 2 | 50% CPU | ✓ Healthy |
| Backup Server 1 | 30% CPU | ✓ Standby ready |
| Load Balancer | ✓ Active | ✓ Distributing traffic |
| Response Time | 200ms | ✓ Normal |
| Customer bisa order | YES | ✓ YES |

**Hasil:**
- ✓ Website tetap online & responsive
- ✓ DDoS attack berhasil diblokir
- ✓ Customer order normal
- ✓ Transaksi Rp 100 miliar tetap lancar
- ✓ Reputasi terjaga

---

#### **Saling Ketergantungan CIA Triad**

Penting untuk dipahami bahwa **CIA bukan pilar yang terpisah**, melainkan **saling tergantung & saling mendukung**:

**SALING KETERGANTUNGAN CIA**

- **Confidentiality + Integrity**
  - Data private & tidak bisa diubah
  - Contoh: Enkripsi + digital signature

- **Confidentiality + Availability**
  - Data private tapi selalu accessible
  - Contoh: Encrypted backup di cloud

- **Integrity + Availability**
  - Data akurat & selalu tersedia
  - Contoh: Version control + redundancy

- **Confidentiality + Integrity + Availability**
  - Keamanan & keandalan sistem optimal
  - Data aman, tidak berubah, always on

---

**Contoh Kolaborasi CIA dalam Sistem Bank Online:**

**SISTEM BANK ONLINE AMAN**

- **CONFIDENTIALITY:**
  - ✓ Login dengan password + 2FA
  - ✓ Data transaksi ter-enkripsi
  - ✓ Hanya pemilik account yang lihat

- **INTEGRITY:**
  - ✓ Setiap transaksi punya digital signature
  - ✓ Hash untuk verifikasi data
  - ✓ Audit log mencatat semua perubahan

- **AVAILABILITY:**
  - ✓ Server multiple (redundancy)
  - ✓ Backup database real-time
  - ✓ Monitoring 24/7
  - ✓ DDoS protection aktif

- **HASIL:**
  - = Keamanan Maksimal + Keandalan Baik

---

#### **Perbandingan CIA Triad dengan Analogi Sehari-hari**

| Pilar | Contoh Nyata | Deskripsi |
|-------|--------------|-----------|
| **CONFIDENTIALITY** | Brankas Bank | Kunci ganda ✓ / Alarm ✓ / Hanya teller authorized ✓ / = Uang aman dari pencuri |
| **INTEGRITY** | Surat Wasiat Notaris | Cap tanda tangan notaris ✓ / Stempel resmi ✓ / Tercatat & sulit dipalsu ✓ / = Isi tidak bisa diubah orang lain |
| **AVAILABILITY** | Apotek 24 Jam | Buka siang & malam ✓ / Stok obat selalu ada ✓ / Emergency staff standby ✓ / = Obat bisa didapat kapanpun |
| **CIA ALL** | Rumah Sakit Modern | Rekam medis ter-enkripsi (Conf) ✓ / Data digital + backup (Avail) ✓ / Log akses diaudit (Integrity) ✓ / Layanan aman, akurat, 24/7 |

---

#### **Contoh Data & Penjelasan CIA Triad (Numbering)**

**1. CONFIDENTIALITY (Kerahasiaan):**

   **Contoh data yang memerlukan Confidentiality:**
   - Password pengguna
   - Nomor kartu kredit
   - Data medis pasien
   - Strategi bisnis rahasia
   - Informasi karyawan (gaji, alamat)

   **Penjelasan Lengkap:**
   Confidentiality berarti data harus dirahasiakan dari pihak yang tidak berwenang. Jika data ini bocor, dampaknya bisa sangat besar:
   - Password bocor → Akun diretas, identitas dicuri
   - Nomor kartu kredit bocor → Penipuan transaksi, uang hilang
   - Data medis bocor → Privacy invaded, diskriminasi kesehatan
   - Strategi bisnis bocor → Kompetitor dapat keuntungan, bisnis rugi
   
   **Cara melindungi:**
   ```
   ✓ Enkripsi data saat disimpan (at rest): AES-256
   ✓ Enkripsi saat dikirim (in transit): HTTPS/TLS
   ✓ Kontrol akses ketat: Hanya authorized users
   ✓ Authentication kuat: Password + 2FA
   ✓ Data masking: Sembunyikan sebagian data di-display
   ✓ Monitoring: Alert jika ada unusual access
   ```

---

**2. INTEGRITY (Integritas):**

   **Contoh data yang memerlukan Integrity:**
   - File konfigurasi server (jangan boleh diubah sembarangan)
   - Data transaksi keuangan (harus akurat, tidak boleh dimanipulasi)
   - Hasil ujian mahasiswa (tidak boleh diubah)
   - Kontrak digital (harus sesuai original)
   - Log audit (harus immutable/tidak bisa diubah)

   **Penjelasan Lengkap:**
   Integrity berarti data harus tetap original, akurat, dan hanya bisa diubah oleh pihak yang berwenang. Jika integrity terganggu, dampaknya:
   - Transaksi dimanipulasi → Uang hilang, rekening tidak seimbang
   - Konfigurasi server diubah → Sistem rusak, layanan down
   - Nilai ujian diubah → Keputusan akademik salah
   - Bukti digital diubah → Kejahatan tidak terdeteksi
   
   **Cara melindungi:**
   ```
   ✓ Digital signature: Tanda tangan digital untuk verifikasi
   ✓ Hash/Checksum: Fingerprint unik data, deteksi perubahan
   ✓ Version control: Tracking semua perubahan & history
   ✓ Access control: Hanya authorized bisa edit
   ✓ Audit logging: Catat siapa ubah apa kapan
   ✓ Read-only mode: Data tidak boleh diubah setelah tertentu
   ```

---

**3. AVAILABILITY (Ketersediaan):**

   **Contoh data/sistem yang memerlukan Availability:**
   - Website e-commerce (harus online 24/7)
   - Layanan email perusahaan (harus akses kapanpun)
   - Sistem ATM bank (harus bisa digunakan customer)
   - Hospital management system (harus reliable untuk save lives)
   - Emergency hotline (harus selalu tersedia)

   **Penjelasan Lengkap:**
   Availability berarti sistem & data harus dapat diakses oleh authorized users kapanpun dibutuhkan. Jika availability terganggu, dampaknya:
   - E-commerce website down → Tidak bisa order, kehilangan penjualan
   - Email down → Komunikasi bisnis terganggu
   - ATM offline → Customer tidak bisa withdrawal uang
   - Hospital system down → Pasien tidak bisa dapat treatment
   - Emergency hotline tidak bisa diakses → Nyawa orang taruhan
   
   **Cara melindungi:**
   ```
   ✓ Redundancy: Backup system siap jika primary down
   ✓ Load balancing: Distribusi traffic ke multiple servers
   ✓ Auto-failover: Automatic switch ke backup
   ✓ Regular backup: Data recovery jika terjadi disaster
   ✓ Monitoring & alerting: Deteksi masalah sedini mungkin
   ✓ DDoS protection: Proteksi dari serangan flooding
   ✓ Capacity planning: Resource cukup untuk peak load
   ✓ Maintenance scheduling: Downtime minimal & planned
   ```

---

#### **Summary: Mengapa CIA Penting?**

**MENGAPA KITA PERLU CIA TRIAD?**

**1. BUSINESS CONTINUITY**
- Jika salah satu pilar jebol, bisnis bisa collapse
- CIA menjaga operasional tetap lancar

**2. TRUST & REPUTATION**
- Customer percaya karena data aman, akurat, dan sistem reliable
- CIA build confidence

**3. COMPLIANCE & LEGAL**
- Regulasi (GDPR, UU ITE) memerlukan CIA untuk melindungi data customer
- Non-compliance = denda besar & masalah hukum

**4. PREVENT FRAUD & CYBERCRIME**
- CIA mencegah:
  - Identity theft (Conf)
  - Data manipulation (Int)
  - Service disruption (Avail)

**5. COMPETITIVE ADVANTAGE**
- Organisasi dengan CIA protection:
  - Lebih dipercaya pelanggan
  - Kurang rentan attack
  - Recovery lebih cepat jika terjadi insiden

**6. MINIMIZE DAMAGE**
- Tidak semua breach bisa dicegah, tapi CIA memastikan damage jika terjadi = minimal

---

#### **Contoh Kasus: Breach & Impact (CIA Perspective)**

**Kasus: Data Breach di E-Learning Platform Universitas**

**SCENARIO:** Hacker berhasil access database student grades

---

**❌ JIKA TIDAK ADA CIA PROTECTION:**

**CONFIDENTIALITY BREACH:**
- Database tidak ter-enkripsi
- Hacker akses semua data: Nama, ID, Nilai, Email, Alamat
- Data dijual ke data broker (Rp 500 juta)
- Identity theft: Beberapa mahasiswa akun bank diretas

INTEGRITY BREACH:
- Hacker ubah nilai: A → F, F → A
- Tidak ada signature untuk verifikasi original
- Mahasiswa beasiswa hilang, mahasiswa jelek jadi lulus
- Chaos: Mahasiswa tidak tahu nilai mana yang benar

AVAILABILITY BREACH:
- Hacker delete backup database
- Tidak ada recovery option
- Data grades hilang selamanya
- Universitas harus redo grades dari scratch (bulan-bulan)

TOTAL DAMAGE:
💰 Financial: Rp 5+ miliar (legal fees, compensation, reputasi)
😤 Reputasi: Universitas dipercaya jadi not trustworthy
👥 Users: Mahasiswa & orang tua kecewa & laporkan ke media
📰 Media: Headline "Universitas Data Breach Terbesar Tahun Ini"
⚖️ Legal: Denda regulasi + lawsuits dari affected parties

--- 

✅ JIKA ADA CIA PROTECTION:

CONFIDENTIALITY:
✓ Database ter-enkripsi (AES-256)
✓ Hacker akses hanya encrypted blobs (tidak bisa baca)
✓ Juga ada access control: Login required + 2FA
✓ Data tidak bisa dijual (encrypted, tidak berguna)

INTEGRITY:
✓ Setiap grade record punya digital signature
✓ Jika hacker ubah nilai, signature invalid
✓ System alert: "TAMPERING DETECTED"
✓ Jika nilai berubah, audit log menunjukkan siapa ubah

AVAILABILITY:
✓ Backup database ter-replicate real-time di multiple servers
✓ Jika hacker delete backup, ada 2-3 backup lain
✓ Disaster recovery plan: Restore dalam hitungan jam
✓ Downtime minimal, data dapat di-recover

 TOTAL DAMAGE DENGAN PROTECTION:
 
💰 Financial: Minimal (quick response, audit log, insurance)

😤 Reputasi: Terjaga (proactive disclosure, quick action)

👥 Users: Percaya (transparent, protective measures)

📰 Media: Positif (Universitas handles breach professionally)

⚖️ Legal: Compliant (Incident response log, no data actual leaked)

---

KEY TAKEAWAY:
CIA Triad bukan hanya nice-to-have, tapi MUST-HAVE untuk
protect assets, maintain trust, & survive cyber incidents.


## 🛡️ B. DEFENSIVE VS OFFENSIVE SECURITY

### 2.1 Defensive Security (Blue Team)

**Definisi:** Strategi dan praktik untuk melindungi sistem dan data dari serangan.

**Tujuan:**
-  Mencegah akses tidak sah
-  Mendeteksi aktivitas mencurigakan
-  Merespons dan memulihkan dari insiden
-  Memastikan business continuity

**Metode & Teknik:**

| Aspek | Penjelasan | Contoh Implementasi |
|-------|-----------|-------------------|
| **Firewalls** | Mengontrol traffic masuk/keluar | UFW, iptables di Linux |
| **Access Control** | Authentikasi & authorization | User, password, permissions |
| **Encryption** | Melindungi data saat transit & rest | SSL/TLS, AES encryption |
| **Patching** | Update sistem & software | Regular security updates |
| **Hardening** | Meminimalkan attack surface | Disable unnecessary services |
| **Monitoring & Logging** | Deteksi aktivitas aneh | Analisa log, SIEM tools |
| **Backup & Disaster Recovery** | Pemulihan dari insiden | Regular backups, snapshots |
| **Security Awareness** | Training staff | Phishing awareness, password policy |

**Timeline Defensive:**
```
Prevention → Detection → Response → Recovery
   (60%)       (25%)       (10%)      (5%)
```

**Penjelasan Timeline:**
- **Prevention (60%)**: Langkah proaktif untuk mengurangi kemungkinan serangan — termasuk patching rutin, hardening konfigurasi, pengaturan firewall/ACL, manajemen akses (IAM), enkripsi, dan kebijakan keamanan. Prioritas besar karena mencegah insiden lebih murah dan lebih cepat dibanding memperbaiki setelah terjadi.
- **Detection (25%)**: Aktivitas monitoring dan deteksi — pengumpulan log, IDS/IPS, SIEM, threat hunting, dan alerting. Tujuannya menemukan indikasi serangan sedini mungkin sehingga dapat diminimalkan dampaknya.
- **Response (10%)**: Tindakan korektif setelah deteksi — containment (isolasi sistem), mitigasi cepat, forensik awal, komunikasi insiden, dan pelaksanaan runbook IR. Efektivitas response mengurangi waktu pemulihan dan kerugian.
- **Recovery (5%)**: Pemulihan layanan dan perbaikan jangka panjang — restore dari backup, patching pasca‑insiden, verifikasi integritas, dan post‑incident review (lessons learned). Bagian kecil namun penting untuk memastikan layanan kembali aman dan stabil.

**Catatan tentang persentase:** Persentase tersebut adalah panduan alokasi effort/anggaran waktu dalam siklus keamanan; proporsi sebenarnya dapat berbeda berdasarkan ukuran organisasi, risiko, dan kompleksitas lingkungan.


---

### 2.2 PENTINGNYA BELAJAR LINUX DALAM CYBERSECURITY

**Mengapa Linux Harus Dipelajari di Cybersecurity?**

Linux adalah fondasi teknologi di industri cybersecurity modern. Pemahaman mendalam tentang Linux bukan pilihan, tetapi keharusan. Berikut penjelasan komprehensif:

---

#### **🖥️ 1. DOMINASI SERVER GLOBAL: 90%+ Berbasis Linux**

**Statistik Industri:**
- **90%+ dari semua server di dunia menjalankan Linux**
- **Top cloud platforms**: AWS, Google Cloud, Azure menggunakan Linux sebagai OS default
- **Enterprise infrastructure**: Data center, cloud infrastructure, server web mayoritas Linux
- **IoT & Edge Computing**: 80% IoT devices berbasis Linux-based OS (Android, embedded Linux)

**Implikasi untuk Cybersecurity:**
Jika Anda ingin mengamankan infrastruktur modern, Anda HARUS mengerti Linux. Serangan cyber paling banyak menargetkan Linux karena:
- Mayoritas server yang digunakan organisasi adalah Linux
- Linux admin & security engineer sangat dibutuhkan
- Kerentanan Linux yang tidak dipatchpun bisa membahayakan ribuan server

**Contoh Real-World:**
- **Google**: Menggunakan Linux kernel yang di-customize (Android based Linux)
- **IBM**: Mainframe & cloud services menggunakan Linux
- **Amazon AWS**: 95%+ infrastructure berbasis Linux
- **Microsoft Azure**: Menawarkan Linux sebagai primary OS option
- **Netflix, Facebook, Twitter**: Semua menggunakan Linux di production

---

#### **🔒 2. LINUX SEBAGAI TULANG PUNGGUNG CYBERSECURITY TOOLS**

**Mayoritas Security Tools Dibangun untuk Linux:**

| Kategori | Tools/Framework | Basis |
|----------|-----------------|-------|
| **Penetration Testing** | Metasploit, nmap, Burp Suite (free), Kali Linux | Linux-first |
| **Network Security** | tcpdump, Wireshark, Suricata, Zeek | Linux-native |
| **Forensics** | Volatility, Sleuth Kit, YARA, OSForensics | Linux-optimized |
| **System Hardening** | AIDE, Lynis, OpenSCAP, CIS Benchmarks | Linux-specific |
| **Monitoring & SIEM** | Splunk, ELK Stack, Graylog, Wazuh | Linux deployment |
| **Vulnerability Scanning** | OpenVAS, Qualys, Rapid7 | Linux-compatible |
| **Malware Analysis** | Cuckoo Sandbox, Ghidra, Radare2 | Linux-powered |
| **Cryptography** | OpenSSL, GnuPG, Hashcat | Linux-native |

**Mengapa Tools Berbasis Linux?**
- **Open-source nature**: Source code transparan untuk audit keamanan
- **Flexibility**: Dapat di-customize untuk kebutuhan spesifik
- **Performance**: Lightweight, efficient, cocok untuk processing data besar
- **Stability**: Production-grade reliability untuk 24/7 operations
- **Community**: Ekosistem besar dengan support & development aktif

---

#### **🛡️ 3. LINUX HARDENING & DEFENSIVE SECURITY**

**Linux di Defensive Security digunakan untuk:**

**A. Server Hardening (Pengurangan Attack Surface)**
```
- Disable unnecessary services (FTP, Telnet, X11)
- Reduce open ports (hanya SSH, HTTP/HTTPS)
- Implement file permissions & SELinux/AppArmor
- Regular patching & security updates
- Firewall configuration (UFW, iptables, nftables)
- Disable root login, enforce strong passwords
```

**B. System Hardening Tools (Linux-based)**
- **Lynis**: Automated security auditing tool untuk Linux systems
- **AIDE** (Advanced Intrusion Detection Environment): File integrity monitoring
- **OpenSCAP**: Configuration & vulnerability scanning
- **CIS Benchmarks**: Security baselines khusus Linux
- **SELinux/AppArmor**: Mandatory access controls

**C. Log Monitoring & Analysis**
- **Syslog/Rsyslog**: Centralized logging
- **ELK Stack** (Elasticsearch, Logstash, Kibana): Log aggregation & analysis
- **Wazuh**: Security monitoring platform
- **Splunk**: Enterprise security information & event management

**D. Network Security**
- **Firewall Management**: iptables, nftables, UFW
- **VPN & Tunneling**: OpenVPN, WireGuard
- **Intrusion Detection**: Suricata, Snort running on Linux
- **DDoS Protection**: HAProxy, Linux kernel tuning

---

#### **⚔️ 4. LINUX DI OFFENSIVE SECURITY (RED TEAM)**

**Linux sebagai primary tool untuk penetration testing:**

**A. Kali Linux Ecosystem**
- **Purpose-built**: Dirancang khusus untuk pentest & ethical hacking
- **Pre-installed tools**: 500+ security tools sudah siap pakai
- **Active development**: Update regular dengan tools & exploits terbaru

**B. Attack Tools yang Linux-based**
- **Metasploit Framework**: Exploitation framework utama (Ruby + Linux)
- **Nmap**: Network mapping & port scanning
- **Burp Suite Community**: Web application security testing
- **Wireshark**: Network traffic analysis
- **John the Ripper / Hashcat**: Password cracking
- **Aircrack-ng**: Wireless security testing
- **SQLmap**: SQL injection testing

**C. Post-Exploitation & Persistence**
- **Bash/Shell scripting**: Automation & custom exploits
- **Privilege escalation**: Linux kernel exploits, sudo misconfigurations
- **Persistence mechanisms**: Cron jobs, systemd services, rootkits
- **Log manipulation**: Clearing audit trails (anti-forensics)

**D. Linux is Attacker-Friendly**
- Transparent file permissions (dapat di-exploit)
- Detailed logs memberikan reconnaissance data
- Kernel vulnerabilities (jika unpatched)
- Misconfiguration adalah entry point utama

---

#### **📊 5. MARKET DEMAND: LINUX SKILLS SANGAT DICARI**

**Job Market Reality:**
- **90% cybersecurity jobs** membutuhkan Linux skills
- **Salary premium**: Security engineer dengan Linux expertise dapat 15-25% lebih tinggi
- **Career progression**: CISOs, security architects wajib menguasai Linux

**Typical Cybersecurity Job Requirements:**
```
✓ Linux system administration (RHEL, CentOS, Ubuntu, Debian)
✓ Linux shell scripting (Bash)
✓ Linux networking & firewall management
✓ Linux hardening & security best practices
✓ Linux log analysis & monitoring
✓ Linux vulnerability assessment
✓ Red team Linux exploitation
```

**Contoh Job Postings Real:**
- **Security Engineer**: "5+ years Linux sysadmin experience required"
- **Penetration Tester**: "Must have Kali Linux & offensive Linux skills"
- **SOC Analyst**: "Linux log analysis & threat hunting required"
- **DevSecOps Engineer**: "Docker, Kubernetes, Linux container security"

---

#### **🔧 6. HANDS-ON REASONS: MENGAPA BELAJAR LINUX PRACTICAL**

**A. Remote Access & Command-Line Power**
- Cybersecurity work 80% dilakukan di terminal/command-line
- SSH (Secure Shell) adalah standard remote access
- Scripting automation menghemat waktu & mengurangi human error

**B. Scripting & Automation**
```bash
# Contoh: Automated vulnerability scanning
for ip in 192.168.1.1-254; do
  nmap -sV $ip >> scan_results.txt
done

# Contoh: Log analysis & threat detection
grep "failed password" /var/log/auth.log | wc -l

# Contoh: Rapid patching across multiple servers
ansible all -m yum -a "name=* state=latest"
```

**C. Container & Cloud Native Security**
- Docker, Kubernetes, Podman adalah Linux-based tools
- Cloud infrastructure (AWS, Azure, GCP) semua Linux-based
- Modern cybersecurity = container security = Linux security

**D. Custom Tool Development**
- Ability to write custom scripts untuk deteksi ancaman
- Network automation & security orchestration
- Threat intelligence processing

---

#### ** 7. KESIMPULAN: Linux = Foundation of Modern Cybersecurity**

**Jika Anda tidak mahir Linux:**
- ❌ Tidak bisa setup defensif infrastructure yang aman
- ❌ Tidak bisa melakukan penetration testing efektif
- ❌ Tidak bisa menganalisis logs & threat intelligence
- ❌ Tidak bisa memahami attacker tactics (99% attack ada Linux element)
- ❌ Tidak kompetitif di job market cybersecurity

**Jika Anda mahir Linux:**
- ✅ Bisa secure 90%+ server di dunia
- ✅ Bisa perform advanced offensive security operations
- ✅ Bisa setup & maintain enterprise security infrastructure
- ✅ Bisa automation security tasks & improve efficiency
- ✅ Salary premium + high job demand

**Investment ROI:**
- **Waktu belajar**: 3-6 bulan untuk fundamental, 1-2 tahun untuk advanced proficiency
- **Return**: 30+ tahun career dalam cybersecurity dengan Linux skills highly valued
- **Adaptability**: Linux skills applicable across cloud, container, IoT, infrastructure security

---

### 2.2 Offensive Security (Red Team)

**Definisi:** Strategi dan praktik untuk mengidentifikasi kerentanan sistem dengan cara simulasi serangan (dengan izin).

**Tujuan:**
-  Menemukan vulnerability sebelum attacker
-  Menguji efektivitas defensive controls
-  Melakukan risk assessment
-  Memberikan rekomendasi perbaikan

**Metode & Teknik:**

| Fase | Penjelasan | Contoh Tools/Commands |
|-----|-----------|----------------------|
| **Reconnaissance** | Information gathering | whois, nmap, Google dorks |
| **Scanning** | Identifikasi open ports & services | nmap -sV, Nikto |
| **Enumeration** | Detail mapping target | nmap -p-, SMB enumeration |
| **Exploitation** | Exploit vulnerability | Metasploit, manual exploit |
| **Privilege Escalation** | Naik privilege user | sudo, kernel exploits |
| **Post-Exploitation** | Maintain access, cover tracks | Shells, rootkit, log clearing |
| **Reporting** | Dokumentasi findings | Burp report, custom report |

**Timeline Offensive:**
```
Recon → Scanning → Enumeration → Exploitation → Post-Exploit → Reporting
  (15%)    (15%)        (20%)         (30%)           (15%)        (5%)
```

**Penjelasan Timeline Offensive (Deskriptif):**
- **Recon (15%)**: Pengumpulan informasi awal tentang target secara pasif/aktif — domain, IP, infrastruktur publik, teknologi yang digunakan, dan sumber intel lain. Teknik: OSINT, whois, DNS enumeration, Google dorking.
- **Scanning (15%)**: Pemindaian untuk menemukan host hidup, port terbuka, dan layanan yang berjalan (mis. nmap). Hasil scanning menentukan permukaan serang yang akan diuji.
- **Enumeration (20%)**: Mengumpulkan detail lebih dalam dari layanan yang ditemukan: versi software, direktori web, account/SMB shares, konfigurasi layanan. Tujuannya menemukan vektor eksploitasi yang konkret.
- **Exploitation (30%)**: Percobaan untuk mengeksploitasi kerentanan yang teridentifikasi guna mendapatkan akses awal. Metode bisa manual atau dengan framework (Metasploit). Fase ini mengambil porsi waktu terbesar karena membutuhkan uji coba dan verifikasi.
- **Post-Exploit (15%)**: Aktivitas setelah akses: eskalasi privilege, pivoting ke jaringan internal, pengumpulan bukti, dan persistence jika diperlukan sesuai ruang lingkup. Fokus pada pengumpulan evidence dan meminimalkan dampak.
- **Reporting (5%)**: Dokumentasi temuan, bukti, langkah reproduksi, dampak, dan rekomendasi mitigasi. Laporan harus jelas untuk tim defensive/owner melakukan perbaikan.

**Catatan tentang persentase:** Persentase ini bersifat panduan alokasi effort dalam engagement pentest; realitasnya bisa berubah berdasarkan scope, kompleksitas target, dan batasan izin.

**Masukan Praktis (Safety & Process):**
- Selalu dapatkan izin tertulis & definisikan scope sebelum mulai.  
- Simpan bukti aktivitas (logs, captures) dan jangan merusak data produksi.  
- Mulai dari teknik non‑destruktif → escalasi bertahap jika diizinkan.  
- Siapkan rollback/mitigasi cepat bila pengujian memengaruhi service.



---

### 2.3 Perbandingan Defensive vs Offensive

| Aspek | Defensive Security | Offensive Security |
|-------|--------------------|--------------------|
| Mindset | "Bagaimana kami bisa melindungi?" | "Bagaimana attacker bisa menyerang?" |
| Strategi | Proactive & Reactive | Proactive |
| Focus | Prevention, Detection | Finding & Testing |
| Tools | Firewalls, IDS, SIEM | Nmap, Burp, Metasploit |
| Operasional | Ongoing: 24/7 monitoring | Project-based: Pentest |
| Goal | System stays secure | Find vulns & fix them |

---

## 🛠️ C. TOOLS & COMMAND YANG DIGUNAKAN

### 3.1 Environment Setup Tools

#### **A. Virtualization Platform**

**VirtualBox (Free & Open Source)**
```bash
# Download dari: https://www.virtualbox.org/wiki/Downloads
# Install & jalankan
```

**VMware Workstation Pro (Commercial)**
```
# Download dari: https://www.vmware.com/products/workstation/workstation-pro.html
# Install & jalankan
```

**Keunggulan:**
- VirtualBox: Gratis, cross-platform
- VMware: Performance lebih baik, snapshot lebih cepat

---

#### **B. Linux Distributions untuk Security**

**Kali Linux (Recommended untuk Offensive)**
```bash
# Download ISO: https://www.kali.org/downloads/
# Spesialisasi: Penetration Testing & Ethical Hacking
# Tools Pre-installed: nmap, Burp, Metasploit, Wireshark, dll
# Desktop Environment: XFCE/Gnome
```

**Ubuntu (Recommended untuk Defensive & General)**
```bash
# Download ISO: https://ubuntu.com/download
# Spesialisasi: General purpose server & desktop
# Tools harus di-install manual
# Desktop Environment: GNOME
```

---

### 3.2 Linux Foundation Commands (Essential)

#### **A. File & Directory Management Commands**

**Penjelasan dan Contoh Praktis:**

```bash
# ===== LISTING & NAVIGASI =====

$ pwd
# Print Working Directory - Menampilkan lokasi folder saat ini
# Contoh output: /home/kali/lab_security
# Gunakan untuk: Cek lokasi Anda di tree struktur folder

$ ls
# List - Menampilkan file & folder di direktori saat ini
# Contoh: Documents Downloads Pictures target_list.txt

$ ls -la
# List All - Menampilkan semua file dengan detail (termasuk hidden files)
# Format: [permissions] [owner] [group] [size] [date] [filename]
# Contoh: -rw-r--r-- kali kali 1024 Jan 15 10:30 target_list.txt
# Gunakan untuk: Melihat permissions, owner, ukuran file

$ ls -lh
# List dengan size readable - Ukuran ditampilkan dalam MB/GB bukan bytes
# Contoh: -rw-r--r-- kali kali 1.5M Jan 15 10:30 wordlist.txt
# Gunakan untuk: Melihat ukuran file dengan mudah

$ cd /path/to/directory
# Change Directory - Pindah ke direktori lain
# Contoh: cd /home/kali/Documents
# Gunakan untuk: Navigate ke folder yang diinginkan

$ cd ..
# Pindah ke parent directory (folder level di atas)
# Contoh: Dari /home/kali/Documents → /home/kali

$ cd ~
# Pindah ke home directory user
# Contoh: Dari /root/tools → /home/kali

$ cd -
# Pindah ke direktori sebelumnya
# Contoh: Dari /home/kali/lab → kembali ke /root/security


# ===== CREATE & DELETE =====

$ mkdir folder_name
# Make Directory - Membuat folder baru
# Contoh: mkdir lab_security
# Hasil: Folder "lab_security" tercipta

$ mkdir -p path/to/nested/folder
# Membuat nested folder (multiple levels sekaligus)
# Contoh: mkdir -p lab_security/scans/results
# Hasil: Semua folder dalam path tercipta

$ touch filename.txt
# Create empty file - Membuat file kosong
# Contoh: touch report.txt
# Gunakan untuk: Membuat file sebelum di-edit

$ rm filename
# Remove - Menghapus file
# Contoh: rm old_report.txt
# ⚠️ WARNING: Tidak bisa di-undo! Gunakan hati-hati

$ rm -r folder_name
# Remove Recursively - Menghapus folder & semua isinya
# Contoh: rm -r /tmp/cache
# ⚠️ DANGER: Hapus semua file dalam folder tanpa warning!

$ rmdir folder_name
# Remove empty Directory - Hapus folder kosong SAJA
# Contoh: rmdir empty_folder
# Berbeda dari rm -r: Hanya bisa hapus folder kosong


# ===== COPY & MOVE =====

$ cp source destination
# Copy - Menyalin file
# Contoh: cp wordlist.txt wordlist_backup.txt
# Hasil: Duplikat file dengan nama baru

$ cp -r source_folder destination
# Copy Recursively - Menyalin folder & semua isinya
# Contoh: cp -r /home/kali/lab /tmp/lab_backup
# Gunakan untuk: Backup folder dengan struktur

$ mv source destination
# Move/Rename - Memindahkan atau rename file
# Contoh 1 (rename): mv old_name.txt new_name.txt
# Contoh 2 (move): mv report.txt /home/kali/documents/
# Gunakan untuk: Organize files atau rename batch


# ===== VIEW FILE CONTENT =====

$ cat filename
# Concatenate - Menampilkan seluruh isi file
# Contoh: cat /etc/passwd
# Output: Semua baris file ditampilkan sekaligus
# Gunakan untuk: File kecil (< 50 lines)

$ less filename
# View dengan pagination - Bisa scroll up/down
# Contoh: less /var/log/auth.log
# Navigasi: Space=next page, b=prev page, q=quit, /=search
# Gunakan untuk: File besar atau log files

$ head -n 20 filename
# Show first N lines - Menampilkan 20 baris pertama
# Contoh: head -n 20 wordlist.txt
# Gunakan untuk: Preview file besar

$ tail -n 20 filename
# Show last N lines - Menampilkan 20 baris akhir
# Contoh: tail -n 100 /var/log/syslog
# Gunakan untuk: Lihat log terbaru

$ tail -f filename
# Follow mode - Monitor file real-time (terus-menerus)
# Contoh: tail -f /var/log/auth.log
# Gunakan untuk: Monitor log active (q=quit)


# ===== EDIT FILE =====

$ nano filename
# Nano editor - Text editor simple untuk CLI
# Interface: Ctrl+O=Save, Ctrl+X=Exit, Ctrl+K=Cut, Ctrl+U=Paste
# Gunakan untuk: Edit file dengan mudah (user-friendly)

$ vi filename
atau
$ vim filename
# Vi/Vim editor - Powerful text editor (steep learning curve)
# Mode: Press 'i' to insert, 'Esc' to exit edit, ':wq' to save+quit
# Gunakan untuk: Advanced editing (powerusers)
```

**Contoh Praktis Sehari-hari:**

```bash
# Skenario 1: Setup lab directory
$ mkdir -p ~/lab_security/scans
$ cd ~/lab_security
$ pwd
# Output: /home/kali/lab_security

# Skenario 2: Membuat & edit file
$ touch report.txt
$ nano report.txt
# Edit isi file → Ctrl+O (save) → Ctrl+X (exit)

$ cat report.txt
# Lihat isi yang baru disimpan

# Skenario 3: Backup & organize
$ cp report.txt report_backup.txt
$ mkdir archive
$ mv report_backup.txt archive/
$ ls -la
# Lihat semua file dengan detail
```

---

#### **B. Text Processing & Searching Commands (Cheatsheet)**

**Penjelasan dan Contoh Praktis:**

```bash
# ===== GREP - Search text pattern =====

$ grep "pattern" filename
# Grep - Cari baris yang mengandung pattern
# Contoh: grep "admin" /etc/passwd
# Hasil: Semua baris yang mengandung kata "admin"

$ grep -i "PATTERN" filename
# Case-insensitive - Tidak peduli uppercase/lowercase
# Contoh: grep -i "error" /var/log/syslog
# Hasil: "Error", "ERROR", "error" semuanya ditemukan

$ grep -v "pattern" filename
# Invert match - Tampilkan baris yang TIDAK mengandung pattern
# Contoh: grep -v "^#" config.txt
# Hasil: Semua baris kecuali comment (dimulai dengan #)

$ grep -n "pattern" filename
# Show line numbers - Tampilkan nomor baris juga
# Contoh: grep -n "failed" auth.log
# Hasil: 42:Jan 15 10:30:05 failed login attempt

$ grep -c "pattern" filename
# Count matches - Hitung berapa banyak baris cocok
# Contoh: grep -c "error" syslog
# Hasil: 25 (ada 25 baris dengan kata "error")

$ grep -E "pattern1|pattern2" filename
# Extended regex - Multiple pattern sekaligus
# Contoh: grep -E "error|warning|failed" logfile
# Hasil: Baris dengan salah satu dari 3 pattern

$ command | grep "pattern"
# Pipe - Cari dalam output command lain
# Contoh: ps aux | grep sshd
# Hasil: Proses yang namanya mengandung "sshd"


# ===== CUT - Extract columns/fields =====

$ cut -d: -f1 /etc/passwd
# Cut delimiter & field - Extract kolom spesifik
# -d: = delimiter adalah colon (:)
# -f1 = ambil field ke-1
# Contoh output: root, daemon, bin, sys, ...
# Gunakan untuk: Extract username dari /etc/passwd

$ cut -d: -f1,5 /etc/passwd
# Multiple fields - Ambil field 1 dan 5
# Contoh output: root:root, bin:bin, ...

$ cut -c1-5 filename
# Character range - Ambil character 1-5 dari setiap baris
# Contoh: cut -c1-3 /etc/hostname
# Gunakan untuk: Extract substring dengan posisi tertentu


# ===== AWK - Pattern scanning & processing =====

$ awk '{print $1}' filename
# Print field pertama dari setiap baris
# Contoh: awk '{print $1}' /var/log/auth.log
# Hasil: First column dari setiap baris log

$ awk -F: '{print $1,$3}' /etc/passwd
# Dengan delimiter - Extract multiple fields
# -F: = field separator adalah colon
# Contoh: root, 0 (username dan UID)

$ awk '{print NR, $0}' filename
# Add line numbers - NR = baris ke berapa
# Contoh: 1 first line, 2 second line, ...

$ awk '{sum+=$1} END {print sum}' filename
# Sum/Calculate - Jumlahkan semua nilai di field 1
# Gunakan untuk: Quick math pada kolom

$ awk '$3 > 1000 {print $1, $3}' filename
# Conditional - Tampilkan field 1 & 3 jika field 3 > 1000
# Gunakan untuk: Filter data berdasarkan kondisi


# ===== SED - Stream editor (find & replace) =====

$ sed 's/old/new/g' filename
# Substitute - Ganti "old" dengan "new"
# g = ganti semua occurrences di setiap baris
# Contoh: sed 's/192.168.1/10.0.0/g' ips.txt
# CATATAN: Ini tidak mengubah file original, hanya output

$ sed -i 's/old/new/g' filename
# In-place edit - Langsung edit file original
# CAUTION: Edit permanent!
# Contoh: sed -i 's/example.com/newdomain.com/g' config.conf

$ sed '5d' filename
# Delete line - Hapus baris ke-5
# Contoh: sed '1,10d' logfile (hapus baris 1-10)

$ sed -n '10,20p' filename
# Print range - Tampilkan hanya baris 10-20
# Contoh: sed -n '1,5p' /var/log/auth.log


# ===== SORT, UNIQ, WC =====

$ sort filename
# Sort - Mengurutkan baris
# Contoh: sort wordlist.txt (A-Z)

$ sort -u filename
# Sort unique - Urutkan dan hapus duplikat
# Contoh: sort -u ip_list.txt

$ uniq filename
# Unique - Hapus duplicate baris (harus sorted terlebih dahulu)
# Contoh: sort data.txt | uniq

$ wc -l filename
# Word count lines - Hitung jumlah baris
# Contoh: wc -l /var/log/auth.log
# Hasil: 5432 /var/log/auth.log

$ wc -w filename
# Count words - Hitung jumlah kata

$ wc -c filename
# Count bytes - Hitung ukuran file


# ===== COMBINING COMMANDS (Pipeline) =====

$ cat wordlist.txt | grep -v "^#" | sort -u | wc -l
# Remove comments → Sort unique → Count lines
# Pipeline = Gunakan output satu command sebagai input command berikutnya

$ ps aux | grep sshd | grep -v grep | awk '{print $2}'
# Find process → Filter → Remove grep itself → Extract PID

$ tail -f /var/log/auth.log | grep "failed"
# Monitor log real-time & filter hanya yang ada "failed"
```

**Praktik Quick:**

```bash
# Contoh 1: Extract username dari /etc/passwd
$ grep "bash" /etc/passwd | cut -d: -f1

# Contoh 2: Count berapa user di sistem
$ wc -l /etc/passwd

# Contoh 3: Find file terbesar di directory
$ ls -la | sort -k5 -nr | head -5

# Contoh 4: Extract IP addresses dari log
$ grep "connection" access.log | awk '{print $1}' | sort -u

# Contoh 5: Find & replace di banyak file
$ find . -type f -name "*.conf" -exec sed -i 's/old/new/g' {} \;
```

---

#### **C. User & Permission Management**

```bash
# User management
$ whoami                      # Show current user
$ id                          # Show user ID & groups
$ sudo -l                     # List sudo privileges
$ su - username               # Switch user
$ sudo command                # Run command with sudo

# Permission management (chmod)
$ chmod 755 file              # rwxr-xr-x (user full, others read+execute)
$ chmod 644 file              # rw-r--r-- (user read+write, others read)
$ chmod +x script.sh          # Add execute permission
$ chmod -w file               # Remove write permission

# Ownership
$ chown user:group file       # Change file owner & group
$ chown -R user:group folder  # Recursively change ownership

# Permission notation:
# r (read) = 4
# w (write) = 2
# x (execute) = 1
# user:group:others
# Example: 755 = 7(user=rwx)+5(group=rx)+5(others=rx)
```

**Example:**
```bash
$ ls -la sensitive_file.txt
# -rw------- root root      # Hanya owner bisa baca/tulis (600)

$ chmod 644 sensitive_file.txt
$ ls -la sensitive_file.txt
# -rw-r--r-- root root      # Owner baca/tulis, others hanya baca
```

---

#### **C. Process Management**

```bash
# Lihat processes
$ ps                          # Proses di terminal saat ini
$ ps aux                      # Semua proses dengan detail
$ ps aux | grep process_name  # Filter process tertentu
$ pgrep process_name          # Find PID by process name

# Process monitoring (realtime)
$ top                         # Monitor CPU, Memory, Processes
$ htop                        # Top dengan interface lebih baik (install dulu)
$ watch -n 1 'ps aux'         # Monitor ps output setiap 1 detik

# Kill/stop processes
$ kill PID                    # Terminate process
$ kill -9 PID                 # Force kill process
$ killall process_name        # Kill semua proses dengan nama sama
$ Ctrl + C                    # Interrupt running process di terminal
```

**Example:**
```bash
$ ps aux | grep apache2
# Lihat Apache processes

$ kill -9 12345
# Force terminate process dengan PID 12345
```

---

#### **D. Network Commands (Networking Basics)**

```bash
# IP & Network info
$ ifconfig                    # Show network interfaces (legacy)
$ ip addr show                # Show IP addresses (modern)
$ ip route show               # Show routing table
$ netstat -an                 # Show active connections
$ ss -an                      # Show sockets (netstat replacement)

# DNS & Hostname
$ hostname                    # Show hostname
$ nslookup domain.com         # Query DNS (Windows & Unix)
$ dig domain.com              # Query DNS dengan detail (Unix)
$ ping IP_or_domain           # Test connectivity

# Port & connectivity
$ netstat -tuln               # Show listening ports
$ ss -tuln                    # Show listening ports (modern)
$ nc -zv IP port              # Test port connectivity (netcat)
$ telnet IP port              # Connect to port (telnet)

# Traffic capture
$ tcpdump -i eth0 -n          # Capture network traffic
$ tcpdump -i eth0 -n 'tcp port 80'  # Capture HTTP traffic
```

**Example:**
```bash
$ ip addr show
# Lihat IP address semua interface

$ netstat -tuln | grep LISTEN
# Lihat semua port yang listening

$ dig google.com
# Query DNS untuk google.com
```

---

#### **E. Logging & System Info**

```bash
# System information
$ uname -a                    # Show system info
$ cat /etc/os-release         # Show OS info
$ uptime                      # Show uptime & load average
$ free -h                     # Show memory usage

# Logging
$ journalctl -xe              # Show journal/system logs
$ tail -f /var/log/syslog     # Follow system log real-time
$ tail -f /var/log/auth.log   # Follow auth log
$ dmesg                       # Show kernel messages
$ last                        # Show last login history
$ lastlog                     # Show last login for all users
$ history                     # Show command history
```

**Example:**
```bash
$ journalctl -xe --priority=err
# Show error logs

$ tail -f /var/log/auth.log
# Monitor authentication attempts
```

---

### 3.3 Security-Specific Tools

#### **A. Port Scanning (nmap)**

```bash
# Basic syntax
$ nmap [OPTIONS] [TARGET]

# Common scans
$ nmap -sn 192.168.1.0/24        # Ping sweep (find live hosts)
$ nmap IP                         # Basic scan (1000 common ports)
$ nmap -p- IP                     # Scan all ports
$ nmap -p 22,80,443 IP            # Scan specific ports
$ nmap -sV IP                     # Detect service versions
$ nmap -O IP                      # OS detection
$ nmap -sV -O -A IP               # Comprehensive scan
$ nmap -Pn IP                     # Skip ping (treat all as up)

# Output options
$ nmap -oN output.txt IP          # Normal output to file
$ nmap -oX output.xml IP          # XML output
$ nmap -oG output.grep IP         # Greppable output
$ nmap -oA output IP              # All formats

# Speed & timing
$ nmap -T0 IP                     # Paranoid (very slow)
$ nmap -T3 IP                     # Normal (default)
$ nmap -T5 IP                     # Insane (very fast)
```

**Example:**
```bash
$ nmap -sn 192.168.1.0/24
# Host discovery di subnet

$ nmap -sV -p 22,80,443 192.168.1.100
# Detect version di port SSH, HTTP, HTTPS
```

---

#### **B. Network Monitoring (Wireshark/tcpdump)**

```bash
# tcpdump (command line packet capture)
$ sudo tcpdump -i eth0                    # Capture interface eth0
$ sudo tcpdump -i eth0 -n                 # -n = no DNS resolution
$ sudo tcpdump -i eth0 'tcp port 80'      # Capture HTTP only
$ sudo tcpdump -i eth0 -w capture.pcap    # Save to file
$ sudo tcpdump -i eth0 -r capture.pcap    # Read from file

# Wireshark (GUI packet analyzer)
$ wireshark                               # Launch GUI
# GUI-based: File → Open capture file → Analyze packets
# Filters: tcp.port == 80, http, dns, etc.
```

**Example:**
```bash
$ sudo tcpdump -i eth0 -n 'tcp port 22' -w ssh_traffic.pcap
# Capture SSH traffic dan simpan ke file
```

---

#### **C. SSH (Secure Shell)**

```bash
# SSH client
$ ssh username@IP                         # Connect to remote host
$ ssh -p 2222 username@IP                 # Connect ke port custom
$ ssh -i /path/to/key username@IP         # Connect dengan private key

# SSH key generation
$ ssh-keygen -t rsa -b 4096               # Generate RSA keypair
$ ssh-keygen -t ed25519                   # Generate EdDSA keypair (modern)

# Copy key to server
$ ssh-copy-id -i ~/.ssh/id_rsa.pub username@IP  # Install public key

# SSH tips
$ ssh username@IP 'command'               # Execute command via SSH
$ scp file username@IP:/path/              # Copy file via SSH
$ scp -r folder username@IP:/path/         # Copy folder via SSH
```

**Example:**
```bash
$ ssh-keygen -t rsa -b 4096
# Generate key, simpan di ~/.ssh/

$ ssh-copy-id -i ~/.ssh/id_rsa.pub admin@192.168.1.100
# Install public key ke server

$ ssh admin@192.168.1.100
# Connect tanpa password (key-based auth)
```

---

### 3.3 LINUX OPERATORS & REDIRECTION (I/O STREAMS)

**Redirection operators untuk mengolah input/output streams:**

#### **A. Input/Output Redirection**

| Operator | Nama | Fungsi | Contoh |
|----------|------|--------|--------|
| `>` | Redirect stdout | Kirim output ke file (overwrite) | `command > file.txt` |
| `>>` | Append stdout | Tambah output ke akhir file | `command >> file.txt` |
| `2>` | Redirect stderr | Kirim error messages ke file | `command 2> errors.txt` |
| `2>>` | Append stderr | Tambah errors ke akhir file | `command 2>> errors.txt` |
| `&>` | Redirect semua | Kirim stdout & stderr ke file | `command &> output.txt` |
| `>&2` | Redirect to stderr | Kirim stdout sebagai stderr | `echo "Error" >&2` |
| `>/dev/null` | Discard output | Buang output (null device) | `command >/dev/null 2>&1` |
| `<` | Redirect stdin | Baca input dari file | `command < input.txt` |
| `<<` | Heredoc | Input multi-line | `cat << EOF ... EOF` |

**Contoh Praktis:**
```bash
# Simpan output ke file (overwrite)
$ nmap 192.168.1.0/24 > scan_results.txt

# Tambah output ke akhir file
$ echo "Scan completed at $(date)" >> scan_results.txt

# Pisahkan stdout & stderr
$ command > success.log 2> error.log

# Kombinasi: stdout & stderr ke file yang sama
$ ./script.sh &> combined_log.txt

# Buang semua output (silent mode)
$ command >/dev/null 2>&1

# Baca dari file sebagai input
$ sort < unsorted_ips.txt > sorted_ips.txt

# Multi-line input (Heredoc)
$ cat << EOF > config.txt
IP: 192.168.1.1
PORT: 22
USER: admin
EOF
```

---

#### **B. Piping & Command Chaining**

| Operator | Nama | Fungsi | Contoh |
|----------|------|--------|--------|
| `\|` | Pipe | Kirim output satu command ke input command lain | `command1 \| command2` |
| `&` | Background | Jalankan command di background | `command &` |
| `&&` | AND operator | Jalankan command2 jika command1 sukses | `cmd1 && cmd2` |
| `\|\|` | OR operator | Jalankan command2 jika command1 gagal | `cmd1 \|\| cmd2` |
| `;` | Separator | Jalankan commands secara sequential | `cmd1; cmd2; cmd3` |

**Contoh Praktis:**
```bash
# Pipe: cari "LISTEN" dalam netstat output
$ netstat -tlnp | grep LISTEN

# Chain multiple pipes: Extract, sort, count
$ cat access.log | grep "ERROR" | sort | uniq -c

# Background execution: jalankan scanning sambil bisa ketik
$ nmap -p- 192.168.1.1 > scan.txt &

# AND operator: jalankan command2 jika command1 sukses
$ cd /path/to/project && ./build.sh && echo "Build successful!"

# OR operator: fallback jika command1 gagal
$ ping -c 1 8.8.8.8 || echo "Internet connection failed"

# Sequential execution: jalankan berurutan
$ echo "Starting scan..."; nmap target.com; echo "Scan done"; echo "Results saved"

# Complex chain: Find + analyze + filter + count
$ find /var/log -name "*.log" | xargs grep "CRITICAL" | wc -l
```

---

### 3.4 LINUX COMMAND STRUCTURE & SYNTAX

**Kerangka umum Linux command:**

```bash
command [options/flags] [arguments/paths]

Contoh breakdown:
$ grep -r "password" /var/www --color
   ↑    ↑                 ↑         ↑
  cmd  flags           argument  option
```

**Komponen:**
- **command**: Program yang dijalankan (grep, nmap, find, dll)
- **flags/options**: Modifikasi perilaku command (biasanya dimulai dengan `-` atau `--`)
  - Short flag: `-h` (single character)
  - Long flag: `--help` (multiple characters)
- **arguments**: Input data untuk command (file path, target, search term)

**Mendapatkan Help:**
```bash
# Display help information
$ command --help

# Manual pages (detailed documentation)
$ man command

# Contoh:
$ grep --help
$ man grep

# Search manual pages
$ man -k "file" | grep -i search
```

---

### 3.5 BASH SCRIPTING FUNDAMENTALS

**Script adalah collection of commands yang di-save dalam file untuk reusability & automation.**

#### **A. Script Structure Dasar**

```bash
#!/bin/bash
# Shebang: Mendeklarasikan interpreter (bash)
# Baris dengan # adalah comment

# ===== VARIABLES =====
username="kali"
ip_target="192.168.1.100"
current_date=$(date +%Y-%m-%d)

# ===== FUNCTION =====
scan_target() {
  echo "[*] Scanning $ip_target..."
  nmap -p- -sV $ip_target -o scan_$current_date.txt
  echo "[+] Scan complete"
}

# ===== MAIN EXECUTION =====
echo "Security Assessment Tool"
scan_target
```

#### **B. Variables & Substitution**

```bash
# Variable assignment (no spaces around =)
name="John"
port=22
result=$?  # Exit code dari command sebelumnya

# Variable expansion (access dengan $)
echo "Name: $name"
echo "Port: ${port}"

# Command substitution (jalankan command, capture output)
current_user=$(whoami)
timestamp=$(date +%s)
line_count=$(wc -l < file.txt)

# Special variables dalam script
$0   # Nama script sendiri
$1   # First argument
$2   # Second argument
$@   # Semua arguments sebagai array
$#   # Jumlah arguments
$?   # Exit code dari command terakhir
$$   # PID dari script
```

**Contoh:**
```bash
#!/bin/bash
# Script dengan arguments

echo "Script name: $0"
echo "First arg: $1"
echo "Second arg: $2"
echo "All args: $@"
echo "Total args: $#"

# Usage: ./script.sh apple banana cherry
# Output:
# Script name: ./script.sh
# First arg: apple
# Second arg: banana
# All args: apple banana cherry
# Total args: 3
```

#### **C. Conditional Statements (if/else)**

```bash
# Basic if statement
if [ condition ]; then
  # code jika true
fi

# if-else
if [ condition ]; then
  # code jika true
else
  # code jika false
fi

# if-elif-else
if [ $? -eq 0 ]; then
  echo "Success"
elif [ $? -eq 1 ]; then
  echo "Error 1"
else
  echo "Other error"
fi
```

**Test Conditions:**

| Operator | Fungsi | Contoh |
|----------|--------|--------|
| `-eq` | Equal | `[ $count -eq 5 ]` |
| `-ne` | Not equal | `[ $status -ne 0 ]` |
| `-lt` | Less than | `[ $age -lt 18 ]` |
| `-le` | Less or equal | `[ $port -le 65535 ]` |
| `-gt` | Greater than | `[ $size -gt 1000 ]` |
| `-ge` | Greater or equal | `[ $memory -ge 4096 ]` |
| `-z` | String is empty | `[ -z "$var" ]` |
| `-n` | String not empty | `[ -n "$var" ]` |
| `=` | String equal | `[ "$name" = "admin" ]` |
| `!=` | String not equal | `[ "$user" != "root" ]` |
| `-f` | File exists | `[ -f "/var/log/auth.log" ]` |
| `-d` | Directory exists | `[ -d "/home/kali" ]` |
| `-r` | File readable | `[ -r "$file" ]` |
| `-w` | File writable | `[ -w "$file" ]` |
| `-x` | File executable | `[ -x "$script" ]` |

**Contoh Praktis:**
```bash
#!/bin/bash
# Check if file exists
if [ -f "scan_results.txt" ]; then
  echo "Scan results found"
  cat scan_results.txt
else
  echo "No scan results"
fi

# Check if argument provided
if [ $# -lt 1 ]; then
  echo "Usage: $0 <target_ip>"
  exit 1
fi

# Check command success
if nmap $1 > /dev/null 2>&1; then
  echo "Target $1 is reachable"
else
  echo "Target $1 is not reachable"
fi
```

#### **D. Loops (for & while)**

**For Loop - Iterasi melalui list/range:**
```bash
# Loop through items
for item in apple banana cherry; do
  echo "Processing: $item"
done

# Loop through array
servers=("web1" "web2" "web3")
for server in "${servers[@]}"; do
  ping -c 1 $server
done

# Loop dengan C-style
for ((i=1; i<=10; i++)); do
  echo "Number: $i"
done

# Loop through files
for file in *.log; do
  echo "Analyzing $file"
  grep "ERROR" "$file"
done

# Loop through command output
for line in $(cat targets.txt); do
  nmap -p 22 $line
done
```

**While Loop - Iterasi selama kondisi true:**
```bash
# Basic while loop
count=1
while [ $count -le 10 ]; do
  echo "Count: $count"
  count=$((count + 1))
done

# Read lines dari file
while read line; do
  echo "IP: $line"
  ping -c 1 $line
done < targets.txt

# Infinite loop (gunakan hati-hati!)
# while true; do
#   ping target.com
#   sleep 5
# done
```

#### **E. Case Statement (Switch)**

```bash
case $variable in
  pattern1)
    # code jika match pattern1
    ;;
  pattern2)
    # code jika match pattern2
    ;;
  *)
    # default case
    ;;
esac
```

**Contoh Praktis:**
```bash
#!/bin/bash

echo "Security Tools Menu"
echo "1. Port scanning"
echo "2. Vulnerability scan"
echo "3. Analysis log"
read -p "Choose option: " option

case $option in
  1)
    echo "Running nmap..."
    nmap -p- $1
    ;;
  2)
    echo "Running vulnerability scan..."
    openvas scan $1
    ;;
  3)
    echo "Analyzing logs..."
    grep "ERROR" /var/log/secure
    ;;
  *)
    echo "Invalid option"
    ;;
esac
```

#### **F. Read Input dari User**

```bash
# Simple read
read variable_name
# User types input → simpan ke $variable_name

# Read dengan prompt
read -p "Enter target IP: " target_ip

# Read tanpa echo (password prompt)
read -sp "Enter password: " password

# Read multiple values
read -p "Enter name age city: " name age city

# Read dari file/stdin
while read line; do
  echo "Processing: $line"
done < targets.txt
```

**Contoh:**
```bash
#!/bin/bash

read -p "Enter scan type (quick/full): " scan_type
read -p "Enter target IP: " target

if [ "$scan_type" = "quick" ]; then
  nmap -F $target
elif [ "$scan_type" = "full" ]; then
  nmap -p- -sV -sC $target
fi
```

---

### 3.6 REGULAR EXPRESSIONS & PATTERN MATCHING

#### **A. POSIX Pattern Matching (glob patterns)**

```bash
# Wildcard patterns
*           # Match any characters (banyak)
?           # Match single character
[abc]       # Match a, b, atau c
[a-z]       # Match any character a to z
[!abc]      # Match anything EXCEPT a, b, c
[0-9]       # Match digits

# Contoh:
ls *.txt         # Semua file .txt
ls test?.log     # test1.log, test2.log, testa.log
ls [0-9]*.txt    # Files dimulai dengan digit
rm -r [!keep]*   # Delete semua except "keep"
```

#### **B. Regular Expressions (regex)**

Used dalam commands seperti `grep`, `sed`, `awk`, `perl`:

| Pattern | Fungsi | Contoh |
|---------|--------|--------|
| `.` | Match any single character | `a.c` matches `abc`, `adc` |
| `*` | Match 0 atau lebih | `ab*c` matches `ac`, `abc`, `abbc` |
| `^` | Start of line | `^Error` matches lines starting with Error |
| `$` | End of line | `error$` matches lines ending with error |
| `[ ]` | Character class | `[0-9]` matches any digit |
| `[^ ]` | Negated class | `[^0-9]` matches non-digit |
| `\|` | OR operator | `cat\|dog` matches cat atau dog |
| `( )` | Grouping | `(ab)+` matches ab, abab, ababab |
| `?` | 0 atau 1 occurrence | `colou?r` matches color, colour |
| `+` | 1 atau lebih | `[0-9]+` matches 1, 12, 123 |
| `{n,m}` | n to m occurrences | `a{2,4}` matches aa, aaa, aaaa |

**Contoh Regex:**
```bash
# Find lines with IP addresses
grep "^[0-9]\{1,3\}\.[0-9]\{1,3\}" access.log

# Extract email addresses
grep -oE "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" data.txt

# Find failed login attempts
grep "failed password\|invalid user" /var/log/auth.log

# Match phone numbers
grep -E "[0-9]{3}-[0-9]{3}-[0-9]{4}" contacts.txt

# Find ports in netstat
netstat -tlnp | grep -oE ":[0-9]+" | sort | uniq
```

---

### 3.7 TEXT PROCESSING & LOG ANALYSIS COMMANDS

**Untuk mengolah log files, configuration files, dan data:**

```bash
# ===== grep: Search untuk pattern =====
grep "ERROR" /var/log/syslog           # Find "ERROR" dalam file
grep -i "error" file.txt               # Case-insensitive search
grep -v "debug" log.txt                # Exclude lines dengan "debug"
grep -r "password" /etc/               # Recursive search di folder
grep -n "CRITICAL" alert.log           # Show line numbers
grep -c "warning" system.log           # Count matching lines
grep "2024-01-" access.log | wc -l     # Count logs dari Jan 2024

# ===== sed: Stream editor (search & replace) =====
sed 's/old/new/' file.txt              # Replace first "old" per line
sed 's/old/new/g' file.txt             # Replace all "old" per line
sed -i 's/old/new/g' file.txt          # Replace in-place (modify file)
sed '5d' file.txt                       # Delete line 5
sed '1,5d' file.txt                    # Delete lines 1-5
sed -n '10,20p' file.txt               # Print lines 10-20

# ===== awk: Data processing & formatting =====
awk '{print $1}' access.log             # Print first column
awk '{print $1, $3}' data.txt           # Print columns 1 & 3
awk -F: '{print $1}' /etc/passwd        # Use : as delimiter
awk '{sum+=$2} END {print sum}' numbers.txt  # Sum column 2
awk '$2 > 100' data.txt                 # Print lines where column 2 > 100
netstat -tlnp | awk '{print $4}' | sort | uniq  # Extract & sort ports

# ===== cut: Extract columns =====
cut -d: -f1 /etc/passwd                 # Extract usernames
cut -d' ' -f2 access.log                # Extract 2nd field (space-delimited)
cut -c1-10 file.txt                     # Extract chars 1-10

# ===== sort: Sorting & unique =====
sort file.txt                           # Sort alphabetically
sort -n file.txt                        # Numeric sort
sort -rn file.txt                       # Reverse numeric sort
sort -u file.txt                        # Sort & remove duplicates
uniq file.txt                           # Remove consecutive duplicates

# ===== wc: Word/line/char count =====
wc -l file.txt                          # Count lines
wc -w file.txt                          # Count words
wc -c file.txt                          # Count bytes

# ===== head & tail =====
head -5 file.txt                        # Show first 5 lines
tail -10 file.txt                       # Show last 10 lines
tail -f log.txt                         # Follow log file (real-time)

# ===== cat & paste =====
cat file.txt                            # Display file contents
cat > file.txt << EOF ... EOF           # Create file with content
cat file1.txt file2.txt                 # Concatenate files
paste file1.txt file2.txt               # Merge files side-by-side
```

**Real-World Examples untuk Log Analysis:**
```bash
# Extract unique IPs dari access log
cat access.log | awk '{print $1}' | sort | uniq

# Count requests per IP
cat access.log | awk '{print $1}' | sort | uniq -c | sort -rn

# Find failed SSH attempts dengan timestamps
grep "Failed password" /var/log/auth.log | grep "sshd" | tail -20

# Count errors by type
grep "ERROR" app.log | awk -F: '{print $2}' | sort | uniq -c

# Monitor real-time logs
tail -f /var/log/syslog | grep "error\|warning\|critical"

# Extract & count top request paths
cat access.log | awk '{print $7}' | sort | uniq -c | sort -rn | head -10
```

---

### 3.8 FILE SEARCH & LOCATE

```bash
# ===== find: Powerful file search =====
find /home -name "*.txt"                # Find all .txt files
find /home -name "*password*"           # Find files dengan "password" di nama
find / -size +100M                      # Find files > 100MB
find / -size -10M                       # Find files < 10MB
find /var/log -mtime -7                 # Modified dalam 7 hari terakhir
find /var/log -atime -3                 # Accessed dalam 3 hari terakhir
find / -type f -perm 777                # Find files dengan permissions 777
find / -user admin                      # Find files owned by "admin"
find / -group wheel                     # Find files in "wheel" group
find / -type d -name "backup"           # Find directories named "backup"

# Combine find dengan actions
find /var/log -name "*.log" -exec rm {} \;    # Delete all .log files
find / -type f -name "*.tmp" -delete          # Delete temp files
find . -name "*.py" -exec grep -l "password" {} \;  # Find Python files with "password"

# ===== locate: Fast database search =====
updatedb                                # Update search database
locate apache.conf                      # Quick search
locate "*.conf"                         # Search by pattern
locate -i password                      # Case-insensitive search
locate -c "/var"                        # Count files in /var

# Note: find lebih comprehensive, locate lebih cepat tapi hanya db
```

---

### 3.9 SCHEDULING TASKS: CRON & AT

#### **A. Crontab (Scheduling recurring tasks)**

```bash
# Edit crontab untuk current user
crontab -e

# View crontab entries
crontab -l

# Remove crontab
crontab -r

# Edit crontab untuk user lain (as root)
crontab -u username -e
```

**Crontab Format:**
```
# ┌───────────── minute (0-59)
# │ ┌───────────── hour (0-23)
# │ │ ┌───────────── day of month (1-31)
# │ │ │ ┌───────────── month (1-12)
# │ │ │ │ ┌───────────── day of week (0-7) [0 & 7 = Sunday]
# │ │ │ │ │
# * * * * * command to execute

# Examples:
0 0 * * *   /home/kali/backup.sh         # Daily at midnight
30 2 * * 0  /usr/bin/full-scan.sh        # Weekly Sunday 2:30 AM
0 * * * *   /home/kali/monitor.sh        # Every hour
*/15 * * * * /home/kali/check-logs.sh    # Every 15 minutes
0 6 1 * *   /home/kali/monthly-report.sh # 1st of month 6 AM
```

**Contoh Praktis:**
```bash
# Backup every day
0 3 * * * /usr/bin/tar -czf /backup/system-$(date +\%Y\%m\%d).tar.gz /home /etc

# Security scan setiap minggu
0 4 * * 0 /home/kali/security-scan.sh >> /var/log/security-scan.log

# Log cleanup setiap bulan
0 0 1 * * find /var/log -name "*.log" -mtime +30 -delete

# Monitor service status setiap 5 menit
*/5 * * * * systemctl is-active nginx || systemctl start nginx
```

**View cron logs:**
```bash
grep CRON /var/log/syslog         # Ubuntu/Debian
tail -f /var/log/cron             # RedHat/CentOS
```

#### **B. at Command (One-time scheduling)**

```bash
# Schedule command untuk waktu tertentu
at 14:30 tomorrow
at> /home/kali/one-time-scan.sh
at> Ctrl+D (finish)

# Schedule untuk date tertentu
at 10:00 January 25 2025
at> /usr/bin/backup.sh

# List scheduled tasks
atq

# Remove task
atrm 1
```

---

### 3.10 PROCESS & BACKGROUND EXECUTION

```bash
# ===== Run command in background =====
command &                              # Run in background
nohup long-running-command &           # Immune to hangups

# ===== ps: List processes =====
ps aux                                 # All processes
ps aux | grep python                   # Find python processes
ps -ef                                 # Full format

# ===== jobs: List background jobs =====
jobs                                   # List jobs
fg %1                                  # Bring job 1 to foreground
bg %1                                  # Resume job 1 in background
kill %1                                # Kill job 1

# ===== top & htop: Monitor processes =====
top                                    # Interactive process monitor
htop                                   # Better version of top

# ===== kill: Terminate processes =====
kill PID                               # Graceful terminate
kill -9 PID                            # Force kill
pkill -f "process_name"                # Kill by name
killall process_name                   # Kill all instances
```

---

### 3.11 SLEEP & DELAYS

```bash
# Pause execution
sleep 5             # Sleep 5 seconds
sleep 1m            # Sleep 1 minute
sleep 2h            # Sleep 2 hours

# Real example: Repeat command every 5 seconds
while true; do
  nmap -sn 192.168.1.0/24
  sleep 5
done

# Delay dalam script
#!/bin/bash
echo "Starting scan..."
sleep 2
nmap -p- target.com
sleep 1
echo "Scan complete"
```

---

### 3.12 SCREEN & TMUX (Terminal Multiplexing)

#### **A. Screen: Simple terminal multiplexing**

```bash
# Start new screen session
screen -S session_name

# Create new window (inside screen)
Ctrl+A c

# Switch windows
Ctrl+A n           # Next window
Ctrl+A p           # Previous window

# Detach from session (Ctrl+A d)
# Session tetap running di background

# List sessions
screen -ls

# Reattach ke session
screen -r session_name

# Kill session
screen -X -S session_name quit
```

**Practical Example:**
```bash
# Start scanning session
screen -S nmap_scan

# Inside screen, start long scan
nmap -p- -sV 192.168.1.0/24 -o results.txt

# Detach (Ctrl+A d) sambil scan terus berjalan

# Later, reattach
screen -r nmap_scan
```

#### **B. Tmux: Modern alternative**

```bash
# Start new tmux session
tmux new-session -s session_name

# Create new window (Ctrl+B c)
# Switch windows (Ctrl+B n, Ctrl+B p)
# Detach (Ctrl+B d)
# List sessions (tmux list-sessions)
# Attach (tmux attach -t session_name)
```

---

### 3.13 MONITORING & SYSTEM COMMANDS

```bash
# ===== System Information =====
uname -a                # System info
hostnamectl             # Hostname & OS info
uptime                  # System uptime & load
df -h                   # Disk usage
du -sh /path            # Directory size
free -h                 # Memory usage
vmstat                  # Virtual memory stats

# ===== Network Monitoring =====
ifconfig                # Network interfaces
ip addr show            # IP configuration
netstat -tlnp           # Listening ports
ss -tlnp                # Socket statistics
route -n                # Routing table
iptables -L -n          # Firewall rules
nftables list table     # nftables rules

# ===== Service Management =====
systemctl status service_name
systemctl start service_name
systemctl stop service_name
systemctl restart service_name
systemctl enable service_name    # Enable on boot
systemctl disable service_name   # Disable on boot

# ===== User & Permission Management =====
id                      # Current user info
sudo -l                 # Sudo privileges
ls -l                   # File permissions
chmod 755 file          # Change permissions
chown user:group file   # Change ownership
```

---

### 3.14 COMPLETE LINUX COMMAND REFERENCE (Kamus Perintah)

**Comprehensive cheat sheet untuk cybersecurity professionals:**

#### **File Management**
```bash
ls, ls -la, ls -lh      # Listing files
cd, pwd, pushd, popd    # Navigation
mkdir, mkdir -p         # Create directories
touch, cat, echo        # Create/view files
cp, cp -r, mv, rm, rm -r  # Copy, move, delete
chmod 755, chown        # Permissions & ownership
ln -s                   # Symbolic links
tar -czf, tar -xzf      # Compress/extract
zip, unzip              # ZIP archives
find, locate, which     # Search files
```

#### **Text Processing**
```bash
cat, head, tail, tail -f         # View contents
grep, grep -i, grep -v           # Search patterns
sed 's/old/new/g'                # Find & replace
awk, cut, sort, uniq             # Data processing
wc, wc -l                        # Count lines
paste, join                      # Combine files
tr, tr -d                        # Translate/delete chars
```

#### **System Information**
```bash
uname, hostnamectl               # System info
uptime, free, df, du             # Resources
ps, ps aux, top, htop            # Processes
systemctl status/start/stop      # Services
whoami, id, sudo -l              # User info
date, cal, timedatectl           # Date & time
dmesg, journalctl                # Logs
```

#### **Networking**
```bash
ping, traceroute                 # Connectivity
netstat, ss, netstat -tlnp       # Ports & sockets
ifconfig, ip addr                # IP config
route, ip route                  # Routing
iptables, ufw, firewall-cmd      # Firewalls
nmap, nmap -p-, nmap -sV         # Port scanning
tcpdump, Wireshark, tshark       # Packet capture
curl, wget, nc, telnet           # Client tools
```

#### **User & Permissions**
```bash
useradd, userdel, usermod        # User management
groupadd, groupdel, groupmod     # Group management
passwd, passwd -l                # Password management
chmod, chown, chgrp              # Permissions
sudo, su, sudo -i                # Privilege access
id, groups, whoami               # User info
```

#### **Package Management**
```bash
apt, apt-get, apt-cache          # Debian/Ubuntu
yum, dnf                         # RedHat/CentOS
pacman                           # Arch Linux
pip, pip3                        # Python packages
npm, cargo                       # Language-specific
```

#### **Security & Cryptography**
```bash
ssh, ssh-keygen, ssh-copy-id     # SSH
gpg, gpg --encrypt               # GPG encryption
openssl, openssl s_client        # SSL/TLS tools
md5sum, sha256sum                # Checksums
openssl passwd                   # Password hashing
```

#### **Advanced Scripting & Automation**
```bash
bash, sh, ksh, zsh               # Shells
for, while, do...done            # Loops
if, then, else, fi               # Conditionals
function, return                 # Functions
set -x, set -e                   # Debug/error handling
trap, exit                       # Signal handling
```

---

### 3.15 KAMUS LINUX LENGKAP: SEMUA COMMAND & FUNGSINYA

**Comprehensive dictionary dari semua command penting di Linux (berdasarkan /bin, /usr/bin, /sbin, /usr/sbin)**

---

#### **📁 A. FILE & DIRECTORY OPERATIONS**

| Command | Fungsi Singkat |
|---------|----------------|
| `ls` | List directory contents - tampilkan file & folder |
| `cd` | Change directory - pindah folder |
| `pwd` | Print working directory - tampilkan lokasi saat ini |
| `mkdir` | Make directory - buat folder baru |
| `rmdir` | Remove empty directory - hapus folder kosong |
| `rm` | Remove - hapus file/folder |
| `cp` | Copy - copy file/folder |
| `mv` | Move - pindah/rename file/folder |
| `touch` | Create empty file - buat file kosong atau update timestamp |
| `cat` | Concatenate - tampilkan isi file |
| `tac` | Reverse cat - tampilkan file dari bawah ke atas |
| `more` | View file page by page - lihat file per halaman |
| `less` | Better more - lihat file dengan navigation lebih baik |
| `head` | Show first lines - tampilkan baris awal file |
| `tail` | Show last lines - tampilkan baris akhir file |
| `ln` | Link - buat link (shortcut) ke file |
| `readlink` | Read symbolic link - baca target symbolic link |
| `stat` | File status - info detail tentang file |
| `file` | Determine file type - deteksi tipe file |
| `basename` | Strip directory path - ambil nama file saja |
| `dirname` | Extract directory - ambil path directory saja |
| `realpath` | Print resolved path - tampilkan full absolute path |
| `tree` | Display directory tree - tampilkan struktur folder |
| `du` | Disk usage - ukuran file/folder |
| `df` | Disk free - info kapasitas disk |
| `dd` | Data duplicator - copy/convert data low-level |
| `truncate` | Shrink/extend file size - ubah ukuran file |
| `split` | Split file - pecah file besar jadi beberapa bagian |
| `shred` | Secure delete - hapus file secara aman (overwrite) |
| `install` | Copy files & set attributes - copy dengan set permission |
| `mktemp` | Create temporary file - buat file temporary |

---

#### **📝 B. TEXT PROCESSING & MANIPULATION**

| Command | Fungsi Singkat |
|---------|----------------|
| `grep` | Search pattern - cari text dalam file |
| `egrep` | Extended grep - grep dengan regex extended |
| `fgrep` | Fixed grep - grep literal string (faster) |
| `sed` | Stream editor - edit text dengan pattern |
| `awk` | Text processing - proses & format text/data |
| `cut` | Cut columns - potong kolom dari text |
| `paste` | Merge lines - gabung lines dari multiple file |
| `join` | Join files - gabung file berdasarkan field |
| `sort` | Sort lines - urutkan baris |
| `uniq` | Unique lines - hapus duplikat berurutan |
| `tr` | Translate characters - ganti/hapus karakter |
| `wc` | Word count - hitung baris/kata/karakter |
| `diff` | Compare files - bandingkan 2 file |
| `cmp` | Compare bytes - bandingkan binary file |
| `comm` | Compare sorted files - bandingkan file tersorted |
| `patch` | Apply patch - terapkan diff patch ke file |
| `expand` | Convert tabs to spaces - ubah tab jadi spasi |
| `unexpand` | Convert spaces to tabs - ubah spasi jadi tab |
| `fold` | Wrap text - bungkus text ke lebar tertentu |
| `fmt` | Format text - format paragraf |
| `column` | Columnate lists - format output jadi kolom |
| `nl` | Number lines - tambah nomor baris |
| `tee` | Read & write - simpan output ke file sambil print |
| `strings` | Extract printable strings - extract text dari binary |
| `od` | Octal dump - tampilkan file dalam format octal/hex |
| `hexdump` | Hex dump - tampilkan file dalam hexadecimal |
| `xxd` | Hex dump + reverse - convert binary <-> hex |
| `base64` | Base64 encode/decode - encode/decode base64 |
| `md5sum` | MD5 checksum - hitung MD5 hash |
| `sha1sum` | SHA1 checksum - hitung SHA1 hash |
| `sha256sum` | SHA256 checksum - hitung SHA256 hash |
| `iconv` | Convert encoding - konversi encoding file |
| `rev` | Reverse lines - balik karakter per baris |

---

#### **🔧 C. SYSTEM INFORMATION & MONITORING**

| Command | Fungsi Singkat |
|---------|----------------|
| `uname` | System information - info kernel & sistem |
| `hostname` | Show/set hostname - tampilkan/set hostname |
| `hostnamectl` | Control hostname & system settings |
| `uptime` | System uptime - lama sistem running |
| `who` | Who is logged in - siapa saja yang login |
| `w` | Who & what - user login & aktivitas mereka |
| `whoami` | Current user - tampilkan username saat ini |
| `id` | User/group ID - tampilkan UID/GID |
| `last` | Last logins - history login terakhir |
| `lastlog` | Last login time - waktu login terakhir semua user |
| `users` | List logged users - list user yang sedang login |
| `logname` | Print login name - nama user login |
| `date` | Show/set date - tampilkan/set tanggal |
| `cal` | Calendar - tampilkan kalender |
| `timedatectl` | Control time/date - manage timezone & waktu |
| `free` | Memory usage - penggunaan RAM |
| `vmstat` | Virtual memory stats - statistik memory virtual |
| `top` | Process monitor - monitor proses real-time |
| `htop` | Better top - top dengan interface lebih baik |
| `ps` | Process status - list proses berjalan |
| `pgrep` | Process grep - cari proses by name |
| `pidof` | PID of program - cari PID dari program |
| `pstree` | Process tree - tampilkan tree proses |
| `lsof` | List open files - list file yang dibuka proses |
| `fuser` | File user - proses mana yang pakai file |
| `iostat` | I/O statistics - statistik disk I/O |
| `mpstat` | CPU statistics - statistik per CPU |
| `sar` | System activity - collect & report system activity |
| `dmesg` | Kernel messages - pesan dari kernel |
| `journalctl` | Query systemd journal - lihat system logs |
| `lscpu` | CPU information - info detail CPU |
| `lsblk` | List block devices - list disk & partisi |
| `lspci` | List PCI devices - list hardware PCI |
| `lsusb` | List USB devices - list USB devices |
| `lshw` | List hardware - list semua hardware |
| `hwinfo` | Hardware info - info hardware lengkap |
| `dmidecode` | DMI table decoder - info hardware dari BIOS |
| `inxi` | System info - info sistem comprehensive |
| `sensors` | Hardware sensors - suhu CPU/GPU |

---

#### **🌐 D. NETWORK & CONNECTIVITY**

| Command | Fungsi Singkat |
|---------|----------------|
| `ping` | Test connectivity - tes koneksi ke host |
| `ping6` | Ping IPv6 - ping untuk IPv6 |
| `traceroute` | Trace route - lacak jalur paket |
| `tracepath` | Trace path - seperti traceroute tanpa root |
| `mtr` | My traceroute - kombinasi ping + traceroute |
| `ip` | IP management - manage IP, routing, interface |
| `ifconfig` | Interface config - konfigurasi network interface (legacy) |
| `route` | Routing table - tampilkan/set routing table |
| `netstat` | Network statistics - statistik network (legacy) |
| `ss` | Socket statistics - socket statistics (modern) |
| `nslookup` | DNS lookup - query DNS server |
| `dig` | DNS dig - query DNS dengan detail |
| `host` | DNS host - simple DNS lookup |
| `whois` | Domain info - info registrasi domain |
| `curl` | Transfer data - download/upload via URL |
| `wget` | Web get - download file dari web |
| `lynx` | Text browser - browser text-based |
| `nc` | Netcat - network utility serba guna |
| `telnet` | Telnet client - remote login (insecure) |
| `ftp` | FTP client - file transfer protocol |
| `sftp` | Secure FTP - FTP over SSH |
| `scp` | Secure copy - copy file via SSH |
| `rsync` | Remote sync - sync file/folder remote |
| `tcpdump` | Packet capture - capture network traffic |
| `tshark` | Wireshark CLI - wireshark command line |
| `nmap` | Network mapper - port scanner |
| `arp` | ARP table - tampilkan/manipulate ARP cache |
| `arping` | ARP ping - ping via ARP |
| `ethtool` | Ethernet tool - manage network interface |
| `iwconfig` | Wireless config - konfigurasi wireless (legacy) |
| `iw` | Wireless tool - manage wireless (modern) |
| `nmcli` | NetworkManager CLI - manage network via NetworkManager |
| `nmtui` | NetworkManager TUI - TUI untuk NetworkManager |

---

#### **👤 E. USER & PERMISSION MANAGEMENT**

| Command | Fungsi Singkat |
|---------|----------------|
| `useradd` | Add user - tambah user baru |
| `adduser` | Add user interactive - tambah user (friendly) |
| `userdel` | Delete user - hapus user |
| `usermod` | Modify user - ubah user properties |
| `groupadd` | Add group - tambah group |
| `groupdel` | Delete group - hapus group |
| `groupmod` | Modify group - ubah group |
| `passwd` | Change password - ubah password |
| `chpasswd` | Batch password - ubah password batch |
| `gpasswd` | Group password - manage group password/member |
| `su` | Switch user - ganti user |
| `sudo` | Superuser do - jalankan command sebagai root |
| `visudo` | Edit sudoers - edit sudo configuration |
| `chown` | Change owner - ubah owner file |
| `chgrp` | Change group - ubah group file |
| `chmod` | Change mode - ubah permission file |
| `chattr` | Change attributes - ubah file attributes |
| `lsattr` | List attributes - tampilkan file attributes |
| `getfacl` | Get ACL - tampilkan Access Control List |
| `setfacl` | Set ACL - set Access Control List |
| `umask` | User mask - set default permission |
| `newgrp` | New group - login ke group baru |
| `groups` | Show groups - tampilkan group user |
| `finger` | User info - info detail user |
| `chfn` | Change finger - ubah user info |
| `chsh` | Change shell - ubah default shell user |

---

#### **⚙️ F. PROCESS MANAGEMENT**

| Command | Fungsi Singkat |
|---------|----------------|
| `kill` | Terminate process - matikan proses by PID |
| `killall` | Kill by name - matikan semua proses by name |
| `pkill` | Process kill - kill proses by pattern |
| `nice` | Run with priority - jalankan dengan prioritas tertentu |
| `renice` | Change priority - ubah prioritas proses running |
| `nohup` | No hangup - jalankan command immune to hangup |
| `bg` | Background - resume job di background |
| `fg` | Foreground - bawa job ke foreground |
| `jobs` | List jobs - list background jobs |
| `disown` | Remove job - hapus job dari shell |
| `wait` | Wait process - tunggu process selesai |
| `timeout` | Run with timeout - jalankan command dengan batas waktu |
| `watch` | Execute periodically - jalankan command berulang |
| `screen` | Terminal multiplexer - terminal multiplexing |
| `tmux` | Terminal multiplexer - terminal multiplexing modern |
| `at` | Schedule once - jadwalkan command sekali |
| `atq` | At queue - list scheduled at jobs |
| `atrm` | At remove - hapus at job |
| `batch` | Batch execute - jalankan saat load rendah |
| `crontab` | Cron table - manage recurring scheduled tasks |
| `systemctl` | Systemd control - manage systemd services |
| `service` | Service control - manage services (legacy) |
| `systemd-analyze` | Analyze boot - analisis boot time |

---

#### **📦 G. PACKAGE MANAGEMENT**

| Command | Fungsi Singkat |
|---------|----------------|
| `apt` | Package manager - Debian/Ubuntu package manager |
| `apt-get` | APT get - legacy APT command |
| `apt-cache` | APT cache - search/info packages |
| `dpkg` | Debian package - low-level package manager |
| `dpkg-query` | Query packages - query installed packages |
| `aptitude` | APT frontend - TUI untuk APT |
| `yum` | Yellowdog updater - RedHat/CentOS package manager |
| `dnf` | Dandified yum - modern yum replacement |
| `rpm` | RPM package - RedHat package manager |
| `zypper` | SUSE package - openSUSE package manager |
| `pacman` | Arch package - Arch Linux package manager |
| `snap` | Snap packages - universal package manager |
| `flatpak` | Flatpak packages - universal package manager |
| `pip` | Python packages - Python package installer |
| `pip3` | Python 3 packages - Python 3 package installer |
| `npm` | Node packages - Node.js package manager |
| `gem` | Ruby gems - Ruby package manager |
| `cargo` | Rust packages - Rust package manager |
| `composer` | PHP packages - PHP dependency manager |

---

#### **🗜️ H. COMPRESSION & ARCHIVE**

| Command | Fungsi Singkat |
|---------|----------------|
| `tar` | Tape archive - archive & extract files |
| `gzip` | GNU zip - compress files (.gz) |
| `gunzip` | GNU unzip - decompress .gz files |
| `bzip2` | Bzip2 compress - compress dengan bzip2 (.bz2) |
| `bunzip2` | Bzip2 decompress - decompress .bz2 |
| `xz` | XZ compress - compress dengan xz (.xz) |
| `unxz` | XZ decompress - decompress .xz |
| `zip` | Zip archive - buat .zip archive |
| `unzip` | Unzip archive - extract .zip archive |
| `rar` | RAR archive - buat .rar archive |
| `unrar` | Unrar archive - extract .rar archive |
| `7z` | 7-Zip - compress dengan 7z |
| `zcat` | Cat compressed - cat untuk .gz files |
| `zless` | Less compressed - less untuk .gz files |
| `zgrep` | Grep compressed - grep dalam .gz files |
| `compress` | Compress - old compress utility |
| `uncompress` | Uncompress - decompress .Z files |

---

#### **🔐 I. SECURITY & CRYPTOGRAPHY**

| Command | Fungsi Singkat |
|---------|----------------|
| `ssh` | Secure shell - remote login via SSH |
| `ssh-keygen` | Generate SSH key - buat keypair SSH |
| `ssh-copy-id` | Copy SSH key - install public key ke server |
| `ssh-agent` | SSH agent - manage SSH keys |
| `ssh-add` | Add SSH key - tambah key ke agent |
| `sshd` | SSH daemon - SSH server |
| `openssl` | SSL/TLS toolkit - crypto & SSL tools |
| `gpg` | GNU privacy guard - encrypt/sign files |
| `gpg2` | GPG version 2 - modern GPG |
| `age` | Modern encryption - simple encryption tool |
| `gpg-agent` | GPG agent - manage GPG keys |
| `pass` | Password manager - CLI password manager |
| `pwgen` | Password generator - generate passwords |
| `mkpasswd` | Make password - generate password hash |
| `chage` | Change age - manage password expiry |
| `lastb` | Last bad logins - failed login attempts |
| `faillog` | Failure log - login failure records |
| `iptables` | Firewall - packet filtering firewall |
| `ip6tables` | IPv6 firewall - firewall untuk IPv6 |
| `nftables` | New firewall - modern firewall framework |
| `ufw` | Uncomplicated firewall - simple firewall |
| `firewall-cmd` | Firewall command - firewalld management |
| `setenforce` | SELinux enforce - set SELinux mode |
| `getenforce` | Get SELinux mode - tampilkan SELinux mode |
| `sestatus` | SELinux status - status SELinux |
| `aa-status` | AppArmor status - status AppArmor |
| `chcon` | Change context - ubah SELinux context |
| `restorecon` | Restore context - restore SELinux context |
| `audit2allow` | Audit to allow - generate SELinux policy |

---

#### **💻 J. DEVELOPMENT TOOLS**

| Command | Fungsi Singkat |
|---------|----------------|
| `gcc` | GNU C compiler - C compiler |
| `g++` | GNU C++ compiler - C++ compiler |
| `make` | Build automation - build projects |
| `cmake` | Cross-platform make - modern build system |
| `git` | Version control - distributed VCS |
| `svn` | Subversion - centralized VCS |
| `diff` | Difference - compare files |
| `patch` | Apply patch - apply diff patches |
| `gdb` | GNU debugger - debug programs |
| `strace` | System trace - trace system calls |
| `ltrace` | Library trace - trace library calls |
| `valgrind` | Memory debugger - debug memory leaks |
| `objdump` | Object dump - disassemble binary |
| `nm` | Name list - list symbols in binary |
| `readelf` | Read ELF - analyze ELF binaries |
| `ldd` | Library dependencies - show shared libraries |
| `ld` | Linker - link object files |
| `ar` | Archive - create static libraries |
| `strip` | Strip symbols - remove debug symbols |
| `python` | Python interpreter - Python programming |
| `python3` | Python 3 - Python 3 interpreter |
| `perl` | Perl interpreter - Perl programming |
| `ruby` | Ruby interpreter - Ruby programming |
| `node` | Node.js - JavaScript runtime |
| `java` | Java runtime - run Java programs |
| `javac` | Java compiler - compile Java |
| `rustc` | Rust compiler - compile Rust |
| `go` | Go toolchain - Go programming |

---

#### **🔨 K. SYSTEM ADMINISTRATION**

| Command | Fungsi Singkat |
|---------|----------------|
| `mount` | Mount filesystem - mount storage device |
| `umount` | Unmount filesystem - unmount device |
| `fdisk` | Partition editor - manage disk partitions |
| `parted` | Partition editor - modern partition tool |
| `mkfs` | Make filesystem - format partition |
| `fsck` | Filesystem check - check & repair filesystem |
| `tune2fs` | Tune ext filesystem - adjust ext2/3/4 parameters |
| `blkid` | Block ID - show block device attributes |
| `lsblk` | List block devices - list storage devices |
| `dd` | Disk duplicator - copy disk/partition |
| `hdparm` | Hard disk parameters - tune hard disk |
| `smartctl` | SMART control - check disk health |
| `sync` | Sync disks - flush filesystem buffers |
| `swapon` | Swap on - enable swap |
| `swapoff` | Swap off - disable swap |
| `mkswap` | Make swap - create swap space |
| `init` | Initialize - change runlevel |
| `telinit` | Tell init - change runlevel |
| `shutdown` | Shutdown system - shutdown/reboot |
| `reboot` | Reboot - restart system |
| `halt` | Halt - stop system |
| `poweroff` | Power off - shutdown system |
| `runlevel` | Show runlevel - display current runlevel |
| `systemd` | System daemon - init system |
| `journalctl` | Journal control - view systemd logs |
| `hostnamectl` | Hostname control - manage hostname |
| `localectl` | Locale control - manage locale |
| `timedatectl` | Time/date control - manage time/date |
| `loginctl` | Login control - manage user sessions |
| `sysctl` | System control - manage kernel parameters |
| `modprobe` | Module probe - load kernel modules |
| `lsmod` | List modules - list loaded kernel modules |
| `insmod` | Insert module - insert kernel module |
| `rmmod` | Remove module - remove kernel module |
| `depmod` | Dependencies - generate module dependencies |
| `update-grub` | Update GRUB - update bootloader config |
| `grub-install` | Install GRUB - install bootloader |

---

#### **🔍 L. SEARCH & FIND**

| Command | Fungsi Singkat |
|---------|----------------|
| `find` | Find files - cari file/folder dengan criteria |
| `locate` | Locate files - cari file cepat via database |
| `updatedb` | Update database - update locate database |
| `which` | Which command - tampilkan lokasi command |
| `whereis` | Where is - lokasi binary/source/man |
| `type` | Type command - info tentang command |
| `command` | Command info - run command bypass alias |
| `apropos` | Apropos - search man pages |
| `whatis` | What is - one-line man page description |
| `man` | Manual - tampilkan manual pages |
| `info` | Info pages - GNU info documentation |
| `help` | Help - bash builtin help |

---

#### **📋 M. TEXT EDITORS**

| Command | Fungsi Singkat |
|---------|----------------|
| `vim` | Vi improved - advanced text editor |
| `vi` | Visual editor - classic text editor |
| `nano` | Nano editor - simple text editor |
| `emacs` | Emacs editor - extensible text editor |
| `gedit` | GNOME editor - GUI text editor |
| `kate` | KDE editor - KDE text editor |
| `sed` | Stream editor - edit text via commands |
| `ed` | Line editor - original Unix editor |
| `ex` | Extended editor - vi predecessor |

---

#### **🖥️ N. SHELL & TERMINAL**

| Command | Fungsi Singkat |
|---------|----------------|
| `bash` | Bourne again shell - default Linux shell |
| `sh` | Shell - POSIX shell |
| `dash` | Debian shell - lightweight POSIX shell |
| `zsh` | Z shell - advanced shell |
| `fish` | Friendly shell - user-friendly shell |
| `ksh` | Korn shell - AT&T shell |
| `tcsh` | TC shell - C shell with features |
| `csh` | C shell - shell dengan C syntax |
| `exit` | Exit shell - keluar dari shell |
| `logout` | Logout - logout dari login shell |
| `clear` | Clear screen - bersihkan layar terminal |
| `reset` | Reset terminal - reset terminal state |
| `tput` | Terminal put - control terminal |
| `tty` | Teletypewriter - print terminal name |
| `stty` | Set tty - set terminal settings |
| `script` | Record session - record terminal session |
| `scriptreplay` | Replay script - replay recorded session |
| `xargs` | Execute args - build & execute commands |
| `parallel` | Parallel execution - run commands parallel |
| `env` | Environment - display/set environment |
| `printenv` | Print environment - print environment vars |
| `set` | Set options - set shell options |
| `unset` | Unset variable - remove variable |
| `export` | Export variable - export to environment |
| `alias` | Create alias - buat command alias |
| `unalias` | Remove alias - hapus alias |
| `history` | Command history - tampilkan command history |
| `fc` | Fix command - edit & rerun commands |
| `source` | Source script - execute script in shell |
| `.` | Dot command - execute script (same as source) |
| `eval` | Evaluate - evaluate & execute string |
| `exec` | Execute - replace shell with command |
| `test` | Test condition - evaluate conditional |
| `[` | Test bracket - conditional test |
| `[[` | Extended test - bash extended test |
| `true` | True condition - return success |
| `false` | False condition - return failure |
| `yes` | Repeat yes - output "yes" repeatedly |
| `seq` | Sequence - generate number sequence |
| `shuf` | Shuffle - randomize lines |
| `factor` | Factor number - prime factorization |
| `bc` | Calculator - arbitrary precision calculator |
| `expr` | Expression - evaluate expressions |
| `printf` | Print formatted - format & print data |
| `echo` | Echo text - print text |
| `read` | Read input - read user input |
| `sleep` | Sleep - delay execution |

---

#### **📊 O. DATA PROCESSING & ANALYSIS**

| Command | Fungsi Singkat |
|---------|----------------|
| `jq` | JSON processor - parse & manipulate JSON |
| `yq` | YAML processor - parse YAML |
| `xmllint` | XML lint - parse & validate XML |
| `csvkit` | CSV toolkit - CSV processing tools |
| `awk` | Pattern processing - text processing language |
| `sed` | Stream editor - stream text editor |
| `perl` | Perl - text processing language |
| `python` | Python - data processing language |
| `sqlite3` | SQLite - lightweight database |
| `mysql` | MySQL client - MySQL database client |
| `psql` | PostgreSQL - PostgreSQL client |
| `redis-cli` | Redis client - Redis database client |

---

#### **🎨 P. MISCELLANEOUS UTILITIES**

| Command | Fungsi Singkat |
|---------|----------------|
| `yes` | Output yes - print "yes" repeatedly |
| `banner` | Print banner - large text banner |
| `figlet` | ASCII art - generate ASCII art text |
| `cowsay` | Cow say - ASCII cow with message |
| `fortune` | Fortune cookie - random quotes |
| `cal` | Calendar - display calendar |
| `date` | Date/time - display/set date |
| `units` | Unit conversion - convert units |
| `bc` | Calculator - command line calculator |
| `factor` | Prime factors - factorize numbers |
| `look` | Look up - search dictionary words |
| `aspell` | Spell checker - spell check utility |
| `rename` | Rename files - batch rename files |
| `tee` | Tee junction - write to file & stdout |
| `xclip` | X clipboard - manipulate clipboard |
| `xsel` | X selection - manipulate X selection |
| `enscript` | Format printing - convert text to PostScript |
| `tty-clock` | Terminal clock - clock in terminal |
| `sl` | Steam locomotive - fun train animation |
| `cmatrix` | Matrix effect - Matrix movie effect |
| `asciinema` | Record terminal - record terminal sessions |
| `termtosvg` | Terminal to SVG - convert terminal to SVG |

---

#### **🔧 Q. ADVANCED SYSTEM TOOLS**

| Command | Fungsi Singkat |
|---------|----------------|
| `chroot` | Change root - change root directory |
| `nsenter` | Namespace enter - enter namespace |
| `unshare` | Unshare namespace - create namespace |
| `capsh` | Capability shell - work with capabilities |
| `setcap` | Set capability - set file capabilities |
| `getcap` | Get capability - show file capabilities |
| `pam_tally2` | PAM tally - track login failures |
| `faillock` | Fail lock - track authentication failures |
| `ausearch` | Audit search - search audit logs |
| `aureport` | Audit report - audit report generator |
| `auditctl` | Audit control - control audit system |
| `logger` | Logger - write to system log |
| `logrotate` | Log rotate - rotate log files |
| `rsyslog` | Syslog daemon - system logging |
| `systemd-analyze` | Systemd analyze - analyze boot performance |
| `perf` | Performance - Linux performance tools |
| `bpftrace` | BPF trace - eBPF tracing tool |
| `dtrace` | Dynamic trace - dynamic tracing |

---

#### **📸 R. BACKUP & RECOVERY**

| Command | Fungsi Singkat |
|---------|----------------|
| `rsync` | Remote sync - efficient file sync |
| `rclone` | Cloud sync - sync to cloud storage |
| `duplicity` | Encrypted backup - encrypted backup tool |
| `restic` | Backup - fast backup program |
| `borg` | Backup - deduplicating backup |
| `tar` | Tape archive - archive files |
| `cpio` | Copy in/out - archive files |
| `dump` | Filesystem dump - backup filesystem |
| `restore` | Restore backup - restore from dump |
| `ddrescue` | Data recovery - recover data from disk |
| `testdisk` | Test disk - recover partitions |
| `photorec` | Photo recovery - recover files |
| `extundelete` | Ext undelete - recover deleted files |
| `foremost` | File recovery - recover files by header |

---

#### **🌍 S. INTERNATIONALIZATION**

| Command | Fungsi Singkat |
|---------|----------------|
| `locale` | Locale settings - display locale info |
| `localectl` | Locale control - manage system locale |
| `iconv` | Convert encoding - convert text encoding |
| `recode` | Recode text - convert character sets |
| `msgfmt` | Message format - compile message catalogs |
| `gettext` | Get text - internationalization tool |

---

#### **🎯 T. PERFORMANCE & BENCHMARKING**

| Command | Fungsi Singkat |
|---------|----------------|
| `time` | Time command - measure command execution time |
| `perf` | Performance - Linux performance analysis |
| `sysbench` | System benchmark - system performance test |
| `stress` | Stress test - stress test system |
| `stress-ng` | Stress new gen - advanced stress test |
| `iperf` | Network performance - network bandwidth test |
| `ab` | Apache bench - HTTP server benchmark |
| `wrk` | HTTP benchmark - modern HTTP benchmark |
| `siege` | HTTP load - HTTP load testing |
| `hdparm` | HD parameters - measure disk performance |
| `dd` | Disk benchmark - measure I/O speed |
| `fio` | Flexible I/O - I/O benchmark tool |
| `bonnie++` | Disk benchmark - filesystem benchmark |

---

### 💡 TIPS MENGGUNAKAN KAMUS INI:

**Cara Cepat Mencari Command:**
```bash
# List all commands di /bin
ls /bin

# List all commands di /usr/bin
ls /usr/bin

# Cari command dengan pattern
compgen -c | grep pattern

# Info singkat command
whatis command_name

# Manual lengkap command
man command_name

# Cari command by functionality
apropos keyword
```

**Contoh Praktis:**
```bash
# Cari semua command untuk "file"
apropos file | grep -i search

# List semua command yang installed
compgen -c | sort | uniq

# Cari tau fungsi command
whatis grep
# Output: grep (1) - print lines that match patterns

# Help untuk builtin commands
help cd
help echo
```

---

**🎓 PANDUAN BELAJAR:**
1. **Fundamental** (Harus dikuasai): `ls`, `cd`, `pwd`, `cp`, `mv`, `rm`, `cat`, `grep`, `find`, `chmod`
2. **Intermediate** (Penting): `sed`, `awk`, `tar`, `ssh`, `ps`, `kill`, `netstat`, `cron`
3. **Advanced** (Professional): `strace`, `lsof`, `tcpdump`, `iptables`, `systemctl`, `rsync`
4. **Expert** (Security Pro): `nmap`, `openssl`, `gpg`, `auditctl`, `selinux tools`, `bpftrace`

---

##  D. PRAKTIK HANDS-ON

### 4.1 FASE PERSIAPAN

#### **Step 1: Setup Virtualization Environment**

```
A. Download & Install Virtualization Tool
   └─ Pilih: VirtualBox (recommended untuk lab)
   └─ Download: https://www.virtualbox.org/wiki/Downloads
   └─ Install sesuai OS Anda

B. Download Linux ISO
   ├─ Kali Linux: https://www.kali.org/downloads/
   │  └─ Recommended: Installer images → VirtualBox 64-bit
   └─ Ubuntu Server (opsional, untuk target): https://ubuntu.com/download/server/
```

---

#### **Step 2: Create Virtual Machine di VirtualBox**

**Untuk Kali Linux (Attack Machine):**

```
1. Buka VirtualBox → Machine → New
   - Name: Kali-Lab
   - Type: Linux
   - Version: Debian (64-bit)
   - Memory: 4096 MB (minimal 2048 MB)

2. Create Virtual Hard Disk
   - VDI (VirtualBox Disk Image)
   - Size: 20-30 GB
   - Fixed size (recommended untuk performance)

3. VM Settings (sebelum start):
   - Storage: Attach ISO file Kali
   - Network: 
     * Adapter 1: NAT (untuk internet)
     * Adapter 2: Host-only (untuk komunikasi antar VM)
   - Processor: 2-4 cores
   - Video Memory: 64 MB

4. Start VM dan install sesuai guided installer
```

**Untuk Ubuntu Server (Target Machine - Optional):**

```
Sama dengan Kali, tapi:
- Name: Ubuntu-Target
- Memory: 2048 MB
- Storage: 15 GB
- Network: Host-only (isolated dari Kali)
```

---

#### **Step 3: Post-Installation Setup di Kali Linux**

Setelah Kali Linux terinstall:

```bash
# 1. Update system
$ sudo apt update
$ sudo apt upgrade -y
$ sudo apt full-upgrade -y

# 2. Install essential tools (opsional, sudah ada di Kali)
$ sudo apt install -y \
  net-tools \
  curl \
  wget \
  git \
  vim \
  python3-pip

# 3. Verify tools (confirm pre-installed)
$ nmap --version
$ wireshark --version
$ burpsuite
$ metasploit

# 4. Setup SSH (untuk akses remote)
$ sudo systemctl enable ssh
$ sudo systemctl start ssh
$ ssh-keygen -t rsa -b 4096

# 5. Configure network (check connectivity)
$ ip addr show
$ route -n
$ ping 8.8.8.8
```

---

### 4.2 FASE EKSEKUSI PRAKTIK - Linux Foundation Basics

#### **Persiapan Awal Sebelum Praktik:**

```bash
# Login ke Kali Linux di VirtualBox
# Username: kali (atau root, tergantung setup)
# Buka Terminal

# Verifikasi environment
$ whoami
# Output: kali (atau root)

$ uname -a
# Output: Linux kali 5.10.0-13-amd64 #1 SMP ... GNU/Linux
# Informasi: OS, kernel version, architecture
```

---

#### **Activity 1: System Information & Hostname Management (30 menit)**

**Objective:** Memahami identitas sistem dan cara mengubahnya

```bash
# ===== VIEW SYSTEM INFO =====

$ uname -a
# Output: Semua informasi sistem (kernel name, version, hardware)

$ uname -s
# Kernel name: Linux

$ uname -r
# Kernel release: 5.10.0-13-amd64

$ uname -m
# Machine hardware: x86_64

$ cat /etc/os-release
# OS details: Kali Linux, version, ID
# Output terlihat seperti: NAME="Kali Linux", VERSION="2024.1", etc

$ hostnamectl
# Lebih detail info tentang hostname & OS
# Output: Static hostname, Icon name, Machine ID, Boot ID


# ===== CHANGE HOSTNAME =====

$ hostname
# Current hostname: Menampilkan nama mesin saat ini
# Output: kali

$ sudo hostnamectl set-hostname lab-security
# Change permanent hostname
# Setelah reboot, hostname akan berubah

$ sudo nano /etc/hostname
# Manual edit hostname file (old method)
# Edit langsung file, ganti nama lama dengan yang baru
# Ctrl+O (save), Ctrl+X (exit)

# Verifikasi perubahan
$ hostname
# Output: lab-security (setelah reboot)
```

**Output Esperado:**

```
$ uname -a
Linux kali 5.10.0-13-amd64 #1 SMP Debian 5.10.106-1 x86_64 GNU/Linux

$ hostnamectl
 Static hostname: lab-security
       Icon name: computer
 Operating System: Kali Linux
           Kernel: Linux 5.10.0-13-amd64
       Architecture: x86-64
```

---

#### **Activity 2: Directory Management & File Operations (30 menit)**

**Objective:** Master basic folder & file operations

```bash
# ===== CREATE DIRECTORY STRUCTURE =====

$ mkdir -p ~/security_lab/scans/results
# Create nested directory structure for organization
# ~ = home directory (/home/kali)
# -p = create parent directories jika tidak ada

$ cd ~/security_lab
$ pwd
# Output: /home/kali/security_lab
# Verify lokasi saat ini

$ ls -la
# Tampilkan semua folders yang baru dibuat
# Output: drwxr-xr-x kali kali ... scans


# ===== FILE CREATION & EDITING =====

$ touch report.txt targets.txt notes.md
# Create multiple empty files sekaligus

$ nano report.txt
# Edit file dengan nano
# Ketik: "Lab Security Report - Pertemuan 1"
# Ctrl+O → Enter → Ctrl+X (save & exit)

$ cat report.txt
# Verify file content
# Output: Lab Security Report - Pertemuan 1

$ nano targets.txt
# Edit targets file
# Ketik:
# 192.168.1.1
# 192.168.1.100
# 192.168.1.101
# Save dengan Ctrl+O, Ctrl+X


# ===== FILE OPERATIONS =====

$ ls -la
# Lihat semua files dengan permissions

$ cp report.txt report_backup.txt
# Backup file

$ mv targets.txt lab_targets.txt
# Rename file

$ mkdir archive
$ mv report_backup.txt archive/
# Move file ke folder lain

$ cat lab_targets.txt
# View file content

$ wc -l lab_targets.txt
# Count lines: Output: 3 lab_targets.txt

$ head -1 lab_targets.txt
# Show first line: 192.168.1.1
```

**Expected Structure:**

```
~/security_lab/
├── report.txt
├── lab_targets.txt
├── notes.md
├── scans/
│   └── results/
└── archive/
    └── report_backup.txt
```

---

#### **Activity 3: Package Installation & Tool Setup (45 menit)**

**Objective:** Install security tools yang akan digunakan

```bash
# ===== UPDATE PACKAGE LIST =====

$ sudo apt update
# Refresh package list dari repository
# Perlu sudo karena modifikasi system

$ sudo apt upgrade -y
# Upgrade installed packages
# -y = automatic yes untuk semua prompts
# CAUTION: Ini bisa butuh waktu lama (coffee break!)


# ===== INSTALL SECURITY TOOLS =====

# Install individual packages
$ sudo apt install -y nmap
# Network mapper - untuk scanning ports

$ sudo apt install -y wireshark
# Packet analyzer - untuk capture network traffic

$ sudo apt install -y tcpdump
# Command-line packet capture tool

$ sudo apt install -y aircrack-ng
# WiFi penetration testing tool

$ sudo apt install -y burpsuite
# Web proxy untuk testing aplikasi web

# Atau install sekaligus
$ sudo apt install -y nmap wireshark tcpdump aircrack-ng burpsuite

# Install additional useful tools
$ sudo apt install -y net-tools
# Network utilities (ifconfig, netstat, dll)

$ sudo apt install -y curl wget
# Download tools


# ===== VERIFY INSTALLATION =====

$ nmap --version
# Output: Nmap version X.XX

$ wireshark --version
# Output: Wireshark X.XX.X

$ tcpdump --version
# Output: tcpdump version X.XX

$ which aircrack-ng
# Output: /usr/bin/aircrack-ng

$ which burpsuite
# Output: /usr/bin/burpsuite


# ===== VERIFY INSTALLED PACKAGES =====

$ apt list --installed | grep -E "nmap|wireshark|tcpdump"
# List installed packages yang match pattern

$ dpkg -l | grep nmap
# Alternative cara check installed package
```

**Expected Output:**

```bash
$ sudo apt install -y nmap wireshark tcpdump
Reading package lists... Done
Building dependency tree... Done
Setting up nmap (7.80)... Done
Setting up wireshark (3.4.5)... Done
Setting up tcpdump (4.99.1)... Done
```

---

#### **Activity 4: Linux Configuration & System Management (60 menit)**

**Objective:** Memahami file konfigurasi Linux dan cara mengatur services

---

##### **🔧 4.1 Pengenalan File Konfigurasi Penting**

Untuk pemula, perlu tahu bahwa **Linux diatur melalui text configuration files**. Berbeda dari Windows yang pakai GUI, Linux lebih sering edit file langsung.

```bash
# File konfigurasi biasanya di folder:
/etc/                 # Sistem-wide configuration (bukan user config)
/home/user/.config/   # User-specific configuration
/root/.ssh/           # SSH keys (khusus root)
```

**Struktur file konfigurasi:**

```
# Format umum Linux config file:
# Komentar dimulai dengan # (tidak dijalankan)
parameter_name=value           # Format 1: key=value
parameter_name value           # Format 2: key value
[section_name]                 # Format 3: config sections
parameter = value
```

---

##### **🔧 4.2 Services & systemctl (Manajemen Layanan)**

**Apa itu service?**
Service = program yang berjalan di background untuk melayani request (SSH, HTTP, database, dll)

**Perintah dasar:**

```bash
# ===== CHECK SERVICE STATUS =====

$ systemctl status ssh
# Tampilkan status service SSH
# Output:
# ● ssh.service - OpenBSD Secure Shell server
#    Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
#    Active: active (running) since Wed 2025-01-15 10:00:00 UTC; 2h 30min ago
#    Main PID: 1234 (sshd)
#    Tasks: 1 (limit: 2345)
#    Memory: 5.6M
#    CPU: 12ms

# Status meanings:
# - Loaded: Service file ditemukan & di-load
# - Active: Service sedang berjalan
# - Enabled: Auto-start saat boot

$ systemctl is-active ssh
# Output: active (jika running)

$ systemctl is-enabled ssh
# Output: enabled (jika auto-start saat boot)


# ===== START / STOP SERVICES =====

$ sudo systemctl start ssh
# Mulai service SSH (jika belum berjalan)

$ sudo systemctl stop ssh
# Stop/matikan service SSH

$ sudo systemctl restart ssh
# Restart service SSH (matikan lalu mulai ulang)
# Gunakan ini setelah edit config file

$ sudo systemctl reload ssh
# Reload configuration tanpa disconnect existing connections
# Lebih halus dari restart


# ===== ENABLE / DISABLE AT BOOT =====

$ sudo systemctl enable ssh
# Enable SSH auto-start saat boot
# Efeknya: SSH akan otomatis jalan setiap kali system restart

$ sudo systemctl disable ssh
# Disable SSH auto-start
# Efeknya: SSH tidak otomatis jalan saat boot, harus manual start

$ sudo systemctl is-enabled ssh
# Check apakah enabled atau tidak


# ===== LIST SEMUA SERVICES =====

$ systemctl list-units --type=service
# Tampilkan semua active services

$ systemctl list-units --type=service --state=failed
# Tampilkan services yang failed

$ systemctl list-units --type=service --all
# Tampilkan semua services (active & inactive)
```

**Praktik Example:**

```bash
# Scenario: Kita ingin enable & verify SSH service

$ sudo systemctl enable ssh
Created symlink /etc/systemd/system/multi-user.target.wants/ssh.service → 
  /lib/systemd/system/ssh.service.

$ sudo systemctl start ssh

$ systemctl status ssh
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2025-01-15 14:30:22 UTC; 15s ago
    Process: 5678 ExecStartPre=/usr/sbin/sshd -t (code=exited, status=0/SUCCESS)
     Main PID: 5679 (sshd)
    Tasks: 1 (limit: 2345)
     Memory: 5.3M
      CPU: 2ms
     CGroup: /system.slice/ssh.service
             └─5679 /usr/sbin/sshd -D

Jan 15 14:30:22 kali systemd[1]: Starting OpenBSD Secure Shell server...
Jan 15 14:30:22 kali systemd[1]: Started OpenBSD Secure Shell server.
```

---

##### **🔧 4.3 SSH Configuration (Keamanan Koneksi Remote)**

**File: `/etc/ssh/sshd_config`** (Server config)
**File: `~/.ssh/config`** (Client config)

**Penjelasan untuk pemula:**

```bash
# SSH = Secure Shell (terenkripsi, aman)
# Default port: 22
# Kalau tidak ada, SSH tidak bisa diakses dari luar

# ===== VIEW SSH CONFIGURATION =====

$ cat /etc/ssh/sshd_config | grep -v "^#" | grep -v "^$"
# Tampilkan config SSH (skip comments & blank lines)

# Output umum:
# Port 22
# AddressFamily any
# ListenAddress 0.0.0.0
# ListenAddress ::
# PermitRootLogin prohibit-password
# PasswordAuthentication yes
# PubkeyAuthentication yes
# ...
```

**Penjelasan parameter penting:**

```bash
# Parameter yang sering di-edit:

Port 22
# Port yang SSH dengarkan (1-65535)
# Default: 22
# Jika ingin ganti ke 2222:
# Port 2222
# Lalu restart: sudo systemctl restart ssh

PermitRootLogin prohibit-password
# Boleh login root? 
# - "yes": Root login dengan password diperbolehkan
# - "prohibit-password": Root hanya boleh login dengan SSH key
# - "no": Root tidak boleh login sama sekali (RECOMMENDED untuk production)

PasswordAuthentication yes
# Boleh login dengan password?
# - "yes": Login dengan username & password (standar)
# - "no": Hanya SSH key yang boleh (lebih aman)

PubkeyAuthentication yes
# Boleh login dengan SSH key?
# - "yes": Login dengan SSH public key (aman)

MaxAuthTries 6
# Berapa kali coba login sebelum disconnect
# Default: 6
# Makin kecil makin aman dari brute-force

ClientAliveInterval 300
# Keepalive timeout (detik)
# Default: 300 (5 menit)
# Jika idle > 5 menit, connection ditutup
```

**Edit SSH Config (untuk pemula):**

```bash
# BACKUP terlebih dahulu!
$ sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup

# Edit dengan nano
$ sudo nano /etc/ssh/sshd_config

# Cari line "PermitRootLogin"
# Ubah dari: PermitRootLogin prohibit-password
# Menjadi:   PermitRootLogin no

# Ctrl+O (save), Ctrl+X (exit)

# Restart SSH
$ sudo systemctl restart ssh

# Verify
$ sudo systemctl status ssh
```

**Verify konfigurasi sebelum restart (PENTING!):**

```bash
$ sudo sshd -t
# Jika output kosong = OK
# Jika ada error = error message muncul

# JANGAN restart kalau ada error, bisa disconnect!
```

---

##### **🔧 4.4 /etc/hosts File (DNS Manual Mapping)**

**Apa itu /etc/hosts?**
File text yang map hostname ke IP address (sebelum query DNS server)

**File location & struktur:**

```bash
# Location
/etc/hosts                  # Linux/Mac
C:\Windows\System32\drivers\etc\hosts   # Windows

# Format:
IP_ADDRESS    hostname    alias1 alias2 ...
127.0.0.1     localhost   localhost.localdomain
::1           localhost   localhost.localdomain
192.168.1.100 kali-lab    lab
192.168.1.101 ubuntu-target target
```

**View & Edit:**

```bash
$ cat /etc/hosts
# Tampilkan file

$ sudo nano /etc/hosts
# Edit dengan nano

# Tambahkan line:
192.168.1.100 kali-lab
192.168.1.101 ubuntu-target

# Ctrl+O (save), Ctrl+X (exit)
```

**Verify & Test:**

```bash
$ ping kali-lab
# PING kali-lab (192.168.1.100) 56(84) bytes of data.
# 64 bytes from kali-lab (192.168.1.100): icmp_seq=1 ttl=64 time=0.245 ms

$ ssh admin@ubuntu-target
# SSH sekarang bisa pakai hostname daripada IP
```

---

##### **🔧 4.5 Network Configuration Basics**

**Lihat network info:**

```bash
# ===== UBUNTU / KALI LINUX (Debian-based) =====

$ cat /etc/netplan/00-installer-config.yaml
# View network config (modern: netplan)
# Atau:
$ cat /etc/network/interfaces
# View network config (legacy: ifupdown)

# Format netplan:
# network:
#   version: 2
#   renderer: networkd
#   ethernets:
#     eth0:
#       dhcp4: true
#       dhcp4-overrides:
#         use-dns: false
#       nameservers:
#         addresses: [8.8.8.8, 8.8.4.4]

# DHCP4: true = otomatis dapat IP dari DHCP server
# Addresses: static IP configuration


# ===== REDHAT / CENTOS (RPM-based) =====

$ cat /etc/sysconfig/network-scripts/ifcfg-eth0
# View network config di RedHat/CentOS

# Format:
# TYPE=Ethernet
# BOOTPROTO=dhcp
# NAME=eth0
# DEVICE=eth0
# ONBOOT=yes
# BOOTPROTO=none (static IP)
# IPADDR=192.168.1.100
# NETMASK=255.255.255.0
# GATEWAY=192.168.1.1
```

**View current network info:**

```bash
# Lihat IP address
$ ip addr show
# atau
$ ifconfig

# Lihat gateway & routing
$ ip route show
# atau
$ route -n

# Lihat DNS
$ cat /etc/resolv.conf
# Output:
# nameserver 8.8.8.8
# nameserver 8.8.4.4
```

---

##### **🔧 4.6 Firewall (iptables / ufw)**

**Apa itu firewall?**
Program yang control traffic masuk/keluar sistem (allow/block port & IP)

**Ubuntu/Kali (use ufw - user-friendly):**

```bash
$ sudo ufw status
# Lihat status firewall
# Output: Status: inactive (belum aktif)
#   atau: Status: active (sudah aktif)

$ sudo ufw enable
# Aktifkan firewall

$ sudo ufw disable
# Nonaktifkan firewall

# ===== RULES =====

$ sudo ufw allow 22/tcp
# Allow port 22 (SSH) TCP traffic

$ sudo ufw allow 80/tcp
# Allow port 80 (HTTP)

$ sudo ufw allow 443/tcp
# Allow port 443 (HTTPS)

$ sudo ufw deny 3306/tcp
# Deny port 3306 (MySQL)

$ sudo ufw allow from 192.168.1.100 to any port 22
# Allow SSH hanya dari IP 192.168.1.100

$ sudo ufw show added
# Tampilkan rules yang ditambahkan

$ sudo ufw reset
# Reset firewall ke default (hapus semua rules)
```

**RedHat/CentOS (use firewalld):**

```bash
$ sudo systemctl status firewalld
# Check firewall status

$ sudo systemctl enable firewalld
$ sudo systemctl start firewalld

$ sudo firewall-cmd --list-all
# Tampilkan semua rules

$ sudo firewall-cmd --permanent --add-port=22/tcp
# Permanent add port 22

$ sudo firewall-cmd --reload
# Reload firewall
```

**Lower level: iptables (advanced, untuk reference saja):**

```bash
$ sudo iptables -L -n
# List semua rules (raw level)
# OUTPUT:
# Chain INPUT (policy ACCEPT)
# target  prot opt source    destination
# ACCEPT  tcp  --  0.0.0.0   0.0.0.0   tcp dpt:22

$ sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
# Add rule: accept port 80 TCP
# -A INPUT = append to INPUT chain
# -p tcp = protocol TCP
# --dport 80 = destination port 80
# -j ACCEPT = jump/action: ACCEPT (allow)

$ sudo iptables -D INPUT -p tcp --dport 80 -j ACCEPT
# Delete rule

$ sudo iptables-save > /etc/iptables/rules.v4
# Save rules (persist across reboot)
```

---

##### **🔧 4.7 Perbandingan Distro (Ubuntu vs Kali vs RedHat vs CentOS)**

**Tabel Perbandingan Config:**

| Aspek | Ubuntu/Debian | Kali Linux | RedHat/CentOS |
|-------|----------------|------------|---------------|
| Base | Debian | Debian | Fedora/RHEL |
| Package Manager | apt | apt | yum/dnf |
| Network Config | netplan/network | netplan/network | nmcli/sysconfig |
| Firewall | ufw/iptables | ufw/iptables | firewalld |
| Init System | systemd | systemd | systemd |
| SSH Config | /etc/ssh/sshd_config (SAMA) | /etc/ssh/sshd_config (SAMA) | /etc/ssh/sshd_config (SAMA) |
| /etc/hosts | /etc/hosts (SAMA SEMUA) | /etc/hosts (SAMA SEMUA) | /etc/hosts (SAMA SEMUA) |
| Package Install | apt install pkg | apt install pkg | dnf install pkg |
| Service Start | systemctl start | systemctl start | systemctl start |
| Default Services | ssh, apache2 | ssh, apache2 | sshd, httpd |

**Command equivalents:**

```bash
# ===== UBUNTU / DEBIAN =====
$ sudo apt install package-name      # Install package
$ sudo systemctl start ssh            # Start service
$ sudo ufw allow 22/tcp               # Firewall rule

# ===== RHEL / CENTOS 7+ =====
$ sudo dnf install package-name       # Install (CentOS 8+)
$ sudo yum install package-name       # Install (CentOS 7)
$ sudo systemctl start sshd           # Start service (note: sshd not ssh)
$ sudo firewall-cmd --add-port=22/tcp # Firewall rule

# ===== NOTE =====
# - Ubuntu/Kali = Debian-based (apt package manager)
# - CentOS/RHEL = RPM-based (yum/dnf package manager)
# - Semua pakai systemd untuk init system (modern Linux)
```

---

##### **🔧 4.8 Konfigurasi Default di Setiap Distro**

**Ubuntu Default:**

```bash
# /etc/hostname
ubuntu-target

# /etc/hosts
127.0.0.1 localhost
192.168.1.101 ubuntu-target

# systemctl services
$ systemctl is-enabled ssh
enabled

$ systemctl is-enabled apache2
disabled
```

**Kali Linux Default:**

```bash
# /etc/hostname
kali

# /etc/hosts
127.0.0.1 localhost
127.0.1.1 kali

# systemctl services (pre-installed tools)
$ systemctl is-enabled ssh
enabled (biasanya)

$ ls -la /lib/systemd/system/ | grep -E "nmap|wireshark"
# Tidak ada (ini tools, bukan services)
```

**CentOS 7 Default:**

```bash
# /etc/hostname
centos7

# /etc/sysconfig/network
NETWORKING=yes

# /etc/sysconfig/network-scripts/ifcfg-eth0
ONBOOT=yes
BOOTPROTO=dhcp
TYPE=Ethernet

# Service name
$ systemctl is-enabled sshd
enabled (note: sshd, not ssh like Debian)
```

---

##### **🔧 4.9 Praktik: Edit Konfigurasi & Restart Service**

**Skenario: Change SSH port & verify**

```bash
# Step 1: Backup original config (ALWAYS!)
$ sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup

# Step 2: Edit config dengan nano
$ sudo nano /etc/ssh/sshd_config

# Step 3: Find & change port
# Cari: Port 22
# Ubah ke: Port 2222
# Ctrl+O (save), Ctrl+X (exit)

# Step 4: VERIFY sebelum restart (CRITICAL!)
$ sudo sshd -t
# Jika OK = no output
# Jika error = error message

# Step 5: Restart service
$ sudo systemctl restart ssh
# atau
$ sudo systemctl restart sshd (untuk RedHat/CentOS)

# Step 6: Verify running
$ sudo systemctl status ssh

# Step 7: Test connectivity dengan port baru
$ ssh -p 2222 username@localhost
# atau dari machine lain:
$ ssh -p 2222 username@192.168.1.100
```

**Skenario: Firewall rule untuk SSH custom port**

```bash
$ sudo ufw allow 2222/tcp
# Allow port 2222

$ sudo ufw allow from 192.168.1.0/24 to any port 2222
# Allow hanya dari subnet tertentu

$ sudo ufw show added
# Verify rules
```

---

### 4.3 FASE MEMBUAT TUGAS - Linux Foundation Assignment

#### **ASSIGNMENT: Linux Foundation Mastery**

**Tujuan:**
Mahasiswa menguasai Linux command-line fundamentals dan dapat setup environment untuk security tools

**Durasi:** 1 minggu (dengan check-in pertemuan berikutnya)

**Requirements & Rubric:**

```
TOTAL SCORE: 100 points

1. SYSTEM INFORMATION & HOSTNAME (15 points)
   ✓ 5 pts: Jalankan uname -a dan screenshot output
            → Tunjukkan: OS, kernel, architecture
   ✓ 5 pts: Change hostname menjadi "[nama-anda]-lab"
            → Verify dengan hostname command
   ✓ 5 pts: Document perubahan di file perubahan_hostname.txt
            → Berisi: hostname lama, hostname baru, command yang digunakan

2. DIRECTORY & FILE MANAGEMENT (25 points)
   ✓ 5 pts: Create directory ~/security_lab/scans/results
            → Screenshot ls -la untuk verifikasi struktur
   ✓ 5 pts: Create 3 files: report.txt, targets.txt, notes.md
            → Edit masing-masing dengan nano (minimal 3 baris text)
            → Screenshot setiap file content dengan cat command
   ✓ 5 pts: Copy, rename, move operations
            → Copy report.txt → report_backup.txt
            → Rename targets.txt → lab_targets.txt
            → Move report_backup.txt ke folder archive/
            → Screenshot akhir ls -laR ~/security_lab
   ✓ 5 pts: File content operations
            → Gunakan cat, head, tail, wc pada files
            → Screenshot setiap command & hasil
   ✓ 5 pts: Permission management (bonus understanding)
            → Set report.txt permission ke 600
            → Verifikasi dengan ls -la
            → Jelaskan apa arti 600

3. TEXT PROCESSING & SEARCHING (20 points)
   ✓ 4 pts: GREP practice
            → Cari file dengan "security" di lab_targets.txt
            → Gunakan grep -i, -v, -n
            → Screenshot hasil
   ✓ 4 pts: CUT & AWK practice
            → Edit targets.txt dengan format: IP:PORT:STATUS
            → Contoh: 192.168.1.1:22:open
            → Extract IP dengan cut & awk
            → Screenshot hasil
   ✓ 4 pts: SORT & UNIQ
            → Create file dengan duplicate IPs
            → Sort & remove duplicate
            → Count unique IPs dengan wc
            → Screenshot hasil
   ✓ 4 pts: PIPELINE practice
            → Combine 2-3 commands dengan |
            → Contoh: cat file | grep pattern | sort | uniq
            → Screenshot & jelaskan setiap step
   ✓ 4 pts: Document semua commands dalam file commands.txt

4. PACKAGE INSTALLATION & VERIFICATION (20 points)
   ✓ 5 pts: Update system
            → sudo apt update && sudo apt upgrade -y
            → Screenshot before & after
            → Catat berapa package di-upgrade
   ✓ 5 pts: Install security tools
            → nmap, wireshark, tcpdump, aircrack-ng, burpsuite
            → Screenshot install process
            → Screenshot hasil apt list --installed
   ✓ 5 pts: Verify each tool
            → nmap --version
            → wireshark --version
            → tcpdump --version
            → which aircrack-ng
            → which burpsuite
            → Screenshot semua output
   ✓ 5 pts: Create installation_log.txt
            → Document setiap tool & version yang terinstall
            → Tanggal & waktu installation

5. NETWORK & CONNECTIVITY SETUP (15 points)
   ✓ 5 pts: Network information
            → ifconfig atau ip addr show
            → Catat: IP address, Netmask, Gateway
            → Screenshot & save ke network_info.txt
   ✓ 5 pts: Port discovery (bersiap untuk pertemuan 2)
            → sudo netstat -tuln | grep LISTEN
            → Screenshot listening ports
            → Dokumentasikan port apa yang terbuka
   ✓ 5 pts: SSH setup & connectivity test
            → Enable SSH: sudo systemctl enable ssh
            → Start SSH: sudo systemctl start ssh
            → Test dari command prompt Windows:
              ssh kali@[VM-IP-ADDRESS]
            → Screenshot successful SSH login dari Windows
            → Dokumentasikan IP VM & command yang digunakan

6. LINUX CONFIGURATION & SERVICES (15 points)
   ✓ 3 pts: systemctl service management
            → systemctl status ssh
            → systemctl is-enabled ssh
            → systemctl list-units --type=service
            → Screenshot output semua commands
   ✓ 3 pts: SSH Configuration Understanding
            → View /etc/ssh/sshd_config
            → Identifikasi 5 parameter penting:
              - Port
              - PermitRootLogin
              - PasswordAuthentication
              - PubkeyAuthentication
              - MaxAuthTries
            → Dokumentasikan arti masing-masing parameter
   ✓ 3 pts: /etc/hosts file configuration
            → Edit /etc/hosts dan tambahkan:
              127.0.0.1 localhost
              192.168.1.100 kali-lab
              192.168.1.101 ubuntu-target
            → Verify dengan: ping kali-lab
            → Screenshot hasil
   ✓ 3 pts: Network configuration
            → View network config: cat /etc/netplan/* atau /etc/network/interfaces
            → View current IP: ip addr show
            → View routing: ip route show
            → View DNS: cat /etc/resolv.conf
            → Dokumentasikan setiap output
   ✓ 3 pts: Firewall (ufw/firewalld)
            → Check firewall status: sudo ufw status
            → Enable firewall: sudo ufw enable
            → Add rule: sudo ufw allow 22/tcp
            → List rules: sudo ufw show added
            → Screenshot semua steps

7. DISTRO COMPARISON & UNDERSTANDING (10 points)
   ✓ 5 pts: Buat tabel perbandingan 4 distro:
            - Ubuntu/Debian
            - Kali Linux
            - RedHat
            - CentOS
            → Kolom: Package Manager, Init System, SSH Service Name, Firewall
            → Screenshot atau tulis di config_comparison.md
   ✓ 5 pts: Command equivalents
            → Tulis 5 command sama-sama di 2 platform berbeda:
              1. Install package
              2. Start SSH service
              3. Check service status
              4. Add firewall rule
              5. View system info
            → Dokumentasikan di equiv_commands.md

8. DOCUMENTATION & PRESENTATION (10 points)
   ✓ 10 pts: Kumpulkan semua file dalam folder submission/
            → Struktur: submission/
            ├── README.md (ringkasan apa yang dikerjakan)
            ├── perubahan_hostname.txt
            ├── commands.txt
            ├── installation_log.txt
            ├── network_info.txt
            ├── ssh_config_explanation.txt
            ├── config_comparison.md
            ├── equiv_commands.md
            ├── firewall_rules.txt
            ├── screenshots/ (folder berisi semua screenshot)
            └── ~/security_lab/ (copy directory structure)
```

**Deliverables:**

```
submission/
├── README.md
│   ├─ Nama & NIM
│   ├─ Ringkasan aktivitas
│   ├─ Tools yang terinstall
│   └─ Kendala & solusi
│
├── perubahan_hostname.txt
│   ├─ Hostname lama
│   ├─ Hostname baru
│   └─ Command yang digunakan
│
├── commands.txt
│   ├─ Semua commands yang dijalankan
│   └─ Penjelasan masing-masing
│
├── installation_log.txt
│   ├─ Daftar tools & version
│   ├─ Tanggal installation
│   └─ Status (success/failed + notes)
│
├── network_info.txt
│   ├─ IP address, netmask, gateway
│   ├─ SSH enabled status
│   └─ SSH connection test hasil
│
├── screenshots/
│   ├─ uname_output.png
│   ├─ hostname_change.png
│   ├─ directory_structure.png
│   ├─ files_content.png
│   ├─ text_processing.png
│   ├─ package_installation.png
│   ├─ ssh_test_from_windows.png
│   └─ [other screenshots]
│
└── security_lab_backup/
    ├─ report.txt
    ├─ lab_targets.txt
    ├─ notes.md
    ├─ scans/
    ├─ archive/
    └─ [full directory structure]
```

**Grading Rubric:**

| Komponen | Score | Kriteria |
|----------|-------|----------|
| System Info & Hostname | 15% | uname command, hostname change verified |
| Directory & File Mgmt | 25% | Directory structure, files created, permissions set |
| Text Processing | 20% | grep, cut, awk, sort, uniq used correctly |
| Package Installation | 20% | Tools installed, versions documented, verified |
| Network Setup | 15% | Network info captured, SSH working, firewall rules added |
| Linux Config & Services | 15% | systemctl, SSH config, /etc/hosts, firewall understood |
| Distro Comparison | 10% | Perbandingan akurat, commands equivalent correct |
| Documentation | 10% | Files terorganisir, penjelasan jelas, complete |
| **TOTAL** | **130%** | **(Max 100 dengan extra credit)** |

**Due Date:** [Satu minggu]

**Submission:**
- Create folder `submission` di home directory
- Upload/submit semua file dalam folder tersebut
- Demonstrasi SSH connectivity test ke instruktur

---

## 📋 E. CONTOH EKSEKUSI LENGKAP

### 5.1 Checklist Quick Reference

Untuk memudahkan, berikut adalah checklist commands yang perlu dikuasai:

```bash
# ===== MUST KNOW =====
pwd                    # Know where you are
cd [path]             # Navigate
ls -la                # List files with details
mkdir -p [path]       # Create directory
touch [file]          # Create file
nano [file]           # Edit file
cat [file]            # View file
cp [src] [dst]        # Copy
mv [src] [dst]        # Move/rename
rm [file]             # Delete
sudo [command]        # Run as root

# ===== SHOULD KNOW =====
grep [pattern] [file] # Search in file
cut -d: -f1 [file]    # Extract column
awk '{print $1}'      # Process text
sort [file]           # Sort lines
uniq [file]           # Remove duplicates
wc -l [file]          # Count lines
pipe: command1 | command2  # Chain commands

# ===== SYSTEM ADMIN =====
uname -a              # System info
hostname              # Machine name
sudo apt install [pkg]  # Install package
sudo apt update       # Update repo
systemctl [action] [service]  # Manage services
```

---

### 5.2 Troubleshooting Common Issues

```bash
# Issue 1: "Permission denied" saat edit file
SOLUSI: Use sudo atau check file permissions
$ sudo nano /etc/hostname    # If system file
$ chmod 644 myfile.txt       # If own file

# Issue 2: "Command not found"
SOLUSI: Package belum terinstall
$ sudo apt install [package-name]
$ which [command]            # Check jika installed

# Issue 3: Directory not empty saat rm
SOLUSI: Use rm -r untuk recursive delete
$ rm -r [folder_name]

# Issue 4: SSH connection refused
SOLUSI: SSH service belum running
$ sudo systemctl start ssh
$ sudo systemctl enable ssh  # Auto-start on boot

# Issue 5: Cannot write to file
SOLUSI: Permission denied, need sudo atau change owner
$ sudo nano [file]           # Use sudo
$ sudo chown $USER [file]    # Change owner
```

---

## 🎓 F. RINGKASAN & NEXT STEPS

---

## 📋 E. CONTOH EKSEKUSI LENGKAP

### 5.1 Contoh Practical Session

**Skenario:** Melakukan reconnaissance terhadap Ubuntu Server di lab

**Timeline: 90 menit**

---

#### **T+0min: Setup & Briefing**

```bash
# Terminal 1: Kali Linux
$ uname -a
Linux kali 5.10.0-13-amd64 #1 SMP Debian 5.10.106-1 x86_64 GNU/Linux

$ whoami
kali

# Cek connectivity
$ ping -c 3 192.168.1.101
PING 192.168.1.101 (192.168.1.101) 56(84) bytes of data.
64 bytes from 192.168.1.101: icmp_seq=1 ttl=64 time=0.245 ms
64 bytes from 192.168.1.101: icmp_seq=2 ttl=64 time=0.182 ms
64 bytes from 192.168.1.101: icmp_seq=3 ttl=64 time=0.156 ms
```

---

#### **T+5min: Passive Information Gathering**

```bash
# Cek IP target
$ ip route show
default via 192.168.1.1 dev eth0 proto dhcp metric 100
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100

# Ping sweep untuk identifikasi host hidup
$ nmap -sn 192.168.1.0/24 | grep "Nmap scan report"
Nmap scan report for 192.168.1.1
Nmap scan report for 192.168.1.100
Nmap scan report for 192.168.1.101
Nmap scan report for 192.168.1.102
```

---

#### **T+15min: Port Scanning**

```bash
# Initial scan
$ nmap 192.168.1.101
Starting Nmap 7.80 ( https://nmap.org ) at 2025-01-15 10:15 UTC
Nmap scan report for 192.168.1.101
Host is up (0.00024s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

# Detailed scan
$ nmap -sV -sC -A 192.168.1.101 -oN ubuntu_scan.txt
Starting Nmap 7.80 ( https://nmap.org ) at 2025-01-15 10:18 UTC
Nmap scan report for ubuntu-target (192.168.1.101)
Host is up (0.00025s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page
MAC Address: 08:00:27:XX:XX:XX (PCS Systemtechnik GmbH)
```

---

#### **T+30min: Network Traffic Analysis**

```bash
# Capture SSH traffic
$ sudo tcpdump -i eth0 -n 'tcp port 22' -w ssh_capture.pcap &

# Generate traffic (di terminal lain)
$ ssh ubuntu@192.168.1.101
# Login & execute command
$ exit

# Analyze dengan tshark (command-line Wireshark)
$ tshark -r ssh_capture.pcap -Y "tcp.flags.syn"
   10   0.046876 192.168.1.100 → 192.168.1.101 TCP 74 52341 → 22 [SYN]
   11   0.047001 192.168.1.101 → 192.168.1.100 TCP 74 22 → 52341 [SYN, ACK]
   12   0.047084 192.168.1.100 → 192.168.1.101 TCP 66 52341 → 22 [ACK]
```

---

#### **T+50min: Enumeration & Analysis**

```bash
# Gather more info
$ nmap -sV --script vuln 192.168.1.101
Starting Nmap 7.80 ( https://nmap.org ) at 2025-01-15 10:35 UTC
Nmap scan report for 192.168.1.101
Host is up (0.00020s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.5
80/tcp open  http    Apache httpd 2.4.41

# Web server enumeration
$ curl -v http://192.168.1.101
* Trying 192.168.1.101:80...
* Connected to 192.168.1.101 (192.168.1.101) port 80 (#0)
> GET / HTTP/1.1
> Host: 192.168.1.101
> User-Agent: curl/7.68.0
> Accept: */*
> 
< HTTP/1.1 200 OK
< Date: Wed, 15 Jan 2025 10:36:45 GMT
< Server: Apache/2.4.41 (Ubuntu)
< Last-Modified: Wed, 15 Jan 2025 10:36:45 GMT
< ETag: "a2d-61066efb3b240"
< Accept-Ranges: bytes
< Content-Length: 2605
< Content-Type: text/html; charset=UTF-8
<
<!DOCTYPE html>
<html>
<head>
    <title>Apache2 Ubuntu Default Page</title>
    ...
```

---

#### **T+70min: Document Findings**

```markdown
# RECONNAISSANCE REPORT
## Target: 192.168.1.101 (ubuntu-target)

### Executive Summary
Target system is an Ubuntu Server running SSH and Apache web server.
Potential vulnerabilities: Outdated software versions, unnecessary services running.

### Findings

#### 1. Active Hosts
- 192.168.1.100 (Attacker/Kali Linux)
- 192.168.1.101 (Target/Ubuntu Server)

#### 2. Open Ports & Services
| Port | Service | Version | Risk |
|------|---------|---------|------|
| 22   | SSH     | OpenSSH 8.2p1 | Medium |
| 80   | HTTP    | Apache 2.4.41 | Low |

#### 3. Service Vulnerabilities
- OpenSSH 8.2p1: No critical CVE found
- Apache 2.4.41: Minor security updates available

#### 4. Network Traffic Analysis
- SSH: Key exchange observed (encrypted)
- HTTP: Plain text HTTP found (should use HTTPS)

### Recommendations
1. Update Apache to latest version
2. Configure HTTPS/SSL
3. Restrict SSH access to specific IPs
4. Enable firewall rules
```

---

#### **T+85min: Q&A & Wrap-up**

```
Diskusi:
Q1: "Port 80 terbuka, artinya apa?"
A: "Web server sedang berjalan. Jika tidak diperlukan, sebaiknya 
   ditutup dengan firewall. Jika diperlukan, gunakan HTTPS (port 443)."

Q2: "Bagaimana cara mencegah port scan seperti ini?"
A: "Menggunakan firewall, changing default ports (security by obscurity 
   tidak recommended), atau blocking ICMP ping."

Q3: "Service version terdeteksi, apa risiko?"
A: "Attacker bisa mencocokkan versi dengan database CVE, 
   mencari exploits yang sesuai."
```

---

### 5.2 Contoh Assignment Output

#### **Student Submission Example:**

```
File: Pertemuan1_Assignment_JohnDoe.md

# ASSIGNMENT 1: NETWORK RECONNAISSANCE

## Part 1: Environment Setup 

### VirtualBox Configuration
- VM Name: Kali-Lab
- OS: Kali Linux 2024.1
- Memory: 4GB
- Storage: 25GB
- Network: NAT + Host-only adapter

Screenshot: [setup_screenshot.png]

### Network Configuration
```bash
$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP>
    inet 127.0.0.1/8 scope host lo

2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP>
    inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0

3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP>
    inet 192.168.56.101/24 brd 192.168.56.255 scope global eth1
```

---

## Part 2: Port Scanning Results 

### Target Information
- Target IP: 192.168.1.101
- Target OS: Ubuntu 20.04 LTS (detected via nmap -O)
- Scan Date: 2025-01-15 10:15 UTC

### Scan Results
```
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu
80/tcp open  http    Apache httpd 2.4.41
443/tcp closed https  
3306/tcp filtered mysql
```

### Analysis
1. FTP service running (port 21) - potential risk
2. SSH service running (port 22) - standard
3. HTTP service running (port 80) - should use HTTPS
4. MySQL filtered (port 3306) - not directly accessible

---

## Part 3: Network Traffic Analysis 

### Captured Packets Analysis
- Total packets captured: 1,247
- SSH traffic: 342 packets
- HTTP traffic: 89 packets
- ARP traffic: 156 packets
- Other: 660 packets

### Key Findings
```
Protocol Distribution:
TCP: 892 packets (71%)
UDP: 245 packets (20%)
ARP: 156 packets (13%)
Other: 54 packets (4%)
```

### Sample Packet Capture
```
Frame 123: SSH Connection Establishment
Source: 192.168.1.100:52341
Destination: 192.168.1.101:22
[SYN] → [SYN, ACK] → [ACK] (Three-way handshake)
Duration: 234ms

Conclusion: SSH connection established successfully
```

---

## Part 4: Linux Practice 

### Commands Executed
```bash
# Directory Management
$ mkdir -p ~/lab_workspace/scans
$ cd ~/lab_workspace

# File Permissions
$ chmod 600 sensitive_data.txt
$ ls -l sensitive_data.txt
-rw------- 1 kali kali 0 Jan 15 10:25 sensitive_data.txt

# Process Monitoring
$ ps aux | grep ssh
root      1234  0.0  0.5  8456  2345 ?  Ss  10:10  0:00 /usr/sbin/sshd -D

# Network Commands
$ netstat -an | grep LISTEN
tcp    0  0 0.0.0.0:22  0.0.0.0:*  LISTEN
tcp    0  0 0.0.0.0:80  0.0.0.0:*  LISTEN
```

---

## Part 5: Conclusions

### Security Assessment Summary

**Offensive Findings:**
-  Successfully identified open ports
-  Detected service versions
-  Captured network traffic
-  Documented attack vectors

**Recommendations:**
1. Disable FTP (use SFTP instead)
2. Update to latest OpenSSH
3. Implement HTTPS
4. Restrict port access via firewall

### Learning Outcomes
-  Understand reconnaissance methodology
-  Use nmap for port scanning
-  Analyze network traffic
-  Linux command proficiency
```

---

## 🎓 F. RINGKASAN & NEXT STEPS

### 6.1 Key Takeaways Pertemuan 1

```
 Defensive vs Offensive Security
   - Defensive: Protect, Monitor, Respond
   - Offensive: Identify, Test, Report

 Linux Fundamentals
   - File management, permissions, processes
   - Network commands, SSH, logging

 Reconnaissance Tools
   - nmap for port scanning
   - Wireshark for traffic analysis
   - SSH for remote access

 Practical Skills
   - Environment setup (VirtualBox + Kali)
   - Information gathering
   - Network analysis
   - Documentation

 Ethical Considerations
   - Always get authorization
   - Document all activities
   - Respect privacy & laws
   - Report findings responsibly
```

### 6.2 Persiapan untuk Pertemuan 2

```
 Pre-Reading:
- TCP/IP networking model (OSI 7 layers)
- Network protocols: TCP, UDP, ICMP
- Port numbers dan services
- Firewall concepts

🛠️ Tools to Install:
- Wireshark (untuk advanced analysis)
- netstat & ss (sudah ada di Linux)
- nmap dengan script NSE

 Practice:
- Scan berbagai targets dengan options berbeda
- Capture traffic dari different services
- Analyze captured traffic dengan filters
```

---

**Prepared by:** Cybersecurity Training Program  
**Effective Date:** January 2025  
**Version:** 1.0
