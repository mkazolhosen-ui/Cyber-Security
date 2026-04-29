# TCP vs UDP

## Overview

- TCP (Transmission Control Protocol): connection-oriented, reliable, ordered delivery.
- UDP (User Datagram Protocol): connectionless, faster, lower overhead, no delivery guarantees.

## Key Differences

- TCP ensures packets arrive in order and retransmits lost data.
- UDP sends packets independently and is better for low-latency traffic.
- TCP uses handshakes and flow control; UDP is simpler and faster.

## Cybersecurity Relevance

- TCP is commonly used for secure, stateful sessions like HTTPS, SSH, and VPN tunnels.
- UDP is used for DNS queries, VoIP, streaming, and some VPN protocols.
- Attackers may exploit UDP for amplification attacks and packet spoofing.
- Defenders need to monitor both protocols: TCP for session-based threats, UDP for service abuse.

## Use in Cybersecurity

- Firewalls often treat TCP and UDP differently because TCP is stateful while UDP is stateless.
- IDS/IPS systems inspect TCP streams for protocol anomalies and UDP flows for suspicious volume.
- Understanding protocol behavior is essential for network segmentation, incident response, and traffic filtering.
