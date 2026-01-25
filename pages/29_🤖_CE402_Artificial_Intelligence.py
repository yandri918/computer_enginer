import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="CE402 - Artificial Intelligence", page_icon="🤖", layout="wide")

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
        background: linear-gradient(135deg, #ec4899 0%, #db2777 100%);
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
        background: linear-gradient(135deg, #fce7f3 0%, #fbcfe8 100%);
        border-left: 5px solid #ec4899;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .ml-box {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .dl-box {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        border-left: 5px solid #10b981;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .nlp-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
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
    <div style="font-size: 1.2rem; opacity: 0.9;">CE402</div>
    <div class="course-title">Artificial Intelligence</div>
    <div>🤖 4 Credits | Semester 7 | AI, ML & Deep Learning</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "4")
with col2:
    st.metric("Semester", "7")
with col3:
    st.metric("Difficulty", "7/7")
with col4:
    st.metric("Hours/Week", "8")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "🔍 Search Algorithms",
    "🤖 Machine Learning",
    "🧠 Neural Networks",
    "🌊 Deep Learning",
    "💬 NLP & Computer Vision",
    "🎯 AI Applications",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive introduction to Artificial Intelligence covering classical AI, machine learning, deep learning, 
        and modern AI applications. Learn search algorithms, knowledge representation, supervised and unsupervised learning, 
        neural networks, convolutional and recurrent networks, natural language processing, computer vision, and AI ethics. 
        Emphasizes hands-on implementation using Python, TensorFlow, and PyTorch. Students will build AI systems from 
        scratch and apply them to real-world problems.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Implement classical AI search algorithms (BFS, DFS, A*)",
        "Build machine learning models (regression, classification, clustering)",
        "Design and train neural networks from scratch",
        "Apply deep learning to computer vision and NLP tasks",
        "Use TensorFlow and PyTorch for AI development",
        "Evaluate and optimize AI model performance",
        "Understand AI ethics and responsible AI development",
        "Deploy AI models to production"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Classical AI:**
        - Search algorithms (BFS, DFS, A*, Minimax)
        - Knowledge representation
        - Logic and reasoning
        - Planning and optimization
        - Game playing (Chess, Go)
        
        **Machine Learning:**
        - Supervised learning (regression, classification)
        - Unsupervised learning (clustering, PCA)
        - Model evaluation and validation
        - Feature engineering
        - Ensemble methods
        """)
    
    with col2:
        st.markdown("""
        **Deep Learning:**
        - Neural networks fundamentals
        - Backpropagation and optimization
        - Convolutional Neural Networks (CNNs)
        - Recurrent Neural Networks (RNNs)
        - Transformers and attention
        
        **Applications:**
        - Natural Language Processing
        - Computer Vision
        - Reinforcement Learning
        - Generative AI (GANs, Diffusion)
        - AI Ethics and Bias
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Artificial Intelligence: A Modern Approach", "author": "Russell & Norvig", "type": "Textbook"},
        {"title": "Deep Learning", "author": "Goodfellow, Bengio & Courville", "type": "Deep Learning"},
        {"title": "Hands-On Machine Learning", "author": "Aurélien Géron", "type": "Practical"},
        {"title": "Fast.ai Course", "author": "Jeremy Howard", "type": "Online Course"}
    ]
    
    for resource in resources:
        title = resource['title']
        author = resource['author']
        rtype = resource['type']
        st.markdown(f"📖 **{title}** by {author} ({rtype})")

