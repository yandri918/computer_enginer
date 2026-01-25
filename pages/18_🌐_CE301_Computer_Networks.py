import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="CE301 - Computer Networks", page_icon="🌐", layout="wide")

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
    
    .protocol-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .network-box {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border-left: 5px solid #10b981;
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
    
    .youtube-box {
        background: linear-gradient(135deg, #fce7f3 0%, #fbcfe8 100%);
        border-left: 5px solid #ec4899;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="course-header">
    <div style="font-size: 1.2rem; opacity: 0.9;">CE301</div>
    <div class="course-title">Computer Networks</div>
    <div>🌐 3 Credits | Semester 4 | Networking</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "4")
with col3:
    st.metric("Difficulty", "5/7")
with col4:
    st.metric("Hours/Week", "7")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "🏗️ Network Models",
    "🔗 Data Link Layer",
    "🌍 Network Layer",
    "🚀 Transport Layer",
    "💻 Application Layer",
    "🔐 Network Security",
    "🛠️ Network Design",
    "🎯 Practice Problems",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive study of computer network architectures, protocols, and technologies. Covers OSI and TCP/IP models, 
        network protocols (Ethernet, IP, TCP, UDP, HTTP), routing algorithms, network security, and wireless networks. 
        Emphasizes both theoretical foundations and practical implementation using network simulation tools and real hardware. 
        Students will design, configure, and troubleshoot networks.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Understand OSI and TCP/IP network models",
        "Analyze network protocols at each layer",
        "Design and implement IP addressing schemes (IPv4/IPv6)",
        "Configure routing protocols (RIP, OSPF, BGP)",
        "Implement network security mechanisms",
        "Troubleshoot network problems",
        "Design scalable network architectures",
        "Understand wireless and mobile networks"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Fundamentals:**
        - Network architectures and topologies
        - OSI 7-layer model
        - TCP/IP protocol suite
        - Network performance metrics
        - Circuit vs packet switching
        
        **Protocols:**
        - Ethernet and MAC protocols
        - IP (IPv4 and IPv6)
        - TCP and UDP
        - HTTP, DNS, SMTP, FTP
        - ARP, ICMP, DHCP
        """)
    
    with col2:
        st.markdown("""
        **Advanced Topics:**
        - Routing algorithms (Distance Vector, Link State)
        - Congestion control
        - Quality of Service (QoS)
        - Network security (Firewalls, VPN, SSL/TLS)
        - Software-Defined Networking (SDN)
        
        **Technologies:**
        - Wireless networks (WiFi, 4G/5G)
        - Network Address Translation (NAT)
        - Virtual LANs (VLANs)
        - Cloud networking
        - IoT networks
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Computer Networking: A Top-Down Approach", "author": "Kurose & Ross", "type": "Textbook"},
        {"title": "Computer Networks", "author": "Andrew Tanenbaum", "type": "Textbook"},
        {"title": "TCP/IP Illustrated", "author": "W. Richard Stevens", "type": "Classic"},
        {"title": "Network Warrior", "author": "Gary Donahue", "type": "Practical"}
    ]
    
    for resource in resources:
        st.markdown(f"📖 **{resource['title']}** by {resource['author']} ({resource['type']})")

# ==================== TAB 2: NETWORK MODELS ====================
with tabs[1]:
    st.markdown("## 🏗️ Network Models")
    
    st.markdown("### 1️⃣ OSI Model (7 Layers)")
    
    osi_data = {
        'Layer': ['7. Application', '6. Presentation', '5. Session', '4. Transport', '3. Network', '2. Data Link', '1. Physical'],
        'Function': [
            'User interface, network services',
            'Data formatting, encryption',
            'Session management',
            'End-to-end connections, reliability',
            'Routing, logical addressing',
            'Frame delivery, MAC addressing',
            'Bit transmission, physical medium'
        ],
        'Protocols': [
            'HTTP, FTP, SMTP, DNS',
            'SSL/TLS, JPEG, MPEG',
            'NetBIOS, RPC',
            'TCP, UDP',
            'IP, ICMP, OSPF, BGP',
            'Ethernet, PPP, WiFi',
            'Ethernet physical, USB'
        ],
        'PDU': ['Data', 'Data', 'Data', 'Segment', 'Packet', 'Frame', 'Bit']
    }
    
    df_osi = pd.DataFrame(osi_data)
    st.dataframe(df_osi, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ TCP/IP Model (4 Layers)")
    
    st.markdown("""
    <div class="theory-box">
        <strong>TCP/IP Model vs OSI Model:</strong><br><br>
        
        <strong>4. Application Layer</strong> (OSI 5-7)<br>
        • Combines Application, Presentation, Session<br>
        • Protocols: HTTP, FTP, SMTP, DNS, SSH<br><br>
        
        <strong>3. Transport Layer</strong> (OSI 4)<br>
        • End-to-end communication<br>
        • Protocols: TCP, UDP<br><br>
        
        <strong>2. Internet Layer</strong> (OSI 3)<br>
        • Routing and logical addressing<br>
        • Protocols: IP, ICMP, ARP<br><br>
        
        <strong>1. Network Access Layer</strong> (OSI 1-2)<br>
        • Combines Physical and Data Link<br>
        • Protocols: Ethernet, WiFi, PPP
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Network Performance Metrics")
    
    st.markdown("""
    <div class="protocol-box">
        <strong>Key Metrics:</strong><br><br>
        
        <strong>Bandwidth:</strong><br>
        • Maximum data rate (bps, Mbps, Gbps)<br>
        • Theoretical capacity of link<br><br>
        
        <strong>Throughput:</strong><br>
        • Actual data rate achieved<br>
        • Always ≤ Bandwidth<br><br>
        
        <strong>Latency (Delay):</strong><br>
        • Time for packet to travel from source to destination<br>
        • Components: Propagation + Transmission + Processing + Queuing<br><br>
        
        <strong>Jitter:</strong><br>
        • Variation in latency<br>
        • Important for real-time applications (VoIP, video)<br><br>
        
        <strong>Packet Loss:</strong><br>
        • Percentage of packets lost<br>
        • Causes: Congestion, errors, buffer overflow
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: DATA LINK LAYER ====================
with tabs[2]:
    st.markdown("## 🔗 Data Link Layer")
    
    st.markdown("### 1️⃣ Ethernet")
    
    st.markdown("""
    <div class="network-box">
        <strong>Ethernet Frame Format:</strong><br><br>
        
        | Preamble | Dest MAC | Src MAC | Type | Data | FCS |<br>
        | 8 bytes  | 6 bytes  | 6 bytes | 2 B  | 46-1500 B | 4 B |<br><br>
        
        <strong>MAC Address:</strong><br>
        • 48-bit (6 bytes) hardware address<br>
        • Format: XX:XX:XX:XX:XX:XX (hexadecimal)<br>
        • First 3 bytes: OUI (Organizationally Unique Identifier)<br>
        • Last 3 bytes: Device-specific<br>
        • Example: 00:1A:2B:3C:4D:5E<br><br>
        
        <strong>Ethernet Standards:</strong><br>
        • 10BASE-T: 10 Mbps over twisted pair<br>
        • 100BASE-TX (Fast Ethernet): 100 Mbps<br>
        • 1000BASE-T (Gigabit Ethernet): 1 Gbps<br>
        • 10GBASE-T: 10 Gbps
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Switching")
    
    st.markdown("""
    <div class="protocol-box">
        <strong>Switch Operation:</strong><br><br>
        
        <strong>Learning:</strong><br>
        • Switch learns MAC addresses from source field<br>
        • Builds MAC address table (port → MAC mapping)<br><br>
        
        <strong>Forwarding:</strong><br>
        • Looks up destination MAC in table<br>
        • Forwards to specific port if known<br>
        • Floods to all ports if unknown (except source)<br><br>
        
        <strong>Filtering:</strong><br>
        • Drops frames destined for same port<br><br>
        
        <strong>Aging:</strong><br>
        • Removes old entries (typically 300 seconds)<br><br>
        
        <strong>Spanning Tree Protocol (STP):</strong><br>
        • Prevents loops in switched networks<br>
        • Creates loop-free topology<br>
        • Blocks redundant paths
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ VLANs")
    
    st.markdown("""
    <div class="network-box">
        <strong>Virtual LANs (VLANs):</strong><br><br>
        
        <strong>Purpose:</strong><br>
        • Logical segmentation of network<br>
        • Broadcast domain separation<br>
        • Security and performance<br><br>
        
        <strong>VLAN Tagging (802.1Q):</strong><br>
        • 4-byte tag inserted in Ethernet frame<br>
        • 12-bit VLAN ID (4096 VLANs)<br>
        • 3-bit priority field<br><br>
        
        <strong>Trunk Ports:</strong><br>
        • Carry traffic for multiple VLANs<br>
        • Tagged frames<br><br>
        
        <strong>Access Ports:</strong><br>
        • Belong to single VLAN<br>
        • Untagged frames
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: NETWORK LAYER ====================
with tabs[3]:
    st.markdown("## 🌍 Network Layer")
    
    st.markdown("### 1️⃣ IP Addressing")
    
    st.markdown("""
    <div class="theory-box">
        <strong>IPv4 Address:</strong><br>
        • 32-bit address (4 bytes)<br>
        • Dotted decimal notation: 192.168.1.1<br>
        • Network portion + Host portion<br><br>
        
        <strong>Address Classes (Classful):</strong><br>
        • Class A: 0.0.0.0 - 127.255.255.255 (8-bit network)<br>
        • Class B: 128.0.0.0 - 191.255.255.255 (16-bit network)<br>
        • Class C: 192.0.0.0 - 223.255.255.255 (24-bit network)<br>
        • Class D: 224.0.0.0 - 239.255.255.255 (Multicast)<br>
        • Class E: 240.0.0.0 - 255.255.255.255 (Reserved)<br><br>
        
        <strong>Private IP Ranges:</strong><br>
        • 10.0.0.0/8 (Class A)<br>
        • 172.16.0.0/12 (Class B)<br>
        • 192.168.0.0/16 (Class C)<br><br>
        
        <strong>Special Addresses:</strong><br>
        • 127.0.0.1: Loopback<br>
        • 0.0.0.0: Default route<br>
        • 255.255.255.255: Broadcast
    </div>
    """, unsafe_allow_html=True)
    
    # Subnet Calculator
    st.markdown("#### 🧮 Subnet Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        ip_input = st.text_input("IP Address", "192.168.1.100")
        cidr = st.slider("CIDR Prefix Length", 8, 30, 24)
    
    try:
        # Parse IP
        octets = [int(x) for x in ip_input.split('.')]
        if len(octets) != 4 or any(o < 0 or o > 255 for o in octets):
            raise ValueError
        
        # Calculate subnet mask
        mask_bits = '1' * cidr + '0' * (32 - cidr)
        mask_octets = [int(mask_bits[i:i+8], 2) for i in range(0, 32, 8)]
        subnet_mask = '.'.join(map(str, mask_octets))
        
        # Calculate network address
        network_octets = [octets[i] & mask_octets[i] for i in range(4)]
        network_addr = '.'.join(map(str, network_octets))
        
        # Calculate broadcast address
        wildcard_octets = [255 - mask_octets[i] for i in range(4)]
        broadcast_octets = [network_octets[i] | wildcard_octets[i] for i in range(4)]
        broadcast_addr = '.'.join(map(str, broadcast_octets))
        
        # Calculate usable hosts
        total_hosts = 2 ** (32 - cidr)
        usable_hosts = total_hosts - 2 if cidr < 31 else 0
        
        with col2:
            st.markdown(f"""
            **Results:**
            - Subnet Mask: {subnet_mask}
            - Network Address: {network_addr}
            - Broadcast Address: {broadcast_addr}
            - Total Hosts: {total_hosts}
            - Usable Hosts: {usable_hosts}
            - First Host: {network_addr[:-1]}{network_octets[3]+1}
            - Last Host: {broadcast_addr[:-1]}{broadcast_octets[3]-1}
            """)
        
    except:
        st.error("Invalid IP address format")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Routing Algorithms")
    
    st.markdown("""
    <div class="protocol-box">
        <strong>Distance Vector Routing:</strong><br>
        • Each router maintains distance table<br>
        • Periodic updates to neighbors<br>
        • Bellman-Ford algorithm<br>
        • Example: RIP (Routing Information Protocol)<br>
        • Problem: Count-to-infinity<br><br>
        
        <strong>Link State Routing:</strong><br>
        • Each router has complete topology<br>
        • Floods link state information<br>
        • Dijkstra's algorithm for shortest path<br>
        • Example: OSPF (Open Shortest Path First)<br>
        • Faster convergence than distance vector<br><br>
        
        <strong>Path Vector Routing:</strong><br>
        • Used for inter-domain routing<br>
        • Maintains path to destination<br>
        • Example: BGP (Border Gateway Protocol)<br>
        • Policy-based routing
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ IPv6")
    
    st.markdown("""
    <div class="network-box">
        <strong>IPv6 Features:</strong><br><br>
        
        <strong>Address:</strong><br>
        • 128-bit address (16 bytes)<br>
        • Hexadecimal notation: 2001:0db8:85a3:0000:0000:8a2e:0370:7334<br>
        • Shortened: 2001:db8:85a3::8a2e:370:7334<br><br>
        
        <strong>Advantages:</strong><br>
        • Larger address space (340 undecillion addresses)<br>
        • No NAT required<br>
        • Built-in IPsec<br>
        • Simplified header<br>
        • Auto-configuration (SLAAC)<br><br>
        
        <strong>Address Types:</strong><br>
        • Unicast: Single interface<br>
        • Multicast: Multiple interfaces<br>
        • Anycast: Nearest interface<br>
        • No broadcast (replaced by multicast)
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: TRANSPORT LAYER ====================
with tabs[4]:
    st.markdown("## 🚀 Transport Layer")
    
    st.markdown("### 1️⃣ TCP vs UDP")
    
    tcp_udp_comparison = {
        'Feature': ['Connection', 'Reliability', 'Ordering', 'Speed', 'Overhead', 'Flow Control', 'Use Cases'],
        'TCP': [
            'Connection-oriented',
            'Reliable (ACK, retransmission)',
            'In-order delivery',
            'Slower',
            'Higher (20+ bytes)',
            'Yes (sliding window)',
            'Web, Email, File transfer'
        ],
        'UDP': [
            'Connectionless',
            'Unreliable (best effort)',
            'No ordering guarantee',
            'Faster',
            'Lower (8 bytes)',
            'No',
            'Streaming, Gaming, DNS, VoIP'
        ]
    }
    
    df_tcp_udp = pd.DataFrame(tcp_udp_comparison)
    st.dataframe(df_tcp_udp, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ TCP Protocol")
    
    st.markdown("""
    <div class="theory-box">
        <strong>TCP Features:</strong><br><br>
        
        <strong>Three-Way Handshake:</strong><br>
        1. Client → Server: SYN<br>
        2. Server → Client: SYN-ACK<br>
        3. Client → Server: ACK<br><br>
        
        <strong>Four-Way Termination:</strong><br>
        1. Client → Server: FIN<br>
        2. Server → Client: ACK<br>
        3. Server → Client: FIN<br>
        4. Client → Server: ACK<br><br>
        
        <strong>Flow Control:</strong><br>
        • Sliding window protocol<br>
        • Receiver advertises window size<br>
        • Prevents sender from overwhelming receiver<br><br>
        
        <strong>Congestion Control:</strong><br>
        • Slow start<br>
        • Congestion avoidance<br>
        • Fast retransmit<br>
        • Fast recovery
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Port Numbers")
    
    st.markdown("""
    <div class="protocol-box">
        <strong>Port Ranges:</strong><br><br>
        
        <strong>Well-Known Ports (0-1023):</strong><br>
        • 20/21: FTP (File Transfer Protocol)<br>
        • 22: SSH (Secure Shell)<br>
        • 23: Telnet<br>
        • 25: SMTP (Email sending)<br>
        • 53: DNS (Domain Name System)<br>
        • 80: HTTP (Web)<br>
        • 110: POP3 (Email receiving)<br>
        • 143: IMAP (Email)<br>
        • 443: HTTPS (Secure Web)<br><br>
        
        <strong>Registered Ports (1024-49151):</strong><br>
        • 3306: MySQL<br>
        • 3389: RDP (Remote Desktop)<br>
        • 5432: PostgreSQL<br>
        • 8080: HTTP alternate<br><br>
        
        <strong>Dynamic/Private Ports (49152-65535):</strong><br>
        • Used for client-side connections
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: APPLICATION LAYER ====================
with tabs[5]:
    st.markdown("## 💻 Application Layer")
    
    st.markdown("### 1️⃣ HTTP/HTTPS")
    
    st.markdown("""
    <div class="network-box">
        <strong>HTTP Methods:</strong><br>
        • GET: Retrieve resource<br>
        • POST: Submit data<br>
        • PUT: Update resource<br>
        • DELETE: Remove resource<br>
        • HEAD: Get headers only<br>
        • PATCH: Partial update<br><br>
        
        <strong>HTTP Status Codes:</strong><br>
        • 1xx: Informational<br>
        • 2xx: Success (200 OK, 201 Created)<br>
        • 3xx: Redirection (301 Moved, 304 Not Modified)<br>
        • 4xx: Client Error (400 Bad Request, 404 Not Found)<br>
        • 5xx: Server Error (500 Internal Error, 503 Unavailable)<br><br>
        
        <strong>HTTPS:</strong><br>
        • HTTP over SSL/TLS<br>
        • Port 443<br>
        • Encryption and authentication<br>
        • Certificate-based trust
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ DNS")
    
    st.markdown("""
    <div class="protocol-box">
        <strong>Domain Name System:</strong><br><br>
        
        <strong>Hierarchy:</strong><br>
        • Root servers (.)<br>
        • Top-Level Domain (TLD): .com, .org, .edu<br>
        • Second-Level Domain: google.com<br>
        • Subdomain: www.google.com<br><br>
        
        <strong>Record Types:</strong><br>
        • A: IPv4 address<br>
        • AAAA: IPv6 address<br>
        • CNAME: Canonical name (alias)<br>
        • MX: Mail exchange<br>
        • NS: Name server<br>
        • TXT: Text records<br><br>
        
        <strong>Resolution Process:</strong><br>
        1. Check local cache<br>
        2. Query recursive resolver<br>
        3. Query root server<br>
        4. Query TLD server<br>
        5. Query authoritative server<br>
        6. Return IP address
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: SECURITY ====================
with tabs[6]:
    st.markdown("## 🔐 Network Security")
    
    st.markdown("### 1️⃣ Firewalls")
    
    st.markdown("""
    <div class="security-box">
        <strong>Firewall Types:</strong><br><br>
        
        <strong>Packet Filtering:</strong><br>
        • Inspects packet headers<br>
        • Rules based on IP, port, protocol<br>
        • Stateless (each packet independent)<br>
        • Fast but limited<br><br>
        
        <strong>Stateful Inspection:</strong><br>
        • Tracks connection state<br>
        • Allows return traffic<br>
        • More secure than packet filtering<br><br>
        
        <strong>Application Layer (Proxy):</strong><br>
        • Inspects application data<br>
        • Can filter based on content<br>
        • Slower but most secure<br><br>
        
        <strong>Next-Generation Firewall (NGFW):</strong><br>
        • Deep packet inspection<br>
        • Intrusion prevention<br>
        • Application awareness
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ VPN")
    
    st.markdown("""
    <div class="security-box">
        <strong>Virtual Private Network:</strong><br><br>
        
        <strong>Purpose:</strong><br>
        • Secure remote access<br>
        • Encrypt traffic over public network<br>
        • Create private tunnel<br><br>
        
        <strong>Types:</strong><br>
        • <strong>Site-to-Site:</strong> Connect networks<br>
        • <strong>Remote Access:</strong> Connect individual users<br><br>
        
        <strong>Protocols:</strong><br>
        • IPsec: Network layer VPN<br>
        • SSL/TLS: Application layer VPN<br>
        • OpenVPN: Open-source solution<br>
        • WireGuard: Modern, fast protocol<br><br>
        
        <strong>Benefits:</strong><br>
        • Confidentiality (encryption)<br>
        • Integrity (authentication)<br>
        • Access to private resources
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Common Attacks")
    
    st.markdown("""
    <div class="security-box">
        <strong>Network Attacks:</strong><br><br>
        
        <strong>DoS/DDoS:</strong><br>
        • Overwhelm target with traffic<br>
        • Distributed from multiple sources<br>
        • Mitigation: Rate limiting, filtering<br><br>
        
        <strong>Man-in-the-Middle (MITM):</strong><br>
        • Intercept communication<br>
        • Eavesdrop or modify data<br>
        • Prevention: Encryption, certificates<br><br>
        
        <strong>Packet Sniffing:</strong><br>
        • Capture network traffic<br>
        • Read unencrypted data<br>
        • Prevention: Encryption (HTTPS, VPN)<br><br>
        
        <strong>IP Spoofing:</strong><br>
        • Fake source IP address<br>
        • Used in DDoS attacks<br>
        • Prevention: Ingress/egress filtering<br><br>
        
        <strong>DNS Attacks:</strong><br>
        • DNS spoofing/poisoning<br>
        • Redirect to malicious sites<br>
        • Prevention: DNSSEC
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: NETWORK DESIGN ====================
with tabs[7]:
    st.markdown("## 🛠️ Network Design")
    
    st.markdown("### 1️⃣ Network Topologies")
    
    st.markdown("""
    <div class="network-box">
        <strong>Physical Topologies:</strong><br><br>
        
        <strong>Bus:</strong><br>
        • Single cable backbone<br>
        • All devices share medium<br>
        • Simple but single point of failure<br><br>
        
        <strong>Star:</strong><br>
        • Central hub/switch<br>
        • Easy to manage<br>
        • Hub is single point of failure<br><br>
        
        <strong>Ring:</strong><br>
        • Circular connection<br>
        • Token passing<br>
        • Break in ring affects all<br><br>
        
        <strong>Mesh:</strong><br>
        • Multiple redundant paths<br>
        • Highly reliable<br>
        • Expensive and complex<br><br>
        
        <strong>Hybrid:</strong><br>
        • Combination of topologies<br>
        • Most common in practice
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Network Design Principles")
    
    st.markdown("""
    <div class="protocol-box">
        <strong>Hierarchical Design:</strong><br><br>
        
        <strong>Core Layer:</strong><br>
        • High-speed backbone<br>
        • Minimal processing<br>
        • Redundant paths<br><br>
        
        <strong>Distribution Layer:</strong><br>
        • Routing between VLANs<br>
        • Policy enforcement<br>
        • Aggregation point<br><br>
        
        <strong>Access Layer:</strong><br>
        • End-user connectivity<br>
        • Port security<br>
        • VLAN assignment<br><br>
        
        <strong>Design Goals:</strong><br>
        • Scalability<br>
        • Redundancy<br>
        • Performance<br>
        • Security<br>
        • Manageability
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 9: PRACTICE PROBLEMS ====================
with tabs[8]:
    st.markdown("## 🎯 Practice Problems")
    
    problems = [
        {
            "title": "Problem 1: Subnetting",
            "question": "You have network 192.168.10.0/24. Divide it into 4 equal subnets. What are the subnet addresses and usable host ranges?",
            "hint": "Need 2 bits for 4 subnets (2² = 4). New prefix length = 24 + 2 = /26",
            "solution": """
**Solution:**

Original: 192.168.10.0/24
Need 4 subnets → 2 bits required → /26

Each subnet has 2^(32-26) = 64 addresses
Usable hosts per subnet = 64 - 2 = 62

**Subnet 1:**
- Network: 192.168.10.0/26
- First host: 192.168.10.1
- Last host: 192.168.10.62
- Broadcast: 192.168.10.63

**Subnet 2:**
- Network: 192.168.10.64/26
- First host: 192.168.10.65
- Last host: 192.168.10.126
- Broadcast: 192.168.10.127

**Subnet 3:**
- Network: 192.168.10.128/26
- First host: 192.168.10.129
- Last host: 192.168.10.190
- Broadcast: 192.168.10.191

**Subnet 4:**
- Network: 192.168.10.192/26
- First host: 192.168.10.193
- Last host: 192.168.10.254
- Broadcast: 192.168.10.255
            """
        },
        {
            "title": "Problem 2: TCP Throughput",
            "question": "Calculate maximum TCP throughput for: Window size = 64 KB, RTT = 100 ms. What happens if RTT increases to 200 ms?",
            "hint": "Throughput = Window Size / RTT",
            "solution": """
**Solution:**

**Formula:** Throughput = Window Size / RTT

**Case 1: RTT = 100 ms**
- Window = 64 KB = 65,536 bytes = 524,288 bits
- RTT = 100 ms = 0.1 seconds
- Throughput = 524,288 bits / 0.1 s = 5,242,880 bps
- **Throughput = 5.24 Mbps**

**Case 2: RTT = 200 ms**
- Window = 524,288 bits
- RTT = 200 ms = 0.2 seconds
- Throughput = 524,288 bits / 0.2 s = 2,621,440 bps
- **Throughput = 2.62 Mbps**

**Conclusion:**
- Doubling RTT halves throughput
- Higher latency significantly impacts TCP performance
- To maintain throughput with higher RTT, need larger window size
            """
        }
    ]
    
    for idx, problem in enumerate(problems, 1):
        with st.expander(f"📝 {problem['title']}", expanded=False):
            st.markdown(f"**Question:** {problem['question']}")
            
            if st.button(f"Show Hint", key=f"hint_{idx}"):
                st.info(f"💡 {problem['hint']}")
            
            if st.button(f"Show Solution", key=f"sol_{idx}"):
                st.markdown(problem['solution'])

# ==================== TAB 10: YOUTUBE RESOURCES ====================
with tabs[9]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning Computer Networks</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {
            "title": "Computer Networks",
            "channel": "Neso Academy",
            "url": "https://www.youtube.com/playlist?list=PLBlnK6fEyqRgMCUAG0XRw78UA8qnv6jEx",
            "description": "Complete networking course from basics",
            "duration": "Playlist (~100 videos)"
        },
        {
            "title": "Networking Fundamentals",
            "channel": "Professor Messer",
            "url": "https://www.youtube.com/playlist?list=PLG49S3nxzAnmpdmX7RoTOyuNJQAb-r-gd",
            "description": "Network+ certification training",
            "duration": "Full Course"
        },
        {
            "title": "Introduction to Computer Networking",
            "channel": "Stanford Online",
            "url": "https://www.youtube.com/playlist?list=PLvFG2xYBrYAQCyz4Wx3NPoYJOFjvU7g2Z",
            "description": "Stanford CS144 - Intro to Computer Networking",
            "duration": "Full Course"
        }
    ]
    
    for resource in beginner_resources:
        st.markdown(f"""
        **[{resource['title']}]({resource['url']})**  
        📺 Channel: {resource['channel']} | ⏱️ {resource['duration']}  
        {resource['description']}
        """)
        st.markdown("---")
    
    # Intermediate Level
    st.markdown("### 🟡 Intermediate Level")
    
    intermediate_resources = [
        {
            "title": "Computer Networking Course",
            "channel": "freeCodeCamp.org",
            "url": "https://www.youtube.com/watch?v=qiQR5rTSshw",
            "description": "Complete networking course (9 hours)",
            "duration": "~9 hours"
        },
        {
            "title": "CCNA Training",
            "channel": "NetworkChuck",
            "url": "https://www.youtube.com/playlist?list=PLIhvC56v63IKrRHh3gvZZBAGvsvOhwrRF",
            "description": "Cisco CCNA certification prep",
            "duration": "Playlist"
        },
        {
            "title": "TCP/IP Protocol Suite",
            "channel": "Eli the Computer Guy",
            "url": "https://www.youtube.com/playlist?list=PLF360ED1082F6F2A5",
            "description": "Deep dive into TCP/IP",
            "duration": "Playlist"
        }
    ]
    
    for resource in intermediate_resources:
        st.markdown(f"""
        **[{resource['title']}]({resource['url']})**  
        📺 Channel: {resource['channel']} | ⏱️ {resource['duration']}  
        {resource['description']}
        """)
        st.markdown("---")
    
    # Advanced Level
    st.markdown("### 🔴 Advanced Level")
    
    advanced_resources = [
        {
            "title": "Advanced Computer Networks",
            "channel": "MIT OpenCourseWare",
            "url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP62K2DjQLRxDNRi0z2IRWnNh",
            "description": "MIT 6.829 - Advanced networking topics",
            "duration": "Full Course"
        },
        {
            "title": "Software-Defined Networking",
            "channel": "Princeton University",
            "url": "https://www.youtube.com/playlist?list=PLpherdrLyny-4Y6jXKvi0Ia_c2tSRdwgM",
            "description": "SDN and network virtualization",
            "duration": "Full Course"
        },
        {
            "title": "Network Security",
            "channel": "Christof Paar",
            "url": "https://www.youtube.com/channel/UC1usFRN4LCMcfIV7UjHNuQg",
            "description": "Cryptography and network security",
            "duration": "Channel"
        }
    ]
    
    for resource in advanced_resources:
        st.markdown(f"""
        **[{resource['title']}]({resource['url']})**  
        📺 Channel: {resource['channel']} | ⏱️ {resource['duration']}  
        {resource['description']}
        """)
        st.markdown("---")
    
    # Practical/Hands-on
    st.markdown("### 🛠️ Practical & Hands-on")
    
    practical_resources = [
        {
            "title": "Packet Tracer Labs",
            "channel": "David Bombal",
            "url": "https://www.youtube.com/c/DavidBombal",
            "description": "Cisco Packet Tracer tutorials",
            "duration": "Channel"
        },
        {
            "title": "Wireshark Tutorial",
            "channel": "HackerSploit",
            "url": "https://www.youtube.com/playlist?list=PLBf0hzazHTGPgyxeEj_9LBHiqjtNEjsqt",
            "description": "Network packet analysis",
            "duration": "Playlist"
        },
        {
            "title": "Home Lab Setup",
            "channel": "Techno Tim",
            "url": "https://www.youtube.com/c/TechnoTimLive",
            "description": "Build your own network lab",
            "duration": "Channel"
        }
    ]
    
    for resource in practical_resources:
        st.markdown(f"""
        **[{resource['title']}]({resource['url']})**  
        📺 Channel: {resource['channel']} | ⏱️ {resource['duration']}  
        {resource['description']}
        """)
        st.markdown("---")
    
    # Study Tips
    st.markdown("### 💡 Study Tips")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Recommended Learning Path:</strong><br>
        1. Understand OSI and TCP/IP models<br>
        2. Learn IP addressing and subnetting<br>
        3. Study routing and switching<br>
        4. Explore transport layer protocols (TCP/UDP)<br>
        5. Learn application layer protocols (HTTP, DNS)<br>
        6. Understand network security<br>
        7. Practice with simulation tools<br>
        8. Build home lab for hands-on experience<br><br>
        
        <strong>Tools & Simulators:</strong><br>
        • <strong>Cisco Packet Tracer:</strong> Free network simulator<br>
        • <strong>GNS3:</strong> Advanced network emulator<br>
        • <strong>Wireshark:</strong> Packet analyzer<br>
        • <strong>nmap:</strong> Network scanner<br>
        • <strong>iperf:</strong> Network performance testing<br><br>
        
        <strong>Certifications:</strong><br>
        • CompTIA Network+<br>
        • Cisco CCNA<br>
        • Cisco CCNP<br>
        • Juniper JNCIA
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE301 - Computer Networks</strong><br>
    <small>UTel University | Department of Computer Engineering</small>
</div>
""", unsafe_allow_html=True)
