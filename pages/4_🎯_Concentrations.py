import streamlit as st
import pandas as pd
import altair as alt
import sys
sys.path.append('.')

from data.concentrations import CONCENTRATIONS, SKILL_CATEGORIES, CONCENTRATION_COMPARISON

st.set_page_config(page_title="Concentrations", page_icon="🎯", layout="wide")

st.title("🎯 Concentration Comparison")
st.markdown("Compare Finance, IT, and Management specializations")

# Concentration selector
selected_concs = st.multiselect(
    "Select concentrations to compare",
    list(CONCENTRATIONS.keys()),
    default=list(CONCENTRATIONS.keys())
)

if not selected_concs:
    st.warning("Please select at least one concentration to view details")
    st.stop()

# Display concentration cards
cols = st.columns(len(selected_concs))

for idx, conc_key in enumerate(selected_concs):
    conc = CONCENTRATIONS[conc_key]
    
    with cols[idx]:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #8b5cf6 0%, #a855f7 100%); 
                    color: white; padding: 2rem; border-radius: 16px; text-align: center;">
            <h2 style="margin: 0; font-size: 1.5rem;">{conc['name']}</h2>
            <p style="margin-top: 0.5rem; opacity: 0.9;">{conc['total_credits']} Credits</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"**Description:**\n{conc['description']}")
        
        st.markdown(f"**💰 Salary Range:** {conc['average_salary']}")
        st.markdown(f"**📈 Job Growth:** {conc['job_growth']}")
        
        st.markdown("**🏢 Top Companies:**")
        for company in conc['top_companies'][:3]:
            st.markdown(f"- {company}")

# Skills Radar Chart
if len(selected_concs) > 0:
    st.markdown("---")
    st.markdown("### 📊 Skills Comparison")
    
    # Prepare data for radar chart
    radar_data = []
    for conc_key in selected_concs:
        conc = CONCENTRATIONS[conc_key]
        for skill, value in conc['skills'].items():
            radar_data.append({
                'concentration': conc_key,
                'skill': skill,
                'value': value
            })
    
    df_radar = pd.DataFrame(radar_data)
    
    # Create radar chart using Altair
    # Note: Altair doesn't have native radar charts, so we'll use a grouped bar chart
    radar_chart = alt.Chart(df_radar).mark_bar(
        cornerRadiusTopLeft=5,
        cornerRadiusTopRight=5
    ).encode(
        x=alt.X('skill:N', title='Skill Area'),
        y=alt.Y('value:Q', title='Proficiency Level (0-100)', scale=alt.Scale(domain=[0, 100])),
        color=alt.Color('concentration:N', title='Concentration'),
        xOffset='concentration:N',
        tooltip=['concentration', 'skill', 'value']
    ).properties(
        height=400
    )
    
    st.altair_chart(radar_chart, use_container_width=True)

# Career Paths
st.markdown("---")
st.markdown("### 💼 Career Paths")

for conc_key in selected_concs:
    conc = CONCENTRATIONS[conc_key]
    
    with st.expander(f"{conc['name']} - Career Opportunities", expanded=True):
        cols = st.columns(2)
        
        for idx, career in enumerate(conc['career_paths']):
            with cols[idx % 2]:
                st.markdown(f"✅ **{career}**")

# Comparison Matrix
if len(selected_concs) > 1:
    st.markdown("---")
    st.markdown("### 🔍 Detailed Comparison")
    
    # Prepare comparison data
    comparison_data = []
    for aspect, values in CONCENTRATION_COMPARISON.items():
        for conc in selected_concs:
            if conc in values:
                comparison_data.append({
                    'aspect': aspect,
                    'concentration': conc,
                    'score': values[conc]
                })
    
    df_comparison = pd.DataFrame(comparison_data)
    
    # Grouped bar chart
    comparison_chart = alt.Chart(df_comparison).mark_bar(
        cornerRadiusTopLeft=5,
        cornerRadiusTopRight=5
    ).encode(
        x=alt.X('aspect:N', title='Aspect'),
        y=alt.Y('score:Q', title='Score (0-100)', scale=alt.Scale(domain=[0, 100])),
        color=alt.Color('concentration:N', title='Concentration'),
        xOffset='concentration:N',
        tooltip=['aspect', 'concentration', 'score']
    ).properties(
        height=400
    )
    
    st.altair_chart(comparison_chart, use_container_width=True)

# Course Requirements
st.markdown("---")
st.markdown("### 📚 Required Courses by Concentration")

for conc_key in selected_concs:
    conc = CONCENTRATIONS[conc_key]
    
    with st.expander(f"{conc['name']} - Course Requirements"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Required Courses:**")
            for course_code in conc['required_courses']:
                st.markdown(f"- {course_code}")
        
        with col2:
            st.markdown("**Recommended Electives:**")
            for course_code in conc['elective_courses']:
                st.markdown(f"- {course_code}")

# Decision Helper
st.markdown("---")
st.markdown("### 🤔 Which Concentration is Right for You?")

quiz_col1, quiz_col2 = st.columns(2)

with quiz_col1:
    st.markdown("**Choose Finance if you:**")
    st.markdown("- Love mathematics and quantitative analysis")
    st.markdown("- Interested in financial markets and trading")
    st.markdown("- Want to work in fintech or banking")
    st.markdown("- Enjoy data analysis and modeling")

with quiz_col2:
    st.markdown("**Choose IT if you:**")
    st.markdown("- Passionate about cutting-edge technology")
    st.markdown("- Want to build scalable systems")
    st.markdown("- Interested in AI/ML and cloud computing")
    st.markdown("- Enjoy solving complex technical problems")

st.markdown("**Choose Management if you:**")
st.markdown("- Enjoy leading teams and projects")
st.markdown("- Want to bridge business and technology")
st.markdown("- Interested in strategy and operations")
st.markdown("- Aspire to executive leadership roles")

st.markdown("---")
st.info("💡 **Tip:** You can combine skills from multiple concentrations through elective courses!")
