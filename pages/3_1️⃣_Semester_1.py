import streamlit as st
import sys
sys.path.append('.')

from data.courses import COURSES

st.set_page_config(page_title="Semester 1 Courses", page_icon="1️⃣", layout="wide")

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .semester-header {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .course-card {
        background: white;
        border-left: 5px solid #3b82f6;
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
    <h1>1️⃣ Semester 1</h1>
    <p>Foundation Courses - Building Your Engineering Base</p>
</div>
""", unsafe_allow_html=True)

# Get semester 1 courses
semester_1_courses = {code: course for code, course in COURSES.items() if course['semester'] == 1}

# Display stats
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Courses", len(semester_1_courses))
with col2:
    total_credits = sum(c['credits'] for c in semester_1_courses.values())
    st.metric("Total Credits", total_credits)
with col3:
    avg_difficulty = sum(c['difficulty'] for c in semester_1_courses.values()) / len(semester_1_courses)
    st.metric("Avg Difficulty", f"{avg_difficulty:.1f}/7")

st.markdown("---")

# Course selection
st.markdown("### 📚 Select a Course to Explore")

course_options = {f"{code} - {course['name']}": code for code, course in sorted(semester_1_courses.items())}
selected_course_name = st.selectbox("Choose course:", list(course_options.keys()))
selected_code = course_options[selected_course_name]
selected_course = semester_1_courses[selected_code]

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

# Deep dive links
if selected_code in ["MA101", "ID101"]:
    st.markdown("---")
    deep_dive_pages = {
        "MA101": "📐 MA101 Calculus",
        "ID101": "📝 ID101 Bahasa Indonesia"
    }
    st.info(f"💡 **Deep Dive Available!** Navigate to **{deep_dive_pages[selected_code]}** in the sidebar for comprehensive course materials.")

# All courses overview
st.markdown("---")
st.markdown("### 📋 All Semester 1 Courses")

for code, course in sorted(semester_1_courses.items(), key=lambda x: x[1]['name']):
    with st.expander(f"{code} - {course['name']}", expanded=False):
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"**Category:** {course['category']}")
            st.markdown(f"**Description:** {course['description']}")
        
        with col2:
            st.metric("Credits", course['credits'])
            st.metric("Difficulty", f"{course['difficulty']}/7")

st.markdown("---")
st.caption("💡 Tip: Semester 1 focuses on building strong foundations in mathematics, programming, and basic sciences.")
