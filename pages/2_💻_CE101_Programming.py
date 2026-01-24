import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="CE101 - Structured Programming", page_icon="💻", layout="wide")

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
        background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .code-box {
        background: #1e293b;
        color: #e2e8f0;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        font-family: 'JetBrains Mono', monospace;
    }
    
    .example-box {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-left: 5px solid #3b82f6;
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
    
    .algorithm-box {
        background: #faf5ff;
        border-left: 4px solid #8b5cf6;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    
    .complexity-badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.85rem;
        font-weight: 600;
        margin: 0.2rem;
    }
    
    .time-complexity {
        background: #dbeafe;
        color: #1e40af;
    }
    
    .space-complexity {
        background: #fce7f3;
        color: #9f1239;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="course-header">
    <div style="font-size: 1.2rem; opacity: 0.9;">CE101</div>
    <div class="course-title">Structured Programming</div>
    <div>💻 4 Credits | Semester 1 | Programming</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "4")
with col2:
    st.metric("Semester", "1")
with col3:
    st.metric("Difficulty", "2/7")
with col4:
    st.metric("Hours/Week", "6")

st.markdown("---")

# Navigation tabs - Graduate level
tabs = st.tabs([
    "📚 Overview",
    "🔤 Fundamentals",
    "🏗️ Data Structures",
    "⚙️ Algorithms",
    "🎨 Design Patterns",
    "🧪 Testing & Debugging",
    "🚀 Advanced Topics",
    "💡 Best Practices",
    "🧮 Practice Problems",
    "📊 Complexity Analysis"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive introduction to structured programming with emphasis on algorithm design, 
        data structures, and software engineering principles. This course covers fundamental to 
        advanced programming concepts using modern languages (Python, C++, Java) and prepares 
        students for graduate-level computer science topics.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Master fundamental programming constructs and control structures",
        "Design and implement efficient algorithms with complexity analysis",
        "Understand and apply advanced data structures (trees, graphs, hash tables)",
        "Write clean, maintainable, and well-documented code",
        "Apply design patterns and software engineering best practices",
        "Debug complex programs using systematic approaches",
        "Analyze time and space complexity of algorithms",
        "Implement recursive and iterative solutions effectively"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Fundamentals:**
        - Variables, types, and operators
        - Control structures (if, loops, switch)
        - Functions and recursion
        - Pointers and memory management
        - File I/O and streams
        
        **Data Structures:**
        - Arrays and linked lists
        - Stacks and queues
        - Trees (BST, AVL, Red-Black)
        - Graphs and hash tables
        - Heaps and priority queues
        """)
    
    with col2:
        st.markdown("""
        **Algorithms:**
        - Sorting (QuickSort, MergeSort, HeapSort)
        - Searching (Binary Search, DFS, BFS)
        - Dynamic Programming
        - Greedy algorithms
        - Divide and Conquer
        
        **Advanced Topics:**
        - Design patterns (OOP)
        - Code optimization
        - Parallel programming basics
        - Memory profiling
        - Software testing
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Introduction to Algorithms (CLRS)", "author": "Cormen et al.", "type": "Textbook"},
        {"title": "The C Programming Language", "author": "Kernighan & Ritchie", "type": "Classic"},
        {"title": "Clean Code", "author": "Robert C. Martin", "type": "Best Practices"},
        {"title": "LeetCode & HackerRank", "author": "Online", "type": "Practice Platform"}
    ]
    
    for resource in resources:
        st.markdown(f"📖 **{resource['title']}** by {resource['author']} ({resource['type']})")

# ==================== TAB 2: FUNDAMENTALS ====================
with tabs[1]:
    st.markdown("## 🔤 Programming Fundamentals")
    
    st.markdown("### 1️⃣ Variables and Data Types")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Primitive Data Types:</strong><br>
        • <strong>Integer:</strong> int, long, short (whole numbers)<br>
        • <strong>Floating-point:</strong> float, double (decimal numbers)<br>
        • <strong>Character:</strong> char (single character)<br>
        • <strong>Boolean:</strong> bool (true/false)<br>
        • <strong>Void:</strong> void (no value)
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
# Python Example
x = 42              # Integer
pi = 3.14159        # Float
name = "Alice"      # String
is_valid = True     # Boolean

# C++ Example
int x = 42;
double pi = 3.14159;
char grade = 'A';
bool is_valid = true;
    """, language="python")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Control Structures")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Conditional Statements:**")
        st.code("""
# If-Else
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'

# Switch (Python 3.10+)
match command:
    case "start":
        start_game()
    case "stop":
        stop_game()
    case _:
        print("Unknown")
        """, language="python")
    
    with col2:
        st.markdown("**Loops:**")
        st.code("""
# For loop
for i in range(10):
    print(i)

# While loop
while x > 0:
    x -= 1

# Do-while (C++)
do {
    x--;
} while (x > 0);
        """, language="python")
    
    st.markdown("---")
    st.markdown("### 3️⃣ Functions and Recursion")
    
    st.markdown("""
    <div class="algorithm-box">
        <strong>Function Design Principles:</strong><br>
        • Single Responsibility Principle<br>
        • Clear input/output contracts<br>
        • Meaningful names<br>
        • Proper documentation<br>
        • Error handling
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
# Iterative Factorial
def factorial_iterative(n):
    \"\"\"Calculate factorial using iteration.\"\"\"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive Factorial
def factorial_recursive(n):
    \"\"\"Calculate factorial using recursion.\"\"\"
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Tail-recursive (optimized)
def factorial_tail(n, accumulator=1):
    \"\"\"Tail-recursive factorial for optimization.\"\"\"
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)
    """, language="python")
    
    # Interactive factorial calculator
    st.markdown("#### 🧮 Interactive Factorial Calculator")
    
    n_fact = st.slider("Select n for factorial", 0, 20, 5)
    
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)
    
    result = factorial(n_fact)
    st.success(f"**{n_fact}! = {result:,}**")
    
    # Visualize growth
    fact_data = []
    for i in range(1, min(n_fact + 1, 15)):
        fact_data.append({'n': i, 'factorial': factorial(i)})
    
    df_fact = pd.DataFrame(fact_data)
    
    fact_chart = alt.Chart(df_fact).mark_line(point=True, strokeWidth=3).encode(
        x=alt.X('n:Q', title='n'),
        y=alt.Y('factorial:Q', title='n!', scale=alt.Scale(type='log')),
        tooltip=['n', 'factorial']
    ).properties(
        width=600,
        height=300,
        title="Factorial Growth (Log Scale)"
    )
    
    st.altair_chart(fact_chart, use_container_width=True)

# ==================== TAB 3: DATA STRUCTURES ====================
with tabs[2]:
    st.markdown("## 🏗️ Data Structures")
    
    st.markdown("### 1️⃣ Arrays and Linked Lists")
    
    comparison = pd.DataFrame({
        'Operation': ['Access', 'Search', 'Insert (beginning)', 'Insert (end)', 'Delete'],
        'Array': ['O(1)', 'O(n)', 'O(n)', 'O(1)*', 'O(n)'],
        'Linked List': ['O(n)', 'O(n)', 'O(1)', 'O(n)', 'O(1)*']
    })
    
    st.dataframe(comparison, use_container_width=True)
    st.caption("* Amortized time complexity")
    
    st.code("""
# Linked List Implementation (Python)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        \"\"\"Insert node at the beginning - O(1)\"\"\"
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        \"\"\"Insert node at the end - O(n)\"\"\"
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def delete_node(self, key):
        \"\"\"Delete first occurrence of key - O(n)\"\"\"
        current = self.head
        
        # If head needs to be deleted
        if current and current.data == key:
            self.head = current.next
            return
        
        # Search for the key
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        # Key not found
        if not current:
            return
        
        # Unlink the node
        prev.next = current.next
    """, language="python")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Stacks and Queues")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Stack (LIFO):**")
        st.code("""
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
        """, language="python")
    
    with col2:
        st.markdown("**Queue (FIFO):**")
        st.code("""
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
    
    def is_empty(self):
        return len(self.items) == 0
        """, language="python")
    
    st.markdown("---")
    st.markdown("### 3️⃣ Trees")
    
    st.markdown("""
    <div class="algorithm-box">
        <strong>Binary Search Tree Properties:</strong><br>
        • Left subtree contains nodes with keys < parent<br>
        • Right subtree contains nodes with keys > parent<br>
        • Both subtrees are also BSTs<br>
        • Average case: O(log n) for search, insert, delete<br>
        • Worst case: O(n) when tree becomes skewed
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        \"\"\"Insert value into BST - O(log n) average\"\"\"
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)
    
    def inorder_traversal(self, node, result=[]):
        \"\"\"Inorder: Left -> Root -> Right\"\"\"
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.val)
            self.inorder_traversal(node.right, result)
        return result
    """, language="python")

# ==================== TAB 4: ALGORITHMS ====================
with tabs[3]:
    st.markdown("## ⚙️ Algorithms")
    
    st.markdown("### 1️⃣ Sorting Algorithms")
    
    sorting_comparison = pd.DataFrame({
        'Algorithm': ['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort', 'Heap Sort'],
        'Best': ['O(n)', 'O(n²)', 'O(n)', 'O(n log n)', 'O(n log n)', 'O(n log n)'],
        'Average': ['O(n²)', 'O(n²)', 'O(n²)', 'O(n log n)', 'O(n log n)', 'O(n log n)'],
        'Worst': ['O(n²)', 'O(n²)', 'O(n²)', 'O(n log n)', 'O(n²)', 'O(n log n)'],
        'Space': ['O(1)', 'O(1)', 'O(1)', 'O(n)', 'O(log n)', 'O(1)'],
        'Stable': ['Yes', 'No', 'Yes', 'Yes', 'No', 'No']
    })
    
    st.dataframe(sorting_comparison, use_container_width=True)
    
    st.markdown("#### QuickSort Implementation")
    
    st.code("""
