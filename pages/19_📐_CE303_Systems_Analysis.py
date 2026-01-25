import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="CE303 - Systems Analysis and Design", page_icon="📐", layout="wide")

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
        background: linear-gradient(135deg, #ec4899 0%, #db2777 100%);
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
        background: linear-gradient(135deg, #fce7f3 0%, #fbcfe8 100%);
        border-left: 5px solid #ec4899;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .methodology-box {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .design-box {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .pattern-box {
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
    <div style="font-size: 1.2rem; opacity: 0.9;">CE303</div>
    <div class="course-title">Systems Analysis and Design</div>
    <div>📐 3 Credits | Semester 4 | Software Engineering</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "4")
with col3:
    st.metric("Difficulty", "5/7")
with col4:
    st.metric("Hours/Week", "7")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "🔄 SDLC Methodologies",
    "📋 Requirements Engineering",
    "📊 UML Diagrams",
    "🏗️ System Design",
    "🎨 Design Patterns",
    "🗄️ Database Design",
    "🧪 Testing & Quality",
    "🎯 Case Studies",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive study of systems analysis and design methodologies for developing information systems. Covers 
        Software Development Life Cycle (SDLC), requirements engineering, system modeling using UML, database design, 
        software architecture, and design patterns. Emphasizes both structured and object-oriented approaches. Students 
        will analyze business requirements, design system solutions, and create comprehensive system documentation.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Understand SDLC methodologies (Waterfall, Agile, Scrum)",
        "Conduct requirements analysis and elicitation",
        "Create UML diagrams (Use Case, Class, Sequence, Activity)",
        "Design system architecture and components",
        "Apply design patterns to solve common problems",
        "Design normalized database schemas",
        "Develop test plans and quality assurance strategies",
        "Manage software projects effectively"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Fundamentals:**
        - Systems development life cycle
        - Feasibility analysis
        - Requirements gathering techniques
        - Stakeholder analysis
        - Project management basics
        
        **Analysis:**
        - Functional vs non-functional requirements
        - Use case modeling
        - Data flow diagrams (DFD)
        - Entity-relationship diagrams (ERD)
        - Process modeling
        """)
    
    with col2:
        st.markdown("""
        **Design:**
        - System architecture patterns
        - Component design
        - Interface design
        - Database normalization
        - Security design
        
        **Advanced Topics:**
        - Design patterns (GoF)
        - Microservices architecture
        - API design
        - DevOps integration
        - Cloud-native design
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Systems Analysis and Design", "author": "Dennis, Wixom & Roth", "type": "Textbook"},
        {"title": "Design Patterns", "author": "Gang of Four (GoF)", "type": "Classic"},
        {"title": "Clean Architecture", "author": "Robert C. Martin", "type": "Modern"},
        {"title": "Domain-Driven Design", "author": "Eric Evans", "type": "Advanced"}
    ]
    
    
    
    for resource in resources:
        title = resource['title']
        author = resource['author']
        rtype = resource['type']
        st.markdown(f"📖 **{title}** by {author} ({rtype})")

