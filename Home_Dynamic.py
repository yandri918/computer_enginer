
import streamlit as st
import json
import os
import sys

# Add current directory to path so we can import simulations
sys.path.append(os.path.dirname(__file__))

try:
    from simulations import SIMULATION_MAP, apply_custom_css
except ImportError:
    # Fallback if file not found (for testing)
    SIMULATION_MAP = {}
    def apply_custom_css(): pass

# Load Data
DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "curriculum.json")

def load_data():
    if not os.path.exists(DATA_FILE):
        st.error("Data file not found. Please run migration script.")
        return {}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    st.set_page_config(page_title="UTel Curriculum Hub", page_icon="🎓", layout="wide")
    
    # Apply global styles
    apply_custom_css()
    
    curriculum = load_data()
    if not curriculum:
        return

    # Sidebar
    st.sidebar.title("🎓 UTel University")
    
    # Semester Selection
    semesters = list(curriculum.keys())
    # Sort semesters naturally (Semester 1, 2, ... 10)
    semesters.sort(key=lambda x: int(x.split(" ")[1]) if x.split(" ")[1].isdigit() else 99)
    
    selected_semester = st.sidebar.selectbox("Select Semester", semesters)
    
    # Course Selection
    courses = curriculum[selected_semester]
    course_options = [f"{c['icon']} {c['id']} - {c['name']}" for c in courses]
    selected_course_idx = st.sidebar.radio("Select Course", range(len(courses)), format_func=lambda i: course_options[i])
    
    course_data = courses[selected_course_idx]
    
    # --- MAIN CONTENT RENDER ---
    
    # Header
    st.markdown(f"""
    <div class="course-header">
        <div style="font-size: 1.2rem; opacity: 0.9;">{course_data['id']}</div>
        <div class="course-title">{course_data['name']}</div>
        <div>{course_data['icon']} {course_data['credits']} Credits | Semester {course_data['semester']} | Difficulty: {course_data['difficulty']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Credits", course_data['credits'])
    col2.metric("Semester", course_data['semester'])
    col3.metric("Difficulty", course_data['difficulty'])
    col4.metric("Hours/Week", course_data['hours'])
    
    st.markdown("---")
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["📚 Syllabus", "🧪 Simulation", "📺 Resources"])
    
    with tab1:
        st.markdown("## 📖 Course Overview")
        st.markdown(f"""
        <div class="theory-box">
            <h3>Course Description</h3>
            <p>{course_data['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📋 Topics Covered")
        if course_data['topics']:
            for topic in course_data['topics']:
                st.markdown(f"- {topic}")
        else:
            st.info("Topics details coming soon.")
            
    with tab2:
        st.subheader("Interactive Simulation")
        
        # Dynamic Dispatch to Simulation Logic
        simulation_func = SIMULATION_MAP.get(course_data['id'])
        
        if simulation_func:
            simulation_func()
        else:
            st.info(f"Interactive simulation for {course_data['name']} is under development.")
            st.markdown("""
            > [!TIP]
            > This is where the interactive Streamlit components will load.
            > Since this is a dynamic page, we load different logic based on the Course ID.
            """)
            
    with tab3:
        st.subheader("Learning Resources")
        
        resources = course_data.get('resources', [])
        
        if not resources:
            st.info("No resources added for this course yet.")
        else:
            for res in resources:
                if res['type'] == 'youtube':
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        st.video(res['url'])
                    with col2:
                        st.markdown(f"**📺 {res['title']}**")
                        st.caption(res.get('description', ''))
                
                elif res['type'] in ['pdf', 'paper']:
                    st.markdown(f"""
                    <div style="padding: 1rem; background-color: #f0fdf4; border-radius: 8px; border-left: 4px solid #10b981; margin-bottom: 0.5rem;">
                        <span style="font-size: 1.2rem;">📄</span>
                        <a href="{res['url']}" target="_blank" style="text-decoration: none; font-weight: 600; color: #064e3b; margin-left: 8px;">
                            {res['title']}
                        </a>
                        <br>
                        <span style="color: #6b7280; font-size: 0.9rem; margin-left: 32px;">{res.get('description', 'PDF Document')}</span>
                    </div>
                    """, unsafe_allow_html=True)
                    
                else: # Generic links/websites
                    st.markdown(f"""
                    <div style="padding: 1rem; background-color: #f8fafc; border-radius: 8px; border-left: 4px solid #64748b; margin-bottom: 0.5rem;">
                        <span style="font-size: 1.2rem;">🔗</span>
                        <a href="{res['url']}" target="_blank" style="text-decoration: none; font-weight: 600; color: #1e293b; margin-left: 8px;">
                            {res['title']}
                        </a>
                        <br>
                        <span style="color: #6b7280; font-size: 0.9rem; margin-left: 32px;">{res.get('description', 'External Link')}</span>
                    </div>
                    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