def quicksort(arr):
    \"\"\"
    QuickSort: Divide and Conquer algorithm
    Time: O(n log n) average, O(n²) worst
    Space: O(log n) for recursion stack
    \"\"\"
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

# Optimized in-place version
def quicksort_inplace(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort_inplace(arr, low, pi - 1)
        quicksort_inplace(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
    """, language="python")
    
    # Interactive sorting visualizer
    st.markdown("#### 📊 Sorting Visualizer")
    
    array_size = st.slider("Array size", 5, 20, 10)
    np.random.seed(42)
    random_array = np.random.randint(1, 100, array_size).tolist()
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Original Array:**")
        st.write(random_array)
    with col2:
        st.write("**Sorted Array:**")
        st.write(sorted(random_array))
    
    # Visualize
    df_sort = pd.DataFrame({
        'index': list(range(len(random_array))) * 2,
        'value': random_array + sorted(random_array),
        'type': ['Original'] * len(random_array) + ['Sorted'] * len(random_array)
    })
    
    sort_chart = alt.Chart(df_sort).mark_bar().encode(
        x=alt.X('index:O', title='Index'),
        y=alt.Y('value:Q', title='Value'),
        color=alt.Color('type:N', scale=alt.Scale(domain=['Original', 'Sorted'],
                                                    range=['#ef4444', '#10b981'])),
        column='type:N',
        tooltip=['index', 'value']
    ).properties(
        width=300,
        height=300
    )
    
    st.altair_chart(sort_chart)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Searching Algorithms")
    
    st.code("""
def binary_search(arr, target):
    \"\"\"
    Binary Search: Efficient search in sorted array
    Time: O(log n)
    Space: O(1)
    Precondition: arr must be sorted
    \"\"\"
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

# Recursive version
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
    """, language="python")
    
    st.markdown("---")
    st.markdown("### 3️⃣ Dynamic Programming")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Dynamic Programming Principles:</strong><br>
        1. <strong>Optimal Substructure:</strong> Optimal solution contains optimal solutions to subproblems<br>
        2. <strong>Overlapping Subproblems:</strong> Same subproblems solved multiple times<br>
        3. <strong>Memoization:</strong> Top-down approach with caching<br>
        4. <strong>Tabulation:</strong> Bottom-up approach with table
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
# Fibonacci: Classic DP Example

# Naive Recursive - O(2^n)
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

# Memoization - O(n)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Tabulation - O(n), O(n) space
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Space Optimized - O(n), O(1) space
def fib_optimized(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
    """, language="python")

# ==================== TAB 5: DESIGN PATTERNS ====================
with tabs[4]:
    st.markdown("## 🎨 Design Patterns")
    
    st.markdown("### 1️⃣ Creational Patterns")
    
    st.markdown("**Singleton Pattern:**")
    st.code("""
class Singleton:
    \"\"\"Ensure a class has only one instance\"\"\"
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
    """, language="python")
    
    st.markdown("**Factory Pattern:**")
    st.code("""
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Usage
factory = AnimalFactory()
dog = factory.create_animal("dog")
print(dog.speak())  # Woof!
    """, language="python")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Structural Patterns")
    
    st.markdown("**Decorator Pattern:**")
    st.code("""
# Function decorator
def timer_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Done"

# Class-based decorator
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        return "ConcreteComponent"

class Decorator(Component):
    def __init__(self, component):
        self._component = component
    
    def operation(self):
        return self._component.operation()

class ConcreteDecorator(Decorator):
    def operation(self):
        return f"ConcreteDecorator({self._component.operation()})"
    """, language="python")
    
    st.markdown("---")
    st.markdown("### 3️⃣ Behavioral Patterns")
    
    st.markdown("**Observer Pattern:**")
    st.code("""
class Subject:
    def __init__(self):
        self._observers = []
        self._state = None
    
    def attach(self, observer):
        self._observers.append(observer)
    
    def detach(self, observer):
        self._observers.remove(observer)
    
    def notify(self):
        for observer in self._observers:
            observer.update(self._state)
    
    def set_state(self, state):
        self._state = state
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, state):
        pass

class ConcreteObserver(Observer):
    def update(self, state):
        print(f"Observer received: {state}")
    """, language="python")

# ==================== TAB 6: TESTING & DEBUGGING ====================
with tabs[5]:
    st.markdown("## 🧪 Testing & Debugging")
    
    st.markdown("### 1️⃣ Unit Testing")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Testing Principles:</strong><br>
        • Write tests before code (TDD - Test Driven Development)<br>
        • Test one thing at a time<br>
        • Use descriptive test names<br>
        • Aim for high code coverage (>80%)<br>
        • Automate testing in CI/CD pipeline
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
import unittest

class Calculator:
    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        \"\"\"Run before each test\"\"\"
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        result = self.calc.add(3, 5)
        self.assertEqual(result, 8)
    
    def test_add_negative_numbers(self):
        result = self.calc.add(-3, -5)
        self.assertEqual(result, -8)
    
    def test_divide_normal(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5.0)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
    
    def tearDown(self):
        \"\"\"Run after each test\"\"\"
        pass

# Run tests
if __name__ == '__main__':
    unittest.main()
    """, language="python")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Debugging Techniques")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Print Debugging:**
        ```python
        def buggy_function(x):
            print(f"Input: {x}")
            result = x * 2
            print(f"Result: {result}")
            return result
        ```
        
        **Assert Statements:**
        ```python
        def divide(a, b):
            assert b != 0, "Divisor cannot be zero"
            return a / b
        ```
        """)
    
    with col2:
        st.markdown("""
        **Using Debugger (pdb):**
        ```python
        import pdb

        def complex_function(data):
            pdb.set_trace()  # Breakpoint
            processed = process_data(data)
            return processed
        ```
        
        **Logging:**
        ```python
        import logging

        logging.basicConfig(level=logging.DEBUG)
        logger = logging.getLogger(__name__)

        def process(data):
            logger.debug(f"Processing: {data}")
            logger.info("Process complete")
        ```
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Common Bug Patterns")
    
    st.markdown("""
    <div class="example-box">
        <strong>Off-by-One Errors:</strong><br>
        ```python
        # Wrong
        for i in range(len(arr) - 1):  # Misses last element
            print(arr[i])
        
        # Correct
        for i in range(len(arr)):
            print(arr[i])
        ```
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="example-box">
        <strong>Mutable Default Arguments:</strong><br>
        ```python
        # Wrong - list is shared across calls
        def append_to(element, to=[]):
            to.append(element)
            return to
        
        # Correct
        def append_to(element, to=None):
            if to is None:
                to = []
            to.append(element)
            return to
        ```
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: ADVANCED TOPICS ====================
with tabs[6]:
    st.markdown("## 🚀 Advanced Topics")
    
    st.markdown("### 1️⃣ Memory Management")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Memory Concepts:</strong><br>
        • <strong>Stack:</strong> Fast, automatic memory (local variables)<br>
        • <strong>Heap:</strong> Manual memory allocation (dynamic objects)<br>
        • <strong>Garbage Collection:</strong> Automatic memory reclamation<br>
        • <strong>Memory Leaks:</strong> Unreleased memory causing issues
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
# Python Memory Management
import sys

# Check object size
x = [1, 2, 3, 4, 5]
print(f"Size of list: {sys.getsizeof(x)} bytes")

# Reference counting
import gc
gc.get_count()  # Get garbage collector stats

# Context managers for resource management
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Usage
with FileManager('data.txt', 'w') as f:
    f.write('Hello, World!')
# File automatically closed
    """, language="python")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Parallel Programming Basics")
    
    st.code("""
# Threading for I/O-bound tasks
import threading
import time

def worker(name, delay):
    print(f"{name} starting")
    time.sleep(delay)
    print(f"{name} finished")

# Create threads
threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Thread-{i}", i+1))
    threads.append(t)
    t.start()

# Wait for all threads
for t in threads:
    t.join()

# Multiprocessing for CPU-bound tasks
from multiprocessing import Pool

def square(x):
    return x * x

if __name__ == '__main__':
    with Pool(4) as p:
        results = p.map(square, range(10))
        print(results)
    """, language="python")
    
    st.markdown("---")
    st.markdown("### 3️⃣ Generators and Iterators")
    
    st.code("""
# Generator function - memory efficient
def fibonacci_generator(n):
    \"\"\"Generate Fibonacci numbers up to n\"\"\"
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Usage
for num in fibonacci_generator(10):
    print(num, end=' ')

# Generator expression
squares = (x**2 for x in range(1000000))  # Memory efficient
# vs
squares_list = [x**2 for x in range(1000000)]  # Uses lots of memory

# Custom iterator
class Countdown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

# Usage
for num in Countdown(5):
    print(num)  # 5, 4, 3, 2, 1
    """, language="python")
    
    st.markdown("---")
    st.markdown("### 4️⃣ Metaclasses and Decorators")
    
    st.code("""
# Advanced decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Prints 3 times

# Class decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Database initialized")

# Metaclass example
class Meta(type):
    def __new__(cls, name, bases, dct):
        # Add timestamp to all classes
        import time
        dct['created_at'] = time.time()
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.created_at)
    """, language="python")

# ==================== TAB 8: BEST PRACTICES ====================
with tabs[7]:
    st.markdown("## 💡 Best Practices")
    
    st.markdown("### 1️⃣ SOLID Principles")
    
    st.markdown("""
    <div class="algorithm-box">
        <strong>S - Single Responsibility Principle</strong><br>
        A class should have only one reason to change.
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
# Bad - Multiple responsibilities
class User:
    def __init__(self, name):
        self.name = name
    
    def save_to_database(self):
        # Database logic
        pass
    
    def send_email(self):
        # Email logic
        pass

