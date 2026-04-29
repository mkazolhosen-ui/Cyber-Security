# NAT (Network Address Translation)

## What is NAT?

- NAT translates private IP addresses to public IP addresses for traffic leaving a local network.
- It conserves public address space and enables multihost connectivity behind a single public IP.

## Types of NAT

- Static NAT maps one private address to one public address.
- Dynamic NAT maps private addresses to a pool of public addresses.
- PAT (Port Address Translation) multiplexes many private addresses onto one public IP using ports.

## Cybersecurity Relevance

- NAT acts as a basic boundary between internal networks and the internet.
- It can obscure internal IPs and make direct inbound attacks harder.
- However, NAT is not a security mechanism on its own and can hide malicious traffic.

## Usefulness in Cybersecurity

- NAT supports network segmentation and helps manage IP address allocation.
- It is often paired with firewalls and proxy services for stronger perimeter defenses.
- Understanding NAT behavior is essential for troubleshooting, logging, and incident response.

## Best Practices

- Combine NAT with firewalls and access control policies.
- Log translated sessions to correlate internal hosts with external activity.
- Avoid relying solely on NAT for security; use it as part of a layered defense.
