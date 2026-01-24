import streamlit as st
import pandas as pd
import altair as alt
import sys
sys.path.append('.')

from data.courses import COURSES, CATEGORY_COLORS
from data.concentrations import CONCENTRATIONS

# Page config
st.set_page_config(
    page_title="UTel University - Computer Engineering",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #1e40af 0%, #7c3aed 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(30, 64, 175, 0.2);
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        color: white;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .main-subtitle {
        font-size: 1.3rem;
        color: #e0e7ff;
        font-weight: 400;
    }
    
    .stat-card {
        background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
        border: 2px solid #bae6fd;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.1);
        transition: transform 0.2s;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(59, 130, 246, 0.2);
    }
    
    .stat-value {
        font-size: 2.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #1e40af 0%, #7c3aed 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .feature-card {
        background: white;
        border-left: 4px solid #3b82f6;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .feature-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #1e293b;
        margin-bottom: 0.5rem;
    }
    
    .feature-desc {
        color: #64748b;
        font-size: 0.95rem;
        line-height: 1.6;
    }
    
    .concentration-badge {
        display: inline-block;
        background: linear-gradient(135deg, #8b5cf6 0%, #a855f7 100%);
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.3rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <div class="main-title">🎓 UTel University</div>
    <div class="main-subtitle">Bachelor in Computer Engineering</div>
</div>
""", unsafe_allow_html=True)

# Calculate statistics
total_courses = len(COURSES)
total_credits = sum(course['credits'] for course in COURSES.values())
categories = set(course['category'] for course in COURSES.values())
avg_difficulty = sum(course['difficulty'] for course in COURSES.values()) / total_courses

# Stats row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-value">{total_courses}</div>
        <div class="stat-label">Total Courses</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-value">{total_credits}</div>
        <div class="stat-label">Total Credits</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-value">{len(categories)}</div>
        <div class="stat-label">Categories</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-value">3</div>
        <div class="stat-label">Concentrations</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Main content
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("### 📊 Course Distribution by Category")
    
    # Prepare data for Altair
    category_data = {}
    for course in COURSES.values():
        cat = course['category']
        category_data[cat] = category_data.get(cat, 0) + course['credits']
    
    df_category = pd.DataFrame([
        {'category': cat, 'credits': credits} 
        for cat, credits in category_data.items()
    ])
    
    # Altair pie chart
    pie_chart = alt.Chart(df_category).mark_arc(innerRadius=50).encode(
        theta=alt.Theta(field="credits", type="quantitative"),
        color=alt.Color(
            field="category", 
            type="nominal",
            scale=alt.Scale(
                domain=list(CATEGORY_COLORS.keys()),
                range=list(CATEGORY_COLORS.values())
            ),
            legend=alt.Legend(title="Category")
        ),
        tooltip=[
            alt.Tooltip('category:N', title='Category'),
            alt.Tooltip('credits:Q', title='Credits')
        ]
    ).properties(
        width=500,
        height=400
    )
    
    st.altair_chart(pie_chart, use_container_width=True)
    
    # Credit distribution by semester
    st.markdown("### 📅 Credits by Semester")
    
    semester_data = {}
    for course in COURSES.values():
        sem = course['semester']
        semester_data[sem] = semester_data.get(sem, 0) + course['credits']
    
    df_semester = pd.DataFrame([
        {'semester': f"Semester {sem}", 'credits': credits}
        for sem, credits in sorted(semester_data.items())
    ])
    
    bar_chart = alt.Chart(df_semester).mark_bar(
        cornerRadiusTopLeft=10,
        cornerRadiusTopRight=10
    ).encode(
        x=alt.X('semester:N', title='Semester', sort=None),
        y=alt.Y('credits:Q', title='Total Credits'),
        color=alt.value('#3b82f6'),
        tooltip=['semester', 'credits']
    ).properties(
        height=300
    )
    
    st.altair_chart(bar_chart, use_container_width=True)

with col_right:
    st.markdown("### 🎯 Concentrations")
    
    for conc_key, conc_data in CONCENTRATIONS.items():
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-title">{conc_data['name']}</div>
            <div class="feature-desc">{conc_data['description']}</div>
            <div style="margin-top: 1rem;">
                <span class="concentration-badge">{conc_data['total_credits']} Credits</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 📈 Program Highlights")
    
    highlights = [
        {"icon": "🏆", "title": "Accredited Program", "desc": "ABET accredited curriculum"},
        {"icon": "💼", "title": "95% Job Placement", "desc": "Within 6 months of graduation"},
        {"icon": "🌍", "title": "Global Recognition", "desc": "Degree recognized worldwide"},
        {"icon": "🔬", "title": "Research Opportunities", "desc": "State-of-the-art labs"}
    ]
    
    for highlight in highlights:
        st.markdown(f"""
        <div style="background: #f8fafc; padding: 1rem; border-radius: 10px; margin: 0.5rem 0;">
            <span style="font-size: 1.5rem;">{highlight['icon']}</span>
            <strong style="margin-left: 0.5rem;">{highlight['title']}</strong>
            <div style="color: #64748b; font-size: 0.85rem; margin-top: 0.3rem;">{highlight['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

# Features section
st.markdown("---")
st.markdown("## 🚀 Explore the Curriculum")

feature_cols = st.columns(3)

features = [
    {
        "icon": "📚",
        "title": "Course Catalog",
        "desc": "Browse all courses with detailed descriptions, prerequisites, and learning outcomes",
        "page": "pages/1_📚_Course_Catalog.py"
    },
    {
        "icon": "🗺️",
        "title": "Curriculum Roadmap",
        "desc": "Visual semester-by-semester course sequence and planning",
        "page": "pages/2_🗺️_Curriculum_Roadmap.py"
    },
    {
        "icon": "🔗",
        "title": "Prerequisites",
        "desc": "Interactive dependency graph showing course relationships",
        "page": "pages/3_🔗_Prerequisites.py"
    },
    {
        "icon": "🎯",
        "title": "Concentrations",
        "desc": "Compare Finance, IT, and Management specializations",
        "page": "pages/4_🎯_Concentrations.py"
    },
    {
        "icon": "📊",
        "title": "Analytics",
        "desc": "Deep dive into credit distribution and difficulty analysis",
        "page": "pages/5_📊_Analytics.py"
    },
    {
        "icon": "🛤️",
        "title": "Learning Path",
        "desc": "Create your personalized course plan and roadmap",
        "page": "pages/6_🛤️_Learning_Path.py"
    }
]

for idx, feature in enumerate(features):
    with feature_cols[idx % 3]:
        st.markdown(f"""
        <div class="feature-card">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">{feature['icon']}</div>
            <div class="feature-title">{feature['title']}</div>
            <div class="feature-desc">{feature['desc']}</div>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 2rem;">
    <strong>UTel University</strong> - Bachelor in Computer Engineering<br>
    <small>Empowering Future Tech Leaders Since 1995</small>
</div>
""", unsafe_allow_html=True)