# ==================== TAB 2: SEARCH ALGORITHMS ====================
with tabs[1]:
    st.markdown("## 🔍 Search Algorithms")
    
    st.markdown("### 1️⃣ Uninformed Search")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Breadth-First Search (BFS):</strong><br>
        • Explores level by level<br>
        • Guarantees shortest path<br>
        • Time: O(b^d), Space: O(b^d)<br>
        • Complete and optimal<br><br>
        
        <strong>Depth-First Search (DFS):</strong><br>
        • Explores as deep as possible<br>
        • Memory efficient<br>
        • Time: O(b^m), Space: O(bm)<br>
        • Not optimal, may not be complete<br><br>
        
        <strong>Uniform Cost Search (UCS):</strong><br>
        • Expands lowest cost node<br>
        • Optimal for weighted graphs<br>
        • Uses priority queue<br>
        • Complete and optimal
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Informed Search (Heuristic)")
    
    st.markdown("""
    <div class="ml-box">
        <strong>A* Search Algorithm:</strong><br>
        f(n) = g(n) + h(n)<br>
        • g(n): Cost from start to n<br>
        • h(n): Estimated cost from n to goal (heuristic)<br>
        • Optimal if h(n) is admissible (never overestimates)<br>
        • Widely used in pathfinding and navigation<br><br>
        
        <strong>Heuristic Functions:</strong><br>
        • <strong>Manhattan Distance:</strong> |x1-x2| + |y1-y2|<br>
        • <strong>Euclidean Distance:</strong> √((x1-x2)² + (y1-y2)²)<br>
        • <strong>Chebyshev Distance:</strong> max(|x1-x2|, |y1-y2|)<br><br>
        
        <strong>Greedy Best-First Search:</strong><br>
        • Uses only h(n), ignores g(n)<br>
        • Faster but not optimal<br>
        • Good for quick solutions
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Game Playing")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Minimax Algorithm:</strong><br>
        • Two-player zero-sum games<br>
        • Maximizing player vs minimizing player<br>
        • Explores entire game tree<br>
        • Guarantees optimal play<br><br>
        
        <strong>Alpha-Beta Pruning:</strong><br>
        • Optimization of minimax<br>
        • Prunes branches that won't affect result<br>
        • Can reduce time from O(b^d) to O(b^(d/2))<br>
        • Same result as minimax, much faster<br><br>
        
        <strong>Monte Carlo Tree Search (MCTS):</strong><br>
        • Used in AlphaGo<br>
        • Simulation-based search<br>
        • Balances exploration and exploitation<br>
        • Effective for large state spaces
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: MACHINE LEARNING ====================
with tabs[2]:
    st.markdown("## 🤖 Machine Learning")
    
    st.markdown("### 1️⃣ Supervised Learning")
    
    st.markdown("""
    <div class="ml-box">
        <strong>Linear Regression:</strong><br>
        y = mx + b<br>
        • Predict continuous values<br>
        • Minimize Mean Squared Error (MSE)<br>
        • Simple and interpretable<br><br>
        
        <strong>Logistic Regression:</strong><br>
        σ(z) = 1 / (1 + e^(-z))<br>
        • Binary classification<br>
        • Outputs probability (0 to 1)<br>
        • Uses sigmoid activation<br><br>
        
        <strong>Decision Trees:</strong><br>
        • Tree-based model<br>
        • Easy to interpret<br>
        • Can overfit without pruning<br>
        • Handles non-linear relationships<br><br>
        
        <strong>Random Forest:</strong><br>
        • Ensemble of decision trees<br>
        • Reduces overfitting<br>
        • Feature importance ranking<br>
        • High accuracy, robust
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Unsupervised Learning")
    
    st.markdown("""
    <div class="theory-box">
        <strong>K-Means Clustering:</strong><br>
        1. Initialize k centroids randomly<br>
        2. Assign points to nearest centroid<br>
        3. Update centroids to mean of assigned points<br>
        4. Repeat until convergence<br>
        • Simple and fast<br>
        • Requires specifying k<br><br>
        
        <strong>Principal Component Analysis (PCA):</strong><br>
        • Dimensionality reduction<br>
        • Find principal components (directions of max variance)<br>
        • Reduce features while preserving information<br>
        • Useful for visualization and preprocessing<br><br>
        
        <strong>Hierarchical Clustering:</strong><br>
        • Creates tree of clusters (dendrogram)<br>
        • Agglomerative (bottom-up) or divisive (top-down)<br>
        • No need to specify k beforehand
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Model Evaluation")
    
    metrics_data = {
        'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC'],
        'Formula': [
            '(TP + TN) / Total',
            'TP / (TP + FP)',
            'TP / (TP + FN)',
            '2 * (Precision * Recall) / (Precision + Recall)',
            'Area under ROC curve'
        ],
        'Use Case': [
            'Balanced datasets',
            'Minimize false positives',
            'Minimize false negatives',
            'Balance precision and recall',
            'Overall model performance'
        ]
    }
    
    df_metrics = pd.DataFrame(metrics_data)
    st.dataframe(df_metrics, use_container_width=True, hide_index=True)

# ==================== TAB 4: NEURAL NETWORKS ====================
with tabs[3]:
    st.markdown("## 🧠 Neural Networks")
    
    st.markdown("### 1️⃣ Perceptron & Multilayer Networks")
    
    st.markdown("""
    <div class="dl-box">
        <strong>Perceptron:</strong><br>
        output = activation(Σ(weights * inputs) + bias)<br>
        • Simplest neural network<br>
        • Linear classifier<br>
        • Can't solve XOR problem<br><br>
        
        <strong>Multilayer Perceptron (MLP):</strong><br>
        • Input layer, hidden layers, output layer<br>
        • Can solve non-linear problems<br>
        • Universal function approximator<br>
        • Requires backpropagation for training<br><br>
        
        <strong>Activation Functions:</strong><br>
        • <strong>Sigmoid:</strong> σ(x) = 1/(1+e^(-x)) - Output (0,1)<br>
        • <strong>Tanh:</strong> tanh(x) - Output (-1,1)<br>
        • <strong>ReLU:</strong> max(0,x) - Most popular, fast<br>
        • <strong>Leaky ReLU:</strong> max(0.01x, x) - Fixes dying ReLU<br>
        • <strong>Softmax:</strong> For multi-class classification
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Backpropagation")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Training Process:</strong><br>
        1. <strong>Forward Pass:</strong> Compute predictions<br>
        2. <strong>Compute Loss:</strong> Compare with actual labels<br>
        3. <strong>Backward Pass:</strong> Calculate gradients<br>
        4. <strong>Update Weights:</strong> Gradient descent<br><br>
        
        <strong>Loss Functions:</strong><br>
        • <strong>MSE:</strong> (1/n)Σ(y - ŷ)² - Regression<br>
        • <strong>Cross-Entropy:</strong> -Σy*log(ŷ) - Classification<br>
        • <strong>Binary Cross-Entropy:</strong> Binary classification<br><br>
        
        <strong>Optimization Algorithms:</strong><br>
        • <strong>SGD:</strong> Stochastic Gradient Descent<br>
        • <strong>Momentum:</strong> Accelerates SGD<br>
        • <strong>Adam:</strong> Adaptive learning rate (most popular)<br>
        • <strong>RMSprop:</strong> Good for RNNs
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Regularization")
    
    st.markdown("""
    <div class="ml-box">
        <strong>Prevent Overfitting:</strong><br><br>
        
        <strong>Dropout:</strong><br>
        • Randomly drop neurons during training<br>
        • Typical rate: 0.2-0.5<br>
        • Prevents co-adaptation<br><br>
        
        <strong>L1/L2 Regularization:</strong><br>
        • L1: Adds |weights| to loss (sparse weights)<br>
        • L2: Adds weights² to loss (weight decay)<br>
        • Penalizes large weights<br><br>
        
        <strong>Batch Normalization:</strong><br>
        • Normalize layer inputs<br>
        • Faster training, higher learning rates<br>
        • Acts as regularization<br><br>
        
        <strong>Early Stopping:</strong><br>
        • Stop when validation loss stops improving<br>
        • Simple and effective
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: DEEP LEARNING ====================
with tabs[4]:
    st.markdown("## 🌊 Deep Learning")
    
    st.markdown("### 1️⃣ Convolutional Neural Networks (CNNs)")
    
    st.markdown("""
    <div class="dl-box">
        <strong>CNN Architecture:</strong><br>
        Input → Conv → ReLU → Pool → Conv → ReLU → Pool → FC → Output<br><br>
        
        <strong>Convolutional Layer:</strong><br>
        • Applies filters/kernels to input<br>
        • Detects features (edges, textures, patterns)<br>
        • Parameter sharing reduces parameters<br>
        • Translation invariant<br><br>
        
        <strong>Pooling Layer:</strong><br>
        • <strong>Max Pooling:</strong> Takes maximum value<br>
        • <strong>Average Pooling:</strong> Takes average<br>
        • Reduces spatial dimensions<br>
        • Provides translation invariance<br><br>
        
        <strong>Famous CNN Architectures:</strong><br>
        • <strong>LeNet-5:</strong> First CNN (1998)<br>
        • <strong>AlexNet:</strong> ImageNet winner (2012)<br>
        • <strong>VGG:</strong> Very deep networks<br>
        • <strong>ResNet:</strong> Skip connections, 152 layers<br>
        • <strong>Inception:</strong> Multiple filter sizes<br>
        • <strong>EfficientNet:</strong> Optimized scaling
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Recurrent Neural Networks (RNNs)")
    
    st.markdown("""
    <div class="theory-box">
        <strong>RNN Basics:</strong><br>
        • Process sequential data<br>
        • Hidden state carries information<br>
        • h_t = tanh(W_h * h_(t-1) + W_x * x_t)<br>
        • Suffers from vanishing/exploding gradients<br><br>
        
        <strong>LSTM (Long Short-Term Memory):</strong><br>
        • Solves vanishing gradient problem<br>
        • Gates: Forget, Input, Output<br>
        • Cell state carries long-term memory<br>
        • Widely used for sequences<br><br>
        
        <strong>GRU (Gated Recurrent Unit):</strong><br>
        • Simpler than LSTM<br>
        • Fewer parameters, faster training<br>
        • Similar performance to LSTM<br><br>
        
        <strong>Applications:</strong><br>
        • Language modeling<br>
        • Machine translation<br>
        • Speech recognition<br>
        • Time series prediction
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Transformers")
    
    st.markdown("""
    <div class="nlp-box">
        <strong>Attention Mechanism:</strong><br>
        • Focus on relevant parts of input<br>
        • Query, Key, Value matrices<br>
        • Attention(Q,K,V) = softmax(QK^T/√d_k)V<br>
        • Parallel processing (faster than RNNs)<br><br>
        
        <strong>Transformer Architecture:</strong><br>
        • Encoder-Decoder structure<br>
        • Multi-head self-attention<br>
        • Positional encoding<br>
        • Feed-forward networks<br><br>
        
        <strong>Famous Models:</strong><br>
        • <strong>BERT:</strong> Bidirectional encoder (Google)<br>
        • <strong>GPT:</strong> Generative pre-trained (OpenAI)<br>
        • <strong>T5:</strong> Text-to-text (Google)<br>
        • <strong>Vision Transformer (ViT):</strong> Images as sequences<br><br>
        
        <strong>Why Transformers?</strong><br>
        • State-of-the-art in NLP<br>
        • Parallel training (faster)<br>
        • Better long-range dependencies<br>
        • Transfer learning with pre-training
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: NLP & CV ====================
with tabs[5]:
    st.markdown("## 💬 NLP & Computer Vision")
    
    st.markdown("### 1️⃣ Natural Language Processing")
    
    st.markdown("""
    <div class="nlp-box">
        <strong>Text Preprocessing:</strong><br>
        • Tokenization (words, subwords, characters)<br>
        • Lowercasing and normalization<br>
        • Stop word removal<br>
        • Stemming and lemmatization<br>
        • Handling special characters<br><br>
        
        <strong>Word Embeddings:</strong><br>
        • <strong>Word2Vec:</strong> CBOW and Skip-gram<br>
        • <strong>GloVe:</strong> Global vectors<br>
        • <strong>FastText:</strong> Subword embeddings<br>
        • <strong>Contextual:</strong> BERT, ELMo (context-dependent)<br><br>
        
        <strong>NLP Tasks:</strong><br>
        • <strong>Sentiment Analysis:</strong> Positive/negative/neutral<br>
        • <strong>Named Entity Recognition (NER):</strong> Extract entities<br>
        • <strong>Machine Translation:</strong> Seq2seq models<br>
        • <strong>Question Answering:</strong> BERT, GPT<br>
        • <strong>Text Summarization:</strong> Extractive or abstractive<br>
        • <strong>Text Generation:</strong> GPT, T5
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Computer Vision")
    
    st.markdown("""
    <div class="dl-box">
        <strong>Image Classification:</strong><br>
        • Assign label to entire image<br>
        • CNNs (ResNet, EfficientNet)<br>
        • Transfer learning from ImageNet<br>
        • Data augmentation (rotation, flip, crop)<br><br>
        
        <strong>Object Detection:</strong><br>
        • <strong>R-CNN Family:</strong> Region-based CNNs<br>
        • <strong>YOLO:</strong> You Only Look Once (real-time)<br>
        • <strong>SSD:</strong> Single Shot Detector<br>
        • Outputs bounding boxes and classes<br><br>
        
        <strong>Semantic Segmentation:</strong><br>
        • Classify each pixel<br>
        • <strong>U-Net:</strong> Medical imaging<br>
        • <strong>DeepLab:</strong> Atrous convolution<br>
        • <strong>Mask R-CNN:</strong> Instance segmentation<br><br>
        
        <strong>Image Generation:</strong><br>
        • <strong>GANs:</strong> Generator vs Discriminator<br>
        • <strong>VAE:</strong> Variational Autoencoders<br>
        • <strong>Diffusion Models:</strong> DALL-E, Stable Diffusion
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: APPLICATIONS ====================
with tabs[6]:
    st.markdown("## 🎯 AI Applications")
    
    st.markdown("### 1️⃣ Real-World Applications")
    
    applications = [
        {
            "category": "Healthcare",
            "examples": [
                "Medical image analysis (X-rays, MRIs)",
                "Disease diagnosis and prediction",
                "Drug discovery and development",
                "Personalized treatment recommendations",
                "Patient monitoring and alerts"
            ]
        },
        {
            "category": "Finance",
            "examples": [
                "Fraud detection and prevention",
                "Algorithmic trading",
                "Credit scoring and risk assessment",
                "Customer service chatbots",
                "Market prediction and analysis"
            ]
        },
        {
            "category": "Autonomous Vehicles",
            "examples": [
                "Object detection and tracking",
                "Lane detection and navigation",
                "Traffic sign recognition",
                "Path planning and decision making",
                "Sensor fusion (camera, lidar, radar)"
            ]
        },
        {
            "category": "E-Commerce",
            "examples": [
                "Product recommendations",
                "Visual search",
                "Demand forecasting",
                "Dynamic pricing",
                "Customer segmentation"
            ]
        }
    ]
    
    for app in applications:
        category = app['category']
        examples = app['examples']
        st.markdown(f"**🔹 {category}:**")
        for example in examples:
            st.markdown(f"• {example}")
        st.markdown("")
    
    st.markdown("---")
    st.markdown("### 2️⃣ AI Ethics")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Ethical Considerations:</strong><br><br>
        
        <strong>Bias and Fairness:</strong><br>
        • Training data bias<br>
        • Algorithmic bias<br>
        • Fairness metrics and mitigation<br>
        • Diverse and representative datasets<br><br>
        
        <strong>Privacy:</strong><br>
        • Data protection and GDPR<br>
        • Differential privacy<br>
        • Federated learning<br>
        • Right to explanation<br><br>
        
        <strong>Transparency:</strong><br>
        • Explainable AI (XAI)<br>
        • Model interpretability<br>
        • LIME, SHAP for explanations<br>
        • Accountability and auditability<br><br>
        
        <strong>Safety and Security:</strong><br>
        • Adversarial attacks<br>
        • Model robustness<br>
        • AI alignment<br>
        • Responsible AI development
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: YOUTUBE ====================
with tabs[7]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning AI and Machine Learning</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {"title": "AI for Everyone", "channel": "Andrew Ng", "url": "https://www.youtube.com/watch?v=NKpuX_yzdYs", "description": "Non-technical AI intro", "duration": "~1 hour"},
        {"title": "Machine Learning Crash Course", "channel": "Google", "url": "https://www.youtube.com/playlist?list=PLqYmG7hTraZCDxZ44o4p3N5Anz3lLRVZF", "description": "ML fundamentals", "duration": "Playlist"},
        {"title": "Neural Networks Explained", "channel": "3Blue1Brown", "url": "https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi", "description": "Visual neural networks", "duration": "~1 hour"}
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
        {"title": "Machine Learning Course", "channel": "Stanford - Andrew Ng", "url": "https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU", "description": "Complete ML course", "duration": "~20 hours"},
        {"title": "Deep Learning Specialization", "channel": "DeepLearning.AI", "url": "https://www.youtube.com/c/Deeplearningai", "description": "Neural networks & DL", "duration": "Channel"},
        {"title": "Fast.ai Practical Deep Learning", "channel": "fast.ai", "url": "https://www.youtube.com/c/howardjeremyp", "description": "Practical DL approach", "duration": "~30 hours"}
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
        {"title": "CS231n: CNNs for Visual Recognition", "channel": "Stanford", "url": "https://www.youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv", "description": "Computer vision", "duration": "~20 hours"},
        {"title": "CS224n: NLP with Deep Learning", "channel": "Stanford", "url": "https://www.youtube.com/playlist?list=PLoROMvodv4rOSH4v6133s9LFPRHjEmbmJ", "description": "NLP and transformers", "duration": "~20 hours"},
        {"title": "MIT Deep Learning", "channel": "MIT", "url": "https://www.youtube.com/playlist?list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI", "description": "Advanced DL topics", "duration": "~15 hours"}
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
        1. Learn Python and NumPy fundamentals<br>
        2. Understand linear algebra and calculus basics<br>
        3. Study classical ML algorithms<br>
        4. Implement neural networks from scratch<br>
        5. Learn TensorFlow or PyTorch<br>
        6. Practice with Kaggle competitions<br>
        7. Build end-to-end AI projects<br>
        8. Stay updated with latest research (arXiv)<br><br>
        
        <strong>Essential Tools:</strong><br>
        • <strong>Python:</strong> NumPy, Pandas, Matplotlib<br>
        • <strong>ML Libraries:</strong> Scikit-learn<br>
        • <strong>DL Frameworks:</strong> TensorFlow, PyTorch<br>
        • <strong>Notebooks:</strong> Jupyter, Google Colab<br>
        • <strong>Datasets:</strong> Kaggle, UCI ML Repository<br><br>
        
        <strong>Career Paths:</strong><br>
        • Machine Learning Engineer<br>
        • AI Research Scientist<br>
        • Data Scientist<br>
        • Computer Vision Engineer<br>
        • NLP Engineer<br>
        • AI Product Manager
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE402 - Artificial Intelligence</strong><br>
    <small>UTel University | Computer Engineering Program</small>
</div>
""", unsafe_allow_html=True)
