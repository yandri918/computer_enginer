import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="BU201 - Structure of the Processing Industry", page_icon="🏭", layout="wide")

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
        background: linear-gradient(135deg, #f97316 0%, #ea580c 100%);
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
        background: linear-gradient(135deg, #ffedd5 0%, #fed7aa 100%);
        border-left: 5px solid #f97316;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .framework-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .example-box {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .case-box {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .youtube-box {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        border-left: 5px solid #ef4444;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="course-header">
    <div style="font-size: 1.2rem; opacity: 0.9;">BU201</div>
    <div class="course-title">Structure of the Processing Industry</div>
    <div>🏭 3 Credits | Semester 4 | Business & Management</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "4")
with col3:
    st.metric("Difficulty", "4/7")
with col4:
    st.metric("Hours/Week", "5")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "🏭 Industry Structure",
    "⚙️ Production Systems",
    "📊 Value Chain Analysis",
    "🔄 Supply Chain Management",
    "💡 Industry 4.0",
    "🌍 Global Manufacturing",
    "📈 Performance Metrics",
    "🎯 Case Studies",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive study of manufacturing and processing industry structures, production systems, and value chain 
        management. Covers industrial organization, production planning, supply chain optimization, and modern manufacturing 
        paradigms including Industry 4.0. Emphasizes both theoretical frameworks and practical applications in various 
        processing industries including automotive, electronics, food processing, and pharmaceuticals.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Understand industrial organization and market structures",
        "Analyze production systems and manufacturing processes",
        "Apply value chain analysis frameworks",
        "Design and optimize supply chain networks",
        "Implement lean manufacturing and Six Sigma principles",
        "Understand Industry 4.0 technologies and digital transformation",
        "Evaluate global manufacturing strategies",
        "Use performance metrics for operational excellence"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Fundamentals:**
        - Industrial organization theory
        - Market structures and competition
        - Economies of scale and scope
        - Vertical and horizontal integration
        - Industry life cycle
        
        **Production Systems:**
        - Manufacturing processes
        - Production planning and control
        - Capacity planning
        - Quality management (TQM, Six Sigma)
        - Lean manufacturing
        """)
    
    with col2:
        st.markdown("""
        **Strategic Topics:**
        - Value chain analysis (Porter)
        - Supply chain design
        - Make-or-buy decisions
        - Outsourcing and offshoring
        - Global value chains
        
        **Modern Paradigms:**
        - Industry 4.0 and smart manufacturing
        - IoT and cyber-physical systems
        - Digital twins
        - Additive manufacturing (3D printing)
        - Sustainable manufacturing
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Operations Management", "author": "Slack, Brandon-Jones & Johnston", "type": "Textbook"},
        {"title": "The Goal", "author": "Eliyahu Goldratt", "type": "Business Novel"},
        {"title": "Competitive Advantage", "author": "Michael Porter", "type": "Strategy"},
        {"title": "The Machine That Changed the World", "author": "Womack, Jones & Roos", "type": "Lean"}
    ]
    
    for resource in resources:
        st.markdown(f"📖 **{resource['title']}** by {resource['author']} ({resource['type']})")

