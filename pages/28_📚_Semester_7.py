import streamlit as st
import pandas as pd

st.set_page_config(page_title="Semester 7", page_icon="🎓", layout="wide")

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .semester-header {
        background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
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
        border-left: 5px solid #8b5cf6;
        transition: transform 0.2s;
    }
    
    .course-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }
    
    .course-code {
        color: #8b5cf6;
        font-weight: 700;
        font-size: 1.1rem;
    }
    
    .course-name {
        font-size: 1.3rem;
        font-weight: 600;
        margin: 0.5rem 0;
    }
    
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 12px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 0.5rem;
    }
    
    .badge-core {
        background: #dbeafe;
        color: #1e40af;
    }
    
    .badge-elective {
        background: #d1fae5;
        color: #065f46;
    }
    
    .badge-concentration {
        background: #fef3c7;
        color: #92400e;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="semester-header">
    <div class="semester-title">📚 Semester 7</div>
    <div style="font-size: 1.2rem; opacity: 0.9;">Advanced Topics & Specialization</div>
    <div style="font-size: 1rem; opacity: 0.8; margin-top: 0.5rem;">Total: 18 Credits | Focus: AI, Advanced Systems & Electives</div>
</div>
""", unsafe_allow_html=True)

# Semester Overview
st.markdown("## 🎯 Semester Overview")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Credits", "18", help="Total credits for this semester")
with col2:
    st.metric("Core Courses", "1", help="Required core courses")
with col3:
    st.metric("Electives", "5", help="Choose from elective courses")
with col4:
    st.metric("Avg Difficulty", "6/7", help="Average difficulty level")

st.markdown("---")

# Semester Description
st.markdown("""
### 📖 About Semester 7

Semester 7 marks the **advanced specialization phase** of your Computer Engineering journey. This semester focuses on:

- **🤖 Artificial Intelligence:** Deep dive into AI, machine learning, and neural networks
- **🌐 Advanced Web Development:** Full-stack development with modern frameworks
- **🎓 Elective Specialization:** Choose courses aligned with your career goals
- **💼 Industry Preparation:** Practical skills for professional software development

This semester allows you to **specialize** in your chosen concentration (IT, Finance, or Management) while building advanced technical skills.
""")

st.markdown("---")

# Courses
st.markdown("## 📚 Semester 7 Courses")

# Course data
courses = [
    {
        "code": "CE401",
        "name": "Web Development",
        "credits": 3,
        "type": "Elective",
        "category": "Programming",
        "difficulty": 5,
        "hours": 7,
        "description": "Modern web development using HTML, CSS, JavaScript, React, Node.js, and databases. Full-stack development from frontend to backend deployment.",
        "topics": ["HTML/CSS/JavaScript", "React & Modern Frontend", "Node.js & Express", "Databases (SQL/NoSQL)", "REST APIs", "Authentication", "Deployment"],
        "concentrations": ["IT", "Management"],
        "page": "26_🌐_CE401_Web_Development"
    },
    {
        "code": "CE402",
        "name": "Artificial Intelligence",
        "credits": 4,
        "type": "Elective",
        "category": "AI/ML",
        "difficulty": 7,
        "hours": 8,
        "description": "Comprehensive AI course covering search algorithms, machine learning, neural networks, deep learning, and AI applications in real-world problems.",
        "topics": ["Search Algorithms", "Machine Learning", "Neural Networks", "Deep Learning", "NLP", "Computer Vision", "AI Ethics"],
        "concentrations": ["IT"],
        "page": None  # To be created
    },
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
            page_link = f"pages/{page}.py"
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
    - ✅ CE402: Artificial Intelligence (Must-take)
    - ✅ CE404: Cloud Computing
    - ✅ CE405: Cybersecurity
    - ⭐ CE401: Web Development
    - ⭐ CE406: Big Data Analytics
    
    **Career Focus:**
    - Software Engineer
    - Cloud Architect
    - AI/ML Engineer
    - Security Specialist
    - DevOps Engineer
    """)

with col2:
    st.markdown("""
    ### 💼 Finance & Management
    
    **Recommended Electives:**
    - ✅ CE401: Web Development
    - ✅ CE403: Mobile App Development
    - ⭐ CE406: Big Data Analytics
    - ⭐ CE402: Artificial Intelligence
    
    **Career Focus:**
    - Fintech Developer
    - Product Manager
    - Technical Consultant
    - Business Analyst
    - Startup Founder
    """)

st.markdown("---")

# Prerequisites Check
st.markdown("## ✅ Prerequisites Check")

prereq_data = {
    'Course': ['CE401', 'CE402', 'CE403', 'CE404', 'CE405', 'CE406'],
    'Prerequisites': [
        'CE201, CE304',
        'CE204, MA201',
        'CE201, CE401',
        'CE303, CE304',
        'CE304, CE305',
        'CE204, MA201, MA301'
    ],
    'Recommended Background': [
        'Basic programming, databases',
        'Data structures, linear algebra',
        'Web development basics',
        'Networking, Linux',
        'Networking, operating systems',
        'Statistics, Python, databases'
    ]
}

df_prereq = pd.DataFrame(prereq_data)
st.dataframe(df_prereq, use_container_width=True, hide_index=True)

st.markdown("---")

# Study Tips
st.markdown("## 💡 Study Tips for Semester 7")

tips_col1, tips_col2 = st.columns(2)

with tips_col1:
    st.markdown("""
    ### 📚 Academic Success
    
    - **Choose Wisely:** Select electives aligned with career goals
    - **Build Portfolio:** Create projects for each course
    - **Industry Tools:** Learn tools used in industry
    - **Collaborate:** Work on group projects
    - **Stay Updated:** Follow tech trends and news
    """)

with tips_col2:
    st.markdown("""
    ### 🚀 Career Preparation
    
    - **Internships:** Apply for summer internships
    - **Open Source:** Contribute to open source projects
    - **Networking:** Attend tech meetups and conferences
    - **Certifications:** Consider AWS, Azure, or Google Cloud certs
    - **Resume:** Build strong technical resume with projects
    """)

st.markdown("---")

# Workload Distribution
st.markdown("## ⏰ Estimated Workload")

workload_data = {
    'Course': ['CE401', 'CE402', 'CE403', 'CE404', 'CE405', 'CE406'],
    'Lectures': [3, 4, 3, 3, 3, 3],
    'Labs': [2, 2, 2, 2, 2, 2],
    'Self-Study': [2, 2, 2, 2, 2, 2],
    'Total Hours/Week': [7, 8, 7, 7, 7, 7]
}

df_workload = pd.DataFrame(workload_data)
st.dataframe(df_workload, use_container_width=True, hide_index=True)

st.markdown("**Note:** Choose 5-6 courses to reach 18 credits. Balance difficulty and workload.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>Semester 7 - Advanced Topics & Specialization</strong><br>
    <small>UTel University | Computer Engineering Program</small>
</div>
""", unsafe_allow_html=True)
