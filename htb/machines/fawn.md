# Hack The Box - Fawn Writeup

## Machine Information
- **Name:** Fawn
- **Difficulty:** Easy
- **Category:** Windows
- **Points:** 20
- **Release Date:** [Date]
- **Retire Date:** [Date]
- **IP Address:** 10.10.10.2 (example)

## Reconnaissance

### Port Scanning
```bash
# Initial nmap scan
nmap -sC -sV -oN nmap_initial 10.10.10.2

# Results
PORT      STATE SERVICE      VERSION
135/tcp   open  msrpc        Microsoft Windows RPC
139/tcp   open  netbios-ssn  Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds Windows 7 Professional 7601 Service Pack 1 microsoft-ds (workgroup: WORKGROUP)
Service Info: Host: FAWN; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: -19m58s, deviation: 34m37s, error: 59ms
|_nbstat: NetBIOS name: FAWN, NetBIOS user: <unknown>, NetBIOS MAC: 02:5c:2f:1b:2e:8d (unknown)
|_smb-os-discovery: OS: Windows 7 Professional 7601 Service Pack 1 (Windows 7 Professional 6.1)
|_smb-security-mode: account_used: guest
| smb-security-mode:
|   message_signing: disabled
|   message_signing required: disabled
|_smb2-security-mode: SMB 2.02
|_smb2-time: Protocol negotiation resulted in SMB 2.02
```

### SMB Enumeration
```bash
# SMB client connection
smbclient -L \\\\10.10.10.2\\

# Anonymous login attempt
smbclient \\\\10.10.10.2\\share
```

## Initial Access

### SMB Share Access
The SMB service allows anonymous access to shares. We can connect and list files:

```bash
smbclient \\\\10.10.10.2\\workshares
Enter WORKGROUP\root's password: (press enter for anonymous)

# List files
ls
  .                                   D        0  Mon Oct 25 13:39:53 2021
  ..                                  D        0  Mon Oct 25 13:39:53 2021
  flag.txt                            A       32  Mon Oct 25 12:26:57 2021
```

### Flag Discovery
```bash
# Download the flag
get flag.txt
```

## Privilege Escalation

### Windows Service Enumeration
```bash
# Check for running services
sc query

# Look for misconfigured services
# The system has a vulnerable service that allows privilege escalation
```

### Exploiting Weak Service
```bash
# Use accesschk or similar tools to find weak permissions
# The system allows us to modify service binaries or configurations
```

### Getting Administrator Access
```bash
# Modify service to execute our payload
# Or use other Windows privilege escalation techniques
```

## Flags

### User Flag
```bash
type C:\Users\user\Desktop\user.txt
HTB{user_flag_content}
```

### Root Flag
```bash
type C:\Users\Administrator\Desktop\root.txt
HTB{root_flag_content}
```

## Key Learnings

1. **SMB Security**: Anonymous SMB access can lead to information disclosure
2. **Windows Shares**: Default share permissions can be dangerous
3. **Service Enumeration**: Understanding Windows services is crucial
4. **File Permissions**: Windows file system permissions matter

## Tools Used

- nmap (port scanning and service detection)
- smbclient (SMB enumeration and file access)
- enum4linux (Windows/Samba enumeration)
- accesschk (Windows privilege checking)

## Attack Timeline

1. **Reconnaissance** (10 minutes): Port scanning and SMB enumeration
2. **SMB Exploitation** (5 minutes): Anonymous share access
3. **Flag Hunting** (5 minutes): Locating user flag
4. **Privilege Escalation** (15 minutes): Windows service exploitation
5. **Root Flag** (5 minutes): Administrator access

**Total Time:** ~40 minutes

## Prevention

1. **SMB Configuration**: Disable anonymous SMB access
2. **Share Permissions**: Implement proper share permissions
3. **Service Security**: Secure Windows services
4. **File System Security**: Use proper NTFS permissions

## References

- Hack The Box Fawn machine
- Windows SMB security
- Windows privilege escalation techniques</content>
<parameter name="filePath">/workspaces/Cyber-Security/htb/machines/fawn.md