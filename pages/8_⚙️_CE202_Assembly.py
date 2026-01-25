import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="CE202 - Assembly Language", page_icon="⚙️", layout="wide")

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
        background: linear-gradient(135deg, #f3e8ff 0%, #e9d5ff 100%);
        border-left: 5px solid #8b5cf6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .instruction-box {
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
    
    .register-box {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-left: 5px solid #3b82f6;
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
    <div style="font-size: 1.2rem; opacity: 0.9;">CE202</div>
    <div class="course-title">Assembly Language</div>
    <div>⚙️ 3 Credits | Semester 3 | Programming</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "3")
with col3:
    st.metric("Difficulty", "5/7")
with col4:
    st.metric("Hours/Week", "6")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "🔧 x86 Architecture",
    "📝 Instructions & Syntax",
    "💾 Registers & Memory",
    "🔄 Control Flow",
    "📊 Data Operations",
    "⚡ Optimization",
    "🛠️ System Programming",
    "🎯 Practice Problems",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive study of low-level programming using x86 assembly language. Covers processor architecture, 
        instruction sets, memory addressing modes, system calls, and optimization techniques. Emphasizes understanding 
        the relationship between high-level code and machine instructions, enabling students to write efficient, 
        hardware-aware programs.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Understand x86 processor architecture and instruction execution",
        "Write assembly programs using NASM/MASM syntax",
        "Master register usage and memory addressing modes",
        "Implement control flow and data manipulation",
        "Optimize code for performance",
        "Interface with operating system through system calls",
        "Debug assembly code using GDB/debuggers",
        "Understand compiler-generated assembly"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Fundamentals:**
        - x86/x64 architecture overview
        - Registers and flags
        - Memory segmentation
        - Instruction formats
        - Addressing modes
        
        **Programming:**
        - Data movement instructions
        - Arithmetic and logic operations
        - Control flow (jumps, loops)
        - Procedures and stack
        - String operations
        """)
    
    with col2:
        st.markdown("""
        **Advanced Topics:**
        - SIMD instructions (SSE, AVX)
        - Inline assembly in C/C++
        - Performance optimization
        - System calls and interrupts
        - Reverse engineering basics
        
        **Tools:**
        - NASM/MASM assemblers
        - GDB debugger
        - Disassemblers (objdump, IDA)
        - Performance profilers
        - Compiler explorers
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Assembly Language for x86 Processors", "author": "Kip Irvine", "type": "Textbook"},
        {"title": "Programming from the Ground Up", "author": "Jonathan Bartlett", "type": "Free Book"},
        {"title": "x86 Assembly Guide", "author": "University of Virginia", "type": "Online"},
        {"title": "Intel 64 and IA-32 Architectures Manual", "author": "Intel", "type": "Reference"}
    ]
    
    for resource in resources:
        st.markdown(f"📖 **{resource['title']}** by {resource['author']} ({resource['type']})")

