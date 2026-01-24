import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="EE101 - Electronics", page_icon="⚡", layout="wide")

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
    
    .circuit-box {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .component-box {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .example-box {
        background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%);
        border-left: 5px solid #8b5cf6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="course-header">
    <div style="font-size: 1.2rem; opacity: 0.9;">EE101</div>
    <div class="course-title">Electronics</div>
    <div>⚡ 3 Credits | Semester 2 | Core</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "2")
with col3:
    st.metric("Difficulty", "4/7")
with col4:
    st.metric("Hours/Week", "6")

st.markdown("---")

# Navigation tabs - Graduate level
tabs = st.tabs([
    "📚 Overview",
    "🔌 Circuit Fundamentals",
    "🔋 AC & DC Analysis",
    "💎 Semiconductors",
    "🔺 Diodes & Applications",
    "📡 Transistors",
    "🎚️ Amplifiers",
    "🔢 Digital Electronics",
    "🎛️ Operational Amplifiers",
    "🧮 Practice Problems"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive introduction to electronic circuits and devices. Covers DC and AC circuit analysis, 
        semiconductor physics, diodes, transistors, amplifiers, and digital logic. Emphasizes both theoretical 
        understanding and practical applications in modern electronics and computer engineering.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Analyze DC and AC circuits using fundamental laws",
        "Understand semiconductor physics and p-n junctions",
        "Design and analyze diode circuits and applications",
        "Apply transistor models for amplifier design",
        "Design operational amplifier circuits",
        "Implement digital logic circuits",
        "Use simulation tools for circuit analysis",
        "Apply electronics principles to computer engineering"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Circuit Analysis:**
        - Ohm's Law and Kirchhoff's Laws
        - Series and parallel circuits
        - Thevenin and Norton theorems
        - AC circuit analysis
        - Frequency response
        
        **Semiconductor Devices:**
        - Semiconductor physics
        - P-N junction diodes
        - Zener diodes and regulators
        - BJT transistors
        - MOSFET transistors
        """)
    
    with col2:
        st.markdown("""
        **Amplifiers:**
        - Common emitter/source amplifiers
        - Frequency response
        - Operational amplifiers
        - Feedback systems
        - Power amplifiers
        
        **Digital Electronics:**
        - Logic gates
        - Boolean algebra
        - Combinational circuits
        - Sequential circuits
        - ADC/DAC converters
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Microelectronic Circuits", "author": "Sedra & Smith", "type": "Textbook"},
        {"title": "The Art of Electronics", "author": "Horowitz & Hill", "type": "Classic"},
        {"title": "Electronic Devices and Circuit Theory", "author": "Boylestad & Nashelsky", "type": "Fundamentals"},
        {"title": "Digital Design", "author": "Morris Mano", "type": "Digital"}
    ]
    
    for resource in resources:
        st.markdown(f"📖 **{resource['title']}** by {resource['author']} ({resource['type']})")

# ==================== TAB 2: CIRCUIT FUNDAMENTALS ====================
with tabs[1]:
    st.markdown("## 🔌 Circuit Fundamentals")
    
    st.markdown("### 1️⃣ Ohm's Law")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Ohm's Law:</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.5rem;">
            V = I × R
        </div>
        where:<br>
        • V = Voltage (Volts)<br>
        • I = Current (Amperes)<br>
        • R = Resistance (Ohms)
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive Ohm's Law calculator
    st.markdown("#### 🧮 Ohm's Law Calculator")
    
    calc_mode = st.radio("Calculate:", ["Voltage (V)", "Current (I)", "Resistance (R)"], horizontal=True)
    
    col1, col2 = st.columns(2)
    
    if calc_mode == "Voltage (V)":
        with col1:
            current = st.number_input("Current (A)", 0.001, 100.0, 1.0, 0.001, format="%.3f")
        with col2:
            resistance = st.number_input("Resistance (Ω)", 0.1, 10000.0, 100.0, 0.1)
        voltage = current * resistance
        st.success(f"**Voltage = {voltage:.3f} V**")
    
    elif calc_mode == "Current (I)":
        with col1:
            voltage = st.number_input("Voltage (V)", 0.1, 1000.0, 12.0, 0.1)
        with col2:
            resistance = st.number_input("Resistance (Ω)", 0.1, 10000.0, 100.0, 0.1)
        current = voltage / resistance
        st.success(f"**Current = {current:.3f} A = {current*1000:.1f} mA**")
    
    else:  # Resistance
        with col1:
            voltage = st.number_input("Voltage (V)", 0.1, 1000.0, 12.0, 0.1)
        with col2:
            current = st.number_input("Current (A)", 0.001, 100.0, 0.12, 0.001, format="%.3f")
        resistance = voltage / current
        st.success(f"**Resistance = {resistance:.2f} Ω**")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Kirchhoff's Laws")
    
    st.markdown("""
    <div class="circuit-box">
        <strong>Kirchhoff's Current Law (KCL):</strong><br>
        Sum of currents entering a node = Sum of currents leaving<br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            ΣI_in = ΣI_out
        </div>
        <strong>Kirchhoff's Voltage Law (KVL):</strong><br>
        Sum of voltages around any closed loop = 0<br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            ΣV = 0
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Series and Parallel Circuits")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Series Resistors:**
        <div style="text-align: center; margin: 1rem 0;">
            R_total = R₁ + R₂ + R₃ + ...
        </div>
        • Same current through all<br>
        • Voltages add up<br>
        • Total resistance increases
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        **Parallel Resistors:**
        <div style="text-align: center; margin: 1rem 0;">
            1/R_total = 1/R₁ + 1/R₂ + 1/R₃ + ...
        </div>
        • Same voltage across all<br>
        • Currents add up<br>
        • Total resistance decreases
        """, unsafe_allow_html=True)

# ==================== TAB 3: AC & DC ANALYSIS ====================
with tabs[2]:
    st.markdown("## 🔋 AC & DC Analysis")
    
    st.markdown("### 1️⃣ Power in DC Circuits")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Power Equations:</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            P = V × I = I²R = V²/R
        </div>
        Power is measured in Watts (W)<br>
        Energy = Power × Time (Watt-hours)
    </div>
    """, unsafe_allow_html=True)
    
    # Power calculator
    st.markdown("#### ⚡ Power Calculator")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        p_voltage = st.number_input("Voltage (V)", 1.0, 1000.0, 12.0, 1.0, key="p_v")
    with col2:
        p_current = st.number_input("Current (A)", 0.001, 100.0, 1.0, 0.001, key="p_i", format="%.3f")
    with col3:
        p_resistance = p_voltage / p_current
        st.metric("Resistance", f"{p_resistance:.2f} Ω")
    
    power = p_voltage * p_current
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Power", f"{power:.3f} W")
    with col2:
        energy_1h = power  # Wh for 1 hour
        st.metric("Energy (1 hour)", f"{energy_1h:.3f} Wh")
    
    st.markdown("---")
    st.markdown("### 2️⃣ AC Circuits")
    
    st.markdown("""
    <div class="circuit-box">
        <strong>AC Voltage:</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            v(t) = V_m sin(ωt + φ)
        </div>
        where:<br>
        • V_m = Peak voltage<br>
        • ω = 2πf (angular frequency)<br>
        • φ = Phase angle<br>
        • V_rms = V_m / √2 (RMS voltage)
    </div>
    """, unsafe_allow_html=True)
    
    # AC waveform visualization
    st.markdown("#### 📊 AC Waveform Visualizer")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        v_peak = st.slider("Peak Voltage (V)", 1, 50, 10)
    with col2:
        frequency = st.slider("Frequency (Hz)", 1, 100, 50)
    with col3:
        phase = st.slider("Phase (degrees)", 0, 360, 0)
    
    # Generate waveform
    t = np.linspace(0, 2/frequency, 500)
    omega = 2 * np.pi * frequency
    phase_rad = np.radians(phase)
    v = v_peak * np.sin(omega * t + phase_rad)
    
    v_rms = v_peak / np.sqrt(2)
    
    df_ac = pd.DataFrame({'Time (s)': t, 'Voltage (V)': v})
    
    ac_chart = alt.Chart(df_ac).mark_line(strokeWidth=3, color='#f59e0b').encode(
        x=alt.X('Time (s):Q'),
        y=alt.Y('Voltage (V):Q', scale=alt.Scale(domain=[-v_peak*1.2, v_peak*1.2])),
        tooltip=['Time (s)', 'Voltage (V)']
    ).properties(
        width=700,
        height=400,
        title=f"AC Waveform: {v_peak}V peak, {frequency}Hz, {phase}° phase"
    )
    
    st.altair_chart(ac_chart, use_container_width=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("V_rms", f"{v_rms:.2f} V")
    with col2:
        st.metric("Period", f"{1/frequency*1000:.1f} ms")
    with col3:
        st.metric("ω", f"{omega:.1f} rad/s")

# ==================== TAB 4: SEMICONDUCTORS ====================
with tabs[3]:
    st.markdown("## 💎 Semiconductors")
    
    st.markdown("### 1️⃣ Semiconductor Physics")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Intrinsic Semiconductors:</strong><br>
        • Pure semiconductor (Si, Ge)<br>
        • Equal number of electrons and holes<br>
        • Conductivity increases with temperature<br><br>
        
        <strong>Extrinsic Semiconductors:</strong><br>
        • <strong>N-type:</strong> Doped with donors (P, As) - excess electrons<br>
        • <strong>P-type:</strong> Doped with acceptors (B, Ga) - excess holes<br>
        • Majority and minority carriers
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ P-N Junction")
    
    st.markdown("""
    <div class="circuit-box">
        <strong>P-N Junction Formation:</strong><br>
        1. <strong>Diffusion:</strong> Electrons diffuse from N to P, holes from P to N<br>
        2. <strong>Depletion Region:</strong> Forms at junction (no free carriers)<br>
        3. <strong>Built-in Potential:</strong> ~0.7V for Si, ~0.3V for Ge<br><br>
        
        <strong>Biasing:</strong><br>
        • <strong>Forward Bias:</strong> P positive, N negative - current flows<br>
        • <strong>Reverse Bias:</strong> P negative, N positive - minimal current
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Energy Bands")
    
    st.markdown("""
    <div class="component-box">
        <strong>Band Gap Energy (E_g):</strong><br>
        • <strong>Conductors:</strong> E_g ≈ 0 (overlapping bands)<br>
        • <strong>Semiconductors:</strong> E_g = 0.7-1.5 eV (Si: 1.12 eV)<br>
        • <strong>Insulators:</strong> E_g > 3 eV<br><br>
        
        At room temperature, thermal energy can excite electrons across band gap in semiconductors.
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: DIODES ====================
with tabs[4]:
    st.markdown("## 🔺 Diodes & Applications")
    
    st.markdown("### 1️⃣ Diode Characteristics")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Ideal Diode:</strong><br>
        • Forward bias (V > 0): Acts like short circuit (R = 0)<br>
        • Reverse bias (V < 0): Acts like open circuit (R = ∞)<br><br>
        
        <strong>Real Diode:</strong><br>
        • Forward bias: V_D ≈ 0.7V (Si), current flows<br>
        • Reverse bias: Small leakage current (~nA)<br>
        • Breakdown: Large reverse voltage causes avalanche
    </div>
    """, unsafe_allow_html=True)
    
    # Diode I-V curve
    st.markdown("#### 📊 Diode I-V Characteristic")
    
    V_diode = np.linspace(-1, 1, 500)
    I_s = 1e-12  # Saturation current
    V_T = 0.026  # Thermal voltage at room temp
    
    # Shockley equation
    I_diode = I_s * (np.exp(V_diode / V_T) - 1)
    I_diode = np.clip(I_diode, -1e-9, 0.1)  # Clip for visualization
    
    df_diode = pd.DataFrame({'Voltage (V)': V_diode, 'Current (A)': I_diode})
    
    diode_chart = alt.Chart(df_diode).mark_line(strokeWidth=3, color='#ef4444').encode(
        x=alt.X('Voltage (V):Q'),
        y=alt.Y('Current (A):Q', scale=alt.Scale(type='log', domain=[1e-12, 0.1])),
        tooltip=['Voltage (V)', 'Current (A)']
    ).properties(
        width=700,
        height=400,
        title="Diode I-V Characteristic (Shockley Equation)"
    )
    
    st.altair_chart(diode_chart, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Diode Applications")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Rectifiers:**
        - Half-wave rectifier
        - Full-wave rectifier
        - Bridge rectifier
        - AC to DC conversion
        """)
    
    with col2:
        st.markdown("""
        **Other Applications:**
        - Voltage regulation (Zener)
        - Signal clipping/clamping
        - Protection circuits
        - LED (Light Emitting Diode)
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Zener Diode")
    
    st.markdown("""
    <div class="circuit-box">
        <strong>Zener Diode Voltage Regulator:</strong><br>
        • Operates in reverse breakdown region<br>
        • Maintains constant voltage (V_Z)<br>
        • Used for voltage regulation<br>
        • Common values: 3.3V, 5V, 12V, 15V
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: TRANSISTORS ====================
with tabs[5]:
    st.markdown("## 📡 Transistors")
    
    st.markdown("### 1️⃣ BJT (Bipolar Junction Transistor)")
    
    st.markdown("""
    <div class="theory-box">
        <strong>BJT Structure:</strong><br>
        • <strong>NPN:</strong> N-P-N layers (most common)<br>
        • <strong>PNP:</strong> P-N-P layers<br><br>
        
        <strong>Terminals:</strong><br>
        • <strong>Emitter (E):</strong> Heavily doped, emits carriers<br>
        • <strong>Base (B):</strong> Thin, lightly doped, controls current<br>
        • <strong>Collector (C):</strong> Collects carriers<br><br>
        
        <strong>Current Relationships:</strong><br>
        I_E = I_B + I_C<br>
        I_C = β × I_B (where β = 50-300)
    </div>
    """, unsafe_allow_html=True)
    
    # BJT calculator
    st.markdown("#### 🧮 BJT Current Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        i_base = st.number_input("Base Current I_B (μA)", 1.0, 1000.0, 10.0, 1.0)
    with col2:
        beta = st.number_input("Current Gain β", 50, 300, 100, 10)
    
    i_base_a = i_base * 1e-6  # Convert to A
    i_collector = beta * i_base_a
    i_emitter = i_base_a + i_collector
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("I_C", f"{i_collector*1000:.2f} mA")
    with col2:
        st.metric("I_E", f"{i_emitter*1000:.2f} mA")
    with col3:
        st.metric("I_C/I_B", f"{beta}×")
    
    st.markdown("---")
    st.markdown("### 2️⃣ MOSFET")
    
    st.markdown("""
    <div class="component-box">
        <strong>MOSFET Types:</strong><br>
        • <strong>N-Channel:</strong> Electrons are majority carriers<br>
        • <strong>P-Channel:</strong> Holes are majority carriers<br><br>
        
        <strong>Operation Modes:</strong><br>
        • <strong>Enhancement Mode:</strong> Normally OFF, needs V_GS > V_th<br>
        • <strong>Depletion Mode:</strong> Normally ON<br><br>
        
        <strong>Advantages over BJT:</strong><br>
        • High input impedance (voltage controlled)<br>
        • Faster switching<br>
        • Lower power consumption<br>
        • Used in digital circuits (CMOS)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Transistor as Switch")
    
    st.markdown("""
    <div class="example-box">
        <strong>Digital Switch Application:</strong><br>
        • <strong>Cutoff:</strong> V_BE < 0.7V, transistor OFF (open switch)<br>
        • <strong>Saturation:</strong> V_BE > 0.7V, I_B sufficient, transistor ON (closed switch)<br>
        • Used in digital logic, motor drivers, relay control
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: AMPLIFIERS ====================
with tabs[6]:
    st.markdown("## 🎚️ Amplifiers")
    
    st.markdown("### 1️⃣ Amplifier Basics")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Voltage Gain (A_v):</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            A_v = V_out / V_in
        </div>
        <strong>Gain in dB:</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            Gain (dB) = 20 log₁₀(A_v)
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Gain calculator
    st.markdown("#### 📊 Amplifier Gain Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        v_in = st.number_input("Input Voltage (mV)", 1.0, 1000.0, 10.0, 1.0)
    with col2:
        v_out = st.number_input("Output Voltage (V)", 0.1, 100.0, 1.0, 0.1)
    
    v_in_v = v_in / 1000  # Convert to V
    gain = v_out / v_in_v
    gain_db = 20 * np.log10(gain)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Voltage Gain", f"{gain:.1f}×")
    with col2:
        st.metric("Gain (dB)", f"{gain_db:.1f} dB")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Common Emitter Amplifier")
    
    st.markdown("""
    <div class="circuit-box">
        <strong>CE Amplifier Characteristics:</strong><br>
        • High voltage gain (A_v = -g_m × R_C)<br>
        • 180° phase shift (inverting)<br>
        • Moderate input/output impedance<br>
        • Most common configuration<br><br>
        
        <strong>Small Signal Model:</strong><br>
        • g_m = transconductance = I_C / V_T<br>
        • r_π = β / g_m (input resistance)<br>
        • V_T ≈ 26 mV at room temperature
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Frequency Response")
    
    st.markdown("""
    <div class="component-box">
        <strong>Bandwidth:</strong><br>
        • <strong>Lower cutoff (f_L):</strong> Due to coupling/bypass capacitors<br>
        • <strong>Upper cutoff (f_H):</strong> Due to transistor capacitances<br>
        • <strong>Bandwidth (BW):</strong> f_H - f_L<br>
        • <strong>Gain-Bandwidth Product:</strong> A_v × BW = constant
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: DIGITAL ELECTRONICS ====================
with tabs[7]:
    st.markdown("## 🔢 Digital Electronics")
    
    st.markdown("### 1️⃣ Logic Gates")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Basic Logic Gates:</strong><br>
        • <strong>NOT:</strong> Y = A̅<br>
        • <strong>AND:</strong> Y = A · B<br>
        • <strong>OR:</strong> Y = A + B<br>
        • <strong>NAND:</strong> Y = (A · B)̅<br>
        • <strong>NOR:</strong> Y = (A + B)̅<br>
        • <strong>XOR:</strong> Y = A ⊕ B<br>
        • <strong>XNOR:</strong> Y = (A ⊕ B)̅
    </div>
    """, unsafe_allow_html=True)
    
    # Truth table generator
    st.markdown("#### 📋 Interactive Truth Table")
    
    gate_type = st.selectbox("Select Logic Gate", ["AND", "OR", "NAND", "NOR", "XOR", "XNOR"])
    
    # Generate truth table
    truth_table = pd.DataFrame({
        'A': [0, 0, 1, 1],
        'B': [0, 1, 0, 1]
    })
    
    if gate_type == "AND":
        truth_table['Y'] = truth_table['A'] & truth_table['B']
    elif gate_type == "OR":
        truth_table['Y'] = truth_table['A'] | truth_table['B']
    elif gate_type == "NAND":
        truth_table['Y'] = ~(truth_table['A'] & truth_table['B']) & 1
    elif gate_type == "NOR":
        truth_table['Y'] = ~(truth_table['A'] | truth_table['B']) & 1
    elif gate_type == "XOR":
        truth_table['Y'] = truth_table['A'] ^ truth_table['B']
    else:  # XNOR
        truth_table['Y'] = ~(truth_table['A'] ^ truth_table['B']) & 1
    
    st.dataframe(truth_table, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Boolean Algebra")
    
    st.markdown("""
    <div class="circuit-box">
        <strong>Boolean Laws:</strong><br>
        • <strong>Identity:</strong> A + 0 = A, A · 1 = A<br>
        • <strong>Null:</strong> A + 1 = 1, A · 0 = 0<br>
        • <strong>Idempotent:</strong> A + A = A, A · A = A<br>
        • <strong>Complement:</strong> A + A̅ = 1, A · A̅ = 0<br>
        • <strong>De Morgan's:</strong> (A + B)̅ = A̅ · B̅, (A · B)̅ = A̅ + B̅
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Combinational Circuits")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Arithmetic Circuits:**
        - Half adder
        - Full adder
        - Subtractor
        - Multiplier
        """)
    
    with col2:
        st.markdown("""
        **Data Processing:**
        - Multiplexer (MUX)
        - Demultiplexer (DEMUX)
        - Encoder
        - Decoder
        """)

# ==================== TAB 9: OPERATIONAL AMPLIFIERS ====================
with tabs[8]:
    st.markdown("## 🎛️ Operational Amplifiers")
    
    st.markdown("### 1️⃣ Op-Amp Basics")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Ideal Op-Amp Characteristics:</strong><br>
        • Infinite input impedance (Z_in = ∞)<br>
        • Zero output impedance (Z_out = 0)<br>
        • Infinite voltage gain (A_v = ∞)<br>
        • Infinite bandwidth<br>
        • Zero offset voltage<br><br>
        
        <strong>Golden Rules:</strong><br>
        1. No current flows into inputs (I_+ = I_- = 0)<br>
        2. Voltages at inputs are equal (V_+ = V_-) when negative feedback
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Inverting Amplifier")
    
    st.markdown("""
    <div class="circuit-box">
        <strong>Inverting Amplifier:</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            V_out = -(R_f / R_in) × V_in
        </div>
        Gain = -R_f / R_in (negative = inverting)
    </div>
    """, unsafe_allow_html=True)
    
    # Inverting amplifier calculator
    st.markdown("#### 🧮 Inverting Amplifier Calculator")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        r_in = st.number_input("R_in (kΩ)", 1.0, 100.0, 10.0, 1.0)
    with col2:
        r_f = st.number_input("R_f (kΩ)", 1.0, 1000.0, 100.0, 1.0)
    with col3:
        v_in_op = st.number_input("V_in (V)", -10.0, 10.0, 1.0, 0.1)
    
    gain_inv = -r_f / r_in
    v_out_inv = gain_inv * v_in_op
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Gain", f"{gain_inv:.1f}×")
    with col2:
        st.metric("V_out", f"{v_out_inv:.2f} V")
    
    st.markdown("---")
    st.markdown("### 3️⃣ Non-Inverting Amplifier")
    
    st.markdown("""
    <div class="component-box">
        <strong>Non-Inverting Amplifier:</strong><br>
        <div style="text-align: center; margin: 1rem 0; font-size: 1.3rem;">
            V_out = (1 + R_f / R_in) × V_in
        </div>
        Gain = 1 + R_f / R_in (positive = non-inverting)
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 10: PRACTICE PROBLEMS ====================
with tabs[9]:
    st.markdown("## 🧮 Practice Problems")
    
    problems = [
        {
            "title": "Problem 1: Series Circuit",
            "question": "Three resistors (10Ω, 20Ω, 30Ω) are connected in series with a 12V battery. Find total resistance and current.",
            "hint": "R_total = R₁ + R₂ + R₃, then use Ohm's law",
            "solution": """
R_total = 10 + 20 + 30 = 60Ω

Using Ohm's Law:
I = V / R = 12V / 60Ω = 0.2A = 200mA

Current is same through all resistors in series.
            """
        },
        {
            "title": "Problem 2: BJT Amplifier",
            "question": "A BJT has β = 100 and I_B = 20μA. Find I_C and I_E.",
            "hint": "Use I_C = β × I_B and I_E = I_B + I_C",
            "solution": """
Given: β = 100, I_B = 20μA

I_C = β × I_B = 100 × 20μA = 2000μA = 2mA

I_E = I_B + I_C = 20μA + 2mA = 2.02mA

Note: I_E ≈ I_C (emitter current ≈ collector current)
            """
        },
        {
            "title": "Problem 3: Op-Amp Inverting Amplifier",
            "question": "Design an inverting amplifier with gain of -10. If R_in = 10kΩ, find R_f and V_out for V_in = 0.5V.",
            "hint": "Gain = -R_f/R_in, solve for R_f",
            "solution": """
Gain = -10 = -R_f / R_in
-10 = -R_f / 10kΩ
R_f = 100kΩ

V_out = Gain × V_in
V_out = -10 × 0.5V = -5V

The output is inverted (negative) and amplified 10×.
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
    <strong>EE101 - Electronics</strong><br>
    <small>UTel University | Department of Electrical Engineering</small>
</div>
""", unsafe_allow_html=True)
