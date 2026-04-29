# Nmap: Network Mapper - Network Discovery and Security Auditing Tool

## Introduction

Nmap (Network Mapper) is a free and open-source utility for network discovery and security auditing. Created by Gordon Lyon (Fyodor), Nmap is one of the most powerful and versatile network scanning tools available. It can discover hosts, services, operating systems, and vulnerabilities on a network.

## Installation

### Linux
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nmap

# CentOS/RHEL/Fedora
sudo yum install nmap  # or dnf install nmap

# Arch Linux
sudo pacman -S nmap
```

### macOS
```bash
# Using Homebrew
brew install nmap

# Using MacPorts
sudo port install nmap
```

### Windows
- Download from https://nmap.org/download.html
- Run the installer
- Add to PATH for command-line usage

### From Source
```bash
wget https://nmap.org/dist/nmap-7.94.tar.bz2
tar xjf nmap-7.94.tar.bz2
cd nmap-7.94
./configure
make
sudo make install
```

## Basic Usage

### Host Discovery
```bash
# Ping scan (host discovery only)
nmap -sn 192.168.1.0/24

# ARP scan (fast for local network)
nmap -PR 192.168.1.0/24

# TCP SYN ping
nmap -PS 192.168.1.1

# UDP ping
nmap -PU 192.168.1.1
```

### Port Scanning
```bash
# Default scan (TCP SYN scan, top 1000 ports)
nmap 192.168.1.1

# Scan specific ports
nmap -p 80,443,22 192.168.1.1

# Scan port range
nmap -p 1-1000 192.168.1.1

# Scan all ports
nmap -p- 192.168.1.1

# UDP scan
nmap -sU 192.168.1.1
```

## Scan Types

### TCP Scans
- **TCP SYN scan (-sS):** Default, stealthy, half-open scan
- **TCP Connect scan (-sT):** Full TCP connection
- **TCP ACK scan (-sA):** Used for firewall rule detection
- **TCP Window scan (-sW):** Similar to ACK scan
- **TCP Maimon scan (-sM):** Uses FIN and ACK flags
- **TCP Idle scan (-sI):** Uses zombie host for stealth
- **TCP FIN scan (-sF):** Sends FIN packets
- **TCP Xmas scan (-sX):** Sets FIN, PSH, URG flags
- **TCP Null scan (-sN):** No flags set

### UDP Scans
- **UDP scan (-sU):** Sends UDP packets to detect open UDP ports

### Other Scan Types
- **SCTP INIT scan (-sY):** For SCTP protocols
- **SCTP COOKIE-ECHO scan (-sZ):** Advanced SCTP scanning
- **IP Protocol scan (-sO):** Scans for IP protocols

## Host Discovery Techniques

### Ping Types
- **ICMP Echo (-PE):** Standard ping
- **TCP SYN Ping (-PS):** TCP SYN to port 80
- **TCP ACK Ping (-PA):** TCP ACK to port 80
- **UDP Ping (-PU):** UDP to port 40125
- **ICMP Timestamp (-PP):** ICMP timestamp request
- **ICMP Address Mask (-PM):** ICMP address mask request
- **ARP Ping (-PR):** ARP request (local network only)

### Timing and Performance
```bash
# Timing templates (0-5, higher = slower but stealthier)
nmap -T0 192.168.1.1  # Paranoid
nmap -T1 192.168.1.1  # Sneaky
nmap -T2 192.168.1.1  # Polite
nmap -T3 192.168.1.1  # Normal
nmap -T4 192.168.1.1  # Aggressive
nmap -T5 192.168.1.1  # Insane

# Custom timing
nmap --min-rate 100 --max-rate 200 192.168.1.1
```

## Service and Version Detection

### Service Detection
```bash
# Version detection
nmap -sV 192.168.1.1

# Aggressive service detection
nmap -sV --version-intensity 9 192.168.1.1

# Light service detection
nmap -sV --version-intensity 1 192.168.1.1
```

### Operating System Detection
```bash
# OS detection
nmap -O 192.168.1.1

# OS detection with version
nmap -O --osscan-guess 192.168.1.1
```

### Script Scanning
```bash
# Default safe scripts
nmap -sC 192.168.1.1

# Specific script
nmap --script=http-title 192.168.1.1

# Script categories
nmap --script=vuln 192.168.1.1
nmap --script=discovery 192.168.1.1
nmap --script=safe 192.168.1.1
```

## Firewall and IDS Evasion

### Fragmentation
```bash
# Fragment packets
nmap -f 192.168.1.1

# Custom MTU
nmap --mtu 24 192.168.1.1
```

### Decoys
```bash
# Use decoy addresses
nmap -D RND:10 192.168.1.1

# Specific decoys
nmap -D 192.168.1.100,192.168.1.101 192.168.1.1
```

### Spoofing
```bash
# Source port spoofing
nmap --source-port 53 192.168.1.1

# IP spoofing (requires --send-ip)
nmap -S 192.168.1.100 192.168.1.1
```

### Timing Evasion
```bash
# Slow scan
nmap -T0 --scan-delay 5s 192.168.1.1

