# Networking Learning Path

This folder contains core networking topics useful for cybersecurity learners. The recommended learning order is designed to build foundational understanding first, then expand into network services, security tools, and defensive controls.

## Recommended Order

1. `osi-model.md`
   - Start here to understand layered network architecture and how protocols fit together.
   - This helps you interpret packet flow, network troubleshooting, and security controls.

2. `tcp-ip.md`
   - Learn the basics of the TCP/IP model and the protocols that power the internet.
   - Key to understanding how data is transported between systems.

3. `tcp-vs-udp.md`
   - Compare connection-oriented and connectionless transport protocols.
   - Important for recognizing service behavior and exploitation patterns.

4. `ip-addressing-ipv4-vs-ipv6.md`
   - Learn IPv4 and IPv6 addressing schemes and their security implications.
   - Essential for network scanning, asset discovery, and firewall rules.

5. `cidr.md`
   - Understand subnetting with CIDR notation.
   - Critical for designing access policies and network segmentation.

6. `nat.md`
   - Learn how Network Address Translation works and why it is used.
   - Useful for understanding internal/external addressing and perimeter defense.

7. `mac-address-arp.md`
   - Study local network addressing and ARP.
   - Helps you detect LAN attacks such as ARP spoofing and man-in-the-middle.

8. `common-ports.md`
   - Review standard service ports and why they matter.
   - Good for prioritizing monitoring and hardening efforts.

9. `dns.md`
   - Learn how DNS resolves names and why it is a frequent attack vector.
   - Valuable for network defense, threat hunting, and incident response.

10. `firewalls.md`
    - Understand how firewalls control traffic and enforce policies.
    - Firewalls are foundational perimeter defenses.

11. `ids-ips.md`
    - Study intrusion detection and prevention systems.
    - Important for detecting and blocking network-based attacks.

12. `vpns-encryption.md`
    - Learn VPNs and encryption for secure remote access and transport confidentiality.
    - Useful for protecting traffic and secure communications.

13. `vlans.md`
    - Learn virtual LANs for network segmentation and isolation.
    - Helps reduce lateral movement and protect sensitive systems.

## Efficient Learning Approach

- Read topics in the order above to build from basic protocol knowledge to security tools and architecture.
- Use hands-on exercises such as packet capture, service scanning, and firewall rule simulation.
- Take notes on how each topic connects to cybersecurity concepts like attack surface, access control, and monitoring.
- Revisit earlier topics after reading security controls to better understand how defenses map to traffic behavior.

## How to Use This Folder

- Start with the files at the top of the list and follow the progression.
- Apply concepts in small labs or capture-the-flag challenges when possible.
- Use this guide as a quick reference to determine the next topic when learning networking for cybersecurity.
