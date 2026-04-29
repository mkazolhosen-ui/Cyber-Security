# CIDR

## What is CIDR?

- CIDR stands for Classless Inter-Domain Routing.
- It is a method for allocating IP addresses and routing by using variable-length subnet masks.

## How CIDR Works

- An IP block is written as `address/prefix`, such as `192.168.0.0/24`.
- The prefix length defines the network size and the number of hosts.

## Cybersecurity Relevance

- CIDR is essential for network design, access control lists, and firewall rules.
- Good subnet planning limits broadcast domains and reduces attack surface.
- Misconfigured CIDR blocks can expose unintended hosts or create gaps in security zones.

## Usefulness in Cybersecurity

- Security teams use CIDR notation to define precise network policies and segment assets.
- Proper CIDR allocation makes monitoring and threat hunting more effective.
- It supports secure network architecture by separating trusted and untrusted networks.

## Best Practices

- Use clear, consistent CIDR boundaries for internal and external networks.
- Document all CIDR ranges and verify firewall rules against them.
- Avoid overly broad CIDR blocks in security policies to reduce lateral movement.
