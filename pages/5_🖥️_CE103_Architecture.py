import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="CE103 - Computer Architecture", page_icon="🖥️", layout="wide")

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
        background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%);
        border-left: 5px solid #8b5cf6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .architecture-box {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-left: 5px solid #3b82f6;
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
    
    .example-box {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="course-header">
    <div style="font-size: 1.2rem; opacity: 0.9;">CE103</div>
    <div class="course-title">Computer Architecture</div>
    <div>🖥️ 3 Credits | Semester 2 | Core</div>
</div>
""", unsafe_allow_html=True)

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
    "🔢 Number Systems & Data",
    "⚙️ CPU Architecture",
    "💾 Memory Hierarchy",
    "🚀 Pipelining",
    "📦 Cache Design",
    "🔄 Parallel Processing",
    "🏗️ Modern Architectures",
    "🧮 Performance Analysis",
    "🎯 Practice Problems",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive study of computer architecture from transistors to modern multicore systems. 
        Covers instruction set architecture (ISA), CPU design, memory hierarchy, pipelining, cache 
        optimization, and parallel processing. Emphasizes quantitative performance analysis and 
        design trade-offs in modern computer systems.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Understand computer organization from gates to systems",
        "Design and analyze CPU architectures (RISC, CISC)",
        "Optimize memory hierarchy and cache performance",
        "Implement and analyze pipelined processors",
        "Apply parallel processing concepts (ILP, TLP, DLP)",
        "Evaluate performance using quantitative metrics",
        "Design modern computer systems with trade-off analysis",
        "Understand GPU and accelerator architectures"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Fundamentals:**
        - Number systems and data representation
        - Boolean algebra and logic gates
        - Combinational and sequential circuits
        - Instruction Set Architecture (ISA)
        - Assembly language programming
        
        **CPU Design:**
        - Single-cycle datapath
        - Multi-cycle implementation
        - Pipelining and hazards
        - Branch prediction
        - Out-of-order execution
        """)
    
    with col2:
        st.markdown("""
        **Memory Systems:**
        - Memory hierarchy principles
        - Cache design and optimization
        - Virtual memory and TLB
        - DRAM and SRAM technologies
        - Memory consistency models
        
        **Advanced Topics:**
        - Superscalar processors
        - VLIW and EPIC architectures
        - Multicore and multiprocessor systems
        - GPU architecture
        - Domain-specific accelerators
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Computer Organization and Design", "author": "Patterson & Hennessy", "type": "Textbook"},
        {"title": "Computer Architecture: A Quantitative Approach", "author": "Hennessy & Patterson", "type": "Graduate"},
        {"title": "Digital Design and Computer Architecture", "author": "Harris & Harris", "type": "Fundamentals"},
        {"title": "Modern Processor Design", "author": "Shen & Lipasti", "type": "Advanced"}
    ]
    
    for resource in resources:
        st.markdown(f"📖 **{resource['title']}** by {resource['author']} ({resource['type']})")

# ==================== TAB 2: NUMBER SYSTEMS ====================
with tabs[1]:
    st.markdown("## 🔢 Number Systems & Data Representation")
    
    st.markdown("### 1️⃣ Number Systems")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Common Number Systems:</strong><br>
        • <strong>Binary (Base-2):</strong> 0, 1<br>
        • <strong>Octal (Base-8):</strong> 0-7<br>
        • <strong>Decimal (Base-10):</strong> 0-9<br>
        • <strong>Hexadecimal (Base-16):</strong> 0-9, A-F
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive number converter
    st.markdown("#### 🔄 Number System Converter")
    
    col1, col2 = st.columns(2)
    with col1:
        decimal_input = st.number_input("Enter decimal number", 0, 65535, 42, 1)
    with col2:
        bits = st.selectbox("Bit width", [8, 16, 32], index=1)
    
    binary = bin(decimal_input)[2:].zfill(bits)
    octal = oct(decimal_input)[2:]
    hexadecimal = hex(decimal_input)[2:].upper()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Binary", binary)
    with col2:
        st.metric("Octal", octal)
    with col3:
        st.metric("Hexadecimal", f"0x{hexadecimal}")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Integer Representation")
    
    st.markdown("""
    <div class="architecture-box">
        <strong>Signed Integer Representations:</strong><br><br>
        <strong>1. Sign-Magnitude:</strong> MSB is sign bit<br>
        Example (8-bit): +5 = 00000101, -5 = 10000101<br><br>
        <strong>2. One's Complement:</strong> Invert all bits for negative<br>
        Example (8-bit): +5 = 00000101, -5 = 11111010<br><br>
        <strong>3. Two's Complement:</strong> Invert and add 1 (most common)<br>
        Example (8-bit): +5 = 00000101, -5 = 11111011<br>
        Range: -2^(n-1) to 2^(n-1) - 1
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Floating-Point Representation")
    
    st.markdown("""
    <div class="theory-box">
        <strong>IEEE 754 Standard:</strong><br><br>
        <strong>Single Precision (32-bit):</strong><br>
        • Sign: 1 bit<br>
        • Exponent: 8 bits (biased by 127)<br>
        • Mantissa: 23 bits<br>
        Value = (-1)^sign × 1.mantissa × 2^(exponent-127)<br><br>
        <strong>Double Precision (64-bit):</strong><br>
        • Sign: 1 bit<br>
        • Exponent: 11 bits (biased by 1023)<br>
        • Mantissa: 52 bits
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: CPU ARCHITECTURE ====================
with tabs[2]:
    st.markdown("## ⚙️ CPU Architecture")
    
    st.markdown("### 1️⃣ Instruction Set Architecture (ISA)")
    
    st.markdown("""
    <div class="architecture-box">
        <strong>ISA Design Principles:</strong><br>
        • <strong>RISC (Reduced Instruction Set Computer):</strong><br>
          - Simple, fixed-length instructions<br>
          - Load/store architecture<br>
          - Many registers<br>
          - Examples: ARM, RISC-V, MIPS<br><br>
        • <strong>CISC (Complex Instruction Set Computer):</strong><br>
          - Variable-length instructions<br>
          - Memory-to-memory operations<br>
          - Fewer registers<br>
          - Examples: x86, x86-64
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 2️⃣ MIPS Instruction Formats")
    
    st.code("""
# R-Type (Register): op rs rt rd shamt funct
ADD  $t0, $t1, $t2    # $t0 = $t1 + $t2
SUB  $t0, $t1, $t2    # $t0 = $t1 - $t2
AND  $t0, $t1, $t2    # $t0 = $t1 & $t2

# I-Type (Immediate): op rs rt immediate
ADDI $t0, $t1, 100    # $t0 = $t1 + 100
LW   $t0, 0($t1)      # $t0 = Memory[$t1 + 0]
SW   $t0, 4($t1)      # Memory[$t1 + 4] = $t0
BEQ  $t0, $t1, Label  # if ($t0 == $t1) goto Label

# J-Type (Jump): op address
J    Label            # goto Label
JAL  Function         # Jump and link (function call)
    """, language="assembly")
    
    st.markdown("---")
    st.markdown("### 3️⃣ Single-Cycle Datapath")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Datapath Components:</strong><br>
        1. <strong>Program Counter (PC):</strong> Holds address of current instruction<br>
        2. <strong>Instruction Memory:</strong> Stores program instructions<br>
        3. <strong>Register File:</strong> 32 general-purpose registers<br>
        4. <strong>ALU:</strong> Performs arithmetic/logic operations<br>
        5. <strong>Data Memory:</strong> Stores program data<br>
        6. <strong>Control Unit:</strong> Generates control signals
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="performance-box">
        <strong>Single-Cycle Performance:</strong><br>
        • Clock period = longest instruction time<br>
        • CPI (Cycles Per Instruction) = 1<br>
        • Simple but inefficient (wastes time on fast instructions)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 4️⃣ Multi-Cycle Implementation")
    
    st.markdown("""
    <div class="architecture-box">
        <strong>Instruction Execution Stages:</strong><br>
        1. <strong>IF (Instruction Fetch):</strong> Fetch instruction from memory<br>
        2. <strong>ID (Instruction Decode):</strong> Decode and read registers<br>
        3. <strong>EX (Execute):</strong> Perform ALU operation<br>
        4. <strong>MEM (Memory Access):</strong> Read/write data memory<br>
        5. <strong>WB (Write Back):</strong> Write result to register<br><br>
        <strong>Advantages:</strong><br>
        • Different instructions take different cycles<br>
        • Better resource utilization<br>
        • Shorter clock period
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: MEMORY HIERARCHY ====================
with tabs[3]:
    st.markdown("## 💾 Memory Hierarchy")
    
    st.markdown("### 1️⃣ Memory Hierarchy Principles")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Memory Hierarchy (Fast → Slow):</strong><br>
        1. <strong>Registers:</strong> ~1 cycle, ~1 KB<br>
        2. <strong>L1 Cache:</strong> ~4 cycles, ~32-64 KB<br>
        3. <strong>L2 Cache:</strong> ~10 cycles, ~256 KB - 1 MB<br>
        4. <strong>L3 Cache:</strong> ~40 cycles, ~8-32 MB<br>
        5. <strong>Main Memory (DRAM):</strong> ~100 cycles, ~4-64 GB<br>
        6. <strong>SSD:</strong> ~10,000 cycles, ~256 GB - 2 TB<br>
        7. <strong>HDD:</strong> ~1,000,000 cycles, ~1-10 TB
    </div>
    """, unsafe_allow_html=True)
    
    # Memory hierarchy visualization
    st.markdown("#### 📊 Memory Hierarchy Visualization")
    
    memory_data = pd.DataFrame({
        'Level': ['Registers', 'L1 Cache', 'L2 Cache', 'L3 Cache', 'DRAM', 'SSD', 'HDD'],
        'Access Time (cycles)': [1, 4, 10, 40, 100, 10000, 1000000],
        'Size (KB)': [1, 64, 512, 16384, 8388608, 268435456, 1073741824],
        'Cost per GB ($)': [10000, 5000, 2000, 1000, 10, 0.2, 0.03]
    })
    
    # Log scale chart for access time
    access_chart = alt.Chart(memory_data).mark_bar(color='#8b5cf6').encode(
        x=alt.X('Level:N', sort=['Registers', 'L1 Cache', 'L2 Cache', 'L3 Cache', 'DRAM', 'SSD', 'HDD']),
        y=alt.Y('Access Time (cycles):Q', scale=alt.Scale(type='log'), title='Access Time (cycles, log scale)'),
        tooltip=['Level', 'Access Time (cycles)', 'Size (KB)', 'Cost per GB ($)']
    ).properties(
        width=700,
        height=400,
        title="Memory Hierarchy: Access Time Comparison"
    )
    
    st.altair_chart(access_chart, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Locality Principles")
    
    st.markdown("""
    <div class="architecture-box">
        <strong>Temporal Locality:</strong><br>
        If a memory location is accessed, it's likely to be accessed again soon.<br>
        Example: Loop variables, frequently called functions<br><br>
        <strong>Spatial Locality:</strong><br>
        If a memory location is accessed, nearby locations are likely to be accessed soon.<br>
        Example: Array traversal, sequential code execution
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Virtual Memory")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Virtual Memory Concepts:</strong><br>
        • <strong>Address Translation:</strong> Virtual → Physical<br>
        • <strong>Page Table:</strong> Maps virtual pages to physical frames<br>
        • <strong>TLB (Translation Lookaside Buffer):</strong> Cache for page table entries<br>
        • <strong>Page Fault:</strong> Requested page not in memory<br>
        • <strong>Page Size:</strong> Typically 4 KB or 4 MB<br><br>
        <strong>Benefits:</strong><br>
        • Memory protection<br>
        • Efficient memory use<br>
        • Simplified programming (large address space)
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: PIPELINING ====================
with tabs[4]:
    st.markdown("## 🚀 Pipelining")
    
    st.markdown("### 1️⃣ Pipeline Concept")
    
    st.markdown("""
    <div class="architecture-box">
        <strong>5-Stage Pipeline:</strong><br>
        1. <strong>IF:</strong> Instruction Fetch<br>
        2. <strong>ID:</strong> Instruction Decode / Register Read<br>
        3. <strong>EX:</strong> Execute / Address Calculation<br>
        4. <strong>MEM:</strong> Memory Access<br>
        5. <strong>WB:</strong> Write Back<br><br>
        <strong>Ideal Speedup:</strong> Number of stages (5×)<br>
        <strong>Actual Speedup:</strong> Less due to hazards and overhead
    </div>
    """, unsafe_allow_html=True)
    
    # Pipeline visualization
    st.markdown("#### 📊 Pipeline Execution Timeline")
    
    instructions = ['I1', 'I2', 'I3', 'I4', 'I5']
    stages = ['IF', 'ID', 'EX', 'MEM', 'WB']
    
    pipeline_data = []
    for i, inst in enumerate(instructions):
        for j, stage in enumerate(stages):
            pipeline_data.append({
                'Instruction': inst,
                'Stage': stage,
                'Cycle': i + j + 1,
                'Stage_Order': j
            })
    
    df_pipeline = pd.DataFrame(pipeline_data)
    
    pipeline_chart = alt.Chart(df_pipeline).mark_rect().encode(
        x=alt.X('Cycle:O', title='Clock Cycle'),
        y=alt.Y('Instruction:N', title='Instruction'),
        color=alt.Color('Stage:N', scale=alt.Scale(scheme='category10')),
        tooltip=['Instruction', 'Stage', 'Cycle']
    ).properties(
        width=700,
        height=300,
        title="5-Stage Pipeline Execution"
    )
    
    st.altair_chart(pipeline_chart, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Pipeline Hazards")
    
    st.markdown("""
    <div class="performance-box">
        <strong>1. Structural Hazards:</strong><br>
        Hardware cannot support all combinations of instructions simultaneously.<br>
        <strong>Solution:</strong> Add more hardware resources or stall pipeline.<br><br>
        
        <strong>2. Data Hazards:</strong><br>
        Instruction depends on result of previous instruction still in pipeline.<br>
        <strong>Solutions:</strong><br>
        • Forwarding (bypassing)<br>
        • Stalling (pipeline bubble)<br>
        • Compiler scheduling<br><br>
        
        <strong>3. Control Hazards:</strong><br>
        Branch instruction changes PC, but next instructions already fetched.<br>
        <strong>Solutions:</strong><br>
        • Branch prediction<br>
        • Delayed branch<br>
        • Branch target buffer (BTB)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Data Forwarding")
    
    st.code("""
# Example: Data Hazard
ADD $t0, $t1, $t2    # $t0 = $t1 + $t2
SUB $t3, $t0, $t4    # $t3 = $t0 - $t4  (needs $t0 from ADD)

# Without forwarding: Need to stall 2 cycles
# With forwarding: Forward result from EX/MEM or MEM/WB stage
    """, language="assembly")

# ==================== TAB 6: CACHE DESIGN ====================
with tabs[5]:
    st.markdown("## 📦 Cache Design")
    
    st.markdown("### 1️⃣ Cache Organization")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Cache Mapping Techniques:</strong><br><br>
        <strong>1. Direct Mapped:</strong><br>
        • Each memory block maps to exactly one cache line<br>
        • Index = (Block Address) mod (Number of Cache Lines)<br>
        • Fast but high conflict misses<br><br>
        
        <strong>2. Fully Associative:</strong><br>
        • Block can go anywhere in cache<br>
        • Requires comparison with all tags<br>
        • Flexible but expensive<br><br>
        
        <strong>3. N-Way Set Associative:</strong><br>
        • Compromise between direct and fully associative<br>
        • Cache divided into sets, each with N lines<br>
        • Common: 2-way, 4-way, 8-way
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Cache Performance")
    
    st.markdown("""
    <div class="performance-box">
        <strong>Performance Metrics:</strong><br><br>
        <strong>Hit Rate:</strong> Fraction of accesses found in cache<br>
        <strong>Miss Rate:</strong> 1 - Hit Rate<br>
        <strong>Hit Time:</strong> Time to access cache<br>
        <strong>Miss Penalty:</strong> Time to fetch from lower level<br><br>
        <strong>Average Memory Access Time (AMAT):</strong><br>
        AMAT = Hit Time + (Miss Rate × Miss Penalty)
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive cache calculator
    st.markdown("#### 🧮 Cache Performance Calculator")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        hit_rate = st.slider("Hit Rate (%)", 50, 99, 95)
    with col2:
        hit_time = st.number_input("Hit Time (cycles)", 1, 10, 1)
    with col3:
        miss_penalty = st.number_input("Miss Penalty (cycles)", 10, 200, 100)
    
    miss_rate = (100 - hit_rate) / 100
    amat = hit_time + (miss_rate * miss_penalty)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Miss Rate", f"{miss_rate*100:.1f}%")
    with col2:
        st.metric("AMAT", f"{amat:.2f} cycles")
    
    st.markdown("---")
    st.markdown("### 3️⃣ Cache Replacement Policies")
    
    st.markdown("""
    <div class="architecture-box">
        <strong>Replacement Algorithms:</strong><br>
        • <strong>LRU (Least Recently Used):</strong> Replace least recently accessed block<br>
        • <strong>FIFO (First In First Out):</strong> Replace oldest block<br>
        • <strong>Random:</strong> Replace random block<br>
        • <strong>LFU (Least Frequently Used):</strong> Replace least frequently accessed
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: PARALLEL PROCESSING ====================
with tabs[6]:
    st.markdown("## 🔄 Parallel Processing")
    
    st.markdown("### 1️⃣ Types of Parallelism")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Instruction-Level Parallelism (ILP):</strong><br>
        • Execute multiple instructions simultaneously<br>
        • Pipelining, superscalar, VLIW<br>
        • Limited by data dependencies<br><br>
        
        <strong>Thread-Level Parallelism (TLP):</strong><br>
        • Execute multiple threads simultaneously<br>
        • Multicore processors, SMT (Simultaneous Multithreading)<br>
        • Better scalability<br><br>
        
        <strong>Data-Level Parallelism (DLP):</strong><br>
        • Same operation on multiple data elements<br>
        • SIMD (Single Instruction Multiple Data)<br>
        • Vector processors, GPUs
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Amdahl's Law")
    
    st.markdown("""
    <div class="performance-box">
        <strong>Amdahl's Law:</strong><br>
        Speedup = 1 / [(1 - P) + P/N]<br><br>
        where:<br>
        • P = Fraction of program that can be parallelized<br>
        • N = Number of processors<br>
        • (1 - P) = Serial portion (cannot be parallelized)
    </div>
    """, unsafe_allow_html=True)
    
    # Amdahl's Law calculator
    st.markdown("#### 📊 Amdahl's Law Calculator")
    
    col1, col2 = st.columns(2)
    with col1:
        parallel_fraction = st.slider("Parallel Fraction (%)", 0, 100, 90)
    with col2:
        num_processors = st.slider("Number of Processors", 1, 64, 8)
    
    P = parallel_fraction / 100
    speedup = 1 / ((1 - P) + P / num_processors)
    efficiency = (speedup / num_processors) * 100
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Speedup", f"{speedup:.2f}×")
    with col2:
        st.metric("Efficiency", f"{efficiency:.1f}%")
    
    # Visualize Amdahl's Law
    processors = list(range(1, 65))
    speedups = [1 / ((1 - P) + P / n) for n in processors]
    
    df_amdahl = pd.DataFrame({
        'Processors': processors,
        'Speedup': speedups
    })
    
    amdahl_chart = alt.Chart(df_amdahl).mark_line(strokeWidth=3, color='#8b5cf6').encode(
        x=alt.X('Processors:Q', title='Number of Processors'),
        y=alt.Y('Speedup:Q', title='Speedup'),
        tooltip=['Processors', 'Speedup']
    ).properties(
        width=700,
        height=400,
        title=f"Amdahl's Law: {parallel_fraction}% Parallelizable"
    )
    
    st.altair_chart(amdahl_chart, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Multicore Architectures")
    
    st.markdown("""
    <div class="architecture-box">
        <strong>Cache Coherence:</strong><br>
        Problem: Multiple cores with private caches may have inconsistent data.<br><br>
        <strong>MESI Protocol:</strong><br>
        • <strong>M (Modified):</strong> Cache line modified, main memory stale<br>
        • <strong>E (Exclusive):</strong> Cache line clean, only copy<br>
        • <strong>S (Shared):</strong> Cache line clean, may have copies<br>
        • <strong>I (Invalid):</strong> Cache line invalid
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: MODERN ARCHITECTURES ====================
with tabs[7]:
    st.markdown("## 🏗️ Modern Architectures")
    
    st.markdown("### 1️⃣ Superscalar Processors")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Superscalar Features:</strong><br>
        • Multiple instruction issue per cycle<br>
        • Out-of-order execution<br>
        • Register renaming<br>
        • Branch prediction<br>
        • Speculative execution<br><br>
        <strong>Examples:</strong> Intel Core, AMD Ryzen, Apple M-series
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ GPU Architecture")
    
    st.markdown("""
    <div class="architecture-box">
        <strong>GPU vs CPU:</strong><br><br>
        <strong>CPU:</strong><br>
        • Few powerful cores (4-64)<br>
        • Low latency, high per-thread performance<br>
        • Complex control logic<br>
        • Large caches<br><br>
        
        <strong>GPU:</strong><br>
        • Thousands of simple cores<br>
        • High throughput, massive parallelism<br>
        • Simple control logic<br>
        • Small caches per core<br>
        • Optimized for SIMD workloads
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Domain-Specific Accelerators")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **AI/ML Accelerators:**
        - Google TPU (Tensor Processing Unit)
        - NVIDIA Tensor Cores
        - Apple Neural Engine
        - Specialized for matrix operations
        """)
    
    with col2:
        st.markdown("""
        **Other Accelerators:**
        - Crypto accelerators (AES, SHA)
        - Video encoders/decoders
        - Network processors
        - FPGA-based accelerators
        """)

# ==================== TAB 9: PERFORMANCE ANALYSIS ====================
with tabs[8]:
    st.markdown("## 🧮 Performance Analysis")
    
    st.markdown("### 1️⃣ Performance Metrics")
    
    st.markdown("""
    <div class="performance-box">
        <strong>Key Metrics:</strong><br><br>
        <strong>Execution Time:</strong> Time to complete a task<br>
        Performance = 1 / Execution Time<br><br>
        
        <strong>CPU Time:</strong><br>
        CPU Time = Instruction Count × CPI × Clock Period<br>
        CPU Time = (Instruction Count × CPI) / Clock Rate<br><br>
        
        <strong>CPI (Cycles Per Instruction):</strong><br>
        CPI = Total Cycles / Instruction Count<br><br>
        
        <strong>MIPS (Million Instructions Per Second):</strong><br>
        MIPS = (Instruction Count) / (Execution Time × 10^6)<br>
        MIPS = Clock Rate / (CPI × 10^6)
    </div>
    """, unsafe_allow_html=True)
    
    # Performance calculator
    st.markdown("#### 🧮 CPU Performance Calculator")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        inst_count = st.number_input("Instructions (millions)", 1, 10000, 1000)
    with col2:
        cpi = st.number_input("CPI", 0.5, 10.0, 2.0, 0.1)
    with col3:
        clock_rate = st.number_input("Clock Rate (GHz)", 0.5, 5.0, 3.0, 0.1)
    
    # Calculate metrics
    total_cycles = inst_count * cpi
    cpu_time = total_cycles / (clock_rate * 1000)  # in milliseconds
    mips = (inst_count / cpu_time) if cpu_time > 0 else 0
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Cycles", f"{total_cycles:.0f}M")
    with col2:
        st.metric("CPU Time", f"{cpu_time:.2f} ms")
    with col3:
        st.metric("MIPS", f"{mips:.0f}")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Benchmarking")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Common Benchmarks:</strong><br>
        • <strong>SPEC CPU:</strong> Standard Performance Evaluation Corporation<br>
        • <strong>Geekbench:</strong> Cross-platform benchmark<br>
        • <strong>Cinebench:</strong> CPU rendering performance<br>
        • <strong>CoreMark:</strong> Embedded processor benchmark<br>
        • <strong>MLPerf:</strong> Machine learning performance
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 10: PRACTICE PROBLEMS ====================
with tabs[9]:
    st.markdown("## 🎯 Practice Problems")
    
    problems = [
        {
            "title": "Problem 1: Cache Performance",
            "question": "A cache has a hit time of 1 cycle and a miss penalty of 100 cycles. If the hit rate is 95%, what is the AMAT?",
            "hint": "AMAT = Hit Time + (Miss Rate × Miss Penalty)",
            "solution": """
Hit Rate = 95% = 0.95
Miss Rate = 1 - 0.95 = 0.05
Hit Time = 1 cycle
Miss Penalty = 100 cycles

AMAT = 1 + (0.05 × 100)
AMAT = 1 + 5
AMAT = 6 cycles
            """
        },
        {
            "title": "Problem 2: Pipeline Speedup",
            "question": "A non-pipelined processor takes 5ns per instruction. A 5-stage pipeline version has 1ns per stage. What is the speedup for 1000 instructions?",
            "hint": "Compare total time for non-pipelined vs pipelined execution",
            "solution": """
Non-pipelined:
Time = 1000 instructions × 5ns = 5000ns

Pipelined (5 stages):
Time = (5 + 999) × 1ns = 1004ns
(5 cycles to fill pipeline, then 1 per instruction)

Speedup = 5000 / 1004 = 4.98×
(Close to ideal 5× speedup)
            """
        },
        {
            "title": "Problem 3: Amdahl's Law",
            "question": "A program has 80% parallelizable code. What is the maximum speedup with infinite processors?",
            "hint": "Use Amdahl's Law with N → ∞",
            "solution": """
P = 0.80 (80% parallelizable)
N → ∞

Speedup = 1 / [(1 - P) + P/N]
As N → ∞, P/N → 0

Speedup = 1 / (1 - 0.80)
Speedup = 1 / 0.20
Speedup = 5×

Maximum speedup is limited by serial portion (20%)
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

# ==================== TAB 11: YOUTUBE RESOURCES ====================
with tabs[10]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="theory-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning Computer Architecture</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {"title": "Computer Architecture", "channel": "CrashCourse Computer Science", "url": "https://www.youtube.com/playlist?list=PL8dPuuaLjXtNlUrcyK6XZ-h8j3c5jC8Fp", "description": "Engaging intro to hardware", "duration": "~5 hours"},
        {"title": "How Computers Work", "channel": "Code.org", "url": "https://www.youtube.com/playlist?list=PLzdnOPI1iJNcsRwJhvksGRngGk19q2r1W", "description": "Bill Gates & others explain", "duration": "~1 hour"},
        {"title": "Digital logic & CPU", "channel": "Ben Eater", "url": "https://www.youtube.com/c/BenEater", "description": "Build a computer from scratch", "duration": "Channel"}
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
        {"title": "Computer Organization", "channel": "Neso Academy", "url": "https://www.youtube.com/playlist?list=PLBlnK6fEyqRgLLlzdgiTUKULKJPYc0A4q", "description": "Detailed academic lectures", "duration": "~20 hours"},
        {"title": "Comp Arch & Org", "channel": "Gate Smashers", "url": "https://www.youtube.com/playlist?list=PLxCzCOWd7aiHMonh3G6QNKq53C6oNXGrX", "description": "Exam-focused tutorials", "duration": "~15 hours"},
        {"title": "Computer Components", "channel": "TechQuickie", "url": "https://www.youtube.com/c/Techquickie", "description": "Hardware explanations", "duration": "Channel"}
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
        {"title": "Computer Architecture (CMU)", "channel": "Onur Mutlu", "url": "https://www.youtube.com/c/OnurMutluLectures", "description": "Carnegie Mellon University", "duration": "~40 hours"},
        {"title": "Advanced Arch", "channel": "MIT OpenCourseWare", "url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP62Wf4TKStR397q2AsuU8W86", "description": "MIT 6.004 Computation", "duration": "~30 hours"},
        {"title": "High Perf Comp", "channel": "Georgia Tech", "url": "https://www.youtube.com/playlist?list=PLAwxTw4SYaPnzO7ItU63yq_SjE2Wv-Jb_", "description": "HPCA lectures", "duration": "~25 hours"}
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
    <div class="architecture-box">
        <strong>Recommended Learning Path:</strong><br>
        1. Watch Crash Course for big picture<br>
        2. Follow Neso Academy for core concepts<br>
        3. Build an 8-bit computer with Ben Eater (Highly recommended!)<br>
        4. Study Patterson & Hennessy textbook<br>
        5. Dive into CMU lectures for advanced topics<br>
        6. Practice assembly programming (MIPS/RISC-V)<br>
        7. Analyze real processor datasheets<br>
        8. Simulate circuits with Logisim<br><br>
        
        <strong>Essential Tools:</strong><br>
        • <strong>Simulation:</strong> Logisim, Gem5, Sniper<br>
        • <strong>Assembly:</strong> MARS (MIPS), Ripes (RISC-V)<br>
        • <strong>Visualization:</strong> CPU visualizers<br>
        • <strong>Books:</strong> Computer Organization and Design
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE103 - Computer Architecture</strong><br>
    <small>UTel University | Department of Computer Engineering</small>
</div>
""", unsafe_allow_html=True)
