import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="CE201 - Object Oriented Programming", page_icon="💻", layout="wide")

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
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
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
        background: linear-gradient(135deg, #ecfeff 0%, #cffafe 100%);
        border-left: 5px solid #06b6d4;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .principle-box {
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
    
    .pattern-box {
        background: linear-gradient(135deg, #f3e8ff 0%, #e9d5ff 100%);
        border-left: 5px solid #8b5cf6;
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
    <div style="font-size: 1.2rem; opacity: 0.9;">CE201</div>
    <div class="course-title">Object Oriented Programming</div>
    <div>💻 4 Credits | Semester 3 | Programming</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "4")
with col2:
    st.metric("Semester", "3")
with col3:
    st.metric("Difficulty", "4/7")
with col4:
    st.metric("Hours/Week", "7")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "🎯 OOP Principles",
    "🏗️ Classes & Objects",
    "🔄 Inheritance",
    "🎭 Polymorphism",
    "📦 Encapsulation",
    "🎨 Design Patterns",
    "⚡ SOLID Principles",
    "🎯 Practice Problems",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive study of object-oriented programming paradigm. Covers fundamental OOP concepts including 
        classes, objects, inheritance, polymorphism, and encapsulation. Emphasizes design patterns, SOLID principles, 
        and best practices for building maintainable, scalable software systems. Uses Java/C++ as primary languages 
        with exposure to modern OOP features.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Master core OOP concepts and principles",
        "Design and implement class hierarchies",
        "Apply inheritance and polymorphism effectively",
        "Implement common design patterns",
        "Follow SOLID principles for clean code",
        "Use UML for system design",
        "Write maintainable and testable code",
        "Understand modern OOP features (generics, lambdas)"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Fundamentals:**
        - Classes and objects
        - Constructors and destructors
        - Access modifiers
        - Methods and properties
        - Static members
        
        **Core Concepts:**
        - Inheritance (single, multiple)
        - Polymorphism (compile-time, runtime)
        - Encapsulation and abstraction
        - Interfaces and abstract classes
        - Composition vs inheritance
        """)
    
    with col2:
        st.markdown("""
        **Advanced Topics:**
        - Design patterns (GoF)
        - SOLID principles
        - Dependency injection
        - Generics and templates
        - Exception handling
        
        **Modern Features:**
        - Lambda expressions
        - Streams and functional programming
        - Reflection and annotations
        - Memory management
        - Unit testing (JUnit, Google Test)
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Head First Design Patterns", "author": "Freeman & Robson", "type": "Textbook"},
        {"title": "Clean Code", "author": "Robert C. Martin", "type": "Best Practices"},
        {"title": "Effective Java", "author": "Joshua Bloch", "type": "Java"},
        {"title": "Design Patterns: Elements of Reusable OO Software", "author": "Gang of Four", "type": "Classic"}
    ]
    
    for resource in resources:
        st.markdown(f"📖 **{resource['title']}** by {resource['author']} ({resource['type']})")

# ==================== TAB 2: OOP PRINCIPLES ====================
with tabs[1]:
    st.markdown("## 🎯 OOP Principles")
    
    st.markdown("### 1️⃣ The Four Pillars of OOP")
    
    st.markdown("""
    <div class="principle-box">
        <strong>1. Encapsulation:</strong><br>
        • Bundle data and methods that operate on that data<br>
        • Hide internal state and implementation details<br>
        • Expose only necessary interfaces<br>
        • Use access modifiers (private, protected, public)<br><br>
        
        <strong>2. Abstraction:</strong><br>
        • Hide complex implementation details<br>
        • Show only essential features<br>
        • Use abstract classes and interfaces<br>
        • Focus on "what" rather than "how"<br><br>
        
        <strong>3. Inheritance:</strong><br>
        • Create new classes from existing ones<br>
        • Reuse code and establish relationships<br>
        • Form "is-a" relationships<br>
        • Enable polymorphism<br><br>
        
        <strong>4. Polymorphism:</strong><br>
        • Objects of different types respond to same message<br>
        • Method overloading (compile-time)<br>
        • Method overriding (runtime)<br>
        • Interface implementation
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Benefits of OOP")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Code Organization:**
        - Modular structure
        - Clear separation of concerns
        - Easier to understand and maintain
        - Natural mapping to real-world
        """)
    
    with col2:
        st.markdown("""
        **Development Benefits:**
        - Code reusability
        - Easier testing and debugging
        - Scalability
        - Team collaboration
        """)

# ==================== TAB 3: CLASSES & OBJECTS ====================
with tabs[2]:
    st.markdown("## 🏗️ Classes & Objects")
    
    st.markdown("### 1️⃣ Class Definition")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Class:</strong> Blueprint or template for creating objects<br>
        <strong>Object:</strong> Instance of a class with specific values<br><br>
        
        <strong>Components:</strong><br>
        • <strong>Attributes/Fields:</strong> Data members (state)<br>
        • <strong>Methods:</strong> Functions (behavior)<br>
        • <strong>Constructors:</strong> Initialize objects<br>
        • <strong>Destructors:</strong> Clean up resources
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Java Example:**")
        st.code("""
public class Student {
    // Attributes
    private String name;
    private int id;
    private double gpa;
    
    // Constructor
    public Student(String name, int id) {
        this.name = name;
        this.id = id;
        this.gpa = 0.0;
    }
    
    // Methods
    public void setGPA(double gpa) {
        if (gpa >= 0.0 && gpa <= 4.0) {
            this.gpa = gpa;
        }
    }
    
    public double getGPA() {
        return this.gpa;
    }
    
    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("ID: " + id);
        System.out.println("GPA: " + gpa);
    }
}

// Usage
Student student = new Student("Alice", 12345);
student.setGPA(3.8);
student.displayInfo();
        """, language="java")
    
    with col2:
        st.markdown("**C++ Example:**")
        st.code("""
class Student {
private:
    std::string name;
    int id;
    double gpa;
    
public:
    // Constructor
    Student(std::string n, int i) 
        : name(n), id(i), gpa(0.0) {}
    
    // Destructor
    ~Student() {
        // Cleanup if needed
    }
    
    // Methods
    void setGPA(double g) {
        if (g >= 0.0 && g <= 4.0) {
            gpa = g;
        }
    }
    
    double getGPA() const {
        return gpa;
    }
    
    void displayInfo() const {
        std::cout << "Name: " << name << std::endl;
        std::cout << "ID: " << id << std::endl;
        std::cout << "GPA: " << gpa << std::endl;
    }
};

// Usage
Student student("Alice", 12345);
student.setGPA(3.8);
student.displayInfo();
        """, language="cpp")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Access Modifiers")
    
    st.markdown("""
    <div class="principle-box">
        <strong>Access Control:</strong><br><br>
        
        • <strong>private:</strong> Accessible only within the class<br>
        • <strong>protected:</strong> Accessible within class and subclasses<br>
        • <strong>public:</strong> Accessible from anywhere<br>
        • <strong>default/package (Java):</strong> Accessible within same package<br><br>
        
        <strong>Best Practice:</strong> Keep fields private, provide public getters/setters
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: INHERITANCE ====================
with tabs[3]:
    st.markdown("## 🔄 Inheritance")
    
    st.markdown("### 1️⃣ Inheritance Basics")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Inheritance:</strong> Mechanism to create new class from existing class<br><br>
        
        • <strong>Base/Parent/Super Class:</strong> Class being inherited from<br>
        • <strong>Derived/Child/Sub Class:</strong> Class that inherits<br>
        • <strong>Relationship:</strong> "is-a" relationship<br><br>
        
        <strong>Types:</strong><br>
        • <strong>Single:</strong> One parent class<br>
        • <strong>Multiple:</strong> Multiple parent classes (C++ only)<br>
        • <strong>Multilevel:</strong> Chain of inheritance<br>
        • <strong>Hierarchical:</strong> Multiple children from one parent<br>
        • <strong>Hybrid:</strong> Combination of above
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**Java Inheritance Example:**")
    st.code("""
// Base class
public class Animal {
    protected String name;
    protected int age;
    
    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    public void eat() {
        System.out.println(name + " is eating");
    }
    
    public void sleep() {
        System.out.println(name + " is sleeping");
    }
}

// Derived class
public class Dog extends Animal {
    private String breed;
    
    public Dog(String name, int age, String breed) {
        super(name, age);  // Call parent constructor
        this.breed = breed;
    }
    
    // Override parent method
    @Override
    public void eat() {
        System.out.println(name + " the dog is eating dog food");
    }
    
    // New method specific to Dog
    public void bark() {
        System.out.println(name + " says: Woof!");
    }
}

// Usage
Dog myDog = new Dog("Buddy", 3, "Golden Retriever");
myDog.eat();    // Calls overridden method
myDog.sleep();  // Calls inherited method
myDog.bark();   // Calls Dog-specific method
    """, language="java")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Method Overriding")
    
    st.markdown("""
    <div class="example-box">
        <strong>Method Overriding (Runtime Polymorphism):</strong><br>
        • Subclass provides specific implementation of parent method<br>
        • Same method signature as parent<br>
        • Uses @Override annotation (Java)<br>
        • Uses virtual keyword (C++)<br><br>
        
        <strong>Rules:</strong><br>
        • Must have same name, parameters, return type<br>
        • Cannot reduce visibility<br>
        • Cannot override final methods<br>
        • Cannot override static methods (can hide them)
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: POLYMORPHISM ====================
with tabs[4]:
    st.markdown("## 🎭 Polymorphism")
    
    st.markdown("### 1️⃣ Types of Polymorphism")
    
    st.markdown("""
    <div class="principle-box">
        <strong>1. Compile-Time Polymorphism (Static):</strong><br>
        • <strong>Method Overloading:</strong> Same name, different parameters<br>
        • <strong>Operator Overloading:</strong> Custom operators (C++)<br>
        • Resolved at compile time<br><br>
        
        <strong>2. Runtime Polymorphism (Dynamic):</strong><br>
        • <strong>Method Overriding:</strong> Subclass redefines parent method<br>
        • <strong>Interface Implementation:</strong> Multiple implementations<br>
        • Resolved at runtime using virtual dispatch
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Method Overloading Example")
    
    st.code("""
public class Calculator {
    // Overloaded methods - same name, different parameters
    
    public int add(int a, int b) {
        return a + b;
    }
    
    public double add(double a, double b) {
        return a + b;
    }
    
    public int add(int a, int b, int c) {
        return a + b + c;
    }
    
    public String add(String a, String b) {
        return a + b;
    }
}

// Usage
Calculator calc = new Calculator();
System.out.println(calc.add(5, 3));           // Calls int version
System.out.println(calc.add(5.5, 3.2));       // Calls double version
System.out.println(calc.add(1, 2, 3));        // Calls 3-parameter version
System.out.println(calc.add("Hello", "World")); // Calls String version
    """, language="java")
    
    st.markdown("---")
    st.markdown("### 3️⃣ Runtime Polymorphism Example")
    
    st.code("""
// Base class
abstract class Shape {
    abstract double area();
    abstract double perimeter();
}

// Derived classes
class Circle extends Shape {
    private double radius;
    
    public Circle(double radius) {
        this.radius = radius;
    }
    
    @Override
    double area() {
        return Math.PI * radius * radius;
    }
    
    @Override
    double perimeter() {
        return 2 * Math.PI * radius;
    }
}

class Rectangle extends Shape {
    private double width, height;
    
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }
    
    @Override
    double area() {
        return width * height;
    }
    
    @Override
    double perimeter() {
        return 2 * (width + height);
    }
}

// Polymorphic usage
Shape[] shapes = {
    new Circle(5.0),
    new Rectangle(4.0, 6.0)
};

for (Shape shape : shapes) {
    System.out.println("Area: " + shape.area());
    System.out.println("Perimeter: " + shape.perimeter());
}
    """, language="java")

# ==================== TAB 6: ENCAPSULATION ====================
with tabs[5]:
    st.markdown("## 📦 Encapsulation")
    
    st.markdown("### 1️⃣ Encapsulation Principles")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Encapsulation:</strong> Bundling data and methods, hiding internal details<br><br>
        
        <strong>Key Concepts:</strong><br>
        • <strong>Data Hiding:</strong> Make fields private<br>
        • <strong>Controlled Access:</strong> Use getters/setters<br>
        • <strong>Validation:</strong> Enforce business rules<br>
        • <strong>Flexibility:</strong> Change implementation without affecting clients<br><br>
        
        <strong>Benefits:</strong><br>
        • Increased security<br>
        • Better maintainability<br>
        • Loose coupling<br>
        • Easier testing
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**Encapsulation Example:**")
    st.code("""
public class BankAccount {
    // Private fields - hidden from outside
    private String accountNumber;
    private double balance;
    private String ownerName;
    
    // Constructor
    public BankAccount(String accountNumber, String ownerName) {
        this.accountNumber = accountNumber;
        this.ownerName = ownerName;
        this.balance = 0.0;
    }
    
    // Controlled access through public methods
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited: $" + amount);
        } else {
            System.out.println("Invalid deposit amount");
        }
    }
    
    public boolean withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawn: $" + amount);
            return true;
        } else {
            System.out.println("Insufficient funds or invalid amount");
            return false;
        }
    }
    
    // Getter - read-only access
    public double getBalance() {
        return balance;
    }
    
    // No setter for balance - can only change through deposit/withdraw
    
    public String getAccountInfo() {
        return "Account: " + accountNumber + ", Owner: " + ownerName;
    }
}

