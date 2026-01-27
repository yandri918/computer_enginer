
import streamlit as st
import json
import os
import sys

# Add current directory to path so we can import simulations
sys.path.append(os.path.dirname(__file__))

try:
    from simulations import SIMULATION_MAP, apply_custom_css
    from quizzes import render_quiz
    from pdf_utils import generate_syllabus_pdf
except ImportError:
    # Fallback if file not found (for testing)
    SIMULATION_MAP = {}
    def apply_custom_css(): pass
    def render_quiz(d): pass
    def generate_syllabus_pdf(d): return b""

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

    # Initialize Session State
    if 'selected_course_id' not in st.session_state:
        st.session_state.selected_course_id = None
        
    # --- SIDEBAR: STUDENT PROFILE (LMS Style) ---
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
        st.markdown("### Welcome, **Student**")
        st.caption("Computer Engineering • Semester 6")
        
        # MOCK PROGRESS
        st.markdown("#### 🎓 Academic Progress")
        st.progress(0.72)
        col_s1, col_s2 = st.columns(2)
        col_s1.metric("GPA", "3.85")
        col_s2.metric("Credits", "112/144")
        
        st.divider()
        st.markdown("#### 🔔 Notifications")
        st.info("Mid-term exams for **MA301** starting next week.")
        
    # --- MAIN STYLE ---
    st.markdown("""
    <style>
    /* Global Clean Tech Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hero Section */
    .hero-box {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 2rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    
    /* Course Cards */
    .course-card-btn {
        width: 100%;
        height: 100%;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        background: white;
        padding: 10px;
        transition: all 0.2s;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: transparent !important;
        font-weight: 600;
        font-size: 1rem;
    }
    
    /* Headings */
    h1, h2, h3 { color: #1e293b; letter-spacing: -0.02em; }
    </style>
    """, unsafe_allow_html=True)

    # --- HERO SECTION ---
    st.markdown("""
    <div class="hero-box">
        <h1 style="color:white; margin:0;">🎓 UTel Academic Portal</h1>
        <p style="opacity: 0.8; margin-top: 0.5rem; font-size: 1.1rem;">
            Access your courses, simulations, and learning resources in one unified hub.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- SEMESTER & COURSE NAVIGATION ---
    
    st.subheader("📚 My Courses")
    
    semesters = list(curriculum.keys())
    semesters.sort(key=lambda x: int(x.split(" ")[1]) if x.split(" ")[1].isdigit() else 99)
    
    # Filter Layout
    col_filter1, col_filter2 = st.columns([1, 2])
    with col_filter1:
        selected_semester = st.selectbox("Current Semester", semesters, index=0, label_visibility="collapsed")
    
    courses = curriculum[selected_semester]
    
    # Course Grid
    cols = st.columns(4) 
    for idx, course in enumerate(courses):
        with cols[idx % 4]:
            is_selected = st.session_state.selected_course_id == course['id']
            # Mock Status (Random for demo feel)
            status_color = "#10b981" if idx % 3 == 0 else "#f59e0b" # Green vs Amber
            status_text = "Completed" if idx % 3 == 0 else "In Progress"
            
            # Button Label with Status Indicator
            label = f"{course['icon']} {course['id']}\n{course['name']}"
            
            if st.button(
                label, 
                key=f"btn_{course['id']}", 
                use_container_width=True,
                type="primary" if is_selected else "secondary"
            ):
                st.session_state.selected_course_id = course['id']
                
            # Mini Status Bar below button
            st.markdown(f"""
            <div style="height: 4px; width: 100%; background: #e2e8f0; border-radius: 2px; margin-top: -8px; margin-bottom: 12px;">
                <div style="height: 100%; width: {'100%' if idx%3==0 else '45%'}; background: {status_color}; border-radius: 2px;"></div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # --- ACTIVE COURSE CONTENT ---
    active_course = next((c for c in courses if c['id'] == st.session_state.selected_course_id), None)
    
    if not active_course and courses:
        active_course = courses[0]
        st.session_state.selected_course_id = active_course['id']
        
    if active_course:
        render_course_content(active_course)

def render_course_content(course_data):
    """Renders the detailed content for a single course."""
    st.markdown(f"""
    <div style="background: white; padding: 2rem; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
        <div style="display: flex; justify-content: space-between; align-items: start;">
            <div>
                <span style="background: #eff6ff; color: #2563eb; padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 600;">{course_data['id']}</span>
                <h1 style="margin-top: 0.5rem; margin-bottom: 0.5rem; font-size: 2.2rem;">{course_data['name']}</h1>
                <div style="display: flex; gap: 1.5rem; color: #64748b; font-size: 0.95rem;">
                    <span>⚡ Difficulty: <b>{course_data['difficulty']}</b></span>
                    <span>🕒 {course_data['hours']} Hrs/Week</span>
                    <span>🏆 {course_data['credits']} Credits</span>
                </div>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 2.5rem;">{course_data['icon']}</div>
            </div>
        </div>
        
        <hr style="margin: 2rem 0; border-color: #f1f5f9;">
        
        <div style="font-size: 1.05rem; line-height: 1.6; color: #334155;">
            {course_data['description']}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("") 

    # Content Tabs
    tab1, tab2, tab_sim, tab_exam = st.tabs(["📚 Syllabus & Topics", "📺 Learning Resources", "🛠️ Launch Simulation", "📝 Final Exam"])

    with tab1:
        col_syl1, col_syl2 = st.columns([3, 1])
        with col_syl1:
             st.markdown("### 📋 Syllabus Breakdown")
        with col_syl2:
            try:
                pdf_bytes = generate_syllabus_pdf(course_data)
                st.download_button(
                    label="📄 Download PDF",
                    data=pdf_bytes,
                    file_name=f"Syllabus_{course_data['id']}.pdf",
                    mime="application/pdf",
                    key=f"dl_syl_{course_data['id']}"
                )
            except Exception as e:
                pass

        for topic in course_data.get('topics', []):
            st.markdown(f"""
            <div style="padding: 12px 16px; margin-bottom: 8px; background: #f8fafc; border-radius: 8px; border-left: 3px solid #cbd5e1; display: flex; align-items: center;">
                <span style="margin-right: 12px; color: #64748b;">•</span> {topic}
            </div>
            """, unsafe_allow_html=True)
            
    with tab2:
        st.markdown("### 📺 Curated Materials")
        resources = course_data.get('resources', [])
        if not resources:
            st.info("Additional resources are being curated.")
        else:
            r_cols = st.columns(2)
            for i, res in enumerate(resources):
                with r_cols[i % 2]:
                    icon = "🎥" if res['type'] == 'youtube' else "🔗"
                    color = "#ef4444" if res['type'] == 'youtube' else "#3b82f6"
                    st.markdown(f"""
                    <a href="{res['url']}" target="_blank" style="text-decoration: none; color: inherit;">
                        <div style="padding: 1.25rem; border: 1px solid #e2e8f0; border-radius: 12px; height: 100%; transition: all 0.2s; background: white;">
                             <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
                                <span style="font-size: 1.5rem; margin-right: 0.75rem; color: {color};">{icon}</span>
                                <h4 style="margin: 0; font-size: 1rem;">{res['title']}</h4>
                             </div>
                             <p style="margin: 0; color: #64748b; font-size: 0.9rem;">{res.get('description','Access external resource')}</p>
                        </div>
                    </a>
                    """, unsafe_allow_html=True)

    with tab_sim:
        st.info("💡 **Interactive Lab**: Modify parameters below to see real-time results.")
        # Wrapper for Simulation
        st.markdown('<div style="background: #fdfbf7; padding: 2rem; border-radius: 12px; border: 1px dashed #d97706;">', unsafe_allow_html=True)
        
        sim_func = SIMULATION_MAP.get(course_data['id'])
        if sim_func:
            try:
                sim_func()
            except Exception as e:
                st.error(f"Simulation Error: {e}")
        else:
            st.warning("⚠️ Simulation lab under construction.")
            
        st.markdown('</div>', unsafe_allow_html=True)

    with tab_exam:
        render_quiz(course_data)

if __name__ == "__main__":
    main()
