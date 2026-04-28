#!/usr/bin/env python3
"""
Advanced Port Scanner
A comprehensive port scanning tool for network security assessment.

DISCLAIMER: This tool is for educational and authorized security testing purposes only.
Unauthorized scanning of networks or systems may be illegal. Always obtain explicit
permission before scanning any target that you do not own.

Author: Cybersecurity Learning Tool
"""

import socket
import argparse
import threading
import time
import sys
import ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# Common port mappings for service detection
COMMON_PORTS = {
    20: "FTP-Data", 21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 67: "DHCP-Server", 68: "DHCP-Client", 69: "TFTP",
    80: "HTTP", 110: "POP3", 111: "RPC", 135: "MSRPC", 139: "NetBIOS-SSN",
    143: "IMAP", 161: "SNMP", 389: "LDAP", 443: "HTTPS", 445: "SMB",
    993: "IMAPS", 995: "POP3S", 1433: "MSSQL", 1521: "Oracle",
    2049: "NFS", 3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
    5900: "VNC", 8080: "HTTP-Proxy", 8443: "HTTPS-Alt"
}

class PortScanner:
    def __init__(self, target, ports, timeout=1, threads=100, verbose=False):
        self.target = target
        self.ports = ports
        self.timeout = timeout
        self.threads = threads
        self.verbose = verbose
        self.open_ports = []
        self.lock = threading.Lock()

    def scan_port_tcp_connect(self, port):
        """TCP Connect Scan - Full connection establishment"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((self.target, port))

            if result == 0:
                service = self.identify_service(port)
                with self.lock:
                    self.open_ports.append((port, "TCP", service))
                if self.verbose:
                    print(f"[+] Port {port}/TCP open - {service}")
            else:
                if self.verbose:
                    print(f"[-] Port {port}/TCP closed")

            sock.close()
        except Exception as e:
            if self.verbose:
                print(f"[!] Error scanning port {port}: {e}")

    def scan_port_udp(self, port):
        """UDP Scan - Send UDP packet and wait for response"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(self.timeout)

            # Send a simple probe
            sock.sendto(b"", (self.target, port))

            try:
                data, addr = sock.recvfrom(1024)
                service = self.identify_service(port)
                with self.lock:
                    self.open_ports.append((port, "UDP", service))
                if self.verbose:
                    print(f"[+] Port {port}/UDP open - {service}")
            except socket.timeout:
                # No response could mean open or filtered
                if self.verbose:
                    print(f"[?] Port {port}/UDP open|filtered")

            sock.close()
        except Exception as e:
            if self.verbose:
                print(f"[!] Error scanning UDP port {port}: {e}")

    def identify_service(self, port):
        """Attempt to identify the service running on a port"""
        if port in COMMON_PORTS:
            return COMMON_PORTS[port]

        try:
            # Try to get service name from socket
            service = socket.getservbyport(port)
            return service.upper()
        except:
            return "Unknown"

    def scan_ports(self, scan_type="tcp"):
        """Main scanning function"""
        print(f"\n[*] Starting {scan_type.upper()} scan on {self.target}")
        print(f"[*] Scanning {len(self.ports)} ports with {self.threads} threads")
        print(f"[*] Timeout: {self.timeout}s")
        print("-" * 50)

        start_time = time.time()

        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            if scan_type.lower() == "tcp":
                futures = [executor.submit(self.scan_port_tcp_connect, port) for port in self.ports]
            elif scan_type.lower() == "udp":
                futures = [executor.submit(self.scan_port_udp, port) for port in self.ports]
            else:
                print("[!] Invalid scan type. Use 'tcp' or 'udp'")
                return

            # Wait for all scans to complete
            for future in as_completed(futures):
                pass  # Results are handled in the scan functions

        end_time = time.time()
        duration = end_time - start_time

        self.display_results(duration)

    def display_results(self, duration):
        """Display scan results"""
        print(f"\n[+] Scan completed in {duration:.2f} seconds")
        print(f"[+] Found {len(self.open_ports)} open ports on {self.target}")
        print("-" * 50)

        if self.open_ports:
            print("PORT      STATE  SERVICE")
            print("-" * 30)
            for port, protocol, service in sorted(self.open_ports):
                print(f"{port:5d}/{protocol:<3} {service}")
        else:
            print("No open ports found.")

def validate_target(target):
    """Validate the target IP address or hostname"""
    try:
        # Try to resolve hostname to IP
        ipaddress.ip_address(target)
        return target
    except ValueError:
        try:
            # Resolve hostname
            ip = socket.gethostbyname(target)
            print(f"[*] Resolved {target} to {ip}")
            return ip
        except socket.gaierror:
            print(f"[!] Could not resolve hostname: {target}")
            sys.exit(1)

def parse_ports(port_string):
    """Parse port specification string"""
    ports = set()

    # Handle comma-separated values and ranges
    parts = port_string.split(',')

    for part in parts:
        part = part.strip()
        if '-' in part:
            # Range specification
            try:
                start, end = map(int, part.split('-'))
                if start > end or start < 1 or end > 65535:
                    raise ValueError
                ports.update(range(start, end + 1))
            except ValueError:
                print(f"[!] Invalid port range: {part}")
                sys.exit(1)
        else:
            # Single port
            try:
                port = int(part)
                if port < 1 or port > 65535:
                    raise ValueError
                ports.add(port)
            except ValueError:
                print(f"[!] Invalid port number: {part}")
                sys.exit(1)

    return sorted(list(ports))

def main():
    parser = argparse.ArgumentParser(
        description="Advanced Port Scanner - Network Security Assessment Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python port_scanner.py -t 192.168.1.1 -p 1-1000
  python port_scanner.py -t example.com -p 80,443,22 -T tcp -v
  python port_scanner.py -t 10.0.0.1 -p 1-1024 -T udp --threads 50
  python port_scanner.py -t scanme.nmap.org -p 1-1000 -T tcp --timeout 2
        """
    )

    parser.add_argument("-t", "--target", required=True,
                       help="Target IP address or hostname")
    parser.add_argument("-p", "--ports", required=True,
                       help="Port range (e.g., 1-1000) or specific ports (e.g., 80,443,22)")
    parser.add_argument("-T", "--type", choices=["tcp", "udp"], default="tcp",
                       help="Scan type (default: tcp)")
    parser.add_argument("--timeout", type=float, default=1.0,
                       help="Timeout for each port scan in seconds (default: 1.0)")
    parser.add_argument("--threads", type=int, default=100,
                       help="Number of threads to use (default: 100)")
    parser.add_argument("-v", "--verbose", action="store_true",
                       help="Enable verbose output")
    parser.add_argument("--common", action="store_true",
                       help="Scan only common ports (overrides -p)")

    args = parser.parse_args()

    # Banner
    print("=" * 60)
    print("        Advanced Port Scanner")
    print("    Network Security Assessment Tool")
    print("=" * 60)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Validate and resolve target
    target = validate_target(args.target)

    # Determine ports to scan
    if args.common:
        ports = list(COMMON_PORTS.keys())
        print(f"[*] Scanning {len(ports)} common ports")
    else:
        ports = parse_ports(args.ports)

    # Create scanner instance
    scanner = PortScanner(
        target=target,
        ports=ports,
        timeout=args.timeout,
        threads=args.threads,
        verbose=args.verbose
    )

    # Perform scan
    try:
        scanner.scan_ports(args.type)
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Scan failed: {e}")
        sys.exit(1)

    print(f"\n[*] Scan finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()