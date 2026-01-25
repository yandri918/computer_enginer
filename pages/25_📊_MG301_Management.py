import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="MG301 - Management Concentration", page_icon="📊", layout="wide")

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    code, pre {
        font-family: 'JetBrains Mono', monospace !important;
    }
    
    .course-header {
        background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    .course-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .theory-box {
        background: linear-gradient(135deg, #ede9fe 0%, #ddd6fe 100%);
        border-left: 5px solid #8b5cf6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .agile-box {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .leadership-box {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .strategy-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .youtube-box {
        background: linear-gradient(135deg, #fee2e2 0%, #fecaca 100%);
        border-left: 5px solid #ef4444;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="course-header">
    <div style="font-size: 1.2rem; opacity: 0.9;">MG301</div>
    <div class="course-title">Concentration - Management</div>
    <div>📊 3 Credits | Semester 6 | Project Management & Leadership</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "6")
with col3:
    st.metric("Difficulty", "4/7")
with col4:
    st.metric("Hours/Week", "5")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "🏃 Agile Methodologies",
    "📋 Project Management",
    "👥 Team Leadership",
    "💼 Business Strategy",
    "🤝 Stakeholder Management",
    "📊 Metrics & KPIs",
    "🎯 Case Studies",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive study of IT project management, agile methodologies, and technical team leadership. Covers Scrum, 
        Kanban, project planning, risk management, team dynamics, business strategy alignment, and stakeholder communication. 
        Emphasizes practical application of management frameworks, leadership skills, and strategic thinking. Students will 
        manage IT projects, lead technical teams, implement agile practices, and align technology initiatives with business goals.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Manage IT projects using agile methodologies (Scrum, Kanban)",
        "Lead and motivate technical teams effectively",
        "Plan, execute, and monitor project deliverables",
        "Manage project risks, budgets, and timelines",
        "Facilitate agile ceremonies (standups, retrospectives, planning)",
        "Align IT initiatives with business strategy",
        "Communicate effectively with stakeholders",
        "Measure and improve team performance with KPIs"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Agile Methodologies:**
        - Scrum framework and roles
        - Kanban boards and WIP limits
        - Sprint planning and execution
        - Daily standups and retrospectives
        - User stories and acceptance criteria
        
        **Project Management:**
        - Project lifecycle (initiation to closure)
        - Work breakdown structure (WBS)
        - Gantt charts and critical path
        - Risk management
        - Budget and resource allocation
        """)
    
    with col2:
        st.markdown("""
        **Leadership & People:**
        - Team formation and dynamics
        - Motivation and engagement
        - Conflict resolution
        - Performance management
        - Coaching and mentoring
        
        **Business & Strategy:**
        - IT-business alignment
        - Value stream mapping
        - OKRs and goal setting
        - Change management
        - Digital transformation
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Scrum: The Art of Doing Twice the Work in Half the Time", "author": "Jeff Sutherland", "type": "Agile"},
        {"title": "The Lean Startup", "author": "Eric Ries", "type": "Strategy"},
        {"title": "Leaders Eat Last", "author": "Simon Sinek", "type": "Leadership"},
        {"title": "PMBOK Guide", "author": "PMI", "type": "Project Management"}
    ]
    
    for resource in resources:
        title = resource['title']
        author = resource['author']
        rtype = resource['type']
        st.markdown(f"📖 **{title}** by {author} ({rtype})")

# ==================== TAB 2: AGILE ====================
with tabs[1]:
    st.markdown("## 🏃 Agile Methodologies")
    
    st.markdown("### 1️⃣ Scrum Framework")
    
    st.markdown("""
    <div class="agile-box">
        <strong>Scrum Roles:</strong><br><br>
        
        <strong>Product Owner:</strong><br>
        • Defines product vision and roadmap<br>
        • Manages product backlog<br>
        • Prioritizes features and user stories<br>
        • Accepts or rejects work results<br>
        • Represents stakeholders and customers<br><br>
        
        <strong>Scrum Master:</strong><br>
        • Facilitates scrum ceremonies<br>
        • Removes impediments and blockers<br>
        • Coaches team on agile practices<br>
        • Protects team from distractions<br>
        • Promotes continuous improvement<br><br>
        
        <strong>Development Team:</strong><br>
        • Self-organizing and cross-functional<br>
        • 5-9 members (ideal size)<br>
        • Collectively responsible for deliverables<br>
        • Estimates and commits to work<br>
        • Delivers potentially shippable increments
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Scrum Ceremonies")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Sprint Planning (2-4 hours for 2-week sprint):</strong><br>
        • What: Select items from product backlog<br>
        • How: Break down into tasks<br>
        • Commitment: Team commits to sprint goal<br>
        • Output: Sprint backlog<br><br>
        
        <strong>Daily Standup (15 minutes):</strong><br>
        • What did I do yesterday?<br>
        • What will I do today?<br>
        • Any blockers or impediments?<br>
        • Time-boxed, same time/place<br>
        • Not a status report to manager<br><br>
        
        <strong>Sprint Review (1-2 hours):</strong><br>
        • Demo completed work to stakeholders<br>
        • Gather feedback<br>
        • Update product backlog<br>
        • Celebrate achievements<br><br>
        
        <strong>Sprint Retrospective (1-2 hours):</strong><br>
        • What went well?<br>
        • What could be improved?<br>
        • Action items for next sprint<br>
        • Team-only meeting<br>
        • Focus on process improvement
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Kanban")
    
    st.markdown("""
    <div class="agile-box">
        <strong>Kanban Principles:</strong><br>
        • Visualize workflow<br>
        • Limit work in progress (WIP)<br>
        • Manage flow<br>
        • Make policies explicit<br>
        • Continuous improvement<br><br>
        
        <strong>Kanban Board Columns:</strong><br>
        • Backlog → To Do → In Progress → Code Review → Testing → Done<br>
        • Customize based on team workflow<br>
        • WIP limits per column (e.g., max 3 items in progress)<br><br>
        
        <strong>Metrics:</strong><br>
        • <strong>Lead Time:</strong> Time from request to delivery<br>
        • <strong>Cycle Time:</strong> Time from start to finish<br>
        • <strong>Throughput:</strong> Items completed per time period<br>
        • <strong>WIP:</strong> Number of items in progress<br><br>
        
        <strong>Scrum vs Kanban:</strong><br>
        • Scrum: Fixed-length sprints, prescribed roles<br>
        • Kanban: Continuous flow, flexible roles<br>
        • Scrumban: Hybrid approach
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 4️⃣ User Stories")
    
    st.markdown("""
    <div class="theory-box">
        <strong>User Story Format:</strong><br>
        "As a [user role], I want [goal/desire] so that [benefit/value]"<br><br>
        
        <strong>Example:</strong><br>
        "As a customer, I want to save my shopping cart so that I can complete my purchase later"<br><br>
        
        <strong>INVEST Criteria:</strong><br>
        • <strong>Independent:</strong> Can be developed separately<br>
        • <strong>Negotiable:</strong> Details can be discussed<br>
        • <strong>Valuable:</strong> Provides value to user<br>
        • <strong>Estimable:</strong> Can be estimated<br>
        • <strong>Small:</strong> Fits in one sprint<br>
        • <strong>Testable:</strong> Has clear acceptance criteria<br><br>
        
        <strong>Acceptance Criteria:</strong><br>
        Given [context], When [action], Then [outcome]<br><br>
        
        <strong>Story Points:</strong><br>
        • Relative sizing (Fibonacci: 1, 2, 3, 5, 8, 13)<br>
        • Planning poker for estimation<br>
        • Velocity: Average story points per sprint
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: PROJECT MANAGEMENT ====================
with tabs[2]:
    st.markdown("## 📋 Project Management")
    
    st.markdown("### 1️⃣ Project Lifecycle")
    
    st.markdown("""
    <div class="theory-box">
        <strong>1. Initiation:</strong><br>
        • Define project charter<br>
        • Identify stakeholders<br>
        • Establish business case<br>
        • Get project approval<br><br>
        
        <strong>2. Planning:</strong><br>
        • Define scope and requirements<br>
        • Create work breakdown structure (WBS)<br>
        • Develop schedule and budget<br>
        • Identify risks<br>
        • Plan resources and communication<br><br>
        
        <strong>3. Execution:</strong><br>
        • Assign tasks to team members<br>
        • Manage resources<br>
        • Communicate with stakeholders<br>
        • Ensure quality<br><br>
        
        <strong>4. Monitoring & Control:</strong><br>
        • Track progress against plan<br>
        • Manage changes<br>
        • Control costs and schedule<br>
        • Report status<br><br>
        
        <strong>5. Closure:</strong><br>
        • Deliver final product<br>
        • Document lessons learned<br>
        • Release resources<br>
        • Celebrate success
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Risk Management")
    
    st.markdown("""
    <div class="agile-box">
        <strong>Risk Management Process:</strong><br><br>
        
        <strong>1. Identify Risks:</strong><br>
        • Brainstorming sessions<br>
        • SWOT analysis<br>
        • Historical data<br>
        • Expert judgment<br><br>
        
        <strong>2. Assess Risks:</strong><br>
        • Probability (Low, Medium, High)<br>
        • Impact (Low, Medium, High)<br>
        • Risk Score = Probability × Impact<br>
        • Prioritize high-score risks<br><br>
        
        <strong>3. Plan Responses:</strong><br>
        • <strong>Avoid:</strong> Eliminate the risk<br>
        • <strong>Mitigate:</strong> Reduce probability or impact<br>
        • <strong>Transfer:</strong> Shift to third party (insurance)<br>
        • <strong>Accept:</strong> Acknowledge and monitor<br><br>
        
        <strong>4. Monitor Risks:</strong><br>
        • Track identified risks<br>
        • Identify new risks<br>
        • Execute response plans<br>
        • Update risk register
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Project Tools")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Project Management Software:</strong><br>
        • <strong>Jira:</strong> Agile project management, issue tracking<br>
        • <strong>Asana:</strong> Task management, workflows<br>
        • <strong>Trello:</strong> Kanban boards, simple and visual<br>
        • <strong>Monday.com:</strong> Customizable workflows<br>
        • <strong>Microsoft Project:</strong> Traditional project management<br><br>
        
        <strong>Collaboration Tools:</strong><br>
        • <strong>Slack:</strong> Team communication<br>
        • <strong>Microsoft Teams:</strong> Chat, meetings, files<br>
        • <strong>Confluence:</strong> Documentation and knowledge base<br>
        • <strong>Miro:</strong> Virtual whiteboard<br><br>
        
        <strong>Version Control:</strong><br>
        • <strong>Git/GitHub:</strong> Code repository<br>
        • <strong>GitLab:</strong> DevOps platform<br>
        • <strong>Bitbucket:</strong> Atlassian's Git solution
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: LEADERSHIP ====================
with tabs[3]:
    st.markdown("## 👥 Team Leadership")
    
    st.markdown("### 1️⃣ Team Development")
    
    st.markdown("""
    <div class="leadership-box">
        <strong>Tuckman's Stages of Team Development:</strong><br><br>
        
        <strong>1. Forming:</strong><br>
        • Team members get to know each other<br>
        • Polite and positive<br>
        • Unclear roles and responsibilities<br>
        • Leader provides direction<br><br>
        
        <strong>2. Storming:</strong><br>
        • Conflicts and competition emerge<br>
        • Frustration with tasks and team members<br>
        • Power struggles<br>
        • Leader facilitates conflict resolution<br><br>
        
        <strong>3. Norming:</strong><br>
        • Team establishes norms and processes<br>
        • Roles clarified<br>
        • Increased collaboration<br>
        • Leader steps back, team self-organizes<br><br>
        
        <strong>4. Performing:</strong><br>
        • High productivity and efficiency<br>
        • Team works autonomously<br>
        • Focus on goals<br>
        • Leader delegates and empowers<br><br>
        
        <strong>5. Adjourning:</strong><br>
        • Project completion<br>
        • Team disbands<br>
        • Celebrate achievements<br>
        • Document lessons learned
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Leadership Styles")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Situational Leadership:</strong><br>
        Adapt style based on team maturity and task complexity<br><br>
        
        <strong>Directive (Telling):</strong><br>
        • High task focus, low relationship focus<br>
        • Clear instructions and close supervision<br>
        • For new or inexperienced team members<br><br>
        
        <strong>Coaching (Selling):</strong><br>
        • High task and relationship focus<br>
        • Explain decisions and provide guidance<br>
        • For developing team members<br><br>
        
        <strong>Supporting (Participating):</strong><br>
        • Low task, high relationship focus<br>
        • Facilitate and support decisions<br>
        • For competent but less confident members<br><br>
        
        <strong>Delegating:</strong><br>
        • Low task and relationship focus<br>
        • Empower team to make decisions<br>
        • For highly skilled and motivated members
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Motivation")
    
    st.markdown("""
    <div class="leadership-box">
        <strong>Intrinsic Motivation (Daniel Pink):</strong><br><br>
        
        <strong>Autonomy:</strong><br>
        • Freedom to choose how to do work<br>
        • Self-directed teams<br>
        • Flexible work arrangements<br><br>
        
        <strong>Mastery:</strong><br>
        • Opportunity to improve skills<br>
        • Challenging but achievable goals<br>
        • Learning and development<br><br>
        
        <strong>Purpose:</strong><br>
        • Meaningful work<br>
        • Connection to larger mission<br>
        • Impact on users and society<br><br>
        
        <strong>Recognition:</strong><br>
        • Acknowledge achievements<br>
        • Public praise<br>
        • Celebrate wins (big and small)<br>
        • Peer recognition programs
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Conflict Resolution")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Thomas-Kilmann Conflict Modes:</strong><br><br>
        
        <strong>Competing (Assertive, Uncooperative):</strong><br>
        • Win-lose approach<br>
        • Use when quick decision needed<br>
        • Can damage relationships<br><br>
        
        <strong>Collaborating (Assertive, Cooperative):</strong><br>
        • Win-win approach<br>
        • Find mutually beneficial solution<br>
        • Time-consuming but best long-term<br><br>
        
        <strong>Compromising (Moderate):</strong><br>
        • Both parties give up something<br>
        • Quick resolution<br>
        • May not fully satisfy either party<br><br>
        
        <strong>Avoiding (Unassertive, Uncooperative):</strong><br>
        • Postpone or ignore conflict<br>
        • Use for trivial issues<br>
        • Can escalate if not addressed<br><br>
        
        <strong>Accommodating (Unassertive, Cooperative):</strong><br>
        • Yield to others<br>
        • Preserve relationships<br>
        • Use when issue more important to others
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: BUSINESS STRATEGY ====================
with tabs[4]:
    st.markdown("## 💼 Business Strategy")
    
    st.markdown("### 1️⃣ IT-Business Alignment")
    
    st.markdown("""
    <div class="strategy-box">
        <strong>Strategic Alignment Model:</strong><br>
        • Business strategy drives IT strategy<br>
        • IT capabilities enable business innovation<br>
        • Organizational infrastructure supports both<br><br>
        
        <strong>Value Proposition:</strong><br>
        • How does IT create business value?<br>
        • Cost reduction vs revenue generation<br>
        • Operational efficiency vs innovation<br>
        • Customer experience improvement<br><br>
        
        <strong>Digital Transformation:</strong><br>
        • Cloud migration<br>
        • Data-driven decision making<br>
        • Automation and AI<br>
        • Customer-centric digital experiences<br>
        • Agile and DevOps adoption
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ OKRs (Objectives and Key Results)")
    
    st.markdown("""
    <div class="theory-box">
        <strong>OKR Framework:</strong><br><br>
        
        <strong>Objective:</strong><br>
        • Qualitative, inspirational goal<br>
        • What you want to achieve<br>
        • Time-bound (quarterly or annually)<br><br>
        
        <strong>Key Results:</strong><br>
        • Quantitative, measurable outcomes<br>
        • How you know you've achieved objective<br>
        • 3-5 key results per objective<br><br>
        
        <strong>Example:</strong><br>
        <strong>Objective:</strong> Improve customer satisfaction<br>
        <strong>Key Results:</strong><br>
        • Increase NPS score from 30 to 50<br>
        • Reduce average response time from 24h to 4h<br>
        • Achieve 95% customer retention rate<br><br>
        
        <strong>Best Practices:</strong><br>
        • Align team OKRs with company OKRs<br>
        • Make OKRs public and transparent<br>
        • Review progress weekly<br>
        • Aim for 70% achievement (stretch goals)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Change Management")
    
    st.markdown("""
    <div class="strategy-box">
        <strong>Kotter's 8-Step Change Model:</strong><br><br>
        
        1. <strong>Create Urgency:</strong> Explain why change is needed<br>
        2. <strong>Build Coalition:</strong> Assemble team of change agents<br>
        3. <strong>Form Vision:</strong> Clear picture of future state<br>
        4. <strong>Communicate Vision:</strong> Share widely and often<br>
        5. <strong>Remove Obstacles:</strong> Eliminate barriers to change<br>
        6. <strong>Create Quick Wins:</strong> Show early successes<br>
        7. <strong>Build on Change:</strong> Don't declare victory too soon<br>
        8. <strong>Anchor in Culture:</strong> Make change stick<br><br>
        
        <strong>Resistance to Change:</strong><br>
        • Fear of unknown<br>
        • Loss of control<br>
        • Lack of understanding<br>
        • Address through communication and involvement
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: STAKEHOLDER MANAGEMENT ====================
with tabs[5]:
    st.markdown("## 🤝 Stakeholder Management")
    
    st.markdown("### 1️⃣ Stakeholder Analysis")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Power-Interest Grid:</strong><br><br>
        
        <strong>High Power, High Interest (Manage Closely):</strong><br>
        • Key decision makers<br>
        • Frequent communication<br>
        • Involve in planning<br>
        • Example: Executive sponsor, product owner<br><br>
        
        <strong>High Power, Low Interest (Keep Satisfied):</strong><br>
        • Can influence but not engaged<br>
        • Regular updates<br>
        • Don't overwhelm with details<br>
        • Example: Senior executives<br><br>
        
        <strong>Low Power, High Interest (Keep Informed):</strong><br>
        • Affected by project but limited influence<br>
        • Regular communication<br>
        • Address concerns<br>
        • Example: End users, team members<br><br>
        
        <strong>Low Power, Low Interest (Monitor):</strong><br>
        • Minimal engagement<br>
        • Periodic updates<br>
        • Example: Peripheral stakeholders
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Communication Planning")
    
    st.markdown("""
    <div class="agile-box">
        <strong>Communication Matrix:</strong><br>
        Define who needs what information, when, and how<br><br>
        
        <strong>Stakeholder Communication Preferences:</strong><br>
        • <strong>Executives:</strong> High-level dashboards, monthly<br>
        • <strong>Product Owner:</strong> Daily standups, sprint reviews<br>
        • <strong>Team:</strong> Daily standups, Slack, documentation<br>
        • <strong>Customers:</strong> Release notes, feature announcements<br><br>
        
        <strong>Communication Channels:</strong><br>
        • <strong>Synchronous:</strong> Meetings, calls, video conferences<br>
        • <strong>Asynchronous:</strong> Email, Slack, documentation<br>
        • <strong>Formal:</strong> Status reports, presentations<br>
        • <strong>Informal:</strong> Hallway conversations, coffee chats
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: METRICS ====================
with tabs[6]:
    st.markdown("## 📊 Metrics & KPIs")
    
    st.markdown("### 1️⃣ Agile Metrics")
    
    metrics_data = {
        'Metric': ['Velocity', 'Sprint Burndown', 'Cumulative Flow', 'Cycle Time', 'Lead Time'],
        'Description': [
            'Story points completed per sprint',
            'Work remaining in sprint',
            'Work items in each stage over time',
            'Time from start to finish',
            'Time from request to delivery'
        ],
        'Use Case': [
            'Capacity planning',
            'Sprint progress tracking',
            'Identify bottlenecks',
            'Process efficiency',
            'Customer satisfaction'
        ]
    }
    
    df_metrics = pd.DataFrame(metrics_data)
    st.dataframe(df_metrics, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Team Performance KPIs")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Productivity Metrics:</strong><br>
        • <strong>Throughput:</strong> Features delivered per sprint<br>
        • <strong>Deployment Frequency:</strong> How often code is deployed<br>
        • <strong>Code Quality:</strong> Bug rate, code coverage, technical debt<br><br>
        
        <strong>Quality Metrics:</strong><br>
        • <strong>Defect Density:</strong> Bugs per 1000 lines of code<br>
        • <strong>Escaped Defects:</strong> Bugs found in production<br>
        • <strong>Test Coverage:</strong> % of code covered by tests<br><br>
        
        <strong>Engagement Metrics:</strong><br>
        • <strong>Employee Satisfaction:</strong> Regular surveys<br>
        • <strong>Retention Rate:</strong> % of team members staying<br>
        • <strong>Absenteeism:</strong> Unplanned absences<br><br>
        
        <strong>DORA Metrics (DevOps):</strong><br>
        • Deployment Frequency<br>
        • Lead Time for Changes<br>
        • Mean Time to Recovery (MTTR)<br>
        • Change Failure Rate
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: CASE STUDIES ====================
with tabs[7]:
    st.markdown("## 🎯 Case Studies")
    
    case_studies = [
        {
            "title": "Case Study 1: Implementing Scrum in Legacy Team",
            "description": "Transform waterfall team to agile Scrum methodology",
            "details": """
**Situation:**
- 15-person development team using waterfall
- 6-month release cycles
- Low morale, high defect rate
- Slow response to market changes

**Challenge:**
- Resistance to change from senior developers
- Lack of agile experience
- Existing long-term commitments
- Management skepticism

**Approach:**
1. **Education:** Agile training for entire team
2. **Pilot:** Start with one small project
3. **Coaching:** Hire experienced Scrum Master
4. **Incremental:** Gradual adoption, not big bang
5. **Metrics:** Track velocity, quality, satisfaction

**Implementation:**
- Week 1-2: Agile training and team building
- Week 3: First sprint planning (2-week sprints)
- Daily standups at 9:30 AM
- Sprint reviews with stakeholders
- Retrospectives for continuous improvement
            """,
            "solution": """
**Results After 6 Months:**

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Release Frequency | 6 months | 2 weeks | 12x faster |
| Defect Rate | 15% | 5% | 67% reduction |
| Team Satisfaction | 3.2/5 | 4.5/5 | 41% increase |
| Time to Market | 180 days | 30 days | 83% reduction |

**Key Success Factors:**
- Executive sponsorship and support
- Dedicated Scrum Master
- Protected sprint time (no interruptions)
- Celebrating early wins
- Continuous learning culture

**Lessons Learned:**
- Change takes time, be patient
- Not all team members will adapt
- Start small, scale gradually
- Metrics help demonstrate value
- Retrospectives are crucial for improvement
            """
        },
        {
            "title": "Case Study 2: Managing Distributed Team",
            "description": "Lead remote team across 3 time zones",
            "details": """
**Situation:**
- Team of 12 developers across US, Europe, Asia
- 3 different time zones (8-hour difference)
- Cultural and language differences
- Coordination challenges

**Challenges:**
- Limited overlap in working hours
- Communication barriers
- Building team cohesion
- Ensuring accountability

**Solutions Implemented:**

**1. Communication:**
- Slack for async communication
- Zoom for video meetings
- Confluence for documentation
- Weekly all-hands at overlapping time

**2. Processes:**
- Asynchronous standups (written updates)
- Rotating meeting times (fair to all zones)
- Clear documentation of decisions
- Recorded meetings for those who can't attend

**3. Tools:**
- Jira for task tracking
- GitHub for code collaboration
- Miro for virtual whiteboarding
- Loom for video updates

**4. Culture:**
- Virtual coffee chats
- Celebrate cultural holidays
- Annual in-person meetup
- Buddy system for new members
            """,
            "solution": """
**Results:**

**Productivity:**
- 24-hour development cycle (follow the sun)
- Faster issue resolution
- Increased code review quality

**Team Satisfaction:**
- 4.3/5 team happiness score
- 95% retention rate
- Strong sense of belonging

**Best Practices:**
- Over-communicate in writing
- Assume positive intent
- Be mindful of time zones
- Use video for important discussions
- Document everything
- Build personal connections

**Tools That Worked:**
- ✅ Slack (async communication)
- ✅ Zoom (video meetings)
- ✅ Confluence (documentation)
- ✅ Jira (project tracking)
- ✅ Donut (random coffee chats)

**Challenges Overcome:**
- Time zone coordination through rotating meetings
- Cultural differences through education and respect
- Isolation through virtual social events
- Accountability through clear expectations and trust
            """
        }
    ]
    
    for idx, case in enumerate(case_studies, 1):
        with st.expander(f"📝 {case['title']}", expanded=False):
            st.markdown(f"**Description:** {case['description']}")
            st.markdown(case['details'])
            
            if st.button(f"Show Solution", key=f"case_{idx}"):
                st.markdown("### Solution")
                st.markdown(case['solution'])

# ==================== TAB 9: YOUTUBE ====================
with tabs[8]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning Project Management and Leadership</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {"title": "Agile Project Management", "channel": "Simplilearn", "url": "https://www.youtube.com/watch?v=thsFsPnUHRA", "description": "Complete agile course", "duration": "~4 hours"},
        {"title": "Scrum in 20 Minutes", "channel": "Axosoft", "url": "https://www.youtube.com/watch?v=SWDhGSZNF9M", "description": "Quick Scrum overview", "duration": "20 min"},
        {"title": "Leadership Skills", "channel": "The Futur", "url": "https://www.youtube.com/c/thefutur", "description": "Leadership and business", "duration": "Channel"}
    ]
    
    for resource in beginner_resources:
        title = resource['title']
        channel = resource['channel']
        url = resource['url']
        description = resource['description']
        duration = resource['duration']
        st.markdown(f"**[{title}]({url})**  \n📺 Channel: {channel} | ⏱️ {duration}  \n{description}")
        st.markdown("---")
    
    # Intermediate Level
    st.markdown("### 🟡 Intermediate Level")
    
    intermediate_resources = [
        {"title": "Scrum Master Training", "channel": "Agile Academy", "url": "https://www.youtube.com/c/AgileAcademy", "description": "Professional Scrum training", "duration": "Channel"},
        {"title": "Project Management Professional", "channel": "Edureka", "url": "https://www.youtube.com/watch?v=vzqDTSZOTic", "description": "PMP certification prep", "duration": "~8 hours"},
        {"title": "OKRs Explained", "channel": "What Matters", "url": "https://www.youtube.com/c/WhatMatters", "description": "OKR framework", "duration": "Channel"}
    ]
    
    for resource in intermediate_resources:
        title = resource['title']
        channel = resource['channel']
        url = resource['url']
        description = resource['description']
        duration = resource['duration']
        st.markdown(f"**[{title}]({url})**  \n📺 Channel: {channel} | ⏱️ {duration}  \n{description}")
        st.markdown("---")
    
    # Advanced Level
    st.markdown("### 🔴 Advanced Level")
    
    advanced_resources = [
        {"title": "Agile at Scale", "channel": "Scaled Agile", "url": "https://www.youtube.com/c/ScaledAgileInc", "description": "SAFe framework", "duration": "Channel"},
        {"title": "Leadership Talks", "channel": "Simon Sinek", "url": "https://www.youtube.com/c/SimonSinek", "description": "Inspirational leadership", "duration": "Channel"},
        {"title": "Product Management", "channel": "Product School", "url": "https://www.youtube.com/c/ProductSchool", "description": "Product leadership", "duration": "Channel"}
    ]
    
    for resource in advanced_resources:
        title = resource['title']
        channel = resource['channel']
        url = resource['url']
        description = resource['description']
        duration = resource['duration']
        st.markdown(f"**[{title}]({url})**  \n📺 Channel: {channel} | ⏱️ {duration}  \n{description}")
        st.markdown("---")
    
    # Study Tips
    st.markdown("### 💡 Study Tips")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Recommended Learning Path:</strong><br>
        1. Understand agile principles and values<br>
        2. Learn Scrum framework thoroughly<br>
        3. Practice facilitation skills<br>
        4. Study leadership and motivation theories<br>
        5. Develop communication skills<br>
        6. Learn project management tools (Jira, Asana)<br>
        7. Get certified (CSM, PMP, SAFe)<br>
        8. Lead real projects and teams<br><br>
        
        <strong>Certifications:</strong><br>
        • <strong>Scrum:</strong> CSM (Certified Scrum Master), PSM (Professional Scrum Master)<br>
        • <strong>Project Management:</strong> PMP (Project Management Professional), CAPM<br>
        • <strong>Agile:</strong> PMI-ACP (Agile Certified Practitioner)<br>
        • <strong>SAFe:</strong> SAFe Agilist, SAFe Scrum Master<br>
        • <strong>Product:</strong> CSPO (Certified Scrum Product Owner)<br><br>
        
        <strong>Career Paths:</strong><br>
        • Scrum Master / Agile Coach<br>
        • IT Project Manager<br>
        • Product Manager<br>
        • Technical Lead / Engineering Manager<br>
        • Program Manager<br>
        • Director of Engineering
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>MG301 - Management Concentration</strong><br>
    <small>UTel University | Computer Engineering Program</small>
</div>
""", unsafe_allow_html=True)
