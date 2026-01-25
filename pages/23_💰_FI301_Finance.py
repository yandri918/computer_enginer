import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="FI301 - Finance Concentration", page_icon="💰", layout="wide")

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
    
    .fintech-box {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .trading-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .blockchain-box {
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
    <div style="font-size: 1.2rem; opacity: 0.9;">FI301</div>
    <div class="course-title">Concentration - Finance</div>
    <div>💰 3 Credits | Semester 6 | Fintech & Financial Systems</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "6")
with col3:
    st.metric("Difficulty", "5/7")
with col4:
    st.metric("Hours/Week", "6")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "🏦 Financial Systems",
    "💳 Fintech Applications",
    "📈 Algorithmic Trading",
    "⛓️ Blockchain & Crypto",
    "📊 Financial Data Analysis",
    "🤖 AI in Finance",
    "🎯 Case Studies",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive study of financial technology (fintech) and computational finance. Covers financial systems, 
        payment technologies, algorithmic trading, blockchain, cryptocurrencies, robo-advisors, and financial data analysis. 
        Emphasizes practical implementation of financial algorithms, risk management, and regulatory compliance. Students will 
        develop fintech applications, implement trading strategies, and analyze financial markets using modern technologies.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Understand modern financial systems and payment infrastructure",
        "Develop fintech applications (mobile banking, payment systems)",
        "Implement algorithmic trading strategies",
        "Work with blockchain and cryptocurrency technologies",
        "Analyze financial data using Python and machine learning",
        "Build robo-advisors and portfolio optimization systems",
        "Understand financial regulations and compliance (KYC, AML)",
        "Apply AI/ML to financial forecasting and risk management"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Financial Systems:**
        - Banking systems and infrastructure
        - Payment processing (ACH, SWIFT, cards)
        - Digital wallets and mobile payments
        - Open banking and APIs
        - Regulatory frameworks (PSD2, GDPR)
        
        **Fintech Applications:**
        - Mobile banking apps
        - Peer-to-peer lending platforms
        - Crowdfunding systems
        - Insurance tech (insurtech)
        - Regtech and compliance automation
        """)
    
    with col2:
        st.markdown("""
        **Trading & Markets:**
        - Market microstructure
        - Order types and execution
        - High-frequency trading (HFT)
        - Quantitative strategies
        - Risk management
        
        **Emerging Technologies:**
        - Blockchain and smart contracts
        - Cryptocurrencies and DeFi
        - Central Bank Digital Currencies (CBDCs)
        - AI/ML in finance
        - Quantum computing in finance
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Python for Finance", "author": "Yves Hilpisch", "type": "Textbook"},
        {"title": "Algorithmic Trading", "author": "Ernest P. Chan", "type": "Trading"},
        {"title": "Mastering Bitcoin", "author": "Andreas Antonopoulos", "type": "Blockchain"},
        {"title": "Machine Learning for Asset Managers", "author": "Marcos López de Prado", "type": "ML"}
    ]
    
    for resource in resources:
        title = resource['title']
        author = resource['author']
        rtype = resource['type']
        st.markdown(f"📖 **{title}** by {author} ({rtype})")

