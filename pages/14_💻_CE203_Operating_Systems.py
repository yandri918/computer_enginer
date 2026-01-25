import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="CE203 - Operating Systems", page_icon="💻", layout="wide")

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
        background: linear-gradient(135deg, #eef2ff 0%, #e0e7ff 100%);
        border-left: 5px solid #6366f1;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .concept-box {
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
    
    .algorithm-box {
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
    <div style="font-size: 1.2rem; opacity: 0.9;">CE203</div>
    <div class="course-title">Operating Systems</div>
    <div>💻 4 Credits | Semester 3 | Systems</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "4")
with col2:
    st.metric("Semester", "3")
with col3:
    st.metric("Difficulty", "5/7")
with col4:
    st.metric("Hours/Week", "8")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "⚙️ Processes & Threads",
    "🔄 Synchronization",
    "📅 CPU Scheduling",
    "💾 Memory Management",
    "📁 File Systems",
    "🔒 Security & Protection",
    "🌐 Modern OS Concepts",
    "🎯 Practice Problems",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive study of operating system principles, design, and implementation. Covers process management, 
        memory management, file systems, I/O systems, and security. Emphasizes both theoretical concepts and practical 
        implementation through projects in C/C++. Students will understand how modern operating systems like Linux, 
        Windows, and macOS work under the hood.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Understand OS architecture and components",
        "Implement process and thread management",
        "Solve synchronization problems (deadlock, race conditions)",
        "Design CPU scheduling algorithms",
        "Manage memory using paging and segmentation",
        "Implement file system operations",
        "Apply security and protection mechanisms",
        "Understand modern OS features (virtualization, containers)"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Fundamentals:**
        - OS structure and services
        - System calls and APIs
        - Processes and threads
        - Inter-process communication (IPC)
        - CPU scheduling algorithms
        
        **Memory Management:**
        - Memory hierarchy
        - Paging and segmentation
        - Virtual memory
        - Page replacement algorithms
        - Memory allocation strategies
        """)
    
    with col2:
        st.markdown("""
        **Advanced Topics:**
        - File systems (ext4, NTFS, FAT)
        - I/O systems and device drivers
        - Deadlock prevention and recovery
        - Security and protection
        - Distributed systems
        
        **Modern Concepts:**
        - Virtualization (hypervisors)
        - Containers (Docker, Kubernetes)
        - Real-time operating systems
        - Mobile OS (Android, iOS)
        - Cloud operating systems
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Operating System Concepts", "author": "Silberschatz, Galvin & Gagne", "type": "Textbook"},
        {"title": "Modern Operating Systems", "author": "Andrew Tanenbaum", "type": "Textbook"},
        {"title": "Operating Systems: Three Easy Pieces", "author": "Arpaci-Dusseau", "type": "Free Book"},
        {"title": "Linux Kernel Development", "author": "Robert Love", "type": "Advanced"}
    ]
    
    for resource in resources:
        st.markdown(f"📖 **{resource['title']}** by {resource['author']} ({resource['type']})")

