# DNS (Domain Name System)

## What is DNS?

- DNS translates human-readable domain names into IP addresses.
- It is a core internet service used by browsers, email, and many applications.

## How DNS Works

- Clients send queries to DNS resolvers on port 53.
- Resolvers look up records such as A, AAAA, CNAME, and MX.
- Responses map names to addresses or other service endpoints.

## Cybersecurity Relevance

- DNS is a frequent vector for reconnaissance, data exfiltration, and malware command-and-control.
- DNS spoofing or poisoning can redirect traffic to malicious sites.
- Attackers can use DNS tunneling to hide data within legitimate DNS requests.

## Usefulness in Cybersecurity

- Monitoring DNS logs helps detect domain generation algorithms (DGAs), suspicious lookups, and infected hosts.
- DNS filtering can block access to known malicious domains.
- Secure DNS configurations (DNSSEC, split-horizon DNS, and encrypted DNS) improve trust and reduce manipulation.

## Defensive Actions

- Deploy DNS filtering and logging at the network boundary.
- Analyze DNS traffic for anomalies, such as sudden spikes or rare domains.
- Harden DNS servers and use validation to prevent cache poisoning.