# ==================== TAB 2: SDLC ====================
with tabs[1]:
    st.markdown("## 🔄 SDLC Methodologies")
    
    st.markdown("### 1️⃣ Waterfall Model")
    
    st.markdown("""
    <div class="methodology-box">
        <strong>Sequential Phases:</strong><br><br>
        
        1. <strong>Requirements:</strong> Gather and document all requirements<br>
        2. <strong>Design:</strong> Create system architecture and detailed design<br>
        3. <strong>Implementation:</strong> Code the system<br>
        4. <strong>Testing:</strong> Verify system meets requirements<br>
        5. <strong>Deployment:</strong> Release to production<br>
        6. <strong>Maintenance:</strong> Fix bugs and add enhancements<br><br>
        
        <strong>Advantages:</strong><br>
        • Simple and easy to understand<br>
        • Well-documented<br>
        • Works well for small, well-defined projects<br><br>
        
        <strong>Disadvantages:</strong><br>
        • Inflexible to changes<br>
        • Late testing phase<br>
        • No working software until late<br>
        • High risk for complex projects
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Agile Methodology")
    
    st.markdown("""
    <div class="methodology-box">
        <strong>Agile Principles:</strong><br><br>
        
        • Individuals and interactions over processes and tools<br>
        • Working software over comprehensive documentation<br>
        • Customer collaboration over contract negotiation<br>
        • Responding to change over following a plan<br><br>
        
        <strong>Characteristics:</strong><br>
        • Iterative and incremental<br>
        • Short development cycles (sprints)<br>
        • Continuous feedback<br>
        • Adaptive planning<br>
        • Self-organizing teams<br><br>
        
        <strong>Popular Frameworks:</strong><br>
        • <strong>Scrum:</strong> Sprints, daily standups, retrospectives<br>
        • <strong>Kanban:</strong> Visual workflow, WIP limits<br>
        • <strong>XP (Extreme Programming):</strong> Pair programming, TDD<br>
        • <strong>SAFe:</strong> Scaled Agile for enterprises
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ SDLC Comparison")
    
    sdlc_comparison = {
        'Aspect': ['Approach', 'Flexibility', 'Customer Involvement', 'Documentation', 'Risk', 'Best For'],
        'Waterfall': [
            'Sequential',
            'Low',
            'Beginning only',
            'Heavy',
            'High',
            'Small, well-defined projects'
        ],
        'Agile': [
            'Iterative',
            'High',
            'Continuous',
            'Light',
            'Low',
            'Complex, evolving projects'
        ],
        'Spiral': [
            'Risk-driven',
            'Medium',
            'Regular',
            'Medium',
            'Very Low',
            'Large, high-risk projects'
        ]
    }
    
    df_sdlc = pd.DataFrame(sdlc_comparison)
    st.dataframe(df_sdlc, use_container_width=True)

# ==================== TAB 3: REQUIREMENTS ====================
with tabs[2]:
    st.markdown("## 📋 Requirements Engineering")
    
    st.markdown("### 1️⃣ Types of Requirements")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Functional Requirements:</strong><br>
        • What the system should do<br>
        • Specific behaviors and functions<br>
        • Examples:<br>
        &nbsp;&nbsp;- User shall be able to login with email and password<br>
        &nbsp;&nbsp;- System shall generate monthly sales reports<br>
        &nbsp;&nbsp;- Application shall send email notifications<br><br>
        
        <strong>Non-Functional Requirements:</strong><br>
        • How the system should perform<br>
        • Quality attributes<br><br>
        
        <strong>Categories:</strong><br>
        • <strong>Performance:</strong> Response time < 2 seconds<br>
        • <strong>Scalability:</strong> Support 10,000 concurrent users<br>
        • <strong>Security:</strong> Encrypt all sensitive data<br>
        • <strong>Usability:</strong> 90% tasks completed without help<br>
        • <strong>Reliability:</strong> 99.9% uptime<br>
        • <strong>Maintainability:</strong> Modular, well-documented code<br>
        • <strong>Portability:</strong> Run on Windows, Mac, Linux
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Requirements Elicitation Techniques")
    
    st.markdown("""
    <div class="methodology-box">
        <strong>1. Interviews:</strong><br>
        • One-on-one or group sessions<br>
        • Structured or unstructured<br>
        • Good for detailed information<br><br>
        
        <strong>2. Questionnaires/Surveys:</strong><br>
        • Reach many stakeholders<br>
        • Quantitative data<br>
        • Less detailed than interviews<br><br>
        
        <strong>3. Observation:</strong><br>
        • Watch users in their environment<br>
        • Discover unstated requirements<br>
        • Time-consuming<br><br>
        
        <strong>4. Document Analysis:</strong><br>
        • Review existing documentation<br>
        • Understand current system<br>
        • Identify gaps<br><br>
        
        <strong>5. Prototyping:</strong><br>
        • Build mockups or demos<br>
        • Get early feedback<br>
        • Clarify vague requirements<br><br>
        
        <strong>6. Workshops:</strong><br>
        • Collaborative sessions<br>
        • JAD (Joint Application Development)<br>
        • Rapid consensus building
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ User Stories (Agile)")
    
    st.markdown("""
    <div class="design-box">
        <strong>Format:</strong><br>
        "As a [role], I want [feature] so that [benefit]"<br><br>
        
        <strong>Examples:</strong><br><br>
        
        <strong>E-commerce:</strong><br>
        • As a customer, I want to add items to cart so that I can purchase multiple products<br>
        • As a customer, I want to track my order so that I know when it will arrive<br>
        • As an admin, I want to manage inventory so that products are always in stock<br><br>
        
        <strong>INVEST Criteria:</strong><br>
        • <strong>I</strong>ndependent: Can be developed separately<br>
        • <strong>N</strong>egotiable: Details can be discussed<br>
        • <strong>V</strong>aluable: Provides value to user<br>
        • <strong>E</strong>stimable: Can estimate effort<br>
        • <strong>S</strong>mall: Fits in one sprint<br>
        • <strong>T</strong>estable: Can verify completion
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: UML ====================
with tabs[3]:
    st.markdown("## 📊 UML Diagrams")
    
    st.markdown("### 1️⃣ Use Case Diagram")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Purpose:</strong> Show system functionality from user perspective<br><br>
        
        <strong>Components:</strong><br>
        • <strong>Actors:</strong> Users or external systems (stick figures)<br>
        • <strong>Use Cases:</strong> System functions (ovals)<br>
        • <strong>Relationships:</strong><br>
        &nbsp;&nbsp;- Association: Actor uses use case<br>
        &nbsp;&nbsp;- Include: Required functionality<br>
        &nbsp;&nbsp;- Extend: Optional functionality<br>
        &nbsp;&nbsp;- Generalization: Inheritance<br><br>
        
        <strong>Example: Online Banking</strong><br>
        Actors: Customer, Bank Staff<br>
        Use Cases:<br>
        • Login<br>
        • View Balance<br>
        • Transfer Money<br>
        • Pay Bills<br>
        • Generate Statement
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Class Diagram")
    
    st.markdown("""
    <div class="design-box">
        <strong>Purpose:</strong> Show static structure of system (classes and relationships)<br><br>
        
        <strong>Class Notation:</strong><br>
        <pre>
        ┌─────────────────┐
        │   ClassName     │
        ├─────────────────┤
        │ - attribute1    │
        │ + attribute2    │
        ├─────────────────┤
        │ + method1()     │
        │ - method2()     │
        └─────────────────┘
        </pre>
        
        <strong>Visibility:</strong><br>
        • + Public<br>
        • - Private<br>
        • # Protected<br>
        • ~ Package<br><br>
        
        <strong>Relationships:</strong><br>
        • <strong>Association:</strong> "has-a" (line)<br>
        • <strong>Aggregation:</strong> "has-a" weak (hollow diamond)<br>
        • <strong>Composition:</strong> "has-a" strong (filled diamond)<br>
        • <strong>Inheritance:</strong> "is-a" (hollow arrow)<br>
        • <strong>Dependency:</strong> "uses" (dashed arrow)<br>
        • <strong>Realization:</strong> "implements" (dashed hollow arrow)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Sequence Diagram")
    
    st.markdown("""
    <div class="methodology-box">
        <strong>Purpose:</strong> Show object interactions over time<br><br>
        
        <strong>Components:</strong><br>
        • <strong>Objects:</strong> Boxes at top<br>
        • <strong>Lifelines:</strong> Vertical dashed lines<br>
        • <strong>Messages:</strong> Horizontal arrows<br>
        • <strong>Activation:</strong> Thin rectangles on lifeline<br><br>
        
        <strong>Message Types:</strong><br>
        • Synchronous: Solid arrow (wait for response)<br>
        • Asynchronous: Open arrow (no wait)<br>
        • Return: Dashed arrow<br>
        • Self-call: Loop back to same object<br><br>
        
        <strong>Example: Login Process</strong><br>
        1. User → UI: Enter credentials<br>
        2. UI → Controller: Validate(username, password)<br>
        3. Controller → Database: Query user<br>
        4. Database → Controller: Return user data<br>
        5. Controller → UI: Login success/failure<br>
        6. UI → User: Display result
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Activity Diagram")
    
    st.markdown("""
    <div class="design-box">
        <strong>Purpose:</strong> Show workflow and business processes<br><br>
        
        <strong>Components:</strong><br>
        • <strong>Start:</strong> Filled circle<br>
        • <strong>Activity:</strong> Rounded rectangle<br>
        • <strong>Decision:</strong> Diamond<br>
        • <strong>Fork/Join:</strong> Thick bar (parallel activities)<br>
        • <strong>End:</strong> Filled circle with border<br><br>
        
        <strong>Use Cases:</strong><br>
        • Business process modeling<br>
        • Algorithm flowcharts<br>
        • Parallel processing<br>
        • Exception handling
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: SYSTEM DESIGN ====================
with tabs[4]:
    st.markdown("## 🏗️ System Design")
    
    st.markdown("### 1️⃣ Architectural Patterns")
    
    st.markdown("""
    <div class="pattern-box">
        <strong>1. Layered Architecture:</strong><br>
        • Presentation Layer (UI)<br>
        • Business Logic Layer<br>
        • Data Access Layer<br>
        • Database Layer<br>
        • Advantages: Separation of concerns, maintainable<br>
        • Disadvantages: Can be slower, tight coupling<br><br>
        
        <strong>2. Client-Server:</strong><br>
        • Clients request services<br>
        • Servers provide services<br>
        • Examples: Web apps, email<br><br>
        
        <strong>3. Microservices:</strong><br>
        • Small, independent services<br>
        • Each service has own database<br>
        • Communicate via APIs<br>
        • Advantages: Scalable, independent deployment<br>
        • Disadvantages: Complex, distributed system challenges<br><br>
        
        <strong>4. Event-Driven:</strong><br>
        • Components communicate via events<br>
        • Loose coupling<br>
        • Examples: Message queues, pub/sub<br><br>
        
        <strong>5. Model-View-Controller (MVC):</strong><br>
        • Model: Data and business logic<br>
        • View: User interface<br>
        • Controller: Handles user input<br>
        • Used in web frameworks (Django, Rails, ASP.NET)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Design Principles")
    
    st.markdown("""
    <div class="theory-box">
        <strong>SOLID Principles:</strong><br><br>
        
        <strong>S - Single Responsibility:</strong><br>
        • Class should have one reason to change<br>
        • Each class does one thing well<br><br>
        
        <strong>O - Open/Closed:</strong><br>
        • Open for extension, closed for modification<br>
        • Use inheritance and interfaces<br><br>
        
        <strong>L - Liskov Substitution:</strong><br>
        • Subtypes must be substitutable for base types<br>
        • Derived classes don't break base class behavior<br><br>
        
        <strong>I - Interface Segregation:</strong><br>
        • Many specific interfaces better than one general<br>
        • Clients shouldn't depend on unused methods<br><br>
        
        <strong>D - Dependency Inversion:</strong><br>
        • Depend on abstractions, not concretions<br>
        • High-level modules don't depend on low-level modules
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ API Design")
    
    st.markdown("""
    <div class="methodology-box">
        <strong>RESTful API Principles:</strong><br><br>
        
        <strong>HTTP Methods:</strong><br>
        • GET: Retrieve resource<br>
        • POST: Create resource<br>
        • PUT: Update resource (full)<br>
        • PATCH: Update resource (partial)<br>
        • DELETE: Remove resource<br><br>
        
        <strong>Best Practices:</strong><br>
        • Use nouns for resources: /users, /products<br>
        • Use HTTP status codes properly<br>
        • Version your API: /v1/users<br>
        • Use pagination for large datasets<br>
        • Implement authentication (OAuth, JWT)<br>
        • Document with OpenAPI/Swagger<br><br>
        
        <strong>Example Endpoints:</strong><br>
        • GET /api/v1/users - List all users<br>
        • GET /api/v1/users/123 - Get user 123<br>
        • POST /api/v1/users - Create new user<br>
        • PUT /api/v1/users/123 - Update user 123<br>
        • DELETE /api/v1/users/123 - Delete user 123
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: DESIGN PATTERNS ====================
with tabs[5]:
    st.markdown("## 🎨 Design Patterns")
    
    st.markdown("### 1️⃣ Creational Patterns")
    
    st.markdown("""
    <div class="pattern-box">
        <strong>Singleton:</strong><br>
        • Ensure only one instance of class<br>
        • Global access point<br>
        • Example: Database connection, Logger<br><br>
        
        <strong>Factory Method:</strong><br>
        • Create objects without specifying exact class<br>
        • Subclasses decide which class to instantiate<br>
        • Example: Document creator (PDF, Word, Excel)<br><br>
        
        <strong>Abstract Factory:</strong><br>
        • Create families of related objects<br>
        • Example: UI components (Windows, Mac, Linux)<br><br>
        
        <strong>Builder:</strong><br>
        • Construct complex objects step by step<br>
        • Separate construction from representation<br>
        • Example: Building a house (foundation, walls, roof)<br><br>
        
        <strong>Prototype:</strong><br>
        • Clone existing objects<br>
        • Avoid expensive creation<br>
        • Example: Copy document with formatting
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Structural Patterns")
    
    st.markdown("""
    <div class="design-box">
        <strong>Adapter:</strong><br>
        • Convert interface to another interface<br>
        • Make incompatible interfaces work together<br>
        • Example: Power adapter, legacy system integration<br><br>
        
        <strong>Decorator:</strong><br>
        • Add responsibilities to objects dynamically<br>
        • Wrap objects with new functionality<br>
        • Example: Coffee with milk, sugar, whipped cream<br><br>
        
        <strong>Facade:</strong><br>
        • Provide simplified interface to complex system<br>
        • Hide complexity<br>
        • Example: Home theater system (one button to start)<br><br>
        
        <strong>Proxy:</strong><br>
        • Placeholder for another object<br>
        • Control access, lazy loading, caching<br>
        • Example: Virtual proxy for large images<br><br>
        
        <strong>Composite:</strong><br>
        • Compose objects into tree structures<br>
        • Treat individual and composite objects uniformly<br>
        • Example: File system (files and folders)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Behavioral Patterns")
    
    st.markdown("""
    <div class="methodology-box">
        <strong>Observer:</strong><br>
        • One-to-many dependency<br>
        • When one object changes, notify dependents<br>
        • Example: Event listeners, MVC<br><br>
        
        <strong>Strategy:</strong><br>
        • Define family of algorithms<br>
        • Make them interchangeable<br>
        • Example: Payment methods (credit card, PayPal, crypto)<br><br>
        
        <strong>Command:</strong><br>
        • Encapsulate request as object<br>
        • Support undo/redo<br>
        • Example: Text editor commands<br><br>
        
        <strong>State:</strong><br>
        • Object changes behavior when state changes<br>
        • Example: TCP connection states<br><br>
        
        <strong>Template Method:</strong><br>
        • Define skeleton of algorithm<br>
        • Subclasses override specific steps<br>
        • Example: Data processing pipeline
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: DATABASE DESIGN ====================
with tabs[6]:
    st.markdown("## 🗄️ Database Design")
    
    st.markdown("### 1️⃣ Entity-Relationship Diagram (ERD)")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Components:</strong><br><br>
        
        <strong>Entity:</strong><br>
        • Object or concept (rectangle)<br>
        • Example: Customer, Product, Order<br><br>
        
        <strong>Attribute:</strong><br>
        • Property of entity (oval)<br>
        • Example: Customer (ID, Name, Email)<br>
        • <strong>Key attribute:</strong> Underlined<br>
        • <strong>Derived attribute:</strong> Dashed oval<br>
        • <strong>Multivalued attribute:</strong> Double oval<br><br>
        
        <strong>Relationship:</strong><br>
        • Association between entities (diamond)<br>
        • Example: Customer PLACES Order<br><br>
        
        <strong>Cardinality:</strong><br>
        • One-to-One (1:1)<br>
        • One-to-Many (1:N)<br>
        • Many-to-Many (M:N)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Normalization")
    
    st.markdown("""
    <div class="design-box">
        <strong>Purpose:</strong> Eliminate redundancy and anomalies<br><br>
        
        <strong>1NF (First Normal Form):</strong><br>
        • Atomic values (no repeating groups)<br>
        • Each column contains single value<br>
        • Each row is unique<br><br>
        
        <strong>2NF (Second Normal Form):</strong><br>
        • Must be in 1NF<br>
        • No partial dependencies<br>
        • All non-key attributes depend on entire primary key<br><br>
        
        <strong>3NF (Third Normal Form):</strong><br>
        • Must be in 2NF<br>
        • No transitive dependencies<br>
        • Non-key attributes depend only on primary key<br><br>
        
        <strong>BCNF (Boyce-Codd Normal Form):</strong><br>
        • Stricter version of 3NF<br>
        • Every determinant is a candidate key<br><br>
        
        <strong>Trade-offs:</strong><br>
        • Higher normalization = less redundancy<br>
        • But more joins = slower queries<br>
        • Sometimes denormalize for performance
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Database Schema Example")
    
    st.markdown("""
    <div class="methodology-box">
        <strong>E-commerce Database:</strong><br><br>
        
        <strong>Customers Table:</strong><br>
        • CustomerID (PK)<br>
        • Name, Email, Phone<br>
        • Address, City, Country<br><br>
        
        <strong>Products Table:</strong><br>
        • ProductID (PK)<br>
        • Name, Description<br>
        • Price, Stock<br>
        • CategoryID (FK)<br><br>
        
        <strong>Orders Table:</strong><br>
        • OrderID (PK)<br>
        • CustomerID (FK)<br>
        • OrderDate, TotalAmount<br>
        • Status<br><br>
        
        <strong>OrderItems Table:</strong><br>
        • OrderItemID (PK)<br>
        • OrderID (FK)<br>
        • ProductID (FK)<br>
        • Quantity, Price<br><br>
        
        <strong>Categories Table:</strong><br>
        • CategoryID (PK)<br>
        • Name, Description
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: TESTING ====================
with tabs[7]:
    st.markdown("## 🧪 Testing & Quality Assurance")
    
    st.markdown("### 1️⃣ Testing Levels")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Unit Testing:</strong><br>
        • Test individual components<br>
        • Developers write tests<br>
        • Fast, automated<br>
        • Tools: JUnit, pytest, Jest<br><br>
        
        <strong>Integration Testing:</strong><br>
        • Test component interactions<br>
        • Verify interfaces work together<br>
        • Database, API, service integration<br><br>
        
        <strong>System Testing:</strong><br>
        • Test complete system<br>
        • End-to-end functionality<br>
        • Performance, security, usability<br><br>
        
        <strong>Acceptance Testing:</strong><br>
        • Validate against requirements<br>
        • User acceptance testing (UAT)<br>
        • Customer verifies system<br>
        • Go/no-go decision
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Testing Techniques")
    
    st.markdown("""
    <div class="methodology-box">
        <strong>Black Box Testing:</strong><br>
        • Test without knowing internal structure<br>
        • Focus on inputs and outputs<br>
        • Techniques:<br>
        &nbsp;&nbsp;- Equivalence partitioning<br>
        &nbsp;&nbsp;- Boundary value analysis<br>
        &nbsp;&nbsp;- Decision tables<br><br>
        
        <strong>White Box Testing:</strong><br>
        • Test with knowledge of internal structure<br>
        • Code coverage<br>
        • Techniques:<br>
        &nbsp;&nbsp;- Statement coverage<br>
        &nbsp;&nbsp;- Branch coverage<br>
        &nbsp;&nbsp;- Path coverage<br><br>
        
        <strong>Gray Box Testing:</strong><br>
        • Combination of black and white box<br>
        • Partial knowledge of internals
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Quality Metrics")
    
    st.markdown("""
    <div class="design-box">
        <strong>Code Quality:</strong><br>
        • Code coverage (% of code tested)<br>
        • Cyclomatic complexity<br>
        • Code duplication<br>
        • Technical debt<br><br>
        
        <strong>Defect Metrics:</strong><br>
        • Defect density (defects per KLOC)<br>
        • Defect removal efficiency<br>
        • Mean time to failure (MTTF)<br>
        • Mean time to repair (MTTR)<br><br>
        
        <strong>Process Metrics:</strong><br>
        • Velocity (story points per sprint)<br>
        • Burn-down rate<br>
        • Lead time<br>
        • Cycle time
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 9: CASE STUDIES ====================
with tabs[8]:
    st.markdown("## 🎯 Case Studies")
    
    case_studies = [
        {
            "title": "Case Study 1: Library Management System",
            "description": "Design a system for managing library operations",
            "requirements": """
**Functional Requirements:**
1. Member registration and management
2. Book catalog and search
3. Check-out and return books
4. Reserve books
5. Fine calculation for overdue books
6. Generate reports

**Non-Functional Requirements:**
- Support 10,000 members
- Response time < 2 seconds
- 99% uptime
- Secure user data
            """,
            "solution": """
**System Design:**

**Actors:**
- Library Member
- Librarian
- System Administrator

**Key Use Cases:**
- Register Member
- Search Books
- Borrow Book
- Return Book
- Pay Fine
- Generate Reports

**Main Classes:**
- Member (memberID, name, email, phone)
- Book (ISBN, title, author, category, status)
- Loan (loanID, memberID, ISBN, borrowDate, dueDate, returnDate)
- Fine (fineID, loanID, amount, paid)
- Librarian (staffID, name, role)

**Database Tables:**
- Members, Books, Loans, Fines, Categories, Authors

**Architecture:**
- 3-tier: Presentation (Web UI), Business Logic, Data Access
- RESTful API for mobile app
- MySQL database
            """
        },
        {
            "title": "Case Study 2: Online Food Delivery System",
            "description": "Design a food delivery platform like Uber Eats",
            "requirements": """
**Functional Requirements:**
1. Customer can browse restaurants
2. Place orders
3. Track delivery in real-time
4. Payment processing
5. Rating and reviews
6. Restaurant management
7. Delivery driver assignment

**Non-Functional Requirements:**
- Handle 100,000 concurrent users
- Real-time tracking
- 99.99% payment success rate
- Mobile-first design
            """,
            "solution": """
**System Design:**

**Microservices Architecture:**
- User Service (authentication, profiles)
- Restaurant Service (menu, availability)
- Order Service (order processing)
- Payment Service (transactions)
- Delivery Service (driver assignment, tracking)
- Notification Service (SMS, push, email)

**Key Technologies:**
- API Gateway (Kong, AWS API Gateway)
- Message Queue (RabbitMQ, Kafka)
- Real-time (WebSockets, Socket.io)
- Geolocation (Google Maps API)
- Payment Gateway (Stripe, PayPal)

**Database Design:**
- Users, Restaurants, MenuItems, Orders, OrderItems
- Drivers, Deliveries, Payments, Reviews

**Scalability:**
- Load balancing
- Database sharding
- Caching (Redis)
- CDN for images
            """
        }
    ]
    
    for idx, case in enumerate(case_studies, 1):
        with st.expander(f"📝 {case['title']}", expanded=False):
            st.markdown(f"**Description:** {case['description']}")
            
            st.markdown("### Requirements")
            st.markdown(case['requirements'])
            
            if st.button(f"Show Solution", key=f"case_{idx}"):
                st.markdown("### Solution")
                st.markdown(case['solution'])

# ==================== TAB 10: YOUTUBE RESOURCES ====================
with tabs[9]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning Systems Analysis and Design</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {
            "title": "Systems Analysis and Design",
            "channel": "Udacity",
            "url": "https://www.youtube.com/playlist?list=PLAwxTw4SYaPkMTetlG7xKWaI5ZAZFX8fL",
            "description": "Complete SDLC course",
            "duration": "Full Course"
        },
        {
            "title": "UML Diagrams Tutorial",
            "channel": "Lucidchart",
            "url": "https://www.youtube.com/playlist?list=PLUoebdZqEHTxNC7hWPPwLsBmWI0KEhZOd",
            "description": "Learn all UML diagram types",
            "duration": "Playlist"
        },
        {
            "title": "Software Engineering Basics",
            "channel": "freeCodeCamp.org",
            "url": "https://www.youtube.com/watch?v=C7MRkqP5NRI",
            "description": "Introduction to software engineering",
            "duration": "~8 hours"
        }
    ]
    
    for resource in beginner_resources:
        st.markdown(f"""
        **[{resource["title"]}]({resource["url"]})**  
        📺 Channel: {resource["channel"]} | ⏱️ {resource["duration"]}  
        {resource["description"]}
        """)
        st.markdown("---")
    
    # Intermediate Level
    st.markdown("### 🟡 Intermediate Level")
    
    intermediate_resources = [
        {
            "title": "Design Patterns",
            "channel": "Christopher Okhravi",
            "url": "https://www.youtube.com/playlist?list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc",
            "description": "Gang of Four design patterns explained",
            "duration": "Playlist"
        },
        {
            "title": "System Design Interview",
            "channel": "Gaurav Sen",
            "url": "https://www.youtube.com/playlist?list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX",
            "description": "System design for interviews",
            "duration": "Playlist"
        },
        {
            "title": "Database Design",
            "channel": "Caleb Curry",
            "url": "https://www.youtube.com/playlist?list=PL_c9BZzLwBRK0Pc28IdvPQizD2mJlgoID",
            "description": "Database design and normalization",
            "duration": "Playlist"
        }
    ]
    
    for resource in intermediate_resources:
        st.markdown(f"""
        **[{resource['title']}]({resource['url']})**  
        📺 Channel: {resource['channel']} | ⏱️ {resource['duration']}  
        {resource['description'}}
        """)
        st.markdown("---")
    
    # Advanced Level
    st.markdown("### 🔴 Advanced Level")
    
    advanced_resources = [
        {
            "title": "Software Architecture",
            "channel": "Mark Richards",
            "url": "https://www.youtube.com/c/markrichards5014",
            "description": "Advanced architecture patterns",
            "duration": "Channel"
        },
        {
            "title": "Domain-Driven Design",
            "channel": "CodeOpinion",
            "url": "https://www.youtube.com/c/CodeOpinion",
            "description": "DDD concepts and practices",
            "duration": "Channel"
        },
        {
            "title": "Microservices Architecture",
            "channel": "TechWorld with Nana",
            "url": "https://www.youtube.com/watch?v=rv4LlmLmVWk",
            "description": "Complete microservices tutorial",
            "duration": "~4 hours"
        }
    ]
    
    for resource in advanced_resources:
        st.markdown(f"""
        **[{resource["title"]}]({resource["url"]})**  
        📺 Channel: {resource["channel"]} | ⏱️ {resource["duration"]}  
        {resource["description"]}
        """)
        st.markdown("---")
    
    # Study Tips
    st.markdown("### 💡 Study Tips")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Recommended Learning Path:</strong><br>
        1. Understand SDLC methodologies<br>
        2. Learn requirements engineering techniques<br>
        3. Master UML diagrams (Use Case, Class, Sequence)<br>
        4. Study design patterns (GoF)<br>
        5. Practice database design and normalization<br>
        6. Learn system architecture patterns<br>
        7. Work on real projects<br>
        8. Read case studies<br><br>
        
        <strong>Tools & Software:</strong><br>
        • <strong>UML Tools:</strong> Lucidchart, Draw.io, Visual Paradigm<br>
        • <strong>Prototyping:</strong> Figma, Adobe XD, Balsamiq<br>
        • <strong>Project Management:</strong> Jira, Trello, Asana<br>
        • <strong>Database Design:</strong> MySQL Workbench, dbdiagram.io<br><br>
        
        <strong>Practice Projects:</strong><br>
        • Library Management System<br>
        • E-commerce Platform<br>
        • Hospital Management System<br>
        • Social Media Application<br>
        • Banking System
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE303 - Systems Analysis and Design</strong><br>
    <small>UTel University | Department of Computer Engineering</small>
</div>
""", unsafe_allow_html=True)