# Randomize timing
nmap --randomize-hosts 192.168.1.0/24
```

## Output Formats

### Normal Output
```bash
nmap 192.168.1.1
```

### XML Output
```bash
nmap -oX output.xml 192.168.1.1
```

### Grepable Output
```bash
nmap -oG output.grep 192.168.1.1
```

### All Formats
```bash
nmap -oA output 192.168.1.1  # Creates .xml, .grep, .nmap files
```

### Script Kiddie Output
```bash
nmap -oS output.skid 192.168.1.1
```

## NSE (Nmap Scripting Engine)

### Script Categories
- **auth:** Authentication related scripts
- **broadcast:** Broadcast discovery scripts
- **brute:** Brute force attack scripts
- **default:** Scripts run by default
- **discovery:** Host/service discovery scripts
- **dos:** Scripts that may cause denial of service
- **exploit:** Exploit scripts
- **external:** Scripts that send data to third parties
- **fuzzer:** Fuzzer scripts
- **intrusive:** Intrusive scripts
- **malware:** Malware detection scripts
- **safe:** Safe scripts that won't harm target
- **version:** Scripts for version detection
- **vuln:** Vulnerability detection scripts

### Popular Scripts
```bash
# Heartbleed vulnerability
nmap --script=ssl-heartbleed 192.168.1.1

# HTTP methods
nmap --script=http-methods 192.168.1.1

# SMB vulnerabilities
nmap --script=smb-vuln* 192.168.1.1

# DNS enumeration
nmap --script=dns-brute 192.168.1.1
```

## Advanced Usage

### Network Sweeping
```bash
# Scan entire subnet
nmap 192.168.1.0/24

# Exclude hosts
nmap 192.168.1.0/24 --exclude 192.168.1.1

# Exclude from file
nmap 192.168.1.0/24 --excludefile exclude.txt
```

### IPv6 Scanning
```bash
# IPv6 scan
nmap -6 2001:db8::1

# IPv6 with port scan
nmap -6 -p 80 2001:db8::1
```

### Through Proxies
```bash
# HTTP proxy
nmap --proxy http://proxy.example.com:8080 192.168.1.1

# SOCKS4 proxy
nmap --proxy socks4://proxy.example.com:1080 192.168.1.1
```

### Zenmap (GUI)
```bash
# Launch GUI (if installed)
zenmap
```

## Common Nmap Commands

### Basic Network Recon
```bash
# Quick host discovery
nmap -sn -T4 192.168.1.0/24

# Comprehensive scan
nmap -sS -sV -O -p- 192.168.1.1

# Web server scan
nmap -sV -p 80,443 --script=http-enum,http-title 192.168.1.1
```

### Vulnerability Assessment
```bash
# Vulnerability scan
nmap --script=vuln 192.168.1.1

# MS17-010 (EternalBlue)
nmap --script=smb-vuln-ms17-010 192.168.1.1

# Heartbleed
nmap -p 443 --script=ssl-heartbleed 192.168.1.1
```

### Firewall Testing
```bash
# Firewall rules
nmap -sA 192.168.1.1

# Traceroute
nmap --traceroute 192.168.1.1
```

## Nmap Scripting

### Writing Custom Scripts
```lua
-- Example NSE script
local nmap = require "nmap"
local stdnse = require "stdnse"

description = [[
Simple HTTP title grabber
]]

author = "Your Name"
license = "Same as Nmap--See https://nmap.org/book/man-legal.html"
categories = {"discovery", "safe"}

portrule = function(host, port)
  return port.protocol == "tcp" and port.number == 80 and port.state == "open"
end

action = function(host, port)
  local socket = nmap.new_socket()
  socket:connect(host, port)
  socket:send("GET / HTTP/1.0\r\n\r\n")
  local response = socket:receive()
  socket:close()

  if response then
    local title = string.match(response, "<title>(.-)</title>")
    if title then
      return "Title: " .. title
    end
  end

  return "No title found"
end
```

## Performance Optimization

### Parallel Scanning
```bash
# Multiple targets
nmap 192.168.1.1 192.168.1.2 192.168.1.3

# From file
nmap -iL targets.txt
```

### Resource Management
```bash
# Limit bandwidth
nmap --min-rate 50 --max-rate 100 192.168.1.1

# Host timeout
nmap --host-timeout 10m 192.168.1.1

# Max retries
nmap --max-retries 2 192.168.1.1
```

## Legal and Ethical Considerations

### Legal Use
- Only scan networks you own or have explicit permission to scan
- Obtain written authorization for security assessments
- Be aware of local laws regarding network scanning
- Respect robots.txt and terms of service

### Ethical Use
- Use Nmap for defensive security purposes
- Report vulnerabilities responsibly
- Don't use for malicious purposes
- Contribute to the Nmap project

## Troubleshooting

### Common Issues
- **Permission denied:** Run with sudo for raw socket access
- **Slow scans:** Adjust timing parameters
- **False positives:** Verify results manually
- **Blocked by firewall:** Use evasion techniques (ethically)

### Debug Mode
```bash
# Verbose output
nmap -v 192.168.1.1

# Very verbose
nmap -vv 192.168.1.1

# Debug output
nmap -d 192.168.1.1
```

## Integration with Other Tools

### Metasploit
```bash
# Import Nmap results
db_import /path/to/nmap.xml
```

### Nessus
- Use Nmap for initial discovery
- Import results for vulnerability scanning

### OpenVAS
- Similar integration capabilities

## Learning Resources

- **Official Nmap website:** https://nmap.org/
- **Nmap book:** "Nmap Network Scanning" by Gordon Lyon
- **Nmap documentation:** https://nmap.org/docs.html
- **NSE documentation:** https://nmap.org/book/nse.html
- **Community forums:** https://forums.nmap.org/

## Conclusion

Nmap is an essential tool for network administrators, security professionals, and penetration testers. Its versatility, from simple host discovery to complex vulnerability detection, makes it invaluable for network security assessments. Understanding Nmap's capabilities and using it responsibly can greatly enhance your ability to secure and maintain networks.

Remember to always use Nmap ethically and legally, and consider obtaining professional certifications like CEH or OSCP to deepen your knowledge of network security tools and techniques.