import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="IT301 - IT Concentration", page_icon="💻", layout="wide")

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
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
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
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .cloud-box {
        background: linear-gradient(135deg, #e0e7ff 0%, #c7d2fe 100%);
        border-left: 5px solid #6366f1;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .security-box {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        border-left: 5px solid #ef4444;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .devops-box {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .youtube-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="course-header">
    <div style="font-size: 1.2rem; opacity: 0.9;">IT301</div>
    <div class="course-title">Concentration - Information Technology</div>
    <div>💻 3 Credits | Semester 6 | Cloud, Security & Infrastructure</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "6")
with col3:
    st.metric("Difficulty", "5/7")
with col4:
    st.metric("Hours/Week", "6")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "☁️ Cloud Computing",
    "🔒 Cybersecurity",
    "🚀 DevOps & CI/CD",
    "🏢 Enterprise Systems",
    "📡 Networking",
    "🛠️ Infrastructure as Code",
    "🎯 Case Studies",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Advanced study of information technology infrastructure, cloud computing, cybersecurity, and enterprise systems. 
        Covers major cloud platforms (AWS, Azure, GCP), security best practices, DevOps methodologies, containerization, 
        orchestration, networking, and infrastructure automation. Emphasizes hands-on implementation, industry certifications, 
        and real-world IT operations. Students will design cloud architectures, implement security measures, automate 
        infrastructure, and manage enterprise IT systems.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Master cloud platforms (AWS, Azure, Google Cloud)",
        "Implement cybersecurity best practices and compliance",
        "Design and deploy containerized applications (Docker, Kubernetes)",
        "Build CI/CD pipelines for automated deployment",
        "Manage enterprise IT infrastructure and systems",
        "Implement Infrastructure as Code (Terraform, CloudFormation)",
        "Configure networking and security groups",
        "Monitor and optimize system performance"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Cloud Computing:**
        - AWS (EC2, S3, Lambda, RDS, VPC)
        - Azure (VMs, Storage, Functions, SQL)
        - Google Cloud Platform (Compute Engine, Cloud Storage)
        - Cloud architecture patterns
        - Serverless computing
        
        **Cybersecurity:**
        - Network security
        - Identity and Access Management (IAM)
        - Encryption and PKI
        - Security monitoring and SIEM
        - Compliance (GDPR, SOC 2, ISO 27001)
        """)
    
    with col2:
        st.markdown("""
        **DevOps & Automation:**
        - CI/CD pipelines (Jenkins, GitLab CI, GitHub Actions)
        - Containerization (Docker)
        - Orchestration (Kubernetes)
        - Infrastructure as Code (Terraform, Ansible)
        - Monitoring (Prometheus, Grafana)
        
        **Enterprise Systems:**
        - Active Directory and LDAP
        - Email systems (Exchange, Gmail)
        - ERP and CRM systems
        - Backup and disaster recovery
        - IT service management (ITIL)
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "AWS Certified Solutions Architect", "author": "Amazon Web Services", "type": "Certification"},
        {"title": "The Phoenix Project", "author": "Gene Kim", "type": "DevOps"},
        {"title": "Kubernetes in Action", "author": "Marko Lukša", "type": "Containers"},
        {"title": "Terraform: Up & Running", "author": "Yevgeniy Brikman", "type": "IaC"}
    ]
    
    for resource in resources:
        title = resource['title']
        author = resource['author']
        rtype = resource['type']
        st.markdown(f"📖 **{title}** by {author} ({rtype})")