# ==================== TAB 2: PROCESSES & THREADS ====================
with tabs[1]:
    st.markdown("## ⚙️ Processes & Threads")
    
    st.markdown("### 1️⃣ Process Concept")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Process:</strong> Program in execution<br><br>
        
        <strong>Process States:</strong><br>
        • <strong>New:</strong> Process is being created<br>
        • <strong>Ready:</strong> Waiting to be assigned to CPU<br>
        • <strong>Running:</strong> Instructions are being executed<br>
        • <strong>Waiting:</strong> Waiting for I/O or event<br>
        • <strong>Terminated:</strong> Process has finished execution<br><br>
        
        <strong>Process Control Block (PCB):</strong><br>
        • Process ID (PID)<br>
        • Program counter<br>
        • CPU registers<br>
        • Memory management info<br>
        • I/O status<br>
        • Accounting information
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Process vs Thread")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Process:**
        - Independent execution unit
        - Own memory space
        - Heavy-weight
        - Expensive context switch
        - IPC required for communication
        - Example: Multiple browser instances
        """)
    
    with col2:
        st.markdown("""
        **Thread:**
        - Lightweight process
        - Shared memory space
        - Light-weight
        - Fast context switch
        - Direct communication
        - Example: Browser tabs
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Thread Models")
    
    st.markdown("""
    <div class="concept-box">
        <strong>User-Level Threads (ULT):</strong><br>
        • Managed by user-level library<br>
        • Fast context switching<br>
        • OS unaware of threads<br>
        • Blocking system call blocks all threads<br><br>
        
        <strong>Kernel-Level Threads (KLT):</strong><br>
        • Managed by OS kernel<br>
        • Slower context switching<br>
        • True parallelism on multicore<br>
        • Blocking call doesn't block process<br><br>
        
        <strong>Hybrid Model (Many-to-Many):</strong><br>
        • Multiplexes many ULT onto smaller KLT<br>
        • Best of both worlds
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**Example: Creating Threads in C (POSIX)**")
    st.code("""
#include <pthread.h>
#include <stdio.h>

void* thread_function(void* arg) {
    int thread_id = *(int*)arg;
    printf("Thread %d is running\\n", thread_id);
    return NULL;
}

int main() {
    pthread_t threads[5];
    int thread_ids[5];
    
    // Create 5 threads
    for (int i = 0; i < 5; i++) {
        thread_ids[i] = i;
        pthread_create(&threads[i], NULL, thread_function, &thread_ids[i]);
    }
    
    // Wait for all threads to complete
    for (int i = 0; i < 5; i++) {
        pthread_join(threads[i], NULL);
    }
    
    return 0;
}
    """, language="c")

# ==================== TAB 3: SYNCHRONIZATION ====================
with tabs[2]:
    st.markdown("## 🔄 Synchronization")
    
    st.markdown("### 1️⃣ Critical Section Problem")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Critical Section:</strong> Code segment where shared resources are accessed<br><br>
        
        <strong>Requirements:</strong><br>
        1. <strong>Mutual Exclusion:</strong> Only one process in critical section<br>
        2. <strong>Progress:</strong> Selection of next process cannot be postponed indefinitely<br>
        3. <strong>Bounded Waiting:</strong> Limit on waiting time<br><br>
        
        <strong>Race Condition:</strong> Outcome depends on timing of events
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Synchronization Mechanisms")
    
    st.markdown("""
    <div class="concept-box">
        <strong>1. Mutex (Mutual Exclusion):</strong><br>
        • Binary lock (locked/unlocked)<br>
        • Only lock holder can unlock<br>
        • Used for protecting critical sections<br><br>
        
        <strong>2. Semaphore:</strong><br>
        • Integer variable<br>
        • wait() (P) and signal() (V) operations<br>
        • Binary semaphore (0 or 1) = mutex<br>
        • Counting semaphore (n resources)<br><br>
        
        <strong>3. Monitor:</strong><br>
        • High-level synchronization construct<br>
        • Encapsulates shared data and procedures<br>
        • Condition variables for waiting<br><br>
        
        <strong>4. Spinlock:</strong><br>
        • Busy waiting (spin in loop)<br>
        • Good for short critical sections<br>
        • Wastes CPU cycles
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**Semaphore Example:**")
    st.code("""
// Semaphore operations
wait(S) {
    while (S <= 0)
        ; // busy wait
    S--;
}

signal(S) {
    S++;
}

// Producer-Consumer with semaphore
semaphore mutex = 1;      // Mutual exclusion
semaphore empty = N;      // Empty slots
semaphore full = 0;       // Full slots

Producer() {
    while (true) {
        // Produce item
        wait(empty);      // Wait for empty slot
        wait(mutex);      // Enter critical section
        // Add item to buffer
        signal(mutex);    // Exit critical section
        signal(full);     // Signal full slot
    }
}

Consumer() {
    while (true) {
        wait(full);       // Wait for full slot
        wait(mutex);      // Enter critical section
        // Remove item from buffer
        signal(mutex);    // Exit critical section
        signal(empty);    // Signal empty slot
        // Consume item
    }
}
    """, language="c")
    
    st.markdown("---")
    st.markdown("### 3️⃣ Classic Synchronization Problems")
    
    st.markdown("""
    <div class="example-box">
        <strong>1. Producer-Consumer Problem:</strong><br>
        • Bounded buffer between producer and consumer<br>
        • Synchronize access to buffer<br><br>
        
        <strong>2. Readers-Writers Problem:</strong><br>
        • Multiple readers can read simultaneously<br>
        • Writers need exclusive access<br>
        • Variants: readers preference, writers preference<br><br>
        
        <strong>3. Dining Philosophers Problem:</strong><br>
        • 5 philosophers, 5 chopsticks<br>
        • Need 2 chopsticks to eat<br>
        • Avoid deadlock and starvation<br><br>
        
        <strong>4. Sleeping Barber Problem:</strong><br>
        • Barber shop with waiting room<br>
        • Synchronize barber and customers
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: CPU SCHEDULING ====================
with tabs[3]:
    st.markdown("## 📅 CPU Scheduling")
    
    st.markdown("### 1️⃣ Scheduling Criteria")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Performance Metrics:</strong><br><br>
        
        • <strong>CPU Utilization:</strong> Keep CPU busy (40-90%)<br>
        • <strong>Throughput:</strong> Processes completed per time unit<br>
        • <strong>Turnaround Time:</strong> Time from submission to completion<br>
        • <strong>Waiting Time:</strong> Time spent in ready queue<br>
        • <strong>Response Time:</strong> Time from submission to first response<br><br>
        
        <strong>Goals:</strong><br>
        • Maximize: CPU utilization, throughput<br>
        • Minimize: Turnaround time, waiting time, response time
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Scheduling Algorithms")
    
    st.markdown("""
    <div class="algorithm-box">
        <strong>1. First-Come, First-Served (FCFS):</strong><br>
        • Non-preemptive<br>
        • Simple queue (FIFO)<br>
        • Convoy effect (short processes wait for long)<br><br>
        
        <strong>2. Shortest Job First (SJF):</strong><br>
        • Optimal average waiting time<br>
        • Can be preemptive (SRTF) or non-preemptive<br>
        • Difficulty: predicting burst time<br>
        • Starvation possible<br><br>
        
        <strong>3. Priority Scheduling:</strong><br>
        • Each process has priority<br>
        • Highest priority runs first<br>
        • Problem: Starvation (solution: aging)<br><br>
        
        <strong>4. Round Robin (RR):</strong><br>
        • Preemptive FCFS with time quantum<br>
        • Fair, good response time<br>
        • Performance depends on quantum size<br><br>
        
        <strong>5. Multilevel Queue:</strong><br>
        • Multiple queues with different priorities<br>
        • Each queue has own scheduling algorithm<br><br>
        
        <strong>6. Multilevel Feedback Queue:</strong><br>
        • Processes can move between queues<br>
        • Aging to prevent starvation<br>
        • Most general, most complex
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive Scheduling Simulator
    st.markdown("#### 🧮 Round Robin Scheduling Simulator")
    
    st.markdown("Enter process burst times (comma-separated):")
    burst_input = st.text_input("Burst times (ms)", "10, 5, 8, 12, 6")
    time_quantum = st.slider("Time Quantum (ms)", 1, 10, 4)
    
    try:
        burst_times = [int(x.strip()) for x in burst_input.split(',')]
        n = len(burst_times)
        
        # Simulate Round Robin
        remaining = burst_times.copy()
        waiting_time = [0] * n
        turnaround_time = [0] * n
        current_time = 0
        
        while any(r > 0 for r in remaining):
            for i in range(n):
                if remaining[i] > 0:
                    if remaining[i] > time_quantum:
                        current_time += time_quantum
                        remaining[i] -= time_quantum
                    else:
                        current_time += remaining[i]
                        waiting_time[i] = current_time - burst_times[i]
                        turnaround_time[i] = current_time
                        remaining[i] = 0
        
        avg_waiting = sum(waiting_time) / n
        avg_turnaround = sum(turnaround_time) / n
        
        # Display results
        df_results = pd.DataFrame({
            'Process': [f'P{i+1}' for i in range(n)],
            'Burst Time': burst_times,
            'Waiting Time': waiting_time,
            'Turnaround Time': turnaround_time
        })
        
        st.dataframe(df_results, use_container_width=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Average Waiting Time", f"{avg_waiting:.2f} ms")
        with col2:
            st.metric("Average Turnaround Time", f"{avg_turnaround:.2f} ms")
        
    except:
        st.error("Please enter valid burst times separated by commas")

# ==================== TAB 5: MEMORY MANAGEMENT ====================
with tabs[4]:
    st.markdown("## 💾 Memory Management")
    
    st.markdown("### 1️⃣ Memory Hierarchy")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Memory Hierarchy (Fast → Slow):</strong><br><br>
        
        1. <strong>Registers:</strong> < 1 ns, few KB<br>
        2. <strong>Cache (L1, L2, L3):</strong> 1-10 ns, MB<br>
        3. <strong>Main Memory (RAM):</strong> 100 ns, GB<br>
        4. <strong>SSD:</strong> 10-100 μs, TB<br>
        5. <strong>HDD:</strong> 1-10 ms, TB<br><br>
        
        <strong>Principle of Locality:</strong><br>
        • <strong>Temporal:</strong> Recently accessed likely to be accessed again<br>
        • <strong>Spatial:</strong> Nearby addresses likely to be accessed
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Paging")
    
    st.markdown("""
    <div class="concept-box">
        <strong>Paging:</strong> Divide memory into fixed-size pages<br><br>
        
        <strong>Components:</strong><br>
        • <strong>Page:</strong> Fixed-size block of logical memory<br>
        • <strong>Frame:</strong> Fixed-size block of physical memory<br>
        • <strong>Page Table:</strong> Maps logical to physical addresses<br><br>
        
        <strong>Address Translation:</strong><br>
        Logical Address = Page Number + Page Offset<br>
        Physical Address = Frame Number + Page Offset<br><br>
        
        <strong>Advantages:</strong><br>
        • No external fragmentation<br>
        • Easy to allocate<br>
        • Supports virtual memory<br><br>
        
        <strong>Disadvantages:</strong><br>
        • Internal fragmentation (last page)<br>
        • Page table overhead
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Page Replacement Algorithms")
    
    st.markdown("""
    <div class="algorithm-box">
        <strong>When to Replace:</strong> Page fault when no free frames<br><br>
        
        <strong>1. FIFO (First-In-First-Out):</strong><br>
        • Replace oldest page<br>
        • Simple but not optimal<br>
        • Belady's anomaly possible<br><br>
        
        <strong>2. Optimal:</strong><br>
        • Replace page not used for longest time in future<br>
        • Theoretical best (requires future knowledge)<br>
        • Used as benchmark<br><br>
        
        <strong>3. LRU (Least Recently Used):</strong><br>
        • Replace page not used for longest time in past<br>
        • Good approximation of optimal<br>
        • Implementation: counters or stack<br><br>
        
        <strong>4. Clock (Second Chance):</strong><br>
        • Approximation of LRU<br>
        • Use reference bit<br>
        • Circular queue with pointer<br><br>
        
        <strong>5. LFU (Least Frequently Used):</strong><br>
        • Replace page with smallest count<br>
        • Requires counter per page
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: FILE SYSTEMS ====================
with tabs[5]:
    st.markdown("## 📁 File Systems")
    
    st.markdown("### 1️⃣ File Concept")
    
    st.markdown("""
    <div class="theory-box">
        <strong>File:</strong> Named collection of related information<br><br>
        
        <strong>File Attributes:</strong><br>
        • Name, type, location<br>
        • Size, protection<br>
        • Time, date, user ID<br><br>
        
        <strong>File Operations:</strong><br>
        • Create, delete<br>
        • Open, close<br>
        • Read, write<br>
        • Seek, truncate<br><br>
        
        <strong>File Types:</strong><br>
        • Regular files (data, programs)<br>
        • Directories<br>
        • Special files (devices)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Directory Structure")
    
    st.markdown("""
    <div class="concept-box">
        <strong>Directory:</strong> Collection of file information<br><br>
        
        <strong>Types:</strong><br>
        • <strong>Single-Level:</strong> All files in one directory<br>
        • <strong>Two-Level:</strong> Separate directory per user<br>
        • <strong>Tree-Structured:</strong> Hierarchical (most common)<br>
        • <strong>Acyclic Graph:</strong> Shared subdirectories<br>
        • <strong>General Graph:</strong> Allows cycles (links)<br><br>
        
        <strong>Path Names:</strong><br>
        • <strong>Absolute:</strong> /home/user/file.txt<br>
        • <strong>Relative:</strong> ../docs/file.txt
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ File Allocation Methods")
    
    st.markdown("""
    <div class="algorithm-box">
        <strong>1. Contiguous Allocation:</strong><br>
        • File occupies consecutive blocks<br>
        • Fast sequential access<br>
        • External fragmentation<br>
        • Difficult to grow files<br><br>
        
        <strong>2. Linked Allocation:</strong><br>
        • Each block points to next<br>
        • No external fragmentation<br>
        • Slow random access<br>
        • Pointer overhead<br><br>
        
        <strong>3. Indexed Allocation:</strong><br>
        • Index block contains pointers<br>
        • Fast random access<br>
        • Pointer overhead<br>
        • Used by Unix (inode)<br><br>
        
        <strong>Unix inode Structure:</strong><br>
        • Direct blocks (12)<br>
        • Single indirect<br>
        • Double indirect<br>
        • Triple indirect
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: SECURITY ====================
with tabs[6]:
    st.markdown("## 🔒 Security & Protection")
    
    st.markdown("### 1️⃣ Protection Mechanisms")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Protection:</strong> Control access to resources<br><br>
        
        <strong>Access Control:</strong><br>
        • <strong>Access Matrix:</strong> Rows = domains, Columns = objects<br>
        • <strong>Access Control List (ACL):</strong> List per object<br>
        • <strong>Capability List:</strong> List per domain<br><br>
        
        <strong>Unix File Permissions:</strong><br>
        • Owner, Group, Others<br>
        • Read (r), Write (w), Execute (x)<br>
        • Example: rwxr-xr-- (754)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Security Threats")
    
    st.markdown("""
    <div class="concept-box">
        <strong>Common Threats:</strong><br><br>
        
        <strong>1. Malware:</strong><br>
        • Viruses, worms, trojans<br>
        • Ransomware, spyware<br><br>
        
        <strong>2. Attacks:</strong><br>
        • Buffer overflow<br>
        • SQL injection<br>
        • Denial of Service (DoS)<br>
        • Man-in-the-middle<br><br>
        
        <strong>3. Social Engineering:</strong><br>
        • Phishing<br>
        • Pretexting<br><br>
        
        <strong>Defense Mechanisms:</strong><br>
        • Authentication (passwords, biometrics)<br>
        • Encryption<br>
        • Firewalls<br>
        • Intrusion detection<br>
        • Regular updates
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: MODERN OS ====================
with tabs[7]:
    st.markdown("## 🌐 Modern OS Concepts")
    
    st.markdown("### 1️⃣ Virtualization")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Virtual Machine:</strong> Software emulation of hardware<br><br>
        
        <strong>Types:</strong><br>
        • <strong>Type 1 (Bare Metal):</strong> VMware ESXi, Hyper-V, Xen<br>
        • <strong>Type 2 (Hosted):</strong> VirtualBox, VMware Workstation<br><br>
        
        <strong>Benefits:</strong><br>
        • Server consolidation<br>
        • Isolation and security<br>
        • Easy migration<br>
        • Testing environments<br><br>
        
        <strong>Technologies:</strong><br>
        • Hardware-assisted (Intel VT-x, AMD-V)<br>
        • Paravirtualization<br>
        • Full virtualization
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Containers")
    
    st.markdown("""
    <div class="example-box">
        <strong>Containers vs VMs:</strong><br><br>
        
        <strong>Containers (Docker):</strong><br>
        • Share OS kernel<br>
        • Lightweight (MB)<br>
        • Fast startup (seconds)<br>
        • Less isolation<br><br>
        
        <strong>Virtual Machines:</strong><br>
        • Full OS per VM<br>
        • Heavy (GB)<br>
        • Slow startup (minutes)<br>
        • Strong isolation<br><br>
        
        <strong>Container Orchestration:</strong><br>
        • Kubernetes<br>
        • Docker Swarm<br>
        • Apache Mesos
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Real-Time Operating Systems (RTOS)")
    
    st.markdown("""
    <div class="concept-box">
        <strong>RTOS:</strong> Guarantees response within time constraints<br><br>
        
        <strong>Types:</strong><br>
        • <strong>Hard Real-Time:</strong> Missing deadline is catastrophic<br>
        &nbsp;&nbsp;Example: Aircraft control, medical devices<br>
        • <strong>Soft Real-Time:</strong> Missing deadline degrades performance<br>
        &nbsp;&nbsp;Example: Video streaming, gaming<br><br>
        
        <strong>Characteristics:</strong><br>
        • Deterministic scheduling<br>
        • Minimal latency<br>
        • Priority-based preemption<br><br>
        
        <strong>Examples:</strong><br>
        • FreeRTOS, VxWorks<br>
        • QNX, RTLinux
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 9: PRACTICE PROBLEMS ====================
with tabs[8]:
    st.markdown("## 🎯 Practice Problems")
    
    problems = [
        {
            "title": "Problem 1: Deadlock Detection",
            "question": "Given 3 processes (P0, P1, P2) and 3 resources (A, B, C). Current allocation and maximum need shown below. Is the system in a safe state?",
            "data": """
Allocation:     Max Need:       Available:
    A B C           A B C           A B C
P0: 0 1 0       P0: 7 5 3           3 3 2
P1: 2 0 0       P1: 3 2 2
P2: 3 0 2       P2: 9 0 2
            """,
            "hint": "Use Banker's Algorithm to check for safe sequence",
            "solution": """
**Solution using Banker's Algorithm:**

1. Calculate Need matrix:
   Need = Max - Allocation
   
   Need:
       A B C
   P0: 7 4 3
   P1: 1 2 2
   P2: 6 0 0

2. Find safe sequence:
   Available = [3, 3, 2]
   
   - P1 can finish: Need[1] ≤ Available
     After P1: Available = [3+2, 3+0, 2+0] = [5, 3, 2]
   
   - P0 can finish: Need[0] ≤ Available
     After P0: Available = [5+0, 3+1, 2+0] = [5, 4, 2]
   
   - P2 can finish: Need[2] ≤ Available
     After P2: Available = [5+3, 4+0, 2+2] = [8, 4, 4]

**Safe sequence: P1 → P0 → P2**

**Answer:** System is in SAFE state
            """
        },
        {
            "title": "Problem 2: Page Replacement",
            "question": "Given reference string: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2. Calculate page faults for FIFO and LRU with 3 frames.",
            "hint": "Track which pages are in memory and when to replace",
            "solution": """
**FIFO (First-In-First-Out):**

Reference: 7  0  1  2  0  3  0  4  2  3  0  3  2
Frames:    7  7  7  2  2  2  2  4  4  4  0  0  0
           -  0  0  0  0  3  3  3  2  2  2  2  2
           -  -  1  1  1  1  0  0  0  3  3  3  3
Fault:     F  F  F  F  -  F  F  F  F  F  F  -  -

**Page Faults (FIFO): 10**

---

**LRU (Least Recently Used):**

Reference: 7  0  1  2  0  3  0  4  2  3  0  3  2
Frames:    7  7  7  2  2  2  2  2  2  2  0  0  0
           -  0  0  0  0  0  0  4  4  3  3  3  3
           -  -  1  1  1  3  3  3  3  3  3  3  2
Fault:     F  F  F  F  -  F  -  F  -  F  F  -  F

**Page Faults (LRU): 9**

**LRU performs better (fewer page faults)**
            """
        }
    ]
    
    for idx, problem in enumerate(problems, 1):
        with st.expander(f"📝 {problem['title']}", expanded=False):
            st.markdown(f"**Question:** {problem['question']}")
            
            if 'data' in problem:
                st.code(problem['data'])
            
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
        <p>High-quality video tutorials for learning Operating Systems</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {
            "title": "Operating Systems",
            "channel": "Neso Academy",
            "url": "https://www.youtube.com/playlist?list=PLBlnK6fEyqRiVhbXDGLXDk_OQAeuVcp2O",
            "description": "Complete OS course covering all fundamental concepts",
            "duration": "Playlist (~100 videos)"
        },
        {
            "title": "Introduction to Operating Systems",
            "channel": "Udacity",
            "url": "https://www.youtube.com/playlist?list=PLqoiDr4YpRdm_nzFhCDZcH5bFW5IvB8OC",
            "description": "Georgia Tech CS course on OS fundamentals",
            "duration": "Full Course"
        },
        {
            "title": "Operating System Basics",
            "channel": "Crash Course Computer Science",
            "url": "https://www.youtube.com/watch?v=26QPDBe-NB8",
            "description": "Quick introduction to OS concepts",
            "duration": "~12 min"
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
            "title": "Operating Systems",
            "channel": "MIT OpenCourseWare",
            "url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP62WVs95MNq3dQBqY2vGOtQ2",
            "description": "MIT 6.828 - Operating System Engineering",
            "duration": "Full Course"
        },
        {
            "title": "Advanced Operating Systems",
            "channel": "UC Berkeley",
            "url": "https://www.youtube.com/playlist?list=PLRdybCcWDFzCag9A0h1m9QYaujD0xefgM",
            "description": "CS 162 - Operating Systems and Systems Programming",
            "duration": "Full Course"
        },
        {
            "title": "Process Synchronization",
            "channel": "Abdul Bari",
            "url": "https://www.youtube.com/playlist?list=PLIY8eNdw5tW_lHyageTADFKBt9weJXndE",
            "description": "Detailed explanation of synchronization problems",
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
            "title": "Linux Kernel Development",
            "channel": "The Linux Foundation",
            "url": "https://www.youtube.com/c/TheLinuxFoundation",
            "description": "Advanced Linux kernel topics",
            "duration": "Channel"
        },
        {
            "title": "Operating Systems: Three Easy Pieces",
            "channel": "OSTEP Authors",
            "url": "https://pages.cs.wisc.edu/~remzi/OSTEP/",
            "description": "Free online textbook with videos",
            "duration": "Book + Videos"
        },
        {
            "title": "Virtualization and Cloud Computing",
            "channel": "VMware",
            "url": "https://www.youtube.com/user/vmwaretv",
            "description": "Advanced virtualization concepts",
            "duration": "Channel"
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
            "title": "Build Your Own OS",
            "channel": "Daedalus Community",
            "url": "https://www.youtube.com/playlist?list=PLHh55M_Kq4OApWScZyPl5HhgsTJS9MZ6M",
            "description": "OS development from scratch",
            "duration": "Playlist"
        },
        {
            "title": "Linux From Scratch",
            "channel": "Linux From Scratch",
            "url": "http://www.linuxfromscratch.org/",
            "description": "Build your own Linux distribution",
            "duration": "Project"
        },
        {
            "title": "Docker Tutorial",
            "channel": "TechWorld with Nana",
            "url": "https://www.youtube.com/watch?v=3c-iBn73dDE",
            "description": "Complete Docker tutorial for beginners",
            "duration": "~3 hours"
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
        1. Understand basic OS concepts (processes, memory, files)<br>
        2. Study synchronization problems and solutions<br>
        3. Learn scheduling algorithms and compare performance<br>
        4. Explore memory management (paging, virtual memory)<br>
        5. Understand file systems and I/O<br>
        6. Practice with Linux commands and system programming<br>
        7. Build small OS components (shell, scheduler)<br>
        8. Explore modern concepts (containers, virtualization)<br><br>
        
        <strong>Practice Resources:</strong><br>
        • <strong>xv6:</strong> Simple Unix-like OS for learning<br>
        • <strong>Linux Kernel:</strong> Read source code<br>
        • <strong>OSTEP:</strong> https://pages.cs.wisc.edu/~remzi/OSTEP/<br>
        • <strong>OSDev Wiki:</strong> https://wiki.osdev.org/
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE203 - Operating Systems</strong><br>
    <small>UTel University | Department of Computer Engineering</small>
</div>
""", unsafe_allow_html=True)
