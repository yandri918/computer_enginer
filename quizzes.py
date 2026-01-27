import streamlit as st
import time

def render_quiz(course_data):
    """Renders a mock exam/quiz for the given course."""
    
    st.markdown(f"### 📝 {course_data['name']} - Final Exam")
    st.caption("Pass this exam to earn your certificate.")
    
    # Initialize Quiz State
    quiz_key = f"quiz_{course_data['id']}_started"
    if quiz_key not in st.session_state:
        st.session_state[quiz_key] = False
        
    if not st.session_state[quiz_key]:
        st.info("Time Limit: 30 Minutes • Questions: 5 • Passing Score: 80%")
        if st.button("Start Exam", key=f"start_{course_data['id']}", type="primary"):
            st.session_state[quiz_key] = True
            st.rerun()
    else:
        # Mock Questions Repository (Generic for demo purposes)
        # In a real app, this would come from a database based on course_id
        questions = [
            {
                "q": "What is a primary concept covered in this course?",
                "options": ["The core principles defined in the syllabus", "Cooking recipes", "Ancient history", "Sports analytics"],
                "correct": "The core principles defined in the syllabus"
            },
            {
                "q": "Which of the following is crucial for success in this field?",
                "options": ["Random guessing", "Critical thinking and application", "Ignoring documentation", "Working in isolation"],
                "correct": "Critical thinking and application"
            },
            {
                "q": "In the context of " + course_data['name'] + ", what does the term 'Scalability' imply?",
                "options": ["Making things heavier", "Handling growth efficiently", "Reducing performance", "Fixed size constraints"],
                "correct": "Handling growth efficiently"
            },
             {
                "q": "What is the industry standard approach for error handling?",
                "options": ["Ignore all errors", "Print to console only", "Graceful degradation and logging", "Crash the application"],
                "correct": "Graceful degradation and logging"
            },
            {
                "q": "Why is continuous learning important in " + course_data['name'] + "?",
                "options": ["Technology evolves rapidly", "It is required by law", "To pass time", "It is not important"],
                "correct": "Technology evolves rapidly"
            }
        ]
        
        # Render Form
        with st.form(key=f"exam_form_{course_data['id']}"):
            score = 0
            user_answers = {}
            
            for i, q in enumerate(questions):
                st.markdown(f"**{i+1}. {q['q']}**")
                user_answers[i] = st.radio(f"Select answer for Q{i+1}", q['options'], key=f"q_{course_data['id']}_{i}", label_visibility="collapsed")
                st.divider()
                
            submitted = st.form_submit_button("Submit Exam")
            
            if submitted:
                # Calculate Score
                correct_count = 0
                for i, q in enumerate(questions):
                    if user_answers[i] == q['correct']:
                        correct_count += 1
                
                final_score = (correct_count / len(questions)) * 100
                
                if final_score >= 80:
                    st.balloons()
                    st.success(f"🎉 Congratulations! You Passed! Score: {final_score:.0f}%")
                    
                    # Certificate Mockup
                    st.markdown("""
                    <div style="padding: 20px; background-color: #f0fdf4; border: 2px solid #16a34a; border-radius: 10px; text-align: center; margin-top: 20px;">
                        <h2 style="color: #166534; margin:0;">CERTIFICATE OF COMPLETION</h2>
                        <p style="color: #15803d;">This certifies that</p>
                        <h3 style="color: #1e293b;">Student User</h3>
                        <p>has successfully completed the course</p>
                        <h3 style="color: #1e293b;">""" + course_data['name'] + """</h3>
                        <p style="font-size: 0.8rem; color: #64748b;">Verified by UTel University • AgriSensa API</p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error(f"Score: {final_score:.0f}%. You did not pass. Please try again.")
