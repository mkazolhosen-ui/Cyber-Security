# MAC Address & ARP

## MAC Address

- A Media Access Control (MAC) address is a hardware identifier assigned to a network interface.
- It operates at Layer 2 of the OSI model and is used for local network communication.

## ARP (Address Resolution Protocol)

- ARP maps IPv4 addresses to MAC addresses so devices can send Ethernet frames on a LAN.
- A device broadcasts an ARP request, and the owner replies with its MAC address.

## Cybersecurity Relevance

- ARP spoofing or poisoning can redirect local traffic to an attacker’s machine.
- MAC addresses are used in network access control, but can be spoofed.
- ARP-based attacks are common in local network intrusion and man-in-the-middle scenarios.

## Usefulness in Cybersecurity

- Network defenders use ARP tables and MAC address filtering to identify hosts and detect anomalies.
- Monitoring ARP traffic can reveal spoofing attempts and misconfigured devices.
- Understanding MAC and ARP behavior is important for securing switches, VLANs, and internal networks.

## Defensive Actions

- Use static ARP entries for critical infrastructure when feasible.
- Deploy network segmentation and 802.1X to limit unauthorized access.
- Monitor for duplicate MAC addresses, unexpected ARP replies, and unusual ARP broadcast patterns.
