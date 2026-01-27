
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Helper for custom CSS
def apply_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono&display=swap');
        
        * { font-family: 'Inter', sans-serif; }
        code, pre { font-family: 'JetBrains Mono', monospace !important; }
        
        .course-header {
            background: linear-gradient(135deg, #8b5cf6 0%, #6366f1 100%);
            color: white; padding: 2.5rem; border-radius: 20px;
            margin-bottom: 2rem; text-align: center;
        }
        .course-title { font-size: 2.5rem; font-weight: 800; margin-bottom: 0.5rem; }
        
        .theory-box {
            background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
            border-left: 5px solid #3b82f6; padding: 1.5rem;
            border-radius: 12px; margin: 1rem 0;
        }
        .example-box {
            background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
            border-left: 5px solid #10b981; padding: 1.5rem;
            border-radius: 12px; margin: 1rem 0;
        }
        .theorem-box {
            background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
            border-left: 5px solid #f59e0b; padding: 1.5rem;
            border-radius: 12px; margin: 1rem 0;
        }
        .definition {
            background: #faf5ff; border-left: 4px solid #8b5cf6;
            padding: 1rem; border-radius: 8px; margin: 0.5rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

def render_ma101_simulation():
    """Interactive Simulation for Calculus (Limits & Derivatives)"""
    st.markdown("### 🧮 Interactive Limit Calculator")
    
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
    
    st.altair_chart(line, use_container_width=True)
    st.info(f"📊 The limit as x → {a_val} is approximately **{limit_val:.2f}**")

def render_ma102_simulation():
    """Interactive Matrix Calculator for Linear Algebra"""
    st.markdown("### 🧮 2×2 Matrix Calculator")
    
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

def render_ce101_simulation():
    """Interactive Simulation for Programming (CE101)"""
    st.markdown("### 💻 Code Playground")
    st.markdown("Experiment with basic Python structures directly in your browser.")

    code_template = st.selectbox("Select a template:", 
        ["Hello World", "For Loop", "If-Else", "Function Definition"])
    
    default_code = ""
    if code_template == "Hello World":
        default_code = 'print("Hello, UTel University!")'
    elif code_template == "For Loop":
        default_code = 'for i in range(5):\n    print(f"Iteration {i}")'
    elif code_template == "If-Else":
        default_code = 'x = 10\nif x > 5:\n    print("x is greater than 5")\nelse:\n    print("x is small")'
    else:
        default_code = 'def greet(name):\n    return f"Hello, {name}!"\n\nprint(greet("Student"))'

    code_input = st.text_area("Write your Python code here:", value=default_code, height=150)
    
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("▶️ Run Code"):
            st.markdown("**Output:**")
            try:
                # Capture stdout
                import sys
                from io import StringIO
                old_stdout = sys.stdout
                redirected_output = sys.stdout = StringIO()
                
                exec(code_input, {})
                
                sys.stdout = old_stdout
                st.code(redirected_output.getvalue())
            except Exception as e:
                st.error(f"Error: {e}")
    
    with col2:
        st.info("💡 Tip: Use `print()` to see output.")

def render_ph101_simulation():
    """Interactive Simulation for Physics (PH101)"""
    st.markdown("### 🧪 Harmonic Oscillator Simulation")
    
    col1, col2 = st.columns(2)
    with col1:
        amplitude = st.slider("Amplitude (A)", 0.1, 5.0, 1.0, 0.1)
        frequency = st.slider("Frequency (f)", 0.1, 5.0, 1.0, 0.1)
    with col2:
        phase = st.slider("Phase (φ)", 0.0, 2*np.pi, 0.0, 0.1)
        damping = st.slider("Damping (ζ)", 0.0, 1.0, 0.0, 0.05)
        
    t = np.linspace(0, 10, 500)
    # y = A * exp(-ζt) * cos(2πft + φ)
    y = amplitude * np.exp(-damping * t) * np.cos(2 * np.pi * frequency * t + phase)
    
    df_oscillator = pd.DataFrame({'Time (s)': t, 'Displacement (m)': y})
    
    chart = alt.Chart(df_oscillator).mark_line(color='#ef4444', strokeWidth=2).encode(
        x='Time (s)',
        y='Displacement (m)',
        tooltip=['Time (s)', 'Displacement (m)']
    ).interactive()
    
    st.altair_chart(chart, use_container_width=True)
    
    # Calculate energy
    k = 10  # Spring constant (assumed)
    m = k / (2 * np.pi * frequency)**2
    potential_energy = 0.5 * k * y**2
    # Velocity v = dy/dt
    # y' = A * [ -ζ * exp(-ζt) * cos(2πft + φ) - exp(-ζt) * 2πf * sin(2πft + φ) ]
    # y' = -A * exp(-ζt) * [ ζ * cos(...) + 2πf * sin(...) ]
    velocity = -amplitude * np.exp(-damping*t) * (damping * np.cos(2*np.pi*frequency*t + phase) + 2*np.pi*frequency * np.sin(2*np.pi*frequency*t + phase))
    kinetic_energy = 0.5 * m * velocity**2
    
    st.info(f"System Properties: Mass = {m:.2f} kg, Spring Constant = {k} N/m")

def render_ce302_simulation():
    """Interactive Simulation for Digital Systems (CE302)"""
    st.markdown("### ⚡ Logic Gate Simulator")
    
    col1, col2 = st.columns(2)
    with col1:
        gate_type = st.selectbox("Select Gate", ["AND", "OR", "NOT", "NAND", "NOR", "XOR"])
    with col2:
        input_a = st.checkbox("Input A", value=False)
        input_b = st.checkbox("Input B", value=False) if gate_type != "NOT" else False
        
    result = False
    if gate_type == "AND":
        result = input_a and input_b
    elif gate_type == "OR":
        result = input_a or input_b
    elif gate_type == "NOT":
        result = not input_a
    elif gate_type == "NAND":
        result = not (input_a and input_b)
    elif gate_type == "NOR":
        result = not (input_a or input_b)
    elif gate_type == "XOR":
        result = input_a != input_b
        
    st.markdown("---")
    c1, c2, c3 = st.columns([1, 1, 1])
    with c1:
        st.metric("Input A", "1" if input_a else "0")
    with c2:
        if gate_type != "NOT":
            st.metric("Input B", "1" if input_b else "0")
    with c3:
        st.metric("Output", "1" if result else "0", delta="High" if result else "Low")
        
    # Truth Table
    st.markdown("#### Truth Table")
    if gate_type == "NOT":
        df = pd.DataFrame({'A': [0, 1], 'Output': [1, 0]})
    else:
        # Generate truth table for 2 inputs
        inputs = [(0,0), (0,1), (1,0), (1,1)]
        outputs = []
        for a, b in inputs:
            if gate_type == "AND": out = a and b
            elif gate_type == "OR": out = a or b
            elif gate_type == "NAND": out = not (a and b)
            elif gate_type == "NOR": out = not (a or b)
            elif gate_type == "XOR": out = a != b
            outputs.append(int(out))
            
        df = pd.DataFrame({
            'A': [i[0] for i in inputs],
            'B': [i[1] for i in inputs],
            'Output': outputs
        })
    
    # Highlight current state
    def highlight_row(row):
        is_active = False
        if gate_type == "NOT":
            is_active = (row['A'] == int(input_a))
        else:
            is_active = (row['A'] == int(input_a)) and (row['B'] == int(input_b))
        return ['background-color: #dbeafe' if is_active else '' for _ in row]

    st.dataframe(df.style.apply(highlight_row, axis=1), use_container_width=True)

def render_ce103_simulation():
    """Interactive Simulation for Computer Architecture (CE103)"""
    st.markdown("### 🖥️ Simple ALU & Number Systems")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Input A**")
        val_a = st.number_input("Decimal Value A", value=10, step=1)
        bin_a = format(val_a & 0xFF, '08b')
        hex_a = format(val_a & 0xFF, '02X')
        st.code(f"BIN: {bin_a}\nHEX: 0x{hex_a}")
        
    with col2:
        st.markdown("**Input B**")
        val_b = st.number_input("Decimal Value B", value=6, step=1)
        bin_b = format(val_b & 0xFF, '08b')
        hex_b = format(val_b & 0xFF, '02X')
        st.code(f"BIN: {bin_b}\nHEX: 0x{hex_b}")

    st.markdown("---")
    st.markdown("**ALU Operation**")
    op = st.selectbox("Operation", ["ADD", "SUB", "AND", "OR", "XOR", "LSHIFT", "RSHIFT"])
    
    res = 0
    if op == "ADD": res = val_a + val_b
    elif op == "SUB": res = val_a - val_b
    elif op == "AND": res = val_a & val_b
    elif op == "OR": res = val_a | val_b
    elif op == "XOR": res = val_a ^ val_b
    elif op == "LSHIFT": res = val_a << 1
    elif op == "RSHIFT": res = val_a >> 1
    
    # Mask to 8-bit for visualization simplicity
    res_8bit = res & 0xFF
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Result (Dec)", res)
    c2.metric("Result (Bin)", format(res_8bit, '08b'))
    c3.metric("Result (Hex)", f"0x{format(res_8bit, '02X')}")
    
    # Visual Bits
    st.caption("8-bit Visualization:")
    bits = [int(x) for x in format(res_8bit, '08b')]
    cols = st.columns(8)
    for i, bit in enumerate(bits):
        cols[i].button(str(bit), key=f"bit_{i}", disabled=True, type="primary" if bit else "secondary")

def render_ee101_simulation():
    """Interactive Simulation for Electronics (EE101)"""
    st.markdown("### ⚡ Circuit Simulator (Ohm's Law)")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("#### Parameters")
        voltage = st.slider("Voltage (V)", 0.0, 24.0, 5.0, 0.5)
        resistance = st.slider("Resistance (Ω)", 10.0, 1000.0, 100.0, 10.0)
        
        current = voltage / resistance * 1000 # mA
        power = (voltage ** 2) / resistance # Watts
        
        st.markdown("#### Calculations")
        st.metric("Current (I)", f"{current:.1f} mA")
        st.metric("Power (P)", f"{power:.3f} W")
        
    with col2:
        st.markdown("#### V-I Characteristic Plot")
        # Generate VI curve for fixed R
        v_range = np.linspace(0, 24, 100)
        i_vals = (v_range / resistance) * 1000 # mA
        
        df_vi = pd.DataFrame({'Voltage (V)': v_range, 'Current (mA)': i_vals})
        
        # Point for current state
        curr_point = pd.DataFrame({'Voltage (V)': [voltage], 'Current (mA)': [current]})
        
        base = alt.Chart(df_vi).mark_line().encode(x='Voltage (V)', y='Current (mA)')
        point = alt.Chart(curr_point).mark_point(color='red', size=100, filled=True).encode(
            x='Voltage (V)', y='Current (mA)', tooltip=['Voltage (V)', 'Current (mA)']
        )
        
        st.altair_chart(base + point, use_container_width=True)
        
        st.info("Ohm's Law: $V = I \\cdot R$")

def render_ce201_simulation():
    """Interactive Simulation for OOP (CE201)"""
    st.markdown("### 🧬 Object-Oriented Designer")
    
    st.markdown("#### Class Definition: `Car`")
    col1, col2 = st.columns(2)
    with col1:
        color = st.selectbox("Color", ["Red", "Blue", "Black", "White"])
        model = st.text_input("Model", "Tesla Model 3")
    with col2:
        speed = st.slider("Max Speed (km/h)", 100, 300, 200)
        is_electric = st.checkbox("Is Electric?", value=True)
        
    st.markdown("#### Object Instantiation")
    if st.button("Create Object"):
        st.code(f"""
class Car:
    def __init__(self, color, model, speed, is_electric):
        self.color = "{color}"
        self.model = "{model}"
        self.max_speed = {speed}
        self.is_electric = {is_electric}

    def drive(self):
        return f"Driving the {color} {model} at {speed} km/h!"

# Object
my_car = Car("{color}", "{model}", {speed}, {is_electric})
print(my_car.drive())
        """, language="python")
        st.success(f"Output: Driving the {color} {model} at {speed} km/h!")

def render_ce202_simulation():
    """Interactive Simulation for Assembly (CE202)"""
    st.markdown("### ⚙️ Simple Register Simulator (x86)")
    
    # Registers
    if 'eax' not in st.session_state: st.session_state.eax = 0
    if 'ebx' not in st.session_state: st.session_state.ebx = 0
    
    c1, c2 = st.columns(2)
    c1.metric("EAX", f"0x{st.session_state.eax:08X}")
    c2.metric("EBX", f"0x{st.session_state.ebx:08X}")
    
    st.markdown("#### Instructions")
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        instr = st.selectbox("Instruction", ["MOV", "ADD", "SUB", "INC", "DEC"])
    with col2:
        target = st.selectbox("Target", ["EAX", "EBX"])
        
    with col3:
        val = 0
        if instr in ["MOV", "ADD", "SUB"]:
            val = st.number_input("Value (Imm)", 0, 100, 5)
            
    if st.button("Execute Step"):
        if instr == "MOV":
            if target == "EAX": st.session_state.eax = val
            else: st.session_state.ebx = val
        elif instr == "ADD":
            if target == "EAX": st.session_state.eax += val
            else: st.session_state.ebx += val
        elif instr == "SUB":
            if target == "EAX": st.session_state.eax -= val
            else: st.session_state.ebx -= val
        elif instr == "INC":
            if target == "EAX": st.session_state.eax += 1
            else: st.session_state.ebx += 1
        elif instr == "DEC":
            if target == "EAX": st.session_state.eax -= 1
            else: st.session_state.ebx -= 1
            
        st.rerun()

def render_ce203_simulation():
    """Interactive Simulation for OS (CE203) - CPU Scheduling"""
    st.markdown("### ⏱️ CPU Scheduling Visualization (FIFO)")
    
    processes = [
        {"id": "P1", "burst": 5, "color": "#ef4444"},
        {"id": "P2", "burst": 3, "color": "#3b82f6"},
        {"id": "P3", "burst": 8, "color": "#10b981"},
        {"id": "P4", "burst": 6, "color": "#f59e0b"}
    ]
    
    # Allow reordering
    st.text("Drag to reorder processes (Simulated by manual input order for now):")
    cols = st.columns(4)
    order = []
    for i, p in enumerate(processes):
        p['order'] = cols[i].number_input(f"{p['id']} Order", 1, 4, i+1)
        
    processes.sort(key=lambda x: x['order'])
    
    # Gantt Chart Calculation
    start_time = 0
    gantt = []
    
    for p in processes:
        gantt.append({
            "Process": p['id'],
            "Start": start_time,
            "End": start_time + p['burst'],
            "Color": p['color']
        })
        start_time += p['burst']
        
    df_gantt = pd.DataFrame(gantt)
    
    chart = alt.Chart(df_gantt).mark_bar().encode(
        x='Start',
        x2='End',
        y='Process',
        color=alt.Color('Process', scale=None, legend=None),
        tooltip=['Process', 'Start', 'End']
    ).properties(height=200)
    
    st.altair_chart(chart, use_container_width=True)
    
    avg_turnaround = sum(x['End'] for x in gantt) / 4
    st.info(f"Average Turnaround Time: {avg_turnaround:.2f} units")

def render_ma201_simulation():
    """Interactive Simulation for Statistics (MA201)"""
    st.markdown("### 📊 Normal Distribution Visualizer")
    
    mu = st.slider("Mean (μ)", -5.0, 5.0, 0.0, 0.5)
    sigma = st.slider("Standard Deviation (σ)", 0.1, 5.0, 1.0, 0.1)
    
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 200)
    y = (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu)/sigma)**2)
    
    df_dist = pd.DataFrame({'x': x, 'Probability Density': y})
    
    area = alt.Chart(df_dist).mark_area(opacity=0.3, color='#3b82f6').encode(
        x='x',
        y='Probability Density'
    )
    line = alt.Chart(df_dist).mark_line(color='#3b82f6').encode(
        x='x',
        y='Probability Density'
    )
    
    st.altair_chart(area + line, use_container_width=True)

