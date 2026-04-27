# 🐧 Complete Linux Server Hardening Cheatsheet
## ACL, chmod, chown, chattr, visudo & Multi-Hosting Security

---

## 📋 Table of Contents
1. [File Permissions (chmod)](#1-file-permissions-chmod)
2. [File Ownership (chown/chgrp)](#2-file-ownership-chownchgrp)
3. [Access Control Lists (ACL)](#3-access-control-lists-acl)
4. [File Attributes (chattr/lsattr)](#4-file-attributes-chattrlsattr)
5. [Sudo Configuration (visudo)](#5-sudo-configuration-visudo)
6. [User & Group Management](#6-user--group-management)
7. [SSH Hardening](#7-ssh-hardening)
8. [Kernel Hardening (sysctl)](#8-kernel-hardening-sysctl)
9. [Service Hardening](#9-service-hardening)
10. [Audit & Logging](#10-audit--logging)
11. [cPanel/WHM Multi-Hosting Setup](#11-cpanelwhm-multi-hosting-setup)
12. [Complete Server Hardening Script](#12-complete-server-hardening-script)

---

# 1. FILE PERMISSIONS (chmod)

## 🔧 Understanding Permissions

```
Permission Structure:
-rwxrwxrwx
│├─┤├─┤├─┤
│ │  │  └── Others (o)
│ │  └───── Group (g)
│ └──────── User/Owner (u)
└────────── File Type (- = file, d = directory, l = symlink)

Numeric Values:
r (read)    = 4
w (write)   = 2
x (execute) = 1

Common Permissions:
777 = rwxrwxrwx (DANGEROUS - full access)
755 = rwxr-xr-x (typical for directories)
644 = rw-r--r-- (typical for files)
600 = rw------- (private files)
700 = rwx------ (private directories)
```

## 📋 chmod Commands

### Basic Usage
```bash
# Numeric mode
chmod 755 file.sh
chmod 644 document.txt
chmod 600 private.key

# Symbolic mode
chmod u+x file.sh          # Add execute for user
chmod g-w file.txt         # Remove write for group
chmod o-rwx secret.txt     # Remove all for others
chmod a+r public.txt       # Add read for all
chmod u=rwx,g=rx,o=r file  # Set specific permissions

# Recursive
chmod -R 755 /var/www/html/
chmod -R 644 /var/www/html/*.php
```

### Security-Focused Permissions
```bash
# ===== WEB SERVER FILES =====
# Web root directory
chmod 755 /var/www/html

# PHP/HTML files (no execute needed)
chmod 644 /var/www/html/*.php
chmod 644 /var/www/html/*.html

# Directories
find /var/www/html -type d -exec chmod 755 {} \;

# Files
find /var/www/html -type f -exec chmod 644 {} \;

# Upload directories (no script execution)
chmod 755 /var/www/html/uploads
chmod 644 /var/www/html/uploads/*

# ===== CONFIGURATION FILES =====
chmod 600 /etc/shadow
chmod 644 /etc/passwd
chmod 640 /etc/sudoers
chmod 600 ~/.ssh/id_rsa
chmod 644 ~/.ssh/id_rsa.pub
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys

# ===== SENSITIVE FILES =====
chmod 600 /etc/mysql/my.cnf
chmod 600 /var/www/html/.env
chmod 600 /var/www/html/wp-config.php
chmod 600 /etc/ssl/private/*.key

# ===== LOG FILES =====
chmod 640 /var/log/auth.log
chmod 640 /var/log/syslog
chmod 600 /var/log/secure

# ===== SCRIPTS =====
chmod 700 /root/scripts/*.sh
chmod 755 /usr/local/bin/*
```

### Special Permissions
```bash
# SUID (Set User ID) - Run as file owner
chmod u+s /usr/bin/program
chmod 4755 /usr/bin/program

# SGID (Set Group ID) - Run as file group
chmod g+s /var/shared/
chmod 2755 /var/shared/

# Sticky Bit - Only owner can delete
chmod +t /tmp
chmod 1777 /tmp

# Combine special permissions
chmod 4755 file    # SUID + rwxr-xr-x
chmod 2755 dir     # SGID + rwxr-xr-x
chmod 1777 /tmp    # Sticky + rwxrwxrwx

# Remove SUID/SGID from dangerous files
chmod u-s /usr/bin/passwd
chmod g-s /usr/bin/wall

# Find SUID files (security audit)
find / -perm -4000 -type f 2>/dev/null

# Find SGID files
find / -perm -2000 -type f 2>/dev/null

# Find world-writable files
find / -perm -0002 -type f 2>/dev/null

# Find world-writable directories
find / -perm -0002 -type d 2>/dev/null
```

### Umask Configuration
```bash
# View current umask
umask

# Set restrictive umask (files: 640, dirs: 750)
umask 027

# Set in /etc/profile or ~/.bashrc
echo "umask 027" >> /etc/profile

# Default umask values:
# 022 = files 644, dirs 755 (default)
# 027 = files 640, dirs 750 (recommended)
# 077 = files 600, dirs 700 (paranoid)
```

---

# 2. FILE OWNERSHIP (chown/chgrp)

## 📋 chown Commands

### Basic Usage
```bash
# Change owner
chown user file.txt
chown root /etc/important.conf

# Change owner and group
chown user:group file.txt
chown www-data:www-data /var/www/html/

# Change group only
chown :group file.txt
chgrp group file.txt

# Recursive
chown -R user:group /var/www/html/
chgrp -R www-data /var/www/html/

# Copy ownership from another file
chown --reference=source.txt target.txt

# Verbose output
chown -v user:group file.txt

# Only change if current owner matches
chown --from=olduser newuser file.txt
```

### Web Server Ownership
```bash
# ===== APACHE =====
chown -R www-data:www-data /var/www/html/
chown root:root /etc/apache2/apache2.conf

# ===== NGINX =====
chown -R www-data:www-data /var/www/html/
chown root:root /etc/nginx/nginx.conf

# ===== PHP-FPM =====
chown -R www-data:www-data /var/lib/php/sessions/

# ===== Mixed ownership (owner + web group) =====
chown -R $USER:www-data /var/www/html/
find /var/www/html -type d -exec chmod 750 {} \;
find /var/www/html -type f -exec chmod 640 {} \;

# ===== Upload directory =====
chown www-data:www-data /var/www/html/uploads/
chmod 755 /var/www/html/uploads/
```

### System Files Ownership
```bash
# Critical system files
chown root:root /etc/passwd
chown root:shadow /etc/shadow
chown root:root /etc/group
chown root:root /etc/sudoers
chown root:root /boot/grub/grub.cfg

# SSH files
chown root:root /etc/ssh/sshd_config
chown $USER:$USER ~/.ssh
chown $USER:$USER ~/.ssh/authorized_keys
chown $USER:$USER ~/.ssh/id_rsa

# Log files
chown root:adm /var/log/auth.log
chown root:adm /var/log/syslog
chown mysql:mysql /var/log/mysql/

# Cron
chown root:root /etc/crontab
chown root:root /etc/cron.d/
```

### Find and Fix Ownership Issues
```bash
# Find files with no owner
find / -nouser -print 2>/dev/null

# Find files with no group
find / -nogroup -print 2>/dev/null

# Fix orphaned files
find / -nouser -exec chown root {} \;
find / -nogroup -exec chgrp root {} \;

# Find files owned by specific user
find / -user username 2>/dev/null

# Find files owned by UID (deleted user)
find / -uid 1001 2>/dev/null
```

---

# 3. ACCESS CONTROL LISTS (ACL)

## 🔧 Enable ACL Support

```bash
# Check if ACL is enabled
mount | grep acl

# Enable ACL on filesystem
# Edit /etc/fstab:
# /dev/sda1 / ext4 defaults,acl 0 1

# Remount with ACL
mount -o remount,acl /

# Install ACL tools
apt install acl        # Debian/Ubuntu
yum install acl        # RHEL/CentOS
```

## 📋 getfacl - View ACL

```bash
# View ACL of file
getfacl file.txt

# View ACL of directory
getfacl /var/www/html/

# Output format:
# file: file.txt
# owner: root
# group: root
# user::rw-
# user:john:r--
# group::r--
# group:developers:rw-
# mask::rw-
# other::r--
```

## 📋 setfacl - Set ACL

### Basic Usage
```bash
# Add user permission
setfacl -m u:john:rwx file.txt

# Add group permission
setfacl -m g:developers:rw file.txt

# Multiple entries
setfacl -m u:john:rwx,g:dev:rw file.txt

# Remove specific ACL
setfacl -x u:john file.txt
setfacl -x g:developers file.txt

# Remove all ACL
setfacl -b file.txt

# Set default ACL (for new files in directory)
setfacl -d -m u:john:rwx /var/www/html/
setfacl -d -m g:developers:rw /var/www/html/

# Recursive
setfacl -R -m u:john:rx /var/www/html/
setfacl -R -m g:www-data:rwx /var/www/html/

# Copy ACL from another file
getfacl source.txt | setfacl --set-file=- target.txt
```

### Real-World ACL Examples

```bash
# ===== WEB DEVELOPMENT TEAM =====
# Create shared web directory
mkdir /var/www/project
chown root:developers /var/www/project
chmod 2775 /var/www/project

# Give developers group full access
setfacl -R -m g:developers:rwx /var/www/project/
setfacl -R -d -m g:developers:rwx /var/www/project/

# Give web server read access
setfacl -R -m u:www-data:rx /var/www/project/
setfacl -R -d -m u:www-data:rx /var/www/project/

# ===== BACKUP USER ACCESS =====
# Allow backup user to read all web files
setfacl -R -m u:backup:rx /var/www/

# ===== DEVELOPER SPECIFIC ACCESS =====
# Give developer write access to specific directory only
setfacl -R -m u:john:rwx /var/www/html/john_project/
setfacl -R -d -m u:john:rwx /var/www/html/john_project/

# Remove developer access
setfacl -R -x u:john /var/www/html/john_project/

# ===== LOG ACCESS FOR MONITORING =====
# Allow monitoring user to read logs
setfacl -R -m u:monitor:r /var/log/apache2/
setfacl -R -m u:monitor:r /var/log/nginx/

# ===== SHARED UPLOAD DIRECTORY =====
mkdir /var/shared/uploads
setfacl -m g:uploaders:rwx /var/shared/uploads
setfacl -d -m g:uploaders:rwx /var/shared/uploads
setfacl -m o::--- /var/shared/uploads  # No access for others
```

### ACL Mask
```bash
# Set mask (maximum effective permissions)
setfacl -m m::rx file.txt

# View effective permissions
getfacl file.txt
# Output shows effective permissions:
# user:john:rwx    #effective:r-x

# Recalculate mask
setfacl -m m::rwx file.txt
```

### Backup and Restore ACL
```bash
# Backup ACL
getfacl -R /var/www/html > acl_backup.txt

# Restore ACL
setfacl --restore=acl_backup.txt

# Backup with tar (preserves ACL)
tar --acls -cvf backup.tar /var/www/html/

# Restore with tar
tar --acls -xvf backup.tar
```

---

# 4. FILE ATTRIBUTES (chattr/lsattr)

## 📋 lsattr - List Attributes

```bash
# View attributes
lsattr file.txt
lsattr -a /etc/        # Include hidden files
lsattr -d /var/www/    # Directory only
lsattr -R /etc/        # Recursive

# Output example:
# ----i--------e-- file.txt
# i = immutable
# e = extent format (ext4)
```

## 📋 chattr - Change Attributes

### Common Attributes
```
i - Immutable (cannot be modified, deleted, renamed)
a - Append only (can only add data)
s - Secure deletion (zero-fill when deleted)
S - Synchronous updates
A - No atime updates
c - Compressed
d - No dump
e - Extent format
j - Data journaling
t - No tail-merging
u - Undeletable
```

### Basic Usage
```bash
# Add attribute
chattr +i file.txt      # Make immutable
chattr +a logfile.log   # Append only

# Remove attribute
chattr -i file.txt
chattr -a logfile.log

# Multiple attributes
chattr +ia file.txt

# Recursive
chattr -R +i /etc/important/
```

### Security Hardening with chattr

```bash
# ===== PROTECT CRITICAL SYSTEM FILES =====
# Make immutable (cannot be modified even by root!)
chattr +i /etc/passwd
chattr +i /etc/shadow
chattr +i /etc/group
chattr +i /etc/gshadow
chattr +i /etc/sudoers
chattr +i /boot/grub/grub.cfg

# Protect SSH configuration
chattr +i /etc/ssh/sshd_config
chattr +i ~/.ssh/authorized_keys

# Protect web server config
chattr +i /etc/apache2/apache2.conf
chattr +i /etc/nginx/nginx.conf

# ===== PROTECT IMPORTANT WEB FILES =====
chattr +i /var/www/html/index.php
chattr +i /var/www/html/wp-config.php
chattr +i /var/www/html/.htaccess

# ===== APPEND-ONLY FOR LOGS =====
# Logs can only grow, not be modified or deleted
chattr +a /var/log/auth.log
chattr +a /var/log/secure
chattr +a /var/log/syslog
chattr +a /var/log/apache2/access.log
chattr +a /var/log/nginx/access.log

# ===== PROTECT CRON =====
chattr +i /etc/crontab
chattr +i /etc/cron.d/*
chattr +i /var/spool/cron/crontabs/*

# ===== PROTECT KERNEL MODULES =====
chattr +i /lib/modules/

# ===== BEFORE SYSTEM UPDATES =====
# Remove immutable temporarily
chattr -i /etc/passwd
chattr -i /etc/shadow
# ... perform updates ...
# Restore protection
chattr +i /etc/passwd
chattr +i /etc/shadow
```

### Find Protected Files
```bash
# Find all immutable files
lsattr -R / 2>/dev/null | grep "^....i"

# Find all append-only files
lsattr -R / 2>/dev/null | grep "^.....a"

# Script to list all protected files
find / -type f -exec lsattr {} \; 2>/dev/null | grep -E "^-+i"
```

### chattr Hardening Script
```bash
#!/bin/bash
# protect-system.sh

# Critical files to protect
CRITICAL_FILES=(
    "/etc/passwd"
    "/etc/shadow"
    "/etc/group"
    "/etc/gshadow"
    "/etc/sudoers"
    "/etc/ssh/sshd_config"
    "/boot/grub/grub.cfg"
)

# Log files (append-only)
LOG_FILES=(
    "/var/log/auth.log"
    "/var/log/syslog"
    "/var/log/secure"
)

# Protect critical files
echo "Protecting critical files..."
for file in "${CRITICAL_FILES[@]}"; do
    if [ -f "$file" ]; then
        chattr +i "$file"
        echo "Protected: $file"
    fi
done

# Set append-only for logs
echo "Setting append-only for logs..."
for file in "${LOG_FILES[@]}"; do
    if [ -f "$file" ]; then
        chattr +a "$file"
        echo "Append-only: $file"
    fi
done

echo "Protection complete!"
```

---

# 5. SUDO CONFIGURATION (visudo)

## 🔧 Edit Sudoers Safely

```bash
# Always use visudo (syntax checking)
visudo

# Edit specific file
visudo -f /etc/sudoers.d/custom

# Check syntax
visudo -c

# Strict mode
visudo -s
```

## 📋 Sudoers Syntax

```bash
# Basic format:
# user/group  hosts=(runas_user:runas_group) commands

# User can run all commands as root
john    ALL=(ALL:ALL) ALL

# User can run specific commands without password
john    ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx

# Group can run all commands
%admin  ALL=(ALL:ALL) ALL
%sudo   ALL=(ALL:ALL) ALL

# Group with NOPASSWD
%wheel  ALL=(ALL) NOPASSWD: ALL

# Specific commands only
john    ALL=(ALL) /usr/bin/apt, /usr/bin/systemctl

# No password for specific commands
john    ALL=(ALL) NOPASSWD: /usr/bin/apt update, /usr/bin/apt upgrade

# Run as specific user
john    ALL=(www-data) /usr/bin/php

# Restrict to specific host
john    webserver=(ALL) /usr/bin/systemctl restart apache2
```

## 📜 Secure Sudoers Configuration

```bash
# /etc/sudoers.d/security

# ===== DEFAULT SETTINGS =====
Defaults    env_reset
Defaults    mail_badpass
Defaults    secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
Defaults    logfile="/var/log/sudo.log"
Defaults    log_input, log_output
Defaults    iolog_dir="/var/log/sudo-io/%{user}"
Defaults    requiretty
Defaults    use_pty
Defaults    passwd_timeout=1
Defaults    timestamp_timeout=5
Defaults    passwd_tries=3
Defaults    badpass_message="Wrong password, access denied"
Defaults    insults

# ===== RESTRICT ROOT LOGIN =====
Defaults    !root_sudo
Defaults    rootpw

# ===== ADMIN GROUP =====
%admin ALL=(ALL:ALL) ALL

# ===== DEVELOPER GROUP =====
# Can restart web services, view logs
%developers ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx, \
                                /usr/bin/systemctl restart apache2, \
                                /usr/bin/systemctl restart php*-fpm, \
                                /usr/bin/tail -f /var/log/nginx/*, \
                                /usr/bin/tail -f /var/log/apache2/*

# ===== MONITORING GROUP =====
%monitoring ALL=(ALL) NOPASSWD: /usr/bin/systemctl status *, \
                                 /usr/bin/journalctl, \
                                 /usr/bin/top, \
                                 /usr/bin/htop, \
                                 /usr/bin/netstat, \
                                 /usr/bin/ss

# ===== BACKUP USER =====
backup ALL=(ALL) NOPASSWD: /usr/bin/rsync, \
                           /usr/bin/tar, \
                           /usr/bin/mysqldump

# ===== SPECIFIC USER PERMISSIONS =====
# John can only manage nginx
john ALL=(ALL) NOPASSWD: /usr/bin/systemctl * nginx, \
                         /usr/bin/nginx -t, \
                         /usr/bin/nginx -s reload

# ===== DENY DANGEROUS COMMANDS =====
# Create command aliases
Cmnd_Alias DANGEROUS = /bin/rm, /bin/dd, /sbin/mkfs*, /sbin/fdisk, \
                       /bin/chmod 777 *, /bin/chown * /*, \
                       /usr/bin/passwd root

# Deny dangerous commands for developers
%developers ALL=(ALL) !DANGEROUS

# ===== WEB HOSTING RESELLER =====
reseller ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx, \
                             /usr/bin/systemctl reload nginx, \
                             /scripts/*, \
                             /usr/local/cpanel/bin/*

# ===== EMERGENCY ACCESS =====
# Emergency user can do anything (use sparingly)
emergency ALL=(ALL:ALL) ALL
```

## 📋 Sudoers.d Directory

```bash
# Create separate files for organization
# /etc/sudoers.d/

# developers
echo '%developers ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx' > /etc/sudoers.d/developers
chmod 440 /etc/sudoers.d/developers

# monitoring
echo '%monitoring ALL=(ALL) NOPASSWD: /usr/bin/systemctl status *' > /etc/sudoers.d/monitoring
chmod 440 /etc/sudoers.d/monitoring

# Validate all files
visudo -c
```

---

# 6. USER & GROUP MANAGEMENT

## 📋 User Management

```bash
# ===== CREATE USERS =====
# Standard user
useradd -m -s /bin/bash username

# User with specific UID/GID
useradd -m -u 1500 -g developers username

# System user (no home, no login)
useradd -r -s /usr/sbin/nologin serviceuser

# User with expiry date
useradd -m -e 2026-12-31 tempuser

# User with specific home directory
useradd -m -d /home/custom username

# ===== MODIFY USERS =====
# Change shell
usermod -s /bin/bash username
usermod -s /usr/sbin/nologin username  # Disable login

# Add to group
usermod -aG sudo username
usermod -aG www-data username
usermod -aG docker username

# Lock user
usermod -L username
passwd -l username

# Unlock user
usermod -U username
passwd -u username

# Change home directory
usermod -d /new/home -m username

# Set expiry
usermod -e 2026-12-31 username
chage -E 2026-12-31 username

# ===== DELETE USERS =====
userdel username          # Keep home
userdel -r username       # Remove home
userdel -f username       # Force delete

# ===== PASSWORD MANAGEMENT =====
# Set password
passwd username

# Force password change on next login
passwd -e username
chage -d 0 username

# Set password expiry policy
chage -M 90 username     # Max 90 days
chage -m 7 username      # Min 7 days
chage -W 14 username     # Warn 14 days before

# View password info
chage -l username
```

## 📋 Group Management

```bash
# ===== CREATE GROUPS =====
groupadd developers
groupadd -g 2000 webmasters

# ===== MODIFY GROUPS =====
groupmod -n newname oldname
groupmod -g 2001 groupname

# ===== DELETE GROUPS =====
groupdel groupname

# ===== GROUP MEMBERSHIP =====
# Add user to group
gpasswd -a username groupname
usermod -aG groupname username

# Remove user from group
gpasswd -d username groupname

# Set group admin
gpasswd -A adminuser groupname

# View group members
getent group groupname
members groupname

# View user's groups
groups username
id username
```

## 📋 Security-Focused User Setup

```bash
# ===== CREATE SECURE WEB USER =====
# Create web user with limited access
useradd -r -d /var/www/html -s /usr/sbin/nologin webuser
usermod -aG www-data webuser

# ===== CREATE SFTP-ONLY USER =====
useradd -m -s /usr/sbin/nologin sftpuser
usermod -aG sftponly sftpuser
# Configure SSH for SFTP jail (see SSH section)

# ===== CREATE DEVELOPER USER =====
useradd -m -s /bin/bash developer
usermod -aG developers,www-data developer
passwd developer

# ===== DISABLE UNUSED SYSTEM ACCOUNTS =====
for user in games news uucp proxy list irc gnats; do
    usermod -s /usr/sbin/nologin $user 2>/dev/null
done

# ===== LOCK SYSTEM ACCOUNTS =====
for user in daemon bin sys sync games man lp mail news uucp; do
    passwd -l $user 2>/dev/null
done
```

---

# 7. SSH HARDENING

## 📜 /etc/ssh/sshd_config

```bash
# ===== BASIC SECURITY =====
Port 2222                          # Change default port
Protocol 2                         # SSH2 only
PermitRootLogin no                 # Disable root login
PasswordAuthentication no          # Key-only authentication
PermitEmptyPasswords no            # No empty passwords
ChallengeResponseAuthentication no
UsePAM yes

# ===== AUTHENTICATION =====
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
MaxAuthTries 3
MaxSessions 2
LoginGraceTime 30

# ===== RESTRICT USERS =====
AllowUsers admin john jane
AllowGroups sshusers developers
DenyUsers guest test
DenyGroups noremote

# ===== LOGGING =====
SyslogFacility AUTH
LogLevel VERBOSE

# ===== IDLE TIMEOUT =====
ClientAliveInterval 300
ClientAliveCountMax 2
TCPKeepAlive yes

# ===== FORWARDING =====
AllowTcpForwarding no
X11Forwarding no
AllowAgentForwarding no
PermitTunnel no
GatewayPorts no

# ===== BANNER =====
Banner /etc/ssh/banner.txt

# ===== CRYPTO HARDENING =====
KexAlgorithms curve25519-sha256@libssh.org,ecdh-sha2-nistp521,ecdh-sha2-nistp384,ecdh-sha2-nistp256,diffie-hellman-group-exchange-sha256
Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr,aes192-ctr,aes128-ctr
MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512,hmac-sha2-256,umac-128@openssh.com

# ===== SFTP CHROOT JAIL =====
Subsystem sftp internal-sftp

Match Group sftponly
    ChrootDirectory /home/%u
    ForceCommand internal-sftp
    AllowTcpForwarding no
    X11Forwarding no
```

## 📋 SSH Key Management

```bash
# Generate secure key
ssh-keygen -t ed25519 -a 100 -C "user@hostname"
ssh-keygen -t rsa -b 4096 -C "user@hostname"

# Copy key to server
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@server

# Set permissions
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_rsa
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_rsa.pub
chmod 600 ~/.ssh/authorized_keys
chmod 600 ~/.ssh/config
```

---

# 8. KERNEL HARDENING (sysctl)

## 📜 /etc/sysctl.conf

```bash
# ===== NETWORK SECURITY =====
# Disable IP forwarding
net.ipv4.ip_forward = 0
net.ipv6.conf.all.forwarding = 0

# Disable source routing
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.default.accept_source_route = 0
net.ipv6.conf.all.accept_source_route = 0
net.ipv6.conf.default.accept_source_route = 0

# Disable ICMP redirects
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0
net.ipv6.conf.all.accept_redirects = 0
net.ipv6.conf.default.accept_redirects = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.default.send_redirects = 0

# Enable IP spoofing protection
net.ipv4.conf.all.rp_filter = 1
net.ipv4.conf.default.rp_filter = 1

# Ignore ICMP broadcast
net.ipv4.icmp_echo_ignore_broadcasts = 1

# Ignore bogus ICMP errors
net.ipv4.icmp_ignore_bogus_error_responses = 1

# Log Martian packets
net.ipv4.conf.all.log_martians = 1
net.ipv4.conf.default.log_martians = 1

# ===== SYN FLOOD PROTECTION =====
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_max_syn_backlog = 2048
net.ipv4.tcp_synack_retries = 2
net.ipv4.tcp_syn_retries = 5

# ===== TCP HARDENING =====
net.ipv4.tcp_timestamps = 0
net.ipv4.tcp_sack = 0
net.ipv4.tcp_fin_timeout = 15
net.ipv4.tcp_keepalive_time = 300
net.ipv4.tcp_keepalive_probes = 5
net.ipv4.tcp_keepalive_intvl = 15

# ===== MEMORY PROTECTION =====
kernel.randomize_va_space = 2
kernel.exec-shield = 1
kernel.kptr_restrict = 2
kernel.dmesg_restrict = 1
kernel.perf_event_paranoid = 3
kernel.yama.ptrace_scope = 1

# ===== FILE SYSTEM =====
fs.protected_hardlinks = 1
fs.protected_symlinks = 1
fs.suid_dumpable = 0

# ===== IPv6 (disable if not needed) =====
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
```

## 📋 Apply sysctl

```bash
# Apply changes
sysctl -p

# Apply specific file
sysctl -p /etc/sysctl.d/99-hardening.conf

# View current value
sysctl net.ipv4.ip_forward

# Set temporarily
sysctl -w net.ipv4.ip_forward=0
```

---

# 9. SERVICE HARDENING

## 📋 Disable Unnecessary Services

```bash
# List all services
systemctl list-unit-files --type=service

# Disable unnecessary services
systemctl disable avahi-daemon
systemctl disable cups
systemctl disable bluetooth
systemctl disable rpcbind
systemctl disable nfs-server
systemctl disable smbd
systemctl disable nmbd

# Stop and disable
systemctl stop service && systemctl disable service

# Mask service (prevent starting)
systemctl mask service

# List active services
systemctl list-units --type=service --state=active
```

## 📋 Systemd Service Hardening

```ini
# /etc/systemd/system/myservice.service.d/hardening.conf

[Service]
# User/Group
User=serviceuser
Group=servicegroup

# No root privileges
NoNewPrivileges=true

# Read-only filesystem
ProtectSystem=strict
ProtectHome=true
PrivateTmp=true

# Restrict capabilities
CapabilityBoundingSet=
AmbientCapabilities=

# Restrict namespace
PrivateDevices=true
ProtectKernelTunables=true
ProtectKernelModules=true
ProtectControlGroups=true

# Restrict network
RestrictAddressFamilies=AF_UNIX AF_INET AF_INET6

# Memory protection
MemoryDenyWriteExecute=true

# System call filter
SystemCallFilter=@system-service
SystemCallErrorNumber=EPERM

# Restrict file creation
UMask=0077
```

---

# 10. AUDIT & LOGGING

## 📋 auditd Configuration

```bash
# Install auditd
apt install auditd audispd-plugins

# /etc/audit/rules.d/audit.rules

# Delete all existing rules
-D

# Buffer size
-b 8192

# Failure mode
-f 1

# ===== FILE ACCESS MONITORING =====
# Monitor passwd/shadow changes
-w /etc/passwd -p wa -k identity
-w /etc/shadow -p wa -k identity
-w /etc/group -p wa -k identity
-w /etc/gshadow -p wa -k identity
-w /etc/sudoers -p wa -k sudoers
-w /etc/sudoers.d/ -p wa -k sudoers

# Monitor SSH
-w /etc/ssh/sshd_config -p wa -k sshd

# Monitor cron
-w /etc/crontab -p wa -k cron
-w /etc/cron.d/ -p wa -k cron
-w /var/spool/cron/ -p wa -k cron

# ===== COMMAND MONITORING =====
# Monitor privileged commands
-a always,exit -F path=/usr/bin/sudo -F perm=x -k privileged
-a always,exit -F path=/usr/bin/su -F perm=x -k privileged
-a always,exit -F path=/usr/bin/passwd -F perm=x -k privileged
-a always,exit -F path=/usr/bin/chsh -F perm=x -k privileged
-a always,exit -F path=/usr/bin/chfn -F perm=x -k privileged

# ===== LOGIN MONITORING =====
-w /var/log/faillog -p wa -k logins
-w /var/log/lastlog -p wa -k logins
-w /var/log/tallylog -p wa -k logins

# ===== SYSTEM CALLS =====
# Monitor file deletion
-a always,exit -F arch=b64 -S unlink -S unlinkat -S rename -S renameat -k delete

# Monitor chmod/chown
-a always,exit -F arch=b64 -S chmod -S fchmod -S fchmodat -k perm_mod
-a always,exit -F arch=b64 -S chown -S fchown -S fchownat -S lchown -k owner_mod
```

## 📋 View Audit Logs

```bash
# Search audit logs
ausearch -k identity
ausearch -k sudoers
ausearch -k privileged

# Generate report
aureport --summary
aureport --auth
aureport --login
aureport --file

# Real-time monitoring
tail -f /var/log/audit/audit.log
```

---

# 11. CPANEL/WHM MULTI-HOSTING SETUP

## 🏗️ Server Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    HOSTING SERVER                           │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────┐    │
│  │                 cPanel/WHM                          │    │
│  │  ┌─────────────────────────────────────────────┐    │    │
│  │  │              Account Isolation              │    │    │
│  │  │  ┌─────────┐ ┌─────────┐ ┌─────────┐       │    │    │
│  │  │  │ user1   │ │ user2   │ │ user3   │       │    │    │
│  │  │  │/home/u1 │ │/home/u2 │ │/home/u3 │       │    │    │
│  │  │  │ quota   │ │ quota   │ │ quota   │       │    │    │
│  │  │  │ limits  │ │ limits  │ │ limits  │       │    │    │
│  │  │  └─────────┘ └─────────┘ └─────────┘       │    │    │
│  │  └─────────────────────────────────────────────┘    │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐   │
│  │  Apache/  │ │   MySQL   │ │   Mail    │ │   FTP     │   │
│  │  Nginx    │ │  (per DB) │ │ (per acc) │ │  (jail)   │   │
│  └───────────┘ └───────────┘ └───────────┘ └───────────┘   │
│                                                              │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              Security Layer                            │  │
│  │  • CSF Firewall    • ModSecurity    • CageFS          │  │
│  │  • Imunify360      • cPHulk         • Account limits  │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## 📋 Initial Server Setup

```bash
# ===== STEP 1: INSTALL CPANEL =====
cd /home && curl -o latest -L https://securedownloads.cpanel.net/latest && sh latest

# ===== STEP 2: INITIAL WHM SETUP =====
# Access: https://SERVER_IP:2087
# Complete initial setup wizard

# ===== STEP 3: BASIC SERVER CONFIGURATION =====
# WHM > Server Configuration > Basic WebHost Manager Setup
# - Server hostname (FQDN)
# - Nameservers (ns1.domain.com, ns2.domain.com)
# - Contact email
```

## 🔒 Security Configuration

### CSF Firewall
```bash
# Install CSF
cd /usr/src
wget https://download.configserver.com/csf.tgz
tar -xzf csf.tgz
cd csf && sh install.sh

# Configure for cPanel
# /etc/csf/csf.conf

TESTING = "0"

# Ports for cPanel
TCP_IN = "20,21,22,25,53,80,110,143,443,465,587,993,995,2077,2078,2079,2080,2082,2083,2086,2087,2095,2096"
TCP_OUT = "20,21,22,25,53,80,110,113,443,587,993,995,2077,2078,2079,2080,2082,2083,2086,2087,2095,2096"
UDP_IN = "20,21,53"
UDP_OUT = "20,21,53,113,123"

# Rate limiting
CONNLIMIT = "22;5,80;70,443;70"
PORTFLOOD = "22;tcp;5;300,80;tcp;50;5,443;tcp;50;5"

# SYN flood protection
SYNFLOOD = "1"
SYNFLOOD_RATE = "100/s"
SYNFLOOD_BURST = "150"

# Login failure daemon
LF_SSHD = "5"
LF_CPANEL = "5"
LF_SMTPAUTH = "5"
LF_HTACCESS = "5"

# Restart CSF
csf -r
```

### ModSecurity
```bash
# Enable ModSecurity in WHM
# WHM > Security Center > ModSecurity Configuration

# Enable OWASP rules
# WHM > Security Center > ModSecurity Vendors
# Add OWASP ModSecurity Core Rule Set

# Custom rules location
/etc/apache2/conf.d/modsec/modsec2.user.conf
```

### cPHulk Brute Force Protection
```bash
# WHM > Security Center > cPHulk Brute Force Protection
# Enable and configure:
# - IP-based protection
# - Account-based protection
# - Automatic IP blocking
```

### CageFS (CloudLinux)
```bash
# Install CloudLinux (if using)
# CageFS virtualizes filesystem per user

# Enable CageFS
cagefsctl --enable-all

# Disable for specific user
cagefsctl --disable username

# Update skeleton
cagefsctl --force-update
```

## 📋 Account Isolation

### PHP Configuration per Account
```bash
# WHM > MultiPHP Manager
# - Set PHP version per domain
# - Set PHP handlers (CGI, FastCGI, PHP-FPM)

# WHM > MultiPHP INI Editor
# Per-account PHP settings:
# - disable_functions
# - open_basedir
# - memory_limit
# - max_execution_time
```

### Recommended disable_functions
```ini
# /etc/php.ini or per-account
disable_functions = exec,passthru,shell_exec,system,proc_open,popen,curl_exec,curl_multi_exec,parse_ini_file,show_source,pcntl_exec,proc_close,proc_get_status,proc_nice,proc_terminate
```

### Account Limits (WHM)
```bash
# WHM > Account Functions > Modify Account

# Disk quota
QUOTA_BLOCKS = 5000000  # 5GB

# Bandwidth limit
BWLIMIT = 50000  # 50GB/month

# Max email accounts
MAXPOP = 100

# Max databases
MAXSQL = 10

# Max subdomains
MAXSUB = 25

# Max addon domains
MAXADDON = 5

# Max parked domains
MAXPARK = 10
```

### Apache Configuration for Isolation
```apache
# /etc/apache2/conf.d/userdata/username/domain.com/custom.conf

# Per-user PHP settings
<IfModule mod_php.c>
    php_admin_value open_basedir "/home/username:/tmp:/usr/local/lib/php"
    php_admin_value upload_tmp_dir "/home/username/tmp"
    php_admin_value session.save_path "/home/username/tmp"
</IfModule>

# Resource limits
<IfModule mod_ruid2.c>
    RMode config
    RUidGid username username
</IfModule>

# Disable dangerous features
<Directory "/home/username/public_html">
    Options -ExecCGI -Includes
    AllowOverride FileInfo Indexes Limit Options=Indexes,MultiViews
</Directory>
```

## 📋 Directory Permissions for cPanel

```bash
# Standard cPanel permissions
# Home directory
chmod 711 /home/username
chown username:username /home/username

# Public HTML
chmod 750 /home/username/public_html
chown username:nobody /home/username/public_html

# Files inside public_html
find /home/username/public_html -type f -exec chmod 644 {} \;
find /home/username/public_html -type d -exec chmod 755 {} \;

# Sensitive files
chmod 600 /home/username/public_html/wp-config.php
chmod 600 /home/username/public_html/.htaccess

# Mail directory
chmod 750 /home/username/mail
chown username:mail /home/username/mail

# Logs
chmod 750 /home/username/logs
chmod 640 /home/username/logs/*

# tmp directory
chmod 700 /home/username/tmp
chown username:username /home/username/tmp
```

### Fix Permissions Script
```bash
#!/bin/bash
# fix-permissions.sh

USERNAME=$1

if [ -z "$USERNAME" ]; then
    echo "Usage: $0 username"
    exit 1
fi

# Home directory
chown -R $USERNAME:$USERNAME /home/$USERNAME
chmod 711 /home/$USERNAME

# Public HTML
chown -R $USERNAME:nobody /home/$USERNAME/public_html
find /home/$USERNAME/public_html -type d -exec chmod 755 {} \;
find /home/$USERNAME/public_html -type f -exec chmod 644 {} \;

# Configuration files
[ -f /home/$USERNAME/public_html/wp-config.php ] && chmod 600 /home/$USERNAME/public_html/wp-config.php
[ -f /home/$USERNAME/public_html/.htaccess ] && chmod 644 /home/$USERNAME/public_html/.htaccess
[ -f /home/$USERNAME/public_html/.env ] && chmod 600 /home/$USERNAME/public_html/.env

# Upload directories
for dir in uploads files media tmp cache; do
    if [ -d /home/$USERNAME/public_html/$dir ]; then
        chmod 755 /home/$USERNAME/public_html/$dir
        find /home/$USERNAME/public_html/$dir -type f -exec chmod 644 {} \;
    fi
done

# Mail
chown -R $USERNAME:mail /home/$USERNAME/mail
chmod 750 /home/$USERNAME/mail

# Logs
chmod 750 /home/$USERNAME/logs

# tmp
chown $USERNAME:$USERNAME /home/$USERNAME/tmp
chmod 700 /home/$USERNAME/tmp

echo "Permissions fixed for $USERNAME"
```

## 📋 MySQL Isolation

```bash
# Each cPanel account has own MySQL user
# Database naming: username_dbname
# User naming: username_dbuser

# MySQL user has access only to their databases
# GRANT ALL PRIVILEGES ON `username\_%`.* TO 'username'@'localhost';

# Remote MySQL access (if needed)
# WHM > SQL Services > Remote MySQL
```

## 📋 Email Security

```bash
# ===== SPAM PROTECTION =====
# WHM > Email > Exim Configuration Manager

# Enable SPF checking
# Enable DKIM signing
# Enable DMARC

# Rate limiting
# WHM > Email > Max Hourly Emails Per Domain

# ===== CONFIGURE SPAMASSASSIN =====
# WHM > Email > Apache SpamAssassin
# Enable per-account spam filtering

# ===== CONFIGURE GREYLISTING =====
# WHM > Email > Greylisting
```

## 🛡️ Additional Security Measures

### Install Imunify360 (Recommended)
```bash
# Install Imunify360
wget https://repo.imunify360.cloudlinux.com/defence360/i360deploy.sh
bash i360deploy.sh

# Features:
# - Proactive Defense
# - Malware scanner
# - Patch management
# - Firewall
# - Intrusion detection
```

### Install ClamAV
```bash
# WHM > Manage Plugins > Install ClamAV

# Configure automatic scanning
# WHM > Security Center > ClamAV Scanner
```

### Configure Backups
```bash
# WHM > Backup > Backup Configuration

# Enable:
# - Daily backups
# - Weekly backups
# - Monthly backups
# - Remote backup destination (FTP, SSH, S3)

# Per-account backup
# WHM > Backup > Configure Backup > Users
```

---

# 12. COMPLETE SERVER HARDENING SCRIPT

```bash
#!/bin/bash
# server-hardening.sh
# Complete Linux Server Hardening Script
# Author: TangselSecTeam

set -e

echo "========================================"
echo "    Linux Server Hardening Script"
echo "========================================"

# Check root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit 1
fi

# ===== STEP 1: UPDATE SYSTEM =====
echo "[1/15] Updating system..."
apt update && apt upgrade -y

# ===== STEP 2: CONFIGURE SSH =====
echo "[2/15] Hardening SSH..."
cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup

cat > /etc/ssh/sshd_config << 'EOF'
Port 2222
Protocol 2
PermitRootLogin no
PasswordAuthentication no
PermitEmptyPasswords no
PubkeyAuthentication yes
MaxAuthTries 3
MaxSessions 2
ClientAliveInterval 300
ClientAliveCountMax 2
AllowTcpForwarding no
X11Forwarding no
EOF

systemctl restart sshd

# ===== STEP 3: CONFIGURE SYSCTL =====
echo "[3/15] Hardening kernel parameters..."
cat > /etc/sysctl.d/99-hardening.conf << 'EOF'
net.ipv4.ip_forward = 0
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.all.send_redirects = 0
net.ipv4.conf.all.rp_filter = 1
net.ipv4.icmp_echo_ignore_broadcasts = 1
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_max_syn_backlog = 2048
kernel.randomize_va_space = 2
fs.protected_hardlinks = 1
fs.protected_symlinks = 1
EOF

sysctl -p /etc/sysctl.d/99-hardening.conf

# ===== STEP 4: SET FILE PERMISSIONS =====
echo "[4/15] Setting secure file permissions..."
chmod 600 /etc/shadow
chmod 644 /etc/passwd
chmod 644 /etc/group
chmod 600 /boot/grub/grub.cfg

# ===== STEP 5: PROTECT CRITICAL FILES =====
echo "[5/15] Protecting critical files with chattr..."
chattr +i /etc/passwd
chattr +i /etc/shadow
chattr +i /etc/group
chattr +i /etc/sudoers

# ===== STEP 6: CONFIGURE UMASK =====
echo "[6/15] Setting secure umask..."
echo "umask 027" >> /etc/profile
echo "umask 027" >> /etc/bash.bashrc

# ===== STEP 7: DISABLE UNUSED SERVICES =====
echo "[7/15] Disabling unused services..."
systemctl disable avahi-daemon 2>/dev/null || true
systemctl disable cups 2>/dev/null || true
systemctl disable bluetooth 2>/dev/null || true

# ===== STEP 8: CONFIGURE AUDITD =====
echo "[8/15] Configuring audit daemon..."
apt install auditd -y

cat > /etc/audit/rules.d/hardening.rules << 'EOF'
-w /etc/passwd -p wa -k identity
-w /etc/shadow -p wa -k identity
-w /etc/group -p wa -k identity
-w /etc/sudoers -p wa -k sudoers
-w /etc/ssh/sshd_config -p wa -k sshd
EOF

systemctl enable auditd
systemctl restart auditd

# ===== STEP 9: INSTALL FAIL2BAN =====
echo "[9/15] Installing and configuring fail2ban..."
apt install fail2ban -y

cat > /etc/fail2ban/jail.local << 'EOF'
[DEFAULT]
bantime = 3600
findtime = 600
maxretry = 3

[sshd]
enabled = true
port = 2222
filter = sshd
logpath = /var/log/auth.log
maxretry = 3
EOF

systemctl enable fail2ban
systemctl restart fail2ban

# ===== STEP 10: CONFIGURE UFW =====
echo "[10/15] Configuring firewall..."
apt install ufw -y

ufw default deny incoming
ufw default allow outgoing
ufw allow 2222/tcp    # SSH
ufw allow 80/tcp      # HTTP
ufw allow 443/tcp     # HTTPS
ufw --force enable

# ===== STEP 11: DISABLE USB STORAGE =====
echo "[11/15] Disabling USB storage..."
echo "blacklist usb-storage" > /etc/modprobe.d/usb-storage.conf

# ===== STEP 12: SECURE SHARED MEMORY =====
echo "[12/15] Securing shared memory..."
echo "tmpfs /run/shm tmpfs defaults,noexec,nosuid 0 0" >> /etc/fstab

# ===== STEP 13: CONFIGURE LOGIN BANNER =====
echo "[13/15] Setting login banner..."
cat > /etc/issue.net << 'EOF'
*******************************************************************
*                   AUTHORIZED ACCESS ONLY                        *
* This system is for authorized users only. All activities are    *
* monitored and recorded. Unauthorized access will be prosecuted. *
*******************************************************************
EOF

# ===== STEP 14: LOCK UNUSED ACCOUNTS =====
echo "[14/15] Locking unused accounts..."
for user in games news uucp proxy list; do
    passwd -l $user 2>/dev/null || true
    usermod -s /usr/sbin/nologin $user 2>/dev/null || true
done

# ===== STEP 15: FINAL CHECKS =====
echo "[15/15] Running security checks..."

# Find world-writable files
echo "World-writable files:"
find /etc -perm -0002 -type f 2>/dev/null

# Find SUID files
echo "SUID files:"
find / -perm -4000 -type f 2>/dev/null | head -20

# Find files without owner
echo "Files without owner:"
find / -nouser -o -nogroup 2>/dev/null | head -20

echo "========================================"
echo "    Server Hardening Complete!"
echo "========================================"
echo "IMPORTANT: Test SSH access before closing this session!"
echo "SSH Port changed to: 2222"
echo ""
echo "To unlock critical files for updates:"
echo "chattr -i /etc/passwd /etc/shadow /etc/group /etc/sudoers"
```

---

## 📊 Quick Reference Tables

### File Permission Cheatsheet

| Permission | Numeric | Use Case |
|------------|---------|----------|
| `rwx------` | 700 | Private directories, scripts |
| `rw-------` | 600 | Private files, keys, configs |
| `rwxr-xr-x` | 755 | Public directories, executables |
| `rw-r--r--` | 644 | Public files, HTML, PHP |
| `rwxr-x---` | 750 | Group-accessible directories |
| `rw-r-----` | 640 | Group-readable files |
| `rwxrwxrwt` | 1777 | /tmp (sticky bit) |

### Important System Files

| File | Owner:Group | Permission |
|------|-------------|------------|
| `/etc/passwd` | root:root | 644 |
| `/etc/shadow` | root:shadow | 640 |
| `/etc/group` | root:root | 644 |
| `/etc/sudoers` | root:root | 440 |
| `/etc/ssh/sshd_config` | root:root | 600 |
| `~/.ssh/` | user:user | 700 |
| `~/.ssh/authorized_keys` | user:user | 600 |
| `~/.ssh/id_rsa` | user:user | 600 |

### ACL Quick Reference

| Command | Description |
|---------|-------------|
| `getfacl file` | View ACL |
| `setfacl -m u:user:rwx file` | Add user permission |
| `setfacl -m g:group:rx file` | Add group permission |
| `setfacl -x u:user file` | Remove user ACL |
| `setfacl -b file` | Remove all ACL |
| `setfacl -d -m u:user:rwx dir` | Set default ACL |
| `setfacl -R -m u:user:rx dir` | Recursive ACL |

### chattr Attributes

| Attribute | Flag | Description |
|-----------|------|-------------|
| Immutable | `+i` | Cannot be modified/deleted |
| Append | `+a` | Can only append data |
| Secure Delete | `+s` | Zero-fill on delete |
| No Dump | `+d` | Exclude from dump |
| Undeletable | `+u` | Keep data on delete |

---

# 13. WEBMIN & VIRTUALMIN INSTALLATION

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                      VMware ESXi / Workstation                  │
├─────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────────────────────────────────────────┐  │
│  │                   Ubuntu Server VM                        │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │                   Virtualmin                        │  │  │
│  │  │  ┌─────────────┐  ┌─────────────┐  ┌────────────┐  │  │  │
│  │  │  │   Domain 1  │  │   Domain 2  │  │  Domain N  │  │  │  │
│  │  │  │  - Apache   │  │  - Nginx    │  │  - Apache  │  │  │  │
│  │  │  │  - MySQL DB │  │  - MariaDB  │  │  - PgSQL   │  │  │  │
│  │  │  │  - PHP-FPM  │  │  - PHP 8.x  │  │  - Node.js │  │  │  │
│  │  │  │  - Email    │  │  - Email    │  │  - Email   │  │  │  │
│  │  │  └─────────────┘  └─────────────┘  └────────────┘  │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  │                                                            │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │                    Webmin                           │  │  │
│  │  │  • System Administration    • User Management      │  │  │
│  │  │  • Network Configuration    • Package Updates      │  │  │
│  │  │  • Firewall Management      • Scheduled Tasks      │  │  │
│  │  │  • Log Viewer               • File Manager         │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                  │
│  Network: Bridged/NAT │ RAM: 4GB+ │ Disk: 50GB+ │ CPU: 2+       │
└─────────────────────────────────────────────────────────────────┘
```

## 🖥️ VMware Setup

### Step 1: Create New Virtual Machine

```
VMware Workstation / ESXi Settings:
┌─────────────────────────────────────┐
│ Guest OS: Ubuntu 64-bit             │
│ RAM: 4096 MB (minimum 2GB)          │
│ CPU: 2 cores (recommended 4)        │
│ Disk: 50 GB (thin provisioned)      │
│ Network: Bridged Adapter            │
│ CD/DVD: Ubuntu Server ISO           │
└─────────────────────────────────────┘
```

### VMware Workstation Pro
```bash
# Create VM dengan settings:
# 1. File > New Virtual Machine > Custom
# 2. Hardware compatibility: Workstation 17.x
# 3. Installer disc image: ubuntu-24.04-live-server-amd64.iso
# 4. Guest OS: Linux > Ubuntu 64-bit
# 5. VM Name: webmin-server
# 6. Processors: 2 cores
# 7. Memory: 4096 MB
# 8. Network: Use bridged networking
# 9. Disk: 50 GB, Store as single file
# 10. Finish

# Edit VM Settings setelah create:
# - Add CD/DVD > Use ISO image
# - Network Adapter > Bridged (Automatic)
# - Enable "Replicate physical network connection state"
```

### VMware ESXi
```bash
# Via vSphere Client:
# 1. Right-click Datacenter > New Virtual Machine
# 2. Name: webmin-server
# 3. Compatibility: ESXi 7.0 and later
# 4. Guest OS Family: Linux
# 5. Guest OS Version: Ubuntu Linux (64-bit)
# 6. Customize hardware:
#    - CPU: 2
#    - Memory: 4096 MB
#    - Hard disk: 50 GB (Thin Provision)
#    - Network: VM Network (or your VLAN)
#    - CD/DVD: Datastore ISO file
# 7. Finish and Power On
```

### Network Configuration (Bridged)
```bash
# VMware Virtual Network Editor (Windows)
# 1. Edit > Virtual Network Editor
# 2. Select VMnet0 (Bridged)
# 3. Bridge to: Physical adapter (e.g., Intel Ethernet)
# 4. Apply

# Di dalam VM Ubuntu, set static IP:
sudo nano /etc/netplan/00-installer-config.yaml
```

```yaml
# /etc/netplan/00-installer-config.yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    ens33:  # atau ens160 untuk ESXi
      addresses:
        - 192.168.1.100/24
      routes:
        - to: default
          via: 192.168.1.1
      nameservers:
        addresses:
          - 8.8.8.8
          - 8.8.4.4
```

```bash
# Apply network config
sudo netplan apply

# Verify
ip addr show
ping google.com
```

## 📦 Ubuntu Server Initial Setup

### Step 2: Update & Basic Packages
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install essential packages
sudo apt install -y \
    curl \
    wget \
    gnupg2 \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    lsb-release \
    unzip \
    vim \
    htop \
    net-tools

# Set timezone
sudo timedatectl set-timezone Asia/Jakarta

# Set hostname
sudo hostnamectl set-hostname webmin.yourdomain.com

# Edit hosts file
sudo nano /etc/hosts
# Add: 192.168.1.100 webmin.yourdomain.com webmin
```

## 🌐 WEBMIN INSTALLATION

### Method 1: Official Repository (Recommended)
```bash
# Add Webmin repository
curl -o setup-repos.sh https://raw.githubusercontent.com/webmin/webmin/master/setup-repos.sh
sudo sh setup-repos.sh

# Install Webmin
sudo apt install webmin -y

# Start and enable
sudo systemctl start webmin
sudo systemctl enable webmin

# Check status
sudo systemctl status webmin
```

### Method 2: Manual Installation
```bash
# Download latest Webmin
cd /tmp
wget https://prdownloads.sourceforge.net/webadmin/webmin_2.111_all.deb

# Install dependencies
sudo apt install -y perl libnet-ssleay-perl openssl libauthen-pam-perl \
    libpam-runtime libio-pty-perl apt-show-versions python3

# Install Webmin
sudo dpkg -i webmin_2.111_all.deb

# Fix dependencies if needed
sudo apt --fix-broken install -y
```

### Access Webmin
```bash
# Webmin runs on port 10000
# Access via browser:
https://YOUR_SERVER_IP:10000

# Login with root or sudo user credentials

# If firewall enabled:
sudo ufw allow 10000/tcp
```

### Webmin Initial Configuration
```bash
# Via Web Interface (https://IP:10000)
# 1. Webmin > Webmin Configuration > SSL Encryption
#    - Enable SSL
#    - Generate Let's Encrypt certificate (if public domain)

# 2. Webmin > Webmin Users
#    - Create admin user (don't use root)
#    - Set strong password
#    - Assign modules

# 3. Webmin > Webmin Configuration > IP Access Control
#    - Allow only trusted IPs
#    - Example: 192.168.1.0/24

# 4. Webmin > Webmin Configuration > Port and Address
#    - Change default port (optional, e.g., 12321)
#    - Listen on specific IP only
```

### Webmin Security Hardening
```bash
# /etc/webmin/miniserv.conf

# Change port (optional)
port=12321

# Bind to specific IP
bind=192.168.1.100

# Enable SSL
ssl=1

# Session timeout (seconds)
session_timeout=600

# Failed login blocking
blockhost_failures=5
blockhost_time=60

# Allowed hosts/networks
allow=192.168.1.0/255.255.255.0 127.0.0.1

# Restart Webmin
sudo systemctl restart webmin
```

### Webmin via Command Line
```bash
# Start/Stop/Restart
sudo /etc/init.d/webmin start
sudo /etc/init.d/webmin stop
sudo /etc/init.d/webmin restart

# Or using systemctl
sudo systemctl start webmin
sudo systemctl stop webmin
sudo systemctl restart webmin

# Change admin password
sudo /usr/share/webmin/changepass.pl /etc/webmin root NEWPASSWORD

# Add new user
sudo /usr/share/webmin/create-user.pl admin ADMINPASSWORD
```

## 🏢 VIRTUALMIN INSTALLATION

### Method 1: Automated Install Script (Recommended)
```bash
# Download Virtualmin install script
wget https://software.virtualmin.com/gpl/scripts/virtualmin-install.sh

# Make executable
chmod +x virtualmin-install.sh

# Run installer (Full LAMP stack)
sudo ./virtualmin-install.sh

# Or with options:
# Minimal install (no mail)
sudo ./virtualmin-install.sh --minimal

# With specific bundle
sudo ./virtualmin-install.sh --bundle LAMP
# Options: LAMP, LEMP (Nginx), LLMP (LiteSpeed)

# Installation takes 10-30 minutes
# Follow the prompts
```

### Installation Options
```bash
# Full install with all features
sudo ./virtualmin-install.sh --bundle LAMP --force

# LEMP stack (Nginx instead of Apache)
sudo ./virtualmin-install.sh --bundle LEMP

# Minimal without mail server
sudo ./virtualmin-install.sh --minimal --bundle LAMP

# Unattended install
sudo VIRTUALMIN_NONINTERACTIVE=1 ./virtualmin-install.sh
```

### What Gets Installed
```
Virtualmin GPL includes:
├── Web Server (Apache or Nginx)
├── PHP (multiple versions via PHP-FPM)
├── MySQL/MariaDB
├── Mail Server
│   ├── Postfix (SMTP)
│   ├── Dovecot (IMAP/POP3)
│   └── SpamAssassin
├── DNS Server (BIND)
├── FTP Server (ProFTPD)
├── Firewall (firewalld)
├── Fail2ban
├── ClamAV (antivirus)
└── Webmin modules
```

### Post-Installation Setup
```bash
# Access Virtualmin
https://YOUR_SERVER_IP:10000

# Login with root credentials

# Run Post-Installation Wizard:
# 1. Virtualmin > System Settings > Re-check Configuration
# 2. Follow the wizard steps:
#    - Preload Virtualmin libraries: Yes
#    - Run email domain lookup server: Yes
#    - MySQL password: Set strong password
#    - MySQL database sizes: Yes
#    - DNS configuration: Set nameservers
#    - Password storage mode: Store only hashed
```

### Virtualmin Initial Configuration

#### DNS Setup
```bash
# Via Virtualmin Web Interface:
# Virtualmin > System Settings > Server Templates > Default > DNS

# Primary nameserver: ns1.yourdomain.com
# Secondary nameserver: ns2.yourdomain.com

# Or edit BIND config:
sudo nano /etc/bind/named.conf.options

options {
    directory "/var/cache/bind";
    
    forwarders {
        8.8.8.8;
        8.8.4.4;
    };
    
    dnssec-validation auto;
    listen-on-v6 { any; };
    
    allow-recursion { 127.0.0.1; 192.168.1.0/24; };
    allow-transfer { none; };
};
```

#### Create Virtual Server (Website)
```bash
# Via Web Interface:
# Virtualmin > Create Virtual Server

# Settings:
# - Domain name: example.com
# - Administration password: (strong password)
# - Administration username: example (auto-generated)
# - Contact email: admin@example.com

# Features to enable:
# ✓ Create website
# ✓ Create MySQL database
# ✓ Create DNS zone
# ✓ Create mail domain
# ✓ Setup SSL website

# Click "Create Server"
```

#### PHP Configuration
```bash
# Via Virtualmin:
# Virtualmin > System Settings > Server Templates > Default > PHP

# PHP execution mode: PHP-FPM (recommended)
# PHP version: 8.2 (or latest)

# Install multiple PHP versions:
sudo apt install php7.4-fpm php8.0-fpm php8.1-fpm php8.2-fpm php8.3-fpm

# Common PHP modules:
sudo apt install php8.2-{mysql,curl,gd,mbstring,xml,zip,bcmath,intl,soap,redis,imagick}

# Per-domain PHP version:
# Virtualmin > Edit Virtual Server > PHP Options
# - PHP version: Select version
# - PHP execution mode: FPM
```

#### SSL/TLS Certificates
```bash
# Via Virtualmin:
# Virtualmin > Server Configuration > SSL Certificate

# Request Let's Encrypt Certificate:
# 1. Select domain
# 2. Click "Let's Encrypt" tab
# 3. Request Certificate
# 4. Enable auto-renewal

# Or via command line:
virtualmin generate-letsencrypt-cert --domain example.com --renew --web
```

### Virtualmin Command Line
```bash
# Create virtual server
virtualmin create-domain --domain example.com --pass SecurePass123 \
    --features-from-template default

# List virtual servers
virtualmin list-domains

# Delete virtual server
virtualmin delete-domain --domain example.com

# Backup domain
virtualmin backup-domain --domain example.com --dest /backup/

# Restore domain
virtualmin restore-domain --source /backup/example.com.tar.gz

# Modify domain
virtualmin modify-domain --domain example.com --quota 10000

# Disable domain
virtualmin disable-domain --domain example.com

# Enable domain
virtualmin enable-domain --domain example.com

# List users
virtualmin list-users --domain example.com

# Create mailbox
virtualmin create-user --domain example.com --user john --pass Password123 \
    --quota 1000 --mail-quota 500
```

### Virtualmin Security Hardening

#### Firewall Configuration
```bash
# Virtualmin uses firewalld by default
# Check status
sudo firewall-cmd --state

# List allowed services
sudo firewall-cmd --list-all

# Required ports:
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --permanent --add-service=smtp
sudo firewall-cmd --permanent --add-service=smtps
sudo firewall-cmd --permanent --add-service=imap
sudo firewall-cmd --permanent --add-service=imaps
sudo firewall-cmd --permanent --add-service=pop3
sudo firewall-cmd --permanent --add-service=pop3s
sudo firewall-cmd --permanent --add-service=dns
sudo firewall-cmd --permanent --add-port=10000/tcp  # Webmin
sudo firewall-cmd --permanent --add-port=20000/tcp  # Usermin

sudo firewall-cmd --reload
```

#### Fail2ban for Virtualmin
```bash
# /etc/fail2ban/jail.local

[DEFAULT]
bantime = 3600
findtime = 600
maxretry = 5

[sshd]
enabled = true

[webmin-auth]
enabled = true
port = 10000
filter = webmin-auth
logpath = /var/webmin/miniserv.log

[postfix]
enabled = true

[dovecot]
enabled = true

[proftpd]
enabled = true

# Restart fail2ban
sudo systemctl restart fail2ban
```

#### Apache Security (Virtualmin)
```bash
# /etc/apache2/conf-available/security.conf

ServerTokens Prod
ServerSignature Off
TraceEnable Off

Header always set X-Content-Type-Options nosniff
Header always set X-Frame-Options SAMEORIGIN
Header always set X-XSS-Protection "1; mode=block"
Header always set Referrer-Policy "strict-origin-when-cross-origin"

# Enable
sudo a2enconf security
sudo systemctl reload apache2
```

#### Directory Permissions for Virtualmin
```bash
# Standard Virtualmin home structure:
# /home/username/
# ├── public_html/      (website files)
# ├── domains/          (addon domains)
# ├── logs/             (access/error logs)
# ├── Maildir/          (email)
# └── etc/              (domain configs)

# Fix permissions for a domain:
virtualmin fix-domain-permissions --domain example.com

# Manual fix:
DOMAIN_USER="example"
chown -R $DOMAIN_USER:$DOMAIN_USER /home/$DOMAIN_USER
find /home/$DOMAIN_USER/public_html -type d -exec chmod 755 {} \;
find /home/$DOMAIN_USER/public_html -type f -exec chmod 644 {} \;
chmod 750 /home/$DOMAIN_USER
chmod 710 /home/$DOMAIN_USER/public_html
```

## 📊 Webmin vs Virtualmin Comparison

| Feature | Webmin | Virtualmin |
|---------|--------|------------|
| **Purpose** | System administration | Web hosting management |
| **Users** | Sysadmins | Hosting providers |
| **Domains** | No domain management | Multi-domain hosting |
| **Email** | Basic mail config | Full mail hosting |
| **DNS** | Basic DNS | Full DNS management |
| **Databases** | MySQL admin | Per-domain databases |
| **SSL** | Manual setup | Auto Let's Encrypt |
| **Backups** | Basic | Per-domain backups |
| **User Isolation** | None | Full account isolation |
| **Port** | 10000 | 10000 (shared) |
| **Price** | Free | GPL (free) / Pro ($) |

## 🔧 Troubleshooting

### Common Issues

```bash
# ===== WEBMIN NOT STARTING =====
# Check logs
sudo tail -f /var/webmin/miniserv.log

# Check port
sudo netstat -tlnp | grep 10000

# Restart service
sudo systemctl restart webmin

# ===== SSL CERTIFICATE ERROR =====
# Regenerate SSL cert
sudo /usr/share/webmin/setup-ssl.pl

# ===== FORGOT PASSWORD =====
# Reset root password
sudo /usr/share/webmin/changepass.pl /etc/webmin root newpassword

# ===== VIRTUALMIN LICENSE =====
# Check license status
virtualmin list-licenses

# Re-register (GPL is free)
# No license needed for GPL version

# ===== DATABASE CONNECTION FAILED =====
# Check MySQL status
sudo systemctl status mysql

# Reset MySQL root password
sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'newpassword';
FLUSH PRIVILEGES;

# ===== DNS NOT RESOLVING =====
# Check BIND status
sudo systemctl status named

# Test DNS
dig @localhost example.com

# Check zone files
sudo named-checkzone example.com /var/named/example.com.hosts

# ===== EMAIL NOT WORKING =====
# Check Postfix
sudo systemctl status postfix
sudo tail -f /var/log/mail.log

# Check Dovecot
sudo systemctl status dovecot
sudo doveadm auth test username password

# ===== APACHE/NGINX NOT STARTING =====
# Check syntax
sudo apache2ctl configtest
sudo nginx -t

# Check logs
sudo tail -f /var/log/apache2/error.log
sudo tail -f /var/log/nginx/error.log
```

### VMware Specific Issues

```bash
# ===== SLOW DISK PERFORMANCE =====
# Enable paravirtual SCSI
# VM Settings > Hard Disk > Virtual Device Node > SCSI 0:0
# VM Settings > Add > SCSI Controller > VMware Paravirtual

# ===== NETWORK DISCONNECTS =====
# Install VMware Tools
sudo apt install open-vm-tools

# Or mount VMware Tools ISO and install
sudo mkdir /mnt/cdrom
sudo mount /dev/cdrom /mnt/cdrom
cd /mnt/cdrom
sudo ./vmware-install.pl

# ===== TIME SYNC ISSUES =====
# Sync with host
sudo vmware-toolbox-cmd timesync enable

# Or use NTP
sudo apt install chrony
sudo systemctl enable chrony

# ===== SCREEN RESOLUTION =====
# For GUI (if installed)
sudo apt install open-vm-tools-desktop

# ===== COPY-PASTE NOT WORKING =====
# Enable in VM Settings
# VM > Settings > Options > Guest Isolation
# Enable "Copy and paste between host and guest"
```

## 📝 Quick Setup Checklist

```bash
# ===== COMPLETE SETUP CHECKLIST =====

# [ ] 1. VMware VM Created
#     - Ubuntu Server ISO attached
#     - 4GB RAM, 2 CPU, 50GB disk
#     - Bridged network

# [ ] 2. Ubuntu Installed
#     - Static IP configured
#     - Hostname set
#     - System updated

# [ ] 3. Webmin Installed
#     - Repository added
#     - Package installed
#     - Service running

# [ ] 4. Virtualmin Installed
#     - Install script completed
#     - Post-install wizard done
#     - Configuration checked

# [ ] 5. Security Configured
#     - Firewall enabled
#     - Fail2ban configured
#     - SSL certificates installed
#     - Access controls set

# [ ] 6. First Domain Created
#     - Virtual server added
#     - Database created
#     - SSL enabled
#     - Email configured

# [ ] 7. Backup Configured
#     - Scheduled backups set
#     - Remote destination configured
```

---

**Author:** TangselSecTeam  
**Version:** 1.1  
**Last Updated:** January 2026
