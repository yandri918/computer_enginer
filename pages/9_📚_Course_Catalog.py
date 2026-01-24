import streamlit as st
import pandas as pd
import altair as alt
import sys
sys.path.append('.')

from data.courses import COURSES, CATEGORY_COLORS, DIFFICULTY_LEVELS

st.set_page_config(page_title="Course Catalog", page_icon="📚", layout="wide")

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .course-card {
        background: white;
        border-left: 5px solid #3b82f6;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transition: all 0.3s;
    }
    
    .course-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.12);
    }
    
    .course-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }
    
    .course-code {
        font-size: 0.85rem;
        font-weight: 700;
        color: #3b82f6;
        background: #eff6ff;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
    }
    
    .course-title {
        font-size: 1.4rem;
        font-weight: 700;
        color: #1e293b;
        margin: 0.5rem 0;
    }
    
    .course-credits {
        font-size: 1rem;
        font-weight: 600;
        color: #7c3aed;
    }
    
    .course-desc {
        color: #64748b;
        line-height: 1.6;
        margin: 1rem 0;
    }
    
    .badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.75rem;
        font-weight: 600;
        margin: 0.2rem;
    }
    
    .badge-category {
        background: #dbeafe;
        color: #1e40af;
    }
    
    .badge-difficulty {
        background: #fef3c7;
        color: #92400e;
    }
    
    .badge-semester {
        background: #d1fae5;
        color: #065f46;
    }
    
    .prerequisites {
        background: #fef2f2;
        border-left: 3px solid #ef4444;
        padding: 0.8rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    
    .learning-outcomes {
        background: #f0fdf4;
        border-left: 3px solid #10b981;
        padding: 0.8rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("📚 Course Catalog")
st.markdown("Browse all Computer Engineering courses with detailed information")

# Sidebar filters
st.sidebar.header("🔍 Filters")

# Search
search_query = st.sidebar.text_input("Search courses", placeholder="Enter course name or code...")

# Category filter
categories = sorted(set(course['category'] for course in COURSES.values()))
selected_categories = st.sidebar.multiselect(
    "Category",
    categories,
    default=categories
)

# Semester filter
semesters = sorted(set(course['semester'] for course in COURSES.values()))
selected_semesters = st.sidebar.multiselect(
    "Semester",
    [f"Semester {s}" for s in semesters],
    default=[f"Semester {s}" for s in semesters]
)
selected_semesters = [int(s.split()[1]) for s in selected_semesters]

# Difficulty filter
difficulty_range = st.sidebar.slider(
    "Difficulty Level",
    min_value=1,
    max_value=7,
    value=(1, 7)
)

# Credits filter
credits_range = st.sidebar.slider(
    "Credits",
    min_value=2,
    max_value=4,
    value=(2, 4)
)

# Type filter
course_types = sorted(set(course['type'] for course in COURSES.values()))
selected_types = st.sidebar.multiselect(
    "Course Type",
    course_types,
    default=course_types
)

# Filter courses
filtered_courses = {}
for code, course in COURSES.items():
    # Apply filters
    if course['category'] not in selected_categories:
        continue
    if course['semester'] not in selected_semesters:
        continue
    if not (difficulty_range[0] <= course['difficulty'] <= difficulty_range[1]):
        continue
    if not (credits_range[0] <= course['credits'] <= credits_range[1]):
        continue
    if course['type'] not in selected_types:
        continue
    
    # Search filter
    if search_query:
        search_lower = search_query.lower()
        if (search_lower not in course['name'].lower() and 
            search_lower not in code.lower() and
            search_lower not in course['description'].lower()):
            continue
    
    filtered_courses[code] = course

# Display results
st.markdown(f"### Found {len(filtered_courses)} courses")

# Sort options
col1, col2 = st.columns([3, 1])
with col2:
    sort_by = st.selectbox(
        "Sort by",
        ["Semester", "Name", "Credits", "Difficulty"],
        label_visibility="collapsed"
    )

# Sort courses
if sort_by == "Semester":
    sorted_courses = sorted(filtered_courses.items(), key=lambda x: (x[1]['semester'], x[1]['name']))
elif sort_by == "Name":
    sorted_courses = sorted(filtered_courses.items(), key=lambda x: x[1]['name'])
elif sort_by == "Credits":
    sorted_courses = sorted(filtered_courses.items(), key=lambda x: x[1]['credits'], reverse=True)
else:  # Difficulty
    sorted_courses = sorted(filtered_courses.items(), key=lambda x: x[1]['difficulty'], reverse=True)

# Display courses
for code, course in sorted_courses:
    # Determine border color based on category
    border_color = CATEGORY_COLORS.get(course['category'], '#3b82f6')
    
    with st.expander(f"{code} - {course['name']}", expanded=False):
        st.markdown(f"""
        <div class="course-card" style="border-left-color: {border_color};">
            <div class="course-header">
                <div>
                    <span class="course-code">{code}</span>
                    <div class="course-title">{course['name']}</div>
                </div>
                <div class="course-credits">{course['credits']} Credits</div>
            </div>
            
            <div>
                <span class="badge badge-category">{course['category']}</span>
                <span class="badge badge-difficulty">{DIFFICULTY_LEVELS[course['difficulty']]}</span>
                <span class="badge badge-semester">Semester {course['semester']}</span>
            </div>
            
            <div class="course-desc">{course['description']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Prerequisites
        if course['prerequisites']:
            prereq_names = [f"{p} - {COURSES[p]['name']}" for p in course['prerequisites'] if p in COURSES]
            st.markdown(f"""
            <div class="prerequisites">
                <strong>📋 Prerequisites:</strong><br>
                {', '.join(prereq_names) if prereq_names else 'None'}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("✅ No prerequisites required")
        
        # Learning outcomes
        st.markdown("""
        <div class="learning-outcomes">
            <strong>🎯 Learning Outcomes:</strong>
        </div>
        """, unsafe_allow_html=True)
        
        for outcome in course['learning_outcomes']:
            st.markdown(f"- {outcome}")
        
        # Additional info
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Hours/Week", f"{course['hours_per_week']} hrs")
        with col2:
            st.metric("Course Type", course['type'])
        with col3:
            conc_str = ", ".join(course['concentrations'])
            st.metric("Concentrations", conc_str if len(conc_str) < 20 else f"{len(course['concentrations'])} tracks")
        
        # Deep dive button for courses with dedicated pages
        if code in ["MA101"]:  # Add more course codes as we create pages
            st.markdown("---")
            if st.button(f"📖 Deep Dive into {code}", key=f"dive_{code}", use_container_width=True):
                st.success(f"✅ Navigate to **📐 MA101 Calculus** in the sidebar to access detailed course materials!")

# Summary statistics
if filtered_courses:
    st.markdown("---")
    st.markdown("### 📊 Filtered Courses Statistics")
    
    # Prepare data
    df_filtered = pd.DataFrame([
        {
            'code': code,
            'name': course['name'],
            'category': course['category'],
            'credits': course['credits'],
            'difficulty': course['difficulty'],
            'semester': course['semester']
        }
        for code, course in filtered_courses.items()
    ])
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Category distribution
        category_counts = df_filtered['category'].value_counts().reset_index()
        category_counts.columns = ['category', 'count']
        
        chart = alt.Chart(category_counts).mark_bar(
            cornerRadiusTopLeft=8,
            cornerRadiusTopRight=8
        ).encode(
            x=alt.X('count:Q', title='Number of Courses'),
            y=alt.Y('category:N', title='Category', sort='-x'),
            color=alt.Color(
                'category:N',
                scale=alt.Scale(
                    domain=list(CATEGORY_COLORS.keys()),
                    range=list(CATEGORY_COLORS.values())
                ),
                legend=None
            ),
            tooltip=['category', 'count']
        ).properties(
            title="Courses by Category",
            height=300
        )
        
        st.altair_chart(chart, use_container_width=True)
    
    with col2:
        # Difficulty distribution
        difficulty_chart = alt.Chart(df_filtered).mark_bar(
            cornerRadiusTopLeft=8,
            cornerRadiusTopRight=8
        ).encode(
            x=alt.X('difficulty:Q', title='Difficulty Level', bin=alt.Bin(maxbins=7)),
            y=alt.Y('count():Q', title='Number of Courses'),
            color=alt.value('#7c3aed'),
            tooltip=[alt.Tooltip('difficulty:Q', title='Difficulty'), alt.Tooltip('count():Q', title='Count')]
        ).properties(
            title="Difficulty Distribution",
            height=300
        )
        
        st.altair_chart(difficulty_chart, use_container_width=True)

else:
    st.warning("No courses match your filters. Try adjusting the filter criteria.")

# Footer
st.markdown("---")
st.caption("💡 Tip: Use the sidebar filters to narrow down courses by category, semester, difficulty, and more!")
