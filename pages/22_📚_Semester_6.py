import streamlit as st
import pandas as pd
from data.courses import COURSES

st.set_page_config(page_title="Semester 6 Overview", page_icon="🎓", layout="wide")

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .semester-header {
        background: linear-gradient(135deg, #a855f7 0%, #9333ea 100%);
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
        border-left: 5px solid;
        transition: transform 0.2s;
    }
    
    .course-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }
    
    .concentration-card {
        background: linear-gradient(135deg, #f3e8ff 0%, #e9d5ff 100%);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 5px solid #a855f7;
    }
    
    .stat-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        margin: 0.5rem;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        color: #92400e;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #78350f;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="semester-header">
    <div class="semester-title">📚 Semester 6</div>
    <div style="font-size: 1.3rem; opacity: 0.95;">Concentration & Capstone</div>
    <div style="font-size: 1rem; opacity: 0.85; margin-top: 0.5rem;">
        Choose your specialization and prepare for graduation
    </div>
</div>
""", unsafe_allow_html=True)

# Get semester 6 courses
semester_6_courses = {code: data for code, data in COURSES.items() if data.get("semester") == 6}

# Calculate statistics
total_credits = sum(course["credits"] for course in semester_6_courses.values())
total_hours = sum(course["hours_per_week"] for course in semester_6_courses.values())
avg_difficulty = sum(course["difficulty"] for course in semester_6_courses.values()) / len(semester_6_courses)

# Statistics
st.markdown("## 📊 Semester Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-number">{len(semester_6_courses)}</div>
        <div class="stat-label">Total Courses</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-number">{total_credits}</div>
        <div class="stat-label">Total Credits</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-number">{total_hours}</div>
        <div class="stat-label">Hours/Week</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-number">{avg_difficulty:.1f}/7</div>
        <div class="stat-label">Avg Difficulty</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Semester Overview
st.markdown("## 🎯 Semester Overview")

st.markdown("""
<div style="background: linear-gradient(135deg, #ede9fe 0%, #ddd6fe 100%); padding: 2rem; border-radius: 15px; border-left: 5px solid #a855f7;">
    <h3>🌟 Specialization Semester</h3>
    <p style="font-size: 1.1rem; line-height: 1.8;">
        Semester 6 is the <strong>concentration semester</strong> where you choose your specialization path. 
        You'll take one concentration course (Finance, IT, or Management) along with Sustainable Development. 
        This semester focuses on applying your knowledge to your chosen field and preparing for your final project.
    </p>
    
    <h4 style="margin-top: 1.5rem;">🎓 Key Focus Areas:</h4>
    <ul style="font-size: 1.05rem; line-height: 1.8;">
        <li><strong>Specialization:</strong> Deep dive into your chosen concentration</li>
        <li><strong>Sustainability:</strong> Environmental and ethical considerations in technology</li>
        <li><strong>Capstone Preparation:</strong> Planning your final graduation project</li>
        <li><strong>Career Readiness:</strong> Preparing for internships and job market</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Concentration Paths
st.markdown("## 🎯 Choose Your Concentration")

st.markdown("""
<div style="background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); padding: 1.5rem; border-radius: 12px; margin-bottom: 2rem;">
    <strong>⚠️ Important:</strong> You must choose ONE concentration course based on your career goals. 
    Each concentration has different prerequisites and focuses on different industry applications.
</div>
""", unsafe_allow_html=True)

# Separate courses by type
concentration_courses = {code: data for code, data in semester_6_courses.items() if data.get("category") == "Concentration"}
general_courses = {code: data for code, data in semester_6_courses.items() if data.get("category") != "Concentration"}

# Display concentration courses
col1, col2, col3 = st.columns(3)

concentration_list = list(concentration_courses.items())

if len(concentration_list) > 0:
    with col1:
        code, course = concentration_list[0]
        st.markdown(f"""
        <div class="concentration-card">
            <h3>💰 {course['name']}</h3>
            <p><strong>Code:</strong> {code}</p>
            <p><strong>Credits:</strong> {course['credits']} | <strong>Difficulty:</strong> {course['difficulty']}/7</p>
            <p><strong>Hours/Week:</strong> {course['hours_per_week']}</p>
            <p style="margin-top: 1rem;">{course['description']}</p>
            <p style="margin-top: 1rem;"><strong>Prerequisites:</strong> {', '.join(course['prerequisites']) if course['prerequisites'] else 'None'}</p>
        </div>
        """, unsafe_allow_html=True)

if len(concentration_list) > 1:
    with col2:
        code, course = concentration_list[1]
        st.markdown(f"""
        <div class="concentration-card">
            <h3>💻 {course['name']}</h3>
            <p><strong>Code:</strong> {code}</p>
            <p><strong>Credits:</strong> {course['credits']} | <strong>Difficulty:</strong> {course['difficulty']}/7</p>
            <p><strong>Hours/Week:</strong> {course['hours_per_week']}</p>
            <p style="margin-top: 1rem;">{course['description']}</p>
            <p style="margin-top: 1rem;"><strong>Prerequisites:</strong> {', '.join(course['prerequisites']) if course['prerequisites'] else 'None'}</p>
        </div>
        """, unsafe_allow_html=True)

if len(concentration_list) > 2:
    with col3:
        code, course = concentration_list[2]
        st.markdown(f"""
        <div class="concentration-card">
            <h3>📊 {course['name']}</h3>
            <p><strong>Code:</strong> {code}</p>
            <p><strong>Credits:</strong> {course['credits']} | <strong>Difficulty:</strong> {course['difficulty']}/7</p>
            <p><strong>Hours/Week:</strong> {course['hours_per_week']}</p>
            <p style="margin-top: 1rem;">{course['description']}</p>
            <p style="margin-top: 1rem;"><strong>Prerequisites:</strong> {', '.join(course['prerequisites']) if course['prerequisites'] else 'None'}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# General Education Course
st.markdown("## 🌍 General Education")

for code, course in general_courses.items():
    category_colors = {
        "General": "#94a3b8"
    }
    color = category_colors.get(course["category"], "#6b7280")
    
    st.markdown(f"""
    <div class="course-card" style="border-left-color: {color};">
        <h3>{course['name']}</h3>
        <p><strong>Code:</strong> {code} | <strong>Category:</strong> {course['category']} | <strong>Type:</strong> {course['type']}</p>
        <p><strong>Credits:</strong> {course['credits']} | <strong>Difficulty:</strong> {course['difficulty']}/7 | <strong>Hours/Week:</strong> {course['hours_per_week']}</p>
        <p style="margin-top: 1rem;">{course['description']}</p>
        <p style="margin-top: 1rem;"><strong>Prerequisites:</strong> {', '.join(course['prerequisites']) if course['prerequisites'] else 'None'}</p>
        
        <details style="margin-top: 1rem;">
            <summary style="cursor: pointer; font-weight: 600;">📋 Learning Outcomes</summary>
            <ul style="margin-top: 0.5rem;">
                {"".join(f"<li>{outcome}</li>" for outcome in course['learning_outcomes'])}
            </ul>
        </details>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Course Comparison Table
st.markdown("## 📊 Course Comparison")

comparison_data = []
for code, course in semester_6_courses.items():
    comparison_data.append({
        "Code": code,
        "Course Name": course["name"],
        "Category": course["category"],
        "Credits": course["credits"],
        "Difficulty": f"{course['difficulty']}/7",
        "Hours/Week": course["hours_per_week"],
        "Type": course["type"]
    })

df = pd.DataFrame(comparison_data)
st.dataframe(df, use_container_width=True, hide_index=True)

st.markdown("---")

# Study Tips
st.markdown("## 💡 Study Tips for Semester 6")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%); padding: 1.5rem; border-radius: 12px; border-left: 5px solid #3b82f6;">
        <h4>🎯 Concentration Focus</h4>
        <ul>
            <li>Choose concentration aligned with career goals</li>
            <li>Network with professionals in your field</li>
            <li>Work on concentration-specific projects</li>
            <li>Attend industry events and seminars</li>
            <li>Build portfolio showcasing specialization</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%); padding: 1.5rem; border-radius: 12px; border-left: 5px solid #10b981;">
        <h4>🚀 Capstone Preparation</h4>
        <ul>
            <li>Start planning your final project</li>
            <li>Identify potential advisors</li>
            <li>Research project topics in your concentration</li>
            <li>Prepare project proposal</li>
            <li>Consider industry partnerships</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Career Paths
