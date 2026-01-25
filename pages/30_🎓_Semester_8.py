import streamlit as st
import pandas as pd

st.set_page_config(page_title="Semester 8", page_icon="🎓", layout="wide")

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .semester-header {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: white;
        padding: 3rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .semester-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .course-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-left: 5px solid #f59e0b;
        transition: transform 0.2s;
    }
    
    .course-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }
    
    .capstone-card {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 1.5rem 0;
        box-shadow: 0 6px 10px rgba(0,0,0,0.15);
        border-left: 8px solid #f59e0b;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="semester-header">
    <div class="semester-title">🎓 Semester 8</div>
    <div style="font-size: 1.2rem; opacity: 0.9;">Final Semester - Capstone & Advanced Electives</div>
    <div style="font-size: 1rem; opacity: 0.8; margin-top: 0.5rem;">Total: 18 Credits | Focus: Specialization & Graduation Project</div>
</div>
""", unsafe_allow_html=True)

# Semester Overview
st.markdown("## 🎯 Semester Overview")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Credits", "18", help="Total credits for this semester")
with col2:
    st.metric("Capstone Project", "6 credits", help="Final graduation project")
with col3:
    st.metric("Electives", "4 courses", help="Advanced elective courses")
with col4:
    st.metric("Avg Difficulty", "6/7", help="Average difficulty level")

st.markdown("---")

# Semester Description
st.markdown("""
### 📖 About Semester 8

**Final semester** - the culmination of your Computer Engineering journey! This semester focuses on:

- **🎯 Capstone Project:** 6-credit final project demonstrating mastery of skills
- **🚀 Advanced Electives:** Specialized courses in cutting-edge technologies
- **💼 Career Preparation:** Industry-ready skills and portfolio building
- **🎓 Graduation Ready:** Complete all requirements for degree

This is your opportunity to **showcase your expertise**, build a **portfolio-worthy project**, and prepare for your **professional career** in technology.
""")

st.markdown("---")

# Capstone Project
st.markdown("## 🎯 Capstone Project (6 Credits)")

st.markdown("""
<div class="capstone-card">
    <h3>🏆 CE499: Final Year Project</h3>
    <p><strong>Duration:</strong> Full semester (16 weeks)</p>
    <p><strong>Credits:</strong> 6</p>
    <p><strong>Type:</strong> Required</p>
    
    <h4>Project Requirements:</h4>
    <ul>
        <li>✅ Original software/hardware project</li>
        <li>✅ Applies concepts from multiple courses</li>
        <li>✅ Demonstrates technical depth and innovation</li>
        <li>✅ Includes documentation and presentation</li>
        <li>✅ Supervised by faculty advisor</li>
    </ul>
    
    <h4>Deliverables:</h4>
    <ul>
        <li>📄 Project proposal (Week 2)</li>
        <li>📊 Mid-semester progress report (Week 8)</li>
        <li>💻 Working prototype/system</li>
        <li>📖 Final report (30-50 pages)</li>
        <li>🎤 Final presentation (20 minutes)</li>
        <li>🎥 Demo video (5 minutes)</li>
    </ul>
    
    <h4>Example Projects:</h4>
    <ul>
        <li>🤖 AI-powered recommendation system</li>
        <li>📱 Mobile app with backend API</li>
        <li>☁️ Cloud-native microservices platform</li>
        <li>🔐 Cybersecurity tool or framework</li>
        <li>📊 Big data analytics dashboard</li>
        <li>🌐 Full-stack web application</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Elective Courses
st.markdown("## 📚 Advanced Elective Courses (Choose 4)")

courses = [
    {
        "code": "CE403",
        "name": "Mobile Application Development",
        "credits": 3,
        "type": "Elective",
        "category": "Programming",
        "difficulty": 5,
        "hours": 7,
        "description": "Native and cross-platform mobile app development for iOS and Android using React Native, Flutter, and modern mobile technologies.",
        "topics": ["React Native", "Flutter", "Mobile UI/UX", "Native APIs", "Push Notifications", "App Store Deployment"],
        "concentrations": ["IT", "Management"],
        "page": None
    },
    {
        "code": "CE404",
        "name": "Cloud Computing",
        "credits": 3,
        "type": "Elective",
        "category": "Infrastructure",
        "difficulty": 6,
        "hours": 7,
        "description": "Cloud platforms (AWS, Azure, GCP), cloud architecture, serverless computing, containers, and cloud-native application development.",
        "topics": ["AWS/Azure/GCP", "Docker & Kubernetes", "Serverless", "Cloud Architecture", "DevOps", "Microservices"],
        "concentrations": ["IT"],
        "page": None
    },
    {
        "code": "CE405",
        "name": "Cybersecurity",
        "credits": 3,
        "type": "Elective",
        "category": "Security",
        "difficulty": 6,
        "hours": 7,
        "description": "Network security, cryptography, ethical hacking, penetration testing, and security best practices for modern applications.",
        "topics": ["Network Security", "Cryptography", "Ethical Hacking", "Penetration Testing", "Security Audits", "Compliance"],
        "concentrations": ["IT"],
        "page": None
    },
    {
        "code": "CE406",
        "name": "Big Data Analytics",
        "credits": 3,
        "type": "Elective",
        "category": "Data Science",
        "difficulty": 6,
        "hours": 7,
        "description": "Big data technologies (Hadoop, Spark), data processing, analytics, visualization, and machine learning at scale.",
        "topics": ["Hadoop & Spark", "Data Processing", "Data Visualization", "ML at Scale", "Real-time Analytics", "Data Warehousing"],
        "concentrations": ["IT", "Finance"],
        "page": None
    },
    {
        "code": "CE407",
        "name": "Blockchain & Cryptocurrency",
        "credits": 3,
        "type": "Elective",
        "category": "Emerging Tech",
        "difficulty": 6,
        "hours": 7,
        "description": "Blockchain technology, smart contracts, cryptocurrency, DeFi, NFTs, and distributed ledger applications.",
        "topics": ["Blockchain Basics", "Smart Contracts", "Ethereum & Solidity", "DeFi", "NFTs", "Consensus Algorithms"],
        "concentrations": ["IT", "Finance"],
        "page": None
    },
    {
        "code": "CE408",
        "name": "Internet of Things (IoT)",
        "credits": 3,
        "type": "Elective",
        "category": "Embedded Systems",
        "difficulty": 5,
        "hours": 7,
        "description": "IoT architecture, sensors, embedded systems, communication protocols, edge computing, and IoT applications.",
        "topics": ["Arduino & Raspberry Pi", "Sensors & Actuators", "MQTT & CoAP", "Edge Computing", "IoT Security", "Smart Home"],
        "concentrations": ["IT"],
        "page": None
    }
]

# Display courses
for course in courses:
    code = course['code']
    name = course['name']
    credits = course['credits']
    ctype = course['type']
    category = course['category']
    difficulty = course['difficulty']
    hours = course['hours']
    description = course['description']
    topics = course['topics']
    concentrations = course['concentrations']
    page = course['page']
    
    with st.expander(f"**{code}: {name}** ({credits} credits)", expanded=False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"**📖 Description:**")
            st.markdown(description)
            
            st.markdown(f"**📚 Key Topics:**")
            topics_str = " • ".join(topics)
            st.markdown(f"• {topics_str}")
        
        with col2:
            st.markdown(f"**📊 Course Info:**")
            st.markdown(f"**Type:** {ctype}")
            st.markdown(f"**Category:** {category}")
            difficulty_str = "⭐" * difficulty
            st.markdown(f"**Difficulty:** {difficulty_str} ({difficulty}/7)")
            st.markdown(f"**Hours/Week:** {hours}")
            
            conc_str = ", ".join(concentrations)
            st.markdown(f"**Concentrations:** {conc_str}")
        
        if page:
            st.markdown(f"**🔗 [View Detailed Course Page →](/{page})**")
        else:
            st.info("📝 Detailed course page coming soon!")

st.markdown("---")

# Course Selection Guide
st.markdown("## 🎯 Course Selection Guide")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 💻 IT Concentration
    
    **Recommended Electives:**
    - ✅ CE404: Cloud Computing (Must-take)
    - ✅ CE405: Cybersecurity
    - ⭐ CE406: Big Data Analytics
    - ⭐ CE408: IoT
    
    **Capstone Ideas:**
    - Cloud-native microservices platform
    - Security audit tool
    - IoT smart home system
    - Real-time analytics dashboard
    """)

with col2:
    st.markdown("""
    ### 💼 Finance & Management
    
    **Recommended Electives:**
    - ✅ CE403: Mobile App Development
    - ✅ CE407: Blockchain & Cryptocurrency
    - ⭐ CE406: Big Data Analytics
    
    **Capstone Ideas:**
    - Fintech mobile app
    - Blockchain-based payment system
    - Trading analytics platform
    - Business intelligence dashboard
    """)

st.markdown("---")

# Timeline
st.markdown("## 📅 Semester Timeline")

timeline_data = {
    'Week': ['1-2', '3-4', '5-8', '9-10', '11-14', '15-16'],
    'Capstone Milestone': [
        'Project proposal & approval',
        'Requirements & design',
        'Implementation (Phase 1)',
        'Mid-semester presentation',
        'Implementation (Phase 2) & testing',
        'Final report & presentation'
    ],
    'Elective Focus': [
        'Course introduction & setup',
        'Fundamentals',
        'Core concepts & labs',
        'Midterm exams',
        'Advanced topics & projects',
        'Final exams & project demos'
    ]
}

df_timeline = pd.DataFrame(timeline_data)
st.dataframe(df_timeline, use_container_width=True, hide_index=True)

st.markdown("---")

# Graduation Requirements
st.markdown("## ✅ Graduation Requirements Checklist")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📚 Academic Requirements
    
    - ✅ Complete all 144 credits
    - ✅ Minimum GPA: 2.0 (C average)
    - ✅ No failing grades in core courses
    - ✅ Complete capstone project
    - ✅ Fulfill concentration requirements
    """)

