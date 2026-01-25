import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="PH101 - Physics", page_icon="⚛️", layout="wide")

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
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
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
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .law-box {
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
    
    .equation-box {
        background: #f8fafc;
        border: 2px solid #e2e8f0;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        text-align: center;
        font-size: 1.3rem;
    }
    
    .experiment-box {
        background: #faf5ff;
        border-left: 4px solid #8b5cf6;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="course-header">
    <div style="font-size: 1.2rem; opacity: 0.9;">PH101</div>
    <div class="course-title">Physics</div>
    <div>⚛️ 3 Credits | Semester 1 | Science</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "1")
with col3:
    st.metric("Difficulty", "4/7")
with col4:
    st.metric("Hours/Week", "5")

st.markdown("---")

# Navigation tabs - Graduate level
tabs = st.tabs([
    "📚 Overview",
    "🎯 Mechanics",
    "⚡ Electricity & Magnetism",
    "🌊 Waves & Optics",
    "🔥 Thermodynamics",
    "⚛️ Modern Physics",
    "🔬 Experiments",
    "🧮 Problem Solving",
    "📊 Simulations",
    "🎓 Applications",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive introduction to fundamental physics principles covering classical mechanics, 
        electromagnetism, waves, thermodynamics, and modern physics. This course emphasizes mathematical 
        rigor, problem-solving skills, and applications to engineering. Prepares students for advanced 
        physics and engineering courses.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Master Newtonian mechanics and apply to real-world systems",
        "Understand electromagnetic theory and Maxwell's equations",
        "Analyze wave phenomena and optical systems",
        "Apply thermodynamic principles to engineering problems",
        "Grasp quantum mechanics fundamentals and applications",
        "Conduct experiments and analyze measurement uncertainties",
        "Solve complex physics problems using calculus",
        "Apply physics principles to computer engineering"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Classical Physics:**
        - Kinematics and dynamics
        - Energy and momentum
        - Rotational motion
        - Gravitation
        - Oscillations and waves
        
        **Electromagnetism:**
        - Electric fields and potentials
        - Magnetic fields and forces
        - Electromagnetic induction
        - Maxwell's equations
        - AC circuits
        """)
    
    with col2:
        st.markdown("""
        **Modern Physics:**
        - Special relativity
        - Quantum mechanics basics
        - Atomic structure
        - Nuclear physics
        - Semiconductors
        
        **Applications:**
        - Circuit analysis
        - Signal processing
        - Sensors and actuators
        - Optoelectronics
        - Quantum computing basics
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "University Physics", "author": "Young & Freedman", "type": "Textbook"},
        {"title": "Feynman Lectures on Physics", "author": "Richard Feynman", "type": "Classic"},
        {"title": "Introduction to Electrodynamics", "author": "David Griffiths", "type": "Advanced"},
        {"title": "MIT OpenCourseWare - Physics", "author": "MIT", "type": "Online"}
    ]
    
    for resource in resources:
        st.markdown(f"📖 **{resource['title']}** by {resource['author']} ({resource['type']})")

# ==================== TAB 2: MECHANICS ====================
with tabs[1]:
    st.markdown("## 🎯 Classical Mechanics")
    
    st.markdown("### 1️⃣ Kinematics")
    
    st.markdown("""
    <div class="law-box">
        <strong>Equations of Motion (Constant Acceleration):</strong><br><br>
        v = v₀ + at<br>
        x = x₀ + v₀t + ½at²<br>
        v² = v₀² + 2a(x - x₀)
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive projectile motion
    st.markdown("#### 🎯 Projectile Motion Simulator")
    
    col1, col2 = st.columns(2)
    with col1:
        v0 = st.slider("Initial velocity (m/s)", 10, 50, 25)
    with col2:
        angle = st.slider("Launch angle (degrees)", 0, 90, 45)
    
    # Calculate trajectory
    g = 9.8  # m/s²
    angle_rad = np.radians(angle)
    v0x = v0 * np.cos(angle_rad)
    v0y = v0 * np.sin(angle_rad)
    
    # Time of flight
    t_flight = 2 * v0y / g
    
    # Generate trajectory points
    t = np.linspace(0, t_flight, 100)
    x = v0x * t
    y = v0y * t - 0.5 * g * t**2
    
    # Calculate max height and range
    max_height = (v0y**2) / (2 * g)
    range_val = (v0**2 * np.sin(2 * angle_rad)) / g
    
    df_projectile = pd.DataFrame({'x': x, 'y': y})
    
    projectile_chart = alt.Chart(df_projectile).mark_line(strokeWidth=3, color='#3b82f6').encode(
        x=alt.X('x:Q', title='Horizontal Distance (m)'),
        y=alt.Y('y:Q', title='Height (m)', scale=alt.Scale(domain=[0, max(y) * 1.2])),
        tooltip=['x', 'y']
    ).properties(
        width=700,
        height=400,
        title=f"Projectile Motion: v₀={v0} m/s, θ={angle}°"
    )
    
    st.altair_chart(projectile_chart, use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Max Height", f"{max_height:.2f} m")
    with col2:
        st.metric("Range", f"{range_val:.2f} m")
    with col3:
        st.metric("Time of Flight", f"{t_flight:.2f} s")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Newton's Laws")
    
    st.markdown("""
    <div class="law-box">
        <strong>Newton's Three Laws:</strong><br><br>
        <strong>1st Law (Inertia):</strong> An object at rest stays at rest, and an object in motion stays in motion unless acted upon by a net external force.<br><br>
        <strong>2nd Law (F = ma):</strong> The acceleration of an object is directly proportional to the net force and inversely proportional to its mass.<br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            ΣF = ma
        </div>
        <strong>3rd Law (Action-Reaction):</strong> For every action, there is an equal and opposite reaction.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="example-box">
        <strong>📝 Example: Force on an Accelerating Car</strong><br><br>
        A 1500 kg car accelerates from rest to 25 m/s in 10 seconds. Find the net force.<br><br>
        <strong>Solution:</strong><br>
        a = (v - v₀) / t = (25 - 0) / 10 = 2.5 m/s²<br>
        F = ma = 1500 kg × 2.5 m/s² = <strong>3750 N</strong>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Energy and Momentum")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Energy:**
        <div class="equation-box">
            KE = ½mv²<br>
            PE = mgh<br>
            E_total = KE + PE
        </div>
        Conservation of Energy:<br>
        E_initial = E_final
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        **Momentum:**
        <div class="equation-box">
            p = mv<br>
            Δp = FΔt (Impulse)
        </div>
        Conservation of Momentum:<br>
        Σp_before = Σp_after
        """, unsafe_allow_html=True)

# ==================== TAB 3: ELECTRICITY & MAGNETISM ====================
with tabs[2]:
    st.markdown("## ⚡ Electricity & Magnetism")
    
    st.markdown("### 1️⃣ Electric Fields and Forces")
    
    st.markdown("""
    <div class="law-box">
        <strong>Coulomb's Law:</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            F = k(q₁q₂)/r²
        </div>
        where k = 8.99 × 10⁹ N·m²/C²
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="law-box">
        <strong>Electric Field:</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            E = F/q = kQ/r²
        </div>
        Electric Potential:<br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            V = kQ/r
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Electric field visualization
    st.markdown("#### ⚡ Electric Field Visualization")
    
    charge_type = st.selectbox("Select charge configuration", 
                                ["Single Positive", "Single Negative", "Dipole", "Two Positive"])
    
    # Create grid
    x = np.linspace(-5, 5, 20)
    y = np.linspace(-5, 5, 20)
    X, Y = np.meshgrid(x, y)
    
    # Calculate electric field
    if charge_type == "Single Positive":
        Q = 1
        r = np.sqrt(X**2 + Y**2) + 0.1
        Ex = Q * X / r**3
        Ey = Q * Y / r**3
    elif charge_type == "Single Negative":
        Q = -1
        r = np.sqrt(X**2 + Y**2) + 0.1
        Ex = Q * X / r**3
        Ey = Q * Y / r**3
    elif charge_type == "Dipole":
        # Positive charge at (0, 1)
        r1 = np.sqrt(X**2 + (Y-1)**2) + 0.1
        Ex1 = X / r1**3
        Ey1 = (Y-1) / r1**3
        # Negative charge at (0, -1)
        r2 = np.sqrt(X**2 + (Y+1)**2) + 0.1
        Ex2 = -X / r2**3
        Ey2 = -(Y+1) / r2**3
        Ex = Ex1 + Ex2
        Ey = Ey1 + Ey2
    else:  # Two Positive
        # Charge at (-1, 0)
        r1 = np.sqrt((X+1)**2 + Y**2) + 0.1
        Ex1 = (X+1) / r1**3
        Ey1 = Y / r1**3
        # Charge at (1, 0)
        r2 = np.sqrt((X-1)**2 + Y**2) + 0.1
        Ex2 = (X-1) / r2**3
        Ey2 = Y / r2**3
        Ex = Ex1 + Ex2
        Ey = Ey1 + Ey2
    
    st.info(f"⚡ Electric field pattern for: {charge_type}")
    st.caption("Field lines show direction and strength of electric field")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Magnetic Fields")
    
    st.markdown("""
    <div class="law-box">
        <strong>Magnetic Force on Moving Charge:</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            F = qvB sin(θ)
        </div>
        <strong>Lorentz Force (Combined E and B):</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            F = q(E + v × B)
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Maxwell's Equations")
    
    st.markdown("""
    <div class="law-box">
        <strong>Maxwell's Four Equations (Integral Form):</strong><br><br>
        <strong>1. Gauss's Law:</strong><br>
        ∮ E·dA = Q_enclosed/ε₀<br><br>
        <strong>2. Gauss's Law for Magnetism:</strong><br>
        ∮ B·dA = 0<br><br>
        <strong>3. Faraday's Law:</strong><br>
        ∮ E·dl = -dΦ_B/dt<br><br>
        <strong>4. Ampère-Maxwell Law:</strong><br>
        ∮ B·dl = μ₀(I + ε₀ dΦ_E/dt)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="theory-box">
        <strong>Significance:</strong><br>
        Maxwell's equations unify electricity and magnetism, predict electromagnetic waves 
        (light), and form the foundation of classical electromagnetism. They are essential 
        for understanding radio, telecommunications, and optics.
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: WAVES & OPTICS ====================
with tabs[3]:
    st.markdown("## 🌊 Waves & Optics")
    
    st.markdown("### 1️⃣ Wave Properties")
    
    st.markdown("""
    <div class="law-box">
        <strong>Wave Equation:</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            y(x,t) = A sin(kx - ωt + φ)
        </div>
        where:<br>
        • A = amplitude<br>
        • k = 2π/λ (wave number)<br>
        • ω = 2πf (angular frequency)<br>
        • v = λf (wave speed)
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive wave simulator
    st.markdown("#### 🌊 Wave Simulator")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        amplitude = st.slider("Amplitude", 0.5, 3.0, 1.0, 0.1)
    with col2:
        frequency = st.slider("Frequency (Hz)", 0.5, 5.0, 1.0, 0.5)
    with col3:
        phase = st.slider("Phase (rad)", 0.0, 2*np.pi, 0.0, 0.1)
    
    # Generate wave
    x = np.linspace(0, 10, 500)
    wavelength = 2  # meters
    k = 2 * np.pi / wavelength
    omega = 2 * np.pi * frequency
    
    # Wave at t=0
    y = amplitude * np.sin(k * x + phase)
    
    df_wave = pd.DataFrame({'x': x, 'y': y})
    
    wave_chart = alt.Chart(df_wave).mark_line(strokeWidth=3, color='#3b82f6').encode(
        x=alt.X('x:Q', title='Position (m)'),
        y=alt.Y('y:Q', title='Displacement', scale=alt.Scale(domain=[-3.5, 3.5])),
        tooltip=['x', 'y']
    ).properties(
        width=700,
        height=300,
        title=f"Wave: A={amplitude}, f={frequency} Hz, λ={wavelength} m"
    )
    
    st.altair_chart(wave_chart, use_container_width=True)
    
    st.metric("Wave Speed", f"{wavelength * frequency:.2f} m/s")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Interference and Diffraction")
    
    st.markdown("""
    <div class="law-box">
        <strong>Double-Slit Interference:</strong><br>
        Constructive: d sin(θ) = mλ (m = 0, 1, 2, ...)<br>
        Destructive: d sin(θ) = (m + ½)λ<br><br>
        <strong>Single-Slit Diffraction:</strong><br>
        Minima: a sin(θ) = mλ (m = ±1, ±2, ...)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Geometric Optics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Mirrors:**
        <div class="equation-box">
            1/f = 1/d_o + 1/d_i<br>
            M = -d_i/d_o
        </div>
        f = focal length<br>
        d_o = object distance<br>
        d_i = image distance<br>
        M = magnification
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        **Lenses:**
        <div class="equation-box">
            1/f = (n-1)(1/R₁ - 1/R₂)
        </div>
        Lensmaker's Equation<br><br>
        <div class="equation-box">
            n₁ sin(θ₁) = n₂ sin(θ₂)
        </div>
        Snell's Law
        """, unsafe_allow_html=True)

# ==================== TAB 5: THERMODYNAMICS ====================
with tabs[4]:
    st.markdown("## 🔥 Thermodynamics")
    
    st.markdown("### 1️⃣ Laws of Thermodynamics")
    
    st.markdown("""
    <div class="law-box">
        <strong>Zeroth Law:</strong> If A is in thermal equilibrium with B, and B with C, then A is in equilibrium with C.<br><br>
        <strong>First Law (Energy Conservation):</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            ΔU = Q - W
        </div>
        ΔU = change in internal energy<br>
        Q = heat added to system<br>
        W = work done by system<br><br>
        <strong>Second Law:</strong> Entropy of an isolated system always increases.<br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            ΔS ≥ 0
        </div>
        <strong>Third Law:</strong> As T → 0 K, S → 0
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Ideal Gas Law")
    
    st.markdown("""
    <div class="law-box">
        <strong>Ideal Gas Law:</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            PV = nRT
        </div>
        P = pressure, V = volume, n = moles<br>
        R = 8.314 J/(mol·K), T = temperature (K)
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive gas law calculator
    st.markdown("#### 🔬 Ideal Gas Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        n_moles = st.number_input("Number of moles (n)", 0.1, 10.0, 1.0, 0.1)
        T_celsius = st.number_input("Temperature (°C)", -50, 200, 25)
    with col2:
        V_liters = st.number_input("Volume (L)", 1.0, 100.0, 22.4, 1.0)
    
    # Calculate pressure
    R = 8.314  # J/(mol·K)
    T_kelvin = T_celsius + 273.15
    V_m3 = V_liters / 1000
    P_pascal = (n_moles * R * T_kelvin) / V_m3
    P_atm = P_pascal / 101325
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Pressure", f"{P_pascal:.0f} Pa")
    with col2:
        st.metric("Pressure", f"{P_atm:.2f} atm")
    with col3:
        st.metric("Temperature", f"{T_kelvin:.2f} K")
    
    st.markdown("---")
    st.markdown("### 3️⃣ Heat Transfer")
    
    st.markdown("""
    <div class="law-box">
        <strong>Conduction:</strong> Q/t = kA(T₂-T₁)/d<br>
        <strong>Convection:</strong> Q/t = hA(T_surface - T_fluid)<br>
        <strong>Radiation:</strong> P = εσAT⁴ (Stefan-Boltzmann Law)
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: MODERN PHYSICS ====================
with tabs[5]:
    st.markdown("## ⚛️ Modern Physics")
    
    st.markdown("### 1️⃣ Special Relativity")
    
    st.markdown("""
    <div class="law-box">
        <strong>Einstein's Postulates:</strong><br>
        1. Laws of physics are the same in all inertial frames<br>
        2. Speed of light (c) is constant in all frames<br><br>
        <strong>Key Equations:</strong><br>
        Time Dilation: Δt = γΔt₀<br>
        Length Contraction: L = L₀/γ<br>
        Mass-Energy: E = mc²<br><br>
        where γ = 1/√(1 - v²/c²) (Lorentz factor)
    </div>
    """, unsafe_allow_html=True)
    
    # Relativistic effects calculator
    st.markdown("#### 🚀 Relativistic Effects Calculator")
    
    velocity_percent = st.slider("Velocity (% of speed of light)", 0, 99, 50)
    v = (velocity_percent / 100) * 3e8  # m/s
    c = 3e8  # m/s
    
    gamma = 1 / np.sqrt(1 - (v/c)**2)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Lorentz Factor (γ)", f"{gamma:.3f}")
    with col2:
        st.metric("Time Dilation", f"{gamma:.3f}×")
    with col3:
        st.metric("Length Contraction", f"{1/gamma:.3f}×")
    
    if velocity_percent > 90:
        st.warning("⚠️ At very high speeds, relativistic effects become significant!")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Quantum Mechanics")
    
    st.markdown("""
    <div class="law-box">
        <strong>Planck's Equation:</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            E = hf = ℏω
        </div>
        h = 6.626 × 10⁻³⁴ J·s (Planck's constant)<br>
        ℏ = h/2π (reduced Planck's constant)<br><br>
        <strong>de Broglie Wavelength:</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            λ = h/p = h/(mv)
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="law-box">
        <strong>Heisenberg Uncertainty Principle:</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            ΔxΔp ≥ ℏ/2<br>
            ΔEΔt ≥ ℏ/2
        </div>
        Cannot simultaneously know exact position and momentum
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Atomic Structure")
    
    st.markdown("""
    <div class="law-box">
        <strong>Bohr Model Energy Levels:</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            E_n = -13.6 eV / n²
        </div>
        For hydrogen atom (n = 1, 2, 3, ...)<br><br>
        <strong>Photon Emission:</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            ΔE = E_final - E_initial = hf
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: EXPERIMENTS ====================
with tabs[6]:
    st.markdown("## 🔬 Laboratory Experiments")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Experimental Physics Principles:</strong><br>
        • Measurement and uncertainty analysis<br>
        • Error propagation<br>
        • Data collection and analysis<br>
        • Scientific method application
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Classic Physics Experiments")
    
    experiments = [
        {
            "title": "1. Pendulum Motion",
            "objective": "Determine gravitational acceleration (g)",
            "procedure": "Measure period T for various lengths L",
            "equation": "T = 2π√(L/g) → g = 4π²L/T²",
            "expected": "g ≈ 9.8 m/s²"
        },
        {
            "title": "2. Ohm's Law Verification",
            "objective": "Verify V = IR relationship",
            "procedure": "Measure voltage and current for various resistances",
            "equation": "V = IR",
            "expected": "Linear V-I relationship"
        },
        {
            "title": "3. Photoelectric Effect",
            "objective": "Determine Planck's constant",
            "procedure": "Measure stopping potential vs frequency",
            "equation": "eV_stop = hf - φ",
            "expected": "h ≈ 6.626 × 10⁻³⁴ J·s"
        },
        {
            "title": "4. Interference Pattern",
            "objective": "Measure wavelength of light",
            "procedure": "Double-slit experiment, measure fringe spacing",
            "equation": "λ = xd/L",
            "expected": "λ ≈ 500-700 nm (visible light)"
        }
    ]
    
    for exp in experiments:
        with st.expander(f"🔬 {exp['title']}", expanded=False):
            st.markdown(f"**Objective:** {exp['objective']}")
            st.markdown(f"**Procedure:** {exp['procedure']}")
            st.markdown(f"**Key Equation:** {exp['equation']}")
            st.markdown(f"**Expected Result:** {exp['expected']}")

# ==================== TAB 8: PROBLEM SOLVING ====================
with tabs[7]:
    st.markdown("## 🧮 Problem Solving")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Problem-Solving Strategy:</strong><br>
        1. <strong>Identify:</strong> What is given? What to find?<br>
        2. <strong>Visualize:</strong> Draw diagrams, free-body diagrams<br>
        3. <strong>Plan:</strong> Which principles/equations apply?<br>
        4. <strong>Execute:</strong> Solve mathematically<br>
        5. <strong>Check:</strong> Units, reasonableness, limits
    </div>
    """, unsafe_allow_html=True)
    
    problems = [
        {
            "title": "Problem 1: Projectile Motion",
            "question": "A ball is thrown horizontally at 15 m/s from a 20m high cliff. How far from the base does it land?",
            "hint": "Use y = ½gt² to find time, then x = v₀t",
            "solution": """
Time to fall: y = ½gt²
20 = ½(9.8)t²
t = √(40/9.8) = 2.02 s

Horizontal distance:
x = v₀t = 15 × 2.02 = 30.3 m
            """
        },
        {
            "title": "Problem 2: Electric Potential",
            "question": "Two point charges +2μC and -3μC are 0.5m apart. Find the electric potential at the midpoint.",
            "hint": "V_total = V₁ + V₂, use V = kQ/r",
            "solution": """
k = 8.99 × 10⁹ N·m²/C²
r = 0.25 m for each charge

V₁ = kQ₁/r = (8.99×10⁹)(2×10⁻⁶)/0.25 = 71,920 V
V₂ = kQ₂/r = (8.99×10⁹)(-3×10⁻⁶)/0.25 = -107,880 V

V_total = 71,920 - 107,880 = -35,960 V
            """
        },
        {
            "title": "Problem 3: Thermodynamics",
            "question": "2 moles of ideal gas at 300K expand isothermally from 10L to 20L. Find work done.",
            "hint": "For isothermal process: W = nRT ln(V_f/V_i)",
            "solution": """
W = nRT ln(V_f/V_i)
W = (2)(8.314)(300) ln(20/10)
W = 4988.4 × ln(2)
W = 4988.4 × 0.693
W = 3,457 J ≈ 3.46 kJ
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

# ==================== TAB 9: SIMULATIONS ====================
with tabs[8]:
    st.markdown("## 📊 Interactive Simulations")
    
    st.markdown("### 🎯 Harmonic Oscillator")
    
    col1, col2 = st.columns(2)
    with col1:
        mass = st.slider("Mass (kg)", 0.1, 5.0, 1.0, 0.1)
    with col2:
        spring_k = st.slider("Spring constant (N/m)", 1.0, 50.0, 10.0, 1.0)
    
    # Calculate period and frequency
    omega = np.sqrt(spring_k / mass)
    period = 2 * np.pi / omega
    frequency = 1 / period
    
    # Generate oscillation
    t = np.linspace(0, 3*period, 500)
    x = np.cos(omega * t)
    v = -omega * np.sin(omega * t)
    
    df_oscillator = pd.DataFrame({
        't': np.concatenate([t, t]),
        'value': np.concatenate([x, v]),
        'type': ['Position'] * len(t) + ['Velocity'] * len(t)
    })
    
    osc_chart = alt.Chart(df_oscillator).mark_line(strokeWidth=2).encode(
        x=alt.X('t:Q', title='Time (s)'),
        y=alt.Y('value:Q', title='Normalized Value'),
        color=alt.Color('type:N', scale=alt.Scale(domain=['Position', 'Velocity'],
                                                    range=['#3b82f6', '#ef4444'])),
        tooltip=['t', 'value', 'type']
    ).properties(
        width=700,
        height=400,
        title="Simple Harmonic Motion"
    ).interactive()
    
    st.altair_chart(osc_chart, use_container_width=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Period", f"{period:.3f} s")
    with col2:
        st.metric("Frequency", f"{frequency:.3f} Hz")

# ==================== TAB 10: APPLICATIONS ====================
with tabs[9]:
    st.markdown("## 🎓 Applications to Engineering")
    
    st.markdown("### Physics in Computer Engineering")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Semiconductors:**
        - Band theory (quantum mechanics)
        - Doping and p-n junctions
        - Transistor operation
        - Integrated circuits
        
        **Optoelectronics:**
        - LEDs and lasers
        - Photodetectors
        - Fiber optics
        - Display technology
        """)
    
    with col2:
        st.markdown("""
        **Electromagnetism:**
        - Circuit design
        - Signal propagation
        - Antenna theory
        - Electromagnetic compatibility
        
        **Quantum Computing:**
        - Qubit physics
        - Superposition and entanglement
        - Quantum gates
        - Decoherence
        """)
    
    st.markdown("---")
    st.markdown("### Real-World Examples")
    
    st.markdown("""
    <div class="example-box">
        <strong>1. CPU Heat Dissipation:</strong><br>
        Uses thermodynamics principles to design cooling systems.<br>
        Q/t = kA(T_CPU - T_ambient)/d
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="example-box">
        <strong>2. Wireless Communication:</strong><br>
        Electromagnetic waves carry information.<br>
        c = fλ (speed of light = frequency × wavelength)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="example-box">
        <strong>3. Touchscreen Technology:</strong><br>
        Capacitive sensing uses electric fields.<br>
        C = εA/d (capacitance)
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 11: YOUTUBE RESOURCES ====================
with tabs[10]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="theory-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning Physics</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {"title": "Physics Explained", "channel": "Khan Academy", "url": "https://www.youtube.com/c/khanacademy", "description": "Comprehensive physics series", "duration": "Channel"},
        {"title": "Physics Fundamentals", "channel": "The Organic Chemistry Tutor", "url": "https://www.youtube.com/c/TheOrganicChemistryTutor", "description": "Clear physics explanations", "duration": "Channel"},
        {"title": "Crash Course Physics", "channel": "CrashCourse", "url": "https://www.youtube.com/playlist?list=PL8dPuuaLjXtN0ge7yDk_UA0ldZJdhwkoV", "description": "Engaging physics intro", "duration": "~10 hours"}
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
        {"title": "MIT 8.01 Classical Mechanics", "channel": "MIT OpenCourseWare", "url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP61qDex7XslwNJ-xxxEFzMNV", "description": "MIT physics course", "duration": "~40 hours"},
        {"title": "Physics Lectures", "channel": "Michel van Biezen", "url": "https://www.youtube.com/c/MichelvanBiezen", "description": "Detailed problem solving", "duration": "Channel"},
        {"title": "Electromagnetism", "channel": "Professor Dave Explains", "url": "https://www.youtube.com/c/ProfessorDaveExplains", "description": "E&M fundamentals", "duration": "Channel"}
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
        {"title": "Quantum Mechanics", "channel": "MIT OpenCourseWare", "url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP60cspQn3N9dYRPiyVWDd80G", "description": "MIT 8.04 QM", "duration": "~40 hours"},
        {"title": "Theoretical Physics", "channel": "Physics Explained", "url": "https://www.youtube.com/c/PhysicsExplainedVideos", "description": "Advanced topics", "duration": "Channel"},
        {"title": "Feynman Lectures", "channel": "The Feynman Lectures", "url": "https://www.youtube.com/c/TheFeynmanLectures", "description": "Classic Feynman lectures", "duration": "Channel"}
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
    <div class="example-box">
        <strong>Recommended Learning Path:</strong><br>
        1. Start with Khan Academy for fundamentals<br>
        2. Watch Crash Course for engaging overviews<br>
        3. Follow MIT OCW for rigorous treatment<br>
        4. Practice problems with Michel van Biezen<br>
        5. Use visualizations (PhET simulations)<br>
        6. Solve textbook problems daily<br>
        7. Connect concepts to real-world applications<br>
        8. Review Feynman Lectures for deep insights<br><br>
        
        <strong>Study Resources:</strong><br>
        • <strong>Simulations:</strong> PhET Interactive Simulations<br>
        • <strong>Practice:</strong> HyperPhysics, Physics Classroom<br>
        • <strong>Books:</strong> Halliday & Resnick, Feynman Lectures<br>
        • <strong>Community:</strong> Physics Stack Exchange, r/AskPhysics<br><br>
        
        <strong>Problem Solving Tips:</strong><br>
        • Draw diagrams and free-body diagrams<br>
        • Identify known and unknown variables<br>
        • Check units and dimensional analysis<br>
        • Verify answers with limiting cases
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>PH101 - Physics</strong><br>
    <small>UTel University | Department of Science</small>
</div>
""", unsafe_allow_html=True)
