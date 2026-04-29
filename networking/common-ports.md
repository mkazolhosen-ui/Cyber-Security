# Common Ports

## Important Ports

- Port 80: HTTP (web traffic)
- Port 443: HTTPS (encrypted web traffic)
- Port 22: SSH (secure remote access)
- Port 53: DNS (domain name resolution)

## Why They Matter

- These ports are foundational for internet services.
- They are frequently targeted by attackers because services on these ports are widely exposed.
- Knowing common ports helps specialists identify normal versus suspicious traffic.

## Cybersecurity Usefulness

- Security monitoring often focuses on these ports first for detection and logging.
- Web servers on 80/443 must be hardened against injection, configuration errors, and certificate attacks.
- SSH on port 22 should be protected with strong authentication, access controls, and rate limiting.
- DNS on port 53 is critical for name resolution and commonly abused in DNS poisoning, tunneling, and reflection attacks.

## Best Practices

- Restrict access to port 22 to authorized hosts.
- Use HTTPS whenever possible and maintain valid certificates.
- Monitor DNS traffic for unusual query patterns and zones.
- Use network filtering and logging for these ports to support threat hunting.
