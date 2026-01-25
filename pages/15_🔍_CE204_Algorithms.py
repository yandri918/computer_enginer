import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="CE204 - Algorithms and Data Structures", page_icon="🔍", layout="wide")

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
        background: linear-gradient(135deg, #f5f3ff 0%, #ede9fe 100%);
        border-left: 5px solid #8b5cf6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .complexity-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .algorithm-box {
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .datastructure-box {
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
    <div style="font-size: 1.2rem; opacity: 0.9;">CE204</div>
    <div class="course-title">Algorithms and Data Structures</div>
    <div>🔍 4 Credits | Semester 4 | Algorithms</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "4")
with col2:
    st.metric("Semester", "4")
with col3:
    st.metric("Difficulty", "6/7")
with col4:
    st.metric("Hours/Week", "10")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "⏱️ Complexity Analysis",
    "🔄 Sorting Algorithms",
    "🔍 Searching & Trees",
    "📊 Graph Algorithms",
    "💡 Dynamic Programming",
    "🗂️ Advanced Data Structures",
    "🧮 Algorithm Design",
    "🎯 Practice Problems",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive study of fundamental algorithms and data structures. Covers algorithm analysis, complexity theory, 
        sorting and searching algorithms, graph algorithms, dynamic programming, and advanced data structures. Emphasizes 
        both theoretical foundations (correctness proofs, complexity analysis) and practical implementation. Students will 
        learn to design efficient algorithms and choose appropriate data structures for real-world problems.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Analyze algorithm time and space complexity",
        "Implement fundamental data structures (arrays, linked lists, trees, graphs)",
        "Design and implement sorting and searching algorithms",
        "Apply graph algorithms (BFS, DFS, Dijkstra, MST)",
        "Solve problems using dynamic programming",
        "Use advanced data structures (heaps, hash tables, tries)",
        "Prove algorithm correctness",
        "Optimize algorithms for performance"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Fundamentals:**
        - Algorithm analysis (Big O, Theta, Omega)
        - Recurrence relations
        - Master theorem
        - Amortized analysis
        - Proof techniques
        
        **Data Structures:**
        - Arrays and linked lists
        - Stacks and queues
        - Trees (BST, AVL, Red-Black)
        - Heaps and priority queues
        - Hash tables
        """)
    
    with col2:
        st.markdown("""
        **Algorithms:**
        - Sorting (Quick, Merge, Heap, Radix)
        - Searching (Binary search, BST)
        - Graph algorithms (BFS, DFS, Dijkstra, Floyd-Warshall)
        - Minimum spanning trees (Kruskal, Prim)
        - Dynamic programming
        
        **Advanced Topics:**
        - Greedy algorithms
        - Divide and conquer
        - Backtracking
        - NP-completeness
        - Approximation algorithms
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Introduction to Algorithms (CLRS)", "author": "Cormen, Leiserson, Rivest, Stein", "type": "Textbook"},
        {"title": "Algorithm Design", "author": "Kleinberg & Tardos", "type": "Textbook"},
        {"title": "The Algorithm Design Manual", "author": "Steven Skiena", "type": "Practical"},
        {"title": "Algorithms", "author": "Robert Sedgewick", "type": "Classic"}
    ]
    
    for resource in resources:
        st.markdown(f"📖 **{resource['title']}** by {resource['author']} ({resource['type']})")

