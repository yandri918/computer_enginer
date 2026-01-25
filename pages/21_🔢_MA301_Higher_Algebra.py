import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="MA301 - Higher Algebra", page_icon="🔢", layout="wide")

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
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
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
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .definition-box {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .theorem-box {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .example-box {
        background: linear-gradient(135deg, #fce7f3 0%, #fbcfe8 100%);
        border-left: 5px solid #ec4899;
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
    <div style="font-size: 1.2rem; opacity: 0.9;">MA301</div>
    <div class="course-title">Higher Algebra</div>
    <div>🔢 3 Credits | Semester 5 | Abstract Algebra</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "5")
with col3:
    st.metric("Difficulty", "6/7")
with col4:
    st.metric("Hours/Week", "8")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "👥 Group Theory",
    "💍 Ring Theory",
    "🌾 Field Theory",
    "📐 Vector Spaces",
    "🔄 Linear Transformations",
    "🎯 Applications",
    "📝 Practice Problems",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Advanced study of algebraic structures including groups, rings, fields, and vector spaces. Covers group theory 
        (subgroups, homomorphisms, quotient groups), ring theory (ideals, polynomial rings), field theory (field extensions, 
        Galois theory), and linear algebra (vector spaces, linear transformations, eigenvalues). Emphasizes abstract thinking, 
        rigorous proofs, and applications to cryptography, coding theory, and quantum mechanics.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Understand and prove properties of groups, rings, and fields",
        "Apply group theory to symmetry and cryptography",
        "Work with polynomial rings and ideals",
        "Understand field extensions and Galois theory",
        "Master vector spaces and linear transformations",
        "Compute eigenvalues and eigenvectors",
        "Apply abstract algebra to real-world problems",
        "Write rigorous mathematical proofs"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Group Theory:**
        - Groups and subgroups
        - Cyclic groups
        - Permutation groups
        - Cosets and Lagrange's theorem
        - Normal subgroups and quotient groups
        - Group homomorphisms and isomorphisms
        
        **Ring Theory:**
        - Rings and subrings
        - Integral domains and fields
        - Ideals and quotient rings
        - Polynomial rings
        - Unique factorization domains
        """)
    
    with col2:
        st.markdown("""
        **Field Theory:**
        - Field extensions
        - Algebraic and transcendental elements
        - Splitting fields
        - Galois theory basics
        
        **Linear Algebra:**
        - Vector spaces and subspaces
        - Linear independence and basis
        - Linear transformations
        - Eigenvalues and eigenvectors
        - Diagonalization
        - Inner product spaces
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Abstract Algebra", "author": "Dummit & Foote", "type": "Textbook"},
        {"title": "A First Course in Abstract Algebra", "author": "John B. Fraleigh", "type": "Textbook"},
        {"title": "Linear Algebra Done Right", "author": "Sheldon Axler", "type": "Linear Algebra"},
        {"title": "Algebra", "author": "Michael Artin", "type": "Advanced"}
    ]
    
    for resource in resources:
        title = resource['title']
        author = resource['author']
        rtype = resource['type']
        st.markdown(f"📖 **{title}** by {author} ({rtype})")

# ==================== TAB 2: GROUP THEORY ====================
with tabs[1]:
    st.markdown("## 👥 Group Theory")
    
    st.markdown("### 1️⃣ Definition of a Group")
    
    st.markdown("""
    <div class="definition-box">
        <strong>Group (G, ∗):</strong><br>
        A set G with binary operation ∗ satisfying:<br><br>
        
        <strong>1. Closure:</strong><br>
        ∀ a, b ∈ G: a ∗ b ∈ G<br><br>
        
        <strong>2. Associativity:</strong><br>
        ∀ a, b, c ∈ G: (a ∗ b) ∗ c = a ∗ (b ∗ c)<br><br>
        
        <strong>3. Identity:</strong><br>
        ∃ e ∈ G such that ∀ a ∈ G: e ∗ a = a ∗ e = a<br><br>
        
        <strong>4. Inverse:</strong><br>
        ∀ a ∈ G, ∃ a⁻¹ ∈ G such that a ∗ a⁻¹ = a⁻¹ ∗ a = e
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Examples of Groups")
    
    st.markdown("""
    <div class="example-box">
        <strong>(ℤ, +):</strong> Integers under addition<br>
        • Identity: 0<br>
        • Inverse of n: -n<br>
        • Abelian (commutative)<br><br>
        
        <strong>(ℚ*, ×):</strong> Non-zero rationals under multiplication<br>
        • Identity: 1<br>
        • Inverse of a/b: b/a<br>
        • Abelian<br><br>
        
        <strong>S₃:</strong> Symmetric group on 3 elements<br>
        • All permutations of {1, 2, 3}<br>
        • |S₃| = 3! = 6<br>
        • Non-abelian<br><br>
        
        <strong>GL(n, ℝ):</strong> General linear group<br>
        • n×n invertible matrices over ℝ<br>
        • Operation: matrix multiplication<br>
        • Non-abelian for n ≥ 2
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Subgroups")
    
    st.markdown("""
    <div class="theorem-box">
        <strong>Subgroup Test:</strong><br>
        H ⊆ G is a subgroup if:<br>
        1. H is non-empty<br>
        2. ∀ a, b ∈ H: ab ∈ H (closure)<br>
        3. ∀ a ∈ H: a⁻¹ ∈ H (inverses)<br><br>
        
        <strong>Lagrange's Theorem:</strong><br>
        If H is a subgroup of finite group G, then |H| divides |G|<br><br>
        
        <strong>Corollary:</strong><br>
        • Order of any element divides |G|<br>
        • If |G| is prime, G is cyclic
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Group Homomorphisms")
    
    st.markdown("""
    <div class="definition-box">
        <strong>Homomorphism φ: G → H:</strong><br>
        φ(ab) = φ(a)φ(b) for all a, b ∈ G<br><br>
        
        <strong>Properties:</strong><br>
        • φ(e_G) = e_H (maps identity to identity)<br>
        • φ(a⁻¹) = φ(a)⁻¹ (preserves inverses)<br><br>
        
        <strong>Kernel:</strong> ker(φ) = {g ∈ G : φ(g) = e_H}<br>
        • ker(φ) is a normal subgroup of G<br><br>
        
        <strong>Image:</strong> Im(φ) = {φ(g) : g ∈ G}<br>
        • Im(φ) is a subgroup of H<br><br>
        
        <strong>First Isomorphism Theorem:</strong><br>
        G/ker(φ) ≅ Im(φ)
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: RING THEORY ====================
with tabs[2]:
    st.markdown("## 💍 Ring Theory")
    
    st.markdown("### 1️⃣ Definition of a Ring")
    
    st.markdown("""
    <div class="definition-box">
        <strong>Ring (R, +, ×):</strong><br>
        A set R with two operations + and × satisfying:<br><br>
        
        <strong>1. (R, +) is an abelian group:</strong><br>
        • Closure, associativity, identity (0), inverses<br>
        • Commutativity: a + b = b + a<br><br>
        
        <strong>2. (R, ×) is a monoid:</strong><br>
        • Closure: ab ∈ R<br>
        • Associativity: (ab)c = a(bc)<br>
        • Identity: ∃ 1 ∈ R (for rings with unity)<br><br>
        
        <strong>3. Distributivity:</strong><br>
        • a(b + c) = ab + ac<br>
        • (a + b)c = ac + bc
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Types of Rings")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Commutative Ring:</strong><br>
        ab = ba for all a, b ∈ R<br><br>
        
        <strong>Integral Domain:</strong><br>
        • Commutative ring with unity<br>
        • No zero divisors: ab = 0 ⟹ a = 0 or b = 0<br>
        • Examples: ℤ, ℤ[x], ℚ, ℝ, ℂ<br><br>
        
        <strong>Field:</strong><br>
        • Integral domain<br>
        • Every non-zero element has multiplicative inverse<br>
        • Examples: ℚ, ℝ, ℂ, ℤ_p (p prime)<br><br>
        
        <strong>Division Ring:</strong><br>
        • Ring with unity<br>
        • Every non-zero element has inverse<br>
        • Not necessarily commutative<br>
        • Example: Quaternions ℍ
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Ideals")
    
    st.markdown("""
    <div class="definition-box">
        <strong>Ideal I of ring R:</strong><br>
        1. (I, +) is a subgroup of (R, +)<br>
        2. ∀ r ∈ R, ∀ a ∈ I: ra ∈ I and ar ∈ I<br><br>
        
        <strong>Principal Ideal:</strong><br>
        Generated by single element a<br>
        (a) = {ra : r ∈ R} (in commutative ring)<br><br>
        
        <strong>Prime Ideal P:</strong><br>
        ab ∈ P ⟹ a ∈ P or b ∈ P<br><br>
        
        <strong>Maximal Ideal M:</strong><br>
        No proper ideal contains M except R<br><br>
        
        <strong>Theorem:</strong><br>
        • M is maximal ⟺ R/M is a field<br>
        • P is prime ⟺ R/P is an integral domain
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Polynomial Rings")
    
    st.markdown("""
    <div class="example-box">
        <strong>R[x]:</strong> Polynomials with coefficients in R<br><br>
        
        <strong>Degree:</strong><br>
        deg(f) = highest power of x with non-zero coefficient<br>
        deg(fg) = deg(f) + deg(g) (if R is integral domain)<br><br>
        
        <strong>Division Algorithm (F[x], F a field):</strong><br>
        For f, g ∈ F[x] with g ≠ 0:<br>
        ∃ unique q, r such that f = qg + r with deg(r) < deg(g)<br><br>
        
        <strong>Irreducible Polynomials:</strong><br>
        Cannot be factored into non-constant polynomials<br>
        • Over ℝ: degree 1 or irreducible quadratics<br>
        • Over ℂ: only degree 1 (Fundamental Theorem of Algebra)
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: FIELD THEORY ====================
with tabs[3]:
    st.markdown("## 🌾 Field Theory")
    
    st.markdown("### 1️⃣ Field Extensions")
    
    st.markdown("""
    <div class="definition-box">
        <strong>Field Extension E/F:</strong><br>
        F ⊆ E, both fields<br><br>
        
        <strong>Degree [E:F]:</strong><br>
        Dimension of E as vector space over F<br><br>
        
        <strong>Tower Law:</strong><br>
        If K/E/F, then [K:F] = [K:E][E:F]<br><br>
        
        <strong>Examples:</strong><br>
        • ℂ/ℝ: [ℂ:ℝ] = 2<br>
        • ℚ(√2)/ℚ: [ℚ(√2):ℚ] = 2<br>
        • ℚ(∛2)/ℚ: [ℚ(∛2):ℚ] = 3
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Algebraic Elements")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Algebraic Element α over F:</strong><br>
        ∃ non-zero polynomial f ∈ F[x] such that f(α) = 0<br><br>
        
        <strong>Minimal Polynomial:</strong><br>
        Unique monic irreducible polynomial m(x) ∈ F[x] with m(α) = 0<br>
        • deg(m) = [F(α):F]<br>
        • m(x) divides any polynomial with α as root<br><br>
        
        <strong>Transcendental Element:</strong><br>
        Not algebraic<br>
        • Examples: π, e over ℚ<br><br>
        
        <strong>Algebraic Extension:</strong><br>
        Every element is algebraic over F
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Splitting Fields")
    
    st.markdown("""
    <div class="definition-box">
        <strong>Splitting Field of f(x) over F:</strong><br>
        Smallest field E containing F where f(x) splits completely<br><br>
        
        <strong>Example:</strong><br>
        f(x) = x² + 1 over ℝ<br>
        Splitting field: ℂ = ℝ(i)<br>
        f(x) = (x - i)(x + i) in ℂ[x]<br><br>
        
        <strong>Theorem:</strong><br>
        Splitting field exists and is unique up to isomorphism
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Galois Theory Basics")
    
    st.markdown("""
    <div class="theorem-box">
        <strong>Galois Group Gal(E/F):</strong><br>
        Group of automorphisms of E that fix F<br><br>
        
        <strong>Fundamental Theorem of Galois Theory:</strong><br>
        For Galois extension E/F:<br>
        • Bijection between subgroups of Gal(E/F) and intermediate fields<br>
        • [E:F] = |Gal(E/F)|<br><br>
        
        <strong>Applications:</strong><br>
        • Prove impossibility of solving quintic by radicals<br>
        • Impossibility of trisecting angle with compass and straightedge<br>
        • Impossibility of doubling the cube
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: VECTOR SPACES ====================
with tabs[4]:
    st.markdown("## 📐 Vector Spaces")
    
    st.markdown("### 1️⃣ Definition")
    
    st.markdown("""
    <div class="definition-box">
        <strong>Vector Space V over field F:</strong><br>
        Set V with operations + (addition) and · (scalar multiplication)<br><br>
        
        <strong>Vector Addition:</strong><br>
        1. Closure: u + v ∈ V<br>
        2. Associativity: (u + v) + w = u + (v + w)<br>
        3. Identity: ∃ 0 ∈ V<br>
        4. Inverses: ∀ v ∈ V, ∃ -v<br>
        5. Commutativity: u + v = v + u<br><br>
        
        <strong>Scalar Multiplication:</strong><br>
        6. Closure: c·v ∈ V<br>
        7. Distributivity: c·(u + v) = c·u + c·v<br>
        8. Distributivity: (c + d)·v = c·v + d·v<br>
        9. Associativity: (cd)·v = c·(d·v)<br>
        10. Identity: 1·v = v
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Basis and Dimension")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Linear Independence:</strong><br>
        Vectors v₁, ..., vₙ are linearly independent if:<br>
        c₁v₁ + ... + cₙvₙ = 0 ⟹ c₁ = ... = cₙ = 0<br><br>
        
        <strong>Span:</strong><br>
        span{v₁, ..., vₙ} = {c₁v₁ + ... + cₙvₙ : cᵢ ∈ F}<br><br>
        
        <strong>Basis:</strong><br>
        Linearly independent set that spans V<br>
        • Every vector has unique representation<br>
        • All bases have same cardinality<br><br>
        
        <strong>Dimension:</strong><br>
        dim(V) = number of vectors in any basis<br><br>
        
        <strong>Examples:</strong><br>
        • ℝⁿ: dim = n, standard basis {e₁, ..., eₙ}<br>
        • Pₙ(ℝ): dim = n+1, basis {1, x, x², ..., xⁿ}<br>
        • Mₘₓₙ(ℝ): dim = mn
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Subspaces")
    
    st.markdown("""
    <div class="definition-box">
        <strong>Subspace W of V:</strong><br>
        1. 0 ∈ W<br>
        2. Closed under addition: u, v ∈ W ⟹ u + v ∈ W<br>
        3. Closed under scalar multiplication: v ∈ W, c ∈ F ⟹ cv ∈ W<br><br>
        
        <strong>Dimension Theorem:</strong><br>
        If W is subspace of finite-dimensional V:<br>
        dim(W) ≤ dim(V)<br>
        Equality holds ⟺ W = V<br><br>
        
        <strong>Sum of Subspaces:</strong><br>
        W₁ + W₂ = {w₁ + w₂ : w₁ ∈ W₁, w₂ ∈ W₂}<br>
        dim(W₁ + W₂) = dim(W₁) + dim(W₂) - dim(W₁ ∩ W₂)
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: LINEAR TRANSFORMATIONS ====================
with tabs[5]:
    st.markdown("## 🔄 Linear Transformations")
    
    st.markdown("### 1️⃣ Definition")
    
    st.markdown("""
    <div class="definition-box">
        <strong>Linear Transformation T: V → W:</strong><br>
        1. T(u + v) = T(u) + T(v)<br>
        2. T(cv) = cT(v)<br><br>
        
        <strong>Kernel (Null Space):</strong><br>
        ker(T) = {v ∈ V : T(v) = 0}<br>
        • Subspace of V<br><br>
        
        <strong>Image (Range):</strong><br>
        Im(T) = {T(v) : v ∈ V}<br>
        • Subspace of W<br><br>
        
        <strong>Rank-Nullity Theorem:</strong><br>
        dim(V) = dim(ker(T)) + dim(Im(T))<br>
        = nullity + rank
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Matrix Representation")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Matrix of T with respect to bases B, C:</strong><br>
        [T]ᴮᶜ where columns are coordinates of T(bᵢ) in basis C<br><br>
        
        <strong>Change of Basis:</strong><br>
        If P is change of basis matrix:<br>
        [T]ᴮ' = P⁻¹[T]ᴮP<br><br>
        
        <strong>Similar Matrices:</strong><br>
        A and B are similar if ∃ invertible P: B = P⁻¹AP<br>
        • Same eigenvalues<br>
        • Same trace<br>
        • Same determinant
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Eigenvalues and Eigenvectors")
    
    st.markdown("""
    <div class="definition-box">
        <strong>Eigenvalue λ and Eigenvector v:</strong><br>
        Av = λv for v ≠ 0<br><br>
        
        <strong>Characteristic Polynomial:</strong><br>
        det(A - λI) = 0<br>
        Roots are eigenvalues<br><br>
        
        <strong>Eigenspace E_λ:</strong><br>
        E_λ = ker(A - λI)<br>
        = {v : Av = λv}<br><br>
        
        <strong>Algebraic Multiplicity:</strong><br>
        Multiplicity of λ as root of characteristic polynomial<br><br>
        
        <strong>Geometric Multiplicity:</strong><br>
        dim(E_λ)<br>
        Always ≤ algebraic multiplicity
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Diagonalization")
    
    st.markdown("""
    <div class="theorem-box">
        <strong>Diagonalizable Matrix:</strong><br>
        A is diagonalizable if ∃ invertible P: P⁻¹AP = D (diagonal)<br><br>
        
        <strong>Theorem:</strong><br>
        A is diagonalizable ⟺<br>
        Sum of geometric multiplicities = n<br><br>
        
        <strong>Sufficient Conditions:</strong><br>
        • A has n distinct eigenvalues<br>
        • A is symmetric (over ℝ)<br><br>
        
        <strong>Spectral Theorem:</strong><br>
        Every symmetric matrix is orthogonally diagonalizable:<br>
        A = QDQᵀ where Q is orthogonal
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: APPLICATIONS ====================
with tabs[6]:
    st.markdown("## 🎯 Applications")
    
    st.markdown("### 1️⃣ Cryptography")
    
    st.markdown("""
    <div class="example-box">
        <strong>RSA Encryption:</strong><br>
        Based on difficulty of factoring large numbers<br><br>
        
        <strong>Key Generation:</strong><br>
        1. Choose large primes p, q<br>
        2. n = pq<br>
        3. φ(n) = (p-1)(q-1) (Euler's totient)<br>
        4. Choose e with gcd(e, φ(n)) = 1<br>
        5. Find d: ed ≡ 1 (mod φ(n))<br>
        6. Public key: (n, e)<br>
        7. Private key: (n, d)<br><br>
        
        <strong>Encryption:</strong> c ≡ mᵉ (mod n)<br>
        <strong>Decryption:</strong> m ≡ cᵈ (mod n)<br><br>
        
        <strong>Group Theory Application:</strong><br>
        Uses properties of (ℤ/nℤ)* multiplicative group
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Error-Correcting Codes")
    
    st.markdown("""
    <div class="example-box">
        <strong>Linear Codes:</strong><br>
        Subspaces of vector space 𝔽ₚⁿ<br><br>
        
        <strong>Hamming Distance:</strong><br>
        Number of positions where codewords differ<br><br>
        
        <strong>Minimum Distance d:</strong><br>
        • Detect up to d-1 errors<br>
        • Correct up to ⌊(d-1)/2⌋ errors<br><br>
        
        <strong>Generator Matrix G:</strong><br>
        Encode message m: c = mG<br><br>
        
        <strong>Parity Check Matrix H:</strong><br>
        Valid codeword c: Hcᵀ = 0
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Quantum Mechanics")
    
    st.markdown("""
    <div class="example-box">
        <strong>State Vectors:</strong><br>
        Quantum states are vectors in complex Hilbert space<br><br>
        
        <strong>Observables:</strong><br>
        Represented by Hermitian operators<br>
        Eigenvalues = possible measurement outcomes<br><br>
        
        <strong>Pauli Matrices:</strong><br>
        σₓ = [[0,1],[1,0]]<br>
        σᵧ = [[0,-i],[i,0]]<br>
        σᵤ = [[1,0],[0,-1]]<br><br>
        
        <strong>Spin States:</strong><br>
        Eigenspaces of Pauli matrices
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: PRACTICE ====================
with tabs[7]:
    st.markdown("## 📝 Practice Problems")
    
    problems = [
        {
            "title": "Problem 1: Group Theory",
            "question": "Prove that if G is a group and a ∈ G has order n, then aᵏ = e if and only if n divides k.",
            "hint": "Use division algorithm: k = qn + r where 0 ≤ r < n",
            "solution": """
**Proof:**

**(⟹) If aᵏ = e, then n | k:**

By division algorithm: k = qn + r where 0 ≤ r < n

Then: aᵏ = a^(qn+r) = (aⁿ)^q · aʳ = e^q · aʳ = aʳ

Since aᵏ = e, we have aʳ = e

But a has order n (smallest positive integer with aⁿ = e)

Since 0 ≤ r < n and aʳ = e, we must have r = 0

Therefore k = qn, so n | k ✓

**(⟸) If n | k, then aᵏ = e:**

If n | k, then k = qn for some integer q

Then: aᵏ = a^(qn) = (aⁿ)^q = e^q = e ✓

**QED**
            """
        },
        {
            "title": "Problem 2: Linear Algebra",
            "question": "Find eigenvalues and eigenvectors of A = [[3, 1], [0, 2]]",
            "hint": "Solve det(A - λI) = 0 for eigenvalues, then (A - λI)v = 0 for eigenvectors",
            "solution": """
**Solution:**

**Step 1: Find Eigenvalues**

Characteristic polynomial:
det(A - λI) = det([[3-λ, 1], [0, 2-λ]])
= (3-λ)(2-λ) - 0
= (3-λ)(2-λ)
= 0

Eigenvalues: λ₁ = 3, λ₂ = 2

**Step 2: Find Eigenvectors**

**For λ₁ = 3:**
(A - 3I)v = 0
[[0, 1], [0, -1]][[x], [y]] = [[0], [0]]

From second row: -y = 0 → y = 0
x is free

Eigenvector: v₁ = [[1], [0]] (or any scalar multiple)

**For λ₂ = 2:**
(A - 2I)v = 0
[[1, 1], [0, 0]][[x], [y]] = [[0], [0]]

From first row: x + y = 0 → y = -x

Eigenvector: v₂ = [[1], [-1]] (or any scalar multiple)

**Answer:**
- λ₁ = 3 with eigenvector v₁ = [[1], [0]]
- λ₂ = 2 with eigenvector v₂ = [[1], [-1]]
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

# ==================== TAB 9: YOUTUBE ====================
with tabs[8]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning Higher Algebra</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {"title": "Abstract Algebra", "channel": "Socratica", "url": "https://www.youtube.com/playlist?list=PLi01XoE8jYoi3SgnnGorR_XOW3IcK-TP6", "description": "Introduction to abstract algebra", "duration": "Playlist"},
        {"title": "Group Theory", "channel": "MathTheBeautiful", "url": "https://www.youtube.com/playlist?list=PLJb1qAQIrmmCVs6RB2KqA_TpPqzFJmXHC", "description": "Visual group theory", "duration": "Playlist"},
        {"title": "Linear Algebra", "channel": "3Blue1Brown", "url": "https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab", "description": "Essence of linear algebra", "duration": "~3 hours"}
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
        {"title": "Abstract Algebra", "channel": "Harvard Extension School", "url": "https://www.youtube.com/playlist?list=PLA58AC5CABC1321A3", "description": "Complete abstract algebra course", "duration": "Full Course"},
        {"title": "Linear Algebra", "channel": "MIT OpenCourseWare", "url": "https://www.youtube.com/playlist?list=PL221E2BBF13BECF6C", "description": "MIT 18.06 Linear Algebra", "duration": "Full Course"},
        {"title": "Group Theory", "channel": "Richard E Borcherds", "url": "https://www.youtube.com/playlist?list=PL8yHsr3EFj53Zxu3iRGMYL_89GDMvdkgt", "description": "Advanced group theory", "duration": "Playlist"}
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
        {"title": "Galois Theory", "channel": "Richard E Borcherds", "url": "https://www.youtube.com/playlist?list=PL8yHsr3EFj52XDLrmvrFDgwcf6XOm2TEE", "description": "Complete Galois theory", "duration": "Full Course"},
        {"title": "Representation Theory", "channel": "Tobias Osborne", "url": "https://www.youtube.com/playlist?list=PLDfPUNusx1EpWRFTHqVdxJfH8sFs3wkdZ", "description": "Group representations", "duration": "Playlist"},
        {"title": "Commutative Algebra", "channel": "Richard E Borcherds", "url": "https://www.youtube.com/playlist?list=PL8yHsr3EFj51pjBvvCPipgAT3SYpIiIsJ", "description": "Advanced ring theory", "duration": "Full Course"}
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
        1. Review linear algebra (vectors, matrices, determinants)<br>
        2. Learn group theory (groups, subgroups, homomorphisms)<br>
        3. Study ring theory (rings, ideals, polynomial rings)<br>
        4. Understand field theory (extensions, Galois theory)<br>
        5. Master linear transformations and eigenvalues<br>
        6. Practice writing proofs<br>
        7. Work on applications (cryptography, coding theory)<br>
        8. Study advanced topics (representation theory)<br><br>
        
        <strong>Proof Techniques:</strong><br>
        • Direct proof<br>
        • Proof by contradiction<br>
        • Proof by induction<br>
        • Proof by contrapositive<br><br>
        
        <strong>Practice Resources:</strong><br>
        • Dummit & Foote exercises<br>
        • Fraleigh problem sets<br>
        • Math Stack Exchange<br>
        • Abstract Algebra forums
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>MA301 - Higher Algebra</strong><br>
    <small>UTel University | Department of Mathematics</small>
</div>
""", unsafe_allow_html=True)
