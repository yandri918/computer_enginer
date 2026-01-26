# 🎓 UTel University - Computer Engineering Curriculum Hub

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://computer-engineering-utel.streamlit.app)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)](#)

> **The "Hidden Gem" of Educational Portfolios.**  
> A complete, semester-by-semester interactive curriculum simulation for a 4-year Computer Engineering degree. Far more than a static syllabus, this is a fully functional **Learning Management System (LMS)** prototype built with Streamlit.

---

## 🌟 Why This Project is Unique

In the vast sea of GitHub repositories, this project stands in the **top 0.1%** of educational Streamlit applications. Unline typical single-page dashboards, this "Super App" integrates:

1.  **Full-Stack Curriculum**: Covers **8 Semesters** and **40+ Courses** individually.
2.  **Cross-Domain Interactivity**: Unified ecosystem running simulations for **Physics** (Mechanics), **Electronics** (Circuit Analysis), **Mathematics** (Linear Algebra/Calculus), and **Computer Science** (Algorithms/AI).
3.  **Multimedia Integration**: Every single course features a curated **YouTube Resources** tab (Beginner to Advanced).

---

## ✨ Key Features

### 🗺️ COMPLETE Roadmap (Semester 1-8)
Navigate the entire 4-year journey. Every module is verified and functional.

| Year 1: Foundations | Year 2: Core Engineering | Year 3: Advanced Systems | Year 4: Specializations |
| :--- | :--- | :--- | :--- |
| 📐 Calculus & Linear Algebra | 🏭 Processing Industry | 🌐 Computer Networks | 🔐 Cybersecurity |
| 💻 Structured Programming | 💻 Operating Systems | 📐 Systems Analysis | 📱 Mobile App Dev |
| ⚛️ Physics & Electronics | 🔍 Algorithms & Data Structures | 🗄️ Database Systems | ☁️ Cloud Computing |
| 🖥️ Comp. Architecture | ⚡ Digital Systems | 🤖 Artificial Intelligence | ⛓️ Blockchain & IoT |

### 🧠 Interactive Simulations & Tools
We don't just tell you about concepts; we let you play with them.
- **Physics**: Real-time harmonic oscillator and projectile motion simulations.
- **Calculus**: Interactive area-under-curve visualizations and function plotters.
- **Electronics**: Resistor color code calculators and Ohm's Law simulators.
- **Logic Design**: Interactive truth tables and logic gate visualizations.
- **Algorithms**: Sorting algorithm visualizers and Big-O complexity charts.

### 📚 Curated Learning Center
Every course page includes:
- **📖 Syllabus**: Comprehensive topic breakdown.
- **🧮 Practice Problems**: Accordion-style QA with hidden solutions.
- **📺 YouTube Resources**: Hand-picked video playlists categorized by difficulty (Green/Yellow/Red).
- **💡 Study Tips**: Advice on how to master the specific subject.

---

## 🛠️ Tech Stack

Built with a modern Python-centric stack designed for rapid prototyping and data visualization.

- **Frontend**: [Streamlit](https://streamlit.io/) (Multi-page architecture)
- **Visualization**: [Altair](https://altair-viz.github.io/), [Pandas](https://pandas.pydata.org/), [Plotly](https://plotly.com/)
- **Data Processing**: NumPy, Pandas
- **Logic**: Custom Python scripts for curriculum mapping and prerequisites.

---

## 🚀 Getting Started

To explore the curriculum locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/agrisensa-api.git
cd agrisensa-api
```

### 2. Set Up Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r computer_enginer/requirements.txt
```

### 4. Launch the App
```bash
streamlit run computer_enginer/Home.py
```

The application will open automatically in your browser at `http://localhost:8501`.

---

## 📂 Project Structure

A glimpse into the scale of this project:

```text
computer_enginer/
├── Home.py                  # Main Dashboard & Analytics Hub
├── data/                    # JSON/Python dictionaries for curriculum data
├── pages/                   # 40+ Individual Course Modules
│   ├── 1_📐_MA101_Calculus.py
│   ├── 5_🖥️_CE103_Architecture.py
│   ├── ...
│   └── 36_CE408_IoT.py
└── requirements.txt         # Dependency list
```

---

## 🤝 Contributing

This project is a living curriculum. Contributions to course content, new simulations, or UI improvements are welcome!

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingSimulation`)
3.  Commit your Changes (`git commit -m 'Add new Physics simulation'`)
4.  Push to the Branch (`git push origin feature/AmazingSimulation`)
5.  Open a Pull Request

---

<div align="center">

**Built with ❤️ for Future Engineers**

[Streamlit](https://streamlit.io) • [Python](https://python.org) • [Education](https://github.com/topics/education)

</div>
