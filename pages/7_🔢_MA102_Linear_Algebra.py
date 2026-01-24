import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="MA102 - Linear Algebra", page_icon="🔢", layout="wide")

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
    
    .theorem-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .example-box {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .application-box {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
</style>
""")

# Header
st.markdown("""
<div style="font-size: 1.2rem; opacity: 0.9;">MA102
    Linear Algebra
    <div>🔢 3 Credits | Semester 2 | Mathematics
""")

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "2")
with col3:
    st.metric("Difficulty", "5/7")
with col4:
    st.metric("Hours/Week", "6")

st.markdown("---")

# Navigation tabs - Graduate level
tabs = st.tabs([
    "📚 Overview",
    "📐 Vectors & Spaces",
    "🔢 Matrices",
    "🎯 Linear Systems",
    "🔄 Linear Transformations",
    "⚡ Eigenvalues & Eigenvectors",
    "📊 Orthogonality",
    "🎨 SVD & Decompositions",
    "🧮 Applications",
    "🎯 Practice Problems"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <h3>Course Description</h3>
        <p>Comprehensive study of linear algebra from vectors to advanced decompositions. Covers vector spaces, 
        matrices, linear transformations, eigenvalues, orthogonality, and singular value decomposition. 
        Emphasizes both theoretical foundations and practical applications in data science, machine learning, 
        and computer graphics.</p>
    """)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Master vector spaces and subspaces",
        "Perform matrix operations and solve linear systems",
        "Understand linear transformations and their properties",
        "Compute eigenvalues and eigenvectors",
        "Apply orthogonalization and projection techniques",
        "Decompose matrices using SVD and other methods",
        "Apply linear algebra to real-world problems",
        "Use computational tools for linear algebra"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Fundamentals:**
        - Vector spaces and subspaces
        - Linear independence
        - Basis and dimension
        - Matrix operations
        - Determinants
        
        **Linear Systems:**
        - Gaussian elimination
        - LU decomposition
        - Matrix inverses
        - Rank and nullity
        - Least squares
        """)
    
    with col2:
        st.markdown("""
        **Advanced Topics:**
        - Eigenvalues and eigenvectors
        - Diagonalization
        - Orthogonal projections
        - Gram-Schmidt process
        - Singular Value Decomposition
        
        **Applications:**
        - Machine learning (PCA)
        - Computer graphics
        - Data compression
        - Network analysis
        - Quantum computing
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Linear Algebra and Its Applications", "author": "Gilbert Strang", "type": "Textbook"},
        {"title": "Introduction to Linear Algebra", "author": "Strang", "type": "Undergraduate"},
        {"title": "Linear Algebra Done Right", "author": "Sheldon Axler", "type": "Graduate"},
        {"title": "MIT OpenCourseWare 18.06", "author": "Gilbert Strang", "type": "Online"}
    ]
    
    for resource in resources:
        st.markdown(f"📖 **{resource['title']}** by {resource['author']} ({resource['type']})")

