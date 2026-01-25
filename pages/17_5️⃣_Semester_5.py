import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path to import data module
sys.path.append(str(Path(__file__).parent.parent))
from data.courses import COURSES

st.set_page_config(page_title="Semester 5 - UTel CE", page_icon="5️⃣", layout="wide")

# Custom CSS with purple/violet theme for Semester 5
st.markdown("""
<style>
    .semester-header {
        background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
        color: white;
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(139, 92, 246, 0.3);
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
        border-left: 5px solid #8b5cf6;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.2s;
    }
    
    .course-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
    }
    
    .stat-box {
        background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%);
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        border: 2px solid #8b5cf6;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="semester-header">
    <div class="semester-title">5️⃣ Semester 5</div>
    <div class="semester-subtitle">Advanced Specialization - Deep Technical Focus</div>
</div>
""", unsafe_allow_html=True)

# Get Semester 5 courses
semester_5_courses = {code: info for code, info in COURSES.items() if info["semester"] == 5}

# Statistics
col1, col2, col3, col4 = st.columns(4)

total_credits = sum(course["credits"] for course in semester_5_courses.values())
core_courses = sum(1 for course in semester_5_courses.values() if course["type"] == "Core")
avg_difficulty = sum(course["difficulty"] for course in semester_5_courses.values()) / len(semester_5_courses) if semester_5_courses else 0
total_hours = sum(course["hours_per_week"] for course in semester_5_courses.values())

with col1:
    st.markdown(f"""
    <div class="stat-box">
        <h2 style="color: #7c3aed; margin: 0;">{len(semester_5_courses)}</h2>
        <p style="margin: 0;">Total Courses</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="stat-box">
        <h2 style="color: #7c3aed; margin: 0;">{total_credits}</h2>
        <p style="margin: 0;">Total Credits</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="stat-box">
        <h2 style="color: #7c3aed; margin: 0;">{avg_difficulty:.1f}/7</h2>
        <p style="margin: 0;">Avg Difficulty</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="stat-box">
        <h2 style="color: #7c3aed; margin: 0;">{total_hours}</h2>
        <p style="margin: 0;">Hours/Week</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Course selector
st.markdown("## 📚 Select a Course to Explore")

course_options = {f"{code} - {info['name']}": code for code, info in sorted(semester_5_courses.items())}
selected_course_name = st.selectbox(
    "Choose course:",
    options=list(course_options.keys()),
    key="course_selector"
)

selected_code = course_options[selected_course_name]
course = semester_5_courses[selected_code]

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
    "MA301": "🔢 Higher Algebra",
    "CE401": "💾 Database Systems",
    "CE402": "🌐 Computer Networks"
}

available_deep_dives = {code: name for code, name in deep_dive_courses.items() if code in semester_5_courses}

if available_deep_dives:
    st.markdown("**Available comprehensive course materials:**")
    
    cols = st.columns(len(available_deep_dives) if len(available_deep_dives) <= 3 else 3)
    for idx, (code, name) in enumerate(available_deep_dives.items()):
        with cols[idx % 3]:
            st.warning(f"""
            **{name}**  
            {code} - {semester_5_courses[code]['name']}
            
            🚧 Coming soon!
            """)
else:
    st.info("📚 Deep dive materials for Semester 5 courses are being developed!")

# Course list
st.markdown("---")
st.markdown("## 📋 All Semester 5 Courses")

for code, info in sorted(semester_5_courses.items()):
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
        <strong>Semester 5 - Advanced Specialization</strong><br>
        Deep technical focus and concentration-specific advanced courses<br>
        <small>UTel University | Computer Engineering Program</small>
    </p>
</div>
""", unsafe_allow_html=True)
