# Wireshark: Network Protocol Analyzer

## Introduction

Wireshark is a free and open-source network protocol analyzer that allows users to capture and interactively browse the traffic running on a computer network. It is widely used by network administrators, security professionals, and developers for troubleshooting network issues, analyzing network security, and understanding network protocols.

## Installation

### Linux
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install wireshark

# For GUI access
sudo usermod -a -G wireshark $USER
# Log out and back in

# CentOS/RHEL
sudo yum install wireshark wireshark-gnome

# Fedora
sudo dnf install wireshark

# Arch Linux
sudo pacman -S wireshark-qt
```

### macOS
```bash
# Using Homebrew
brew install wireshark

# Or download from https://www.wireshark.org/download.html
```

### Windows
- Download installer from https://www.wireshark.org/download.html
- Run installer with WinPcap/Npcap
- Install USBPcap if needed for USB traffic

### From Source
```bash
git clone https://gitlab.com/wireshark/wireshark.git
cd wireshark
mkdir build
cd build
cmake ../
make
sudo make install
```

## Getting Started

### Starting Wireshark
```bash
# Command line
wireshark

# Or with specific interface
wireshark -i eth0

# Capture to file
wireshark -i eth0 -w capture.pcap
```

### Interface Selection
1. Launch Wireshark
2. Select network interface from the list
3. Click "Start" to begin capturing

### Basic Capture
- **Start/Stop:** Use toolbar buttons or Ctrl+E
- **Restart:** Clear current capture and start fresh
- **Options:** Configure capture parameters

## Interface Configuration

### Capture Interfaces
- **Ethernet:** eth0, enp0s3, etc.
- **Wi-Fi:** wlan0, wlp2s0, etc.
- **Loopback:** lo (for localhost traffic)
- **Virtual interfaces:** Docker, VPN, etc.

### Capture Options
- **Promiscuous mode:** Capture all traffic on network segment
- **Monitor mode:** For wireless networks (requires special setup)
- **Buffer size:** Amount of RAM for packet buffer
- **Snap length:** Maximum bytes to capture per packet

## Packet Capture Filters

### Capture Filters (BPF Syntax)
```bash
# Host filters
host 192.168.1.1
not host 192.168.1.1

# Network filters
net 192.168.1.0/24
net 192.168.0.0 mask 255.255.0.0

# Port filters
port 80
portrange 1-1024
not port 22

# Protocol filters
tcp
udp
icmp
arp

# Complex filters
host 192.168.1.1 and port 80
tcp port 443 or udp port 53
```

### Applying Capture Filters
1. Click "Capture" > "Options"
2. Select interface
3. Enter filter in "Capture Filter" field
4. Click "Start"

## Display Filters

### Basic Display Filters
```bash
# Protocol filters
http
dns
tcp
udp
icmp

# Address filters
ip.src == 192.168.1.1
ip.dst == 192.168.1.1
eth.addr == aa:bb:cc:dd:ee:ff

# Port filters
tcp.port == 80
tcp.srcport == 443
udp.port == 53

# Packet content
http contains "password"
tcp contains "GET"

# Packet length
frame.len > 1000
tcp.len > 0
```

### Advanced Display Filters
```bash
# TCP flags
tcp.flags.syn == 1
tcp.flags.ack == 1
tcp.flags.fin == 1

# HTTP specific
http.request.method == "POST"
http.response.code == 404
http.host == "example.com"

# DNS queries
dns.qry.name == "google.com"
dns.flags.response == 0