def render_ce204_simulation():
    """Interactive Simulation for Algorithms (CE204)"""
    st.markdown("### 🔢 Sorting Algorithm Visualizer")
    
    algo = st.selectbox("Algorithm", ["Bubble Sort", "Quick Sort (Visual Only)"])
    n = st.slider("Number of Elements", 10, 50, 20)
    
    if st.button("Generate New Array"):
        st.session_state.arr = np.random.randint(1, 100, n).tolist()
        
    if 'arr' not in st.session_state:
        st.session_state.arr = np.random.randint(1, 100, n).tolist()
        
    arr = st.session_state.arr.copy()
    
    # Simple Bubble Sort Step-by-Step (Simulated)
    # For a real visualizer we'd need animation, here we show init vs sorted
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Initial Array**")
        st.bar_chart(pd.DataFrame({'Value': arr}))
        
    with col2:
        st.markdown("**Sorted Array**")
        arr.sort()
        st.bar_chart(pd.DataFrame({'Value': arr}))
        
    st.info("ℹ️ Full animation requires more complex state management. This compares Initial vs Sorted states.")
    
    st.code("""
# Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    """, language="python")

def render_ce301_simulation():
    """Interactive Simulation for Computer Networks (CE301)"""
    st.markdown("### 🌐 IPv4 Subnet Calculator")
    
    ip_str = st.text_input("IP Address", "192.168.1.1")
    cidr = st.slider("CIDR / Prefix", 1, 32, 24)
    
    try:
        # Simple manual calculation avoiding 'ipaddress' module complexities for now/compatibility
        parts = list(map(int, ip_str.split('.')))
        if len(parts) != 4: raise ValueError
        
        ip_bin = 0
        for p in parts: ip_bin = (ip_bin << 8) + p
        
        mask_bin = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF
        net_bin = ip_bin & mask_bin
        broad_bin = net_bin | (~mask_bin & 0xFFFFFFFF)
        
        def to_ip(n):
            return f"{(n >> 24) & 0xFF}.{(n >> 16) & 0xFF}.{(n >> 8) & 0xFF}.{n & 0xFF}"
            
        net_addr = to_ip(net_bin)
        broad_addr = to_ip(broad_bin)
        hosts = (2 ** (32 - cidr)) - 2 if cidr < 31 else 0
        
        col1, col2 = st.columns(2)
        col1.metric("Network Address", net_addr)
        col2.metric("Broadcast Address", broad_addr)
        
        col3, col4 = st.columns(2)
        col3.metric("Subnet Mask", to_ip(mask_bin))
        col4.metric("Usable Hosts", f"{hosts:,}")
        
    except:
        st.error("Invalid IP Address format")

