import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="MA101 - Calculus", page_icon="📐", layout="wide")

# Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    code {
        font-family: 'JetBrains Mono', monospace;
    }
    
    .course-header {
        background: linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%);
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
    
    .course-code {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    .theory-box {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .formula-box {
        background: #f8fafc;
        border: 2px solid #e2e8f0;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        text-align: center;
        font-size: 1.2rem;
    }
    
    .example-box {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .practice-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .definition {
        background: #faf5ff;
        border-left: 4px solid #8b5cf6;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    
    .theorem {
        background: #fef2f2;
        border-left: 4px solid #ef4444;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="course-header">
    <div class="course-code">MA101</div>
    <div class="course-title">Differential and Integral Calculus</div>
    <div>📐 4 Credits | Semester 1 | Mathematics</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "4")
with col2:
    st.metric("Semester", "1")
with col3:
    st.metric("Difficulty", "5/7")
with col4:
    st.metric("Hours/Week", "6")

st.markdown("---")

# Navigation tabs - Expanded for graduate level
tabs = st.tabs([
    "📚 Overview",
    "📖 Differential Calculus",
    "∫ Integral Calculus",
    "🔬 Multivariable Calculus",
    "∇ Vector Calculus",
    "📐 Differential Equations",
    "🌊 Fourier Analysis",
    "📊 Applications",
    "🎓 Graduate Topics",
    "🧮 Practice Problems",
    "📈 Visualizations"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Fundamental calculus concepts including limits, derivatives, and integrals with applications 
        to engineering and computer science. This course provides the mathematical foundation for 
        advanced topics in algorithms, machine learning, and optimization.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Compute derivatives and integrals of various functions",
        "Solve optimization problems using calculus techniques",
        "Apply calculus to real-world engineering scenarios",
        "Understand limits, continuity, and convergence",
        "Analyze rates of change and accumulation"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Part 1: Differential Calculus**
        - Limits and Continuity
        - Derivatives and Differentiation Rules
        - Chain Rule and Implicit Differentiation
        - Applications: Optimization, Related Rates
        - Higher Order Derivatives
        """)
    
    with col2:
        st.markdown("""
        **Part 2: Integral Calculus**
        - Antiderivatives and Indefinite Integrals
        - Definite Integrals and Riemann Sums
        - Fundamental Theorem of Calculus
        - Integration Techniques
        - Applications: Area, Volume, Work
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Calculus: Early Transcendentals", "author": "James Stewart", "type": "Textbook"},
        {"title": "3Blue1Brown - Essence of Calculus", "author": "Grant Sanderson", "type": "Video Series"},
        {"title": "Khan Academy - Calculus", "author": "Sal Khan", "type": "Online Course"},
        {"title": "MIT OpenCourseWare - Single Variable Calculus", "author": "MIT", "type": "Lectures"}
    ]
    
    for resource in resources:
        st.markdown(f"📖 **{resource['title']}** by {resource['author']} ({resource['type']})")

# ==================== TAB 2: DIFFERENTIAL CALCULUS ====================
with tabs[1]:
    st.markdown("## 📖 Differential Calculus")
    
    # Limits
    st.markdown("### 1️⃣ Limits and Continuity")
    
    st.markdown("""
    <div class="definition">
        <strong>Definition: Limit</strong><br>
        The limit of f(x) as x approaches a is L, written as:<br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            lim<sub>x→a</sub> f(x) = L
        </div>
        if f(x) can be made arbitrarily close to L by making x sufficiently close to a.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="example-box">
        <strong>📝 Example 1: Computing a Limit</strong><br><br>
        Find: lim<sub>x→2</sub> (x² + 3x - 1)<br><br>
        <strong>Solution:</strong><br>
        Simply substitute x = 2:<br>
        = (2)² + 3(2) - 1<br>
        = 4 + 6 - 1<br>
        = <strong>9</strong>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive limit calculator
    st.markdown("#### 🧮 Interactive Limit Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        a_val = st.number_input("Approach value (a)", value=2.0, step=0.1)
    with col2:
        func_type = st.selectbox("Function type", ["Polynomial", "Rational", "Exponential"])
    
    # Generate data for limit visualization
    x_vals = np.linspace(a_val - 2, a_val + 2, 100)
    
    if func_type == "Polynomial":
        y_vals = x_vals**2 + 3*x_vals - 1
        limit_val = a_val**2 + 3*a_val - 1
    elif func_type == "Rational":
        y_vals = (x_vals**2 - 4) / (x_vals - 2) if a_val == 2 else x_vals**2 / x_vals
        limit_val = 4 if a_val == 2 else a_val
    else:  # Exponential
        y_vals = np.exp(x_vals)
        limit_val = np.exp(a_val)
    
    df_limit = pd.DataFrame({'x': x_vals, 'y': y_vals})
    
    # Altair chart
    line = alt.Chart(df_limit).mark_line(color='#3b82f6', strokeWidth=3).encode(
        x=alt.X('x:Q', title='x'),
        y=alt.Y('y:Q', title='f(x)'),
        tooltip=['x', 'y']
    )
    
    # Point at limit
    point_data = pd.DataFrame({'x': [a_val], 'y': [limit_val]})
    point = alt.Chart(point_data).mark_circle(size=200, color='#ef4444').encode(
        x='x:Q',
        y='y:Q',
        tooltip=[alt.Tooltip('x:Q', title='x'), alt.Tooltip('y:Q', title='Limit')]
    )
    
    chart = (line + point).properties(
        width=600,
        height=400,
        title=f"Limit as x → {a_val}"
    ).interactive()
    
    st.altair_chart(chart, use_container_width=True)
    st.info(f"📊 The limit as x → {a_val} is approximately **{limit_val:.2f}**")
    
    # Derivatives
    st.markdown("---")
    st.markdown("### 2️⃣ Derivatives")
    
    st.markdown("""
    <div class="definition">
        <strong>Definition: Derivative</strong><br>
        The derivative of f(x) at x = a is:<br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            f'(a) = lim<sub>h→0</sub> [f(a+h) - f(a)] / h
        </div>
        The derivative represents the instantaneous rate of change.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 📐 Common Derivative Rules")
    
    rules_col1, rules_col2 = st.columns(2)
    
    with rules_col1:
        st.markdown("""
        **Power Rule:**
        - d/dx [xⁿ] = n·xⁿ⁻¹
        
        **Sum Rule:**
        - d/dx [f(x) + g(x)] = f'(x) + g'(x)
        
        **Product Rule:**
        - d/dx [f(x)·g(x)] = f'(x)·g(x) + f(x)·g'(x)
        """)
    
    with rules_col2:
        st.markdown("""
        **Chain Rule:**
        - d/dx [f(g(x))] = f'(g(x))·g'(x)
        
        **Exponential:**
        - d/dx [eˣ] = eˣ
        
        **Logarithm:**
        - d/dx [ln(x)] = 1/x
        """)
    
    st.markdown("""
    <div class="example-box">
        <strong>📝 Example 2: Finding Derivatives</strong><br><br>
        Find the derivative of f(x) = 3x⁴ - 2x² + 5x - 1<br><br>
        <strong>Solution:</strong><br>
        Using the power rule for each term:<br>
        f'(x) = 3·4x³ - 2·2x + 5<br>
        f'(x) = <strong>12x³ - 4x + 5</strong>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive derivative visualizer
    st.markdown("#### 📊 Derivative Visualizer")
    
    func_choice = st.selectbox(
        "Select function to visualize",
        ["x²", "x³", "sin(x)", "eˣ", "ln(x)"]
    )
    
    x_range = np.linspace(-5, 5, 200)
    
    if func_choice == "x²":
        y_func = x_range**2
        y_deriv = 2*x_range
    elif func_choice == "x³":
        y_func = x_range**3
        y_deriv = 3*x_range**2
    elif func_choice == "sin(x)":
        y_func = np.sin(x_range)
        y_deriv = np.cos(x_range)
    elif func_choice == "eˣ":
        y_func = np.exp(x_range)
        y_deriv = np.exp(x_range)
    else:  # ln(x)
        x_range = np.linspace(0.1, 5, 200)
        y_func = np.log(x_range)
        y_deriv = 1/x_range
    
    df_deriv = pd.DataFrame({
        'x': np.concatenate([x_range, x_range]),
        'y': np.concatenate([y_func, y_deriv]),
        'type': ['Function'] * len(x_range) + ['Derivative'] * len(x_range)
    })
    
    deriv_chart = alt.Chart(df_deriv).mark_line(strokeWidth=3).encode(
        x=alt.X('x:Q', title='x'),
        y=alt.Y('y:Q', title='y'),
        color=alt.Color('type:N', scale=alt.Scale(domain=['Function', 'Derivative'], 
                                                    range=['#3b82f6', '#ef4444'])),
        tooltip=['x', 'y', 'type']
    ).properties(
        width=700,
        height=400,
        title=f"f(x) = {func_choice} and its derivative"
    ).interactive()
    
    st.altair_chart(deriv_chart, use_container_width=True)
    
    # Optimization
    st.markdown("---")
    st.markdown("### 3️⃣ Optimization Problems")
    
    st.markdown("""
    <div class="theorem">
        <strong>Theorem: Critical Points</strong><br>
        To find maximum or minimum values of f(x):<br>
        1. Find f'(x)<br>
        2. Set f'(x) = 0 and solve for x (critical points)<br>
        3. Use second derivative test: f''(x) &lt; 0 → maximum, f''(x) &gt; 0 → minimum
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="example-box">
        <strong>📝 Example 3: Optimization</strong><br><br>
        Find the dimensions of a rectangle with perimeter 100m that maximizes area.<br><br>
        <strong>Solution:</strong><br>
        Let x = length, y = width<br>
        Perimeter: 2x + 2y = 100 → y = 50 - x<br>
        Area: A(x) = x·y = x(50 - x) = 50x - x²<br>
        A'(x) = 50 - 2x<br>
        Set A'(x) = 0: 50 - 2x = 0 → x = 25<br>
        Therefore y = 50 - 25 = 25<br>
        <strong>Answer: 25m × 25m (a square)</strong>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: INTEGRAL CALCULUS ====================
with tabs[2]:
    st.markdown("## ∫ Integral Calculus")
    
    st.markdown("### 1️⃣ Antiderivatives and Indefinite Integrals")
    
    st.markdown("""
    <div class="definition">
        <strong>Definition: Antiderivative</strong><br>
        F(x) is an antiderivative of f(x) if F'(x) = f(x)<br>
        The indefinite integral is:<br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            ∫ f(x) dx = F(x) + C
        </div>
        where C is the constant of integration.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 📐 Common Integration Rules")
    
    int_col1, int_col2 = st.columns(2)
    
    with int_col1:
        st.markdown("""
        **Power Rule:**
        - ∫ xⁿ dx = xⁿ⁺¹/(n+1) + C (n ≠ -1)
        
        **Exponential:**
        - ∫ eˣ dx = eˣ + C
        
        **Trigonometric:**
        - ∫ sin(x) dx = -cos(x) + C
        - ∫ cos(x) dx = sin(x) + C
        """)
    
    with int_col2:
        st.markdown("""
        **Logarithm:**
        - ∫ 1/x dx = ln|x| + C
        
        **Sum Rule:**
        - ∫ [f(x) + g(x)] dx = ∫ f(x) dx + ∫ g(x) dx
        
        **Constant Multiple:**
        - ∫ k·f(x) dx = k·∫ f(x) dx
        """)
    
    st.markdown("""
    <div class="example-box">
        <strong>📝 Example 4: Indefinite Integral</strong><br><br>
        Find: ∫ (3x² + 2x - 5) dx<br><br>
        <strong>Solution:</strong><br>
        ∫ (3x² + 2x - 5) dx<br>
        = 3·∫ x² dx + 2·∫ x dx - 5·∫ 1 dx<br>
        = 3·(x³/3) + 2·(x²/2) - 5x + C<br>
        = <strong>x³ + x² - 5x + C</strong>
    </div>
    """, unsafe_allow_html=True)
    
    # Definite Integrals
    st.markdown("---")
    st.markdown("### 2️⃣ Definite Integrals")
    
    st.markdown("""
    <div class="theorem">
        <strong>Fundamental Theorem of Calculus</strong><br>
        If F(x) is an antiderivative of f(x), then:<br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            ∫<sub>a</sub><sup>b</sup> f(x) dx = F(b) - F(a)
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive Riemann Sum visualizer
    st.markdown("#### 📊 Riemann Sum Visualizer")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        a_int = st.number_input("Lower bound (a)", value=0.0, step=0.5)
    with col2:
        b_int = st.number_input("Upper bound (b)", value=4.0, step=0.5)
    with col3:
        n_rect = st.slider("Number of rectangles", 4, 50, 10)
    
    # Generate Riemann sum data
    x_vals = np.linspace(a_int, b_int, 1000)
    y_vals = x_vals**2  # f(x) = x²
    
    # Rectangle data
    rect_width = (b_int - a_int) / n_rect
    rect_x = []
    rect_y = []
    
    for i in range(n_rect):
        x_left = a_int + i * rect_width
        x_right = x_left + rect_width
        y_height = x_left**2  # Left Riemann sum
        
        rect_x.extend([x_left, x_left, x_right, x_right, x_left, None])
        rect_y.extend([0, y_height, y_height, 0, 0, None])
    
    # Create dataframes
    df_func = pd.DataFrame({'x': x_vals, 'y': y_vals})
    df_rect = pd.DataFrame({'x': rect_x, 'y': rect_y})
    
    # Altair charts
    func_line = alt.Chart(df_func).mark_line(color='#3b82f6', strokeWidth=3).encode(
        x=alt.X('x:Q', title='x'),
        y=alt.Y('y:Q', title='f(x) = x²')
    )
    
    rectangles = alt.Chart(df_rect).mark_line(color='#10b981', strokeWidth=2, opacity=0.5).encode(
        x='x:Q',
        y='y:Q'
    )
    
    riemann_chart = (rectangles + func_line).properties(
        width=700,
        height=400,
        title=f"Riemann Sum Approximation with {n_rect} rectangles"
    ).interactive()
    
    st.altair_chart(riemann_chart, use_container_width=True)
    
    # Calculate actual integral
    actual_integral = (b_int**3 / 3) - (a_int**3 / 3)
    riemann_sum = sum([(a_int + i*rect_width)**2 * rect_width for i in range(n_rect)])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Riemann Sum", f"{riemann_sum:.4f}")
    with col2:
        st.metric("Actual Integral", f"{actual_integral:.4f}")
    with col3:
        error = abs(riemann_sum - actual_integral)
        st.metric("Error", f"{error:.4f}")
    
    st.markdown("""
    <div class="example-box">
        <strong>📝 Example 5: Definite Integral</strong><br><br>
        Evaluate: ∫<sub>0</sub><sup>2</sup> (x² + 1) dx<br><br>
        <strong>Solution:</strong><br>
        First find antiderivative: F(x) = x³/3 + x<br>
        Apply FTC:<br>
        = F(2) - F(0)<br>
        = (2³/3 + 2) - (0³/3 + 0)<br>
        = (8/3 + 2) - 0<br>
        = <strong>14/3 ≈ 4.667</strong>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: MULTIVARIABLE CALCULUS ====================
with tabs[3]:
    st.markdown("## 🔬 Multivariable Calculus")
    
    st.markdown("### 1️⃣ Partial Derivatives")
    
    st.markdown("""
    <div class="definition">
        <strong>Definition: Partial Derivative</strong><br>
        For a function f(x, y), the partial derivatives are:<br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            ∂f/∂x = lim<sub>h→0</sub> [f(x+h, y) - f(x, y)] / h<br>
            ∂f/∂y = lim<sub>h→0</sub> [f(x, y+h) - f(x, y)] / h
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="example-box">
        <strong>📝 Example: Partial Derivatives</strong><br><br>
        Find ∂f/∂x and ∂f/∂y for f(x, y) = x²y + 3xy² - 5<br><br>
        <strong>Solution:</strong><br>
        ∂f/∂x = 2xy + 3y² (treat y as constant)<br>
        ∂f/∂y = x² + 6xy (treat x as constant)
    </div>
    """, unsafe_allow_html=True)
    
    # 3D Surface visualization
    st.markdown("#### 📊 3D Surface Visualization")
    
    func_3d = st.selectbox("Select 3D function", ["x² + y²", "sin(x)cos(y)", "x²y", "e^(-(x²+y²))"])
    
    # Create mesh grid
    x_3d = np.linspace(-3, 3, 50)
    y_3d = np.linspace(-3, 3, 50)
    X, Y = np.meshgrid(x_3d, y_3d)
    
    if func_3d == "x² + y²":
        Z = X**2 + Y**2
    elif func_3d == "sin(x)cos(y)":
        Z = np.sin(X) * np.cos(Y)
    elif func_3d == "x²y":
        Z = X**2 * Y
    else:  # e^(-(x²+y²))
        Z = np.exp(-(X**2 + Y**2))
    
    # Create contour data for Altair
    contour_data = []
    for i in range(len(x_3d)):
        for j in range(len(y_3d)):
            contour_data.append({
                'x': x_3d[i],
                'y': y_3d[j],
                'z': Z[j, i]
            })
    
    df_contour = pd.DataFrame(contour_data)
    
    # Heatmap visualization
    heatmap = alt.Chart(df_contour).mark_rect().encode(
        x=alt.X('x:Q', title='x'),
        y=alt.Y('y:Q', title='y'),
        color=alt.Color('z:Q', scale=alt.Scale(scheme='viridis'), title='f(x,y)'),
        tooltip=['x', 'y', 'z']
    ).properties(
        width=600,
        height=500,
        title=f"Heatmap of f(x,y) = {func_3d}"
    )
    
    st.altair_chart(heatmap, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Gradient and Directional Derivatives")
    
    st.markdown("""
    <div class="theorem">
        <strong>Theorem: Gradient Vector</strong><br>
        The gradient of f(x, y) is:<br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            ∇f = (∂f/∂x, ∂f/∂y)
        </div>
        The gradient points in the direction of steepest ascent.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 3️⃣ Double and Triple Integrals")
    
    st.markdown("""
    <div class="definition">
        <strong>Double Integral</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            ∬<sub>R</sub> f(x,y) dA = ∫<sub>a</sub><sup>b</sup> ∫<sub>c</sub><sup>d</sup> f(x,y) dy dx
        </div>
        Represents volume under the surface f(x,y).
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: VECTOR CALCULUS ====================
with tabs[4]:
    st.markdown("## ∇ Vector Calculus")
    
    st.markdown("### 1️⃣ Vector Fields")
    
    st.markdown("""
    <div class="definition">
        <strong>Vector Field</strong><br>
        A vector field assigns a vector to each point in space:<br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            F(x, y) = P(x,y)i + Q(x,y)j
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Vector field visualization
    st.markdown("#### 🧭 Vector Field Visualization")
    
    field_type = st.selectbox("Select vector field", ["Radial: (x, y)", "Rotational: (-y, x)", "Gradient: (y, x)"])
    
    # Create grid for vector field
    x_vec = np.linspace(-2, 2, 15)
    y_vec = np.linspace(-2, 2, 15)
    X_vec, Y_vec = np.meshgrid(x_vec, y_vec)
    
    if field_type == "Radial: (x, y)":
        U, V = X_vec, Y_vec
    elif field_type == "Rotational: (-y, x)":
        U, V = -Y_vec, X_vec
    else:  # Gradient
        U, V = Y_vec, X_vec
    
    # Normalize for better visualization
    magnitude = np.sqrt(U**2 + V**2)
    U_norm = U / (magnitude + 0.1)
    V_norm = V / (magnitude + 0.1)
    
    # Create arrow data
    arrow_data = []
    for i in range(len(x_vec)):
        for j in range(len(y_vec)):
            arrow_data.append({
                'x': x_vec[i],
                'y': y_vec[j],
                'dx': U_norm[j, i] * 0.2,
                'dy': V_norm[j, i] * 0.2
            })
    
    df_arrows = pd.DataFrame(arrow_data)
    
    st.info(f"🧭 Vector field: F(x,y) = {field_type}")
    st.caption("Note: Arrows show direction and relative magnitude of the vector field")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Line Integrals")
    
    st.markdown("""
    <div class="theorem">
        <strong>Line Integral of a Vector Field</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            ∫<sub>C</sub> F·dr = ∫<sub>a</sub><sup>b</sup> F(r(t))·r'(t) dt
        </div>
        Represents work done by force field F along curve C.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 3️⃣ Green's Theorem")
    
    st.markdown("""
    <div class="theorem">
        <strong>Green's Theorem</strong><br>
        For a positively oriented simple closed curve C and region D:<br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            ∮<sub>C</sub> (P dx + Q dy) = ∬<sub>D</sub> (∂Q/∂x - ∂P/∂y) dA
        </div>
        Relates line integral around curve to double integral over region.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 4️⃣ Divergence and Curl")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Divergence:**
        <div style="text-align: center; margin: 1rem 0;">
            div F = ∇·F = ∂P/∂x + ∂Q/∂y + ∂R/∂z
        </div>
        Measures "outflow" from a point.
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        **Curl:**
        <div style="text-align: center; margin: 1rem 0;">
            curl F = ∇×F
        </div>
        Measures "rotation" of the field.
        """, unsafe_allow_html=True)

# ==================== TAB 6: DIFFERENTIAL EQUATIONS ====================
with tabs[5]:
    st.markdown("## 📐 Differential Equations")
    
    st.markdown("### 1️⃣ First-Order ODEs")
    
    st.markdown("""
    <div class="definition">
        <strong>Separable Differential Equations</strong><br>
        Form: dy/dx = g(x)h(y)<br>
        Solution method: Separate variables and integrate both sides.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="example-box">
        <strong>📝 Example: Separable ODE</strong><br><br>
        Solve: dy/dx = xy<br><br>
        <strong>Solution:</strong><br>
        dy/y = x dx<br>
        ∫ dy/y = ∫ x dx<br>
        ln|y| = x²/2 + C<br>
        y = Ae^(x²/2) where A = e^C
    </div>
    """, unsafe_allow_html=True)
    
    # Direction field visualization
    st.markdown("#### 🎯 Direction Field Visualizer")
    
    de_type = st.selectbox("Select differential equation", ["dy/dx = x", "dy/dx = y", "dy/dx = x - y", "dy/dx = x² + y²"])
    
    x_de = np.linspace(-3, 3, 20)
    y_de = np.linspace(-3, 3, 20)
    X_de, Y_de = np.meshgrid(x_de, y_de)
    
    if de_type == "dy/dx = x":
        slopes = X_de
    elif de_type == "dy/dx = y":
        slopes = Y_de
    elif de_type == "dy/dx = x - y":
        slopes = X_de - Y_de
    else:  # x² + y²
        slopes = X_de**2 + Y_de**2
    
    st.info(f"📊 Direction field for: {de_type}")
    st.caption("Each small line segment shows the slope dy/dx at that point")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Second-Order Linear ODEs")
    
    st.markdown("""
    <div class="theorem">
        <strong>Homogeneous Linear ODE</strong><br>
        Form: ay'' + by' + cy = 0<br>
        Characteristic equation: ar² + br + c = 0<br><br>
        Solutions depend on discriminant b² - 4ac:<br>
        • b² - 4ac > 0: y = C₁e^(r₁x) + C₂e^(r₂x)<br>
        • b² - 4ac = 0: y = (C₁ + C₂x)e^(rx)<br>
        • b² - 4ac < 0: y = e^(αx)(C₁cos(βx) + C₂sin(βx))
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 3️⃣ Applications")
    
    app_de_col1, app_de_col2 = st.columns(2)
    
    with app_de_col1:
        st.markdown("""
        **Physics & Engineering:**
        - Spring-mass systems
        - RC/RLC circuits
        - Heat diffusion
        - Wave propagation
        """)
    
    with app_de_col2:
        st.markdown("""
        **Computer Science:**
        - Population models
        - Algorithm analysis
        - Neural network dynamics
        - Control systems
        """)

# ==================== TAB 7: FOURIER ANALYSIS ====================
with tabs[6]:
    st.markdown("## 🌊 Fourier Analysis")
    
    st.markdown("### 1️⃣ Fourier Series")
    
    st.markdown("""
    <div class="definition">
        <strong>Fourier Series Expansion</strong><br>
        Any periodic function f(x) with period 2π can be expressed as:<br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.1rem;">
            f(x) = a₀/2 + Σ[aₙcos(nx) + bₙsin(nx)]
        </div>
        where:<br>
        aₙ = (1/π)∫₋π^π f(x)cos(nx)dx<br>
        bₙ = (1/π)∫₋π^π f(x)sin(nx)dx
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive Fourier series approximation
    st.markdown("#### 🎵 Fourier Series Approximation")
    
    wave_type = st.selectbox("Select function to approximate", ["Square Wave", "Sawtooth Wave", "Triangle Wave"])
    n_terms = st.slider("Number of Fourier terms", 1, 20, 5)
    
    x_fourier = np.linspace(-np.pi, np.pi, 500)
    
    # Original function
    if wave_type == "Square Wave":
        y_original = np.sign(np.sin(x_fourier))
        # Fourier approximation
        y_approx = np.zeros_like(x_fourier)
        for n in range(1, n_terms + 1):
            if n % 2 == 1:  # Only odd terms
                y_approx += (4/(n*np.pi)) * np.sin(n*x_fourier)
    elif wave_type == "Sawtooth Wave":
        y_original = x_fourier
        y_approx = np.zeros_like(x_fourier)
        for n in range(1, n_terms + 1):
            y_approx += (2*(-1)**(n+1)/n) * np.sin(n*x_fourier)
    else:  # Triangle Wave
        y_original = np.abs(x_fourier)
        y_approx = np.zeros_like(x_fourier)
        for n in range(1, n_terms + 1):
            if n % 2 == 1:
                y_approx += (8/(np.pi**2 * n**2)) * (-1)**((n-1)/2) * np.cos(n*x_fourier)
    
    # Create dataframe for plotting
    df_fourier = pd.DataFrame({
        'x': np.concatenate([x_fourier, x_fourier]),
        'y': np.concatenate([y_original, y_approx]),
        'type': ['Original'] * len(x_fourier) + [f'Fourier ({n_terms} terms)'] * len(x_fourier)
    })
    
    fourier_chart = alt.Chart(df_fourier).mark_line(strokeWidth=2).encode(
        x=alt.X('x:Q', title='x'),
        y=alt.Y('y:Q', title='f(x)'),
        color=alt.Color('type:N', scale=alt.Scale(domain=['Original', f'Fourier ({n_terms} terms)'],
                                                    range=['#3b82f6', '#ef4444'])),
        tooltip=['x', 'y', 'type']
    ).properties(
        width=700,
        height=400,
        title=f"Fourier Series Approximation of {wave_type}"
    ).interactive()
    
    st.altair_chart(fourier_chart, use_container_width=True)
    
    st.info(f"📊 Using {n_terms} Fourier terms. Increase for better approximation!")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Fourier Transform")
    
    st.markdown("""
    <div class="theorem">
        <strong>Fourier Transform</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.1rem;">
            F(ω) = ∫₋∞^∞ f(t)e^(-iωt) dt
        </div>
        Inverse Fourier Transform:<br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.1rem;">
            f(t) = (1/2π)∫₋∞^∞ F(ω)e^(iωt) dω
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 3️⃣ Applications")
    
    st.markdown("""
    **Modern Applications:**
    - Signal processing & telecommunications
    - Image compression (JPEG)
    - Audio analysis (MP3)
    - Quantum mechanics
    - Machine learning (spectral methods)
    - Computer vision (frequency domain filtering)
    """)

# ==================== TAB 8: APPLICATIONS ====================
with tabs[7]:
    st.markdown("## 📊 Applications of Calculus")
    
    st.markdown("### 1️⃣ Area Under Curves")
    
    st.markdown("""
    The definite integral ∫<sub>a</sub><sup>b</sup> f(x) dx represents the **area** between 
    the curve f(x) and the x-axis from x = a to x = b.
    """)
    
    # Interactive area calculator
    st.markdown("#### 🧮 Area Calculator")
    
    func_area = st.selectbox("Select function", ["x²", "sin(x)", "eˣ", "1/x"], key="area_func")
    
    col1, col2 = st.columns(2)
    with col1:
        a_area = st.number_input("Lower bound", value=0.0, step=0.5, key="a_area")
    with col2:
        b_area = st.number_input("Upper bound", value=2.0, step=0.5, key="b_area")
    
    x_area = np.linspace(a_area, b_area, 200)
    
    if func_area == "x²":
        y_area = x_area**2
        area_val = (b_area**3 / 3) - (a_area**3 / 3)
    elif func_area == "sin(x)":
        y_area = np.sin(x_area)
        area_val = -np.cos(b_area) + np.cos(a_area)
    elif func_area == "eˣ":
        y_area = np.exp(x_area)
        area_val = np.exp(b_area) - np.exp(a_area)
    else:  # 1/x
        if a_area <= 0:
            a_area = 0.1
        x_area = np.linspace(a_area, b_area, 200)
        y_area = 1/x_area
        area_val = np.log(b_area) - np.log(a_area)
    
    df_area = pd.DataFrame({'x': x_area, 'y': y_area})
    
    area_chart = alt.Chart(df_area).mark_area(
        line={'color': '#3b82f6'},
        color=alt.Gradient(
            gradient='linear',
            stops=[
                alt.GradientStop(color='#dbeafe', offset=0),
                alt.GradientStop(color='#3b82f6', offset=1)
            ],
            x1=0,
            x2=0,
            y1=1,
            y2=0
        )
    ).encode(
        x=alt.X('x:Q', title='x'),
        y=alt.Y('y:Q', title=f'f(x) = {func_area}'),
        tooltip=['x', 'y']
    ).properties(
        width=700,
        height=400,
        title=f"Area under {func_area} from {a_area} to {b_area}"
    )
    
    st.altair_chart(area_chart, use_container_width=True)
    st.success(f"📐 **Area = {area_val:.4f}** square units")
    
    # More applications
    st.markdown("---")
    st.markdown("### 2️⃣ Other Applications")
    
    app_col1, app_col2 = st.columns(2)
    
    with app_col1:
        st.markdown("""
        **In Computer Science:**
        - Algorithm complexity analysis
        - Machine learning optimization
        - Computer graphics (curves, surfaces)
        - Signal processing
        """)
    
    with app_col2:
        st.markdown("""
        **In Engineering:**
        - Circuit analysis (RC circuits)
        - Control systems
        - Fluid dynamics
        - Structural analysis
        """)

# ==================== TAB 5: PRACTICE PROBLEMS ====================
with tabs[4]:
    st.markdown("## 🧮 Practice Problems")
    
    st.markdown("""
    <div class="practice-box">
        <strong>💡 Practice makes perfect!</strong><br>
        Try these problems to test your understanding. Solutions are provided below.
    </div>
    """, unsafe_allow_html=True)
    
    problems = [
        {
            "title": "Problem 1: Limits",
            "question": "Find: lim(x→3) (x² - 9)/(x - 3)",
            "hint": "Factor the numerator first",
            "solution": "= lim(x→3) (x-3)(x+3)/(x-3) = lim(x→3) (x+3) = 6"
        },
        {
            "title": "Problem 2: Derivatives",
            "question": "Find f'(x) if f(x) = (2x + 1)³",
            "hint": "Use the chain rule",
            "solution": "f'(x) = 3(2x + 1)² · 2 = 6(2x + 1)²"
        },
        {
            "title": "Problem 3: Optimization",
            "question": "Find the minimum value of f(x) = x² - 4x + 7",
            "hint": "Find critical points using f'(x) = 0",
            "solution": "f'(x) = 2x - 4 = 0 → x = 2, f(2) = 4 - 8 + 7 = 3 (minimum)"
        },
        {
            "title": "Problem 4: Integration",
            "question": "Evaluate: ∫(4x³ - 6x + 2) dx",
            "hint": "Use power rule for each term",
            "solution": "= x⁴ - 3x² + 2x + C"
        },
        {
            "title": "Problem 5: Definite Integral",
            "question": "Evaluate: ∫₁³ (2x + 1) dx",
            "hint": "Find antiderivative then apply FTC",
            "solution": "= [x² + x]₁³ = (9 + 3) - (1 + 1) = 10"
        }
    ]
    
    for idx, problem in enumerate(problems, 1):
        with st.expander(f"📝 {problem['title']}", expanded=False):
            st.markdown(f"**Question:** {problem['question']}")
            
            if st.button(f"Show Hint", key=f"hint_{idx}"):
                st.info(f"💡 {problem['hint']}")
            
            if st.button(f"Show Solution", key=f"sol_{idx}"):
                st.success(f"✅ **Solution:** {problem['solution']}")

# ==================== TAB 6: VISUALIZATIONS ====================
with tabs[5]:
    st.markdown("## 📈 Interactive Visualizations")
    
    st.markdown("### 🎨 Function Explorer")
    
    st.markdown("Explore different functions and their properties")
    
    # Function builder
    col1, col2, col3 = st.columns(3)
    
    with col1:
        coef_a = st.slider("Coefficient a", -5.0, 5.0, 1.0, 0.1)
    with col2:
        coef_b = st.slider("Coefficient b", -5.0, 5.0, 0.0, 0.1)
    with col3:
        coef_c = st.slider("Coefficient c", -5.0, 5.0, 0.0, 0.1)
    
    x_viz = np.linspace(-10, 10, 300)
    y_viz = coef_a * x_viz**2 + coef_b * x_viz + coef_c
    y_deriv_viz = 2 * coef_a * x_viz + coef_b
    
    df_viz = pd.DataFrame({
        'x': np.concatenate([x_viz, x_viz]),
        'y': np.concatenate([y_viz, y_deriv_viz]),
        'type': ['f(x)'] * len(x_viz) + ["f'(x)"] * len(x_viz)
    })
    
    viz_chart = alt.Chart(df_viz).mark_line(strokeWidth=3).encode(
        x=alt.X('x:Q', title='x'),
        y=alt.Y('y:Q', title='y'),
        color=alt.Color('type:N', scale=alt.Scale(domain=['f(x)', "f'(x)"], 
                                                    range=['#3b82f6', '#ef4444'])),
        tooltip=['x', 'y', 'type']
    ).properties(
        width=800,
        height=500,
        title=f"f(x) = {coef_a:.1f}x² + {coef_b:.1f}x + {coef_c:.1f}"
    ).interactive()
    
    st.altair_chart(viz_chart, use_container_width=True)
    
    # Show critical points
    if coef_a != 0:
        critical_x = -coef_b / (2 * coef_a)
        critical_y = coef_a * critical_x**2 + coef_b * critical_x + coef_c
        
        if coef_a > 0:
            point_type = "Minimum"
        else:
            point_type = "Maximum"
        
        st.info(f"📍 Critical Point ({point_type}): ({critical_x:.2f}, {critical_y:.2f})")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>MA101 - Differential and Integral Calculus</strong><br>
    <small>UTel University | Department of Mathematics</small>
</div>
""", unsafe_allow_html=True)
