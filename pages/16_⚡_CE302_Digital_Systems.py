import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="CE302 - Digital Systems and Peripherals", page_icon="⚡", layout="wide")

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
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
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
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .logic-box {
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
    
    .peripheral-box {
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
    
    .truth-table {
        font-family: 'JetBrains Mono', monospace;
        background: #f9fafb;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="course-header">
    <div style="font-size: 1.2rem; opacity: 0.9;">CE302</div>
    <div class="course-title">Digital Systems and Peripherals</div>
    <div>⚡ 3 Credits | Semester 4 | Systems</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "4")
with col3:
    st.metric("Difficulty", "4/7")
with col4:
    st.metric("Hours/Week", "6")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "🔢 Number Systems",
    "🚪 Logic Gates",
    "🔄 Combinational Circuits",
    "⏰ Sequential Circuits",
    "🤖 Finite State Machines",
    "💾 Memory Systems",
    "🔌 Peripheral Interfacing",
    "🎯 Practice Problems",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive study of digital logic design, combinational and sequential circuits, and peripheral interfacing. 
        Covers Boolean algebra, logic gates, flip-flops, registers, counters, memory systems, and I/O interfacing. 
        Emphasizes both theoretical foundations and practical implementation using HDL (Verilog/VHDL). Students will 
        design and simulate digital circuits and interface with real-world peripherals.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Master number systems and Boolean algebra",
        "Design combinational circuits (adders, multiplexers, decoders)",
        "Implement sequential circuits (flip-flops, registers, counters)",
        "Design finite state machines (FSM)",
        "Understand memory organization and types",
        "Interface with peripherals (UART, SPI, I2C)",
        "Use HDL for circuit design (Verilog/VHDL)",
        "Optimize digital circuits for speed and area"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Fundamentals:**
        - Number systems (Binary, Octal, Hex)
        - Boolean algebra and theorems
        - Logic gates (AND, OR, NOT, NAND, NOR, XOR)
        - Karnaugh maps (K-maps)
        - Quine-McCluskey method
        
        **Combinational Logic:**
        - Adders and subtractors
        - Multiplexers and demultiplexers
        - Encoders and decoders
        - Comparators
        - ALU design
        """)
    
    with col2:
        st.markdown("""
        **Sequential Logic:**
        - Latches and flip-flops
        - Registers and shift registers
        - Counters (synchronous, asynchronous)
        - Finite state machines
        - Timing analysis
        
        **Systems:**
        - Memory (RAM, ROM, Cache)
        - Peripheral interfaces (UART, SPI, I2C)
        - Bus protocols
        - Microcontroller interfacing
        - FPGA design
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Digital Design", "author": "Morris Mano & Michael Ciletti", "type": "Textbook"},
        {"title": "Digital Fundamentals", "author": "Thomas Floyd", "type": "Textbook"},
        {"title": "FPGA Prototyping by Verilog Examples", "author": "Pong Chu", "type": "HDL"},
        {"title": "The Art of Electronics", "author": "Horowitz & Hill", "type": "Classic"}
    ]
    
    for resource in resources:
        st.markdown(f"📖 **{resource['title']}** by {resource['author']} ({resource['type']})")

# ==================== TAB 2: NUMBER SYSTEMS ====================
with tabs[1]:
    st.markdown("## 🔢 Number Systems")
    
    st.markdown("### 1️⃣ Common Number Systems")
    
    number_systems = {
        'System': ['Binary', 'Octal', 'Decimal', 'Hexadecimal'],
        'Base': [2, 8, 10, 16],
        'Digits': ['0-1', '0-7', '0-9', '0-9, A-F'],
        'Example': ['1010₂', '12₈', '10₁₀', 'A₁₆']
    }
    
    df_numbers = pd.DataFrame(number_systems)
    st.dataframe(df_numbers, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Number Conversion")
    
    st.markdown("""
    <div class="logic-box">
        <strong>Decimal to Binary:</strong><br>
        Repeatedly divide by 2, read remainders bottom-up<br>
        Example: 13₁₀ = 1101₂<br><br>
        
        <strong>Binary to Decimal:</strong><br>
        Σ(bit × 2^position)<br>
        Example: 1101₂ = 1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 13₁₀<br><br>
        
        <strong>Binary to Hexadecimal:</strong><br>
        Group 4 bits, convert each group<br>
        Example: 11010110₂ = D6₁₆<br><br>
        
        <strong>Hexadecimal to Binary:</strong><br>
        Convert each hex digit to 4 bits<br>
        Example: A5₁₆ = 10100101₂
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive Number Converter
    st.markdown("#### 🧮 Number System Converter")
    
    col1, col2 = st.columns(2)
    
    with col1:
        input_base = st.selectbox("From Base", ["Binary (2)", "Octal (8)", "Decimal (10)", "Hexadecimal (16)"])
        input_value = st.text_input("Enter value", "1010")
    
    with col2:
        output_base = st.selectbox("To Base", ["Decimal (10)", "Binary (2)", "Octal (8)", "Hexadecimal (16)"])
    
    try:
        # Parse input base
        base_map = {"Binary (2)": 2, "Octal (8)": 8, "Decimal (10)": 10, "Hexadecimal (16)": 16}
        from_base = base_map[input_base]
        to_base = base_map[output_base]
        
        # Convert to decimal first
        decimal_value = int(input_value, from_base)
        
        # Convert to target base
        if to_base == 10:
            result = str(decimal_value)
        elif to_base == 2:
            result = bin(decimal_value)[2:]
        elif to_base == 8:
            result = oct(decimal_value)[2:]
        elif to_base == 16:
            result = hex(decimal_value)[2:].upper()
        
        st.success(f"**Result:** {result}")
        st.info(f"Decimal equivalent: {decimal_value}")
        
    except ValueError:
        st.error("Invalid input for selected base")
    
    st.markdown("---")
    st.markdown("### 3️⃣ Signed Number Representation")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Sign-Magnitude:</strong><br>
        MSB = sign (0=positive, 1=negative), remaining bits = magnitude<br>
        Example: +5 = 0101, -5 = 1101 (4-bit)<br><br>
        
        <strong>1's Complement:</strong><br>
        Negative = flip all bits<br>
        Example: +5 = 0101, -5 = 1010<br>
        Problem: Two representations of zero<br><br>
        
        <strong>2's Complement (Most Common):</strong><br>
        Negative = flip all bits + 1<br>
        Example: +5 = 0101, -5 = 1011<br>
        Range (n bits): -2^(n-1) to 2^(n-1)-1<br>
        Advantage: Single zero, simple arithmetic
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: LOGIC GATES ====================
with tabs[2]:
    st.markdown("## 🚪 Logic Gates")
    
    st.markdown("### 1️⃣ Basic Logic Gates")
    
    # Truth tables
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**AND Gate**")
        st.markdown("""
        ```
        A B | Y
        ----+---
        0 0 | 0
        0 1 | 0
        1 0 | 0
        1 1 | 1
        ```
        Y = A · B
        """)
    
    with col2:
        st.markdown("**OR Gate**")
        st.markdown("""
        ```
        A B | Y
        ----+---
        0 0 | 0
        0 1 | 1
        1 0 | 1
        1 1 | 1
        ```
        Y = A + B
        """)
    
    with col3:
        st.markdown("**NOT Gate**")
        st.markdown("""
        ```
        A | Y
        --+---
        0 | 1
        1 | 0
        ```
        Y = A'
        """)
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**NAND Gate**")
        st.markdown("""
        ```
        A B | Y
        ----+---
        0 0 | 1
        0 1 | 1
        1 0 | 1
        1 1 | 0
        ```
        Y = (A · B)'
        """)
    
    with col2:
        st.markdown("**NOR Gate**")
        st.markdown("""
        ```
        A B | Y
        ----+---
        0 0 | 1
        0 1 | 0
        1 0 | 0
        1 1 | 0
        ```
        Y = (A + B)'
        """)
    
    with col3:
        st.markdown("**XOR Gate**")
        st.markdown("""
        ```
        A B | Y
        ----+---
        0 0 | 0
        0 1 | 1
        1 0 | 1
        1 1 | 0
        ```
        Y = A ⊕ B
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Boolean Algebra Theorems")
    
    st.markdown("""
    <div class="logic-box">
        <strong>Identity Laws:</strong><br>
        • A + 0 = A<br>
        • A · 1 = A<br><br>
        
        <strong>Null Laws:</strong><br>
        • A + 1 = 1<br>
        • A · 0 = 0<br><br>
        
        <strong>Idempotent Laws:</strong><br>
        • A + A = A<br>
        • A · A = A<br><br>
        
        <strong>Complement Laws:</strong><br>
        • A + A' = 1<br>
        • A · A' = 0<br>
        • (A')' = A<br><br>
        
        <strong>Commutative Laws:</strong><br>
        • A + B = B + A<br>
        • A · B = B · A<br><br>
        
        <strong>Associative Laws:</strong><br>
        • (A + B) + C = A + (B + C)<br>
        • (A · B) · C = A · (B · C)<br><br>
        
        <strong>Distributive Laws:</strong><br>
        • A · (B + C) = A·B + A·C<br>
        • A + (B · C) = (A+B) · (A+C)<br><br>
        
        <strong>De Morgan's Theorems:</strong><br>
        • (A + B)' = A' · B'<br>
        • (A · B)' = A' + B'
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Universal Gates")
    
    st.markdown("""
    <div class="theory-box">
        <strong>NAND and NOR are Universal Gates</strong><br><br>
        
        Any Boolean function can be implemented using only NAND or only NOR gates<br><br>
        
        <strong>Using NAND:</strong><br>
        • NOT: A NAND A = A'<br>
        • AND: (A NAND B) NAND (A NAND B) = A · B<br>
        • OR: (A NAND A) NAND (B NAND B) = A + B<br><br>
        
        <strong>Using NOR:</strong><br>
        • NOT: A NOR A = A'<br>
        • OR: (A NOR B) NOR (A NOR B) = A + B<br>
        • AND: (A NOR A) NOR (B NOR B) = A · B
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: COMBINATIONAL CIRCUITS ====================
with tabs[3]:
    st.markdown("## 🔄 Combinational Circuits")
    
    st.markdown("### 1️⃣ Adders")
    
    st.markdown("""
    <div class="circuit-box">
        <strong>Half Adder:</strong><br>
        Adds two 1-bit numbers<br>
        • Sum = A ⊕ B<br>
        • Carry = A · B<br><br>
        
        <strong>Full Adder:</strong><br>
        Adds three 1-bit numbers (A, B, Carry-in)<br>
        • Sum = A ⊕ B ⊕ Cin<br>
        • Cout = (A · B) + (Cin · (A ⊕ B))<br><br>
        
        <strong>Ripple Carry Adder:</strong><br>
        Chain of full adders for n-bit addition<br>
        • Delay: O(n) - carry propagates through all bits<br><br>
        
        <strong>Carry Lookahead Adder:</strong><br>
        Faster addition using parallel carry generation<br>
        • Delay: O(log n)<br>
        • More complex hardware
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Multiplexers and Demultiplexers")
    
    st.markdown("""
    <div class="circuit-box">
        <strong>Multiplexer (MUX):</strong><br>
        Selects one of many inputs based on select lines<br>
        • 2:1 MUX: Y = S'·A + S·B<br>
        • 4:1 MUX: 4 inputs, 2 select lines<br>
        • 8:1 MUX: 8 inputs, 3 select lines<br>
        • n:1 MUX needs log₂(n) select lines<br><br>
        
        <strong>Demultiplexer (DEMUX):</strong><br>
        Routes one input to one of many outputs<br>
        • Inverse operation of MUX<br>
        • 1:4 DEMUX: 1 input, 2 select lines, 4 outputs<br><br>
        
        <strong>Applications:</strong><br>
        • Data routing<br>
        • Function implementation<br>
        • Parallel to serial conversion
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Encoders and Decoders")
    
    st.markdown("""
    <div class="circuit-box">
        <strong>Encoder:</strong><br>
        Converts 2ⁿ inputs to n-bit binary code<br>
        • 4:2 Encoder: 4 inputs → 2-bit output<br>
        • Priority Encoder: Handles multiple active inputs<br><br>
        
        <strong>Decoder:</strong><br>
        Converts n-bit binary to 2ⁿ outputs<br>
        • 2:4 Decoder: 2-bit input → 4 outputs<br>
        • 3:8 Decoder: 3-bit input → 8 outputs<br>
        • Used for memory address decoding<br><br>
        
        <strong>7-Segment Decoder:</strong><br>
        • BCD to 7-segment display<br>
        • Displays digits 0-9
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: SEQUENTIAL CIRCUITS ====================
with tabs[4]:
    st.markdown("## ⏰ Sequential Circuits")
    
    st.markdown("### 1️⃣ Latches vs Flip-Flops")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Latch (Level-Triggered):**
        - Transparent when enable is active
        - Output changes with input
        - Asynchronous
        - Example: SR Latch, D Latch
        
        **Characteristics:**
        - Simpler design
        - Faster
        - Timing issues (race conditions)
        """)
    
    with col2:
        st.markdown("""
        **Flip-Flop (Edge-Triggered):**
        - Changes only on clock edge
        - Holds value between edges
        - Synchronous
        - Example: D, JK, T Flip-Flops
        
        **Characteristics:**
        - More complex
        - Predictable timing
        - Preferred in synchronous systems
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Common Flip-Flops")
    
    st.markdown("""
    <div class="circuit-box">
        <strong>D Flip-Flop:</strong><br>
        • Q(next) = D<br>
        • Stores one bit<br>
        • Most common in digital systems<br><br>
        
        <strong>JK Flip-Flop:</strong><br>
        • J=0, K=0: No change<br>
        • J=0, K=1: Reset (Q=0)<br>
        • J=1, K=0: Set (Q=1)<br>
        • J=1, K=1: Toggle<br><br>
        
        <strong>T Flip-Flop:</strong><br>
        • T=0: No change<br>
        • T=1: Toggle<br>
        • Used in counters<br><br>
        
        <strong>SR Flip-Flop:</strong><br>
        • S=1, R=0: Set<br>
        • S=0, R=1: Reset<br>
        • S=0, R=0: No change<br>
        • S=1, R=1: Invalid (avoid)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Registers and Counters")
    
    st.markdown("""
    <div class="circuit-box">
        <strong>Registers:</strong><br>
        • Group of flip-flops<br>
        • Store multi-bit data<br>
        • Types: Parallel load, Shift register<br><br>
        
        <strong>Shift Registers:</strong><br>
        • Serial-In Serial-Out (SISO)<br>
        • Serial-In Parallel-Out (SIPO)<br>
        • Parallel-In Serial-Out (PISO)<br>
        • Parallel-In Parallel-Out (PIPO)<br>
        • Applications: Data conversion, delay<br><br>
        
        <strong>Counters:</strong><br>
        • <strong>Asynchronous (Ripple):</strong> Clock cascades, slower<br>
        • <strong>Synchronous:</strong> All FFs clocked together, faster<br>
        • <strong>Up Counter:</strong> Increments<br>
        • <strong>Down Counter:</strong> Decrements<br>
        • <strong>Modulo-N Counter:</strong> Counts 0 to N-1<br>
        • <strong>Ring Counter:</strong> Circular shift<br>
        • <strong>Johnson Counter:</strong> Twisted ring
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: FSM ====================
with tabs[5]:
    st.markdown("## 🤖 Finite State Machines")
    
    st.markdown("### 1️⃣ FSM Types")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Moore Machine:**
        - Output depends only on current state
        - Output changes on clock edge
        - More states needed
        - Synchronous output
        
        **Example:**
        ```
        State A: Output = 0
        State B: Output = 1
        ```
        """)
    
    with col2:
        st.markdown("""
        **Mealy Machine:**
        - Output depends on state AND input
        - Output can change immediately
        - Fewer states needed
        - Asynchronous output
        
        **Example:**
        ```
        State A, Input=0: Output = 0
        State A, Input=1: Output = 1
        ```
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ FSM Design Steps")
    
    st.markdown("""
    <div class="theory-box">
        <strong>FSM Design Process:</strong><br><br>
        
        1. <strong>State Diagram:</strong> Draw states and transitions<br>
        2. <strong>State Table:</strong> List present state, input, next state, output<br>
        3. <strong>State Assignment:</strong> Assign binary codes to states<br>
        4. <strong>Flip-Flop Selection:</strong> Choose FF type (usually D)<br>
        5. <strong>Excitation Table:</strong> Determine FF inputs<br>
        6. <strong>Logic Minimization:</strong> Use K-maps or Boolean algebra<br>
        7. <strong>Circuit Implementation:</strong> Draw circuit diagram<br>
        8. <strong>Verification:</strong> Simulate and test
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Example: Sequence Detector")
    
    st.markdown("""
    <div class="circuit-box">
        <strong>Problem:</strong> Detect sequence "101" in input stream<br><br>
        
        <strong>States:</strong><br>
        • S0: Initial state (no match)<br>
        • S1: Detected "1"<br>
        • S2: Detected "10"<br>
        • S3: Detected "101" (output = 1)<br><br>
        
        <strong>State Transitions (Moore):</strong><br>
        • S0 --1--> S1<br>
        • S0 --0--> S0<br>
        • S1 --0--> S2<br>
        • S1 --1--> S1<br>
        • S2 --1--> S3<br>
        • S2 --0--> S0<br>
        • S3 --0--> S2<br>
        • S3 --1--> S1<br><br>
        
        <strong>Outputs:</strong><br>
        S0, S1, S2: Output = 0<br>
        S3: Output = 1
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: MEMORY SYSTEMS ====================
with tabs[6]:
    st.markdown("## 💾 Memory Systems")
    
    st.markdown("### 1️⃣ Memory Types")
    
    memory_comparison = {
        'Type': ['SRAM', 'DRAM', 'ROM', 'EPROM', 'EEPROM', 'Flash'],
        'Volatile': ['Yes', 'Yes', 'No', 'No', 'No', 'No'],
        'Speed': ['Fast', 'Slow', 'Fast', 'Fast', 'Medium', 'Medium'],
        'Density': ['Low', 'High', 'High', 'High', 'Medium', 'High'],
        'Cost': ['High', 'Low', 'Low', 'Medium', 'High', 'Medium'],
        'Use Case': ['Cache', 'Main RAM', 'Firmware', 'Legacy', 'Config', 'Storage']
    }
    
    df_memory = pd.DataFrame(memory_comparison)
    st.dataframe(df_memory, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Memory Organization")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Memory Specifications:</strong><br><br>
        
        <strong>Capacity:</strong> Total storage<br>
        • Example: 1K × 8 = 1024 words × 8 bits/word<br>
        • Address lines: log₂(words) = 10 bits<br>
        • Data lines: 8 bits<br><br>
        
        <strong>Access Time:</strong> Time to read/write<br>
        • SRAM: 1-10 ns<br>
        • DRAM: 50-100 ns<br>
        • Flash: 25-100 μs (write)<br><br>
        
        <strong>Memory Hierarchy:</strong><br>
        1. Registers (fastest, smallest)<br>
        2. L1 Cache<br>
        3. L2 Cache<br>
        4. L3 Cache<br>
        5. Main Memory (RAM)<br>
        6. SSD/HDD (slowest, largest)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Cache Memory")
    
    st.markdown("""
    <div class="circuit-box">
        <strong>Cache Mapping Techniques:</strong><br><br>
        
        <strong>1. Direct Mapped:</strong><br>
        • Each memory block maps to exactly one cache line<br>
        • Simple, fast<br>
        • High conflict misses<br><br>
        
        <strong>2. Fully Associative:</strong><br>
        • Any memory block can go anywhere in cache<br>
        • Complex, slower<br>
        • Low conflict misses<br><br>
        
        <strong>3. Set Associative (n-way):</strong><br>
        • Compromise between direct and fully associative<br>
        • Block maps to a set, can go in any line within set<br>
        • Most common (2-way, 4-way, 8-way)<br><br>
        
        <strong>Replacement Policies:</strong><br>
        • LRU (Least Recently Used)<br>
        • FIFO (First In First Out)<br>
        • Random
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: PERIPHERALS ====================
with tabs[7]:
    st.markdown("## 🔌 Peripheral Interfacing")
    
    st.markdown("### 1️⃣ Communication Protocols")
    
    st.markdown("""
    <div class="peripheral-box">
        <strong>UART (Universal Asynchronous Receiver-Transmitter):</strong><br>
        • Serial, asynchronous<br>
        • 2 wires: TX, RX<br>
        • Configurable baud rate (9600, 115200, etc.)<br>
        • Start bit, data bits (5-9), parity, stop bit<br>
        • Simple, widely used<br>
        • Example: Serial console, GPS modules<br><br>
        
        <strong>SPI (Serial Peripheral Interface):</strong><br>
        • Serial, synchronous<br>
        • 4 wires: MOSI, MISO, SCK, SS/CS<br>
        • Full-duplex<br>
        • Fast (MHz range)<br>
        • Master-slave architecture<br>
        • Example: SD cards, displays, sensors<br><br>
        
        <strong>I2C (Inter-Integrated Circuit):</strong><br>
        • Serial, synchronous<br>
        • 2 wires: SDA (data), SCL (clock)<br>
        • Multi-master, multi-slave<br>
        • 7-bit or 10-bit addressing<br>
        • Slower than SPI (100 kHz, 400 kHz, 3.4 MHz)<br>
        • Example: EEPROMs, RTCs, sensors
    </div>
    """, unsafe_allow_html=True)
    
    # Protocol comparison
    protocol_comparison = {
        'Feature': ['Wires', 'Speed', 'Duplex', 'Complexity', 'Distance'],
        'UART': ['2', 'Medium', 'Full', 'Low', 'Short'],
        'SPI': ['4+', 'Fast', 'Full', 'Medium', 'Very Short'],
        'I2C': ['2', 'Slow-Medium', 'Half', 'Medium', 'Short']
    }
    
    df_protocols = pd.DataFrame(protocol_comparison)
    st.dataframe(df_protocols, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ GPIO (General Purpose I/O)")
    
    st.markdown("""
    <div class="peripheral-box">
        <strong>GPIO Modes:</strong><br><br>
        
        <strong>Input:</strong><br>
        • Read digital signals<br>
        • Pull-up/pull-down resistors<br>
        • Debouncing for buttons<br><br>
        
        <strong>Output:</strong><br>
        • Drive LEDs, relays<br>
        • Push-pull or open-drain<br>
        • Current limiting<br><br>
        
        <strong>Alternate Functions:</strong><br>
        • UART TX/RX<br>
        • SPI MOSI/MISO<br>
        • PWM output<br>
        • ADC input
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Interrupts")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Interrupt Mechanism:</strong><br><br>
        
        <strong>Types:</strong><br>
        • Hardware interrupts (external events)<br>
        • Software interrupts (system calls)<br>
        • Exceptions (errors)<br><br>
        
        <strong>Priority:</strong><br>
        • Non-maskable (NMI): Cannot be disabled<br>
        • Maskable: Can be enabled/disabled<br>
        • Priority levels for nested interrupts<br><br>
        
        <strong>Interrupt Service Routine (ISR):</strong><br>
        1. Save context (registers)<br>
        2. Execute ISR code<br>
        3. Restore context<br>
        4. Return from interrupt<br><br>
        
        <strong>Best Practices:</strong><br>
        • Keep ISRs short<br>
        • Avoid blocking operations<br>
        • Use flags for main loop processing
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 9: PRACTICE PROBLEMS ====================
with tabs[8]:
    st.markdown("## 🎯 Practice Problems")
    
    problems = [
        {
            "title": "Problem 1: Boolean Simplification",
            "question": "Simplify: F = A'B'C + A'BC + AB'C + ABC",
            "hint": "Factor out common terms or use K-map",
            "solution": """
**Solution:**

Method 1: Algebraic
```
F = A'B'C + A'BC + AB'C + ABC
  = A'C(B' + B) + AC(B' + B)
  = A'C(1) + AC(1)
  = A'C + AC
  = C(A' + A)
  = C(1)
  = C
```

Method 2: K-map
```
     BC
A    00  01  11  10
0    0   0   1   1
1    0   0   1   1
```

Group all 1s in C column → F = C

**Answer: F = C**
            """
        },
        {
            "title": "Problem 2: Counter Design",
            "question": "Design a modulo-5 counter (counts 0→1→2→3→4→0) using JK flip-flops.",
            "hint": "3 flip-flops needed (2³ = 8 > 5). Create state table and find JK inputs.",
            "solution": """
**Solution:**

**States:** 000, 001, 010, 011, 100 (0-4)

**State Table:**
```
Present  Next    J2 K2  J1 K1  J0 K0
Q2Q1Q0   Q2Q1Q0
000      001     0  X   0  X   1  X
001      010     0  X   1  X   X  1
010      011     0  X   X  0   1  X
011      100     1  X   X  1   X  1
100      000     X  1   0  X   0  X
```

**K-maps for JK inputs:**
(Simplified expressions)
- J2 = Q1·Q0
- K2 = Q1'·Q0'
- J1 = Q0
- K1 = Q0
- J0 = Q2'
- K0 = 1

**Circuit:** Connect JK FFs according to above equations
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

# ==================== TAB 10: YOUTUBE RESOURCES ====================
with tabs[9]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning Digital Systems and Logic Design</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {
            "title": "Digital Electronics",
            "channel": "Neso Academy",
            "url": "https://www.youtube.com/playlist?list=PLBlnK6fEyqRjMH3mWf6kwqiTbT798eAOm",
            "description": "Complete digital electronics course from basics",
            "duration": "Playlist (~150 videos)"
        },
        {
            "title": "Digital Logic Design",
            "channel": "Gate Smashers",
            "url": "https://www.youtube.com/playlist?list=PLxCzCOWd7aiGmXg4NoX6R31AsC5LeCPHe",
            "description": "Comprehensive digital logic tutorials",
            "duration": "Playlist"
        },
        {
            "title": "Introduction to Digital Systems",
            "channel": "MIT OpenCourseWare",
            "url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP62WVs95MNq3dQBqY2vGOtQ2",
            "description": "MIT 6.004 - Computation Structures",
            "duration": "Full Course"
        }
    ]
    
    for resource in beginner_resources:
        st.markdown(f"""
        **[{resource['title']}]({resource['url']})**  
        📺 Channel: {resource['channel']} | ⏱️ {resource['duration']}  
        {resource['description']}
        """)
        st.markdown("---")
    
    # Intermediate Level
    st.markdown("### 🟡 Intermediate Level")
    
    intermediate_resources = [
        {
            "title": "Verilog HDL Tutorial",
            "channel": "Nandland",
            "url": "https://www.youtube.com/playlist?list=PLnAoag7Ew-vp6jKhPPKJpPPKJpPPKJpPP",
            "description": "Learn Verilog for FPGA design",
            "duration": "Playlist"
        },
        {
            "title": "Digital Design and Computer Architecture",
            "channel": "ETH Zurich",
            "url": "https://www.youtube.com/playlist?list=PL5Q2soXY2Zi-IXWTT7xoNYpst5-zdZQ6y",
            "description": "Advanced digital design concepts",
            "duration": "Full Course"
        },
        {
            "title": "FPGA Design Tutorial",
            "channel": "Intel FPGA",
            "url": "https://www.youtube.com/c/IntelFPGA",
            "description": "FPGA programming and design",
            "duration": "Channel"
        }
    ]
    
    for resource in intermediate_resources:
        st.markdown(f"""
        **[{resource['title']}]({resource['url']})**  
        📺 Channel: {resource['channel']} | ⏱️ {resource['duration']}  
        {resource['description']}
        """)
        st.markdown("---")
    
    # Advanced Level
    st.markdown("### 🔴 Advanced Level")
    
    advanced_resources = [
        {
            "title": "Advanced Digital Design",
            "channel": "UC Berkeley",
            "url": "https://www.youtube.com/playlist?list=PLkFD6_40KJIxrKaukIqIZMrtSRf6hNdPp",
            "description": "EECS 151 - Digital Design and Integrated Circuits",
            "duration": "Full Course"
        },
        {
            "title": "ASIC Design Flow",
            "channel": "VLSI System Design",
            "url": "https://www.youtube.com/c/VLSISystemDesign",
            "description": "ASIC and VLSI design",
            "duration": "Channel"
        },
        {
            "title": "Hardware Security",
            "channel": "NYU Tandon",
            "url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP62WVs95MNq3dQBqY2vGOtQ2",
            "description": "Security in digital systems",
            "duration": "Playlist"
        }
    ]
    
    for resource in advanced_resources:
        st.markdown(f"""
        **[{resource['title']}]({resource['url']})**  
        📺 Channel: {resource['channel']} | ⏱️ {resource['duration']}  
        {resource['description']}
        """)
        st.markdown("---")
    
    # Practical/Hands-on
    st.markdown("### 🛠️ Practical & Hands-on")
    
    practical_resources = [
        {
            "title": "Arduino Tutorials",
            "channel": "Paul McWhorter",
            "url": "https://www.youtube.com/playlist?list=PLGs0VKk2DiYw-L-RibttcvK-WBZm8WLEP",
            "description": "Microcontroller interfacing and programming",
            "duration": "Playlist"
        },
        {
            "title": "FPGA Projects",
            "channel": "Digilent",
            "url": "https://www.youtube.com/c/DigilentInc",
            "description": "Hands-on FPGA projects",
            "duration": "Channel"
        },
        {
            "title": "Digital Circuit Simulation",
            "channel": "Logisim Evolution",
            "url": "https://github.com/logisim-evolution/logisim-evolution",
            "description": "Free digital circuit simulator",
            "duration": "Tool"
        }
    ]
    
    for resource in practical_resources:
        st.markdown(f"""
        **[{resource['title']}]({resource['url']})**  
        📺 Channel: {resource['channel']} | ⏱️ {resource['duration']}  
        {resource['description']}
        """)
        st.markdown("---")
    
    # Study Tips
    st.markdown("### 💡 Study Tips")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Recommended Learning Path:</strong><br>
        1. Master number systems and Boolean algebra<br>
        2. Understand logic gates and truth tables<br>
        3. Design combinational circuits (adders, MUX, decoders)<br>
        4. Learn sequential circuits (flip-flops, registers, counters)<br>
        5. Design finite state machines<br>
        6. Study memory systems and organization<br>
        7. Learn HDL (Verilog or VHDL)<br>
        8. Practice with FPGA boards<br><br>
        
        <strong>Tools & Simulators:</strong><br>
        • <strong>Logisim:</strong> Free digital circuit simulator<br>
        • <strong>ModelSim:</strong> HDL simulator<br>
        • <strong>Quartus/Vivado:</strong> FPGA design tools<br>
        • <strong>Arduino/Raspberry Pi:</strong> Microcontroller practice<br><br>
        
        <strong>Practice Resources:</strong><br>
        • Design circuits on paper first<br>
        • Simulate before building<br>
        • Build real circuits on breadboard<br>
        • Program FPGAs with your designs
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE302 - Digital Systems and Peripherals</strong><br>
    <small>UTel University | Department of Computer Engineering</small>
</div>
""", unsafe_allow_html=True)