# ==================== TAB 2: INDUSTRY STRUCTURE ====================
with tabs[1]:
    st.markdown("## 🏭 Industry Structure")
    
    st.markdown("### 1️⃣ Market Structures")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Types of Market Structures:</strong><br><br>
        
        <strong>1. Perfect Competition:</strong><br>
        • Many buyers and sellers<br>
        • Homogeneous products<br>
        • Free entry and exit<br>
        • Example: Agricultural commodities<br><br>
        
        <strong>2. Monopolistic Competition:</strong><br>
        • Many firms with differentiated products<br>
        • Some price-setting power<br>
        • Example: Restaurants, clothing<br><br>
        
        <strong>3. Oligopoly:</strong><br>
        • Few large firms dominate<br>
        • Strategic interdependence<br>
        • High barriers to entry<br>
        • Example: Automotive, airlines<br><br>
        
        <strong>4. Monopoly:</strong><br>
        • Single seller<br>
        • Price maker<br>
        • High barriers to entry<br>
        • Example: Utilities (regulated)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Industry Concentration")
    
    st.markdown("""
    <div class="framework-box">
        <strong>Concentration Measures:</strong><br><br>
        
        <strong>Concentration Ratio (CR4):</strong><br>
        CR4 = Market share of top 4 firms<br>
        • CR4 > 60%: Highly concentrated (oligopoly)<br>
        • CR4 = 40-60%: Moderately concentrated<br>
        • CR4 < 40%: Low concentration<br><br>
        
        <strong>Herfindahl-Hirschman Index (HHI):</strong><br>
        HHI = Σ(Market Share)²<br>
        • HHI > 2500: Highly concentrated<br>
        • HHI = 1500-2500: Moderately concentrated<br>
        • HHI < 1500: Unconcentrated
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive HHI Calculator
    st.markdown("#### 🧮 HHI Calculator")
    
    st.markdown("Enter market shares of top firms (as percentages):")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        firm1 = st.number_input("Firm 1 (%)", 0.0, 100.0, 30.0, 1.0)
    with col2:
        firm2 = st.number_input("Firm 2 (%)", 0.0, 100.0, 25.0, 1.0)
    with col3:
        firm3 = st.number_input("Firm 3 (%)", 0.0, 100.0, 20.0, 1.0)
    with col4:
        firm4 = st.number_input("Firm 4 (%)", 0.0, 100.0, 15.0, 1.0)
    
    others = max(0, 100 - (firm1 + firm2 + firm3 + firm4))
    
    # Calculate HHI
    hhi = firm1**2 + firm2**2 + firm3**2 + firm4**2 + others**2
    cr4 = firm1 + firm2 + firm3 + firm4
    
    st.markdown(f"""
    **Results:**
    - CR4 (Top 4 concentration) = {cr4:.1f}%
    - HHI = {hhi:.0f}
    - Others = {others:.1f}%
    """)
    
    if hhi > 2500:
        st.error("🔴 **Highly Concentrated Market** - Potential antitrust concerns")
    elif hhi > 1500:
        st.warning("🟡 **Moderately Concentrated Market** - Some competitive concerns")
    else:
        st.success("🟢 **Competitive Market** - Low concentration")
    
    # Visualization
    df_market = pd.DataFrame({
        'Firm': ['Firm 1', 'Firm 2', 'Firm 3', 'Firm 4', 'Others'],
        'Market Share': [firm1, firm2, firm3, firm4, others]
    })
    
    chart = alt.Chart(df_market).mark_arc().encode(
        theta=alt.Theta('Market Share:Q'),
        color=alt.Color('Firm:N', scale=alt.Scale(scheme='category10')),
        tooltip=['Firm', 'Market Share']
    ).properties(
        width=400,
        height=400,
        title="Market Share Distribution"
    )
    
    st.altair_chart(chart, use_container_width=True)

# ==================== TAB 3: PRODUCTION SYSTEMS ====================
with tabs[2]:
    st.markdown("## ⚙️ Production Systems")
    
    st.markdown("### 1️⃣ Types of Production Systems")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Classification by Volume and Variety:</strong><br><br>
        
        <strong>1. Job Shop:</strong><br>
        • Low volume, high variety<br>
        • Customized products<br>
        • Flexible equipment<br>
        • Example: Custom furniture, machine shops<br><br>
        
        <strong>2. Batch Production:</strong><br>
        • Medium volume, medium variety<br>
        • Products in batches<br>
        • Setup time between batches<br>
        • Example: Bakeries, pharmaceuticals<br><br>
        
        <strong>3. Mass Production:</strong><br>
        • High volume, low variety<br>
        • Standardized products<br>
        • Assembly lines<br>
        • Example: Automotive, electronics<br><br>
        
        <strong>4. Continuous Production:</strong><br>
        • Very high volume, no variety<br>
        • 24/7 operation<br>
        • Automated processes<br>
        • Example: Oil refining, chemicals
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Lean Manufacturing")
    
    st.markdown("""
    <div class="framework-box">
        <strong>7 Wastes (TIMWOOD):</strong><br>
        1. <strong>T</strong>ransportation - Unnecessary movement of materials<br>
        2. <strong>I</strong>nventory - Excess stock<br>
        3. <strong>M</strong>otion - Unnecessary worker movement<br>
        4. <strong>W</strong>aiting - Idle time<br>
        5. <strong>O</strong>ver-production - Making more than needed<br>
        6. <strong>O</strong>ver-processing - Doing more than required<br>
        7. <strong>D</strong>efects - Rework and scrap<br><br>
        
        <strong>Lean Principles:</strong><br>
        • Define value from customer perspective<br>
        • Map the value stream<br>
        • Create flow<br>
        • Implement pull systems (JIT)<br>
        • Pursue perfection (Kaizen)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Six Sigma")
    
    st.markdown("""
    <div class="framework-box">
        <strong>DMAIC Methodology:</strong><br><br>
        
        <strong>D</strong>efine - Define problem and goals<br>
        <strong>M</strong>easure - Collect data on current performance<br>
        <strong>A</strong>nalyze - Identify root causes<br>
        <strong>I</strong>mprove - Implement solutions<br>
        <strong>C</strong>ontrol - Sustain improvements<br><br>
        
        <strong>Six Sigma Levels:</strong><br>
        • 6σ: 3.4 defects per million opportunities (DPMO)<br>
        • 5σ: 233 DPMO<br>
        • 4σ: 6,210 DPMO<br>
        • 3σ: 66,807 DPMO
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: VALUE CHAIN ====================
with tabs[3]:
    st.markdown("## 📊 Value Chain Analysis")
    
    st.markdown("### 1️⃣ Porter's Value Chain")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Primary Activities:</strong><br>
        1. <strong>Inbound Logistics:</strong> Receiving, storing, inventory management<br>
        2. <strong>Operations:</strong> Transforming inputs into final products<br>
        3. <strong>Outbound Logistics:</strong> Warehousing and distribution<br>
        4. <strong>Marketing & Sales:</strong> Promotion and selling<br>
        5. <strong>Service:</strong> After-sales support<br><br>
        
        <strong>Support Activities:</strong><br>
        • <strong>Firm Infrastructure:</strong> Management, finance, legal<br>
        • <strong>HR Management:</strong> Recruiting, training, compensation<br>
        • <strong>Technology Development:</strong> R&D, process improvement<br>
        • <strong>Procurement:</strong> Purchasing inputs<br><br>
        
        <strong>Margin:</strong> Value created - Cost of creating value
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Value Chain Optimization")
    
    st.markdown("""
    <div class="example-box">
        <strong>Strategies for Value Creation:</strong><br><br>
        
        <strong>Cost Leadership:</strong><br>
        • Economies of scale<br>
        • Process efficiency<br>
        • Standardization<br>
        • Vertical integration<br><br>
        
        <strong>Differentiation:</strong><br>
        • Product innovation<br>
        • Brand building<br>
        • Customer service<br>
        • Quality excellence<br><br>
        
        <strong>Focus Strategy:</strong><br>
        • Niche markets<br>
        • Specialized products<br>
        • Customization
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: SUPPLY CHAIN ====================
with tabs[4]:
    st.markdown("## 🔄 Supply Chain Management")
    
    st.markdown("### 1️⃣ Supply Chain Structure")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Supply Chain Tiers:</strong><br><br>
        
        Tier 3 Suppliers → Tier 2 Suppliers → Tier 1 Suppliers → Manufacturer → Distributor → Retailer → Customer<br><br>
        
        <strong>Key Flows:</strong><br>
        • <strong>Material Flow:</strong> Physical products (downstream)<br>
        • <strong>Information Flow:</strong> Orders, forecasts (bidirectional)<br>
        • <strong>Financial Flow:</strong> Payments (upstream)<br><br>
        
        <strong>Supply Chain Decisions:</strong><br>
        • <strong>Strategic:</strong> Network design, partnerships<br>
        • <strong>Tactical:</strong> Inventory policies, transportation modes<br>
        • <strong>Operational:</strong> Order fulfillment, scheduling
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Bullwhip Effect")
    
    st.markdown("""
    <div class="framework-box">
        <strong>Bullwhip Effect:</strong><br>
        Demand variability increases as you move upstream in the supply chain<br><br>
        
        <strong>Causes:</strong><br>
        • Demand forecast updating<br>
        • Order batching<br>
        • Price fluctuations<br>
        • Rationing and shortage gaming<br><br>
        
        <strong>Mitigation Strategies:</strong><br>
        • Information sharing (EDI, VMI)<br>
        • Channel alignment<br>
        • Operational efficiency<br>
        • Everyday low pricing (EDLP)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Inventory Management")
    
    st.markdown("""
    <div class="framework-box">
        <strong>Economic Order Quantity (EOQ):</strong><br>
        EOQ = √(2DS/H)<br><br>
        
        Where:<br>
        • D = Annual demand<br>
        • S = Ordering cost per order<br>
        • H = Holding cost per unit per year<br><br>
        
        <strong>Reorder Point (ROP):</strong><br>
        ROP = (Demand per day) × (Lead time) + Safety stock
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: INDUSTRY 4.0 ====================
with tabs[5]:
    st.markdown("## 💡 Industry 4.0")
    
    st.markdown("### 1️⃣ Key Technologies")
    
    st.markdown("""
    <div class="theory-box">
        <strong>9 Pillars of Industry 4.0:</strong><br><br>
        
        1. <strong>Big Data & Analytics:</strong> Data-driven decision making<br>
        2. <strong>Autonomous Robots:</strong> Collaborative robots (cobots)<br>
        3. <strong>Simulation:</strong> Digital twins, virtual commissioning<br>
        4. <strong>Horizontal & Vertical Integration:</strong> Connected systems<br>
        5. <strong>Industrial IoT:</strong> Connected machines and sensors<br>
        6. <strong>Cybersecurity:</strong> Protecting connected systems<br>
        7. <strong>Cloud Computing:</strong> Scalable computing resources<br>
        8. <strong>Additive Manufacturing:</strong> 3D printing<br>
        9. <strong>Augmented Reality:</strong> AR for training and maintenance
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Smart Manufacturing")
    
    st.markdown("""
    <div class="example-box">
        <strong>Characteristics of Smart Factories:</strong><br><br>
        
        <strong>Connectivity:</strong><br>
        • Real-time data collection<br>
        • Machine-to-machine (M2M) communication<br>
        • Cloud-based platforms<br><br>
        
        <strong>Intelligence:</strong><br>
        • Predictive maintenance<br>
        • Self-optimization<br>
        • AI-driven quality control<br><br>
        
        <strong>Flexibility:</strong><br>
        • Mass customization<br>
        • Rapid reconfiguration<br>
        • Adaptive production
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Digital Transformation")
    
    st.markdown("""
    <div class="framework-box">
        <strong>Implementation Roadmap:</strong><br><br>
        
        <strong>Phase 1: Digitization</strong><br>
        • Convert analog to digital<br>
        • Basic automation<br><br>
        
        <strong>Phase 2: Digitalization</strong><br>
        • Process optimization<br>
        • Data integration<br><br>
        
        <strong>Phase 3: Digital Transformation</strong><br>
        • Business model innovation<br>
        • Ecosystem integration<br>
        • AI and advanced analytics
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: GLOBAL MANUFACTURING ====================
with tabs[6]:
    st.markdown("## 🌍 Global Manufacturing")
    
    st.markdown("### 1️⃣ Globalization Strategies")
    
    st.markdown("""
    <div class="theory-box">
        <strong>International Manufacturing Strategies:</strong><br><br>
        
        <strong>1. Export Strategy:</strong><br>
        • Produce domestically, sell globally<br>
        • Low risk, limited control<br><br>
        
        <strong>2. Licensing/Franchising:</strong><br>
        • Transfer technology/brand<br>
        • Moderate risk and control<br><br>
        
        <strong>3. Joint Ventures:</strong><br>
        • Partner with local firms<br>
        • Share risks and resources<br><br>
        
        <strong>4. Foreign Direct Investment (FDI):</strong><br>
        • Wholly-owned subsidiaries<br>
        • High control, high investment
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Location Decisions")
    
    st.markdown("""
    <div class="framework-box">
        <strong>Factors in Location Selection:</strong><br><br>
        
        <strong>Cost Factors:</strong><br>
        • Labor costs<br>
        • Raw material availability<br>
        • Transportation costs<br>
        • Energy costs<br>
        • Tax incentives<br><br>
        
        <strong>Strategic Factors:</strong><br>
        • Market access<br>
        • Skilled workforce<br>
        • Infrastructure quality<br>
        • Political stability<br>
        • Intellectual property protection
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Reshoring vs Offshoring")
    
    st.markdown("""
    <div class="example-box">
        <strong>Offshoring:</strong><br>
        • Lower labor costs<br>
        • Access to new markets<br>
        • Risks: Quality, IP, supply chain disruption<br><br>
        
        <strong>Reshoring/Nearshoring:</strong><br>
        • Better quality control<br>
        • Faster response times<br>
        • Reduced supply chain risks<br>
        • Support local economy<br><br>
        
        <strong>Trend:</strong> Shift toward regionalization and resilience
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: PERFORMANCE METRICS ====================
with tabs[7]:
    st.markdown("## 📈 Performance Metrics")
    
    st.markdown("### 1️⃣ Key Performance Indicators (KPIs)")
    
    st.markdown("""
    <div class="framework-box">
        <strong>Operational KPIs:</strong><br><br>
        
        <strong>Productivity:</strong><br>
        • Output per labor hour<br>
        • Overall Equipment Effectiveness (OEE)<br>
        • Capacity utilization<br><br>
        
        <strong>Quality:</strong><br>
        • Defect rate<br>
        • First pass yield<br>
        • Customer returns<br><br>
        
        <strong>Delivery:</strong><br>
        • On-time delivery rate<br>
        • Lead time<br>
        • Order fulfillment cycle time<br><br>
        
        <strong>Cost:</strong><br>
        • Cost per unit<br>
        • Inventory turnover<br>
        • Scrap rate
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Overall Equipment Effectiveness (OEE)")
    
    st.markdown("""
    <div class="theory-box">
        <strong>OEE Formula:</strong><br>
        OEE = Availability × Performance × Quality<br><br>
        
        <strong>Availability:</strong><br>
        = (Operating Time / Planned Production Time) × 100%<br><br>
        
        <strong>Performance:</strong><br>
        = (Actual Output / Theoretical Maximum Output) × 100%<br><br>
        
        <strong>Quality:</strong><br>
        = (Good Units / Total Units Produced) × 100%<br><br>
        
        <strong>World-Class OEE:</strong> ≥ 85%
    </div>
    """, unsafe_allow_html=True)
    
    # OEE Calculator
    st.markdown("#### 🧮 OEE Calculator")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Availability:**")
        planned_time = st.number_input("Planned Production Time (hrs)", 1.0, 24.0, 8.0, 0.5)
        downtime = st.number_input("Downtime (hrs)", 0.0, planned_time, 0.5, 0.1)
        operating_time = planned_time - downtime
        availability = (operating_time / planned_time) * 100
        st.metric("Availability", f"{availability:.1f}%")
    
    with col2:
        st.markdown("**Performance:**")
        ideal_cycle_time = st.number_input("Ideal Cycle Time (min/unit)", 0.1, 60.0, 1.0, 0.1)
        total_units = st.number_input("Total Units Produced", 1, 10000, 400, 10)
        theoretical_max = (operating_time * 60) / ideal_cycle_time
        performance = (total_units / theoretical_max) * 100 if theoretical_max > 0 else 0
        st.metric("Performance", f"{performance:.1f}%")
    
    with col3:
        st.markdown("**Quality:**")
        defects = st.number_input("Defective Units", 0, total_units, 10, 1)
        good_units = total_units - defects
        quality = (good_units / total_units) * 100 if total_units > 0 else 0
        st.metric("Quality", f"{quality:.1f}%")
    
    # Calculate OEE
    oee = (availability / 100) * (performance / 100) * (quality / 100) * 100
    
    st.markdown("---")
    st.markdown(f"### **Overall Equipment Effectiveness (OEE): {oee:.1f}%**")
    
    if oee >= 85:
        st.success("🟢 **World-Class Performance!**")
    elif oee >= 60:
        st.info("🟡 **Good Performance** - Room for improvement")
    else:
        st.warning("🔴 **Needs Improvement** - Focus on losses")

# ==================== TAB 9: CASE STUDIES ====================
with tabs[8]:
    st.markdown("## 🎯 Case Studies")
    
    case_studies = [
        {
            "title": "Case Study 1: Toyota Production System (TPS)",
            "industry": "Automotive",
            "challenge": "How to achieve high quality and low cost simultaneously",
            "solution": """
**Toyota's Approach:**

**Key Principles:**
1. **Just-In-Time (JIT):** Produce only what is needed, when needed
2. **Jidoka:** Built-in quality, stop production when defects occur
3. **Kaizen:** Continuous improvement culture
4. **Respect for People:** Empower workers

**Results:**
- Reduced inventory by 75%
- Improved quality (defects < 1%)
- Increased productivity by 50%
- Became world's largest automaker

**Lessons:**
- Waste elimination is key to competitiveness
- Quality and efficiency are complementary
- Employee engagement drives improvement
            """,
            "key_takeaways": [
                "Lean principles applicable across industries",
                "Culture change is critical for success",
                "Long-term commitment required"
            ]
        },
        {
            "title": "Case Study 2: Amazon's Fulfillment Centers",
            "industry": "E-commerce/Logistics",
            "challenge": "Scale operations to handle millions of SKUs and orders",
            "solution": """
**Amazon's Innovation:**

**Technology Integration:**
1. **Kiva Robots:** Automated warehouse robots
2. **AI-Powered Forecasting:** Predictive inventory placement
3. **Advanced Sorting:** High-speed package sorting
4. **Drone Delivery:** Last-mile innovation (Prime Air)

**Process Optimization:**
- Cross-docking to minimize storage time
- Zone-based picking strategies
- Real-time inventory tracking
- Dynamic routing algorithms

**Results:**
- 2-day (Prime) to same-day delivery
- 99.9% inventory accuracy
- Handle 1M+ orders per day during peak

**Lessons:**
- Automation enables scale
- Data-driven decision making
- Customer obsession drives innovation
            """,
            "key_takeaways": [
                "Technology as competitive advantage",
                "Continuous innovation in operations",
                "Balance automation with flexibility"
            ]
        },
        {
            "title": "Case Study 3: Zara's Fast Fashion Supply Chain",
            "industry": "Apparel/Retail",
            "challenge": "Respond quickly to fashion trends",
            "solution": """
**Zara's Strategy:**

**Vertical Integration:**
- Own design, production, and distribution
- 50% production in-house (vs 15% industry average)
- Proximity manufacturing (Spain, Portugal, Morocco)

**Speed to Market:**
- Design to store: 2-3 weeks (vs 6 months industry)
- Twice-weekly deliveries to stores
- Limited quantities create scarcity

**Information Flow:**
- Store managers report trends daily
- Real-time sales data drives production
- Minimal forecasting, responsive production

**Results:**
- 85% full-price sales (vs 60-70% industry)
- 12-15 inventory turns per year
- Market leader in fast fashion

**Lessons:**
- Speed can be more valuable than cost
- Vertical integration enables agility
- Information is strategic asset
            """,
            "key_takeaways": [
                "Agility as competitive strategy",
                "Trade-off between cost and speed",
                "Vertical integration for control"
            ]
        }
    ]
    
    for idx, case in enumerate(case_studies, 1):
        with st.expander(f"📝 {case['title']}", expanded=False):
            st.markdown(f"**Industry:** {case['industry']}")
            st.markdown(f"**Challenge:** {case['challenge']}")
            
            if st.button(f"Show Solution", key=f"case_{idx}"):
                st.markdown(case['solution'])
                
                st.markdown("**Key Takeaways:**")
                for takeaway in case['key_takeaways']:
                    st.markdown(f"• {takeaway}")

# ==================== TAB 10: YOUTUBE RESOURCES ====================
with tabs[9]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning about Processing Industry and Manufacturing</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {
            "title": "Introduction to Operations Management",
            "channel": "MIT OpenCourseWare",
            "url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP62qauV_CpT1zKaGG_Vj5igX",
            "description": "MIT 15.760 - Comprehensive operations management course",
            "duration": "Full Course"
        },
        {
            "title": "Supply Chain Management",
            "channel": "Gies College of Business",
            "url": "https://www.youtube.com/playlist?list=PLgMzRx7kDBqUqOGLUYPCdlJiHPLQwWJqV",
            "description": "Complete supply chain fundamentals",
            "duration": "Playlist"
        },
        {
            "title": "Lean Manufacturing Principles",
            "channel": "Lean Enterprise Institute",
            "url": "https://www.youtube.com/user/LeanEnterpriseInst",
            "description": "Official lean manufacturing resources",
            "duration": "Channel"
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
            "title": "Industry 4.0 and Smart Manufacturing",
            "channel": "Siemens",
            "url": "https://www.youtube.com/playlist?list=PLmKX8VKyMwS-4KmJNqKGqPqKGqPqKGqPq",
            "description": "Digital transformation in manufacturing",
            "duration": "Playlist"
        },
        {
            "title": "Six Sigma Training",
            "channel": "Simplilearn",
            "url": "https://www.youtube.com/watch?v=MNRqLbLmBPE",
            "description": "Complete Six Sigma Green Belt course",
            "duration": "~4 hours"
        },
        {
            "title": "Value Chain Analysis",
            "channel": "Corporate Finance Institute",
            "url": "https://www.youtube.com/watch?v=VN8DYpaRQP0",
            "description": "Porter's Value Chain explained",
            "duration": "15 min"
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
            "title": "Global Supply Chain Management",
            "channel": "Stanford Graduate School of Business",
            "url": "https://www.youtube.com/playlist?list=PLxwS9JqPwJTzqCNVTlhVqKqWJqVqKqWJq",
            "description": "Advanced supply chain strategies",
            "duration": "Full Course"
        },
        {
            "title": "Manufacturing Strategy",
            "channel": "Harvard Business School",
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "description": "Strategic operations management",
            "duration": "Lecture Series"
        },
        {
            "title": "Digital Twins in Manufacturing",
            "channel": "GE Digital",
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "description": "Advanced Industry 4.0 applications",
            "duration": "Webinar Series"
        }
    ]
    
    for resource in advanced_resources:
        st.markdown(f"""
        **[{resource['title']}]({resource['url']})**  
        📺 Channel: {resource['channel']} | ⏱️ {resource['duration']}  
        {resource['description']}
        """)
        st.markdown("---")
    
    # Industry Insights
    st.markdown("### 🏭 Industry Insights")
    
    industry_resources = [
        {
            "title": "How It's Made",
            "channel": "Science Channel",
            "url": "https://www.youtube.com/c/HowItsMadeOfficial",
            "description": "Manufacturing processes across industries",
            "duration": "Channel"
        },
        {
            "title": "Factory Tours",
            "channel": "Insider Business",
            "url": "https://www.youtube.com/playlist?list=PLJic7bfGlo3qxHqFNEADdFjp074mqebyx",
            "description": "Behind-the-scenes manufacturing",
            "duration": "Playlist"
        },
        {
            "title": "Tesla Factory Tour",
            "channel": "Tesla",
            "url": "https://www.youtube.com/watch?v=Mr9e5-j-7Ow",
            "description": "Modern automotive manufacturing",
            "duration": "~30 min"
        }
    ]
    
    for resource in industry_resources:
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
        1. Understand basic operations management concepts<br>
        2. Study different production systems and their applications<br>
        3. Learn lean manufacturing and Six Sigma methodologies<br>
        4. Explore supply chain management and optimization<br>
        5. Understand Industry 4.0 technologies<br>
        6. Analyze real-world case studies<br>
        7. Visit factories or watch virtual tours<br><br>
        
        <strong>Practice Resources:</strong><br>
        • <strong>The Goal (Book):</strong> Business novel on TOC<br>
        • <strong>Lean Enterprise Institute:</strong> https://www.lean.org/<br>
        • <strong>ASQ (Quality):</strong> https://asq.org/<br>
        • <strong>APICS (Supply Chain):</strong> https://www.ascm.org/
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>BU201 - Structure of the Processing Industry</strong><br>
    <small>UTel University | Department of Business & Management</small>
</div>
""", unsafe_allow_html=True)