# ==================== TAB 2: CLOUD COMPUTING ====================
with tabs[1]:
    st.markdown("## ☁️ Cloud Computing")
    
    st.markdown("### 1️⃣ AWS (Amazon Web Services)")
    
    st.markdown("""
    <div class="cloud-box">
        <strong>Core Services:</strong><br><br>
        
        <strong>Compute:</strong><br>
        • <strong>EC2:</strong> Virtual servers, instance types (t2, m5, c5)<br>
        • <strong>Lambda:</strong> Serverless functions, event-driven<br>
        • <strong>ECS/EKS:</strong> Container services<br>
        • <strong>Elastic Beanstalk:</strong> Platform as a Service<br><br>
        
        <strong>Storage:</strong><br>
        • <strong>S3:</strong> Object storage, buckets, versioning<br>
        • <strong>EBS:</strong> Block storage for EC2<br>
        • <strong>EFS:</strong> Elastic File System<br>
        • <strong>Glacier:</strong> Archive storage<br><br>
        
        <strong>Database:</strong><br>
        • <strong>RDS:</strong> Relational (MySQL, PostgreSQL, Oracle)<br>
        • <strong>DynamoDB:</strong> NoSQL, key-value<br>
        • <strong>ElastiCache:</strong> Redis, Memcached<br>
        • <strong>Aurora:</strong> High-performance MySQL/PostgreSQL<br><br>
        
        <strong>Networking:</strong><br>
        • <strong>VPC:</strong> Virtual Private Cloud<br>
        • <strong>Route 53:</strong> DNS service<br>
        • <strong>CloudFront:</strong> CDN<br>
        • <strong>ELB:</strong> Elastic Load Balancing
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Azure (Microsoft Azure)")
    
    st.markdown("""
    <div class="cloud-box">
        <strong>Core Services:</strong><br><br>
        
        <strong>Compute:</strong><br>
        • <strong>Virtual Machines:</strong> Windows and Linux VMs<br>
        • <strong>Azure Functions:</strong> Serverless compute<br>
        • <strong>App Service:</strong> Web apps, APIs<br>
        • <strong>AKS:</strong> Azure Kubernetes Service<br><br>
        
        <strong>Storage:</strong><br>
        • <strong>Blob Storage:</strong> Object storage<br>
        • <strong>File Storage:</strong> SMB file shares<br>
        • <strong>Disk Storage:</strong> Managed disks<br>
        • <strong>Archive Storage:</strong> Long-term storage<br><br>
        
        <strong>Database:</strong><br>
        • <strong>Azure SQL:</strong> Managed SQL Server<br>
        • <strong>Cosmos DB:</strong> Multi-model NoSQL<br>
        • <strong>MySQL/PostgreSQL:</strong> Managed databases<br><br>
        
        <strong>Integration:</strong><br>
        • <strong>Active Directory:</strong> Identity management<br>
        • <strong>Office 365:</strong> Productivity suite<br>
        • <strong>Power Platform:</strong> Low-code tools
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Google Cloud Platform (GCP)")
    
    st.markdown("""
    <div class="cloud-box">
        <strong>Core Services:</strong><br><br>
        
        <strong>Compute:</strong><br>
        • <strong>Compute Engine:</strong> Virtual machines<br>
        • <strong>Cloud Functions:</strong> Serverless<br>
        • <strong>App Engine:</strong> PaaS<br>
        • <strong>GKE:</strong> Google Kubernetes Engine<br><br>
        
        <strong>Storage:</strong><br>
        • <strong>Cloud Storage:</strong> Object storage<br>
        • <strong>Persistent Disk:</strong> Block storage<br>
        • <strong>Filestore:</strong> Managed NFS<br><br>
        
        <strong>Database:</strong><br>
        • <strong>Cloud SQL:</strong> MySQL, PostgreSQL<br>
        • <strong>Firestore:</strong> NoSQL document database<br>
        • <strong>Bigtable:</strong> Wide-column NoSQL<br>
        • <strong>Spanner:</strong> Globally distributed SQL<br><br>
        
        <strong>AI/ML:</strong><br>
        • <strong>Vertex AI:</strong> ML platform<br>
        • <strong>BigQuery:</strong> Data warehouse<br>
        • <strong>TensorFlow:</strong> ML framework
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Cloud Architecture Patterns")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Multi-Tier Architecture:</strong><br>
        • Web tier (load balancer, web servers)<br>
        • Application tier (app servers)<br>
        • Database tier (primary, replicas)<br>
        • Scalable and maintainable<br><br>
        
        <strong>Microservices:</strong><br>
        • Independent services<br>
        • API gateway<br>
        • Service mesh<br>
        • Containerized deployment<br><br>
        
        <strong>Serverless:</strong><br>
        • Event-driven functions<br>
        • Auto-scaling<br>
        • Pay per execution<br>
        • No server management<br><br>
        
        <strong>High Availability:</strong><br>
        • Multi-AZ deployment<br>
        • Auto-scaling groups<br>
        • Health checks<br>
        • Disaster recovery
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: CYBERSECURITY ====================
with tabs[2]:
    st.markdown("## 🔒 Cybersecurity")
    
    st.markdown("### 1️⃣ Network Security")
    
    st.markdown("""
    <div class="security-box">
        <strong>Firewalls:</strong><br>
        • Packet filtering<br>
        • Stateful inspection<br>
        • Application-level gateways<br>
        • Next-generation firewalls (NGFW)<br><br>
        
        <strong>Intrusion Detection/Prevention:</strong><br>
        • <strong>IDS:</strong> Detect malicious activity<br>
        • <strong>IPS:</strong> Block threats in real-time<br>
        • Signature-based detection<br>
        • Anomaly-based detection<br><br>
        
        <strong>VPN (Virtual Private Network):</strong><br>
        • Site-to-site VPN<br>
        • Remote access VPN<br>
        • IPsec, SSL/TLS<br>
        • Encrypted tunnels<br><br>
        
        <strong>Zero Trust Security:</strong><br>
        • Never trust, always verify<br>
        • Least privilege access<br>
        • Micro-segmentation<br>
        • Continuous monitoring
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Identity and Access Management (IAM)")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Authentication:</strong><br>
        • <strong>Single Sign-On (SSO):</strong> One login for multiple apps<br>
        • <strong>Multi-Factor Authentication (MFA):</strong> Something you know + have + are<br>
        • <strong>OAuth 2.0:</strong> Authorization framework<br>
        • <strong>SAML:</strong> Security Assertion Markup Language<br><br>
        
        <strong>Authorization:</strong><br>
        • <strong>RBAC:</strong> Role-Based Access Control<br>
        • <strong>ABAC:</strong> Attribute-Based Access Control<br>
        • <strong>Least Privilege:</strong> Minimum necessary permissions<br>
        • <strong>Separation of Duties:</strong> No single person has complete control<br><br>
        
        <strong>Identity Providers:</strong><br>
        • Active Directory (Microsoft)<br>
        • Okta<br>
        • Auth0<br>
        • AWS IAM, Azure AD, Google Cloud Identity
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Encryption")
    
    st.markdown("""
    <div class="security-box">
        <strong>Symmetric Encryption:</strong><br>
        • Same key for encryption and decryption<br>
        • Fast, efficient<br>
        • AES (Advanced Encryption Standard)<br>
        • Use cases: Data at rest<br><br>
        
        <strong>Asymmetric Encryption:</strong><br>
        • Public key for encryption, private key for decryption<br>
        • RSA, ECC (Elliptic Curve Cryptography)<br>
        • Use cases: Key exchange, digital signatures<br><br>
        
        <strong>Hashing:</strong><br>
        • One-way function<br>
        • SHA-256, SHA-3<br>
        • Use cases: Password storage, integrity verification<br><br>
        
        <strong>TLS/SSL:</strong><br>
        • Secure communication over networks<br>
        • HTTPS, certificate authorities<br>
        • Perfect Forward Secrecy (PFS)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Security Monitoring")
    
    st.markdown("""
    <div class="theory-box">
        <strong>SIEM (Security Information and Event Management):</strong><br>
        • Centralized log collection<br>
        • Real-time analysis<br>
        • Threat detection<br>
        • Compliance reporting<br>
        • Tools: Splunk, ELK Stack, QRadar<br><br>
        
        <strong>Vulnerability Management:</strong><br>
        • Regular scanning<br>
        • Patch management<br>
        • Penetration testing<br>
        • Bug bounty programs<br><br>
        
        <strong>Incident Response:</strong><br>
        1. Preparation<br>
        2. Detection and Analysis<br>
        3. Containment<br>
        4. Eradication<br>
        5. Recovery<br>
        6. Post-Incident Review
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: DEVOPS ====================
with tabs[3]:
    st.markdown("## 🚀 DevOps & CI/CD")
    
    st.markdown("### 1️⃣ Continuous Integration/Continuous Deployment")
    
    st.markdown("""
    <div class="devops-box">
        <strong>CI/CD Pipeline:</strong><br><br>
        
        <strong>1. Source Control:</strong><br>
        • Git (GitHub, GitLab, Bitbucket)<br>
        • Branching strategies (GitFlow, trunk-based)<br>
        • Pull requests and code review<br><br>
        
        <strong>2. Build:</strong><br>
        • Compile code<br>
        • Run unit tests<br>
        • Static code analysis<br>
        • Dependency management<br><br>
        
        <strong>3. Test:</strong><br>
        • Integration tests<br>
        • End-to-end tests<br>
        • Performance tests<br>
        • Security scans<br><br>
        
        <strong>4. Deploy:</strong><br>
        • Staging environment<br>
        • Production deployment<br>
        • Blue-green deployment<br>
        • Canary releases<br>
        • Rollback capability
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Containerization")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Docker:</strong><br>
        • Lightweight virtualization<br>
        • Dockerfile for image creation<br>
        • Docker Compose for multi-container apps<br>
        • Docker Hub for image registry<br><br>
        
        <strong>Docker Commands:</strong><br>
        <pre>
# Build image
docker build -t myapp:1.0 .

# Run container
docker run -d -p 8080:80 myapp:1.0

# List containers
docker ps

# View logs
docker logs container_id

# Stop container
docker stop container_id
        </pre><br>
        
        <strong>Best Practices:</strong><br>
        • Use official base images<br>
        • Minimize layers<br>
        • Don't run as root<br>
        • Use .dockerignore<br>
        • Multi-stage builds for smaller images
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Kubernetes")
    
    st.markdown("""
    <div class="devops-box">
        <strong>Kubernetes Architecture:</strong><br>
        • <strong>Master Node:</strong> API server, scheduler, controller manager<br>
        • <strong>Worker Nodes:</strong> Run containers (pods)<br>
        • <strong>etcd:</strong> Distributed key-value store<br><br>
        
        <strong>Core Concepts:</strong><br>
        • <strong>Pod:</strong> Smallest deployable unit<br>
        • <strong>Deployment:</strong> Manages replica sets<br>
        • <strong>Service:</strong> Exposes pods to network<br>
        • <strong>ConfigMap:</strong> Configuration data<br>
        • <strong>Secret:</strong> Sensitive data<br>
        • <strong>Ingress:</strong> HTTP routing<br>
        • <strong>Namespace:</strong> Virtual clusters<br><br>
        
        <strong>kubectl Commands:</strong><br>
        <pre>
# Get resources
kubectl get pods
kubectl get services

# Deploy application
kubectl apply -f deployment.yaml

# Scale deployment
kubectl scale deployment myapp --replicas=5

# View logs
kubectl logs pod_name

# Execute command in pod
kubectl exec -it pod_name -- /bin/bash
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: ENTERPRISE SYSTEMS ====================
with tabs[4]:
    st.markdown("## 🏢 Enterprise Systems")
    
    st.markdown("### 1️⃣ Active Directory")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Active Directory Domain Services (AD DS):</strong><br>
        • Centralized user and computer management<br>
        • Authentication and authorization<br>
        • Group Policy for configuration management<br>
        • Organizational Units (OUs)<br><br>
        
        <strong>Key Components:</strong><br>
        • <strong>Domain Controller:</strong> Stores AD database<br>
        • <strong>Users and Groups:</strong> Identity management<br>
        • <strong>Group Policy Objects (GPO):</strong> Settings and policies<br>
        • <strong>LDAP:</strong> Lightweight Directory Access Protocol<br><br>
        
        <strong>Azure Active Directory:</strong><br>
        • Cloud-based identity service<br>
        • SSO for cloud apps<br>
        • Multi-factor authentication<br>
        • Integration with on-premises AD
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Email Systems")
    
    st.markdown("""
    <div class="cloud-box">
        <strong>Microsoft Exchange:</strong><br>
        • On-premises email server<br>
        • Mailbox management<br>
        • Calendar and contacts<br>
        • Outlook integration<br><br>
        
        <strong>Office 365 / Microsoft 365:</strong><br>
        • Cloud-based email (Exchange Online)<br>
        • SharePoint, OneDrive<br>
        • Teams for collaboration<br>
        • Security and compliance features<br><br>
        
        <strong>Google Workspace:</strong><br>
        • Gmail for business<br>
        • Google Drive<br>
        • Google Meet<br>
        • Admin console for management
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Backup and Disaster Recovery")
    
    st.markdown("""
    <div class="security-box">
        <strong>Backup Strategies:</strong><br>
        • <strong>Full Backup:</strong> Complete copy of all data<br>
        • <strong>Incremental:</strong> Changes since last backup<br>
        • <strong>Differential:</strong> Changes since last full backup<br>
        • <strong>3-2-1 Rule:</strong> 3 copies, 2 different media, 1 offsite<br><br>
        
        <strong>Disaster Recovery:</strong><br>
        • <strong>RTO:</strong> Recovery Time Objective<br>
        • <strong>RPO:</strong> Recovery Point Objective<br>
        • <strong>Hot Site:</strong> Fully operational backup site<br>
        • <strong>Warm Site:</strong> Partially equipped<br>
        • <strong>Cold Site:</strong> Basic infrastructure only<br><br>
        
        <strong>Tools:</strong><br>
        • Veeam Backup & Replication<br>
        • AWS Backup<br>
        • Azure Backup<br>
        • Commvault
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: NETWORKING ====================
with tabs[5]:
    st.markdown("## 📡 Networking")
    
    st.markdown("### 1️⃣ Network Fundamentals")
    
    st.markdown("""
    <div class="theory-box">
        <strong>OSI Model:</strong><br>
        1. Physical: Cables, signals<br>
        2. Data Link: MAC addresses, switches<br>
        3. Network: IP addresses, routing<br>
        4. Transport: TCP, UDP<br>
        5. Session: Connections<br>
        6. Presentation: Encryption, compression<br>
        7. Application: HTTP, FTP, SMTP<br><br>
        
        <strong>TCP/IP Model:</strong><br>
        1. Network Access<br>
        2. Internet (IP)<br>
        3. Transport (TCP/UDP)<br>
        4. Application<br><br>
        
        <strong>IP Addressing:</strong><br>
        • IPv4: 32-bit (192.168.1.1)<br>
        • IPv6: 128-bit (2001:0db8::1)<br>
        • CIDR notation: 192.168.1.0/24<br>
        • Private ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Cloud Networking")
    
    st.markdown("""
    <div class="cloud-box">
        <strong>Virtual Private Cloud (VPC):</strong><br>
        • Isolated network in cloud<br>
        • Subnets (public, private)<br>
        • Route tables<br>
        • Internet Gateway<br>
        • NAT Gateway<br><br>
        
        <strong>Security Groups:</strong><br>
        • Virtual firewalls<br>
        • Inbound and outbound rules<br>
        • Stateful (AWS) vs Stateless (Network ACLs)<br>
        • Allow rules only<br><br>
        
        <strong>Load Balancing:</strong><br>
        • <strong>Application Load Balancer:</strong> HTTP/HTTPS (Layer 7)<br>
        • <strong>Network Load Balancer:</strong> TCP/UDP (Layer 4)<br>
        • <strong>Classic Load Balancer:</strong> Legacy<br>
        • Health checks and auto-scaling
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: INFRASTRUCTURE AS CODE ====================
with tabs[6]:
    st.markdown("## 🛠️ Infrastructure as Code")
    
    st.markdown("### 1️⃣ Terraform")
    
    st.markdown("""
    <div class="devops-box">
        <strong>Terraform Basics:</strong><br>
        • Declarative infrastructure<br>
        • Multi-cloud support<br>
        • State management<br>
        • Modules for reusability<br><br>
        
        <strong>Example: AWS EC2 Instance</strong><br>
        <pre>
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  
  tags = {
    Name = "WebServer"
  }
}

output "instance_ip" {
  value = aws_instance.web.public_ip
}
        </pre><br>
        
        <strong>Terraform Commands:</strong><br>
        <pre>
# Initialize
terraform init

# Plan changes
terraform plan

# Apply changes
terraform apply

# Destroy infrastructure
terraform destroy
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Ansible")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Ansible Basics:</strong><br>
        • Agentless configuration management<br>
        • YAML playbooks<br>
        • SSH-based<br>
        • Idempotent operations<br><br>
        
        <strong>Example Playbook:</strong><br>
        <pre>
---
- name: Install and configure web server
  hosts: webservers
  become: yes
  
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
    
    - name: Start nginx
      service:
        name: nginx
        state: started
        enabled: yes
    
    - name: Copy config file
      copy:
        src: nginx.conf
        dest: /etc/nginx/nginx.conf
      notify: Restart nginx
  
  handlers:
    - name: Restart nginx
      service:
        name: nginx
        state: restarted
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: CASE STUDIES ====================
with tabs[7]:
    st.markdown("## 🎯 Case Studies")
    
    case_studies = [
        {
            "title": "Case Study 1: Deploy Scalable Web App on AWS",
            "description": "Design and deploy a highly available web application on AWS",
            "details": """
**Objective:** Deploy a 3-tier web application with auto-scaling, load balancing, and database replication.

**Requirements:**
1. Web tier: Auto-scaling group of EC2 instances behind ALB
2. Application tier: Containerized microservices on ECS
3. Database tier: RDS MySQL with Multi-AZ deployment
4. CDN for static assets (CloudFront)
5. S3 for file storage
6. Route 53 for DNS
7. CloudWatch for monitoring

**Architecture:**
- VPC with public and private subnets across 2 AZs
- Application Load Balancer in public subnets
- EC2 instances in private subnets
- RDS in private subnets with read replicas
- NAT Gateway for outbound internet access
- Security groups for network isolation

**Implementation:**
1. Create VPC and subnets
2. Set up Internet Gateway and NAT Gateway
3. Configure route tables
4. Launch RDS instance
5. Create Auto Scaling Group
6. Configure Application Load Balancer
7. Set up CloudFront distribution
8. Configure Route 53
9. Implement monitoring and alerts
            """,
            "solution": """
**Terraform Configuration:**

```hcl
# VPC
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  enable_dns_hostnames = true
  
  tags = {
    Name = "main-vpc"
  }
}

# Public Subnet
resource "aws_subnet" "public" {
  count = 2
  vpc_id = aws_vpc.main.id
  cidr_block = "10.0.${count.index}.0/24"
  availability_zone = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = true
  
  tags = {
    Name = "public-subnet-${count.index + 1}"
  }
}

# Application Load Balancer
resource "aws_lb" "main" {
  name = "web-alb"
  load_balancer_type = "application"
  subnets = aws_subnet.public[*].id
  security_groups = [aws_security_group.alb.id]
}

# Auto Scaling Group
resource "aws_autoscaling_group" "web" {
  desired_capacity = 2
  max_size = 4
  min_size = 2
  vpc_zone_identifier = aws_subnet.private[*].id
  target_group_arns = [aws_lb_target_group.web.arn]
  
  launch_template {
    id = aws_launch_template.web.id
    version = "$Latest"
  }
}
```

**Results:**
- 99.99% uptime achieved
- Auto-scales from 2 to 4 instances based on CPU
- Average response time: 150ms
- Handles 10,000 concurrent users
- Monthly cost: ~$500
            """
        },
        {
            "title": "Case Study 2: Implement CI/CD Pipeline",
            "description": "Build automated deployment pipeline with GitHub Actions and Kubernetes",
            "details": """
**Objective:** Create CI/CD pipeline that automatically builds, tests, and deploys application to Kubernetes cluster.

**Pipeline Stages:**
1. **Trigger:** Push to main branch
2. **Build:** Compile code, run unit tests
3. **Docker:** Build and push container image
4. **Test:** Run integration tests
5. **Deploy:** Deploy to Kubernetes cluster
6. **Verify:** Health checks and smoke tests

**Tools:**
- GitHub Actions for CI/CD
- Docker for containerization
- Kubernetes for orchestration
- Helm for package management
- ArgoCD for GitOps

**Deployment Strategy:**
- Blue-green deployment
- Automated rollback on failure
- Canary releases for gradual rollout
            """,
            "solution": """
**GitHub Actions Workflow:**

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v2
      
      - name: Run tests
        run: |
          npm install
          npm test
      
      - name: Build Docker image
        run: |
          docker build -t myapp:${{ github.sha }} .
      
      - name: Push to registry
        run: |
          echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
          docker push myapp:${{ github.sha }}
      
      - name: Deploy to Kubernetes
        run: |
          kubectl set image deployment/myapp myapp=myapp:${{ github.sha }}
          kubectl rollout status deployment/myapp
```

**Results:**
- Deployment time reduced from 2 hours to 10 minutes
- Zero-downtime deployments
- Automated testing catches 95% of bugs before production
- 50+ deployments per week
            """
        }
    ]
    
    for idx, case in enumerate(case_studies, 1):
        with st.expander(f"📝 {case['title']}", expanded=False):
            st.markdown(f"**Description:** {case['description']}")
            st.markdown(case['details'])
            
            if st.button(f"Show Solution", key=f"case_{idx}"):
                st.markdown("### Solution")
                st.markdown(case['solution'])

# ==================== TAB 9: YOUTUBE ====================
with tabs[8]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning IT and Cloud Computing</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {"title": "AWS Certified Cloud Practitioner", "channel": "freeCodeCamp.org", "url": "https://www.youtube.com/watch?v=SOTamWNgDKc", "description": "Complete AWS beginner course", "duration": "~4 hours"},
        {"title": "Docker Tutorial", "channel": "TechWorld with Nana", "url": "https://www.youtube.com/watch?v=3c-iBn73dDE", "description": "Docker crash course", "duration": "~3 hours"},
        {"title": "Networking Fundamentals", "channel": "NetworkChuck", "url": "https://www.youtube.com/playlist?list=PLIhvC56v63IJVXv0GJcl9vO5Z6znCVb1P", "description": "Complete networking course", "duration": "Playlist"}
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
        {"title": "Kubernetes Course", "channel": "TechWorld with Nana", "url": "https://www.youtube.com/watch?v=X48VuDVv0do", "description": "Complete Kubernetes tutorial", "duration": "~4 hours"},
        {"title": "DevOps with GitLab CI", "channel": "Valentin Despa", "url": "https://www.youtube.com/watch?v=qP8kir2GUgo", "description": "GitLab CI/CD course", "duration": "~5 hours"},
        {"title": "Terraform Course", "channel": "freeCodeCamp.org", "url": "https://www.youtube.com/watch?v=SLB_c_ayRMo", "description": "Infrastructure as Code", "duration": "~2 hours"}
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
        {"title": "AWS Solutions Architect", "channel": "A Cloud Guru", "url": "https://www.youtube.com/c/AcloudGuru", "description": "Advanced AWS certification", "duration": "Channel"},
        {"title": "Kubernetes Security", "channel": "KodeKloud", "url": "https://www.youtube.com/c/KodeKloud", "description": "Advanced K8s topics", "duration": "Channel"},
        {"title": "Site Reliability Engineering", "channel": "Google Cloud Tech", "url": "https://www.youtube.com/playlist?list=PLIivdWyY5sqJrKl7D2u-gmis8h9K66qoj", "description": "SRE best practices", "duration": "Playlist"}
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
        1. Learn Linux command line basics<br>
        2. Understand networking fundamentals<br>
        3. Master one cloud platform (AWS recommended)<br>
        4. Learn Docker containerization<br>
        5. Study Kubernetes orchestration<br>
        6. Implement CI/CD pipelines<br>
        7. Learn Infrastructure as Code (Terraform)<br>
        8. Get cloud certifications<br><br>
        
        <strong>Certifications:</strong><br>
        • <strong>AWS:</strong> Cloud Practitioner → Solutions Architect → DevOps Engineer<br>
        • <strong>Azure:</strong> AZ-900 → AZ-104 → AZ-400<br>
        • <strong>Google Cloud:</strong> Associate Cloud Engineer → Professional Cloud Architect<br>
        • <strong>Kubernetes:</strong> CKA (Certified Kubernetes Administrator)<br>
        • <strong>Security:</strong> CompTIA Security+, CISSP<br><br>
        
        <strong>Career Paths:</strong><br>
        • Cloud Architect<br>
        • DevOps Engineer<br>
        • Site Reliability Engineer (SRE)<br>
        • Cybersecurity Specialist<br>
        • Systems Administrator
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>IT301 - Information Technology Concentration</strong><br>
    <small>UTel University | Computer Engineering Program</small>
</div>
""", unsafe_allow_html=True)
