import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="CE405 - Cybersecurity", page_icon="🔐", layout="wide")

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    code, pre {
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    .course-header {
        background: linear-gradient(135deg, #dc2626 0%, #b91c1c 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .course-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .theory-box {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        border-left: 5px solid #dc2626;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .crypto-box {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .attack-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .defense-box {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .youtube-box {
        background: linear-gradient(135deg, #ede9fe 0%, #ddd6fe 100%);
        border-left: 5px solid #8b5cf6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="course-header">
    <div style="font-size: 1.2rem; opacity: 0.9;">CE405</div>
    <div class="course-title">Cybersecurity</div>
    <div>🔐 3 Credits | Semester 8 | Security, Cryptography & Ethical Hacking</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "8")
with col3:
    st.metric("Difficulty", "6/7")
with col4:
    st.metric("Hours/Week", "7")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "🔒 Cryptography",
    "🌐 Network Security",
    "⚔️ Common Attacks",
    "🛡️ Defense Strategies",
    "🎯 Ethical Hacking",
    "📋 Compliance & Standards",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive introduction to cybersecurity covering cryptography, network security, ethical hacking, and security 
        best practices. Learn encryption algorithms, secure protocols, common attack vectors, defense mechanisms, penetration 
        testing, and security compliance. Emphasizes hands-on labs with tools like Wireshark, Metasploit, Burp Suite, and 
        Nmap. Students will learn to identify vulnerabilities, perform security audits, and implement security controls to 
        protect systems and data.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Understand cryptographic algorithms (AES, RSA, SHA)",
        "Implement secure network protocols (TLS/SSL, VPN)",
        "Identify and exploit common vulnerabilities (OWASP Top 10)",
        "Perform penetration testing and security audits",
        "Use security tools (Wireshark, Metasploit, Nmap, Burp Suite)",
        "Apply defense-in-depth security strategies",
        "Understand security compliance (GDPR, PCI-DSS, ISO 27001)",
        "Develop secure coding practices"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Cryptography:**
        - Symmetric encryption (AES, DES)
        - Asymmetric encryption (RSA, ECC)
        - Hash functions (SHA-256, MD5)
        - Digital signatures and certificates
        - Public Key Infrastructure (PKI)
        
        **Network Security:**
        - Firewalls and IDS/IPS
        - VPN and secure tunneling
        - TLS/SSL protocols
        - DNS security (DNSSEC)
        - Wireless security (WPA3)
        """)
    
    with col2:
        st.markdown("""
        **Attacks & Defense:**
        - SQL injection and XSS
        - CSRF and session hijacking
        - DDoS and DoS attacks
        - Man-in-the-Middle (MITM)
        - Social engineering
        
        **Tools & Compliance:**
        - Penetration testing tools
        - Security scanning (Nessus, OpenVAS)
        - SIEM (Splunk, ELK)
        - GDPR, PCI-DSS, HIPAA
        - ISO 27001, NIST frameworks
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "The Web Application Hacker's Handbook", "author": "Stuttard & Pinto", "type": "Web Security"},
        {"title": "Metasploit: The Penetration Tester's Guide", "author": "Kennedy et al.", "type": "Pen Testing"},
        {"title": "Applied Cryptography", "author": "Bruce Schneier", "type": "Cryptography"},
        {"title": "OWASP Testing Guide", "author": "OWASP", "type": "Web Security"}
    ]
    
    for resource in resources:
        title = resource['title']
        author = resource['author']
        rtype = resource['type']
        st.markdown(f"📖 **{title}** by {author} ({rtype})")

# ==================== TAB 2: CRYPTOGRAPHY ====================
with tabs[1]:
    st.markdown("## 🔒 Cryptography")
    
    st.markdown("### 1️⃣ Symmetric Encryption")
    
    st.markdown("""
    <div class="crypto-box">
        <strong>AES (Advanced Encryption Standard):</strong><br>
        • Block cipher, 128-bit blocks<br>
        • Key sizes: 128, 192, 256 bits<br>
        • Industry standard for encryption<br>
        • Fast and secure<br>
        • Used in: TLS, VPN, disk encryption<br><br>
        
        <strong>DES/3DES (Data Encryption Standard):</strong><br>
        • DES: 56-bit key (deprecated, insecure)<br>
        • 3DES: Triple DES, 168-bit key<br>
        • Being phased out for AES<br><br>
        
        <strong>Modes of Operation:</strong><br>
        • <strong>ECB:</strong> Electronic Codebook (insecure, don't use)<br>
        • <strong>CBC:</strong> Cipher Block Chaining (common)<br>
        • <strong>CTR:</strong> Counter mode (parallel encryption)<br>
        • <strong>GCM:</strong> Galois/Counter Mode (authenticated encryption)<br><br>
        
        <strong>Key Management:</strong><br>
        • Secure key generation (random)<br>
        • Key storage (HSM, key vaults)<br>
        • Key rotation policies<br>
        • Never hardcode keys in code!
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Asymmetric Encryption")
    
    st.markdown("""
    <div class="theory-box">
        <strong>RSA (Rivest-Shamir-Adleman):</strong><br>
        • Public key encryption<br>
        • Key sizes: 2048, 3072, 4096 bits<br>
        • Slower than symmetric encryption<br>
        • Used for key exchange, digital signatures<br>
        • Based on factorization problem<br><br>
        
        <strong>ECC (Elliptic Curve Cryptography):</strong><br>
        • Smaller keys, same security as RSA<br>
        • 256-bit ECC ≈ 3072-bit RSA<br>
        • Faster and more efficient<br>
        • Used in: Bitcoin, TLS 1.3<br><br>
        
        <strong>Diffie-Hellman Key Exchange:</strong><br>
        • Secure key exchange over insecure channel<br>
        • Foundation of TLS/SSL<br>
        • Vulnerable to MITM without authentication<br><br>
        
        <strong>Digital Signatures:</strong><br>
        • RSA signatures<br>
        • ECDSA (Elliptic Curve DSA)<br>
        • Provides authentication and non-repudiation<br>
        • Hash message, encrypt with private key
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Hash Functions")
    
    st.markdown("""
    <div class="crypto-box">
        <strong>SHA-256 (Secure Hash Algorithm):</strong><br>
        • 256-bit output<br>
        • One-way function (irreversible)<br>
        • Collision resistant<br>
        • Used in: Bitcoin, TLS, file integrity<br><br>
        
        <strong>MD5 (Message Digest 5):</strong><br>
        • 128-bit output<br>
        • <strong>BROKEN - DO NOT USE for security!</strong><br>
        • Collision attacks exist<br>
        • OK for checksums only<br><br>
        
        <strong>SHA-1:</strong><br>
        • 160-bit output<br>
        • <strong>Deprecated - collision attacks</strong><br>
        • Being phased out<br><br>
        
        <strong>Password Hashing:</strong><br>
        • <strong>bcrypt:</strong> Adaptive, slow (good for passwords)<br>
        • <strong>scrypt:</strong> Memory-hard<br>
        • <strong>Argon2:</strong> Modern, winner of password hashing competition<br>
        • Always use salt!<br>
        • Never use plain SHA-256 for passwords
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: NETWORK SECURITY ====================
with tabs[2]:
    st.markdown("## 🌐 Network Security")
    
    st.markdown("### 1️⃣ Firewalls")
    
    st.markdown("""
    <div class="defense-box">
        <strong>Types of Firewalls:</strong><br><br>
        
        <strong>Packet Filtering:</strong><br>
        • Inspects packet headers (IP, port)<br>
        • Fast but limited<br>
        • Stateless<br><br>
        
        <strong>Stateful Inspection:</strong><br>
        • Tracks connection state<br>
        • More secure than packet filtering<br>
        • Most common type<br><br>
        
        <strong>Application Layer (WAF):</strong><br>
        • Inspects application data (HTTP, SQL)<br>
        • Protects web applications<br>
        • Can detect SQL injection, XSS<br><br>
        
        <strong>Next-Generation Firewall (NGFW):</strong><br>
        • Deep packet inspection<br>
        • Intrusion prevention (IPS)<br>
        • Application awareness<br>
        • SSL/TLS inspection
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ IDS/IPS")
    
    st.markdown("""
    <div class="theory-box">
        <strong>IDS (Intrusion Detection System):</strong><br>
        • Monitors network traffic<br>
        • Detects suspicious activity<br>
        • Alerts administrators<br>
        • Passive (doesn't block)<br><br>
        
        <strong>IPS (Intrusion Prevention System):</strong><br>
        • Active defense<br>
        • Blocks malicious traffic<br>
        • Can cause false positives<br>
        • Inline deployment<br><br>
        
        <strong>Detection Methods:</strong><br>
        • <strong>Signature-based:</strong> Known attack patterns<br>
        • <strong>Anomaly-based:</strong> Deviation from baseline<br>
        • <strong>Heuristic:</strong> Behavioral analysis<br><br>
        
        <strong>Popular Tools:</strong><br>
        • Snort (open source IDS/IPS)<br>
        • Suricata<br>
        • Zeek (formerly Bro)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ VPN & TLS")
    
    st.markdown("""
    <div class="crypto-box">
        <strong>VPN (Virtual Private Network):</strong><br>
        • Encrypted tunnel over public network<br>
        • <strong>IPsec:</strong> Network layer VPN<br>
        • <strong>OpenVPN:</strong> SSL/TLS-based VPN<br>
        • <strong>WireGuard:</strong> Modern, fast VPN<br>
        • Use cases: Remote access, site-to-site<br><br>
        
        <strong>TLS/SSL (Transport Layer Security):</strong><br>
        • Secures HTTP (HTTPS)<br>
        • TLS 1.3 is current standard<br>
        • SSL is deprecated (insecure)<br><br>
        
        <strong>TLS Handshake:</strong><br>
        1. Client Hello (supported ciphers)<br>
        2. Server Hello (chosen cipher, certificate)<br>
        3. Key exchange (Diffie-Hellman)<br>
        4. Encrypted communication<br><br>
        
        <strong>Certificate Validation:</strong><br>
        • Check certificate chain<br>
        • Verify domain name<br>
        • Check expiration date<br>
        • Certificate pinning for mobile apps
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: ATTACKS ====================
with tabs[3]:
    st.markdown("## ⚔️ Common Attacks")
    
    st.markdown("### 1️⃣ OWASP Top 10")
    
    owasp_data = {
        'Rank': ['A01', 'A02', 'A03', 'A04', 'A05'],
        'Vulnerability': [
            'Broken Access Control',
            'Cryptographic Failures',
            'Injection',
            'Insecure Design',
            'Security Misconfiguration'
        ],
        'Example': [
            'Unauthorized access to admin panel',
            'Weak encryption, exposed keys',
            'SQL injection, command injection',
            'Missing security controls',
            'Default credentials, open ports'
        ],
        'Mitigation': [
            'Proper authorization checks',
            'Strong encryption (AES-256)',
            'Parameterized queries, input validation',
            'Threat modeling, secure architecture',
            'Security hardening, least privilege'
        ]
    }
    
    df_owasp = pd.DataFrame(owasp_data)
    st.dataframe(df_owasp, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Injection Attacks")
    
    st.markdown("""
    <div class="attack-box">
        <strong>SQL Injection:</strong><br>
        <pre>
# Vulnerable code
query = "SELECT * FROM users WHERE username = '" + username + "'"

# Attack: username = "admin' OR '1'='1"
# Result: SELECT * FROM users WHERE username = 'admin' OR '1'='1'
# Returns all users!

# Secure code (parameterized query)
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        </pre><br>
        
        <strong>Command Injection:</strong><br>
        <pre>
# Vulnerable
os.system("ping " + user_input)

# Attack: user_input = "8.8.8.8; rm -rf /"
# Executes: ping 8.8.8.8; rm -rf /

# Secure
subprocess.run(["ping", user_input], check=True)
        </pre><br>
        
        <strong>XSS (Cross-Site Scripting):</strong><br>
        • <strong>Reflected XSS:</strong> Malicious script in URL<br>
        • <strong>Stored XSS:</strong> Script saved in database<br>
        • <strong>DOM-based XSS:</strong> Client-side JavaScript<br>
        • Mitigation: Escape output, Content Security Policy (CSP)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Other Common Attacks")
    
    st.markdown("""
    <div class="theory-box">
        <strong>CSRF (Cross-Site Request Forgery):</strong><br>
        • Tricks user into executing unwanted actions<br>
        • Example: Hidden form that transfers money<br>
        • Mitigation: CSRF tokens, SameSite cookies<br><br>
        
        <strong>Man-in-the-Middle (MITM):</strong><br>
        • Attacker intercepts communication<br>
        • Can read/modify data<br>
        • Mitigation: TLS/SSL, certificate pinning<br><br>
        
        <strong>DDoS (Distributed Denial of Service):</strong><br>
        • Overwhelm server with traffic<br>
        • Types: SYN flood, UDP flood, HTTP flood<br>
        • Mitigation: Rate limiting, CDN, DDoS protection services<br><br>
        
        <strong>Session Hijacking:</strong><br>
        • Steal session cookie<br>
        • Impersonate user<br>
        • Mitigation: Secure cookies (HttpOnly, Secure), session timeout<br><br>
        
        <strong>Social Engineering:</strong><br>
        • Phishing emails<br>
        • Pretexting (fake scenario)<br>
        • Baiting (malicious USB)<br>
        • Mitigation: Security awareness training
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: DEFENSE ====================
with tabs[4]:
    st.markdown("## 🛡️ Defense Strategies")
    
    st.markdown("### 1️⃣ Defense in Depth")
    
    st.markdown("""
    <div class="defense-box">
        <strong>Layered Security:</strong><br><br>
        
        <strong>Layer 1: Perimeter Security</strong><br>
        • Firewall<br>
        • IDS/IPS<br>
        • DDoS protection<br><br>
        
        <strong>Layer 2: Network Security</strong><br>
        • Network segmentation<br>
        • VPN for remote access<br>
        • Wireless security (WPA3)<br><br>
        
        <strong>Layer 3: Host Security</strong><br>
        • Antivirus/anti-malware<br>
        • Host-based firewall<br>
        • Patch management<br>
        • Endpoint Detection and Response (EDR)<br><br>
        
        <strong>Layer 4: Application Security</strong><br>
        • Input validation<br>
        • Secure coding practices<br>
        • Web Application Firewall (WAF)<br>
        • Code review and SAST/DAST<br><br>
        
        <strong>Layer 5: Data Security</strong><br>
        • Encryption at rest and in transit<br>
        • Access control (RBAC)<br>
        • Data loss prevention (DLP)<br>
        • Backup and recovery
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Secure Coding Practices")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Input Validation:</strong><br>
        • Whitelist allowed characters<br>
        • Validate length, format, type<br>
        • Reject unexpected input<br>
        • Never trust user input!<br><br>
        
        <strong>Output Encoding:</strong><br>
        • HTML encoding for web output<br>
        • URL encoding for URLs<br>
        • JavaScript encoding for JS context<br>
        • Prevents XSS attacks<br><br>
        
        <strong>Authentication & Authorization:</strong><br>
        • Strong password policies<br>
        • Multi-factor authentication (MFA)<br>
        • Principle of least privilege<br>
        • Session management<br><br>
        
        <strong>Error Handling:</strong><br>
        • Don't expose stack traces<br>
        • Generic error messages to users<br>
        • Log detailed errors securely<br>
        • Fail securely (deny by default)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Security Monitoring")
    
    st.markdown("""
    <div class="defense-box">
        <strong>SIEM (Security Information and Event Management):</strong><br>
        • Centralized log collection<br>
        • Real-time analysis<br>
        • Correlation of events<br>
        • Alert on suspicious activity<br>
        • Tools: Splunk, ELK Stack, QRadar<br><br>
        
        <strong>Security Metrics:</strong><br>
        • Mean Time to Detect (MTTD)<br>
        • Mean Time to Respond (MTTR)<br>
        • Number of incidents<br>
        • Patch compliance rate<br>
        • Vulnerability scan results<br><br>
        
        <strong>Incident Response:</strong><br>
        1. <strong>Preparation:</strong> IR plan, team, tools<br>
        2. <strong>Detection:</strong> Identify incident<br>
        3. <strong>Containment:</strong> Isolate affected systems<br>
        4. <strong>Eradication:</strong> Remove threat<br>
        5. <strong>Recovery:</strong> Restore systems<br>
        6. <strong>Lessons Learned:</strong> Post-incident review
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: ETHICAL HACKING ====================
with tabs[5]:
    st.markdown("## 🎯 Ethical Hacking")
    
    st.markdown("### 1️⃣ Penetration Testing Methodology")
    
    st.markdown("""
    <div class="attack-box">
        <strong>Phases of Penetration Testing:</strong><br><br>
        
        <strong>1. Reconnaissance:</strong><br>
        • Passive: OSINT, Google dorking, WHOIS<br>
        • Active: Port scanning, service enumeration<br>
        • Tools: Nmap, Shodan, theHarvester<br><br>
        
        <strong>2. Scanning & Enumeration:</strong><br>
        • Port scanning (Nmap)<br>
        • Vulnerability scanning (Nessus, OpenVAS)<br>
        • Service version detection<br>
        • Banner grabbing<br><br>
        
        <strong>3. Exploitation:</strong><br>
        • Exploit vulnerabilities<br>
        • Gain access to systems<br>
        • Tools: Metasploit, SQLmap, Burp Suite<br><br>
        
        <strong>4. Post-Exploitation:</strong><br>
        • Privilege escalation<br>
        • Lateral movement<br>
        • Data exfiltration<br>
        • Maintain access (persistence)<br><br>
        
        <strong>5. Reporting:</strong><br>
        • Document findings<br>
        • Risk assessment<br>
        • Remediation recommendations<br>
        • Executive summary
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Essential Tools")
    
    tools_data = {
        'Tool': ['Nmap', 'Metasploit', 'Burp Suite', 'Wireshark', 'John the Ripper'],
        'Category': ['Scanning', 'Exploitation', 'Web Testing', 'Network Analysis', 'Password Cracking'],
        'Use Case': [
            'Port scanning, service detection',
            'Exploit framework, payload generation',
            'Web app testing, proxy, scanner',
            'Packet capture and analysis',
            'Password hash cracking'
        ],
        'Difficulty': ['Easy', 'Medium', 'Medium', 'Medium', 'Easy']
    }
    
    df_tools = pd.DataFrame(tools_data)
    st.dataframe(df_tools, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Legal & Ethical Considerations")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Legal Requirements:</strong><br>
        • <strong>Written Authorization:</strong> Always get permission!<br>
        • Scope of engagement clearly defined<br>
        • Rules of engagement documented<br>
        • Non-disclosure agreement (NDA)<br><br>
        
        <strong>Ethical Guidelines:</strong><br>
        • Only test authorized systems<br>
        • Don't cause damage or disruption<br>
        • Protect confidential information<br>
        • Report vulnerabilities responsibly<br>
        • Follow code of ethics (EC-Council, ISC²)<br><br>
        
        <strong>Certifications:</strong><br>
        • <strong>CEH:</strong> Certified Ethical Hacker<br>
        • <strong>OSCP:</strong> Offensive Security Certified Professional<br>
        • <strong>GPEN:</strong> GIAC Penetration Tester<br>
        • <strong>CompTIA PenTest+:</strong> Entry-level pen testing
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: COMPLIANCE ====================
with tabs[6]:
    st.markdown("## 📋 Compliance & Standards")
    
    st.markdown("### 1️⃣ Major Regulations")
    
    st.markdown("""
    <div class="defense-box">
        <strong>GDPR (General Data Protection Regulation):</strong><br>
        • EU data privacy law<br>
        • Applies to EU citizens' data<br>
        • Right to access, deletion, portability<br>
        • Data breach notification (72 hours)<br>
        • Fines up to €20M or 4% revenue<br><br>
        
        <strong>PCI-DSS (Payment Card Industry):</strong><br>
        • Protects credit card data<br>
        • 12 requirements, 6 control objectives<br>
        • Encryption of cardholder data<br>
        • Regular security testing<br>
        • Mandatory for merchants<br><br>
        
        <strong>HIPAA (Health Insurance Portability):</strong><br>
        • US healthcare data protection<br>
        • Protected Health Information (PHI)<br>
        • Administrative, physical, technical safeguards<br>
        • Business Associate Agreements (BAA)<br><br>
        
        <strong>SOX (Sarbanes-Oxley):</strong><br>
        • Financial reporting accuracy<br>
        • IT controls for financial systems<br>
        • Audit trails and access controls
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Security Frameworks")
    
    st.markdown("""
    <div class="theory-box">
        <strong>ISO 27001:</strong><br>
        • Information security management system (ISMS)<br>
        • Risk assessment and treatment<br>
        • 114 security controls (Annex A)<br>
        • Certification available<br><br>
        
        <strong>NIST Cybersecurity Framework:</strong><br>
        • 5 core functions: Identify, Protect, Detect, Respond, Recover<br>
        • Risk-based approach<br>
        • Widely adopted in US<br><br>
        
        <strong>CIS Controls:</strong><br>
        • 18 critical security controls<br>
        • Prioritized and actionable<br>
        • Implementation groups (IG1, IG2, IG3)<br><br>
        
        <strong>OWASP ASVS:</strong><br>
        • Application Security Verification Standard<br>
        • 3 levels of security requirements<br>
        • For web applications
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: YOUTUBE ====================
with tabs[7]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning Cybersecurity</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {"title": "Cybersecurity Fundamentals", "channel": "Professor Messer", "url": "https://www.youtube.com/c/professormesser", "description": "CompTIA Security+ course", "duration": "Channel"},
        {"title": "Introduction to Cybersecurity", "channel": "Cisco", "url": "https://www.youtube.com/watch?v=inWWhr5tnEA", "description": "Cybersecurity basics", "duration": "~1 hour"},
        {"title": "How Encryption Works", "channel": "Computerphile", "url": "https://www.youtube.com/watch?v=jhXCTbFnK8o", "description": "Cryptography explained", "duration": "~10 min"}
    ]
    
    for resource in beginner_resources:
        title = resource['title']
        channel = resource['channel']
        url = resource['url']
        description = resource['description']
        duration = resource['duration']
        st.markdown(f"**[{title}]({url})**  \n📺 Channel: {channel} | ⏱️ {duration}  \n{description}")
        st.markdown("---")
    
    # Intermediate Level
    st.markdown("### 🟡 Intermediate Level")
    
    intermediate_resources = [
        {"title": "Ethical Hacking Course", "channel": "freeCodeCamp.org", "url": "https://www.youtube.com/watch?v=3Kq1MIfTWCE", "description": "Complete ethical hacking", "duration": "~15 hours"},
        {"title": "Web Security", "channel": "LiveOverflow", "url": "https://www.youtube.com/c/LiveOverflow", "description": "Web hacking tutorials", "duration": "Channel"},
        {"title": "Network Security", "channel": "NetworkChuck", "url": "https://www.youtube.com/c/NetworkChuck", "description": "Networking and security", "duration": "Channel"}
    ]
    
    for resource in intermediate_resources:
        title = resource['title']
        channel = resource['channel']
        url = resource['url']
        description = resource['description']
        duration = resource['duration']
        st.markdown(f"**[{title}]({url})**  \n📺 Channel: {channel} | ⏱️ {duration}  \n{description}")
        st.markdown("---")
    
    # Advanced Level
    st.markdown("### 🔴 Advanced Level")
    
    advanced_resources = [
        {"title": "Advanced Penetration Testing", "channel": "The Cyber Mentor", "url": "https://www.youtube.com/c/TheCyberMentor", "description": "OSCP prep, pen testing", "duration": "Channel"},
        {"title": "Malware Analysis", "channel": "OALabs", "url": "https://www.youtube.com/c/OALabs", "description": "Reverse engineering", "duration": "Channel"},
        {"title": "Bug Bounty", "channel": "STÖK", "url": "https://www.youtube.com/c/STOKfredrik", "description": "Bug bounty hunting", "duration": "Channel"}
    ]
    
    for resource in advanced_resources:
        title = resource['title']
        channel = resource['channel']
        url = resource['url']
        description = resource['description']
        duration = resource['duration']
        st.markdown(f"**[{title}]({url})**  \n📺 Channel: {channel} | ⏱️ {duration}  \n{description}")
        st.markdown("---")
    
    # Study Tips
    st.markdown("### 💡 Study Tips")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Recommended Learning Path:</strong><br>
        1. Learn networking fundamentals (TCP/IP, HTTP)<br>
        2. Understand Linux command line<br>
        3. Study cryptography basics<br>
        4. Practice with CTF challenges (HackTheBox, TryHackMe)<br>
        5. Learn penetration testing methodology<br>
        6. Master security tools (Nmap, Burp Suite, Metasploit)<br>
        7. Get certified (Security+, CEH, OSCP)<br>
        8. Participate in bug bounty programs<br><br>
        
        <strong>Practice Platforms:</strong><br>
        • <strong>TryHackMe:</strong> Beginner-friendly labs<br>
        • <strong>HackTheBox:</strong> Advanced challenges<br>
        • <strong>PortSwigger Web Security Academy:</strong> Web hacking<br>
        • <strong>PentesterLab:</strong> Hands-on exercises<br>
        • <strong>VulnHub:</strong> Vulnerable VMs<br><br>
        
        <strong>Career Paths:</strong><br>
        • Penetration Tester<br>
        • Security Analyst<br>
        • Security Engineer<br>
        • Incident Responder<br>
        • Security Architect<br>
        • Bug Bounty Hunter
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE405 - Cybersecurity</strong><br>
    <small>UTel University | Computer Engineering Program</small>
</div>
""", unsafe_allow_html=True)