with col2:
    st.markdown("""
    ### 🎓 Final Steps
    
    - ✅ Submit graduation application
    - ✅ Clear all financial obligations
    - ✅ Return library books
    - ✅ Complete exit survey
    - ✅ Order cap and gown
    """)

st.markdown("---")

# Career Preparation
st.markdown("## 🚀 Career Preparation")

career_col1, career_col2 = st.columns(2)

with career_col1:
    st.markdown("""
    ### 💼 Job Search
    
    - **Resume:** Highlight capstone project and skills
    - **Portfolio:** GitHub with 3-5 strong projects
    - **LinkedIn:** Professional profile with projects
    - **Job Boards:** LinkedIn, Indeed, Glassdoor
    - **Networking:** Alumni, meetups, conferences
    - **Interview Prep:** LeetCode, system design
    """)

with career_col2:
    st.markdown("""
    ### 📜 Certifications (Optional)
    
    - **Cloud:** AWS Solutions Architect, Azure
    - **Security:** CompTIA Security+, CEH
    - **Data:** Google Data Engineer
    - **Mobile:** Google Android Developer
    - **Project Management:** PMP, Scrum Master
    - **AI/ML:** TensorFlow Developer
    """)

st.markdown("---")

# Success Tips
st.markdown("## 💡 Success Tips for Final Semester")