# SSL/TLS
ssl.handshake.type == 1
tls.record.version == 0x0303
```

### Filter Expressions
- **and/or/not:** Logical operators
- **==/!=:** Equality
- **matches:** Regular expressions
- **contains:** Substring search
- **in:** Set membership

## Packet Analysis

### Packet Details Pane
- **Frame:** Physical layer information
- **Ethernet:** Data link layer
- **IP:** Network layer
- **TCP/UDP:** Transport layer
- **HTTP/DNS/etc.:** Application layer

### Following Streams
- **TCP streams:** Follow TCP conversation
- **UDP streams:** Follow UDP conversation
- **HTTP streams:** Follow HTTP request/response
- **TLS streams:** Decrypt if keys available

### Expert Information
- **Errors:** Packet errors and warnings
- **Warnings:** Potential issues
- **Notes:** Informational messages
- **Chats:** Normal protocol behavior

## Protocol Dissection

### Common Protocols

#### HTTP/HTTPS
- Request/Response analysis
- Headers inspection
- Content decoding
- Cookie analysis

#### DNS
- Query/Response tracking
- Name resolution
- DNS tunneling detection

#### TCP
- Connection establishment (3-way handshake)
- Sequence/acknowledgment numbers
- Window size and flow control
- Connection teardown

#### UDP
- Connectionless datagram analysis
- Port-based service identification

#### ICMP
- Echo requests/replies (ping)
- Error messages
- Traceroute analysis

### Advanced Protocol Analysis
- **VoIP:** RTP, SIP, SDP
- **Wireless:** 802.11 management/control/data
- **Routing:** OSPF, BGP, RIP
- **Security:** SSL/TLS, IPsec, SSH

## Statistical Analysis

### Protocol Hierarchy
- View > Statistics > Protocol Hierarchy
- Shows distribution of protocols in capture

### Conversations
- View > Statistics > Conversations
- Shows traffic between endpoints
- Sort by bytes, packets, duration

### Endpoints
- View > Statistics > Endpoints
- Shows all communicating hosts
- Resolve names and identify roles

### IO Graphs
- View > Statistics > IO Graphs
- Visualize traffic patterns over time
- Multiple graphs with different filters

### Flow Graphs
- View > Statistics > Flow Graph
- Visual representation of packet flows
- TCP sequence diagrams

## Exporting and Saving

### Save Capture Files
```bash
# Save all packets
File > Save As > capture.pcapng

# Save displayed packets only
File > Export Specified Packets > capture_filtered.pcapng
```

### Export Objects
- **HTTP objects:** File > Export Objects > HTTP
- **SMB objects:** File > Export Objects > SMB
- **DICOM objects:** File > Export Objects > DICOM

### Export Packet Dissections
- **As text:** File > Export Packet Dissections > As Plain Text
- **As CSV:** File > Export Packet Dissections > As CSV
- **As JSON:** File > Export Packet Dissections > As JSON

## Command Line Tools

### Tshark (Terminal-based Wireshark)
```bash
# Basic capture
tshark -i eth0

# With display filter
tshark -i eth0 -Y "http"

# Write to file
tshark -i eth0 -w capture.pcap

# Read from file
tshark -r capture.pcap

# Extract fields
tshark -r capture.pcap -T fields -e ip.src -e ip.dst
```

### Capinfos
```bash
# File information
capinfos capture.pcap

# Detailed statistics
capinfos -A capture.pcap
```

### Editcap
```bash
# Split capture file
editcap -c 1000 capture.pcap split.pcap

# Change timestamp
editcap -t 3600 capture.pcap adjusted.pcap

