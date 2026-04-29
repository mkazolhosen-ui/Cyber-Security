#  Cybersecurity Learning Log

---

##  2026-03-02

### Focus

Networking Basics + Nmap Introduction

###  Key Concepts

* TCP/IP layers and communication flow
* Difference between TCP and UDP
* Common ports (21, 22, 80, 443)

### 🧪 Practical Work

* Ran:
  nmap -sC -sV <target>
* Identified open ports and services

### Challenges

* Confusion about Nmap script outputs
* Didn’t fully understand service versions

###  Insights

* Enumeration is the most important step
* Even simple scans reveal a lot of info

###  Next Steps

* Learn advanced Nmap flags
* Start HTB "Meow"

---

## 2026-03-03

### Focus

SMB Enumeration + HTB Practice

### Key Concepts

* SMB protocol basics
* Anonymous login vulnerability

###  Practical Work

* Completed HTB "Meow"
* Enumerated SMB shares

###  Challenges

* Didn’t know which tool to use first
* Needed hints during exploitation

###  Insights

* Always check for anonymous access
* Enumeration > exploitation

### Next Steps

* Start "Fawn"
* Practice SMB tools

---

## 🗓️ 2026-03-04

### Focus

Hands-on Practice (HTB Starting Point)

### 🧪 Practical Work

* Completed:

  * Meow ✅
  * Fawn ✅
  * Dancing ✅

### Challenges

* Took time to understand attack flow
* Needed hints for SMB exploitation

### Insights

* Repetition improves speed
* Understanding services is key

### Next Steps

* Start "Redeemer"
* Learn Redis basics


## 2026-03-05

### Focus

Redis Enumeration & HTB Practice

###  Key Concepts

* Redis database basics
* Unauthenticated service exposure
* Key-value data retrieval

### 🧪Practical Work

* Completed HTB "Redeemer"
* Connected using:
  redis-cli -h 10.129.136.187
* Retrieved keys using:
  keys *
* Extracted flag using:
  get flag

###  Challenges

* First time interacting with Redis
* Didn’t know commands initially

### Insights

* Some services don’t require authentication (critical misconfiguration)
* Enumeration is often enough to gain access
* Always check for open databases like Redis

### Next Steps

* Practice more enumeration techniques
* Start next HTB machine (Explosion / Preignition)
* Learn basic database security concepts