# ==================== TAB 2: COMPLEXITY ANALYSIS ====================
with tabs[1]:
    st.markdown("## ⏱️ Complexity Analysis")
    
    st.markdown("### 1️⃣ Asymptotic Notation")
    
    st.markdown("""
    <div class="complexity-box">
        <strong>Big O Notation (Upper Bound):</strong><br>
        f(n) = O(g(n)) if ∃ c, n₀ such that f(n) ≤ c·g(n) for all n ≥ n₀<br><br>
        
        <strong>Big Omega (Lower Bound):</strong><br>
        f(n) = Ω(g(n)) if ∃ c, n₀ such that f(n) ≥ c·g(n) for all n ≥ n₀<br><br>
        
        <strong>Big Theta (Tight Bound):</strong><br>
        f(n) = Θ(g(n)) if f(n) = O(g(n)) AND f(n) = Ω(g(n))<br><br>
        
        <strong>Little o (Strict Upper Bound):</strong><br>
        f(n) = o(g(n)) if lim(n→∞) f(n)/g(n) = 0
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Common Complexity Classes")
    
    # Complexity comparison table
    complexity_data = {
        'Complexity': ['O(1)', 'O(log n)', 'O(n)', 'O(n log n)', 'O(n²)', 'O(n³)', 'O(2ⁿ)', 'O(n!)'],
        'Name': ['Constant', 'Logarithmic', 'Linear', 'Linearithmic', 'Quadratic', 'Cubic', 'Exponential', 'Factorial'],
        'n=10': ['1', '3', '10', '33', '100', '1K', '1K', '3.6M'],
        'n=100': ['1', '7', '100', '664', '10K', '1M', '1.3×10³⁰', '9.3×10¹⁵⁷'],
        'n=1000': ['1', '10', '1K', '10K', '1M', '1B', 'Huge', 'Huge'],
        'Example': ['Array access', 'Binary search', 'Linear search', 'Merge sort', 'Bubble sort', 'Matrix multiply', 'Subset sum', 'TSP brute force']
    }
    
    df_complexity = pd.DataFrame(complexity_data)
    st.dataframe(df_complexity, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Master Theorem")
    
    st.markdown("""
    <div class="theory-box">
        <strong>For recurrences: T(n) = aT(n/b) + f(n)</strong><br><br>
        
        <strong>Case 1:</strong> If f(n) = O(n^(log_b(a) - ε)) for some ε > 0<br>
        → T(n) = Θ(n^(log_b(a)))<br><br>
        
        <strong>Case 2:</strong> If f(n) = Θ(n^(log_b(a)))<br>
        → T(n) = Θ(n^(log_b(a)) log n)<br><br>
        
        <strong>Case 3:</strong> If f(n) = Ω(n^(log_b(a) + ε)) for some ε > 0<br>
        AND af(n/b) ≤ cf(n) for some c < 1<br>
        → T(n) = Θ(f(n))<br><br>
        
        <strong>Examples:</strong><br>
        • Merge Sort: T(n) = 2T(n/2) + Θ(n) → T(n) = Θ(n log n)<br>
        • Binary Search: T(n) = T(n/2) + Θ(1) → T(n) = Θ(log n)
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: SORTING ====================
with tabs[2]:
    st.markdown("## 🔄 Sorting Algorithms")
    
    st.markdown("### 1️⃣ Comparison-Based Sorting")
    
    # Sorting algorithms comparison
    sorting_data = {
        'Algorithm': ['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort'],
        'Best': ['O(n)', 'O(n²)', 'O(n)', 'O(n log n)', 'O(n log n)', 'O(n log n)'],
        'Average': ['O(n²)', 'O(n²)', 'O(n²)', 'O(n log n)', 'O(n log n)', 'O(n log n)'],
        'Worst': ['O(n²)', 'O(n²)', 'O(n²)', 'O(n log n)', 'O(n²)', 'O(n log n)'],
        'Space': ['O(1)', 'O(1)', 'O(1)', 'O(n)', 'O(log n)', 'O(1)'],
        'Stable': ['Yes', 'No', 'Yes', 'Yes', 'No', 'No']
    }
    
    df_sorting = pd.DataFrame(sorting_data)
    st.dataframe(df_sorting, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Quick Sort")
    
    st.markdown("""
    <div class="algorithm-box">
        <strong>Divide and Conquer Algorithm:</strong><br><br>
        
        <strong>Steps:</strong><br>
        1. Choose pivot element<br>
        2. Partition: elements < pivot on left, > pivot on right<br>
        3. Recursively sort left and right subarrays<br><br>
        
        <strong>Complexity:</strong><br>
        • Best/Average: O(n log n)<br>
        • Worst: O(n²) (already sorted, bad pivot)<br>
        • Space: O(log n) for recursion stack<br><br>
        
        <strong>Optimizations:</strong><br>
        • Random pivot selection<br>
        • Median-of-three pivot<br>
        • Hybrid with insertion sort for small arrays
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
def quicksort(arr, low, high):
    if low < high:
        # Partition array and get pivot index
        pi = partition(arr, low, high)
        
        # Recursively sort left and right subarrays
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    # Choose rightmost element as pivot
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example usage
arr = [10, 7, 8, 9, 1, 5]
quicksort(arr, 0, len(arr) - 1)
print(arr)  # [1, 5, 7, 8, 9, 10]
    """, language="python")
    
    st.markdown("---")
    st.markdown("### 3️⃣ Merge Sort")
    
    st.code("""
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    
    # Conquer (merge)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # Merge two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result
    """, language="python")

# ==================== TAB 4: SEARCHING & TREES ====================
with tabs[3]:
    st.markdown("## 🔍 Searching & Trees")
    
    st.markdown("### 1️⃣ Binary Search")
    
    st.markdown("""
    <div class="algorithm-box">
        <strong>Requirements:</strong> Sorted array<br>
        <strong>Complexity:</strong> O(log n)<br>
        <strong>Space:</strong> O(1) iterative, O(log n) recursive<br><br>
        
        <strong>Idea:</strong> Repeatedly divide search space in half
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found
    """, language="python")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Binary Search Tree (BST)")
    
    st.markdown("""
    <div class="datastructure-box">
        <strong>Properties:</strong><br>
        • Left subtree contains only nodes with keys < node's key<br>
        • Right subtree contains only nodes with keys > node's key<br>
        • Both subtrees are also BSTs<br><br>
        
        <strong>Operations:</strong><br>
        • Search: O(h) where h = height<br>
        • Insert: O(h)<br>
        • Delete: O(h)<br>
        • Best case (balanced): h = log n → O(log n)<br>
        • Worst case (skewed): h = n → O(n)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Balanced Trees")
    
    st.markdown("""
    <div class="theory-box">
        <strong>AVL Tree:</strong><br>
        • Self-balancing BST<br>
        • Height difference between left and right ≤ 1<br>
        • Rotations to maintain balance<br>
        • All operations: O(log n)<br><br>
        
        <strong>Red-Black Tree:</strong><br>
        • Self-balancing BST<br>
        • Each node colored red or black<br>
        • Properties ensure height ≤ 2 log(n+1)<br>
        • Used in C++ STL map, Java TreeMap<br><br>
        
        <strong>B-Tree:</strong><br>
        • Generalization of BST<br>
        • Multiple keys per node<br>
        • Used in databases and file systems<br>
        • Minimizes disk I/O
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: GRAPH ALGORITHMS ====================
with tabs[4]:
    st.markdown("## 📊 Graph Algorithms")
    
    st.markdown("### 1️⃣ Graph Traversal")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Breadth-First Search (BFS):**")
        st.code("""
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        """, language="python")
        
        st.markdown("""
        **Properties:**
        - Uses queue (FIFO)
        - Finds shortest path (unweighted)
        - Level-order traversal
        - Time: O(V + E)
        - Space: O(V)
        """)
    
    with col2:
        st.markdown("**Depth-First Search (DFS):**")
        st.code("""
def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(vertex)
    print(vertex)
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited
        """, language="python")
        
        st.markdown("""
        **Properties:**
        - Uses stack (recursion/explicit)
        - Explores as far as possible
        - Used for topological sort
        - Time: O(V + E)
        - Space: O(V)
        """)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Shortest Path Algorithms")
    
    st.markdown("""
    <div class="algorithm-box">
        <strong>Dijkstra's Algorithm:</strong><br>
        • Single-source shortest path<br>
        • Non-negative edge weights<br>
        • Greedy algorithm<br>
        • Time: O((V + E) log V) with min-heap<br><br>
        
        <strong>Bellman-Ford Algorithm:</strong><br>
        • Single-source shortest path<br>
        • Handles negative weights<br>
        • Detects negative cycles<br>
        • Time: O(VE)<br><br>
        
        <strong>Floyd-Warshall Algorithm:</strong><br>
        • All-pairs shortest path<br>
        • Dynamic programming<br>
        • Time: O(V³)<br>
        • Space: O(V²)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Minimum Spanning Tree")
    
    st.markdown("""
    <div class="algorithm-box">
        <strong>Kruskal's Algorithm:</strong><br>
        • Sort edges by weight<br>
        • Add edge if doesn't create cycle<br>
        • Uses Union-Find data structure<br>
        • Time: O(E log E)<br><br>
        
        <strong>Prim's Algorithm:</strong><br>
        • Start from arbitrary vertex<br>
        • Grow tree by adding minimum weight edge<br>
        • Uses priority queue<br>
        • Time: O(E log V) with binary heap
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: DYNAMIC PROGRAMMING ====================
with tabs[5]:
    st.markdown("## 💡 Dynamic Programming")
    
    st.markdown("### 1️⃣ DP Fundamentals")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Dynamic Programming:</strong> Solve complex problems by breaking down into simpler subproblems<br><br>
        
        <strong>When to use DP:</strong><br>
        1. <strong>Optimal Substructure:</strong> Optimal solution contains optimal solutions to subproblems<br>
        2. <strong>Overlapping Subproblems:</strong> Same subproblems solved multiple times<br><br>
        
        <strong>Approaches:</strong><br>
        • <strong>Top-Down (Memoization):</strong> Recursion + cache<br>
        • <strong>Bottom-Up (Tabulation):</strong> Iterative, fill table<br><br>
        
        <strong>Steps:</strong><br>
        1. Define subproblems<br>
        2. Find recurrence relation<br>
        3. Identify base cases<br>
        4. Determine computation order<br>
        5. Optimize space if possible
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Classic DP Problems")
    
    st.markdown("**Fibonacci (Memoization):**")
    st.code("""
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Time: O(n), Space: O(n)
    """, language="python")
    
    st.markdown("**Longest Common Subsequence:**")
    st.code("""
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# Time: O(mn), Space: O(mn)
    """, language="python")
    
    st.markdown("**0/1 Knapsack:**")
    st.code("""
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

# Time: O(nW), Space: O(nW)
    """, language="python")

# ==================== TAB 7: ADVANCED DATA STRUCTURES ====================
with tabs[6]:
    st.markdown("## 🗂️ Advanced Data Structures")
    
    st.markdown("### 1️⃣ Heap")
    
    st.markdown("""
    <div class="datastructure-box">
        <strong>Binary Heap:</strong> Complete binary tree satisfying heap property<br><br>
        
        <strong>Types:</strong><br>
        • <strong>Max Heap:</strong> Parent ≥ children<br>
        • <strong>Min Heap:</strong> Parent ≤ children<br><br>
        
        <strong>Operations:</strong><br>
        • Insert: O(log n)<br>
        • Extract-Max/Min: O(log n)<br>
        • Peek: O(1)<br>
        • Build heap: O(n)<br><br>
        
        <strong>Applications:</strong><br>
        • Priority queue<br>
        • Heap sort<br>
        • Dijkstra's algorithm
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Hash Table")
    
    st.markdown("""
    <div class="datastructure-box">
        <strong>Hash Table:</strong> Maps keys to values using hash function<br><br>
        
        <strong>Operations (Average):</strong><br>
        • Insert: O(1)<br>
        • Search: O(1)<br>
        • Delete: O(1)<br><br>
        
        <strong>Collision Resolution:</strong><br>
        • <strong>Chaining:</strong> Linked list at each bucket<br>
        • <strong>Open Addressing:</strong> Linear probing, quadratic probing, double hashing<br><br>
        
        <strong>Load Factor:</strong> α = n/m (n = elements, m = buckets)<br>
        • Rehash when α exceeds threshold (typically 0.75)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Trie (Prefix Tree)")
    
    st.markdown("""
    <div class="datastructure-box">
        <strong>Trie:</strong> Tree for storing strings, efficient prefix operations<br><br>
        
        <strong>Operations:</strong><br>
        • Insert: O(m) where m = string length<br>
        • Search: O(m)<br>
        • Prefix search: O(m)<br>
        • Space: O(ALPHABET_SIZE × m × n)<br><br>
        
        <strong>Applications:</strong><br>
        • Autocomplete<br>
        • Spell checker<br>
        • IP routing<br>
        • Dictionary implementation
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: ALGORITHM DESIGN ====================
with tabs[7]:
    st.markdown("## 🧮 Algorithm Design Techniques")
    
    st.markdown("### 1️⃣ Divide and Conquer")
    
    st.markdown("""
    <div class="algorithm-box">
        <strong>Strategy:</strong> Break problem into smaller subproblems, solve recursively, combine solutions<br><br>
        
        <strong>Steps:</strong><br>
        1. <strong>Divide:</strong> Break into smaller subproblems<br>
        2. <strong>Conquer:</strong> Solve subproblems recursively<br>
        3. <strong>Combine:</strong> Merge solutions<br><br>
        
        <strong>Examples:</strong><br>
        • Merge Sort, Quick Sort<br>
        • Binary Search<br>
        • Strassen's Matrix Multiplication<br>
        • Closest Pair of Points
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Greedy Algorithms")
    
    st.markdown("""
    <div class="algorithm-box">
        <strong>Strategy:</strong> Make locally optimal choice at each step<br><br>
        
        <strong>When to use:</strong><br>
        • Greedy choice property<br>
        • Optimal substructure<br><br>
        
        <strong>Examples:</strong><br>
        • Activity Selection<br>
        • Huffman Coding<br>
        • Dijkstra's Algorithm<br>
        • Kruskal's MST<br>
        • Fractional Knapsack<br><br>
        
        <strong>Note:</strong> Doesn't always give optimal solution (e.g., 0/1 Knapsack)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Backtracking")
    
    st.markdown("""
    <div class="algorithm-box">
        <strong>Strategy:</strong> Build solution incrementally, abandon when constraints violated<br><br>
        
        <strong>Template:</strong><br>
        1. Choose: Make a choice<br>
        2. Explore: Recursively explore<br>
        3. Unchoose: Backtrack if needed<br><br>
        
        <strong>Examples:</strong><br>
        • N-Queens Problem<br>
        • Sudoku Solver<br>
        • Subset Sum<br>
        • Graph Coloring<br>
        • Hamiltonian Path
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 9: PRACTICE PROBLEMS ====================
with tabs[8]:
    st.markdown("## 🎯 Practice Problems")
    
    problems = [
        {
            "title": "Problem 1: Two Sum",
            "difficulty": "Easy",
            "question": "Given an array of integers and a target, return indices of two numbers that add up to target.",
            "example": "Input: nums = [2,7,11,15], target = 9\nOutput: [0,1] (nums[0] + nums[1] = 2 + 7 = 9)",
            "hint": "Use hash table to store complements",
            "solution": """
**Solution using Hash Table:**

```python
def two_sum(nums, target):
    seen = {}  # value -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []  # No solution

# Time: O(n), Space: O(n)
```

**Explanation:**
1. Iterate through array
2. For each number, calculate complement (target - num)
3. Check if complement exists in hash table
4. If yes, return indices
5. If no, add current number to hash table
            """
        },
        {
            "title": "Problem 2: Merge K Sorted Lists",
            "difficulty": "Hard",
            "question": "Merge k sorted linked lists into one sorted list.",
            "example": "Input: [[1,4,5],[1,3,4],[2,6]]\nOutput: [1,1,2,3,4,4,5,6]",
            "hint": "Use min-heap to track smallest elements",
            "solution": """
**Solution using Min-Heap:**

```python
import heapq

def merge_k_lists(lists):
    heap = []
    
    # Add first node from each list to heap
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
    
    dummy = ListNode(0)
    current = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next

# Time: O(N log k) where N = total nodes, k = lists
# Space: O(k) for heap
```
            """
        }
    ]
    
    for idx, problem in enumerate(problems, 1):
        with st.expander(f"📝 {problem['title']} ({problem['difficulty']})", expanded=False):
            st.markdown(f"**Question:** {problem['question']}")
            st.code(problem['example'])
            
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
        <p>High-quality video tutorials for learning Algorithms and Data Structures</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {
            "title": "Data Structures and Algorithms",
            "channel": "freeCodeCamp.org",
            "url": "https://www.youtube.com/watch?v=8hly31xKli0",
            "description": "Complete DSA course for beginners",
            "duration": "~5 hours"
        },
        {
            "title": "Algorithms and Data Structures Tutorial",
            "channel": "CS Dojo",
            "url": "https://www.youtube.com/playlist?list=PLBZBJbE_rGRV8D7XZ08LK6z-4zPoWzu5H",
            "description": "Beginner-friendly explanations",
            "duration": "Playlist"
        },
        {
            "title": "Data Structures Easy to Advanced",
            "channel": "William Fiset",
            "url": "https://www.youtube.com/playlist?list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu",
            "description": "Comprehensive data structures course",
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
            "title": "Introduction to Algorithms (MIT 6.006)",
            "channel": "MIT OpenCourseWare",
            "url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb",
            "description": "MIT's legendary algorithms course",
            "duration": "Full Course"
        },
        {
            "title": "Algorithms Specialization",
            "channel": "Stanford (Tim Roughgarden)",
            "url": "https://www.youtube.com/playlist?list=PLXFMmlk03Dt7Q0xr1PIAriY5623cKiH7V",
            "description": "Stanford's algorithms course",
            "duration": "Full Course"
        },
        {
            "title": "Abdul Bari Algorithms",
            "channel": "Abdul Bari",
            "url": "https://www.youtube.com/playlist?list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O",
            "description": "Clear explanations with animations",
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
            "title": "Advanced Algorithms (MIT 6.854)",
            "channel": "MIT OpenCourseWare",
            "url": "https://www.youtube.com/playlist?list=PL6ogFv-ieghdoGKGg2Bik3Gl1glBTEu8c",
            "description": "Graduate-level algorithms",
            "duration": "Full Course"
        },
        {
            "title": "Competitive Programming",
            "channel": "Errichto",
            "url": "https://www.youtube.com/c/Errichto",
            "description": "Advanced algorithms and problem-solving",
            "duration": "Channel"
        },
        {
            "title": "Dynamic Programming",
            "channel": "Tushar Roy",
            "url": "https://www.youtube.com/playlist?list=PLrmLmBdmIlpsHaNTPP_jHHDx_os9ItYXr",
            "description": "In-depth DP problems",
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
    
    # Practice Platforms
    st.markdown("### 💻 Practice Platforms")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Recommended Practice Sites:</strong><br><br>
        
        • <strong>LeetCode:</strong> https://leetcode.com/ (Interview prep)<br>
        • <strong>HackerRank:</strong> https://www.hackerrank.com/<br>
        • <strong>Codeforces:</strong> https://codeforces.com/ (Competitive)<br>
        • <strong>TopCoder:</strong> https://www.topcoder.com/<br>
        • <strong>Project Euler:</strong> https://projecteuler.net/ (Math)<br>
        • <strong>CSES Problem Set:</strong> https://cses.fi/problemset/<br><br>
        
        <strong>Study Tips:</strong><br>
        1. Master one data structure at a time<br>
        2. Understand time/space complexity<br>
        3. Practice coding without IDE first<br>
        4. Learn to recognize problem patterns<br>
        5. Solve problems multiple ways<br>
        6. Review and optimize your solutions
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE204 - Algorithms and Data Structures</strong><br>
    <small>UTel University | Department of Computer Engineering</small>
</div>
""", unsafe_allow_html=True)
