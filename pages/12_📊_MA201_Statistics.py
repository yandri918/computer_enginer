import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from scipy import stats

st.set_page_config(page_title="MA201 - Statistics and Probability", page_icon="📊", layout="wide")

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
        background: linear-gradient(135deg, #a855f7 0%, #9333ea 100%);
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
        border-left: 5px solid #a855f7;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .formula-box {
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
    
    .distribution-box {
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
    <div style="font-size: 1.2rem; opacity: 0.9;">MA201</div>
    <div class="course-title">Statistics and Probability</div>
    <div>📊 3 Credits | Semester 3 | Mathematics</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "3")
with col3:
    st.metric("Difficulty", "4/7")
with col4:
    st.metric("Hours/Week", "5")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "📈 Descriptive Statistics",
    "🎲 Probability Theory",
    "📊 Distributions",
    "🔬 Hypothesis Testing",
    "📉 Regression Analysis",
    "🎯 Bayesian Statistics",
    "💻 Applications",
    "🎯 Practice Problems",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive study of statistics and probability theory with applications to data science and machine learning. 
        Covers descriptive statistics, probability distributions, statistical inference, hypothesis testing, regression analysis, 
        and Bayesian methods. Emphasizes both theoretical foundations and practical applications using computational tools.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Analyze and visualize data using descriptive statistics",
        "Calculate probabilities using probability theory",
        "Work with common probability distributions",
        "Perform hypothesis testing and confidence intervals",
        "Apply regression analysis to real-world data",
        "Understand Bayesian inference principles",
        "Use statistical software (Python, R) for analysis",
        "Interpret statistical results correctly"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Fundamentals:**
        - Descriptive statistics
        - Data visualization
        - Measures of central tendency
        - Measures of dispersion
        - Correlation and covariance
        
        **Probability:**
        - Sample spaces and events
        - Conditional probability
        - Bayes' theorem
        - Random variables
        - Expected value and variance
        """)
    
    with col2:
        st.markdown("""
        **Inference:**
        - Sampling distributions
        - Central Limit Theorem
        - Confidence intervals
        - Hypothesis testing
        - p-values and significance
        
        **Advanced Topics:**
        - Linear regression
        - Multiple regression
        - ANOVA
        - Chi-square tests
        - Bayesian inference
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Introduction to Probability", "author": "Blitzstein & Hwang", "type": "Textbook"},
        {"title": "Statistical Inference", "author": "Casella & Berger", "type": "Graduate"},
        {"title": "Think Stats", "author": "Allen Downey", "type": "Free Book"},
        {"title": "Bayesian Data Analysis", "author": "Gelman et al.", "type": "Advanced"}
    ]
    
    for resource in resources:
        st.markdown(f"📖 **{resource['title']}** by {resource['author']} ({resource['type']})")

