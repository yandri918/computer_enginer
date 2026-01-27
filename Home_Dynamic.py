
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

    # --- MAIN CONTENT RENDER ---
    
    st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        font-weight: bold;
        padding: 1rem;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("## 🎓 Computer Engineering Curriculum")
    st.info("The interactive curriculum for Semesters 1-8 is now hosted on a dedicated high-performance instance.")

    st.markdown("### Access Full Curriculum")
    st.markdown("Click the button below to open the official application with all interactive simulations and resources.")

    st.markdown("""
    <div style="text-align: center; padding: 2rem;">
        <a href="https://computerenginer.streamlit.app/" target="_blank" style="
            background-color: #2563eb;
            color: white;
            padding: 1rem 2rem;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 1.2rem;
            display: inline-block;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: all 0.2s;
        ">
            🚀 Open App (computerenginer.streamlit.app)
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.caption("Powered by UTel University • AgriSensa API")

if __name__ == "__main__":
    main()