# Remove packets
editcap -r capture.pcap filtered.pcap 1-100
```

### Mergecap
```bash
# Merge multiple files
mergecap -w merged.pcap file1.pcap file2.pcap
```

## Advanced Features

### Decryption
#### SSL/TLS Decryption
1. Capture SSL/TLS handshake
2. Extract session keys
3. Configure Wireshark: Edit > Preferences > Protocols > TLS
4. Add key file or (Pre)-Master-Secret log

#### WPA2 Decryption
1. Capture 4-way handshake
2. Edit > Preferences > Protocols > IEEE 802.11
3. Enter WPA key or passphrase

### Coloring Rules
- View > Coloring Rules
- Create custom color filters
- Highlight important traffic

### Name Resolution
- Enable MAC name resolution
- Enable network name resolution
- Enable transport name resolution

### Preferences
- Edit > Preferences
- Customize appearance and behavior
- Configure protocol dissectors

## Troubleshooting

### Common Issues

#### No Packets Captured
- Check interface permissions (may need root/sudo)
- Verify interface is up and connected
- Check firewall rules
- Try different interface

#### High CPU Usage
- Use capture filters to reduce traffic
- Increase buffer size
- Use command-line tools for large captures

#### Packet Loss
- Increase kernel buffer size
- Use larger snap length if needed
- Check system resources

#### Display Issues
- Update Wireshark to latest version
- Reset preferences to defaults
- Check for conflicting plugins

### Performance Tips
- Use capture filters to limit traffic
- Disable name resolution during capture
- Use ring buffers for continuous capture
- Split large captures into smaller files

## Security Analysis

### Detecting Attacks
- **Port scanning:** Look for SYN packets to many ports
- **DDoS attacks:** High volume of similar packets
- **Malware:** Unusual traffic patterns, C2 communications
- **Data exfiltration:** Large outbound transfers

### Network Forensics
- Timeline analysis of incidents
- Packet carving for file extraction
- Session reconstruction
- Anomaly detection

### Compliance
- PCI DSS logging requirements
- HIPAA network monitoring
- SOX audit trails

## Plugins and Extensions

### Lua Scripts
```lua
-- Example dissector
local myproto = Proto("myproto", "My Protocol")

local fields = {
    command = ProtoField.uint8("myproto.command", "Command", base.DEC),
    length = ProtoField.uint16("myproto.length", "Length", base.DEC),
    data = ProtoField.bytes("myproto.data", "Data")
}

myproto.fields = fields

function myproto.dissector(buffer, pinfo, tree)
    pinfo.cols.protocol = "MYPROTO"

    local subtree = tree:add(myproto, buffer(), "My Protocol Data")
    subtree:add(fields.command, buffer(0,1))
    subtree:add(fields.length, buffer(1,2))
    subtree:add(fields.data, buffer(3))
end

-- Register dissector
local tcp_table = DissectorTable.get("tcp.port")
tcp_table:add(12345, myproto)
```

### Custom Plugins
- Protocol dissectors
- Tap listeners
- File readers/writers
- GUI extensions

## Integration with Other Tools

### Network Analysis
- **tcpdump:** Command-line packet capture
- **Snort:** Intrusion detection system
- **Suricata:** Next-generation IDS/IPS

### Security Tools
- **Metasploit:** Exploit framework
- **Nmap:** Network scanning
- **Burp Suite:** Web application testing

### Development
- **Scapy:** Packet manipulation
- **dpkt:** Python packet parsing
- **PyShark:** Python wrapper for tshark

## Learning Resources

- **Official Website:** https://www.wireshark.org/
- **Documentation:** https://www.wireshark.org/docs/
- **Wiki:** https://wiki.wireshark.org/
- **User Guide:** https://www.wireshark.org/docs/wsug_html/
- **Sample Captures:** https://wiki.wireshark.org/SampleCaptures

### Books
- "Wireshark Network Analysis" by Laura Chappell
- "Practical Packet Analysis" by Chris Sanders
- "Wireshark 101" by Laura Chappell

### Online Courses
- Wireshark University (free)
- Udemy Wireshark courses
- Coursera network analysis courses

## Best Practices

### Capture Strategy
- Use appropriate capture filters
- Capture during specific time windows
- Use multiple interfaces if needed
- Document capture methodology

### Analysis Approach
- Start with broad view (statistics)
- Narrow down with display filters
- Follow conversations for context
- Use expert information for issues

### Security Considerations
- Handle sensitive data appropriately
- Use encryption for stored captures
- Be aware of legal implications
- Obtain permission for network monitoring

## Conclusion

Wireshark is an indispensable tool for network analysis, troubleshooting, and security assessment. Its comprehensive protocol support, powerful filtering capabilities, and extensive analysis features make it suitable for both beginners and advanced users. Whether debugging network issues, performing security audits, or learning about network protocols, Wireshark provides the visibility needed to understand what's happening on the network.

Remember to use Wireshark responsibly and in accordance with applicable laws and organizational policies. Network monitoring should always be conducted with proper authorization and purpose.