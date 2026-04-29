# IP Addressing (IPv4 vs IPv6)

## IPv4

- Uses 32-bit addresses, typically written in dotted decimal form (e.g., 192.168.1.1).
- Limited address space led to widespread use of NAT.

## IPv6

- Uses 128-bit addresses, written in hexadecimal colon-separated format.
- Designed to provide a vastly larger address space and simplified routing.

## Cybersecurity Relevance

- IPv4 and IPv6 behave differently in networking tools, firewall rules, and packet inspection.
- IPv6 adoption introduces new attack surfaces, such as neighbor discovery and ICMPv6 misuse.
- Misconfigured dual-stack environments can expose systems unexpectedly.

## Usefulness in Cybersecurity

- Security teams must understand both address families for asset discovery and segmentation.
- IPv6 traffic should be monitored and secured with the same rigor as IPv4.
- Proper IPv6 deployment avoids address collisions and reduces reliance on NAT, but also requires strong access controls.

## Best Practices

- Maintain accurate IP inventories for both IPv4 and IPv6.
- Apply consistent security policies and firewall rules across both protocols.
- Validate IPv6 configuration and monitor for suspicious unsolicited traffic.
