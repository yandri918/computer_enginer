import streamlit as st
import pandas as pd
import altair as alt
import sys
sys.path.append('.')

from data.courses import COURSES, CATEGORY_COLORS

st.set_page_config(page_title="Curriculum Roadmap", page_icon="🗺️", layout="wide")

st.title("🗺️ Curriculum Roadmap")
st.markdown("Visual semester-by-semester course sequence")

# Organize courses by semester
semester_courses = {}
for code, course in COURSES.items():
    sem = course['semester']
    if sem not in semester_courses:
        semester_courses[sem] = []
    semester_courses[sem].append({
        'code': code,
        **course
    })

# Prepare data for Gantt chart
gantt_data = []
for code, course in COURSES.items():
    gantt_data.append({
        'course': f"{code}",
        'name': course['name'],
        'semester': course['semester'],
        'category': course['category'],
        'credits': course['credits'],
        'difficulty': course['difficulty']
    })

df_gantt = pd.DataFrame(gantt_data)

# Semester view selector
view_mode = st.radio(
    "View Mode",
    ["All Semesters", "By Semester"],
    horizontal=True
)

if view_mode == "All Semesters":
    st.markdown("### 📅 Complete 8-Semester Roadmap")
    
    # Gantt-style visualization
    chart = alt.Chart(df_gantt).mark_bar(
        cornerRadiusTopLeft=5,
        cornerRadiusTopRight=5,
        height=20
    ).encode(
        x=alt.X('semester:O', title='Semester', axis=alt.Axis(labelAngle=0)),
        y=alt.Y('course:N', title='Course Code', sort=alt.EncodingSortField(field='semester', order='ascending')),
        color=alt.Color(
            'category:N',
            scale=alt.Scale(
                domain=list(CATEGORY_COLORS.keys()),
                range=list(CATEGORY_COLORS.values())
            ),
            legend=alt.Legend(title="Category", orient='right')
        ),
        tooltip=[
            alt.Tooltip('course:N', title='Code'),
            alt.Tooltip('name:N', title='Course Name'),
            alt.Tooltip('semester:O', title='Semester'),
            alt.Tooltip('category:N', title='Category'),
            alt.Tooltip('credits:Q', title='Credits'),
            alt.Tooltip('difficulty:Q', title='Difficulty')
        ]
    ).properties(
        height=800
    ).interactive()
    
    st.altair_chart(chart, use_container_width=True)
    
    # Credit accumulation chart
    st.markdown("### 📈 Cumulative Credits Progress")
    
    semester_credits = df_gantt.groupby('semester')['credits'].sum().reset_index()
    semester_credits['cumulative'] = semester_credits['credits'].cumsum()
    
    # Area chart for cumulative credits
    area_chart = alt.Chart(semester_credits).mark_area(
        line={'color': '#3b82f6'},
        color=alt.Gradient(
            gradient='linear',
            stops=[
                alt.GradientStop(color='#dbeafe', offset=0),
                alt.GradientStop(color='#3b82f6', offset=1)
            ],
            x1=0,
            x2=0,
            y1=1,
            y2=0
        )
    ).encode(
        x=alt.X('semester:O', title='Semester'),
        y=alt.Y('cumulative:Q', title='Cumulative Credits'),
        tooltip=[
            alt.Tooltip('semester:O', title='Semester'),
            alt.Tooltip('credits:Q', title='Credits This Semester'),
            alt.Tooltip('cumulative:Q', title='Total Credits')
        ]
    ).properties(
        height=300
    )
    
    # Add points
    points = alt.Chart(semester_credits).mark_circle(
        size=100,
        color='#1e40af'
    ).encode(
        x='semester:O',
        y='cumulative:Q',
        tooltip=['semester:O', 'credits:Q', 'cumulative:Q']
    )
    
    st.altair_chart(area_chart + points, use_container_width=True)

else:  # By Semester view
    selected_semester = st.selectbox(
        "Select Semester",
        [f"Semester {i}" for i in range(1, 9)],
        index=0
    )
    
    sem_num = int(selected_semester.split()[1])
    courses_in_sem = semester_courses.get(sem_num, [])
    
    if courses_in_sem:
        st.markdown(f"### 📚 {selected_semester} - {len(courses_in_sem)} Courses")
        
        total_credits = sum(c['credits'] for c in courses_in_sem)
        avg_difficulty = sum(c['difficulty'] for c in courses_in_sem) / len(courses_in_sem)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Courses", len(courses_in_sem))
        with col2:
            st.metric("Total Credits", total_credits)
        with col3:
            st.metric("Avg Difficulty", f"{avg_difficulty:.1f}/7")
        
        # Display courses in cards
        for course in sorted(courses_in_sem, key=lambda x: x['name']):
            with st.expander(f"{course['code']} - {course['name']}", expanded=True):
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"**Category:** {course['category']}")
                    st.markdown(f"**Description:** {course['description']}")
                    
                    if course['prerequisites']:
                        prereq_str = ", ".join(course['prerequisites'])
                        st.warning(f"📋 **Prerequisites:** {prereq_str}")
                    else:
                        st.success("✅ No prerequisites")
                
                with col2:
                    st.metric("Credits", course['credits'])
                    st.metric("Difficulty", f"{course['difficulty']}/7")
                    st.metric("Hours/Week", course['hours_per_week'])
        
        # Category breakdown for this semester
        st.markdown("### 📊 Category Breakdown")
        
        df_sem = pd.DataFrame(courses_in_sem)
        category_credits = df_sem.groupby('category')['credits'].sum().reset_index()
        
        pie = alt.Chart(category_credits).mark_arc(innerRadius=50).encode(
            theta=alt.Theta('credits:Q'),
            color=alt.Color(
                'category:N',
                scale=alt.Scale(
                    domain=list(CATEGORY_COLORS.keys()),
                    range=list(CATEGORY_COLORS.values())
                )
            ),
            tooltip=['category', 'credits']
        ).properties(
            width=400,
            height=400
        )
        
        st.altair_chart(pie, use_container_width=True)
    else:
        st.info(f"No courses scheduled for {selected_semester}")

# Recommended sequence
st.markdown("---")
st.markdown("### 💡 Recommended Course Sequence Tips")

tips = [
    "📌 **Semester 1-2**: Focus on foundational courses (Math, Programming, Physics)",
    "📌 **Semester 3-4**: Build core CS skills (OOP, Data Structures, OS)",
    "📌 **Semester 5-6**: Specialize with concentration courses and electives",
    "📌 **Semester 7-8**: Advanced topics, capstone project, and internship",
    "⚠️ **Always check prerequisites** before enrolling in a course",
    "💡 **Balance difficulty**: Mix challenging courses with easier ones each semester"
]

for tip in tips:
    st.markdown(tip)

st.markdown("---")
st.caption("🎓 This roadmap is a suggested sequence. Consult with your academic advisor for personalized planning.")
