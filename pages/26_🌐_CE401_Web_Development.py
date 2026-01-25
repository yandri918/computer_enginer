import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="CE401 - Web Development", page_icon="🌐", layout="wide")

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
        background: linear-gradient(135deg, #cffafe 0%, #a5f3fc 100%);
        border-left: 5px solid #06b6d4;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .frontend-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .backend-box {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .fullstack-box {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
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
    <div style="font-size: 1.2rem; opacity: 0.9;">CE401</div>
    <div class="course-title">Web Development</div>
    <div>🌐 3 Credits | Semester 7 | Full-Stack Development</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "7")
with col3:
    st.metric("Difficulty", "5/7")
with col4:
    st.metric("Hours/Week", "7")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "🎨 Frontend Fundamentals",
    "⚛️ React & Modern Frontend",
    "🔧 Backend Development",
    "🗄️ Databases & APIs",
    "🔐 Authentication & Security",
    "🚀 Deployment & DevOps",
    "🎯 Full-Stack Projects",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive study of modern web development covering frontend, backend, and full-stack technologies. Learn HTML5, 
        CSS3, JavaScript ES6+, React, Node.js, Express, databases (SQL and NoSQL), RESTful APIs, authentication, security, 
        and deployment. Emphasizes hands-on project development, responsive design, performance optimization, and industry 
        best practices. Students will build complete web applications from scratch and deploy them to production.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Build responsive websites with HTML5, CSS3, and JavaScript",
        "Develop modern frontend applications with React",
        "Create RESTful APIs with Node.js and Express",
        "Design and implement databases (PostgreSQL, MongoDB)",
        "Implement user authentication and authorization",
        "Deploy web applications to cloud platforms (Vercel, Heroku, AWS)",
        "Apply security best practices (XSS, CSRF, SQL injection prevention)",
        "Optimize web performance and SEO"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Frontend:**
        - HTML5 semantic elements
        - CSS3 (Flexbox, Grid, animations)
        - JavaScript ES6+ (async/await, modules)
        - React (hooks, context, routing)
        - State management (Redux, Zustand)
        
        **Backend:**
        - Node.js and npm
        - Express.js framework
        - RESTful API design
        - Middleware and error handling
        - File uploads and processing
        """)
    
    with col2:
        st.markdown("""
        **Database & Auth:**
        - PostgreSQL (relational)
        - MongoDB (NoSQL)
        - Prisma ORM
        - JWT authentication
        - OAuth 2.0 (Google, GitHub)
        
        **Deployment & Tools:**
        - Git and GitHub
        - Vercel, Netlify, Heroku
        - Docker containers
        - CI/CD pipelines
        - Performance monitoring
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Eloquent JavaScript", "author": "Marijn Haverbeke", "type": "JavaScript"},
        {"title": "You Don't Know JS", "author": "Kyle Simpson", "type": "JavaScript"},
        {"title": "React Documentation", "author": "React Team", "type": "React"},
        {"title": "Node.js Design Patterns", "author": "Mario Casciaro", "type": "Backend"}
    ]
    
    for resource in resources:
        title = resource['title']
        author = resource['author']
        rtype = resource['type']
        st.markdown(f"📖 **{title}** by {author} ({rtype})")