# Good - Separated concerns
class User:
    def __init__(self, name):
        self.name = name

class UserRepository:
    def save(self, user):
        # Database logic
        pass

class EmailService:
    def send(self, user, message):
        # Email logic
        pass
    """, language="python")
    
    st.markdown("""
    <div class="algorithm-box">
        <strong>O - Open/Closed Principle</strong><br>
        Open for extension, closed for modification.
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
# Bad - Need to modify class for new shapes
class AreaCalculator:
    def calculate(self, shape):
        if shape.type == 'circle':
            return 3.14 * shape.radius ** 2
        elif shape.type == 'rectangle':
            return shape.width * shape.height

# Good - Extensible without modification
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    """, language="python")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Clean Code Principles")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Meaningful Names:**
        ```python
        # Bad
        def calc(x, y):
            return x + y
        
        # Good
        def calculate_total_price(base_price, tax):
            return base_price + tax
        ```
        
        **Small Functions:**
        ```python
        # Functions should do ONE thing
        def process_order(order):
            validate_order(order)
            calculate_total(order)
            apply_discount(order)
            save_to_database(order)
        ```
        """)
    
    with col2:
        st.markdown("""
        **Avoid Magic Numbers:**
        ```python
        # Bad
        if age > 18:
            allow_access()
        
        # Good
        LEGAL_AGE = 18
        if age > LEGAL_AGE:
            allow_access()
        ```
        
        **DRY (Don't Repeat Yourself):**
        ```python
        # Extract common logic
        def validate_email(email):
            return '@' in email and '.' in email
        
        def validate_user(user):
            return validate_email(user.email)
        ```
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Code Documentation")
    
    st.code("""
def binary_search(arr: list[int], target: int) -> int:
    \"\"\"
    Perform binary search on a sorted array.
    
    Args:
        arr: Sorted list of integers to search
        target: Integer value to find
    
    Returns:
        Index of target if found, -1 otherwise
    
    Raises:
        ValueError: If arr is not sorted
    
    Examples:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search([1, 2, 3, 4, 5], 6)
        -1
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    \"\"\"
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
    """, language="python")
    
    st.markdown("---")
    st.markdown("### 4️⃣ Error Handling")
    
    st.code("""
# Specific exceptions
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError:
        print("Invalid types for division")
        return None
    else:
        return result
    finally:
        print("Division operation completed")

# Custom exceptions
class InvalidInputError(Exception):
    \"\"\"Raised when input validation fails\"\"\"
    pass

def process_age(age):
    if age < 0:
        raise InvalidInputError("Age cannot be negative")
    if age > 150:
        raise InvalidInputError("Age seems unrealistic")
    return age

# Context managers for cleanup
from contextlib import contextmanager

@contextmanager
def database_connection(db_name):
    conn = connect_to_database(db_name)
    try:
        yield conn
    finally:
        conn.close()
    """, language="python")

# ==================== TAB 9: PRACTICE PROBLEMS ====================
with tabs[8]:
    st.markdown("## 🧮 Practice Problems")
    
    st.markdown("""
    <div class="practice-box">
        <strong>💡 LeetCode-Style Problems</strong><br>
        Practice these problems to master programming concepts!
    </div>
    """, unsafe_allow_html=True)
    
    problems = [
        {
            "title": "Problem 1: Two Sum",
            "difficulty": "Easy",
            "description": "Given an array of integers and a target, return indices of two numbers that add up to target.",
            "example": "Input: nums = [2,7,11,15], target = 9\nOutput: [0,1]\nExplanation: nums[0] + nums[1] = 2 + 7 = 9",
            "hint": "Use a hash map to store complements",
            "solution": """
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Time: O(n), Space: O(n)
            """
        },
        {
            "title": "Problem 2: Valid Parentheses",
            "difficulty": "Easy",
            "description": "Given a string containing '(', ')', '{', '}', '[', ']', determine if the input string is valid.",
            "example": "Input: s = '({[]})'\nOutput: True\n\nInput: s = '([)]'\nOutput: False",
            "hint": "Use a stack to track opening brackets",
            "solution": """
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    
    return not stack

# Time: O(n), Space: O(n)
            """
        },
        {
            "title": "Problem 3: Reverse Linked List",
            "difficulty": "Medium",
            "description": "Reverse a singly linked list.",
            "example": "Input: 1 -> 2 -> 3 -> 4 -> 5\nOutput: 5 -> 4 -> 3 -> 2 -> 1",
            "hint": "Use three pointers: prev, current, next",
            "solution": """
def reverse_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

# Time: O(n), Space: O(1)
            """
        },
        {
            "title": "Problem 4: Maximum Subarray (Kadane's Algorithm)",
            "difficulty": "Medium",
            "description": "Find the contiguous subarray with the largest sum.",
            "example": "Input: [-2,1,-3,4,-1,2,1,-5,4]\nOutput: 6\nExplanation: [4,-1,2,1] has the largest sum = 6",
            "hint": "Keep track of current sum and maximum sum",
            "solution": """
def max_subarray(nums):
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Time: O(n), Space: O(1)
            """
        },
        {
            "title": "Problem 5: Longest Palindromic Substring",
            "difficulty": "Hard",
            "description": "Find the longest palindromic substring in a string.",
            "example": "Input: s = 'babad'\nOutput: 'bab' or 'aba'",
            "hint": "Expand around center for each position",
            "solution": """
def longest_palindrome(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    start = end = 0
    for i in range(len(s)):
        len1 = expand_around_center(i, i)      # Odd length
        len2 = expand_around_center(i, i + 1)  # Even length
        max_len = max(len1, len2)
        
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    return s[start:end + 1]

# Time: O(n²), Space: O(1)
            """
        }
    ]
    
    for idx, problem in enumerate(problems, 1):
        with st.expander(f"📝 {problem['title']} - {problem['difficulty']}", expanded=False):
            st.markdown(f"**Description:** {problem['description']}")
            st.markdown(f"**Example:**\n```\n{problem['example']}\n```")
            
            if st.button(f"Show Hint", key=f"hint_prob_{idx}"):
                st.info(f"💡 {problem['hint']}")
            
            if st.button(f"Show Solution", key=f"sol_prob_{idx}"):
                st.code(problem['solution'], language="python")

# ==================== TAB 10: COMPLEXITY ANALYSIS ====================
with tabs[9]:
    st.markdown("## 📊 Complexity Analysis")
    
    st.markdown("### 1️⃣ Big O Notation")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Common Time Complexities (Best to Worst):</strong><br>
        • O(1) - Constant<br>
        • O(log n) - Logarithmic<br>
        • O(n) - Linear<br>
        • O(n log n) - Linearithmic<br>
        • O(n²) - Quadratic<br>
        • O(n³) - Cubic<br>
        • O(2ⁿ) - Exponential<br>
        • O(n!) - Factorial
    </div>
    """, unsafe_allow_html=True)
    
    # Complexity visualization
    st.markdown("#### 📈 Complexity Growth Comparison")
    
    n_values = list(range(1, 21))
    complexity_data = []
    
    for n in n_values:
        complexity_data.append({'n': n, 'O(1)': 1, 'type': 'O(1)'})
        complexity_data.append({'n': n, 'O(log n)': np.log2(n) if n > 0 else 0, 'type': 'O(log n)'})
        complexity_data.append({'n': n, 'O(n)': n, 'type': 'O(n)'})
        complexity_data.append({'n': n, 'O(n log n)': n * np.log2(n) if n > 0 else 0, 'type': 'O(n log n)'})
        complexity_data.append({'n': n, 'O(n²)': n**2, 'type': 'O(n²)'})
    
    df_complexity = pd.DataFrame(complexity_data)
    df_complexity['value'] = df_complexity.apply(lambda row: row[row['type']], axis=1)
    
    complexity_chart = alt.Chart(df_complexity).mark_line(strokeWidth=2).encode(
        x=alt.X('n:Q', title='Input Size (n)'),
        y=alt.Y('value:Q', title='Operations', scale=alt.Scale(type='log')),
        color=alt.Color('type:N', title='Complexity'),
        tooltip=['n', 'type', 'value']
    ).properties(
        width=700,
        height=400,
        title="Time Complexity Growth (Log Scale)"
    ).interactive()
    
    st.altair_chart(complexity_chart, use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Analyzing Code Complexity")
    
    st.code("""
# O(1) - Constant
def get_first_element(arr):
    return arr[0]  # Always one operation

# O(n) - Linear
def find_max(arr):
    max_val = arr[0]
    for num in arr:  # n iterations
        if num > max_val:
            max_val = num
    return max_val

# O(n²) - Quadratic
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):           # n iterations
        for j in range(n - i - 1):  # n iterations
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# O(log n) - Logarithmic
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:  # log n iterations
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# O(n log n) - Linearithmic
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])    # log n levels
    right = merge_sort(arr[mid:])
    return merge(left, right)        # n operations per level
    """, language="python")
    
    st.markdown("---")
    st.markdown("### 3️⃣ Space Complexity")
    
    st.markdown("""
    <div class="example-box">
        <strong>Space Complexity Examples:</strong>
    </div>
    """, unsafe_allow_html=True)
    
    st.code("""
# O(1) Space - Constant
def sum_array(arr):
    total = 0  # Only one variable
    for num in arr:
        total += num
    return total

# O(n) Space - Linear
def create_copy(arr):
    return arr.copy()  # New array of size n

# O(n) Space - Recursive call stack
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)  # n recursive calls on stack

# O(n²) Space - 2D array
def create_matrix(n):
    return [[0] * n for _ in range(n)]  # n x n matrix
    """, language="python")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE101 - Structured Programming</strong><br>
    <small>UTel University | Department of Computer Engineering</small>
</div>
""", unsafe_allow_html=True)
