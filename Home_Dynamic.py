
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

    # Initialize Session State
    if 'selected_course_id' not in st.session_state:
        st.session_state.selected_course_id = None
        
    # --- HEADER ---
    st.markdown("""
    <style>
    .big-font { font-size: 1.2rem !important; }
    .course-card {
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        background-color: white;
        text-align: center;
        transition: transform 0.2s;
        height: 100%;
    }
    .course-card:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        border-color: #3b82f6;
    }
    </style>
    """, unsafe_allow_html=True)

    # --- SEMESTER SELECTION (Top Navigation) ---
    semesters = list(curriculum.keys())
    semesters.sort(key=lambda x: int(x.split(" ")[1]) if x.split(" ")[1].isdigit() else 99)
    
    col_nav1, col_nav2 = st.columns([1, 3])
    with col_nav1:
        st.image("https://img.icons8.com/fluency/96/console.png", width=60)
    with col_nav2:
        st.title("Computer Engineering Hub")
    
    # Semantic Semester Tabs
    selected_semester = st.selectbox("📅 Select Semester", semesters, index=0)
    
    # --- COURSE SELECTION (Grid Layout) ---
    courses = curriculum[selected_semester]
    
    st.markdown(f"### 📂 Courses in {selected_semester}")
    
    # Create a grid of buttons
    cols = st.columns(4) # 4 cards per row
    
    for idx, course in enumerate(courses):
        with cols[idx % 4]:
            # Use a container for card-like feel
            with st.container():
                # We use a button that updates session state
                is_selected = st.session_state.selected_course_id == course['id']
                btn_type = "primary" if is_selected else "secondary"
                
                if st.button(
                    f"{course['icon']}\n{course['id']}\n{course['name']}", 
                    key=f"btn_{course['id']}", 
                    use_container_width=True,
                    type=btn_type,
                    help=f"{course['credits']} Credits"
                ):
                    st.session_state.selected_course_id = course['id']

    st.markdown("---")

    # --- CONTENT RENDER ---
    # Find the data for the selected course (or default to first)
    active_course = next((c for c in courses if c['id'] == st.session_state.selected_course_id), None)
    
    if not active_course and courses:
        # Default to first if nothing selected or switched semester
        active_course = courses[0]
        st.session_state.selected_course_id = active_course['id']
        
    if active_course:
        render_course_content(active_course)

def render_course_content(course_data):
    """Renders the detailed content for a single course."""
    # Header
    st.markdown(f"""
    <div class="course-header" style="background: linear-gradient(90deg, #eff6ff 0%, #f8fafc 100%); padding: 1.5rem; border-radius: 12px; border-left: 6px solid #3b82f6;">
        <div style="font-size: 1rem; color: #64748b; font-weight: 600;">{course_data['id']} • {course_data['credits']} Credits</div>
        <div style="font-size: 2rem; font-weight: 800; color: #1e293b; margin: 0.5rem 0;">{course_data['name']}</div>
        <div style="display: flex; gap: 1rem; align-items: center;">
            <span style="background: white; padding: 4px 12px; border-radius: 20px; font-size: 0.9rem; border: 1px solid #cbd5e1;">⚡ Difficulty: {course_data['difficulty']}</span>
            <span style="background: white; padding: 4px 12px; border-radius: 20px; font-size: 0.9rem; border: 1px solid #cbd5e1;">⏱️ {course_data['hours']} hrs/week</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("") # Spacer
    
    # Tabs
    tab1, tab2, tab3 = st.tabs(["📚 Syllabus", "🧪 Simulation", "📺 Resources"])
    
    with tab1:
        col_desc, col_topic = st.columns([2, 1])
        with col_desc:
            st.markdown("#### Course Description")
            st.write(course_data['description'])
        with col_topic:
            st.markdown("#### 📋 Key Topics")
            for topic in course_data.get('topics', [])[:5]: # Show top 5
                st.markdown(f"• {topic}")
            if len(course_data.get('topics', [])) > 5:
                st.caption(f"...and {len(course_data['topics'])-5} more")
            
    with tab2:
        st.subheader(f"Interactive: {course_data['name']}")
        # Dynamic Dispatch
        simulation_func = SIMULATION_MAP.get(course_data['id'])
        if simulation_func:
            try:
                simulation_func()
            except Exception as e:
                st.error(f"Simulation Error: {e}")
        else:
            st.info("Simulation under development.")
            
    with tab3:
        st.subheader("Curated Resources")
        resources = course_data.get('resources', [])
        if not resources:
            st.info("No specific resources yet.")
        else:
            # Display resources in a neat grid
            r_cols = st.columns(2)
            for i, res in enumerate(resources):
                with r_cols[i % 2]:
                    icon = "📺" if res['type'] == 'youtube' else "🔗"
                    st.markdown(f"""
                    <div style="padding: 1rem; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 1rem;">
                        <strong><a href="{res['url']}" target="_blank" style="text-decoration: none; color: #2563eb;">{icon} {res['title']}</a></strong><br>
                        <span style="font-size: 0.9rem; color: #64748b;">{res.get('description','')}</span>
                    </div>
                    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