# ==================== TAB 2: FRONTEND FUNDAMENTALS ====================
with tabs[1]:
    st.markdown("## 🎨 Frontend Fundamentals")
    
    st.markdown("### 1️⃣ HTML5")
    
    st.markdown("""
    <div class="frontend-box">
        <strong>Semantic HTML:</strong><br>
        <pre>
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
    &lt;title&gt;My Website&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;header&gt;
        &lt;nav&gt;
            &lt;ul&gt;
                &lt;li&gt;&lt;a href="#home"&gt;Home&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#about"&gt;About&lt;/a&gt;&lt;/li&gt;
            &lt;/ul&gt;
        &lt;/nav&gt;
    &lt;/header&gt;
    
    &lt;main&gt;
        &lt;article&gt;
            &lt;h1&gt;Article Title&lt;/h1&gt;
            &lt;p&gt;Content here...&lt;/p&gt;
        &lt;/article&gt;
    &lt;/main&gt;
    
    &lt;footer&gt;
        &lt;p&gt;&copy; 2024 My Website&lt;/p&gt;
    &lt;/footer&gt;
&lt;/body&gt;
&lt;/html&gt;
        </pre><br>
        
        <strong>Key Elements:</strong><br>
        • &lt;header&gt;, &lt;nav&gt;, &lt;main&gt;, &lt;article&gt;, &lt;section&gt;, &lt;aside&gt;, &lt;footer&gt;<br>
        • &lt;figure&gt;, &lt;figcaption&gt; for images<br>
        • &lt;video&gt;, &lt;audio&gt; for media<br>
        • &lt;form&gt;, &lt;input&gt;, &lt;button&gt; for user input
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ CSS3")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Flexbox Layout:</strong><br>
        <pre>
.container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1rem;
}

.item {
    flex: 1;
    min-width: 200px;
}
        </pre><br>
        
        <strong>Grid Layout:</strong><br>
        <pre>
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
}
        </pre><br>
        
        <strong>Responsive Design:</strong><br>
        <pre>
/* Mobile first */
.container {
    padding: 1rem;
}

/* Tablet */
@media (min-width: 768px) {
    .container {
        padding: 2rem;
    }
}

/* Desktop */
@media (min-width: 1024px) {
    .container {
        padding: 3rem;
        max-width: 1200px;
        margin: 0 auto;
    }
}
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ JavaScript ES6+")
    
    st.markdown("""
    <div class="frontend-box">
        <strong>Modern JavaScript Features:</strong><br>
        <pre>
// Arrow functions
const add = (a, b) => a + b;

// Destructuring
const { name, age } = user;
const [first, second] = array;

// Spread operator
const newArray = [...oldArray, newItem];
const newObject = { ...oldObject, newProp: value };

// Template literals
const message = `Hello, ${name}!`;

// Async/await
async function fetchData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}

// Modules
export const myFunction = () => { };
import { myFunction } from './utils';

// Optional chaining
const value = user?.profile?.email;