def render_ce304_simulation():
    """Interactive Simulation for Databases (CE304)"""
    st.markdown("### 🗄️ SQL Playground (Mock)")
    
    # Mock Database
    students = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'gpa': [3.8, 3.2, 3.9, 2.5]
    })
    
    st.markdown("**Table: `students`**")
    st.dataframe(students)
    
    query_type = st.radio("Query", ["SELECT *", "SELECT WHERE gpa > 3.5", "COUNT(*)"])
    
    st.markdown("**Result:**")
    if query_type == "SELECT *":
        st.code("SELECT * FROM students;")
        st.dataframe(students)
    elif query_type == "SELECT WHERE gpa > 3.5":
        st.code("SELECT * FROM students WHERE gpa > 3.5;")
        st.dataframe(students[students['gpa'] > 3.5])
    elif query_type == "COUNT(*)":
        st.code("SELECT COUNT(*) FROM students;")
        st.metric("Count", len(students))

# Map course ID to simulation function
SIMULATION_MAP = {
    "MA101": render_ma101_simulation,
    "MA102": render_ma102_simulation,
    "CE101": render_ce101_simulation,
    "PH101": render_ph101_simulation,
    "CE302": render_ce302_simulation,
    "CE103": render_ce103_simulation,
    "EE101": render_ee101_simulation,
    "CE201": render_ce201_simulation,
    "CE202": render_ce202_simulation,
    "CE203": render_ce203_simulation,
    "MA201": render_ma201_simulation,
    "CE204": render_ce204_simulation,
    "CE301": render_ce301_simulation,
    "CE304": render_ce304_simulation
}