# ==================== TAB 2: x86 ARCHITECTURE ====================
with tabs[1]:
    st.markdown("## 🔧 x86 Architecture")
    
    st.markdown("### 1️⃣ Processor Overview")
    
    st.markdown("""
    <div class="theory-box">
        <strong>x86 Architecture:</strong><br>
        • <strong>CISC Design:</strong> Complex Instruction Set Computer<br>
        • <strong>Backward Compatible:</strong> 8086 → 80286 → 80386 → x64<br>
        • <strong>Variable Length Instructions:</strong> 1-15 bytes<br>
        • <strong>Little Endian:</strong> Least significant byte first<br><br>
        
        <strong>Execution Modes:</strong><br>
        • <strong>Real Mode:</strong> 16-bit, 1MB addressable (8086 compatible)<br>
        • <strong>Protected Mode:</strong> 32-bit, 4GB addressable, memory protection<br>
        • <strong>Long Mode (x64):</strong> 64-bit, virtual memory, extended registers
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ CPU Components")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Execution Units:**
        - **ALU:** Arithmetic Logic Unit
        - **FPU:** Floating Point Unit
        - **Control Unit:** Instruction decode
        - **Cache:** L1, L2, L3 hierarchy
        """)
    
    with col2:
        st.markdown("""
        **Support Components:**
        - **MMU:** Memory Management Unit
        - **TLB:** Translation Lookaside Buffer
        - **Branch Predictor:** Control flow optimization
        - **Prefetcher:** Instruction/data prefetch
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Instruction Pipeline")
    
    st.markdown("""
    <div class="instruction-box">
        <strong>5-Stage Pipeline (Classic):</strong><br>
        1. <strong>Fetch:</strong> Read instruction from memory<br>
        2. <strong>Decode:</strong> Interpret instruction opcode<br>
        3. <strong>Execute:</strong> Perform operation in ALU<br>
        4. <strong>Memory:</strong> Access data memory if needed<br>
        5. <strong>Write-back:</strong> Store result to register<br><br>
        
        <strong>Modern Processors:</strong> 14-20+ stage pipelines with superscalar execution
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: INSTRUCTIONS ====================
with tabs[2]:
    st.markdown("## 📝 Instructions & Syntax")
    
    st.markdown("### 1️⃣ Assembly Syntax")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Intel Syntax (NASM/MASM):**")
        st.code("""
; Intel syntax
mov eax, 5          ; dest, src
add eax, ebx
mov [address], eax  ; memory write
        """, language="nasm")
    
    with col2:
        st.markdown("**AT&T Syntax (GAS):**")
        st.code("""
# AT&T syntax
movl $5, %eax       # src, dest
addl %ebx, %eax
movl %eax, address  # memory write
        """, language="gas")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Instruction Categories")
    
    st.markdown("""
    <div class="instruction-box">
        <strong>Data Movement:</strong><br>
        • <strong>MOV:</strong> Move data between registers/memory<br>
        • <strong>PUSH/POP:</strong> Stack operations<br>
        • <strong>LEA:</strong> Load Effective Address<br>
        • <strong>XCHG:</strong> Exchange values<br><br>
        
        <strong>Arithmetic:</strong><br>
        • <strong>ADD/SUB:</strong> Addition/Subtraction<br>
        • <strong>MUL/DIV:</strong> Multiplication/Division<br>
        • <strong>INC/DEC:</strong> Increment/Decrement<br>
        • <strong>NEG:</strong> Two's complement negation<br><br>
        
        <strong>Logical:</strong><br>
        • <strong>AND/OR/XOR:</strong> Bitwise operations<br>
        • <strong>NOT:</strong> Bitwise complement<br>
        • <strong>SHL/SHR:</strong> Shift left/right<br>
        • <strong>ROL/ROR:</strong> Rotate left/right
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Example Program")
    
    st.markdown("**Simple Addition (NASM):**")
    st.code("""
section .data
    num1 dd 10          ; Define doubleword (32-bit)
    num2 dd 20
    result dd 0

section .text
    global _start

_start:
    mov eax, [num1]     ; Load num1 into EAX
    add eax, [num2]     ; Add num2 to EAX
    mov [result], eax   ; Store result
    
    ; Exit program (Linux syscall)
    mov eax, 1          ; sys_exit
    xor ebx, ebx        ; return 0
    int 0x80            ; syscall
    """, language="nasm")

# ==================== TAB 4: REGISTERS & MEMORY ====================
with tabs[3]:
    st.markdown("## 💾 Registers & Memory")
    
    st.markdown("### 1️⃣ General Purpose Registers")
    
    st.markdown("""
    <div class="register-box">
        <strong>32-bit Registers (x86):</strong><br>
        • <strong>EAX:</strong> Accumulator (arithmetic operations)<br>
        • <strong>EBX:</strong> Base (memory addressing)<br>
        • <strong>ECX:</strong> Counter (loop operations)<br>
        • <strong>EDX:</strong> Data (I/O operations, multiplication)<br>
        • <strong>ESI:</strong> Source Index (string operations)<br>
        • <strong>EDI:</strong> Destination Index (string operations)<br>
        • <strong>EBP:</strong> Base Pointer (stack frame)<br>
        • <strong>ESP:</strong> Stack Pointer (top of stack)<br><br>
        
        <strong>64-bit Extensions (x64):</strong><br>
        RAX, RBX, RCX, RDX, RSI, RDI, RBP, RSP + R8-R15
    </div>
    """, unsafe_allow_html=True)
    
    # Register size visualization
    st.markdown("#### Register Size Hierarchy")
    
    register_data = pd.DataFrame({
        'Register': ['RAX (64-bit)', 'EAX (32-bit)', 'AX (16-bit)', 'AH (8-bit high)', 'AL (8-bit low)'],
        'Bits': [64, 32, 16, 8, 8],
        'Type': ['64-bit', '32-bit', '16-bit', '8-bit', '8-bit']
    })
    
    chart = alt.Chart(register_data).mark_bar().encode(
        x=alt.X('Bits:Q', title='Size (bits)'),
        y=alt.Y('Register:N', sort='-x', title='Register Name'),
        color=alt.Color('Type:N', scale=alt.Scale(scheme='category10')),
        tooltip=['Register', 'Bits', 'Type']
    ).properties(
        width=600,
        height=300,
        title="x86 Register Size Hierarchy (RAX example)"
    )
    
    st.altair_chart(chart, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Special Registers")
    
    st.markdown("""
    <div class="register-box">
        <strong>Instruction Pointer:</strong><br>
        • <strong>EIP/RIP:</strong> Points to next instruction to execute<br><br>
        
        <strong>Flags Register (EFLAGS/RFLAGS):</strong><br>
        • <strong>CF:</strong> Carry Flag (unsigned overflow)<br>
        • <strong>ZF:</strong> Zero Flag (result is zero)<br>
        • <strong>SF:</strong> Sign Flag (result is negative)<br>
        • <strong>OF:</strong> Overflow Flag (signed overflow)<br>
        • <strong>PF:</strong> Parity Flag (even parity)<br>
        • <strong>DF:</strong> Direction Flag (string operations)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Memory Addressing Modes")
    
    st.markdown("""
    <div class="instruction-box">
        <strong>Addressing Modes:</strong><br><br>
        
        1. <strong>Immediate:</strong> mov eax, 5 (constant value)<br>
        2. <strong>Register:</strong> mov eax, ebx (register to register)<br>
        3. <strong>Direct:</strong> mov eax, [0x1234] (absolute address)<br>
        4. <strong>Indirect:</strong> mov eax, [ebx] (address in register)<br>
        5. <strong>Base + Displacement:</strong> mov eax, [ebx + 8]<br>
        6. <strong>Indexed:</strong> mov eax, [ebx + ecx*4]<br>
        7. <strong>Base + Index + Disp:</strong> mov eax, [ebx + ecx*4 + 8]
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
; Array access example
mov ebx, array_base     ; Base address
mov ecx, 3              ; Index
mov eax, [ebx + ecx*4]  ; Load array[3] (4 bytes per element)
    """, language="nasm")

# ==================== TAB 5: CONTROL FLOW ====================
with tabs[4]:
    st.markdown("## 🔄 Control Flow")
    
    st.markdown("### 1️⃣ Conditional Jumps")
    
    st.markdown("""
    <div class="instruction-box">
        <strong>Comparison:</strong><br>
        • <strong>CMP:</strong> Compare (subtract without storing)<br>
        • <strong>TEST:</strong> Bitwise AND (without storing)<br><br>
        
        <strong>Unsigned Jumps:</strong><br>
        • <strong>JE/JZ:</strong> Jump if Equal/Zero<br>
        • <strong>JNE/JNZ:</strong> Jump if Not Equal/Not Zero<br>
        • <strong>JA:</strong> Jump if Above (>)<br>
        • <strong>JAE:</strong> Jump if Above or Equal (>=)<br>
        • <strong>JB:</strong> Jump if Below (<)<br>
        • <strong>JBE:</strong> Jump if Below or Equal (<=)<br><br>
        
        <strong>Signed Jumps:</strong><br>
        • <strong>JG:</strong> Jump if Greater (>)<br>
        • <strong>JGE:</strong> Jump if Greater or Equal (>=)<br>
        • <strong>JL:</strong> Jump if Less (<)<br>
        • <strong>JLE:</strong> Jump if Less or Equal (<=)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Loops")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**While Loop:**")
        st.code("""
mov ecx, 10         ; Counter
while_loop:
    ; Loop body
    dec ecx         ; Decrement
    jnz while_loop  ; Jump if not zero
        """, language="nasm")
    
    with col2:
        st.markdown("**For Loop:**")
        st.code("""
mov ecx, 10         ; Counter
for_loop:
    ; Loop body
    loop for_loop   ; Dec ECX, jump if != 0
        """, language="nasm")
    
    st.markdown("---")
    st.markdown("### 3️⃣ Procedures (Functions)")
    
    st.markdown("""
    <div class="example-box">
        <strong>Function Call Convention (cdecl):</strong><br>
        1. Push arguments right-to-left<br>
        2. CALL instruction (pushes return address)<br>
        3. Function prologue (save EBP, set up stack frame)<br>
        4. Function body<br>
        5. Function epilogue (restore EBP)<br>
        6. RET instruction (pop return address)<br>
        7. Caller cleans up stack
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
; Function definition
my_function:
    push ebp            ; Save old base pointer
    mov ebp, esp        ; Set up new stack frame
    sub esp, 16         ; Allocate local variables
    
    ; Function body
    mov eax, [ebp+8]    ; Access first parameter
    add eax, [ebp+12]   ; Access second parameter
    
    mov esp, ebp        ; Restore stack
    pop ebp             ; Restore base pointer
    ret                 ; Return

; Function call
push 20                 ; Second argument
push 10                 ; First argument
call my_function
add esp, 8              ; Clean up stack (2 * 4 bytes)
    """, language="nasm")

# ==================== TAB 6: DATA OPERATIONS ====================
with tabs[5]:
    st.markdown("## 📊 Data Operations")
    
    st.markdown("### 1️⃣ Arithmetic Operations")
    
    # Interactive arithmetic calculator
    st.markdown("#### 🧮 Assembly Arithmetic Simulator")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        num1 = st.number_input("EAX (operand 1)", -1000, 1000, 10, 1)
    with col2:
        operation = st.selectbox("Operation", ["ADD", "SUB", "MUL", "AND", "OR", "XOR"])
    with col3:
        num2 = st.number_input("EBX (operand 2)", -1000, 1000, 5, 1)
    
    if operation == "ADD":
        result = num1 + num2
        asm_code = f"add eax, ebx  ; {num1} + {num2} = {result}"
    elif operation == "SUB":
        result = num1 - num2
        asm_code = f"sub eax, ebx  ; {num1} - {num2} = {result}"
    elif operation == "MUL":
        result = num1 * num2
        asm_code = f"imul eax, ebx ; {num1} * {num2} = {result}"
    elif operation == "AND":
        result = num1 & num2
        asm_code = f"and eax, ebx  ; {num1} & {num2} = {result} (0x{result:X})"
    elif operation == "OR":
        result = num1 | num2
        asm_code = f"or eax, ebx   ; {num1} | {num2} = {result} (0x{result:X})"
    else:  # XOR
        result = num1 ^ num2
        asm_code = f"xor eax, ebx  ; {num1} ^ {num2} = {result} (0x{result:X})"
    
    st.code(asm_code, language="nasm")
    st.success(f"**Result:** EAX = {result}")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Bit Manipulation")
    
    st.markdown("""
    <div class="instruction-box">
        <strong>Shift Operations:</strong><br>
        • <strong>SHL:</strong> Shift Left (multiply by 2ⁿ)<br>
        • <strong>SHR:</strong> Shift Right (unsigned divide by 2ⁿ)<br>
        • <strong>SAR:</strong> Shift Arithmetic Right (signed divide)<br><br>
        
        <strong>Rotate Operations:</strong><br>
        • <strong>ROL:</strong> Rotate Left<br>
        • <strong>ROR:</strong> Rotate Right<br>
        • <strong>RCL/RCR:</strong> Rotate through Carry
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
mov eax, 8
shl eax, 2      ; 8 << 2 = 32 (multiply by 4)
shr eax, 1      ; 32 >> 1 = 16 (divide by 2)
    """, language="nasm")

# ==================== TAB 7: OPTIMIZATION ====================
with tabs[6]:
    st.markdown("## ⚡ Optimization Techniques")
    
    st.markdown("### 1️⃣ Performance Tips")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Register Usage:</strong><br>
        • Keep frequently used variables in registers<br>
        • Minimize memory access (cache misses expensive)<br>
        • Use register renaming-friendly code<br><br>
        
        <strong>Instruction Selection:</strong><br>
        • Use LEA for arithmetic: lea eax, [ebx + ecx*4 + 8]<br>
        • XOR for zeroing: xor eax, eax (faster than mov eax, 0)<br>
        • TEST instead of CMP when checking zero<br>
        • Prefer INC/DEC over ADD/SUB 1 (smaller encoding)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Loop Optimization")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Unoptimized:**")
        st.code("""
mov ecx, 100
loop_start:
    mov eax, [array + ecx*4]
    add eax, 1
    mov [array + ecx*4], eax
    dec ecx
    jnz loop_start
        """, language="nasm")
    
    with col2:
        st.markdown("**Optimized (Loop Unrolling):**")
        st.code("""
mov ecx, 25  ; 100/4
loop_start:
    add dword [array + ecx*16], 1
    add dword [array + ecx*16+4], 1
    add dword [array + ecx*16+8], 1
    add dword [array + ecx*16+12], 1
    dec ecx
    jnz loop_start
        """, language="nasm")
    
    st.markdown("---")
    st.markdown("### 3️⃣ SIMD Instructions")
    
    st.markdown("""
    <div class="instruction-box">
        <strong>SSE/AVX (Single Instruction Multiple Data):</strong><br>
        • Process multiple data elements in parallel<br>
        • 128-bit (SSE) or 256-bit (AVX) registers<br>
        • Ideal for vector/matrix operations<br><br>
        
        <strong>Example - Add 4 floats at once:</strong>
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
; SSE: Add 4 floats in parallel
movaps xmm0, [array1]    ; Load 4 floats
movaps xmm1, [array2]    ; Load 4 floats
addps xmm0, xmm1         ; Add all 4 pairs
movaps [result], xmm0    ; Store 4 results
    """, language="nasm")

# ==================== TAB 8: SYSTEM PROGRAMMING ====================
with tabs[7]:
    st.markdown("## 🛠️ System Programming")
    
    st.markdown("### 1️⃣ System Calls (Linux)")
    
    st.markdown("""
    <div class="theory-box">
        <strong>System Call Convention (x86 Linux):</strong><br>
        • <strong>EAX:</strong> System call number<br>
        • <strong>EBX, ECX, EDX, ESI, EDI, EBP:</strong> Arguments (in order)<br>
        • <strong>INT 0x80:</strong> Trigger system call<br>
        • <strong>EAX:</strong> Return value<br><br>
        
        <strong>Common System Calls:</strong><br>
        • sys_exit (1), sys_read (3), sys_write (4)<br>
        • sys_open (5), sys_close (6)<br>
        • sys_fork (2), sys_execve (11)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**Hello World Example:**")
    st.code("""
section .data
    msg db 'Hello, World!', 0xA  ; Message with newline
    len equ $ - msg               ; Calculate length

section .text
    global _start

_start:
    ; sys_write(stdout, msg, len)
    mov eax, 4          ; sys_write
    mov ebx, 1          ; stdout
    mov ecx, msg        ; message address
    mov edx, len        ; message length
    int 0x80            ; syscall
    
    ; sys_exit(0)
    mov eax, 1          ; sys_exit
    xor ebx, ebx        ; return 0
    int 0x80            ; syscall
    """, language="nasm")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Inline Assembly (C/C++)")
    
    st.markdown("""
    <div class="example-box">
        <strong>GCC Inline Assembly:</strong><br>
        Embed assembly code directly in C/C++ programs for performance-critical sections
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
#include <stdio.h>

int main() {
    int a = 10, b = 20, result;
    
    // Inline assembly
    __asm__ (
        "movl %1, %%eax\\n"
        "addl %2, %%eax\\n"
        "movl %%eax, %0\\n"
        : "=r" (result)           // Output
        : "r" (a), "r" (b)        // Inputs
        : "%eax"                  // Clobbered registers
    );
    
    printf("Result: %d\\n", result);
    return 0;
}
    """, language="c")

# ==================== TAB 9: PRACTICE PROBLEMS ====================
with tabs[8]:
    st.markdown("## 🎯 Practice Problems")
    
    problems = [
        {
            "title": "Problem 1: Sum Array",
            "question": "Write assembly code to sum all elements in an array of 10 integers",
            "hint": "Use a loop with ECX as counter, accumulate in EAX",
            "solution": """
section .data
    array dd 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    len equ 10

section .text
    global _start

_start:
    xor eax, eax        ; Clear sum
    mov ecx, len        ; Counter
    mov ebx, 0          ; Index

sum_loop:
    add eax, [array + ebx*4]  ; Add element
    inc ebx             ; Next index
    loop sum_loop       ; Dec ECX, jump if != 0
    
    ; EAX now contains sum (55)
    ; Exit
    mov ebx, eax
    mov eax, 1
    int 0x80
            """
        },
        {
            "title": "Problem 2: Factorial",
            "question": "Implement factorial(n) using recursion or iteration",
            "hint": "Use MUL instruction, be careful with register preservation",
            "solution": """
; Iterative factorial
factorial:
    push ebp
    mov ebp, esp
    
    mov ecx, [ebp+8]    ; Get n
    mov eax, 1          ; Result = 1
    
fact_loop:
    cmp ecx, 1
    jle fact_done
    imul eax, ecx       ; result *= n
    dec ecx
    jmp fact_loop
    
fact_done:
    pop ebp
    ret
            """
        },
        {
            "title": "Problem 3: String Length",
            "question": "Calculate the length of a null-terminated string",
            "hint": "Use SCASB instruction or manual loop",
            "solution": """
strlen:
    push ebp
    mov ebp, esp
    
    mov edi, [ebp+8]    ; String address
    xor eax, eax        ; Search for null (0)
    mov ecx, -1         ; Max count
    cld                 ; Clear direction flag
    repne scasb         ; Scan until AL found
    
    not ecx             ; Invert count
    dec ecx             ; Adjust for null
    mov eax, ecx        ; Return length
    
    pop ebp
    ret
            """
        }
    ]
    
    for idx, problem in enumerate(problems, 1):
        with st.expander(f"📝 {problem['title']}", expanded=False):
            st.markdown(f"**Question:** {problem['question']}")
            
            if st.button(f"Show Hint", key=f"hint_{idx}"):
                st.info(f"💡 {problem['hint']}")
            
            if st.button(f"Show Solution", key=f"sol_{idx}"):
                st.code(problem['solution'], language="nasm")

# ==================== TAB 10: YOUTUBE RESOURCES ====================
with tabs[9]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning x86 Assembly Language</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {
            "title": "Assembly Language Programming Tutorial",
            "channel": "Derek Banas",
            "url": "https://www.youtube.com/watch?v=ViNnfoE56V8",
            "description": "Complete beginner tutorial covering x86 assembly basics",
            "duration": "~1 hour"
        },
        {
            "title": "x86 Assembly Crash Course",
            "channel": "Creel",
            "url": "https://www.youtube.com/watch?v=75gBFiFtAb8",
            "description": "Quick introduction to assembly language fundamentals",
            "duration": "30 min"
        },
        {
            "title": "Assembly Language Tutorial",
            "channel": "ProgrammingKnowledge",
            "url": "https://www.youtube.com/playlist?list=PL2EF13wm-hWCoj6tUBGUmrkJmH1972dBB",
            "description": "Complete playlist from basics to advanced topics",
            "duration": "Playlist"
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
            "title": "x86 Assembly Language Programming",
            "channel": "Davy Wybiral",
            "url": "https://www.youtube.com/playlist?list=PLmxT2pVYo5LB5EzTPZGfFN0c2GDiSXgQe",
            "description": "In-depth coverage of x86 architecture and programming",
            "duration": "Playlist"
        },
        {
            "title": "Assembly Programming Tutorial",
            "channel": "Tutorialspoint",
            "url": "https://www.youtube.com/watch?v=wLXIWKUWpSs",
            "description": "Comprehensive tutorial with practical examples",
            "duration": "~3 hours"
        },
        {
            "title": "NASM Assembly Tutorial",
            "channel": "Kupala",
            "url": "https://www.youtube.com/playlist?list=PLetF-YjXm-sCH6FrTz4AQhfH6INDQvQSn",
            "description": "NASM-specific tutorials with Linux focus",
            "duration": "Playlist"
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
            "title": "Reverse Engineering with Ghidra",
            "channel": "stacksmashing",
            "url": "https://www.youtube.com/playlist?list=PLrIMxe8xtVPqwMJPZRGPqPpVlhJWNuDHR",
            "description": "Advanced reverse engineering and assembly analysis",
            "duration": "Playlist"
        },
        {
            "title": "x86 Exploitation",
            "channel": "LiveOverflow",
            "url": "https://www.youtube.com/playlist?list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN",
            "description": "Binary exploitation and security-focused assembly",
            "duration": "Playlist"
        },
        {
            "title": "Computer Architecture",
            "channel": "Onur Mutlu Lectures",
            "url": "https://www.youtube.com/playlist?list=PL5PHm2jkkXmi5CxxI7b3JCL1TWybTDtKq",
            "description": "Deep dive into processor architecture and optimization",
            "duration": "Full Course"
        }
    ]
    
    for resource in advanced_resources:
        st.markdown(f"""
        **[{resource['title']}]({resource['url']})**  
        📺 Channel: {resource['channel']} | ⏱️ {resource['duration']}  
        {resource['description']}
        """)
        st.markdown("---")
    
    # Tools & Debugging
    st.markdown("### 🛠️ Tools & Debugging")
    
    tools_resources = [
        {
            "title": "GDB Tutorial",
            "channel": "Chris Kanich",
            "url": "https://www.youtube.com/watch?v=PorfLSr3DDI",
            "description": "Learn to debug assembly with GDB",
            "duration": "~1 hour"
        },
        {
            "title": "IDA Pro Tutorial",
            "channel": "OALabs",
            "url": "https://www.youtube.com/playlist?list=PLtPrYlwXDImiO_hzK7npBi4eKQQBgygLD",
            "description": "Professional disassembler and debugger tutorial",
            "duration": "Playlist"
        },
        {
            "title": "Compiler Explorer",
            "channel": "Matt Godbolt",
            "url": "https://www.youtube.com/watch?v=kIoZDUd5DKw",
            "description": "See how C/C++ compiles to assembly in real-time",
            "duration": "30 min"
        }
    ]
    
    for resource in tools_resources:
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
        1. Start with beginner tutorials to understand basics<br>
        2. Practice writing simple programs (loops, functions)<br>
        3. Learn to use debuggers (GDB) to step through code<br>
        4. Study compiler output (use Compiler Explorer)<br>
        5. Move to intermediate topics (optimization, SIMD)<br>
        6. Explore advanced topics (reverse engineering, exploitation)<br><br>
        
        <strong>Practice Resources:</strong><br>
        • <strong>Compiler Explorer:</strong> https://godbolt.org<br>
        • <strong>Online Assembler:</strong> https://www.tutorialspoint.com/compile_assembly_online.php<br>
        • <strong>x86 Reference:</strong> https://www.felixcloutier.com/x86/<br>
        • <strong>Intel Manuals:</strong> https://software.intel.com/content/www/us/en/develop/articles/intel-sdm.html
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE202 - Assembly Language</strong><br>
    <small>UTel University | Department of Computer Engineering</small>
</div>
""", unsafe_allow_html=True)