// Nullish coalescing
const name = user.name ?? 'Guest';
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: REACT ====================
with tabs[2]:
    st.markdown("## ⚛️ React & Modern Frontend")
    
    st.markdown("### 1️⃣ React Basics")
    
    st.markdown("""
    <div class="fullstack-box">
        <strong>Functional Components & Hooks:</strong><br>
        <pre>
import React, { useState, useEffect } from 'react';

function Counter() {
    const [count, setCount] = useState(0);
    
    useEffect(() => {
        document.title = `Count: ${count}`;
    }, [count]);
    
    return (
        &lt;div&gt;
            &lt;p&gt;Count: {count}&lt;/p&gt;
            &lt;button onClick={() => setCount(count + 1)}&gt;
                Increment
            &lt;/button&gt;
        &lt;/div&gt;
    );
}

export default Counter;
        </pre><br>
        
        <strong>Common Hooks:</strong><br>
        • <strong>useState:</strong> State management<br>
        • <strong>useEffect:</strong> Side effects (API calls, subscriptions)<br>
        • <strong>useContext:</strong> Access context values<br>
        • <strong>useRef:</strong> DOM references and mutable values<br>
        • <strong>useMemo:</strong> Memoize expensive calculations<br>
        • <strong>useCallback:</strong> Memoize functions
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ React Router")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Client-Side Routing:</strong><br>
        <pre>
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';

function App() {
    return (
        &lt;BrowserRouter&gt;
            &lt;nav&gt;
                &lt;Link to="/"&gt;Home&lt;/Link&gt;
                &lt;Link to="/about"&gt;About&lt;/Link&gt;
                &lt;Link to="/users"&gt;Users&lt;/Link&gt;
            &lt;/nav&gt;
            
            &lt;Routes&gt;
                &lt;Route path="/" element={&lt;Home /&gt;} /&gt;
                &lt;Route path="/about" element={&lt;About /&gt;} /&gt;
                &lt;Route path="/users/:id" element={&lt;UserProfile /&gt;} /&gt;
            &lt;/Routes&gt;
        &lt;/BrowserRouter&gt;
    );
}
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ State Management")
    
    st.markdown("""
    <div class="fullstack-box">
        <strong>Context API:</strong><br>
        <pre>
// Create context
const UserContext = React.createContext();

// Provider
function App() {
    const [user, setUser] = useState(null);
    
    return (
        &lt;UserContext.Provider value={{ user, setUser }}&gt;
            &lt;Dashboard /&gt;
        &lt;/UserContext.Provider&gt;
    );
}

// Consumer
function Dashboard() {
    const { user } = useContext(UserContext);
    return &lt;div&gt;Welcome, {user?.name}&lt;/div&gt;;
}
        </pre><br>
        
        <strong>Redux (for complex apps):</strong><br>
        • Centralized state store<br>
        • Actions and reducers<br>
        • Redux Toolkit for simplified setup<br>
        • DevTools for debugging
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: BACKEND ====================
with tabs[3]:
    st.markdown("## 🔧 Backend Development")
    
    st.markdown("### 1️⃣ Node.js & Express")
    
    st.markdown("""
    <div class="backend-box">
        <strong>Basic Express Server:</strong><br>
        <pre>
const express = require('express');
const app = express();

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Routes
app.get('/', (req, res) => {
    res.json({ message: 'Hello World' });
});

app.get('/users/:id', (req, res) => {
    const { id } = req.params;
    res.json({ userId: id });
});

app.post('/users', (req, res) => {
    const { name, email } = req.body;
    // Save to database
    res.status(201).json({ id: 1, name, email });
});

// Error handling
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ error: 'Something went wrong!' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ RESTful API Design")
    
    st.markdown("""
    <div class="theory-box">
        <strong>REST Principles:</strong><br><br>
        
        <strong>HTTP Methods:</strong><br>
        • <strong>GET:</strong> Retrieve resources<br>
        • <strong>POST:</strong> Create new resources<br>
        • <strong>PUT:</strong> Update entire resource<br>
        • <strong>PATCH:</strong> Partial update<br>
        • <strong>DELETE:</strong> Remove resource<br><br>
        
        <strong>Status Codes:</strong><br>
        • <strong>200 OK:</strong> Successful GET, PUT, PATCH<br>
        • <strong>201 Created:</strong> Successful POST<br>
        • <strong>204 No Content:</strong> Successful DELETE<br>
        • <strong>400 Bad Request:</strong> Invalid input<br>
        • <strong>401 Unauthorized:</strong> Authentication required<br>
        • <strong>403 Forbidden:</strong> No permission<br>
        • <strong>404 Not Found:</strong> Resource doesn't exist<br>
        • <strong>500 Internal Server Error:</strong> Server error<br><br>
        
        <strong>URL Structure:</strong><br>
        • /api/users (collection)<br>
        • /api/users/123 (specific resource)<br>
        • /api/users/123/posts (nested resource)<br>
        • Use nouns, not verbs<br>
        • Use plural for collections
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Middleware")
    
    st.markdown("""
    <div class="backend-box">
        <strong>Custom Middleware:</strong><br>
        <pre>
// Logging middleware
const logger = (req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();
};

// Authentication middleware
const authenticate = (req, res, next) => {
    const token = req.headers.authorization?.split(' ')[1];
    
    if (!token) {
        return res.status(401).json({ error: 'No token provided' });
    }
    
    try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET);
        req.user = decoded;
        next();
    } catch (error) {
        res.status(401).json({ error: 'Invalid token' });
    }
};

// Apply middleware
app.use(logger);
app.use('/api/protected', authenticate);
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: DATABASES ====================
with tabs[4]:
    st.markdown("## 🗄️ Databases & APIs")
    
    st.markdown("### 1️⃣ PostgreSQL with Prisma")
    
    st.markdown("""
    <div class="fullstack-box">
        <strong>Prisma Schema:</strong><br>
        <pre>
// schema.prisma
datasource db {
    provider = "postgresql"
    url      = env("DATABASE_URL")
}

generator client {
    provider = "prisma-client-js"
}

model User {
    id        Int      @id @default(autoincrement())
    email     String   @unique
    name      String?
    posts     Post[]
    createdAt DateTime @default(now())
}

model Post {
    id        Int      @id @default(autoincrement())
    title     String
    content   String?
    published Boolean  @default(false)
    author    User     @relation(fields: [authorId], references: [id])
    authorId  Int
    createdAt DateTime @default(now())
}
        </pre><br>
        
        <strong>Using Prisma Client:</strong><br>
        <pre>
const { PrismaClient } = require('@prisma/client');
const prisma = new PrismaClient();

// Create user
const user = await prisma.user.create({
    data: {
        email: 'alice@example.com',
        name: 'Alice',
    },
});

// Find users
const users = await prisma.user.findMany({
    include: { posts: true },
});

// Update user
const updated = await prisma.user.update({
    where: { id: 1 },
    data: { name: 'Alice Smith' },
});

// Delete user
await prisma.user.delete({
    where: { id: 1 },
});
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ MongoDB with Mongoose")
    
    st.markdown("""
    <div class="backend-box">
        <strong>Mongoose Schema:</strong><br>
        <pre>
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
    email: {
        type: String,
        required: true,
        unique: true,
    },
    name: String,
    password: {
        type: String,
        required: true,
    },
    posts: [{
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Post',
    }],
}, { timestamps: true });

const User = mongoose.model('User', userSchema);

// Create user
const user = await User.create({
    email: 'alice@example.com',
    name: 'Alice',
    password: hashedPassword,
});

// Find users
const users = await User.find().populate('posts');

// Update user
await User.findByIdAndUpdate(userId, { name: 'Alice Smith' });

// Delete user
await User.findByIdAndDelete(userId);
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: AUTHENTICATION ====================
with tabs[5]:
    st.markdown("## 🔐 Authentication & Security")
    
    st.markdown("### 1️⃣ JWT Authentication")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Login & Token Generation:</strong><br>
        <pre>
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Register
app.post('/api/register', async (req, res) => {
    const { email, password } = req.body;
    
    // Hash password
    const hashedPassword = await bcrypt.hash(password, 10);
    
    // Save user
    const user = await prisma.user.create({
        data: { email, password: hashedPassword },
    });
    
    res.status(201).json({ message: 'User created' });
});

// Login
app.post('/api/login', async (req, res) => {
    const { email, password } = req.body;
    
    // Find user
    const user = await prisma.user.findUnique({
        where: { email },
    });
    
    if (!user) {
        return res.status(401).json({ error: 'Invalid credentials' });
    }
    
    // Verify password
    const valid = await bcrypt.compare(password, user.password);
    
    if (!valid) {
        return res.status(401).json({ error: 'Invalid credentials' });
    }
    
    // Generate JWT
    const token = jwt.sign(
        { userId: user.id, email: user.email },
        process.env.JWT_SECRET,
        { expiresIn: '7d' }
    );
    
    res.json({ token, user: { id: user.id, email: user.email } });
});
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Security Best Practices")
    
    st.markdown("""
    <div class="fullstack-box">
        <strong>Common Vulnerabilities:</strong><br><br>
        
        <strong>XSS (Cross-Site Scripting):</strong><br>
        • Sanitize user input<br>
        • Use Content Security Policy (CSP)<br>
        • Escape HTML in templates<br><br>
        
        <strong>CSRF (Cross-Site Request Forgery):</strong><br>
        • Use CSRF tokens<br>
        • SameSite cookie attribute<br>
        • Verify origin header<br><br>
        
        <strong>SQL Injection:</strong><br>
        • Use parameterized queries<br>
        • ORM (Prisma, Sequelize)<br>
        • Input validation<br><br>
        
        <strong>Best Practices:</strong><br>
        • HTTPS only<br>
        • Environment variables for secrets<br>
        • Rate limiting<br>
        • Helmet.js for security headers<br>
        • Regular dependency updates<br>
        • Input validation (Joi, Zod)
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: DEPLOYMENT ====================
with tabs[6]:
    st.markdown("## 🚀 Deployment & DevOps")
    
    st.markdown("### 1️⃣ Deployment Platforms")
    
    platforms_data = {
        'Platform': ['Vercel', 'Netlify', 'Heroku', 'AWS', 'Railway'],
        'Best For': ['Next.js, React', 'Static sites, JAMstack', 'Full-stack apps', 'Enterprise, scalable', 'Full-stack, databases'],
        'Free Tier': ['Yes', 'Yes', 'Limited', 'Limited', 'Yes'],
        'Difficulty': ['Easy', 'Easy', 'Medium', 'Hard', 'Easy']
    }
    
    df_platforms = pd.DataFrame(platforms_data)
    st.dataframe(df_platforms, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Docker")
    
    st.markdown("""
    <div class="backend-box">
        <strong>Dockerfile:</strong><br>
        <pre>
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .

EXPOSE 3000

CMD ["node", "server.js"]
        </pre><br>
        
        <strong>docker-compose.yml:</strong><br>
        <pre>
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: PROJECTS ====================
with tabs[7]:
    st.markdown("## 🎯 Full-Stack Projects")
    
    projects = [
        {
            "title": "Project 1: Blog Platform",
            "description": "Full-stack blog with authentication and CRUD operations",
            "features": """
**Features:**
- User registration and login (JWT)
- Create, read, update, delete posts
- Rich text editor (TinyMCE or Quill)
- Image uploads (Cloudinary)
- Comments system
- Search and filtering
- Responsive design

**Tech Stack:**
- Frontend: React, React Router, Tailwind CSS
- Backend: Node.js, Express
- Database: PostgreSQL with Prisma
- Auth: JWT, bcrypt
- Deployment: Vercel (frontend), Railway (backend)
            """,
            "implementation": """
**Implementation Steps:**

1. **Setup:**
   - Initialize React app with Vite
   - Setup Express server
   - Configure Prisma with PostgreSQL

2. **Backend API:**
   - User authentication endpoints
   - Post CRUD endpoints
   - Comment endpoints
   - File upload endpoint

3. **Frontend:**
   - Login/Register pages
   - Dashboard with post list
   - Post editor with rich text
   - Post detail page with comments
   - User profile page

4. **Deployment:**
   - Deploy frontend to Vercel
   - Deploy backend to Railway
   - Setup environment variables
   - Configure CORS

**GitHub:** Example repository with complete code
            """
        },
        {
            "title": "Project 2: E-Commerce Store",
            "description": "Online store with shopping cart and payment integration",
            "features": """
**Features:**
- Product catalog with categories
- Shopping cart (local storage)
- User authentication
- Order management
- Payment integration (Stripe)
- Admin dashboard
- Email notifications

**Tech Stack:**
- Frontend: React, Redux, Material-UI
- Backend: Node.js, Express
- Database: MongoDB with Mongoose
- Payment: Stripe API
- Email: SendGrid
- Deployment: Heroku
            """,
            "implementation": """
**Key Components:**

**1. Product Management:**
```javascript
// Product model
const productSchema = new mongoose.Schema({
    name: String,
    description: String,
    price: Number,
    category: String,
    image: String,
    stock: Number,
});
```

**2. Shopping Cart:**
```javascript
// Redux slice for cart
const cartSlice = createSlice({
    name: 'cart',
    initialState: { items: [] },
    reducers: {
        addToCart: (state, action) => {
            const item = state.items.find(i => i.id === action.payload.id);
            if (item) {
                item.quantity += 1;
            } else {
                state.items.push({ ...action.payload, quantity: 1 });
            }
        },
        removeFromCart: (state, action) => {
            state.items = state.items.filter(i => i.id !== action.payload);
        },
    },
});
```

**3. Stripe Payment:**
```javascript
// Backend payment endpoint
app.post('/api/create-payment-intent', async (req, res) => {
    const { amount } = req.body;
    
    const paymentIntent = await stripe.paymentIntents.create({
        amount: amount * 100, // cents
        currency: 'usd',
    });
    
    res.json({ clientSecret: paymentIntent.client_secret });
});
```
            """
        }
    ]
    
    for idx, project in enumerate(projects, 1):
        with st.expander(f"📝 {project['title']}", expanded=False):
            st.markdown(f"**Description:** {project['description']}")
            st.markdown(project['features'])
            
            if st.button(f"Show Implementation", key=f"proj_{idx}"):
                st.markdown("### Implementation")
                st.markdown(project['implementation'])

# ==================== TAB 9: YOUTUBE ====================
with tabs[8]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning Web Development</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {"title": "HTML & CSS Full Course", "channel": "freeCodeCamp.org", "url": "https://www.youtube.com/watch?v=mU6anWqZJcc", "description": "Complete HTML/CSS tutorial", "duration": "~11 hours"},
        {"title": "JavaScript for Beginners", "channel": "Programming with Mosh", "url": "https://www.youtube.com/watch?v=W6NZfCO5SIk", "description": "JavaScript fundamentals", "duration": "~1 hour"},
        {"title": "React Tutorial", "channel": "Net Ninja", "url": "https://www.youtube.com/playlist?list=PL4cUxeGkcC9gZD-Tvwfod2gaISzfRiP9d", "description": "React for beginners", "duration": "Playlist"}
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
        {"title": "Full Stack MERN", "channel": "Traversy Media", "url": "https://www.youtube.com/watch?v=-0exw-9YJBo", "description": "Complete MERN stack app", "duration": "~7 hours"},
        {"title": "Node.js & Express", "channel": "freeCodeCamp.org", "url": "https://www.youtube.com/watch?v=Oe421EPjeBE", "description": "Backend development", "duration": "~8 hours"},
        {"title": "Next.js Tutorial", "channel": "Codevolution", "url": "https://www.youtube.com/playlist?list=PLC3y8-rFHvwgC9mj0qv972IO5DmD-H0ZH", "description": "Next.js framework", "duration": "Playlist"}
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
        {"title": "Advanced React Patterns", "channel": "Jack Herrington", "url": "https://www.youtube.com/c/JackHerrington", "description": "Advanced React techniques", "duration": "Channel"},
        {"title": "System Design", "channel": "Gaurav Sen", "url": "https://www.youtube.com/c/GauravSensei", "description": "Web architecture", "duration": "Channel"},
        {"title": "Web Performance", "channel": "Google Chrome Developers", "url": "https://www.youtube.com/c/GoogleChromeDevelopers", "description": "Performance optimization", "duration": "Channel"}
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
    <div class="theory-box">
        <strong>Recommended Learning Path:</strong><br>
        1. Master HTML, CSS, JavaScript fundamentals<br>
        2. Learn React and component-based architecture<br>
        3. Study Node.js and Express for backend<br>
        4. Understand databases (SQL and NoSQL)<br>
        5. Implement authentication and security<br>
        6. Build full-stack projects<br>
        7. Learn deployment and DevOps<br>
        8. Optimize performance and SEO<br><br>
        
        <strong>Essential Tools:</strong><br>
        • <strong>Code Editor:</strong> VS Code with extensions<br>
        • <strong>Version Control:</strong> Git and GitHub<br>
        • <strong>Package Manager:</strong> npm or yarn<br>
        • <strong>API Testing:</strong> Postman or Insomnia<br>
        • <strong>Database Tools:</strong> pgAdmin, MongoDB Compass<br>
        • <strong>Browser DevTools:</strong> Chrome, Firefox<br><br>
        
        <strong>Career Paths:</strong><br>
        • Frontend Developer<br>
        • Backend Developer<br>
        • Full-Stack Developer<br>
        • React Developer<br>
        • Node.js Developer
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE401 - Web Development</strong><br>
    <small>UTel University | Computer Engineering Program</small>
</div>
""", unsafe_allow_html=True)