tips_col1, tips_col2 = st.columns(2)

with tips_col1:
    st.markdown("""
    ### 🎯 Capstone Project
    
    - **Start Early:** Don't wait until week 5
    - **Scope Wisely:** Ambitious but achievable
    - **Document Everything:** Code, decisions, progress
    - **Regular Meetings:** Weekly advisor check-ins
    - **Version Control:** Git from day one
    - **Testing:** Unit tests, integration tests
    """)

with tips_col2:
    st.markdown("""
    ### 📚 Balancing Workload
    
    - **Time Management:** Capstone is 6 credits!
    - **Prioritize:** Focus on high-impact tasks
    - **Ask for Help:** Professors, peers, online
    - **Stay Healthy:** Sleep, exercise, breaks
    - **Celebrate Milestones:** Acknowledge progress
    - **Enjoy the Journey:** Last semester!
    """)

st.markdown("---")

# Post-Graduation Paths
st.markdown("## 🌟 Post-Graduation Paths")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 💼 Industry
    
    **Roles:**
    - Software Engineer
    - Full-Stack Developer
    - Cloud Engineer
    - Data Scientist
    - Security Analyst
    - Mobile Developer
    
    **Companies:**
    - Tech giants (Google, Microsoft)
    - Startups
    - Consulting firms
    - Financial institutions
    """)

with col2:
    st.markdown("""
    ### 🎓 Graduate School
    
    **Programs:**
    - MS in Computer Science
    - MS in Data Science
    - MS in Cybersecurity
    - MBA (Tech focus)
    - PhD in CS/AI
    
    **Benefits:**
    - Deeper specialization
    - Research opportunities
    - Higher salary potential
    - Academic career path
    """)

with col3:
    st.markdown("""
    ### 🚀 Entrepreneurship
    
    **Options:**
    - Tech startup
    - Freelance consulting
    - SaaS product
    - Mobile app business
    - Open source project
    
    **Resources:**
    - Incubators/accelerators
    - Venture capital
    - Angel investors
    - Crowdfunding
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>Semester 8 - Final Semester & Graduation</strong><br>
    <small>UTel University | Computer Engineering Program</small><br>
    <div style="margin-top: 1rem; font-size: 1.5rem;">🎓 Congratulations on reaching the final semester! 🎉</div>
</div>
""", unsafe_allow_html=True)