st.markdown("## 🎓 Career Paths by Concentration")

career_paths = {
    "Finance": {
        "icon": "💰",
        "roles": [
            "Quantitative Analyst",
            "Financial Software Developer",
            "Fintech Engineer",
            "Algorithmic Trader",
            "Risk Analyst"
        ],
        "skills": [
            "Financial modeling",
            "Algorithmic trading",
            "Data analysis",
            "Blockchain technology",
            "Risk management"
        ]
    },
    "IT": {
        "icon": "💻",
        "roles": [
            "Cloud Architect",
            "DevOps Engineer",
            "Cybersecurity Specialist",
            "Systems Administrator",
            "Network Engineer"
        ],
        "skills": [
            "Cloud computing (AWS, Azure, GCP)",
            "Cybersecurity",
            "Infrastructure management",
            "Automation and scripting",
            "Enterprise systems"
        ]
    },
    "Management": {
        "icon": "📊",
        "roles": [
            "IT Project Manager",
            "Product Manager",
            "Scrum Master",
            "Technical Lead",
            "Business Analyst"
        ],
        "skills": [
            "Agile methodologies",
            "Team leadership",
            "Project management",
            "Business strategy",
            "Stakeholder management"
        ]
    }
}

cols = st.columns(3)

for idx, (concentration, data) in enumerate(career_paths.items()):
    with cols[idx]:
        st.markdown(f"""
        <div style="background: white; padding: 1.5rem; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); height: 100%;">
            <h3>{data['icon']} {concentration}</h3>
            
            <h4 style="margin-top: 1.5rem;">Career Roles:</h4>
            <ul>
                {"".join(f"<li>{role}</li>" for role in data['roles'])}
            </ul>
            
            <h4 style="margin-top: 1.5rem;">Key Skills:</h4>
            <ul>
                {"".join(f"<li>{skill}</li>" for skill in data['skills'])}
            </ul>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Next Steps
st.markdown("## 🎯 Next Steps")

st.markdown("""
<div style="background: linear-gradient(135deg, #fce7f3 0%, #fbcfe8 100%); padding: 2rem; border-radius: 15px; border-left: 5px solid #ec4899;">
    <h3>📅 Semester 6 Checklist</h3>
    <ul style="font-size: 1.05rem; line-height: 2;">
        <li>✅ <strong>Choose your concentration</strong> (Finance, IT, or Management)</li>
        <li>✅ <strong>Complete Sustainable Development</strong> course</li>
        <li>✅ <strong>Plan your capstone project</strong> for Semester 7</li>
        <li>✅ <strong>Network with industry professionals</strong> in your field</li>
        <li>✅ <strong>Update your portfolio</strong> with concentration projects</li>
        <li>✅ <strong>Apply for internships</strong> or job opportunities</li>
        <li>✅ <strong>Prepare for graduation</strong> and career transition</li>
    </ul>
    
    <h3 style="margin-top: 2rem;">🎓 After Semester 6</h3>
    <p style="font-size: 1.05rem; line-height: 1.8;">
        <strong>Semester 7:</strong> Capstone project, final electives, and graduation preparation<br>
        <strong>Semester 8:</strong> Internship, thesis defense, and graduation
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>Semester 6 - Concentration & Capstone Preparation</strong><br>
    <small>UTel University | Computer Engineering Program</small>
</div>
""", unsafe_allow_html=True)
