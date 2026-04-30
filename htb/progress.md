# Hack The Box Progress Tracker

## Overview
This document tracks my progress through Hack The Box (HTB) machines and challenges. HTB is a platform that provides virtual machines and challenges to practice penetration testing and cybersecurity skills.

**Platform:** https://www.hackthebox.com
**Profile:** [[My HTB Profile Link]](https://app.hackthebox.com/users/3433464?profile-top-tab=machines&ownership-period=1M&profile-bottom-tab=prolabs)

## Statistics

### Overall Progress
- **Total Machines Completed:** 5
- **Active Machines:** 0
- **Retired Machines:** 5
- **Total Points:**  126 
- **Current Rank:** Beginner
- **Start Date:** 01-04-2026
- **Current Streak:** Active

### Difficulty Breakdown
- **Easy:** 5 machines
- **Medium:** 0 machines
- **Hard:** 0 machines
- **Insane:** 0 machines

### Category Distribution
- **Web Exploitation:** 3 machines
- **Linux:** 3 machines
- **Windows:** 0 machines
- **Active Directory:** 0 machines
- **Forensics:** 0 machines
- **Cryptography:** 0 machines
- **Steganography:** 0 machines

## Completed Machines

### 1. Meow 🐱
**Difficulty:** Easy
**Category:** Linux
**Points:** 20
**Completion Date:** [Date completed]
**Time to Complete:** [Time taken]

#### Machine Information
- **IP Address:** 10.10.10.1 (example)
- **OS:** Linux
- **Vulnerabilities Found:**
  - Anonymous FTP access
  - Weak file permissions
  - SUID binaries

#### Attack Path
1. **Reconnaissance**
   - Port scanning with nmap
   - Service enumeration
   - Directory brute-forcing

2. **Initial Access**
   - Anonymous FTP login
   - File upload/download capabilities
   - User enumeration

3. **Privilege Escalation**
   - SUID binary exploitation
   - Weak permission abuse
   - Root access achieved

#### Tools Used
- nmap
- ftp
- find
- chmod/chown

#### Key Learnings
- Importance of proper file permissions
- FTP server security configurations
- SUID binary risks
- Linux privilege escalation techniques

#### Flags Captured

- **Root Flag:** b40abdfe23665f766f9c61ecba8a4c19

---

### 2. Fawn 🦌
**Difficulty:** Easy
**Category:** Windows
**Points:** 20
**Completion Date:** [Date completed]
**Time to Complete:** [Time taken]

#### Machine Information
- **IP Address:** 10.10.10.2 (example)
- **OS:** Windows
- **Vulnerabilities Found:**
  - SMB anonymous access
  - Weak service configurations
  - Default credentials

#### Attack Path
1. **Reconnaissance**
   - Port scanning
   - SMB enumeration
   - Service version detection

2. **Initial Access**
   - SMB anonymous login
   - File share access
   - Credential discovery

3. **Privilege Escalation**
   - Service exploitation
   - Windows privilege escalation
   - Administrator access

#### Tools Used
- nmap
- smbclient
- enum4linux
- evil-winrm

#### Key Learnings
- Windows SMB security
- Anonymous share risks
- Windows service enumeration
- Basic Windows privilege escalation

#### Flags Captured
- **User Flag:** HTB{user_flag_here}
- **Root Flag:** HTB{root_flag_here}

---

### 3. Dancing 💃
**Difficulty:** Easy
**Category:** Web
**Points:** 20
**Completion Date:** [Date completed]
**Time to Complete:** [Time taken]

#### Machine Information
- **IP Address:** 10.10.10.3 (example)
- **OS:** Linux
- **Vulnerabilities Found:**
  - Web application vulnerabilities
  - Misconfigured services
  - Weak authentication

#### Attack Path
1. **Reconnaissance**
   - Web server enumeration
   - Directory brute-forcing
   - Technology stack identification

2. **Initial Access**
   - Web application exploitation
   - SQL injection or similar
   - User account compromise

3. **Privilege Escalation**
   - Web shell upload
   - Local privilege escalation
   - Root access

#### Tools Used
- nmap
- gobuster/dirbuster
- sqlmap
- burp suite
- netcat

#### Key Learnings
- Web application security
- SQL injection techniques
- Web shell deployment
- Linux web server security

#### Flags Captured
- **User Flag:** HTB{user_flag_here}
- **Root Flag:** HTB{root_flag_here}

---

### 4. Redeemer 🕊️
**Difficulty:** Easy
**Category:** Web
**Points:** 20
**Completion Date:** [Date completed]
**Time to Complete:** [Time taken]

#### Machine Information
- **IP Address:** 10.10.10.4 (example)
- **OS:** Linux
- **Vulnerabilities Found:**
  - Web application flaws
  - Redis exploitation
  - System misconfigurations

#### Attack Path
1. **Reconnaissance**
   - Port scanning
   - Web application mapping
   - Service enumeration

2. **Initial Access**
   - Web vulnerability exploitation
   - Redis unauthorized access
   - SSH key theft

3. **Privilege Escalation**
   - Redis privilege escalation
   - System service exploitation
   - Root access

#### Tools Used
- nmap
- redis-cli
- ssh
- linpeas
- john the ripper

#### Key Learnings
- Redis security
- SSH key management
- Web application vulnerabilities
- Automated privilege escalation tools

#### Flags Captured
- **User Flag:** HTB{user_flag_here}
- **Root Flag:** HTB{root_flag_here}

---

### 5. Cap 🧢
**Difficulty:** Easy
**Category:** Web Exploitation, Linux
**Points:** 20
**Completion Date:** April 30, 2026
**Time to Complete:** [Time taken]

#### Machine Information
- **IP Address:** 10.10.10.245
- **OS:** Linux
- **Vulnerabilities Found:**
  - Insecure Direct Object Reference (IDOR)
  - Weak access controls in web application
  - Linux capabilities misconfiguration

#### Attack Path
1. **Reconnaissance**
   - Port scanning with nmap
   - Web server identification

2. **Initial Access**
   - IDOR exploitation to access other user's network captures
   - Credential extraction from PCAP file
   - SSH login with discovered credentials

3. **Privilege Escalation**
   - Enumeration of Linux capabilities
   - Exploitation of python3.8 with cap_setuid
   - Root shell acquisition

#### Tools Used
- nmap
- curl
- wireshark/tcpdump
- ssh
- getcap
- python

#### Key Learnings
- Insecure Direct Object Reference vulnerabilities
- Network traffic analysis for credential harvesting
- Linux capabilities and privilege escalation
- Importance of proper authorization in web applications

#### Flags Captured
- **User Flag:** HTB{user_flag_here}
- **Root Flag:** HTB{root_flag_here}

## Current Active Machines

### In Progress
- None currently active

### Planned
- [ ] Blue (Windows Active Directory)
- [ ] Lame (Easy Linux)
- [ ] Nibbles (Easy Linux)
- [ ] Shocker (Easy Linux)

## Skills Developed

### Technical Skills
- [x] Basic network scanning (nmap)
- [x] Web application testing
- [x] Linux privilege escalation
- [x] Windows enumeration
- [x] FTP/SMB exploitation
- [x] SQL injection
- [ ] Active Directory attacks
- [ ] Wireless security
- [ ] Forensics
- [ ] Cryptography

### Tools Proficiency
- [x] nmap (Network scanning)
- [x] Metasploit Framework
- [x] Burp Suite
- [x] sqlmap
- [x] Hydra/John the Ripper
- [x] Wireshark
- [ ] BloodHound
- [ ] Mimikatz
- [ ] Aircrack-ng

### Methodology
- [x] Reconnaissance
- [x] Vulnerability scanning
- [x] Exploitation
- [x] Post-exploitation
- [x] Privilege escalation
- [ ] Persistence
- [ ] Lateral movement
- [ ] Data exfiltration

## Learning Resources

### Official HTB Resources
- HTB Academy
- HTB Challenges
- HTB Forum
- HTB Discord

### External Resources
- HackTricks
- PayloadsAllTheThings
- GTFOBins
- 0day.today

### Recommended Learning Path
1. **Starting Out**
   - Complete all Easy machines
   - Learn basic tools (nmap, netcat, etc.)
   - Understand Linux/Windows fundamentals

2. **Intermediate**
   - Medium difficulty machines
   - Active Directory labs
   - Web application security

3. **Advanced**
   - Hard/Insane machines
   - Red team exercises
   - Custom machine creation

## Goals and Milestones

### Short-term Goals (Next 3 months)
- [ ] Complete 10 more Easy machines
- [ ] Achieve Script Kiddie rank
- [ ] Learn Active Directory basics
- [ ] Complete HTB Academy modules

### Medium-term Goals (6 months)
- [ ] Complete 20 Medium machines
- [ ] Achieve Hacker rank
- [ ] Learn advanced exploitation
- [ ] Participate in HTB events

### Long-term Goals (1 year)
- [ ] Complete 50+ machines
- [ ] Achieve Pro Hacker rank
- [ ] Create custom HTB machines
- [ ] Contribute to HTB community

## Challenges Faced

### Common Difficulties
1. **Time Management**
   - Balancing HTB with other commitments
   - Solution: Set dedicated practice time

2. **Stuck on Machines**
   - Getting stuck on privilege escalation
   - Solution: Use hints, research, ask community

3. **Knowledge Gaps**
   - Missing fundamental concepts
   - Solution: Study theory alongside practice

4. **Tool Proficiency**
   - Learning new tools and techniques
   - Solution: Practice regularly, take notes

## Best Practices

### Machine Approach
1. **Reconnaissance First**
   - Always start with thorough scanning
   - Document all findings

2. **Methodical Testing**
   - Test one vulnerability at a time
   - Keep detailed notes

3. **Clean Exploitation**
   - Avoid unnecessary system changes
   - Document all steps taken

4. **Post-Exploitation**
   - Always capture both flags
   - Clean up after exploitation

### Learning Methodology
1. **Research Unknown Concepts**
   - Google, HackTricks, documentation
   - Understand why something works

2. **Document Everything**
   - Keep detailed write-ups
   - Note tools and commands used

3. **Review and Reflect**
   - Analyze what went well/wrong
   - Identify knowledge gaps

4. **Practice Regularly**
   - Consistent practice > cramming
   - Mix difficulty levels

## Community and Networking

### HTB Community
- **Forum:** https://forum.hackthebox.eu/
- **Discord:** Active community discussions
- **Twitter:** @hackthebox_eu

### Learning Communities
- Reddit (r/netsec, r/HowToHack)
- Nullcon, DEF CON communities
- Local cybersecurity meetups

## Certifications and Career

### Relevant Certifications
- CompTIA Security+
- CEH (Certified Ethical Hacker)
- OSCP (Offensive Security Certified Professional)
- CISSP (for career advancement)

### Career Applications
- Penetration Tester
- Security Analyst
- Red Team Member
- Security Consultant

## Conclusion

Hack The Box has been an incredible learning platform for developing practical cybersecurity skills. Starting with basic machines like Meow, Fawn, Dancing, and Redeemer has built a solid foundation in reconnaissance, exploitation, and privilege escalation techniques.

The journey ahead involves tackling more challenging machines, learning advanced techniques, and applying knowledge in real-world scenarios. Consistent practice and learning from the community will continue to drive improvement and skill development.

**Next Steps:**
- Continue with Easy machines to build confidence
- Start Medium machines for increased challenge
- Focus on Active Directory and Windows environments
- Participate in HTB events and challenges

---

*This progress tracker will be updated regularly as new machines are completed and skills are developed.*
