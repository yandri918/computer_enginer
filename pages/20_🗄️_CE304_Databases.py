import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="CE304 - Databases", page_icon="🗄️", layout="wide")

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
    
    .sql-box {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .design-box {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .performance-box {
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
    <div style="font-size: 1.2rem; opacity: 0.9;">CE304</div>
    <div class="course-title">Databases</div>
    <div>🗄️ 3 Credits | Semester 4 | Data Management</div>
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
    "🏗️ Relational Model",
    "💻 SQL Basics",
    "🔍 Advanced SQL",
    "📐 Database Design",
    "⚡ Transactions & Concurrency",
    "🚀 Performance & Indexing",
    "🌐 NoSQL Databases",
    "🎯 Practice Problems",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive study of database management systems (DBMS), covering relational database theory, SQL programming, 
        database design and normalization, transaction management, query optimization, and NoSQL databases. Emphasizes both 
        theoretical foundations and practical implementation. Students will design databases, write complex SQL queries, 
        optimize performance, and work with modern database technologies.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Understand relational database theory and algebra",
        "Design normalized database schemas (1NF-BCNF)",
        "Write complex SQL queries (joins, subqueries, aggregations)",
        "Implement transactions with ACID properties",
        "Optimize database performance with indexing",
        "Understand concurrency control mechanisms",
        "Work with NoSQL databases (MongoDB, Redis, Cassandra)",
        "Design scalable database architectures"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Fundamentals:**
        - Relational model and algebra
        - Entity-Relationship modeling
        - Functional dependencies
        - Normalization (1NF to BCNF)
        - SQL data types and constraints
        
        **SQL:**
        - DDL (CREATE, ALTER, DROP)
        - DML (SELECT, INSERT, UPDATE, DELETE)
        - Joins (INNER, LEFT, RIGHT, FULL)
        - Subqueries and CTEs
        - Aggregate functions and GROUP BY
        """)
    
    with col2:
        st.markdown("""
        **Advanced Topics:**
        - Transaction management (ACID)
        - Concurrency control (locking, MVCC)
        - Query optimization
        - Indexing strategies (B-tree, Hash)
        - Database security
        
        **Modern Databases:**
        - NoSQL databases (Document, Key-Value, Column, Graph)
        - CAP theorem
        - Sharding and replication
        - Cloud databases
        - NewSQL systems
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Database System Concepts", "author": "Silberschatz, Korth & Sudarshan", "type": "Textbook"},
        {"title": "Fundamentals of Database Systems", "author": "Elmasri & Navathe", "type": "Textbook"},
        {"title": "Designing Data-Intensive Applications", "author": "Martin Kleppmann", "type": "Modern"},
        {"title": "SQL Performance Explained", "author": "Markus Winand", "type": "Performance"}
    ]
    
    for resource in resources:
        title = resource['title']
        author = resource['author']
        rtype = resource['type']
        st.markdown(f"📖 **{title}** by {author} ({rtype})")

# ==================== TAB 2: RELATIONAL MODEL ====================
with tabs[1]:
    st.markdown("## 🏗️ Relational Model")
    
    st.markdown("### 1️⃣ Relational Concepts")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Relation (Table):</strong><br>
        • Set of tuples (rows)<br>
        • Each tuple has same attributes (columns)<br>
        • Order of tuples doesn't matter<br>
        • No duplicate tuples<br><br>
        
        <strong>Schema:</strong><br>
        • Relation name<br>
        • Attribute names and types<br>
        • Example: Students(StudentID: INT, Name: VARCHAR, GPA: FLOAT)<br><br>
        
        <strong>Keys:</strong><br>
        • <strong>Superkey:</strong> Set of attributes that uniquely identifies tuples<br>
        • <strong>Candidate Key:</strong> Minimal superkey<br>
        • <strong>Primary Key:</strong> Chosen candidate key<br>
        • <strong>Foreign Key:</strong> References primary key in another relation<br><br>
        
        <strong>Integrity Constraints:</strong><br>
        • <strong>Entity Integrity:</strong> Primary key cannot be NULL<br>
        • <strong>Referential Integrity:</strong> Foreign key must reference existing primary key<br>
        • <strong>Domain Integrity:</strong> Values must be from valid domain
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Relational Algebra")
    
    st.markdown("""
    <div class="sql-box">
        <strong>Selection (σ):</strong><br>
        • Select rows that satisfy condition<br>
        • σ<sub>GPA>3.5</sub>(Students)<br><br>
        
        <strong>Projection (π):</strong><br>
        • Select specific columns<br>
        • π<sub>Name,GPA</sub>(Students)<br><br>
        
        <strong>Union (∪):</strong><br>
        • Combine tuples from two relations<br>
        • Relations must be union-compatible<br><br>
        
        <strong>Intersection (∩):</strong><br>
        • Common tuples in both relations<br><br>
        
        <strong>Difference (−):</strong><br>
        • Tuples in first but not second<br><br>
        
        <strong>Cartesian Product (×):</strong><br>
        • All possible combinations<br><br>
        
        <strong>Join (⋈):</strong><br>
        • Combine relations based on condition<br>
        • Students ⋈<sub>StudentID</sub> Enrollments
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: SQL BASICS ====================
with tabs[2]:
    st.markdown("## 💻 SQL Basics")
    
    st.markdown("### 1️⃣ DDL (Data Definition Language)")
    
    st.markdown("""
    <div class="sql-box">
        <strong>CREATE TABLE:</strong><br>
        <pre>
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE,
    GPA DECIMAL(3,2) CHECK (GPA >= 0 AND GPA <= 4.0),
    EnrollmentDate DATE DEFAULT CURRENT_DATE
);
        </pre><br>
        
        <strong>ALTER TABLE:</strong><br>
        <pre>
-- Add column
ALTER TABLE Students ADD COLUMN Phone VARCHAR(15);

-- Modify column
ALTER TABLE Students MODIFY COLUMN Name VARCHAR(150);

-- Drop column
ALTER TABLE Students DROP COLUMN Phone;
        </pre><br>
        
        <strong>DROP TABLE:</strong><br>
        <pre>
DROP TABLE Students;  -- Delete table and data
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ DML (Data Manipulation Language)")
    
    st.markdown("""
    <div class="sql-box">
        <strong>INSERT:</strong><br>
        <pre>
-- Insert single row
INSERT INTO Students (StudentID, Name, Email, GPA)
VALUES (1, 'John Doe', 'john@example.com', 3.75);

-- Insert multiple rows
INSERT INTO Students VALUES
    (2, 'Jane Smith', 'jane@example.com', 3.90, '2024-01-15'),
    (3, 'Bob Johnson', 'bob@example.com', 3.50, '2024-01-15');
        </pre><br>
        
        <strong>SELECT:</strong><br>
        <pre>
-- Select all columns
SELECT * FROM Students;

-- Select specific columns
SELECT Name, GPA FROM Students;

-- With WHERE clause
SELECT Name, GPA FROM Students WHERE GPA > 3.5;

-- With ORDER BY
SELECT Name, GPA FROM Students ORDER BY GPA DESC;

-- With LIMIT
SELECT Name, GPA FROM Students ORDER BY GPA DESC LIMIT 10;
        </pre><br>
        
        <strong>UPDATE:</strong><br>
        <pre>
-- Update single row
UPDATE Students SET GPA = 3.80 WHERE StudentID = 1;

-- Update multiple rows
UPDATE Students SET GPA = GPA + 0.1 WHERE GPA < 3.0;
        </pre><br>
        
        <strong>DELETE:</strong><br>
        <pre>
-- Delete specific rows
DELETE FROM Students WHERE GPA < 2.0;

-- Delete all rows (keep table structure)
DELETE FROM Students;
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: ADVANCED SQL ====================
with tabs[3]:
    st.markdown("## 🔍 Advanced SQL")
    
    st.markdown("### 1️⃣ Joins")
    
    st.markdown("""
    <div class="sql-box">
        <strong>INNER JOIN:</strong><br>
        Returns only matching rows from both tables<br>
        <pre>
SELECT Students.Name, Courses.CourseName
FROM Students
INNER JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
INNER JOIN Courses ON Enrollments.CourseID = Courses.CourseID;
        </pre><br>
        
        <strong>LEFT JOIN (LEFT OUTER JOIN):</strong><br>
        Returns all rows from left table, matching rows from right<br>
        <pre>
SELECT Students.Name, Enrollments.Grade
FROM Students
LEFT JOIN Enrollments ON Students.StudentID = Enrollments.StudentID;
        </pre><br>
        
        <strong>RIGHT JOIN:</strong><br>
        Returns all rows from right table, matching rows from left<br><br>
        
        <strong>FULL OUTER JOIN:</strong><br>
        Returns all rows from both tables<br><br>
        
        <strong>CROSS JOIN:</strong><br>
        Cartesian product of both tables
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Aggregate Functions")
    
    st.markdown("""
    <div class="sql-box">
        <strong>Common Aggregates:</strong><br>
        <pre>
-- COUNT
SELECT COUNT(*) FROM Students;
SELECT COUNT(DISTINCT Major) FROM Students;

-- SUM, AVG, MIN, MAX
SELECT AVG(GPA) AS AvgGPA FROM Students;
SELECT MIN(GPA), MAX(GPA) FROM Students;

-- GROUP BY
SELECT Major, AVG(GPA) AS AvgGPA
FROM Students
GROUP BY Major;

-- HAVING (filter after grouping)
SELECT Major, AVG(GPA) AS AvgGPA
FROM Students
GROUP BY Major
HAVING AVG(GPA) > 3.5;
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Subqueries")
    
    st.markdown("""
    <div class="sql-box">
        <strong>Scalar Subquery:</strong><br>
        <pre>
SELECT Name, GPA
FROM Students
WHERE GPA > (SELECT AVG(GPA) FROM Students);
        </pre><br>
        
        <strong>IN Subquery:</strong><br>
        <pre>
SELECT Name FROM Students
WHERE StudentID IN (
    SELECT StudentID FROM Enrollments WHERE Grade = 'A'
);
        </pre><br>
        
        <strong>EXISTS Subquery:</strong><br>
        <pre>
SELECT Name FROM Students s
WHERE EXISTS (
    SELECT 1 FROM Enrollments e
    WHERE e.StudentID = s.StudentID AND e.Grade = 'A'
);
        </pre><br>
        
        <strong>Common Table Expression (CTE):</strong><br>
        <pre>
WITH HighGPA AS (
    SELECT StudentID, Name, GPA
    FROM Students
    WHERE GPA > 3.5
)
SELECT * FROM HighGPA ORDER BY GPA DESC;
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: DATABASE DESIGN ====================
with tabs[4]:
    st.markdown("## 📐 Database Design")
    
    st.markdown("### 1️⃣ Normalization")
    
    st.markdown("""
    <div class="design-box">
        <strong>1NF (First Normal Form):</strong><br>
        • Atomic values (no repeating groups)<br>
        • Each column contains single value<br>
        • Each row is unique (has primary key)<br><br>
        
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
        • Every determinant is a candidate key<br>
        • Eliminates all anomalies in most cases
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Functional Dependencies")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Definition:</strong><br>
        X → Y means "X functionally determines Y"<br>
        If two tuples have same X value, they must have same Y value<br><br>
        
        <strong>Example:</strong><br>
        StudentID → Name, Email, GPA<br>
        (StudentID uniquely determines these attributes)<br><br>
        
        <strong>Armstrong's Axioms:</strong><br>
        • <strong>Reflexivity:</strong> If Y ⊆ X, then X → Y<br>
        • <strong>Augmentation:</strong> If X → Y, then XZ → YZ<br>
        • <strong>Transitivity:</strong> If X → Y and Y → Z, then X → Z<br><br>
        
        <strong>Closure:</strong><br>
        • X<sup>+</sup> = set of all attributes functionally determined by X<br>
        • Used to find candidate keys
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: TRANSACTIONS ====================
with tabs[5]:
    st.markdown("## ⚡ Transactions & Concurrency")
    
    st.markdown("### 1️⃣ ACID Properties")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Atomicity:</strong><br>
        • All or nothing<br>
        • Transaction either completes fully or has no effect<br>
        • Rollback on failure<br><br>
        
        <strong>Consistency:</strong><br>
        • Database remains in valid state<br>
        • All constraints satisfied<br>
        • Integrity maintained<br><br>
        
        <strong>Isolation:</strong><br>
        • Concurrent transactions don't interfere<br>
        • Appears as if transactions execute serially<br>
        • Prevents dirty reads, lost updates<br><br>
        
        <strong>Durability:</strong><br>
        • Committed changes persist<br>
        • Survive system failures<br>
        • Write-ahead logging
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Isolation Levels")
    
    isolation_levels = {
        'Level': ['READ UNCOMMITTED', 'READ COMMITTED', 'REPEATABLE READ', 'SERIALIZABLE'],
        'Dirty Read': ['Yes', 'No', 'No', 'No'],
        'Non-Repeatable Read': ['Yes', 'Yes', 'No', 'No'],
        'Phantom Read': ['Yes', 'Yes', 'Yes', 'No'],
        'Performance': ['Fastest', 'Fast', 'Slow', 'Slowest']
    }
    
    df_isolation = pd.DataFrame(isolation_levels)
    st.dataframe(df_isolation, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Concurrency Control")
    
    st.markdown("""
    <div class="sql-box">
        <strong>Locking:</strong><br>
        • <strong>Shared Lock (S):</strong> Multiple transactions can read<br>
        • <strong>Exclusive Lock (X):</strong> Only one transaction can write<br>
        • <strong>Two-Phase Locking (2PL):</strong> Growing phase, shrinking phase<br>
        • <strong>Deadlock:</strong> Circular wait for locks<br><br>
        
        <strong>MVCC (Multi-Version Concurrency Control):</strong><br>
        • Keep multiple versions of data<br>
        • Readers don't block writers<br>
        • Writers don't block readers<br>
        • Used by PostgreSQL, MySQL InnoDB<br><br>
        
        <strong>Timestamp Ordering:</strong><br>
        • Each transaction gets timestamp<br>
        • Ensure serializable order<br>
        • No locks needed
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: PERFORMANCE ====================
with tabs[6]:
    st.markdown("## 🚀 Performance & Indexing")
    
    st.markdown("### 1️⃣ Indexing")
    
    st.markdown("""
    <div class="performance-box">
        <strong>B-Tree Index:</strong><br>
        • Most common index type<br>
        • Balanced tree structure<br>
        • Good for range queries<br>
        • O(log n) search time<br><br>
        
        <strong>Hash Index:</strong><br>
        • Fast equality lookups<br>
        • O(1) average case<br>
        • No range queries<br>
        • Not sorted<br><br>
        
        <strong>Bitmap Index:</strong><br>
        • Good for low-cardinality columns<br>
        • Example: Gender, Status<br>
        • Space efficient<br><br>
        
        <strong>Full-Text Index:</strong><br>
        • For text search<br>
        • Tokenization and stemming<br>
        • Example: Search in articles
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Query Optimization")
    
    st.markdown("""
    <div class="sql-box">
        <strong>EXPLAIN Plan:</strong><br>
        <pre>
EXPLAIN SELECT * FROM Students WHERE GPA > 3.5;
        </pre><br>
        
        <strong>Optimization Tips:</strong><br>
        • Use indexes on WHERE, JOIN, ORDER BY columns<br>
        • Avoid SELECT * (specify needed columns)<br>
        • Use LIMIT for large result sets<br>
        • Avoid functions on indexed columns<br>
        • Use EXISTS instead of IN for large subqueries<br>
        • Denormalize for read-heavy workloads<br>
        • Partition large tables<br><br>
        
        <strong>Query Execution Steps:</strong><br>
        1. Parsing (syntax check)<br>
        2. Optimization (choose best plan)<br>
        3. Execution (run the plan)<br>
        4. Return results
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: NOSQL ====================
with tabs[7]:
    st.markdown("## 🌐 NoSQL Databases")
    
    st.markdown("### 1️⃣ NoSQL Types")
    
    nosql_types = {
        'Type': ['Document', 'Key-Value', 'Column-Family', 'Graph'],
        'Example': ['MongoDB, CouchDB', 'Redis, DynamoDB', 'Cassandra, HBase', 'Neo4j, ArangoDB'],
        'Data Model': ['JSON documents', 'Key-value pairs', 'Column families', 'Nodes and edges'],
        'Use Case': ['Content management', 'Caching, sessions', 'Time-series, analytics', 'Social networks, recommendations']
    }
    
    df_nosql = pd.DataFrame(nosql_types)
    st.dataframe(df_nosql, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ CAP Theorem")
    
    st.markdown("""
    <div class="theory-box">
        <strong>CAP Theorem:</strong><br>
        Distributed system can provide at most 2 of 3 guarantees:<br><br>
        
        <strong>Consistency (C):</strong><br>
        • All nodes see same data at same time<br>
        • Strong consistency<br><br>
        
        <strong>Availability (A):</strong><br>
        • Every request gets response<br>
        • System always operational<br><br>
        
        <strong>Partition Tolerance (P):</strong><br>
        • System continues despite network failures<br>
        • Essential for distributed systems<br><br>
        
        <strong>Trade-offs:</strong><br>
        • <strong>CP:</strong> Consistent but may be unavailable (MongoDB, HBase)<br>
        • <strong>AP:</strong> Available but may be inconsistent (Cassandra, DynamoDB)<br>
        • <strong>CA:</strong> Not partition-tolerant (Traditional RDBMS in single node)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ MongoDB Example")
    
    st.markdown("""
    <div class="sql-box">
        <strong>Insert Document:</strong><br>
        <pre>
db.students.insertOne({
    name: "John Doe",
    email: "john@example.com",
    gpa: 3.75,
    courses: ["CS101", "MATH201", "PHYS101"]
});
        </pre><br>
        
        <strong>Query Documents:</strong><br>
        <pre>
// Find all students with GPA > 3.5
db.students.find({ gpa: { $gt: 3.5 } });

// Find with projection
db.students.find(
    { gpa: { $gt: 3.5 } },
    { name: 1, gpa: 1, _id: 0 }
);
        </pre><br>
        
        <strong>Update Document:</strong><br>
        <pre>
db.students.updateOne(
    { email: "john@example.com" },
    { $set: { gpa: 3.80 } }
);
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 9: PRACTICE ====================
with tabs[8]:
    st.markdown("## 🎯 Practice Problems")
    
    problems = [
        {
            "title": "Problem 1: Complex Join Query",
            "question": "Write a query to find students who are enrolled in more than 3 courses and have GPA > 3.5. Show student name, GPA, and number of courses.",
            "hint": "Use JOIN, GROUP BY, HAVING, and WHERE clauses",
            "solution": """
**Solution:**

```sql
SELECT 
    s.Name,
    s.GPA,
    COUNT(e.CourseID) AS NumCourses
FROM Students s
INNER JOIN Enrollments e ON s.StudentID = e.StudentID
WHERE s.GPA > 3.5
GROUP BY s.StudentID, s.Name, s.GPA
HAVING COUNT(e.CourseID) > 3
ORDER BY NumCourses DESC, s.GPA DESC;
```

**Explanation:**
1. JOIN Students with Enrollments
2. Filter students with GPA > 3.5 (WHERE)
3. Group by student
4. Filter groups with > 3 courses (HAVING)
5. Order by number of courses and GPA
            """
        },
        {
            "title": "Problem 2: Normalization",
            "question": "Given table: Orders(OrderID, CustomerName, CustomerEmail, ProductName, ProductPrice, Quantity). Normalize to 3NF.",
            "hint": "Identify functional dependencies and create separate tables",
            "solution": """
**Solution:**

**Functional Dependencies:**
- OrderID → CustomerName, CustomerEmail
- CustomerEmail → CustomerName
- ProductName → ProductPrice
- OrderID, ProductName → Quantity

**Normalized Schema (3NF):**

**Customers Table:**
```sql
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    CustomerEmail VARCHAR(100) UNIQUE
);
```

**Products Table:**
```sql
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    ProductPrice DECIMAL(10,2)
);
```

**Orders Table:**
```sql
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
```

**OrderItems Table:**
```sql
CREATE TABLE OrderItems (
    OrderID INT,
    ProductID INT,
    Quantity INT,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
```

**Benefits:**
- No redundancy
- No update anomalies
- Maintains data integrity
            """
        }
    ]
    
    for idx, problem in enumerate(problems, 1):
        with st.expander(f"📝 {problem['title']}", expanded=False):
            st.markdown(f"**Question:** {problem['question']}")
            
            if st.button(f"Show Hint", key=f"hint_{idx}"):
                st.info(f"💡 {problem['hint']}")
            
            if st.button(f"Show Solution", key=f"sol_{idx}"):
                st.markdown(problem['solution'])

# ==================== TAB 10: YOUTUBE ====================
with tabs[9]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning Databases</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {"title": "SQL Tutorial - Full Course", "channel": "freeCodeCamp.org", "url": "https://www.youtube.com/watch?v=HXV3zeQKqGY", "description": "Complete SQL course for beginners", "duration": "~4 hours"},
        {"title": "Database Design Course", "channel": "freeCodeCamp.org", "url": "https://www.youtube.com/watch?v=ztHopE5Wnpc", "description": "Learn database design and normalization", "duration": "~8 hours"},
        {"title": "MySQL Tutorial", "channel": "Programming with Mosh", "url": "https://www.youtube.com/watch?v=7S_tz1z_5bA", "description": "MySQL for beginners", "duration": "~3 hours"}
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
        {"title": "Advanced SQL", "channel": "Caleb Curry", "url": "https://www.youtube.com/playlist?list=PL_c9BZzLwBRKn20DFbNeLAAbw4ZMTlZPH", "description": "Advanced SQL concepts and queries", "duration": "Playlist"},
        {"title": "Database Systems", "channel": "CMU Database Group", "url": "https://www.youtube.com/playlist?list=PLSE8ODhjZXjbohkNBWQs_otTrBTrjyohi", "description": "CMU 15-445 Database Systems", "duration": "Full Course"},
        {"title": "PostgreSQL Tutorial", "channel": "Amigoscode", "url": "https://www.youtube.com/watch?v=qw--VYLpxG4", "description": "Complete PostgreSQL guide", "duration": "~4 hours"}
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
        {"title": "Database Internals", "channel": "CMU Database Group", "url": "https://www.youtube.com/playlist?list=PLSE8ODhjZXjasmrEd2_Yi1deeE360zv5O", "description": "CMU 15-721 Advanced Database Systems", "duration": "Full Course"},
        {"title": "MongoDB University", "channel": "MongoDB", "url": "https://www.youtube.com/c/MongoDBofficial", "description": "Official MongoDB tutorials", "duration": "Channel"},
        {"title": "Distributed Databases", "channel": "Martin Kleppmann", "url": "https://www.youtube.com/watch?v=cQP8WApzIQQ", "description": "Distributed systems and databases", "duration": "Talks"}
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
        1. Learn SQL basics (SELECT, INSERT, UPDATE, DELETE)<br>
        2. Master joins and subqueries<br>
        3. Understand database design and normalization<br>
        4. Study transactions and ACID properties<br>
        5. Learn indexing and query optimization<br>
        6. Explore NoSQL databases<br>
        7. Practice with real projects<br>
        8. Work with cloud databases (AWS RDS, Azure SQL)<br><br>
        
        <strong>Tools & Databases:</strong><br>
        • <strong>MySQL:</strong> Most popular open-source RDBMS<br>
        • <strong>PostgreSQL:</strong> Advanced features, JSON support<br>
        • <strong>MongoDB:</strong> Document database<br>
        • <strong>Redis:</strong> In-memory key-value store<br>
        • <strong>SQLite:</strong> Embedded database for learning<br><br>
        
        <strong>Practice Platforms:</strong><br>
        • LeetCode Database problems<br>
        • HackerRank SQL challenges<br>
        • SQLZoo interactive tutorials<br>
        • Mode Analytics SQL tutorial
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE304 - Databases</strong><br>
    <small>UTel University | Department of Computer Engineering</small>
</div>
""", unsafe_allow_html=True)
