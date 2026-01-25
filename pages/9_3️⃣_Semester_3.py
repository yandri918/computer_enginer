import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path to import data module
sys.path.append(str(Path(__file__).parent.parent))
from data.courses import COURSES

st.set_page_config(page_title="Semester 3 - UTel CE", page_icon="3️⃣", layout="wide")

# Custom CSS with orange/amber theme for Semester 3
st.markdown("""
<style>
    .semester-header {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(245, 158, 11, 0.3);
    }
    
    .semester-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .semester-subtitle {
        font-size: 1.3rem;
        opacity: 0.95;
        font-weight: 300;
    }
    
    .course-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #f59e0b;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    
    .course-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }
    
    .stat-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        border: 2px solid #f59e0b;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="semester-header">
    <div class="semester-title">3️⃣ Semester 3</div>
    <div class="semester-subtitle">Advancing Your Knowledge - Core Engineering Principles</div>
</div>
""", unsafe_allow_html=True)

# Get Semester 3 courses
semester_3_courses = {code: info for code, info in COURSES.items() if info["semester"] == 3}

# Statistics
col1, col2, col3, col4 = st.columns(4)

total_credits = sum(course["credits"] for course in semester_3_courses.values())
core_courses = sum(1 for course in semester_3_courses.values() if course["type"] == "Core")
avg_difficulty = sum(course["difficulty"] for course in semester_3_courses.values()) / len(semester_3_courses) if semester_3_courses else 0
total_hours = sum(course["hours_per_week"] for course in semester_3_courses.values())

with col1:
    st.markdown(f"""
    <div class="stat-box">
        <h2 style="color: #d97706; margin: 0;">{len(semester_3_courses)}</h2>
        <p style="margin: 0;">Total Courses</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="stat-box">
        <h2 style="color: #d97706; margin: 0;">{total_credits}</h2>
        <p style="margin: 0;">Total Credits</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="stat-box">
        <h2 style="color: #d97706; margin: 0;">{avg_difficulty:.1f}/7</h2>
        <p style="margin: 0;">Avg Difficulty</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="stat-box">
        <h2 style="color: #d97706; margin: 0;">{total_hours}</h2>
        <p style="margin: 0;">Hours/Week</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Course selector
st.markdown("## 📚 Select a Course to Explore")

course_options = {f"{code} - {info['name']}": code for code, info in sorted(semester_3_courses.items())}
selected_course_name = st.selectbox(
    "Choose course:",
    options=list(course_options.keys()),
    key="course_selector"
)

selected_code = course_options[selected_course_name]
course = semester_3_courses[selected_code]

# Display selected course details
st.markdown(f"### {selected_code} - {course['name']}")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"""
    **Category:** {course['category']}  
    **Type:** {course['type']}  
    **Credits:** {course['credits']} SKS  
    **Difficulty:** {'⭐' * course['difficulty']} ({course['difficulty']}/7)  
    **Study Hours:** {course['hours_per_week']} hours/week
    
    **Description:**  
    {course['description']}
    """)
    
    # Prerequisites
    if course['prerequisites']:
        prereq_names = [f"{p} - {COURSES[p]['name']}" for p in course['prerequisites'] if p in COURSES]
        st.markdown(f"""
        **Prerequisites:**  
        {', '.join(prereq_names)}
        """)
    else:
        st.info("ℹ️ No prerequisites required")

with col2:
    st.markdown("**Learning Outcomes:**")
    for outcome in course['learning_outcomes']:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("**Relevant Concentrations:**")
    for conc in course['concentrations']:
        st.markdown(f"🎯 {conc}")

# Deep dive links for courses with dedicated pages
st.markdown("---")
st.markdown("## 🎓 Deep Dive Materials")

deep_dive_courses = {
    "CE201": "💻 Object Oriented Programming",
    "CE202": "⚙️ Assembly Language",
    "MA201": "🔢 Linear Algebra"
}

available_deep_dives = {code: name for code, name in deep_dive_courses.items() if code in semester_3_courses}

if available_deep_dives:
    st.markdown("**Available comprehensive course materials:**")
    
    cols = st.columns(len(available_deep_dives))
    for idx, (code, name) in enumerate(available_deep_dives.items()):
        with cols[idx]:
            if code == "CE202":
                st.info(f"""
                **{name}**  
                {code} - {semester_3_courses[code]['name']}
                
                📍 Find in sidebar under course pages
                """)
            else:
                st.warning(f"""
                **{name}**  
                {code} - {semester_3_courses[code]['name']}
                
                🚧 Coming soon!
                """)
else:
    st.info("📚 Deep dive materials for Semester 3 courses are being developed!")

# Course list
st.markdown("---")
st.markdown("## 📋 All Semester 3 Courses")

for code, info in sorted(semester_3_courses.items()):
    with st.expander(f"{code} - {info['name']} ({info['credits']} SKS)"):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"**{info['description']}**")
            st.markdown(f"**Category:** {info['category']} | **Type:** {info['type']}")
            
            if info['prerequisites']:
                prereq_list = ', '.join(info['prerequisites'])
                st.markdown(f"**Prerequisites:** {prereq_list}")
        
        with col2:
            st.metric("Difficulty", f"{info['difficulty']}/7")
            st.metric("Hours/Week", info['hours_per_week'])

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 2rem;">
    <p style="font-size: 0.9rem;">
        <strong>Semester 3 - Advancing Your Knowledge</strong><br>
        Building on fundamentals with core engineering principles<br>
        <small>UTel University | Computer Engineering Program</small>
    </p>
</div>
""", unsafe_allow_html=True)
