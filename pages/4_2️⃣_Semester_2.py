import streamlit as st
import sys
sys.path.append('.')

from data.courses import COURSES

st.set_page_config(page_title="Semester 2 Courses", page_icon="2️⃣", layout="wide")

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .semester-header {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .course-card {
        background: white;
        border-left: 5px solid #10b981;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="semester-header">
    <h1>2️⃣ Semester 2</h1>
    <p>Advancing Your Knowledge - Core Engineering Principles</p>
</div>
""", unsafe_allow_html=True)

# Get semester 2 courses
semester_2_courses = {code: course for code, course in COURSES.items() if course['semester'] == 2}

# Display stats
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Courses", len(semester_2_courses))
with col2:
    total_credits = sum(c['credits'] for c in semester_2_courses.values())
    st.metric("Total Credits", total_credits)
with col3:
    avg_difficulty = sum(c['difficulty'] for c in semester_2_courses.values()) / len(semester_2_courses)
    st.metric("Avg Difficulty", f"{avg_difficulty:.1f}/7")

st.markdown("---")

# Course selection
st.markdown("### 📚 Select a Course to Explore")

course_options = {f"{code} - {course['name']}": code for code, course in sorted(semester_2_courses.items())}
selected_course_name = st.selectbox("Choose course:", list(course_options.keys()))
selected_code = course_options[selected_course_name]
selected_course = semester_2_courses[selected_code]

# Display selected course
st.markdown(f"## {selected_code} - {selected_course['name']}")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", selected_course['credits'])
with col2:
    st.metric("Category", selected_course['category'])
with col3:
    st.metric("Difficulty", f"{selected_course['difficulty']}/7")
with col4:
    st.metric("Hours/Week", selected_course['hours_per_week'])

st.markdown(f"**Description:** {selected_course['description']}")

st.markdown("**Learning Outcomes:**")
for outcome in selected_course['learning_outcomes']:
    st.markdown(f"✅ {outcome}")

# Prerequisites
if selected_course.get('prerequisites'):
    st.markdown("**Prerequisites:**")
    for prereq in selected_course['prerequisites']:
        prereq_course = COURSES.get(prereq)
        if prereq_course:
            st.markdown(f"📌 {prereq} - {prereq_course['name']}")

# Deep dive links (if available)
# Currently no deep dive pages for semester 2 courses yet
# if selected_code in ["CE201", "MA201"]:
#     st.markdown("---")
#     st.info(f"💡 **Deep Dive Available!** Navigate to the course page in the sidebar for comprehensive materials.")

# All courses overview
st.markdown("---")
st.markdown("### 📋 All Semester 2 Courses")

for code, course in sorted(semester_2_courses.items(), key=lambda x: x[1]['name']):
    with st.expander(f"{code} - {course['name']}", expanded=False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"**Category:** {course['category']}")
            st.markdown(f"**Description:** {course['description']}")
            
            if course.get('prerequisites'):
                st.markdown("**Prerequisites:**")
                for prereq in course['prerequisites']:
                    prereq_course = COURSES.get(prereq)
                    if prereq_course:
                        st.markdown(f"  • {prereq} - {prereq_course['name']}")
        
        with col2:
            st.metric("Credits", course['credits'])
            st.metric("Difficulty", f"{course['difficulty']}/7")

st.markdown("---")
st.caption("💡 Tip: Semester 2 builds upon Semester 1 foundations with more advanced topics in programming, mathematics, and engineering principles.")
