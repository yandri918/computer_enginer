import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="SD101 - Sustainable Development", page_icon="🌱", layout="wide")

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
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
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
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .environment-box {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .tech-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .sdg-box {
        background: linear-gradient(135deg, #ede9fe 0%, #ddd6fe 100%);
        border-left: 5px solid #8b5cf6;
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
    <div style="font-size: 1.2rem; opacity: 0.9;">SD101</div>
    <div class="course-title">Sustainable Development</div>
    <div>🌱 2 Credits | Semester 6 | Sustainability & Ethics</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "2")
with col2:
    st.metric("Semester", "6")
with col3:
    st.metric("Difficulty", "2/7")
with col4:
    st.metric("Hours/Week", "3")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "🌍 UN SDGs",
    "♻️ Circular Economy",
    "⚡ Renewable Energy",
    "💻 Green Technology",
    "🏢 Corporate Sustainability",
    "🎯 Case Studies",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Introduction to sustainable development principles, environmental impact assessment, and responsible technology 
        development. Covers UN Sustainable Development Goals (SDGs), circular economy, renewable energy, green technology, 
        carbon footprint, e-waste management, and corporate social responsibility. Emphasizes ethical considerations in 
        technology, environmental stewardship, and sustainable business practices. Students will learn to design sustainable 
        systems and assess environmental impact of technology projects.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Understand UN Sustainable Development Goals (SDGs)",
        "Assess environmental impact of technology projects",
        "Apply circular economy principles to product design",
        "Evaluate renewable energy technologies",
        "Design sustainable and energy-efficient systems",
        "Implement e-waste management strategies",
        "Apply ethical principles to technology development",
        "Measure and reduce carbon footprint"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Sustainability Principles:**
        - Triple bottom line (People, Planet, Profit)
        - UN Sustainable Development Goals
        - Environmental impact assessment
        - Life cycle analysis
        - Carbon footprint calculation
        
        **Green Technology:**
        - Energy-efficient computing
        - Green data centers
        - Renewable energy systems
        - Smart grids and IoT
        - Sustainable software design
        """)
    
    with col2:
        st.markdown("""
        **Circular Economy:**
        - Reduce, Reuse, Recycle
        - Product lifecycle management
        - E-waste management
        - Sustainable supply chains
        - Cradle-to-cradle design
        
        **Corporate Responsibility:**
        - ESG (Environmental, Social, Governance)
        - Corporate sustainability reporting
        - Green certifications (LEED, Energy Star)
        - Stakeholder engagement
        - Sustainable innovation
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Cradle to Cradle", "author": "William McDonough", "type": "Circular Economy"},
        {"title": "The Sixth Extinction", "author": "Elizabeth Kolbert", "type": "Environment"},
        {"title": "Drawdown", "author": "Paul Hawken", "type": "Climate Solutions"},
        {"title": "Sustainable Web Design", "author": "Tom Greenwood", "type": "Green Tech"}
    ]
    
    for resource in resources:
        title = resource['title']
        author = resource['author']
        rtype = resource['type']
        st.markdown(f"📖 **{title}** by {author} ({rtype})")

# ==================== TAB 2: UN SDGs ====================
with tabs[1]:
    st.markdown("## 🌍 UN Sustainable Development Goals")
    
    st.markdown("""
    <div class="sdg-box">
        <h3>17 Global Goals for 2030</h3>
        <p>The United Nations' blueprint for achieving a better and more sustainable future for all.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # SDGs relevant to technology
    st.markdown("### 🎯 SDGs Most Relevant to Technology")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="theory-box">
            <h4>🎓 SDG 4: Quality Education</h4>
            <strong>Technology's Role:</strong><br>
            • E-learning platforms (Coursera, edX)<br>
            • Educational apps and games<br>
            • Virtual reality for immersive learning<br>
            • AI tutors and personalized learning<br>
            • Open educational resources (OER)<br><br>
            
            <h4>⚡ SDG 7: Affordable & Clean Energy</h4>
            <strong>Technology's Role:</strong><br>
            • Smart grids and energy management<br>
            • Solar and wind power optimization<br>
            • Energy storage solutions (batteries)<br>
            • IoT for energy monitoring<br>
            • Blockchain for peer-to-peer energy trading
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="environment-box">
            <h4>🏭 SDG 9: Industry, Innovation & Infrastructure</h4>
            <strong>Technology's Role:</strong><br>
            • Industry 4.0 and automation<br>
            • 5G and broadband connectivity<br>
            • Sustainable manufacturing<br>
            • Digital infrastructure<br>
            • Innovation hubs and incubators<br><br>
            
            <h4>🌆 SDG 11: Sustainable Cities</h4>
            <strong>Technology's Role:</strong><br>
            • Smart city solutions<br>
            • IoT sensors for traffic and pollution<br>
            • Green building technologies<br>
            • Public transportation optimization<br>
            • Waste management systems
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        <div class="tech-box">
            <h4>🌡️ SDG 13: Climate Action</h4>
            <strong>Technology's Role:</strong><br>
            • Climate modeling and prediction<br>
            • Carbon capture and storage<br>
            • Renewable energy technologies<br>
            • Green transportation (EVs)<br>
            • Climate monitoring satellites<br><br>
            
            <h4>🤝 SDG 17: Partnerships for Goals</h4>
            <strong>Technology's Role:</strong><br>
            • Collaboration platforms<br>
            • Open source software<br>
            • Data sharing and APIs<br>
            • Global innovation networks<br>
            • Technology transfer
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="theory-box">
            <h4>💻 Technology's Cross-Cutting Impact</h4>
            <strong>Digital Divide:</strong><br>
            • Internet access inequality<br>
            • Device affordability<br>
            • Digital literacy<br><br>
            
            <strong>Responsible Innovation:</strong><br>
            • AI ethics and bias<br>
            • Data privacy and security<br>
            • Environmental impact of tech<br>
            • E-waste management<br><br>
            
            <strong>Measurement:</strong><br>
            • SDG indicators and metrics<br>
            • Impact assessment tools<br>
            • Sustainability reporting
        </div>
        """, unsafe_allow_html=True)

# ==================== TAB 3: CIRCULAR ECONOMY ====================
with tabs[2]:
    st.markdown("## ♻️ Circular Economy")
    
    st.markdown("### 1️⃣ Circular Economy Principles")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Linear vs Circular Economy:</strong><br><br>
        
        <strong>Linear Economy (Take-Make-Waste):</strong><br>
        1. Extract raw materials<br>
        2. Manufacture products<br>
        3. Use products<br>
        4. Dispose as waste<br>
        • Unsustainable resource depletion<br>
        • Environmental pollution<br><br>
        
        <strong>Circular Economy:</strong><br>
        1. Design out waste and pollution<br>
        2. Keep products and materials in use<br>
        3. Regenerate natural systems<br><br>
        
        <strong>Key Strategies:</strong><br>
        • <strong>Reduce:</strong> Minimize resource consumption<br>
        • <strong>Reuse:</strong> Extend product lifespan<br>
        • <strong>Repair:</strong> Fix instead of replace<br>
        • <strong>Refurbish:</strong> Restore to like-new condition<br>
        • <strong>Remanufacture:</strong> Rebuild products<br>
        • <strong>Recycle:</strong> Convert waste into new materials
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ E-Waste Management")
    
    st.markdown("""
    <div class="environment-box">
        <strong>E-Waste Problem:</strong><br>
        • 50+ million tons generated annually<br>
        • Only 20% properly recycled<br>
        • Contains toxic materials (lead, mercury)<br>
        • Valuable materials wasted (gold, copper)<br><br>
        
        <strong>E-Waste Hierarchy:</strong><br>
        1. <strong>Prevention:</strong> Design for longevity<br>
        2. <strong>Reuse:</strong> Donate or sell working devices<br>
        3. <strong>Repair:</strong> Fix broken components<br>
        4. <strong>Refurbish:</strong> Upgrade and resell<br>
        5. <strong>Recycle:</strong> Extract valuable materials<br>
        6. <strong>Disposal:</strong> Safe disposal as last resort<br><br>
        
        <strong>Best Practices:</strong><br>
        • Buy durable, repairable devices<br>
        • Support right-to-repair legislation<br>
        • Use certified e-waste recyclers<br>
        • Data wiping before disposal<br>
        • Choose modular designs (Framework laptop)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Product Lifecycle Management")
    
    st.markdown("""
    <div class="tech-box">
        <strong>Life Cycle Assessment (LCA):</strong><br>
        Evaluate environmental impact from cradle to grave<br><br>
        
        <strong>Stages:</strong><br>
        1. <strong>Raw Material Extraction:</strong> Mining, energy use<br>
        2. <strong>Manufacturing:</strong> Energy, water, emissions<br>
        3. <strong>Transportation:</strong> Carbon footprint<br>
        4. <strong>Use Phase:</strong> Energy consumption, maintenance<br>
        5. <strong>End of Life:</strong> Recycling, disposal<br><br>
        
        <strong>Design for Sustainability:</strong><br>
        • Modular design for easy repair<br>
        • Use recycled and recyclable materials<br>
        • Energy-efficient operation<br>
        • Minimize packaging<br>
        • Extended producer responsibility (EPR)<br><br>
        
        <strong>Examples:</strong><br>
        • Fairphone: Modular, repairable smartphone<br>
        • Framework: Upgradeable laptop<br>
        • Patagonia: Repair and resale programs
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: RENEWABLE ENERGY ====================
with tabs[3]:
    st.markdown("## ⚡ Renewable Energy")
    
    st.markdown("### 1️⃣ Renewable Energy Sources")
    
    energy_data = {
        'Source': ['Solar', 'Wind', 'Hydro', 'Geothermal', 'Biomass'],
        'Advantages': [
            'Abundant, scalable, low maintenance',
            'High efficiency, cost-effective',
            'Reliable, energy storage',
            'Consistent output, small footprint',
            'Carbon neutral, waste reduction'
        ],
        'Challenges': [
            'Intermittent, storage needed',
            'Location dependent, visual impact',
            'Environmental impact, location limited',
            'Geographic limitations',
            'Land use, emissions if not managed'
        ],
        'Tech Applications': [
            'Data centers, IoT sensors',
            'Grid power, charging stations',
            'Base load power',
            'Data centers in volcanic regions',
            'Backup power, heating'
        ]
    }
    
    df_energy = pd.DataFrame(energy_data)
    st.dataframe(df_energy, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Energy Efficiency in Computing")
    
    st.markdown("""
    <div class="tech-box">
        <strong>Green Data Centers:</strong><br>
        • <strong>PUE (Power Usage Effectiveness):</strong> Total power / IT power<br>
        • Target: PUE < 1.2 (Google achieves 1.1)<br>
        • Free cooling (outside air)<br>
        • Waste heat recovery<br>
        • Renewable energy powered<br><br>
        
        <strong>Energy-Efficient Hardware:</strong><br>
        • ARM processors (lower power than x86)<br>
        • SSDs instead of HDDs<br>
        • Energy Star certified equipment<br>
        • Server virtualization (consolidation)<br>
        • GPU optimization for AI workloads<br><br>
        
        <strong>Software Optimization:</strong><br>
        • Efficient algorithms (lower complexity)<br>
        • Code optimization and profiling<br>
        • Lazy loading and caching<br>
        • Database query optimization<br>
        • Serverless computing (pay per use)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Carbon Footprint")
    
    st.markdown("""
    <div class="environment-box">
        <strong>Carbon Footprint Calculation:</strong><br>
        CO₂ emissions from activities and products<br><br>
        
        <strong>Technology Carbon Footprint:</strong><br>
        • <strong>Manufacturing:</strong> 70-80% of total emissions<br>
        • <strong>Transportation:</strong> 5-10%<br>
        • <strong>Use Phase:</strong> 10-20%<br>
        • <strong>End of Life:</strong> 1-5%<br><br>
        
        <strong>Reduction Strategies:</strong><br>
        • Use renewable energy<br>
        • Optimize code efficiency<br>
        • Cloud computing (shared resources)<br>
        • Edge computing (reduce data transfer)<br>
        • Carbon offsetting programs<br><br>
        
        <strong>Carbon Neutral Tech Companies:</strong><br>
        • Google: Carbon neutral since 2007<br>
        • Microsoft: Carbon negative by 2030<br>
        • Apple: Carbon neutral by 2030<br>
        • Amazon: Net-zero carbon by 2040
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: GREEN TECHNOLOGY ====================
with tabs[4]:
    st.markdown("## 💻 Green Technology")
    
    st.markdown("### 1️⃣ Sustainable Software Design")
    
    st.markdown("""
    <div class="tech-box">
        <strong>Principles of Green Software:</strong><br><br>
        
        <strong>1. Energy Efficiency:</strong><br>
        • Optimize algorithms (O(n) vs O(n²))<br>
        • Reduce network requests<br>
        • Compress images and assets<br>
        • Lazy loading and code splitting<br>
        • Efficient database queries<br><br>
        
        <strong>2. Carbon Awareness:</strong><br>
        • Schedule jobs during low-carbon periods<br>
        • Use regions with renewable energy<br>
        • Carbon-aware load balancing<br><br>
        
        <strong>3. Hardware Efficiency:</strong><br>
        • Optimize for mobile devices<br>
        • Reduce memory usage<br>
        • Minimize CPU cycles<br>
        • GPU optimization<br><br>
        
        <strong>Tools:</strong><br>
        • Website Carbon Calculator<br>
        • Lighthouse (performance audits)<br>
        • Green Software Foundation tools<br>
        • Cloud Carbon Footprint
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Green AI")
    
    st.markdown("""
    <div class="theory-box">
        <strong>AI's Environmental Impact:</strong><br>
        • Training large models: High energy consumption<br>
        • GPT-3 training: ~1,287 MWh (284 tons CO₂)<br>
        • Inference: Ongoing energy use<br><br>
        
        <strong>Green AI Practices:</strong><br>
        • <strong>Model Efficiency:</strong> Smaller, optimized models<br>
        • <strong>Transfer Learning:</strong> Reuse pre-trained models<br>
        • <strong>Quantization:</strong> Reduce model size<br>
        • <strong>Pruning:</strong> Remove unnecessary parameters<br>
        • <strong>Distillation:</strong> Train smaller student models<br>
        • <strong>Edge AI:</strong> Run models on devices<br><br>
        
        <strong>Sustainable ML Frameworks:</strong><br>
        • TensorFlow Lite (mobile/edge)<br>
        • ONNX Runtime (optimized inference)<br>
        • PyTorch Mobile<br>
        • Carbon Tracker for ML
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ IoT for Sustainability")
    
    st.markdown("""
    <div class="environment-box">
        <strong>Smart City Applications:</strong><br>
        • <strong>Smart Lighting:</strong> LED + sensors, 50-70% energy savings<br>
        • <strong>Traffic Management:</strong> Reduce congestion and emissions<br>
        • <strong>Waste Management:</strong> Smart bins, optimized collection<br>
        • <strong>Air Quality Monitoring:</strong> Real-time pollution data<br>
        • <strong>Water Management:</strong> Leak detection, usage optimization<br><br>
        
        <strong>Smart Agriculture:</strong><br>
        • Precision farming (reduce water, fertilizer)<br>
        • Soil moisture sensors<br>
        • Drone monitoring<br>
        • Automated irrigation<br><br>
        
        <strong>Smart Buildings:</strong><br>
        • HVAC optimization (30% energy savings)<br>
        • Occupancy-based lighting<br>
        • Energy monitoring dashboards<br>
        • Predictive maintenance
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: CORPORATE SUSTAINABILITY ====================
with tabs[5]:
    st.markdown("## 🏢 Corporate Sustainability")
    
    st.markdown("### 1️⃣ ESG Framework")
    
    st.markdown("""
    <div class="sdg-box">
        <strong>ESG (Environmental, Social, Governance):</strong><br><br>
        
        <strong>Environmental:</strong><br>
        • Carbon emissions and climate impact<br>
        • Energy efficiency and renewable energy<br>
        • Waste management and recycling<br>
        • Water usage and conservation<br>
        • Biodiversity and ecosystem protection<br><br>
        
        <strong>Social:</strong><br>
        • Employee diversity and inclusion<br>
        • Labor practices and human rights<br>
        • Community engagement<br>
        • Data privacy and security<br>
        • Product safety and quality<br><br>
        
        <strong>Governance:</strong><br>
        • Board diversity and independence<br>
        • Executive compensation<br>
        • Business ethics and transparency<br>
        • Risk management<br>
        • Stakeholder engagement
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Sustainability Reporting")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Reporting Frameworks:</strong><br>
        • <strong>GRI (Global Reporting Initiative):</strong> Most widely used<br>
        • <strong>SASB (Sustainability Accounting Standards Board):</strong> Industry-specific<br>
        • <strong>TCFD (Task Force on Climate-related Financial Disclosures):</strong> Climate risk<br>
        • <strong>CDP (Carbon Disclosure Project):</strong> Environmental impact<br><br>
        
        <strong>Key Metrics:</strong><br>
        • Scope 1, 2, 3 emissions<br>
        • Energy consumption (renewable %)<br>
        • Water usage<br>
        • Waste generated and recycled<br>
        • Employee diversity statistics<br>
        • Supply chain sustainability<br><br>
        
        <strong>Certifications:</strong><br>
        • <strong>B Corp:</strong> Certified benefit corporation<br>
        • <strong>ISO 14001:</strong> Environmental management<br>
        • <strong>LEED:</strong> Green building certification<br>
        • <strong>Energy Star:</strong> Energy efficiency
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: CASE STUDIES ====================
with tabs[6]:
    st.markdown("## 🎯 Case Studies")
    
    case_studies = [
        {
            "title": "Case Study 1: Google's Carbon-Neutral Data Centers",
            "description": "How Google achieved carbon neutrality and industry-leading PUE",
            "details": """
**Challenge:**
- Data centers consume massive amounts of energy
- Traditional cooling methods inefficient
- Need to reduce carbon footprint

**Solutions Implemented:**

**1. Renewable Energy:**
- 100% renewable energy matching since 2017
- Largest corporate buyer of renewable energy
- Power Purchase Agreements (PPAs) for wind and solar
- On-site solar installations

**2. Cooling Optimization:**
- Machine learning for cooling optimization
- Free cooling (outside air when possible)
- Evaporative cooling
- Hot/cold aisle containment
- Waste heat recovery

**3. Hardware Efficiency:**
- Custom-designed servers
- Tensor Processing Units (TPUs) for AI
- Server utilization optimization
- Decommissioning old hardware

**4. Location Strategy:**
- Build near renewable energy sources
- Use regions with cooler climates
- Proximity to fiber optic networks
            """,
            "solution": """
**Results:**

| Metric | Achievement |
|--------|-------------|
| PUE | 1.10 (industry avg: 1.67) |
| Carbon Neutral | Since 2007 |
| Renewable Energy | 100% matched |
| Efficiency Gain | 50% more efficient than typical DC |
| Water Savings | 3.5 billion gallons annually |

**Key Innovations:**
- DeepMind AI reduced cooling energy by 40%
- Achieved 30% improvement in PUE
- Eliminated diesel backup generators (using batteries)

**Lessons Learned:**
- AI can significantly optimize energy use
- Renewable energy is cost-competitive
- Transparency drives accountability
- Continuous improvement is essential

**Future Goals:**
- Carbon-free energy 24/7 by 2030
- Zero waste to landfill
- Replenish 120% of water consumed
            """
        },
        {
            "title": "Case Study 2: Fairphone - Sustainable Smartphone",
            "description": "Building a modular, repairable, and ethical smartphone",
            "details": """
**Challenge:**
- Smartphones have short lifespans (2-3 years)
- E-waste problem growing
- Conflict minerals in supply chain
- Poor labor conditions in manufacturing

**Fairphone's Approach:**

**1. Modular Design:**
- User-replaceable battery
- Swappable camera modules
- Replaceable screen
- Upgradeable components
- 10/10 iFixit repairability score

**2. Ethical Sourcing:**
- Conflict-free minerals
- Fair trade gold
- Transparent supply chain
- Worker welfare programs
- Living wages for factory workers

**3. Longevity:**
- 5+ years software support
- Spare parts availability
- Repair guides and community
- Trade-in and recycling program

**4. Circular Economy:**
- Take-back program
- Refurbishment and resale
- Material recovery
- E-waste recycling partnerships
            """,
            "solution": """
**Impact:**

**Environmental:**
- 30% lower carbon footprint than average smartphone
- 40% recycled materials
- Extended device lifespan (5+ years vs 2-3)
- Reduced e-waste

**Social:**
- Improved working conditions
- Fair wages for 1000+ workers
- Conflict-free minerals
- Transparency in supply chain

**Economic:**
- Profitable business model
- Growing market share
- Premium pricing justified by values
- Strong customer loyalty

**Challenges:**
- Higher cost than competitors
- Limited scale and availability
- Trade-offs in specs vs repairability
- Supply chain complexity

**Key Takeaways:**
- Consumers willing to pay for sustainability
- Modular design is technically feasible
- Transparency builds trust
- Right-to-repair movement growing
            """
        }
    ]
    
    for idx, case in enumerate(case_studies, 1):
        with st.expander(f"📝 {case['title']}", expanded=False):
            st.markdown(f"**Description:** {case['description']}")
            st.markdown(case['details'])
            
            if st.button(f"Show Results", key=f"case_{idx}"):
                st.markdown("### Results & Impact")
                st.markdown(case['solution'])

# ==================== TAB 8: YOUTUBE ====================
with tabs[7]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video content for learning about Sustainability</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {"title": "UN Sustainable Development Goals", "channel": "United Nations", "url": "https://www.youtube.com/watch?v=0XTBYMfZyrM", "description": "Introduction to SDGs", "duration": "~3 min"},
        {"title": "Circular Economy", "channel": "Ellen MacArthur Foundation", "url": "https://www.youtube.com/watch?v=zCRKvDyyHmI", "description": "What is circular economy", "duration": "~4 min"},
        {"title": "Climate Change 101", "channel": "National Geographic", "url": "https://www.youtube.com/watch?v=oJAbATJCugs", "description": "Climate science basics", "duration": "~3 min"}
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
        {"title": "Renewable Energy", "channel": "Kurzgesagt", "url": "https://www.youtube.com/watch?v=0Hh5MYv7lWc", "description": "Can 100% renewable work?", "duration": "~9 min"},
        {"title": "E-Waste Problem", "channel": "Vox", "url": "https://www.youtube.com/watch?v=dd_ZttK3PuM", "description": "The e-waste crisis", "duration": "~7 min"},
        {"title": "Green Technology", "channel": "DW Planet A", "url": "https://www.youtube.com/c/DWPlanetA", "description": "Sustainable tech solutions", "duration": "Channel"}
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
        {"title": "Climate Solutions", "channel": "Project Drawdown", "url": "https://www.youtube.com/c/ProjectDrawdown", "description": "Top climate solutions", "duration": "Channel"},
        {"title": "Sustainable Business", "channel": "Harvard Business Review", "url": "https://www.youtube.com/user/HarvardBusiness", "description": "Corporate sustainability", "duration": "Channel"},
        {"title": "Green Software", "channel": "Green Software Foundation", "url": "https://www.youtube.com/c/GreenSoftwareFoundation", "description": "Sustainable software", "duration": "Channel"}
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
        1. Understand UN SDGs and global challenges<br>
        2. Learn circular economy principles<br>
        3. Study renewable energy technologies<br>
        4. Explore green technology and software<br>
        5. Understand corporate sustainability (ESG)<br>
        6. Calculate carbon footprint<br>
        7. Apply sustainability to your projects<br>
        8. Stay updated on climate solutions<br><br>
        
        <strong>Practical Actions:</strong><br>
        • Measure your personal carbon footprint<br>
        • Optimize code for energy efficiency<br>
        • Choose renewable energy providers<br>
        • Repair instead of replace devices<br>
        • Recycle e-waste properly<br>
        • Support sustainable companies<br>
        • Advocate for climate action<br><br>
        
        <strong>Career Opportunities:</strong><br>
        • Sustainability Consultant<br>
        • ESG Analyst<br>
        • Green Technology Developer<br>
        • Renewable Energy Engineer<br>
        • Circular Economy Specialist<br>
        • Corporate Sustainability Manager
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>SD101 - Sustainable Development</strong><br>
    <small>UTel University | Computer Engineering Program</small>
</div>
""", unsafe_allow_html=True)