// Usage
BankAccount account = new BankAccount("123456", "Alice");
account.deposit(1000);
account.withdraw(200);
System.out.println("Balance: $" + account.getBalance());
// account.balance = 10000;  // ERROR: balance is private!
    """, language="java")

# ==================== TAB 7: DESIGN PATTERNS ====================
with tabs[6]:
    st.markdown("## 🎨 Design Patterns")
    
    st.markdown("### 1️⃣ Creational Patterns")
    
    st.markdown("""
    <div class="pattern-box">
        <strong>Singleton Pattern:</strong><br>
        Ensure a class has only one instance and provide global access<br><br>
        
        <strong>Factory Pattern:</strong><br>
        Create objects without specifying exact class<br><br>
        
        <strong>Builder Pattern:</strong><br>
        Construct complex objects step by step<br><br>
        
        <strong>Prototype Pattern:</strong><br>
        Create new objects by cloning existing ones
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**Singleton Example:**")
    st.code("""
public class Database {
    // Private static instance
    private static Database instance;
    
    // Private constructor prevents instantiation
    private Database() {
        // Initialize database connection
    }
    
    // Public static method to get instance
    public static Database getInstance() {
        if (instance == null) {
            synchronized (Database.class) {
                if (instance == null) {
                    instance = new Database();
                }
            }
        }
        return instance;
    }
    
    public void query(String sql) {
        System.out.println("Executing: " + sql);
    }
}

// Usage
Database db1 = Database.getInstance();
Database db2 = Database.getInstance();
// db1 and db2 refer to the same instance
    """, language="java")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Structural Patterns")
    
    st.markdown("""
    <div class="pattern-box">
        <strong>Adapter Pattern:</strong><br>
        Convert interface of a class into another interface<br><br>
        
        <strong>Decorator Pattern:</strong><br>
        Add new functionality to objects dynamically<br><br>
        
        <strong>Facade Pattern:</strong><br>
        Provide simplified interface to complex subsystem<br><br>
        
        <strong>Composite Pattern:</strong><br>
        Compose objects into tree structures
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Behavioral Patterns")
    
    st.markdown("""
    <div class="pattern-box">
        <strong>Observer Pattern:</strong><br>
        Define one-to-many dependency between objects<br><br>
        
        <strong>Strategy Pattern:</strong><br>
        Define family of algorithms, make them interchangeable<br><br>
        
        <strong>Command Pattern:</strong><br>
        Encapsulate request as an object<br><br>
        
        <strong>Iterator Pattern:</strong><br>
        Access elements sequentially without exposing structure
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: SOLID PRINCIPLES ====================
with tabs[7]:
    st.markdown("## ⚡ SOLID Principles")
    
    st.markdown("""
    <div class="principle-box">
        <h3>SOLID: Five Principles for Better OOP Design</h3>
        
        <strong>S - Single Responsibility Principle (SRP):</strong><br>
        A class should have only one reason to change<br>
        • Each class should have one job/responsibility<br>
        • Easier to understand and maintain<br><br>
        
        <strong>O - Open/Closed Principle (OCP):</strong><br>
        Open for extension, closed for modification<br>
        • Add new functionality without changing existing code<br>
        • Use inheritance and interfaces<br><br>
        
        <strong>L - Liskov Substitution Principle (LSP):</strong><br>
        Subtypes must be substitutable for their base types<br>
        • Derived classes should extend, not replace behavior<br>
        • Maintain behavioral compatibility<br><br>
        
        <strong>I - Interface Segregation Principle (ISP):</strong><br>
        Clients shouldn't depend on interfaces they don't use<br>
        • Many specific interfaces better than one general<br>
        • Avoid "fat" interfaces<br><br>
        
        <strong>D - Dependency Inversion Principle (DIP):</strong><br>
        Depend on abstractions, not concretions<br>
        • High-level modules shouldn't depend on low-level<br>
        • Both should depend on abstractions
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**SRP Example:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("❌ **Bad (Multiple Responsibilities):**")
        st.code("""
class User {
    private String name;
    private String email;
    
    // User data management
    public void setName(String name) {
        this.name = name;
    }
    
    // Email sending (different responsibility!)
    public void sendEmail(String message) {
        // Send email logic
    }
    
    // Database operations (another responsibility!)
    public void saveToDatabase() {
        // Save logic
    }
}
        """, language="java")
    
    with col2:
        st.markdown("✅ **Good (Single Responsibility):**")
        st.code("""
class User {
    private String name;
    private String email;
    
    public void setName(String name) {
        this.name = name;
    }
    // Only user data management
}

class EmailService {
    public void sendEmail(User user, String msg) {
        // Email logic
    }
}

class UserRepository {
    public void save(User user) {
        // Database logic
    }
}
        """, language="java")

# ==================== TAB 9: PRACTICE PROBLEMS ====================
with tabs[8]:
    st.markdown("## 🎯 Practice Problems")
    
    problems = [
        {
            "title": "Problem 1: Library Management System",
            "question": "Design a library system with Book, Member, and Librarian classes. Implement borrowing and returning books.",
            "hint": "Use inheritance for different types of members (Student, Faculty). Consider encapsulation for book availability.",
            "solution": """
// Base class
abstract class LibraryMember {
    protected String id;
    protected String name;
    protected int maxBooks;
    
    public abstract boolean canBorrow();
}

// Derived classes
class Student extends LibraryMember {
    public Student(String id, String name) {
        this.id = id;
        this.name = name;
        this.maxBooks = 3;
    }
    
    @Override
    public boolean canBorrow() {
        return borrowedBooks.size() < maxBooks;
    }
}

class Faculty extends LibraryMember {
    public Faculty(String id, String name) {
        this.id = id;
        this.name = name;
        this.maxBooks = 10;
    }
    
    @Override
    public boolean canBorrow() {
        return borrowedBooks.size() < maxBooks;
    }
}

// Book class
class Book {
    private String isbn;
    private String title;
    private boolean available;
    
    public Book(String isbn, String title) {
        this.isbn = isbn;
        this.title = title;
        this.available = true;
    }
    
    public boolean isAvailable() {
        return available;
    }
    
    public void borrow() {
        available = false;
    }
    
    public void returnBook() {
        available = true;
    }
}
            """
        },
        {
            "title": "Problem 2: Shape Calculator",
            "question": "Create a shape hierarchy with Circle, Rectangle, and Triangle. Calculate area and perimeter polymorphically.",
            "hint": "Use abstract base class with abstract methods for area() and perimeter()",
            "solution": """
abstract class Shape {
    abstract double area();
    abstract double perimeter();
    
    public void display() {
        System.out.println("Area: " + area());
        System.out.println("Perimeter: " + perimeter());
    }
}

class Circle extends Shape {
    private double radius;
    
    public Circle(double radius) {
        this.radius = radius;
    }
    
    @Override
    double area() {
        return Math.PI * radius * radius;
    }
    
    @Override
    double perimeter() {
        return 2 * Math.PI * radius;
    }
}

class Rectangle extends Shape {
    private double width, height;
    
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }
    
    @Override
    double area() {
        return width * height;
    }
    
    @Override
    double perimeter() {
        return 2 * (width + height);
    }
}

// Polymorphic usage
Shape[] shapes = {
    new Circle(5),
    new Rectangle(4, 6)
};

for (Shape s : shapes) {
    s.display();
}
            """
        }
    ]
    
    for idx, problem in enumerate(problems, 1):
        with st.expander(f"📝 {problem['title']}", expanded=False):
            st.markdown(f"**Question:** {problem['question']}")
            
            if st.button(f"Show Hint", key=f"hint_{idx}"):
                st.info(f"💡 {problem['hint']}")
            
            if st.button(f"Show Solution", key=f"sol_{idx}"):
                st.code(problem['solution'], language="java")

# ==================== TAB 10: YOUTUBE RESOURCES ====================
with tabs[9]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning Object-Oriented Programming</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {
            "title": "Object Oriented Programming (OOP) in Java",
            "channel": "Programming with Mosh",
            "url": "https://www.youtube.com/watch?v=pTB0EiLXUC8",
            "description": "Complete OOP tutorial covering all fundamental concepts",
            "duration": "~1 hour"
        },
        {
            "title": "Java OOP Basics",
            "channel": "freeCodeCamp.org",
            "url": "https://www.youtube.com/watch?v=A74TOX803D0",
            "description": "Comprehensive Java OOP course for beginners",
            "duration": "~2 hours"
        },
        {
            "title": "OOP Concepts in Java",
            "channel": "Telusko",
            "url": "https://www.youtube.com/playlist?list=PLsyeobzWxl7pe_IiTfNyr55kwJPWbgxB5",
            "description": "Step-by-step playlist covering OOP fundamentals",
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
            "title": "Design Patterns in Object Oriented Programming",
            "channel": "Christopher Okhravi",
            "url": "https://www.youtube.com/playlist?list=PLrhzvIcii6GNjpARdnO4ueTUAVR9eMBpc",
            "description": "Complete design patterns series with clear explanations",
            "duration": "Playlist"
        },
        {
            "title": "SOLID Principles",
            "channel": "Web Dev Simplified",
            "url": "https://www.youtube.com/watch?v=_jDNAf3CzeY",
            "description": "Clear explanation of SOLID principles with examples",
            "duration": "30 min"
        },
        {
            "title": "Advanced Java Programming",
            "channel": "Cave of Programming",
            "url": "https://www.youtube.com/playlist?list=PL9DF6E4B45C36D411",
            "description": "Advanced OOP concepts and best practices",
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
            "title": "Clean Code - Uncle Bob",
            "channel": "Uncle Bob Martin",
            "url": "https://www.youtube.com/watch?v=7EmboKQH8lM",
            "description": "Clean code principles and best practices",
            "duration": "Full Course"
        },
        {
            "title": "Refactoring Guru - Design Patterns",
            "channel": "Refactoring Guru",
            "url": "https://refactoring.guru/design-patterns",
            "description": "Comprehensive design patterns resource (website + videos)",
            "duration": "Reference"
        },
        {
            "title": "Java Design Patterns and Architecture",
            "channel": "Derek Banas",
            "url": "https://www.youtube.com/playlist?list=PLF206E906175C7E07",
            "description": "Complete design patterns implementation in Java",
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
    
    # Language-Specific
    st.markdown("### 💻 Language-Specific Resources")
    
    lang_resources = [
        {
            "title": "C++ OOP Tutorial",
            "channel": "The Cherno",
            "url": "https://www.youtube.com/playlist?list=PLlrATfBNZ98dudnM48yfGUldqGD0S4FFb",
            "description": "Professional C++ OOP series",
            "duration": "Playlist"
        },
        {
            "title": "Python OOP Tutorial",
            "channel": "Corey Schafer",
            "url": "https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc",
            "description": "Clear Python OOP explanations",
            "duration": "Playlist"
        },
        {
            "title": "C# OOP Fundamentals",
            "channel": "IAmTimCorey",
            "url": "https://www.youtube.com/watch?v=N4HYbJjiJhY",
            "description": "Complete C# OOP course",
            "duration": "~3 hours"
        }
    ]
    
    for resource in lang_resources:
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
        1. Master basic OOP concepts (classes, objects, inheritance)<br>
        2. Practice with small projects (library system, bank account)<br>
        3. Learn design patterns (start with Singleton, Factory, Observer)<br>
        4. Study SOLID principles and apply to your code<br>
        5. Read "Clean Code" and "Design Patterns" books<br>
        6. Contribute to open-source projects<br><br>
        
        <strong>Practice Resources:</strong><br>
        • <strong>LeetCode OOP:</strong> https://leetcode.com/tag/object-oriented-design/<br>
        • <strong>Refactoring Guru:</strong> https://refactoring.guru/<br>
        • <strong>SourceMaking:</strong> https://sourcemaking.com/design_patterns<br>
        • <strong>Java Design Patterns:</strong> https://github.com/iluwatar/java-design-patterns
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE201 - Object Oriented Programming</strong><br>
    <small>UTel University | Department of Computer Engineering</small>
</div>
""", unsafe_allow_html=True)