# ==================== TAB 2: VECTORS & SPACES ====================
with tabs[1]:
    st.markdown("## 📐 Vectors & Vector Spaces")
    
    st.markdown("### 1️⃣ Vector Operations")
    
    st.markdown("""
    **Vector in ℝⁿ:**  

        v = [v₁, v₂, ..., vₙ]ᵀ


        
        **Operations:**  

        • **Addition:** u + v = [u₁+v₁, u₂+v₂, ..., uₙ+vₙ]ᵀ  

        • **Scalar multiplication:** cv = [cv₁, cv₂, ..., cvₙ]ᵀ  

        • **Dot product:** u·v = u₁v₁ + u₂v₂ + ... + uₙvₙ  

        • **Norm:** ||v|| = √(v·v) = √(v₁² + v₂² + ... + vₙ²)
    """)
    
    # Interactive vector calculator
    st.markdown("#### 🧮 2D Vector Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Vector u:**")
        u1 = st.number_input("u₁", -10.0, 10.0, 3.0, 0.5)
        u2 = st.number_input("u₂", -10.0, 10.0, 4.0, 0.5)
    with col2:
        st.markdown("**Vector v:**")
        v1 = st.number_input("v₁", -10.0, 10.0, 1.0, 0.5)
        v2 = st.number_input("v₂", -10.0, 10.0, 2.0, 0.5)
    
    # Calculate operations
    u = np.array([u1, u2])
    v = np.array([v1, v2])
    
    u_plus_v = u + v
    dot_product = np.dot(u, v)
    norm_u = np.linalg.norm(u)
    norm_v = np.linalg.norm(v)
    
    # Visualize vectors
    vectors_data = pd.DataFrame({
        'x': [0, 0, 0],
        'y': [0, 0, 0],
        'x2': [u1, v1, u_plus_v[0]],
        'y2': [u2, v2, u_plus_v[1]],
        'vector': ['u', 'v', 'u+v']
    })
    
    vector_chart = alt.Chart(vectors_data).mark_rule(strokeWidth=3).encode(
        x=alt.X('x:Q', scale=alt.Scale(domain=[-10, 10]), title='x'),
        y=alt.Y('y:Q', scale=alt.Scale(domain=[-10, 10]), title='y'),
        x2='x2:Q',
        y2='y2:Q',
        color=alt.Color('vector:N', scale=alt.Scale(domain=['u', 'v', 'u+v'],
                                                      range=['#ec4899', '#3b82f6', '#10b981'])),
        tooltip=['vector', 'x2', 'y2']
    ).properties(
        width=600,
        height=600,
        title="Vector Visualization"
    )
    
    st.altair_chart(vector_chart, use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("u + v", f"[{u_plus_v[0]:.1f}, {u_plus_v[1]:.1f}]")
    with col2:
        st.metric("u · v", f"{dot_product:.2f}")
    with col3:
        st.metric("||u||, ||v||", f"{norm_u:.2f}, {norm_v:.2f}")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Vector Spaces")
    
    st.markdown("""
    **Definition: Vector Space**  

        A set V with operations + and · is a vector space if:


        **Closure:**  

        1. u + v ∈ V for all u, v ∈ V  

        2. cv ∈ V for all c ∈ ℝ, v ∈ V


        **Axioms:**  

        3. Commutativity: u + v = v + u  

        4. Associativity: (u + v) + w = u + (v + w)  

        5. Zero vector: ∃ 0 such that v + 0 = v  

        6. Additive inverse: ∃ -v such that v + (-v) = 0  

        7-10. Scalar multiplication properties
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Linear Independence")
    
    st.markdown("""
    **Linear Independence:**  

        Vectors v₁, v₂, ..., vₙ are linearly independent if:  

        c₁v₁ + c₂v₂ + ... + cₙvₙ = 0 ⟹ c₁ = c₂ = ... = cₙ = 0


        
        **Span:**  

        span{v₁, v₂, ..., vₙ} = {c₁v₁ + c₂v₂ + ... + cₙvₙ | cᵢ ∈ ℝ}


        
        **Basis:**  

        A linearly independent set that spans the space


        
        **Dimension:**  

        Number of vectors in a basis
    """)

# ==================== TAB 3: MATRICES ====================
with tabs[2]:
    st.markdown("## 🔢 Matrices")
    
    st.markdown("### 1️⃣ Matrix Operations")
    
    st.markdown("""
    **Matrix A (m × n):**  

        A = [aᵢⱼ] where i = 1,...,m and j = 1,...,n


        
        **Operations:**  

        • **Addition:** (A + B)ᵢⱼ = aᵢⱼ + bᵢⱼ  

        • **Scalar multiplication:** (cA)ᵢⱼ = c·aᵢⱼ  

        • **Multiplication:** (AB)ᵢⱼ = Σₖ aᵢₖbₖⱼ  

        • **Transpose:** (Aᵀ)ᵢⱼ = aⱼᵢ
    """)
    
    # Interactive matrix calculator
    st.markdown("#### 🧮 2×2 Matrix Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Matrix A:**")
        a11 = st.number_input("a₁₁", -10.0, 10.0, 2.0, 0.5, key="a11")
        a12 = st.number_input("a₁₂", -10.0, 10.0, 1.0, 0.5, key="a12")
        a21 = st.number_input("a₂₁", -10.0, 10.0, 3.0, 0.5, key="a21")
        a22 = st.number_input("a₂₂", -10.0, 10.0, 4.0, 0.5, key="a22")
    
    with col2:
        st.markdown("**Matrix B:**")
        b11 = st.number_input("b₁₁", -10.0, 10.0, 1.0, 0.5, key="b11")
        b12 = st.number_input("b₁₂", -10.0, 10.0, 0.0, 0.5, key="b12")
        b21 = st.number_input("b₂₁", -10.0, 10.0, 0.0, 0.5, key="b21")
        b22 = st.number_input("b₂₂", -10.0, 10.0, 1.0, 0.5, key="b22")
    
    A = np.array([[a11, a12], [a21, a22]])
    B = np.array([[b11, b12], [b21, b22]])
    
    # Calculate operations
    A_plus_B = A + B
    AB = A @ B
    det_A = np.linalg.det(A)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**A + B:**")
        st.code(f"[{A_plus_B[0,0]:.1f}  {A_plus_B[0,1]:.1f}]\n[{A_plus_B[1,0]:.1f}  {A_plus_B[1,1]:.1f}]")
    with col2:
        st.markdown("**AB:**")
        st.code(f"[{AB[0,0]:.1f}  {AB[0,1]:.1f}]\n[{AB[1,0]:.1f}  {AB[1,1]:.1f}]")
    with col3:
        st.metric("det(A)", f"{det_A:.2f}")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Determinants")
    
    st.markdown("""
    **Determinant Properties:**  

        • det(AB) = det(A)·det(B)  

        • det(Aᵀ) = det(A)  

        • det(A⁻¹) = 1/det(A)  

        • det(cA) = cⁿ·det(A) for n×n matrix


        
        **2×2 Matrix:**  

        det([a b; c d]) = ad - bc


        
        **3×3 Matrix (Cofactor expansion):**  

        det(A) = a₁₁C₁₁ + a₁₂C₁₂ + a₁₃C₁₃
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Matrix Inverse")
    
    st.markdown("""
    **Inverse Matrix:**  

        A is invertible if ∃ A⁻¹ such that AA⁻¹ = A⁻¹A = I


        
        **Conditions for Invertibility:**  

        • det(A) ≠ 0  

        • Columns are linearly independent  

        • Rows are linearly independent  

        • rank(A) = n for n×n matrix


        
        **2×2 Inverse:**  

        A⁻¹ = (1/det(A)) × [d -b; -c a] for A = [a b; c d]
    """)
    
    if abs(det_A) > 0.01:
        A_inv = np.linalg.inv(A)
        st.markdown("**A⁻¹:**")
        st.code(f"[{A_inv[0,0]:.3f}  {A_inv[0,1]:.3f}]\n[{A_inv[1,0]:.3f}  {A_inv[1,1]:.3f}]")
    else:
        st.warning("⚠️ Matrix A is singular (det ≈ 0), inverse does not exist")

# ==================== TAB 4: LINEAR SYSTEMS ====================
with tabs[3]:
    st.markdown("## 🎯 Linear Systems")
    
    st.markdown("### 1️⃣ Solving Linear Systems")
    
    st.markdown("""
    **System of Linear Equations:**
    
    Ax = b
    
    where A is m×n matrix, x is n×1 vector, b is m×1 vector
    
    **Solution Types:**
    - **Unique solution:** rank(A) = rank([A|b]) = n
    - **Infinite solutions:** rank(A) = rank([A|b]) < n
    - **No solution:** rank(A) < rank([A|b])
    """)
    
    # Interactive linear system solver
    st.markdown("#### 🧮 2×2 Linear System Solver")
    st.markdown("Solve: Ax = b")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Coefficient Matrix A:**")
        st.code(f"[{a11:.1f}  {a12:.1f}]\n[{a21:.1f}  {a22:.1f}]")
    with col2:
        st.markdown("**Right-hand side b:**")
        b1 = st.number_input("b₁", -10.0, 10.0, 5.0, 0.5)
        b2 = st.number_input("b₂", -10.0, 10.0, 7.0, 0.5)
    
    b_vec = np.array([b1, b2])
    
    if abs(det_A) > 0.01:
        x_solution = np.linalg.solve(A, b_vec)
        st.success(f"**Solution:** x = [{x_solution[0]:.3f}, {x_solution[1]:.3f}]ᵀ")
        
        # Verify
        Ax = A @ x_solution
        st.info(f"**Verification:** Ax = [{Ax[0]:.3f}, {Ax[1]:.3f}]ᵀ ≈ b")
    else:
        st.error("System is singular (det(A) ≈ 0). No unique solution exists.")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Gaussian Elimination")
    
    st.markdown("""
    **Row Operations:**  

        1. Swap two rows  

        2. Multiply a row by a non-zero scalar  

        3. Add a multiple of one row to another


        
        **Row Echelon Form (REF):**  

        • All zero rows at bottom  

        • Leading entry of each row is to the right of the one above


        
        **Reduced Row Echelon Form (RREF):**  

        • REF conditions  

        • Leading entry in each row is 1  

        • Leading 1 is only non-zero entry in its column
    """)

# ==================== TAB 5: LINEAR TRANSFORMATIONS ====================
with tabs[4]:
    st.markdown("## 🔄 Linear Transformations")
    
    st.markdown("### 1️⃣ Definition")
    
    st.markdown("""
    **Linear Transformation T: V → W**  

        T is linear if for all u, v ∈ V and c ∈ ℝ:


        1. T(u + v) = T(u) + T(v) (Additivity)  

        2. T(cu) = cT(u) (Homogeneity)


        
        **Matrix Representation:**  

        Every linear transformation T: ℝⁿ → ℝᵐ can be represented as:  

        T(x) = Ax for some m×n matrix A
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Common Transformations in ℝ²")
    
    transformation_type = st.selectbox("Select Transformation", 
                                       ["Rotation", "Scaling", "Reflection", "Shear"])
    
    if transformation_type == "Rotation":
        angle = st.slider("Rotation angle (degrees)", 0, 360, 45)
        theta = np.radians(angle)
        T = np.array([[np.cos(theta), -np.sin(theta)],
                      [np.sin(theta), np.cos(theta)]])
        st.markdown(f"**Rotation by {angle}°**")
    elif transformation_type == "Scaling":
        sx = st.slider("Scale x", 0.1, 3.0, 1.5, 0.1)
        sy = st.slider("Scale y", 0.1, 3.0, 1.5, 0.1)
        T = np.array([[sx, 0], [0, sy]])
        st.markdown(f"**Scaling: x by {sx}, y by {sy}**")
    elif transformation_type == "Reflection":
        axis = st.radio("Reflection axis", ["x-axis", "y-axis", "y=x"])
        if axis == "x-axis":
            T = np.array([[1, 0], [0, -1]])
        elif axis == "y-axis":
            T = np.array([[-1, 0], [0, 1]])
        else:  # y=x
            T = np.array([[0, 1], [1, 0]])
        st.markdown(f"**Reflection across {axis}**")
    else:  # Shear
        k = st.slider("Shear factor", -2.0, 2.0, 0.5, 0.1)
        T = np.array([[1, k], [0, 1]])
        st.markdown(f"**Horizontal shear by {k}**")
    
    st.code(f"T = [{T[0,0]:.2f}  {T[0,1]:.2f}]\n    [{T[1,0]:.2f}  {T[1,1]:.2f}]")
    
    # Visualize transformation
    st.markdown("#### Transformation Visualization")
    
    # Original unit square
    square = np.array([[0, 1, 1, 0, 0],
                       [0, 0, 1, 1, 0]])
    
    # Transformed square
    transformed = T @ square
    
    # Create visualization data
    viz_data = []
    for i in range(5):
        viz_data.append({'x': square[0,i], 'y': square[1,i], 'type': 'Original'})
        viz_data.append({'x': transformed[0,i], 'y': transformed[1,i], 'type': 'Transformed'})
    
    df_transform = pd.DataFrame(viz_data)
    
    transform_chart = alt.Chart(df_transform).mark_line(strokeWidth=3).encode(
        x=alt.X('x:Q', scale=alt.Scale(domain=[-3, 3]), title='x'),
        y=alt.Y('y:Q', scale=alt.Scale(domain=[-3, 3]), title='y'),
        color=alt.Color('type:N', scale=alt.Scale(domain=['Original', 'Transformed'],
                                                    range=['#ec4899', '#3b82f6'])),
        order='x:Q'
    ).properties(
        width=600,
        height=600,
        title="Linear Transformation"
    )
    
    st.altair_chart(transform_chart, use_container_width=True)

# ==================== TAB 6: EIGENVALUES ====================
with tabs[5]:
    st.markdown("## ⚡ Eigenvalues & Eigenvectors")
    
    st.markdown("### 1️⃣ Definition")
    
    st.markdown("""
    **Eigenvalue and Eigenvector:**  

        For matrix A, scalar λ is an eigenvalue and v ≠ 0 is an eigenvector if:  

        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            Av = λv
        
        **Characteristic Equation:**  

        det(A - λI) = 0


        
        **Properties:**  

        • Sum of eigenvalues = trace(A)  

        • Product of eigenvalues = det(A)  

        • Eigenvectors for different eigenvalues are linearly independent
    """)
    
    # Eigenvalue calculator
    st.markdown("#### 🧮 Eigenvalue Calculator (2×2)")
    
    st.markdown("**Matrix A:**")
    st.code(f"[{a11:.1f}  {a12:.1f}]\n[{a21:.1f}  {a22:.1f}]")
    
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Eigenvalues:**")
        st.metric("λ₁", f"{eigenvalues[0]:.3f}")
        st.metric("λ₂", f"{eigenvalues[1]:.3f}")
    
    with col2:
        st.markdown("**Eigenvectors:**")
        st.code(f"v₁ = [{eigenvectors[0,0]:.3f}]\n     [{eigenvectors[1,0]:.3f}]")
        st.code(f"v₂ = [{eigenvectors[0,1]:.3f}]\n     [{eigenvectors[1,1]:.3f}]")
    
    # Verify
    Av1 = A @ eigenvectors[:,0]
    λv1 = eigenvalues[0] * eigenvectors[:,0]
    st.info(f"**Verification:** Av₁ = [{Av1[0]:.3f}, {Av1[1]:.3f}]ᵀ ≈ λ₁v₁ = [{λv1[0]:.3f}, {λv1[1]:.3f}]ᵀ")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Diagonalization")
    
    st.markdown("""
    **Diagonalization:**  

        Matrix A is diagonalizable if A = PDP⁻¹ where:  

        • D is diagonal matrix of eigenvalues  

        • P is matrix of eigenvectors


        
        **Conditions:**  

        • A has n linearly independent eigenvectors  

        • Symmetric matrices are always diagonalizable


        
        **Applications:**  

        • Computing Aⁿ = PDⁿP⁻¹  

        • Solving differential equations  

        • Principal Component Analysis (PCA)
    """)

# ==================== TAB 7: ORTHOGONALITY ====================
with tabs[6]:
    st.markdown("## 📊 Orthogonality")
    
    st.markdown("### 1️⃣ Inner Products")
    
    st.markdown("""
    **Inner Product (Dot Product):**  

        ⟨u, v⟩ = u·v = u₁v₁ + u₂v₂ + ... + uₙvₙ = uᵀv


        
        **Properties:**  

        • ⟨u, v⟩ = ⟨v, u⟩ (Symmetry)  

        • ⟨u + v, w⟩ = ⟨u, w⟩ + ⟨v, w⟩ (Linearity)  

        • ⟨cu, v⟩ = c⟨u, v⟩  

        • ⟨u, u⟩ ≥ 0, equality iff u = 0


        
        **Orthogonality:**  

        Vectors u and v are orthogonal if ⟨u, v⟩ = 0
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Gram-Schmidt Process")
    
    st.markdown("""
    **Gram-Schmidt Orthogonalization:**  

        Given linearly independent vectors {v₁, v₂, ..., vₙ}, construct orthogonal {u₁, u₂, ..., uₙ}:


        
        u₁ = v₁  

        u₂ = v₂ - proj_{u₁}(v₂)  

        u₃ = v₃ - proj_{u₁}(v₃) - proj_{u₂}(v₃)  

        ...


        
        where proj_u(v) = (⟨v,u⟩/⟨u,u⟩)u


        
        **Orthonormal basis:**  

        Normalize: eᵢ = uᵢ/||uᵢ||
    """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Orthogonal Projections")
    
    st.markdown("""
    **Projection onto subspace W:**  

        proj_W(v) = (vᵀu₁)u₁ + (vᵀu₂)u₂ + ... + (vᵀuₖ)uₖ  

        where {u₁, u₂, ..., uₖ} is orthonormal basis for W


        
        **Least Squares:**  

        Best approximation to Ax = b when no exact solution exists:  

        x̂ = (AᵀA)⁻¹Aᵀb (Normal equation)
    """)

# ==================== TAB 8: SVD ====================
with tabs[7]:
    st.markdown("## 🎨 SVD & Decompositions")
    
    st.markdown("### 1️⃣ Singular Value Decomposition")
    
    st.markdown("""
    **SVD Theorem:**  

        Every m×n matrix A can be factored as:  

        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            A = UΣVᵀ
        
        where:  

        • U is m×m orthogonal matrix (left singular vectors)  

        • Σ is m×n diagonal matrix (singular values σ₁ ≥ σ₂ ≥ ... ≥ 0)  

        • V is n×n orthogonal matrix (right singular vectors)


        
        **Properties:**  

        • Singular values are square roots of eigenvalues of AᵀA  

        • rank(A) = number of non-zero singular values  

        • ||A||₂ = σ₁ (largest singular value)
    """)
    
    # SVD calculator
    st.markdown("#### 🧮 SVD Calculator (2×2)")
    
    st.markdown("**Matrix A:**")
    st.code(f"[{a11:.1f}  {a12:.1f}]\n[{a21:.1f}  {a22:.1f}]")
    
    U, S, Vt = np.linalg.svd(A)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**U:**")
        st.code(f"[{U[0,0]:.3f}  {U[0,1]:.3f}]\n[{U[1,0]:.3f}  {U[1,1]:.3f}]")
    with col2:
        st.markdown("**Σ:**")
        st.code(f"[{S[0]:.3f}  0]\n[0  {S[1]:.3f}]")
    with col3:
        st.markdown("**Vᵀ:**")
        st.code(f"[{Vt[0,0]:.3f}  {Vt[0,1]:.3f}]\n[{Vt[1,0]:.3f}  {Vt[1,1]:.3f}]")
    
    st.metric("Condition Number", f"{S[0]/S[1]:.2f}" if S[1] > 0.001 else "∞")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Applications of SVD")
    
    st.markdown("""
    **Data Compression:**  

        Low-rank approximation: A ≈ Σᵢ₌₁ᵏ σᵢuᵢvᵢᵀ (keep top k singular values)


        
        **Principal Component Analysis (PCA):**  

        Find directions of maximum variance in data


        
        **Pseudoinverse:**  

        A⁺ = VΣ⁺Uᵀ where Σ⁺ has 1/σᵢ on diagonal


        
        **Image Processing:**  

        Noise reduction, feature extraction, compression
    """)

# ==================== TAB 9: APPLICATIONS ====================
with tabs[8]:
    st.markdown("## 🧮 Applications")
    
    st.markdown("### 1️⃣ Machine Learning")
    
    st.markdown("""
    **Principal Component Analysis (PCA):**  

        • Dimensionality reduction  

        • Feature extraction  

        • Data visualization  

        • Uses eigendecomposition of covariance matrix


        
        **Linear Regression:**  

        • Minimize ||Ax - b||²  

        • Solution: x = (AᵀA)⁻¹Aᵀb  

        • Uses least squares and pseudoinverse


        
        **Recommender Systems:**  

        • Matrix factorization  

        • SVD for collaborative filtering  

        • Low-rank approximations
    """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Computer Graphics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **3D Transformations:**
        - Rotation matrices
        - Scaling and translation
        - Perspective projection
        - Homogeneous coordinates
        """)
    
    with col2:
        st.markdown("""
        **Image Processing:**
        - Image compression (SVD)
        - Edge detection
        - Image transformations
        - Color space conversions
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Network Analysis")
    
    st.markdown("""
    **PageRank Algorithm:**  

        • Google's ranking algorithm  

        • Uses eigenvector of adjacency matrix  

        • Dominant eigenvector gives importance scores


        
        **Graph Theory:**  

        • Adjacency matrices  

        • Spectral graph theory  

        • Community detection  

        • Network centrality measures
    """)

# ==================== TAB 10: PRACTICE PROBLEMS ====================
with tabs[9]:
    st.markdown("## 🎯 Practice Problems")
    
    problems = [
        {
            "title": "Problem 1: Vector Operations",
            "question": "Given u = [3, -2, 1] and v = [1, 4, -2], find: (a) u + 2v, (b) u·v, (c) ||u||",
            "hint": "Use vector addition, dot product, and norm formulas",
            "solution": """
(a) u + 2v = [3, -2, 1] + 2[1, 4, -2]
           = [3, -2, 1] + [2, 8, -4]
           = [5, 6, -3]

(b) u·v = 3(1) + (-2)(4) + 1(-2)
        = 3 - 8 - 2
        = -7

(c) ||u|| = √(3² + (-2)² + 1²)
          = √(9 + 4 + 1)
          = √14 ≈ 3.742
            """
        },
        {
            "title": "Problem 2: Matrix Multiplication",
            "question": "Compute AB where A = [1 2; 3 4] and B = [2 0; 1 3]",
            "hint": "(AB)ᵢⱼ = Σₖ aᵢₖbₖⱼ",
            "solution": """
AB = [1 2] [2 0]
     [3 4] [1 3]

(AB)₁₁ = 1(2) + 2(1) = 2 + 2 = 4
(AB)₁₂ = 1(0) + 2(3) = 0 + 6 = 6
(AB)₂₁ = 3(2) + 4(1) = 6 + 4 = 10
(AB)₂₂ = 3(0) + 4(3) = 0 + 12 = 12

AB = [4  6]
     [10 12]
            """
        },
        {
            "title": "Problem 3: Eigenvalues",
            "question": "Find eigenvalues of A = [4 2; 1 3]",
            "hint": "Solve det(A - λI) = 0",
            "solution": """
det(A - λI) = det([4-λ  2  ])
                  [1    3-λ])

= (4-λ)(3-λ) - 2(1)
= 12 - 4λ - 3λ + λ² - 2
= λ² - 7λ + 10
= (λ - 5)(λ - 2)

Eigenvalues: λ₁ = 5, λ₂ = 2
            """
        }
    ]
    
    for idx, problem in enumerate(problems, 1):
        with st.expander(f"📝 {problem['title']}", expanded=False):
            st.markdown(f"**Question:** {problem['question']}")
            
            if st.button(f"Show Hint", key=f"hint_{idx}"):
                st.info(f"💡 {problem['hint']}")
            
            if st.button(f"Show Solution", key=f"sol_{idx}"):
                st.code(problem['solution'])

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    **MA102 - Linear Algebra**  

    <small>UTel University | Department of Mathematics</small>
""")