# ==================== TAB 2: DESCRIPTIVE STATISTICS ====================
with tabs[1]:
    st.markdown("## 📈 Descriptive Statistics")
    
    st.markdown("### 1️⃣ Measures of Central Tendency")
    
    st.markdown("""
    <div class="formula-box">
        <strong>Mean (Average):</strong><br>
        μ = (Σx) / n = (x₁ + x₂ + ... + xₙ) / n<br><br>
        
        <strong>Median:</strong><br>
        Middle value when data is sorted<br>
        • Odd n: value at position (n+1)/2<br>
        • Even n: average of values at n/2 and (n/2)+1<br><br>
        
        <strong>Mode:</strong><br>
        Most frequently occurring value(s)<br><br>
        
        <strong>When to use:</strong><br>
        • Mean: Symmetric distributions, no outliers<br>
        • Median: Skewed distributions, outliers present<br>
        • Mode: Categorical data, multimodal distributions
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive Statistics Calculator
    st.markdown("#### 🧮 Interactive Statistics Calculator")
    
    data_input = st.text_area(
        "Enter data (comma-separated):",
        "12, 15, 18, 20, 22, 25, 28, 30, 35, 40",
        height=100
    )
    
    try:
        data = [float(x.strip()) for x in data_input.split(',')]
        data_array = np.array(data)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Mean", f"{np.mean(data_array):.2f}")
            st.metric("Median", f"{np.median(data_array):.2f}")
        
        with col2:
            st.metric("Std Dev", f"{np.std(data_array, ddof=1):.2f}")
            st.metric("Variance", f"{np.var(data_array, ddof=1):.2f}")
        
        with col3:
            st.metric("Min", f"{np.min(data_array):.2f}")
            st.metric("Max", f"{np.max(data_array):.2f}")
        
        # Visualization
        df = pd.DataFrame({'value': data_array})
        
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X('value:Q', bin=alt.Bin(maxbins=10), title='Value'),
            y=alt.Y('count()', title='Frequency')
        ).properties(
            width=600,
            height=300,
            title="Histogram"
        )
        
        mean_line = alt.Chart(pd.DataFrame({'mean': [np.mean(data_array)]})).mark_rule(color='red', size=2).encode(
            x='mean:Q'
        )
        
        st.altair_chart(chart + mean_line, use_container_width=True)
        
    except:
        st.error("Please enter valid numeric data separated by commas")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Measures of Dispersion")
    
    st.markdown("""
    <div class="formula-box">
        <strong>Range:</strong><br>
        Range = Max - Min<br><br>
        
        <strong>Variance (σ²):</strong><br>
        σ² = Σ(x - μ)² / n (population)<br>
        s² = Σ(x - x̄)² / (n-1) (sample)<br><br>
        
        <strong>Standard Deviation (σ):</strong><br>
        σ = √(variance)<br><br>
        
        <strong>Coefficient of Variation:</strong><br>
        CV = (σ / μ) × 100%
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: PROBABILITY THEORY ====================
with tabs[2]:
    st.markdown("## 🎲 Probability Theory")
    
    st.markdown("### 1️⃣ Basic Probability")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Probability Axioms:</strong><br>
        1. P(A) ≥ 0 for any event A<br>
        2. P(S) = 1 (sample space)<br>
        3. P(A ∪ B) = P(A) + P(B) if A and B are mutually exclusive<br><br>
        
        <strong>Key Formulas:</strong><br>
        • <strong>Complement:</strong> P(A') = 1 - P(A)<br>
        • <strong>Addition Rule:</strong> P(A ∪ B) = P(A) + P(B) - P(A ∩ B)<br>
        • <strong>Multiplication Rule:</strong> P(A ∩ B) = P(A) × P(B|A)<br>
        • <strong>Independence:</strong> P(A ∩ B) = P(A) × P(B)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Conditional Probability & Bayes' Theorem")
    
    st.markdown("""
    <div class="formula-box">
        <strong>Conditional Probability:</strong><br>
        P(A|B) = P(A ∩ B) / P(B)<br><br>
        
        <strong>Bayes' Theorem:</strong><br>
        P(A|B) = [P(B|A) × P(A)] / P(B)<br><br>
        
        <strong>Law of Total Probability:</strong><br>
        P(B) = Σ P(B|Aᵢ) × P(Aᵢ)
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive Bayes' Theorem Calculator
    st.markdown("#### 🧮 Bayes' Theorem Calculator")
    
    st.markdown("**Medical Test Example:**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        disease_rate = st.slider("Disease Prevalence P(D)", 0.0, 1.0, 0.01, 0.001, 
                                 help="Probability of having the disease")
        sensitivity = st.slider("Test Sensitivity P(+|D)", 0.0, 1.0, 0.95, 0.01,
                               help="True positive rate")
    
    with col2:
        specificity = st.slider("Test Specificity P(-|~D)", 0.0, 1.0, 0.90, 0.01,
                               help="True negative rate")
    
    # Calculate
    false_positive_rate = 1 - specificity
    p_positive = (sensitivity * disease_rate) + (false_positive_rate * (1 - disease_rate))
    p_disease_given_positive = (sensitivity * disease_rate) / p_positive if p_positive > 0 else 0
    
    st.markdown(f"""
    **Results:**
    - P(Test Positive) = {p_positive:.4f}
    - **P(Disease | Test Positive) = {p_disease_given_positive:.4f} ({p_disease_given_positive*100:.2f}%)**
    """)
    
    if p_disease_given_positive < disease_rate * 10:
        st.warning("⚠️ Note: Even with a positive test, the probability of having the disease may be low due to low prevalence!")

# ==================== TAB 4: DISTRIBUTIONS ====================
with tabs[3]:
    st.markdown("## 📊 Probability Distributions")
    
    st.markdown("### 1️⃣ Discrete Distributions")
    
    st.markdown("""
    <div class="distribution-box">
        <strong>Binomial Distribution:</strong><br>
        P(X = k) = C(n,k) × p^k × (1-p)^(n-k)<br>
        • n trials, probability p of success<br>
        • E[X] = np, Var(X) = np(1-p)<br><br>
        
        <strong>Poisson Distribution:</strong><br>
        P(X = k) = (λ^k × e^(-λ)) / k!<br>
        • λ = average rate<br>
        • E[X] = λ, Var(X) = λ<br><br>
        
        <strong>Geometric Distribution:</strong><br>
        P(X = k) = (1-p)^(k-1) × p<br>
        • Number of trials until first success
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive Distribution Visualizer
    st.markdown("#### 📊 Binomial Distribution Visualizer")
    
    col1, col2 = st.columns(2)
    with col1:
        n = st.slider("Number of trials (n)", 1, 50, 20)
    with col2:
        p = st.slider("Probability of success (p)", 0.0, 1.0, 0.5, 0.05)
    
    x = np.arange(0, n+1)
    pmf = stats.binom.pmf(x, n, p)
    
    df_binom = pd.DataFrame({'k': x, 'P(X=k)': pmf})
    
    chart = alt.Chart(df_binom).mark_bar().encode(
        x=alt.X('k:Q', title='Number of Successes (k)'),
        y=alt.Y('P(X=k):Q', title='Probability'),
        tooltip=['k', 'P(X=k)']
    ).properties(
        width=600,
        height=300,
        title=f"Binomial Distribution: n={n}, p={p}"
    )
    
    st.altair_chart(chart, use_container_width=True)
    
    st.markdown(f"**Expected Value:** E[X] = {n*p:.2f}")
    st.markdown(f"**Standard Deviation:** σ = {np.sqrt(n*p*(1-p)):.2f}")
    
    st.markdown("---")
    st.markdown("### 2️⃣ Continuous Distributions")
    
    st.markdown("""
    <div class="distribution-box">
        <strong>Normal Distribution:</strong><br>
        f(x) = (1/(σ√(2π))) × e^(-(x-μ)²/(2σ²))<br>
        • μ = mean, σ = standard deviation<br>
        • 68-95-99.7 rule (empirical rule)<br><br>
        
        <strong>Exponential Distribution:</strong><br>
        f(x) = λe^(-λx) for x ≥ 0<br>
        • Models time between events<br>
        • E[X] = 1/λ, Var(X) = 1/λ²<br><br>
        
        <strong>Uniform Distribution:</strong><br>
        f(x) = 1/(b-a) for a ≤ x ≤ b<br>
        • E[X] = (a+b)/2
    </div>
    """, unsafe_allow_html=True)
    
    # Normal Distribution Visualizer
    st.markdown("#### 📈 Normal Distribution Visualizer")
    
    col1, col2 = st.columns(2)
    with col1:
        mu = st.slider("Mean (μ)", -10.0, 10.0, 0.0, 0.5)
    with col2:
        sigma = st.slider("Std Dev (σ)", 0.1, 5.0, 1.0, 0.1)
    
    x_norm = np.linspace(mu - 4*sigma, mu + 4*sigma, 200)
    pdf = stats.norm.pdf(x_norm, mu, sigma)
    
    df_norm = pd.DataFrame({'x': x_norm, 'f(x)': pdf})
    
    chart_norm = alt.Chart(df_norm).mark_line(color='purple', strokeWidth=2).encode(
        x=alt.X('x:Q', title='x'),
        y=alt.Y('f(x):Q', title='Probability Density')
    ).properties(
        width=600,
        height=300,
        title=f"Normal Distribution: μ={mu}, σ={sigma}"
    )
    
    st.altair_chart(chart_norm, use_container_width=True)

# ==================== TAB 5: HYPOTHESIS TESTING ====================
with tabs[4]:
    st.markdown("## 🔬 Hypothesis Testing")
    
    st.markdown("### 1️⃣ Hypothesis Testing Framework")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Steps:</strong><br>
        1. State null hypothesis (H₀) and alternative (H₁)<br>
        2. Choose significance level (α, typically 0.05)<br>
        3. Calculate test statistic<br>
        4. Find p-value or critical value<br>
        5. Make decision: reject or fail to reject H₀<br><br>
        
        <strong>Types of Errors:</strong><br>
        • <strong>Type I Error (α):</strong> Reject H₀ when it's true (false positive)<br>
        • <strong>Type II Error (β):</strong> Fail to reject H₀ when it's false (false negative)<br>
        • <strong>Power:</strong> 1 - β (probability of correctly rejecting false H₀)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Common Tests")
    
    st.markdown("""
    <div class="formula-box">
        <strong>Z-Test (known σ):</strong><br>
        z = (x̄ - μ₀) / (σ/√n)<br><br>
        
        <strong>t-Test (unknown σ):</strong><br>
        t = (x̄ - μ₀) / (s/√n)<br>
        df = n - 1<br><br>
        
        <strong>Two-Sample t-Test:</strong><br>
        t = (x̄₁ - x̄₂) / √(s₁²/n₁ + s₂²/n₂)<br><br>
        
        <strong>Chi-Square Test:</strong><br>
        χ² = Σ(Observed - Expected)² / Expected
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive t-Test Calculator
    st.markdown("#### 🧮 One-Sample t-Test Calculator")
    
    col1, col2 = st.columns(2)
    
    with col1:
        sample_mean = st.number_input("Sample Mean (x̄)", value=105.0)
        sample_std = st.number_input("Sample Std Dev (s)", value=15.0, min_value=0.1)
        sample_size = st.number_input("Sample Size (n)", value=30, min_value=2)
    
    with col2:
        null_mean = st.number_input("Null Hypothesis Mean (μ₀)", value=100.0)
        alpha = st.selectbox("Significance Level (α)", [0.01, 0.05, 0.10], index=1)
        tail_type = st.selectbox("Test Type", ["Two-tailed", "Right-tailed", "Left-tailed"])
    
    # Calculate t-statistic
    t_stat = (sample_mean - null_mean) / (sample_std / np.sqrt(sample_size))
    df = sample_size - 1
    
    if tail_type == "Two-tailed":
        p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df))
        critical_value = stats.t.ppf(1 - alpha/2, df)
    elif tail_type == "Right-tailed":
        p_value = 1 - stats.t.cdf(t_stat, df)
        critical_value = stats.t.ppf(1 - alpha, df)
    else:  # Left-tailed
        p_value = stats.t.cdf(t_stat, df)
        critical_value = -stats.t.ppf(1 - alpha, df)
    
    st.markdown(f"""
    **Results:**
    - t-statistic = {t_stat:.4f}
    - p-value = {p_value:.4f}
    - Critical value = ±{critical_value:.4f} (for α={alpha})
    - Degrees of freedom = {df}
    """)
    
    if p_value < alpha:
        st.success(f"✅ **Reject H₀** (p-value < α)")
        st.markdown("There is sufficient evidence to reject the null hypothesis.")
    else:
        st.info(f"❌ **Fail to reject H₀** (p-value ≥ α)")
        st.markdown("There is insufficient evidence to reject the null hypothesis.")

# ==================== TAB 6: REGRESSION ====================
with tabs[5]:
    st.markdown("## 📉 Regression Analysis")
    
    st.markdown("### 1️⃣ Simple Linear Regression")
    
    st.markdown("""
    <div class="formula-box">
        <strong>Model:</strong><br>
        y = β₀ + β₁x + ε<br><br>
        
        <strong>Least Squares Estimates:</strong><br>
        β₁ = Σ[(xᵢ - x̄)(yᵢ - ȳ)] / Σ(xᵢ - x̄)²<br>
        β₀ = ȳ - β₁x̄<br><br>
        
        <strong>R² (Coefficient of Determination):</strong><br>
        R² = 1 - (SSE / SST)<br>
        • Proportion of variance explained by model<br>
        • Range: 0 to 1 (higher is better)
    </div>
    """, unsafe_allow_html=True)
    
    # Interactive Regression Demo
    st.markdown("#### 📊 Interactive Linear Regression")
    
    # Generate sample data
    np.random.seed(42)
    n_points = st.slider("Number of data points", 10, 100, 50)
    noise_level = st.slider("Noise level", 0.0, 5.0, 1.0, 0.1)
    
    x_data = np.linspace(0, 10, n_points)
    y_true = 2 * x_data + 3
    y_data = y_true + np.random.normal(0, noise_level, n_points)
    
    # Calculate regression
    slope, intercept = np.polyfit(x_data, y_data, 1)
    y_pred = slope * x_data + intercept
    
    # Calculate R²
    ss_res = np.sum((y_data - y_pred) ** 2)
    ss_tot = np.sum((y_data - np.mean(y_data)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)
    
    # Create visualization
    df_scatter = pd.DataFrame({'x': x_data, 'y': y_data, 'y_pred': y_pred})
    
    scatter = alt.Chart(df_scatter).mark_circle(size=60).encode(
        x=alt.X('x:Q', title='X'),
        y=alt.Y('y:Q', title='Y'),
        tooltip=['x', 'y']
    )
    
    line = alt.Chart(df_scatter).mark_line(color='red', strokeWidth=2).encode(
        x='x:Q',
        y='y_pred:Q'
    )
    
    chart_reg = (scatter + line).properties(
        width=600,
        height=400,
        title="Linear Regression"
    )
    
    st.altair_chart(chart_reg, use_container_width=True)
    
    st.markdown(f"""
    **Regression Equation:** y = {intercept:.2f} + {slope:.2f}x
    
    **Model Statistics:**
    - Slope (β₁) = {slope:.4f}
    - Intercept (β₀) = {intercept:.4f}
    - R² = {r_squared:.4f}
    """)

# ==================== TAB 7: BAYESIAN STATISTICS ====================
with tabs[6]:
    st.markdown("## 🎯 Bayesian Statistics")
    
    st.markdown("### 1️⃣ Bayesian Inference")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Bayes' Theorem for Parameters:</strong><br>
        P(θ|data) = [P(data|θ) × P(θ)] / P(data)<br><br>
        
        <strong>Components:</strong><br>
        • <strong>Prior P(θ):</strong> Belief about parameter before seeing data<br>
        • <strong>Likelihood P(data|θ):</strong> Probability of data given parameter<br>
        • <strong>Posterior P(θ|data):</strong> Updated belief after seeing data<br>
        • <strong>Evidence P(data):</strong> Normalizing constant<br><br>
        
        <strong>Key Concept:</strong><br>
        Posterior ∝ Likelihood × Prior
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Bayesian vs Frequentist")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Frequentist:**
        - Parameters are fixed, unknown
        - Probability = long-run frequency
        - Confidence intervals
        - p-values for hypothesis testing
        - No prior information used
        """)
    
    with col2:
        st.markdown("""
        **Bayesian:**
        - Parameters are random variables
        - Probability = degree of belief
        - Credible intervals
        - Posterior probabilities
        - Incorporates prior knowledge
        """)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Conjugate Priors")
    
    st.markdown("""
    <div class="formula-box">
        <strong>Beta-Binomial (proportion estimation):</strong><br>
        • Prior: Beta(α, β)<br>
        • Likelihood: Binomial(n, p)<br>
        • Posterior: Beta(α + successes, β + failures)<br><br>
        
        <strong>Normal-Normal (mean estimation):</strong><br>
        • Prior: Normal(μ₀, σ₀²)<br>
        • Likelihood: Normal(μ, σ²)<br>
        • Posterior: Normal (weighted average of prior and data)
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: APPLICATIONS ====================
with tabs[7]:
    st.markdown("## 💻 Real-World Applications")
    
    st.markdown("### 1️⃣ Data Science & Machine Learning")
    
    st.markdown("""
    <div class="example-box">
        <strong>Feature Engineering:</strong><br>
        • Normalization and standardization<br>
        • Handling outliers using statistical methods<br>
        • Feature selection using correlation<br><br>
        
        <strong>Model Evaluation:</strong><br>
        • Cross-validation<br>
        • Confidence intervals for predictions<br>
        • Hypothesis testing for model comparison<br><br>
        
        <strong>Probabilistic Models:</strong><br>
        • Naive Bayes classifier<br>
        • Gaussian Mixture Models<br>
        • Bayesian networks
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ A/B Testing")
    
    st.markdown("""
    <div class="example-box">
        <strong>Process:</strong><br>
        1. Define metric (conversion rate, click-through rate)<br>
        2. Determine sample size (power analysis)<br>
        3. Randomly assign users to A or B<br>
        4. Collect data<br>
        5. Perform two-sample test<br>
        6. Make decision based on statistical significance<br><br>
        
        <strong>Example:</strong><br>
        • H₀: Conversion rate A = Conversion rate B<br>
        • H₁: Conversion rate A ≠ Conversion rate B<br>
        • Use two-proportion z-test
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Quality Control")
    
    st.markdown("""
    <div class="example-box">
        <strong>Statistical Process Control:</strong><br>
        • Control charts (X-bar, R-charts)<br>
        • Capability analysis (Cp, Cpk)<br>
        • Acceptance sampling<br><br>
        
        <strong>Six Sigma:</strong><br>
        • DMAIC methodology<br>
        • Process capability<br>
        • Defect rate: 3.4 per million
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 9: PRACTICE PROBLEMS ====================
with tabs[8]:
    st.markdown("## 🎯 Practice Problems")
    
    problems = [
        {
            "title": "Problem 1: Probability Calculation",
            "question": "A box contains 5 red balls and 3 blue balls. If you draw 2 balls without replacement, what is the probability that both are red?",
            "hint": "Use conditional probability: P(2nd red | 1st red) × P(1st red)",
            "solution": """
**Solution:**

P(1st red) = 5/8
P(2nd red | 1st red) = 4/7

P(both red) = (5/8) × (4/7) = 20/56 = 5/14 ≈ 0.357

**Answer:** 5/14 or approximately 35.7%
            """
        },
        {
            "title": "Problem 2: Hypothesis Testing",
            "question": "A manufacturer claims their light bulbs last 1000 hours on average. A sample of 36 bulbs has mean 980 hours and std dev 50 hours. Test at α=0.05.",
            "hint": "Use one-sample t-test. H₀: μ = 1000, H₁: μ ≠ 1000",
            "solution": """
**Solution:**

Given: x̄ = 980, s = 50, n = 36, μ₀ = 1000, α = 0.05

t = (980 - 1000) / (50/√36) = -20 / 8.33 = -2.40

df = 35
Critical value (two-tailed): ±2.030

Since |t| = 2.40 > 2.030, reject H₀

**Conclusion:** There is sufficient evidence to reject the manufacturer's claim.
            """
        },
        {
            "title": "Problem 3: Regression Analysis",
            "question": "Given data points: (1,3), (2,5), (3,7), (4,9), (5,11). Find the regression line and R².",
            "hint": "Use least squares formulas for slope and intercept",
            "solution": """
**Solution:**

x̄ = 3, ȳ = 7

β₁ = Σ[(xᵢ - x̄)(yᵢ - ȳ)] / Σ(xᵢ - x̄)²
   = 20 / 10 = 2

β₀ = ȳ - β₁x̄ = 7 - 2(3) = 1

**Regression line:** y = 1 + 2x

Since all points lie on the line:
**R² = 1.0** (perfect fit)
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
        <p>High-quality video tutorials for learning Statistics and Probability</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {
            "title": "Statistics Fundamentals",
            "channel": "StatQuest with Josh Starmer",
            "url": "https://www.youtube.com/playlist?list=PLblh5JKOoLUK0FLuzwntyYI10UQFUhsY9",
            "description": "Clear, intuitive explanations of statistics concepts",
            "duration": "Playlist"
        },
        {
            "title": "Probability and Statistics",
            "channel": "Khan Academy",
            "url": "https://www.youtube.com/playlist?list=PLC58778F28211FA19",
            "description": "Complete course from basics to advanced topics",
            "duration": "Full Course"
        },
        {
            "title": "Introduction to Probability",
            "channel": "MIT OpenCourseWare",
            "url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP60hI9ATjSFgLZpbNJ7myAg6",
            "description": "MIT 6.041 - Rigorous probability theory",
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
            "title": "Statistical Inference",
            "channel": "Brandon Foltz",
            "url": "https://www.youtube.com/playlist?list=PLIeGtxpvyG-LoKUpV0fSY8BGKIMIdmfCi",
            "description": "Hypothesis testing, confidence intervals, regression",
            "duration": "Playlist"
        },
        {
            "title": "Bayesian Statistics",
            "channel": "Arxiv Insights",
            "url": "https://www.youtube.com/watch?v=HZGCoVF3YvM",
            "description": "Introduction to Bayesian thinking",
            "duration": "20 min"
        },
        {
            "title": "Regression Analysis",
            "channel": "zedstatistics",
            "url": "https://www.youtube.com/playlist?list=PLTNMv857s9WUI1Nz4SssXDKAELESXz-bi",
            "description": "Complete regression analysis course",
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
            "title": "Mathematical Statistics",
            "channel": "Harvard Statistics",
            "url": "https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo",
            "description": "Stat 110 - Probability theory and statistics",
            "duration": "Full Course"
        },
        {
            "title": "Bayesian Data Analysis",
            "channel": "Richard McElreath",
            "url": "https://www.youtube.com/playlist?list=PLDcUM9US4XdMROZ57-OIRtIK0aOynbgZN",
            "description": "Statistical Rethinking - Modern Bayesian methods",
            "duration": "Full Course"
        },
        {
            "title": "Machine Learning & Statistics",
            "channel": "mathematicalmonk",
            "url": "https://www.youtube.com/playlist?list=PLD0F06AA0D2E8FFBA",
            "description": "Mathematical foundations for ML",
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
    
    # Tools & Software
    st.markdown("### 🛠️ Tools & Software")
    
    tools_resources = [
        {
            "title": "Python for Statistics",
            "channel": "Corey Schafer",
            "url": "https://www.youtube.com/watch?v=Iq9DzN6mvYA",
            "description": "Using NumPy, Pandas, and SciPy for statistics",
            "duration": "~1 hour"
        },
        {
            "title": "R Programming for Statistics",
            "channel": "MarinStatsLectures",
            "url": "https://www.youtube.com/playlist?list=PLqzoL9-eJTNBDdKgJgJzaQcY6OXmsXAHU",
            "description": "Complete R statistics course",
            "duration": "Playlist"
        },
        {
            "title": "Statistical Visualization",
            "channel": "Storytelling with Data",
            "url": "https://www.youtube.com/c/storytellingwithdata",
            "description": "Effective data visualization techniques",
            "duration": "Channel"
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
        1. Master descriptive statistics and visualization<br>
        2. Learn probability theory fundamentals<br>
        3. Study common probability distributions<br>
        4. Practice hypothesis testing with real data<br>
        5. Learn regression analysis<br>
        6. Explore Bayesian methods<br>
        7. Apply to real-world projects<br><br>
        
        <strong>Practice Resources:</strong><br>
        • <strong>Kaggle:</strong> https://www.kaggle.com/learn/intro-to-machine-learning<br>
        • <strong>Seeing Theory:</strong> https://seeing-theory.brown.edu/<br>
        • <strong>StatQuest:</strong> https://statquest.org/<br>
        • <strong>OpenIntro Statistics:</strong> https://www.openintro.org/book/os/
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>MA201 - Statistics and Probability</strong><br>
    <small>UTel University | Department of Mathematics</small>
</div>
""", unsafe_allow_html=True)