# ==================== TAB 2: FINANCIAL SYSTEMS ====================
with tabs[1]:
    st.markdown("## 🏦 Financial Systems")
    
    st.markdown("### 1️⃣ Banking Infrastructure")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Core Banking System:</strong><br>
        • Account management<br>
        • Transaction processing<br>
        • Customer data management<br>
        • Interest calculation<br>
        • Loan management<br><br>
        
        <strong>Payment Networks:</strong><br>
        • <strong>ACH (Automated Clearing House):</strong> Batch processing, 1-3 days<br>
        • <strong>Wire Transfer:</strong> Real-time, high value<br>
        • <strong>SWIFT:</strong> International payments<br>
        • <strong>Real-Time Payments (RTP):</strong> Instant settlement<br>
        • <strong>Card Networks:</strong> Visa, Mastercard, Amex<br><br>
        
        <strong>Payment Flow:</strong><br>
        1. Customer initiates payment<br>
        2. Merchant acquirer receives request<br>
        3. Card network routes to issuing bank<br>
        4. Issuing bank authorizes/declines<br>
        5. Settlement occurs (typically T+1 or T+2)<br>
        6. Funds transferred to merchant
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Digital Payments")
    
    st.markdown("""
    <div class="fintech-box">
        <strong>Mobile Wallets:</strong><br>
        • Apple Pay, Google Pay, Samsung Pay<br>
        • NFC (Near Field Communication)<br>
        • Tokenization for security<br>
        • Biometric authentication<br><br>
        
        <strong>QR Code Payments:</strong><br>
        • Popular in Asia (Alipay, WeChat Pay)<br>
        • Low infrastructure requirements<br>
        • Merchant-presented or consumer-presented<br><br>
        
        <strong>Buy Now, Pay Later (BNPL):</strong><br>
        • Klarna, Afterpay, Affirm<br>
        • Split payments over time<br>
        • Credit risk assessment<br>
        • Integration with e-commerce<br><br>
        
        <strong>Cryptocurrency Payments:</strong><br>
        • Bitcoin, Ethereum, stablecoins<br>
        • Decentralized, borderless<br>
        • Lower fees for international transfers<br>
        • Volatility challenges
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Open Banking")
    
    st.markdown("""
    <div class="theory-box">
        <strong>PSD2 (Payment Services Directive 2):</strong><br>
        • European regulation<br>
        • Banks must provide APIs<br>
        • Third-party access to account data<br>
        • Strong Customer Authentication (SCA)<br><br>
        
        <strong>Open Banking APIs:</strong><br>
        • Account information (read balance, transactions)<br>
        • Payment initiation (make payments)<br>
        • Confirmation of funds<br><br>
        
        <strong>Use Cases:</strong><br>
        • Personal finance management (Mint, YNAB)<br>
        • Account aggregation<br>
        • Credit scoring with alternative data<br>
        • Automated savings and investments
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: FINTECH APPLICATIONS ====================
with tabs[2]:
    st.markdown("## 💳 Fintech Applications")
    
    st.markdown("### 1️⃣ Mobile Banking")
    
    st.markdown("""
    <div class="fintech-box">
        <strong>Core Features:</strong><br>
        • Account balance and transaction history<br>
        • Fund transfers (P2P, bill pay)<br>
        • Mobile check deposit<br>
        • Card management (freeze, limits)<br>
        • Budgeting and spending insights<br><br>
        
        <strong>Security Measures:</strong><br>
        • Multi-factor authentication (MFA)<br>
        • Biometric login (fingerprint, face ID)<br>
        • Device binding<br>
        • Transaction monitoring and alerts<br>
        • End-to-end encryption<br><br>
        
        <strong>Technology Stack:</strong><br>
        • Frontend: React Native, Flutter<br>
        • Backend: Node.js, Python, Java<br>
        • Database: PostgreSQL, MongoDB<br>
        • Cloud: AWS, Azure, GCP<br>
        • APIs: RESTful, GraphQL
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Peer-to-Peer Lending")
    
    st.markdown("""
    <div class="theory-box">
        <strong>P2P Lending Platforms:</strong><br>
        • LendingClub, Prosper, Funding Circle<br>
        • Connect borrowers directly with investors<br>
        • Lower interest rates than traditional banks<br>
        • Higher returns for investors<br><br>
        
        <strong>Process Flow:</strong><br>
        1. Borrower applies for loan<br>
        2. Platform assesses creditworthiness<br>
        3. Loan listed on marketplace<br>
        4. Investors fund loan (whole or fractional)<br>
        5. Borrower receives funds<br>
        6. Monthly payments distributed to investors<br><br>
        
        <strong>Risk Assessment:</strong><br>
        • Credit score analysis<br>
        • Income verification<br>
        • Debt-to-income ratio<br>
        • Alternative data (social media, education)<br>
        • Machine learning models
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Robo-Advisors")
    
    st.markdown("""
    <div class="fintech-box">
        <strong>Automated Investment Management:</strong><br>
        • Betterment, Wealthfront, Vanguard Digital Advisor<br>
        • Algorithm-based portfolio management<br>
        • Low fees (0.25% - 0.50% annually)<br>
        • Automatic rebalancing<br>
        • Tax-loss harvesting<br><br>
        
        <strong>Portfolio Construction:</strong><br>
        1. Risk assessment questionnaire<br>
        2. Determine asset allocation (stocks/bonds)<br>
        3. Select low-cost ETFs<br>
        4. Optimize for tax efficiency<br>
        5. Monitor and rebalance periodically<br><br>
        
        <strong>Modern Portfolio Theory (MPT):</strong><br>
        • Diversification reduces risk<br>
        • Efficient frontier optimization<br>
        • Risk-return trade-off<br>
        • Sharpe ratio maximization
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: ALGORITHMIC TRADING ====================
with tabs[3]:
    st.markdown("## 📈 Algorithmic Trading")
    
    st.markdown("### 1️⃣ Trading Strategies")
    
    st.markdown("""
    <div class="trading-box">
        <strong>Momentum Trading:</strong><br>
        • Buy assets with upward price trends<br>
        • Sell assets with downward trends<br>
        • Moving average crossovers<br>
        • Relative Strength Index (RSI)<br><br>
        
        <strong>Mean Reversion:</strong><br>
        • Prices tend to revert to mean<br>
        • Buy when undervalued, sell when overvalued<br>
        • Bollinger Bands<br>
        • Z-score analysis<br><br>
        
        <strong>Arbitrage:</strong><br>
        • Exploit price differences across markets<br>
        • Statistical arbitrage (pairs trading)<br>
        • Triangular arbitrage (forex)<br>
        • Index arbitrage<br><br>
        
        <strong>Market Making:</strong><br>
        • Provide liquidity by quoting bid/ask<br>
        • Profit from bid-ask spread<br>
        • Inventory management<br>
        • High-frequency trading (HFT)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Technical Indicators")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Trend Indicators:</strong><br>
        • <strong>Moving Averages:</strong> SMA, EMA, WMA<br>
        • <strong>MACD:</strong> Moving Average Convergence Divergence<br>
        • <strong>ADX:</strong> Average Directional Index<br><br>
        
        <strong>Momentum Indicators:</strong><br>
        • <strong>RSI:</strong> Relative Strength Index (0-100)<br>
        • <strong>Stochastic Oscillator:</strong> %K and %D lines<br>
        • <strong>Williams %R:</strong> Momentum indicator<br><br>
        
        <strong>Volatility Indicators:</strong><br>
        • <strong>Bollinger Bands:</strong> Price envelope<br>
        • <strong>ATR:</strong> Average True Range<br>
        • <strong>VIX:</strong> Volatility Index<br><br>
        
        <strong>Volume Indicators:</strong><br>
        • <strong>OBV:</strong> On-Balance Volume<br>
        • <strong>Volume Profile:</strong> Price-volume distribution<br>
        • <strong>VWAP:</strong> Volume Weighted Average Price
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Backtesting")
    
    st.markdown("""
    <div class="trading-box">
        <strong>Backtesting Process:</strong><br>
        1. Define trading strategy<br>
        2. Obtain historical data<br>
        3. Simulate trades<br>
        4. Calculate performance metrics<br>
        5. Optimize parameters<br>
        6. Validate with out-of-sample data<br><br>
        
        <strong>Performance Metrics:</strong><br>
        • <strong>Total Return:</strong> Overall profit/loss<br>
        • <strong>Sharpe Ratio:</strong> Risk-adjusted return<br>
        • <strong>Maximum Drawdown:</strong> Largest peak-to-trough decline<br>
        • <strong>Win Rate:</strong> % of profitable trades<br>
        • <strong>Profit Factor:</strong> Gross profit / Gross loss<br><br>
        
        <strong>Common Pitfalls:</strong><br>
        • Overfitting (curve fitting)<br>
        • Look-ahead bias<br>
        • Survivorship bias<br>
        • Transaction costs ignored<br>
        • Slippage not accounted for
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: BLOCKCHAIN ====================
with tabs[4]:
    st.markdown("## ⛓️ Blockchain & Cryptocurrency")
    
    st.markdown("### 1️⃣ Blockchain Fundamentals")
    
    st.markdown("""
    <div class="blockchain-box">
        <strong>Blockchain Structure:</strong><br>
        • Distributed ledger technology<br>
        • Blocks linked by cryptographic hashes<br>
        • Immutable and transparent<br>
        • Decentralized consensus<br><br>
        
        <strong>Consensus Mechanisms:</strong><br>
        • <strong>Proof of Work (PoW):</strong> Bitcoin, computational puzzles<br>
        • <strong>Proof of Stake (PoS):</strong> Ethereum 2.0, validators stake coins<br>
        • <strong>Delegated PoS:</strong> EOS, elected validators<br>
        • <strong>Practical Byzantine Fault Tolerance (PBFT):</strong> Hyperledger<br><br>
        
        <strong>Smart Contracts:</strong><br>
        • Self-executing contracts<br>
        • Code stored on blockchain<br>
        • Triggered by conditions<br>
        • Solidity (Ethereum), Rust (Solana)<br>
        • Use cases: DeFi, NFTs, DAOs
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Cryptocurrencies")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Major Cryptocurrencies:</strong><br>
        • <strong>Bitcoin (BTC):</strong> Digital gold, store of value<br>
        • <strong>Ethereum (ETH):</strong> Smart contract platform<br>
        • <strong>Stablecoins:</strong> USDT, USDC, DAI (pegged to USD)<br>
        • <strong>Altcoins:</strong> Cardano, Solana, Polkadot<br><br>
        
        <strong>Cryptocurrency Wallets:</strong><br>
        • <strong>Hot Wallets:</strong> Connected to internet (MetaMask, Trust Wallet)<br>
        • <strong>Cold Wallets:</strong> Offline storage (Ledger, Trezor)<br>
        • <strong>Custodial:</strong> Exchange holds keys<br>
        • <strong>Non-custodial:</strong> User controls private keys<br><br>
        
        <strong>Exchanges:</strong><br>
        • <strong>Centralized (CEX):</strong> Binance, Coinbase, Kraken<br>
        • <strong>Decentralized (DEX):</strong> Uniswap, SushiSwap, PancakeSwap<br>
        • <strong>Order book vs AMM:</strong> Traditional vs automated market maker
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ DeFi (Decentralized Finance)")
    
    st.markdown("""
    <div class="blockchain-box">
        <strong>DeFi Protocols:</strong><br>
        • <strong>Lending/Borrowing:</strong> Aave, Compound<br>
        • <strong>Decentralized Exchanges:</strong> Uniswap, Curve<br>
        • <strong>Yield Farming:</strong> Earn interest on crypto<br>
        • <strong>Staking:</strong> Lock tokens for rewards<br>
        • <strong>Derivatives:</strong> dYdX, Synthetix<br><br>
        
        <strong>Liquidity Pools:</strong><br>
        • Users provide liquidity (token pairs)<br>
        • Earn trading fees<br>
        • Automated Market Maker (AMM)<br>
        • Impermanent loss risk<br><br>
        
        <strong>Risks:</strong><br>
        • Smart contract vulnerabilities<br>
        • Rug pulls and scams<br>
        • Regulatory uncertainty<br>
        • High volatility<br>
        • Gas fees (Ethereum)
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: FINANCIAL DATA ANALYSIS ====================
with tabs[5]:
    st.markdown("## 📊 Financial Data Analysis")
    
    st.markdown("### 1️⃣ Data Sources")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Market Data Providers:</strong><br>
        • <strong>Free:</strong> Yahoo Finance, Alpha Vantage, IEX Cloud<br>
        • <strong>Paid:</strong> Bloomberg Terminal, Reuters, FactSet<br>
        • <strong>Crypto:</strong> CoinGecko, CoinMarketCap, Messari<br><br>
        
        <strong>Data Types:</strong><br>
        • <strong>Price Data:</strong> OHLCV (Open, High, Low, Close, Volume)<br>
        • <strong>Fundamental Data:</strong> Financial statements, ratios<br>
        • <strong>Alternative Data:</strong> Sentiment, satellite imagery, web scraping<br>
        • <strong>News & Events:</strong> Earnings, dividends, splits<br><br>
        
        <strong>Python Libraries:</strong><br>
        • <strong>pandas:</strong> Data manipulation<br>
        • <strong>yfinance:</strong> Yahoo Finance API<br>
        • <strong>pandas-datareader:</strong> Multiple data sources<br>
        • <strong>ccxt:</strong> Cryptocurrency exchange data
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Time Series Analysis")
    
    st.markdown("""
    <div class="fintech-box">
        <strong>Statistical Methods:</strong><br>
        • <strong>ARIMA:</strong> AutoRegressive Integrated Moving Average<br>
        • <strong>GARCH:</strong> Generalized AutoRegressive Conditional Heteroskedasticity<br>
        • <strong>VAR:</strong> Vector AutoRegression<br>
        • <strong>Cointegration:</strong> Long-term equilibrium relationships<br><br>
        
        <strong>Feature Engineering:</strong><br>
        • Returns (simple, log)<br>
        • Rolling statistics (mean, std, min, max)<br>
        • Technical indicators<br>
        • Lagged features<br>
        • Fourier transforms<br><br>
        
        <strong>Stationarity:</strong><br>
        • Mean and variance constant over time<br>
        • Augmented Dickey-Fuller test<br>
        • Differencing to achieve stationarity<br>
        • Required for many time series models
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: AI IN FINANCE ====================
with tabs[6]:
    st.markdown("## 🤖 AI in Finance")
    
    st.markdown("### 1️⃣ Machine Learning Applications")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Price Prediction:</strong><br>
        • Regression models (Linear, Ridge, Lasso)<br>
        • Random Forest, Gradient Boosting<br>
        • Neural Networks (LSTM, GRU, Transformers)<br>
        • Ensemble methods<br><br>
        
        <strong>Classification Tasks:</strong><br>
        • Direction prediction (up/down)<br>
        • Credit scoring<br>
        • Fraud detection<br>
        • Customer churn prediction<br><br>
        
        <strong>Clustering:</strong><br>
        • Customer segmentation<br>
        • Portfolio diversification<br>
        • Market regime detection<br>
        • Anomaly detection
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Natural Language Processing")
    
    st.markdown("""
    <div class="fintech-box">
        <strong>Sentiment Analysis:</strong><br>
        • News sentiment (positive/negative/neutral)<br>
        • Social media analysis (Twitter, Reddit)<br>
        • Earnings call transcripts<br>
        • Impact on stock prices<br><br>
        
        <strong>NLP Techniques:</strong><br>
        • Bag of Words, TF-IDF<br>
        • Word embeddings (Word2Vec, GloVe)<br>
        • Transformers (BERT, GPT)<br>
        • Named Entity Recognition (NER)<br><br>
        
        <strong>Applications:</strong><br>
        • Automated trading signals<br>
        • Risk assessment<br>
        • Market research<br>
        • Regulatory compliance monitoring
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: CASE STUDIES ====================
with tabs[7]:
    st.markdown("## 🎯 Case Studies")
    
    case_studies = [
        {
            "title": "Case Study 1: Building a Simple Trading Bot",
            "description": "Develop a momentum-based trading bot using Python",
            "details": """
**Objective:** Create an automated trading bot that executes trades based on moving average crossover strategy.

**Requirements:**
1. Fetch real-time stock data
2. Calculate 50-day and 200-day moving averages
3. Generate buy signal when 50-day MA crosses above 200-day MA (Golden Cross)
4. Generate sell signal when 50-day MA crosses below 200-day MA (Death Cross)
5. Execute trades via broker API
6. Track portfolio performance

**Technology Stack:**
- Python 3.x
- pandas for data manipulation
- yfinance for market data
- Alpaca API for trading
- matplotlib for visualization

**Implementation Steps:**
1. Set up Alpaca paper trading account
2. Fetch historical data for backtesting
3. Implement moving average calculation
4. Create signal generation logic
5. Implement order execution
6. Add risk management (stop loss, position sizing)
7. Monitor and log trades
8. Calculate performance metrics
            """,
            "solution": """
**Key Code Snippets:**

```python
import yfinance as yf
import pandas as pd
from alpaca.trading.client import TradingClient

# Fetch data
def get_data(symbol, period='1y'):
    data = yf.download(symbol, period=period)
    return data

# Calculate moving averages
def calculate_signals(data):
    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['MA200'] = data['Close'].rolling(window=200).mean()
    
    # Generate signals
    data['Signal'] = 0
    data.loc[data['MA50'] > data['MA200'], 'Signal'] = 1  # Buy
    data.loc[data['MA50'] < data['MA200'], 'Signal'] = -1  # Sell
    
    return data

# Execute trade
def execute_trade(symbol, signal, quantity):
    if signal == 1:
        # Place buy order
        order = trading_client.submit_order(
            symbol=symbol,
            qty=quantity,
            side='buy',
            type='market',
            time_in_force='day'
        )
    elif signal == -1:
        # Place sell order
        order = trading_client.submit_order(
            symbol=symbol,
            qty=quantity,
            side='sell',
            type='market',
            time_in_force='day'
        )
```

**Results:**
- Backtest on SPY (S&P 500 ETF) from 2020-2024
- Total Return: 15.2%
- Sharpe Ratio: 0.85
- Maximum Drawdown: -12.3%
- Win Rate: 58%
            """
        },
        {
            "title": "Case Study 2: Credit Risk Assessment with ML",
            "description": "Build a machine learning model to predict loan default",
            "details": """
**Objective:** Develop a credit scoring model using machine learning to predict probability of loan default.

**Dataset:** LendingClub loan data
- Features: Credit score, income, debt-to-income ratio, employment length, loan amount, purpose
- Target: Default (1) or Paid (0)

**Approach:**
1. Data preprocessing and cleaning
2. Exploratory data analysis
3. Feature engineering
4. Model training (Logistic Regression, Random Forest, XGBoost)
5. Model evaluation (AUC-ROC, Precision-Recall)
6. Feature importance analysis
7. Model deployment

**Evaluation Metrics:**
- AUC-ROC: Area under ROC curve
- Precision: True positives / (True positives + False positives)
- Recall: True positives / (True positives + False negatives)
- F1-Score: Harmonic mean of precision and recall
            """,
            "solution": """
**Model Performance:**

| Model | AUC-ROC | Precision | Recall | F1-Score |
|-------|---------|-----------|--------|----------|
| Logistic Regression | 0.72 | 0.68 | 0.65 | 0.66 |
| Random Forest | 0.78 | 0.74 | 0.71 | 0.72 |
| XGBoost | 0.82 | 0.79 | 0.76 | 0.77 |

**Top Features:**
1. Credit score (FICO)
2. Debt-to-income ratio
3. Number of delinquencies
4. Revolving credit utilization
5. Employment length

**Business Impact:**
- Reduced default rate by 15%
- Improved loan approval accuracy
- Automated decision-making for 80% of applications
- Saved $2M annually in bad debt
            """
        }
    ]
    
    for idx, case in enumerate(case_studies, 1):
        with st.expander(f"📝 {case['title']}", expanded=False):
            st.markdown(f"**Description:** {case['description']}")
            st.markdown(case['details'])
            
            if st.button(f"Show Solution", key=f"case_{idx}"):
                st.markdown("### Solution")
                st.markdown(case['solution'])

# ==================== TAB 9: YOUTUBE ====================
with tabs[8]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning Finance and Fintech</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {"title": "Python for Finance", "channel": "freeCodeCamp.org", "url": "https://www.youtube.com/watch?v=xfzGZB4HhEE", "description": "Complete Python finance course", "duration": "~13 hours"},
        {"title": "Algorithmic Trading", "channel": "Part Time Larry", "url": "https://www.youtube.com/c/parttimelarry", "description": "Beginner-friendly trading tutorials", "duration": "Channel"},
        {"title": "Blockchain Basics", "channel": "Simply Explained", "url": "https://www.youtube.com/playlist?list=PLzvRQMJ9HDiTqZmbtFisdXFxul5k0F-Q4", "description": "Blockchain and crypto explained", "duration": "Playlist"}
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
        {"title": "Quantitative Finance", "channel": "QuantPy", "url": "https://www.youtube.com/c/QuantPy", "description": "Quant finance with Python", "duration": "Channel"},
        {"title": "Machine Learning for Trading", "channel": "Sentdex", "url": "https://www.youtube.com/playlist?list=PLQVvvaa0QuDe6ZBtkCNWNUbdaBo2vA4RO", "description": "ML applied to trading", "duration": "Playlist"},
        {"title": "Cryptocurrency Trading", "channel": "DataDash", "url": "https://www.youtube.com/c/DataDash", "description": "Crypto market analysis", "duration": "Channel"}
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
        {"title": "Quantitative Trading", "channel": "QuantInsti", "url": "https://www.youtube.com/c/QuantInsti", "description": "Professional quant trading", "duration": "Channel"},
        {"title": "DeFi Development", "channel": "Dapp University", "url": "https://www.youtube.com/c/DappUniversity", "description": "Build DeFi applications", "duration": "Channel"},
        {"title": "Financial Engineering", "channel": "MIT OpenCourseWare", "url": "https://www.youtube.com/playlist?list=PLUl4u3cNGP63ctJIEC1UnZ0btsphnnoHR", "description": "MIT 15.401 Finance Theory", "duration": "Full Course"}
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
        1. Learn Python programming basics<br>
        2. Master pandas and numpy for data analysis<br>
        3. Understand financial markets and instruments<br>
        4. Study technical analysis and indicators<br>
        5. Learn algorithmic trading strategies<br>
        6. Explore blockchain and cryptocurrency<br>
        7. Apply machine learning to finance<br>
        8. Build real projects and portfolios<br><br>
        
        <strong>Tools & Platforms:</strong><br>
        • <strong>Data:</strong> Yahoo Finance, Alpha Vantage, Quandl<br>
        • <strong>Trading:</strong> Alpaca, Interactive Brokers, TD Ameritrade<br>
        • <strong>Backtesting:</strong> Backtrader, Zipline, QuantConnect<br>
        • <strong>Blockchain:</strong> Remix, Hardhat, Truffle<br>
        • <strong>ML:</strong> scikit-learn, TensorFlow, PyTorch<br><br>
        
        <strong>Career Paths:</strong><br>
        • Quantitative Analyst<br>
        • Algorithmic Trader<br>
        • Fintech Developer<br>
        • Blockchain Engineer<br>
        • Financial Data Scientist
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>FI301 - Finance Concentration</strong><br>
    <small>UTel University | Computer Engineering Program</small>
</div>
""", unsafe_allow_html=True)
