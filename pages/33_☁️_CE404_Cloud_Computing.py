import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="CE404 - Cloud Computing", page_icon="☁️", layout="wide")

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
        background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%);
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
        background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);
        border-left: 5px solid #0ea5e9;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .aws-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .docker-box {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .k8s-box {
        background: linear-gradient(135deg, #ddd6fe 0%, #c4b5fd 100%);
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
    <div style="font-size: 1.2rem; opacity: 0.9;">CE404</div>
    <div class="course-title">Cloud Computing</div>
    <div>☁️ 3 Credits | Semester 8 | AWS, Docker, Kubernetes & DevOps</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "8")
with col3:
    st.metric("Difficulty", "6/7")
with col4:
    st.metric("Hours/Week", "7")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "☁️ Cloud Platforms",
    "🐳 Docker",
    "⚓ Kubernetes",
    "🚀 Serverless",
    "🔄 DevOps & CI/CD",
    "🏗️ Cloud Architecture",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive cloud computing course covering major cloud platforms (AWS, Azure, GCP), containerization (Docker), 
        orchestration (Kubernetes), serverless computing, and DevOps practices. Learn cloud architecture patterns, 
        infrastructure as code (Terraform), CI/CD pipelines, microservices, and cloud-native application development. 
        Emphasizes hands-on labs with real cloud deployments. Students will build and deploy scalable cloud applications 
        using industry-standard tools and best practices.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Deploy applications to AWS, Azure, and GCP",
        "Containerize applications with Docker",
        "Orchestrate containers with Kubernetes",
        "Build serverless applications (Lambda, Cloud Functions)",
        "Implement CI/CD pipelines (GitHub Actions, Jenkins)",
        "Use Infrastructure as Code (Terraform, CloudFormation)",
        "Design cloud-native microservices architectures",
        "Optimize cloud costs and performance"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Cloud Fundamentals:**
        - IaaS, PaaS, SaaS models
        - Cloud service models
        - Regions and availability zones
        - Virtual machines and networking
        - Storage solutions (S3, EBS, Blob)
        
        **Containers & Orchestration:**
        - Docker containers and images
        - Docker Compose
        - Kubernetes pods and deployments
        - Services and ingress
        - Helm charts
        """)
    
    with col2:
        st.markdown("""
        **Serverless & DevOps:**
        - AWS Lambda, Azure Functions
        - API Gateway
        - Event-driven architecture
        - CI/CD pipelines
        - Infrastructure as Code
        
        **Architecture:**
        - Microservices patterns
        - Load balancing and auto-scaling
        - Monitoring and logging
        - Security and compliance
        - Cost optimization
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "AWS Certified Solutions Architect", "author": "AWS", "type": "Certification"},
        {"title": "Docker Deep Dive", "author": "Nigel Poulton", "type": "Docker"},
        {"title": "Kubernetes in Action", "author": "Marko Lukša", "type": "Kubernetes"},
        {"title": "The Phoenix Project", "author": "Gene Kim", "type": "DevOps"}
    ]
    
    for resource in resources:
        title = resource['title']
        author = resource['author']
        rtype = resource['type']
        st.markdown(f"📖 **{title}** by {author} ({rtype})")

# ==================== TAB 2: CLOUD PLATFORMS ====================
with tabs[1]:
    st.markdown("## ☁️ Cloud Platforms")
    
    st.markdown("### 1️⃣ Platform Comparison")
    
    platform_data = {
        'Service': ['Compute', 'Storage', 'Database', 'Serverless', 'Container'],
        'AWS': ['EC2', 'S3, EBS', 'RDS, DynamoDB', 'Lambda', 'ECS, EKS'],
        'Azure': ['Virtual Machines', 'Blob Storage', 'SQL Database, Cosmos DB', 'Functions', 'AKS'],
        'GCP': ['Compute Engine', 'Cloud Storage', 'Cloud SQL, Firestore', 'Cloud Functions', 'GKE']
    }
    
    df_platform = pd.DataFrame(platform_data)
    st.dataframe(df_platform, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ AWS Services")
    
    st.markdown("""
    <div class="aws-box">
        <strong>Compute:</strong><br>
        • <strong>EC2:</strong> Virtual machines<br>
        • <strong>Lambda:</strong> Serverless functions<br>
        • <strong>ECS/EKS:</strong> Container orchestration<br>
        • <strong>Elastic Beanstalk:</strong> PaaS for web apps<br><br>
        
        <strong>Storage:</strong><br>
        • <strong>S3:</strong> Object storage (files, backups)<br>
        • <strong>EBS:</strong> Block storage (EC2 volumes)<br>
        • <strong>EFS:</strong> File storage (NFS)<br>
        • <strong>Glacier:</strong> Archive storage<br><br>
        
        <strong>Database:</strong><br>
        • <strong>RDS:</strong> Managed relational DB (MySQL, PostgreSQL)<br>
        • <strong>DynamoDB:</strong> NoSQL database<br>
        • <strong>Aurora:</strong> High-performance MySQL/PostgreSQL<br>
        • <strong>ElastiCache:</strong> Redis/Memcached<br><br>
        
        <strong>Networking:</strong><br>
        • <strong>VPC:</strong> Virtual private cloud<br>
        • <strong>Route 53:</strong> DNS service<br>
        • <strong>CloudFront:</strong> CDN<br>
        • <strong>ELB:</strong> Load balancer
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Getting Started with AWS")
    
    st.markdown("""
    <div class="theory-box">
        <strong>AWS CLI Setup:</strong><br>
        <pre>
# Install AWS CLI
pip install awscli

# Configure credentials
aws configure
# Enter: Access Key ID, Secret Access Key, Region, Output format

# Test connection
aws s3 ls

# Create S3 bucket
aws s3 mb s3://my-bucket-name

# Upload file
aws s3 cp file.txt s3://my-bucket-name/

# Launch EC2 instance
aws ec2 run-instances \\
  --image-id ami-0c55b159cbfafe1f0 \\
  --instance-type t2.micro \\
  --key-name my-key-pair
        </pre><br>
        
        <strong>Free Tier:</strong><br>
        • 750 hours EC2 t2.micro per month<br>
        • 5GB S3 storage<br>
        • 1 million Lambda requests<br>
        • 750 hours RDS db.t2.micro<br>
        • Valid for 12 months
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: DOCKER ====================
with tabs[2]:
    st.markdown("## 🐳 Docker")
    
    st.markdown("### 1️⃣ Docker Basics")
    
    st.markdown("""
    <div class="docker-box">
        <strong>What is Docker?</strong><br>
        • Containerization platform<br>
        • Package app + dependencies<br>
        • Consistent across environments<br>
        • Lightweight (vs VMs)<br><br>
        
        <strong>Core Concepts:</strong><br>
        • <strong>Image:</strong> Blueprint for container<br>
        • <strong>Container:</strong> Running instance of image<br>
        • <strong>Dockerfile:</strong> Instructions to build image<br>
        • <strong>Registry:</strong> Store images (Docker Hub)<br><br>
        
        <strong>Basic Commands:</strong><br>
        <pre>
# Pull image from Docker Hub
docker pull nginx

# Run container
docker run -d -p 80:80 nginx

# List running containers
docker ps

# Stop container
docker stop container_id

# Remove container
docker rm container_id

# List images
docker images

# Remove image
docker rmi image_name
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Dockerfile")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Example Dockerfile (Node.js app):</strong><br>
        <pre>
# Base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy app files
COPY . .

# Expose port
EXPOSE 3000

# Start command
CMD ["npm", "start"]
        </pre><br>
        
        <strong>Build and Run:</strong><br>
        <pre>
# Build image
docker build -t my-app:1.0 .

# Run container
docker run -d -p 3000:3000 my-app:1.0

# View logs
docker logs container_id

# Execute command in container
docker exec -it container_id sh
        </pre><br>
        
        <strong>Best Practices:</strong><br>
        • Use official base images<br>
        • Minimize layers (combine RUN commands)<br>
        • Use .dockerignore<br>
        • Don't run as root<br>
        • Multi-stage builds for smaller images
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Docker Compose")
    
    st.markdown("""
    <div class="docker-box">
        <strong>Multi-container Applications:</strong><br>
        <pre>
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://db:5432/mydb
    depends_on:
      - db
  
  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
        </pre><br>
        
        <strong>Commands:</strong><br>
        <pre>
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild images
docker-compose build
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: KUBERNETES ====================
with tabs[3]:
    st.markdown("## ⚓ Kubernetes")
    
    st.markdown("### 1️⃣ Kubernetes Architecture")
    
    st.markdown("""
    <div class="k8s-box">
        <strong>Components:</strong><br><br>
        
        <strong>Control Plane:</strong><br>
        • <strong>API Server:</strong> Frontend for K8s<br>
        • <strong>etcd:</strong> Key-value store<br>
        • <strong>Scheduler:</strong> Assigns pods to nodes<br>
        • <strong>Controller Manager:</strong> Manages controllers<br><br>
        
        <strong>Worker Nodes:</strong><br>
        • <strong>Kubelet:</strong> Agent on each node<br>
        • <strong>Container Runtime:</strong> Docker, containerd<br>
        • <strong>Kube-proxy:</strong> Network proxy<br><br>
        
        <strong>Key Resources:</strong><br>
        • <strong>Pod:</strong> Smallest deployable unit<br>
        • <strong>Deployment:</strong> Manages replica sets<br>
        • <strong>Service:</strong> Exposes pods<br>
        • <strong>Ingress:</strong> HTTP routing<br>
        • <strong>ConfigMap/Secret:</strong> Configuration
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Kubernetes Manifests")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Deployment YAML:</strong><br>
        <pre>
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-app
        image: my-app:1.0
        ports:
        - containerPort: 3000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: url
        </pre><br>
        
        <strong>Service YAML:</strong><br>
        <pre>
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
spec:
  type: LoadBalancer
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 3000
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ kubectl Commands")
    
    st.markdown("""
    <div class="k8s-box">
        <strong>Basic Commands:</strong><br>
        <pre>
# Apply manifest
kubectl apply -f deployment.yaml

# Get resources
kubectl get pods
kubectl get deployments
kubectl get services

# Describe resource
kubectl describe pod pod-name

# View logs
kubectl logs pod-name

# Execute command in pod
kubectl exec -it pod-name -- sh

# Scale deployment
kubectl scale deployment my-app --replicas=5

# Delete resource
kubectl delete deployment my-app

# Port forward
kubectl port-forward pod-name 8080:3000
        </pre><br>
        
        <strong>Managed Kubernetes:</strong><br>
        • <strong>EKS:</strong> AWS Elastic Kubernetes Service<br>
        • <strong>AKS:</strong> Azure Kubernetes Service<br>
        • <strong>GKE:</strong> Google Kubernetes Engine<br>
        • Handles control plane management
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: SERVERLESS ====================
with tabs[4]:
    st.markdown("## 🚀 Serverless")
    
    st.markdown("### 1️⃣ AWS Lambda")
    
    st.markdown("""
    <div class="aws-box">
        <strong>What is Serverless?</strong><br>
        • No server management<br>
        • Pay per execution<br>
        • Auto-scaling<br>
        • Event-driven<br><br>
        
        <strong>Lambda Function (Node.js):</strong><br>
        <pre>
exports.handler = async (event) => {
    const name = event.queryStringParameters?.name || 'World';
    
    return {
        statusCode: 200,
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            message: `Hello, ${name}!`,
        }),
    };
};
        </pre><br>
        
        <strong>Lambda Triggers:</strong><br>
        • API Gateway (HTTP requests)<br>
        • S3 events (file upload)<br>
        • DynamoDB streams<br>
        • CloudWatch Events (cron)<br>
        • SNS/SQS messages<br><br>
        
        <strong>Limitations:</strong><br>
        • Max execution time: 15 minutes<br>
        • Max memory: 10GB<br>
        • Cold start latency<br>
        • Stateless (use external storage)
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Serverless Framework")
    
    st.markdown("""
    <div class="theory-box">
        <strong>serverless.yml:</strong><br>
        <pre>
service: my-serverless-app

provider:
  name: aws
  runtime: nodejs18.x
  region: us-east-1

functions:
  hello:
    handler: handler.hello
    events:
      - http:
          path: hello
          method: get
  
  processImage:
    handler: handler.processImage
    events:
      - s3:
          bucket: my-images
          event: s3:ObjectCreated:*

resources:
  Resources:
    MyDynamoDBTable:
      Type: AWS::DynamoDB::Table
      Properties:
        TableName: my-table
        AttributeDefinitions:
          - AttributeName: id
            AttributeType: S
        KeySchema:
          - AttributeName: id
            KeyType: HASH
        BillingMode: PAY_PER_REQUEST
        </pre><br>
        
        <strong>Deploy:</strong><br>
        <pre>
# Install Serverless Framework
npm install -g serverless

# Deploy
serverless deploy

# Invoke function
serverless invoke -f hello

# View logs
serverless logs -f hello -t
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: DEVOPS ====================
with tabs[5]:
    st.markdown("## 🔄 DevOps & CI/CD")
    
    st.markdown("### 1️⃣ CI/CD Pipeline")
    
    st.markdown("""
    <div class="docker-box">
        <strong>GitHub Actions Workflow:</strong><br>
        <pre>
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run tests
        run: npm test
      
      - name: Run linter
        run: npm run lint

  build-and-deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Build Docker image
        run: docker build -t my-app:${{ github.sha }} .
      
      - name: Push to Docker Hub
        run: |
          echo ${{ secrets.DOCKER_PASSWORD }} | docker login -u ${{ secrets.DOCKER_USERNAME }} --password-stdin
          docker push my-app:${{ github.sha }}
      
      - name: Deploy to Kubernetes
        run: |
          kubectl set image deployment/my-app my-app=my-app:${{ github.sha }}
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Infrastructure as Code")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Terraform Example:</strong><br>
        <pre>
# main.tf
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  
  tags = {
    Name = "WebServer"
  }
}

resource "aws_s3_bucket" "data" {
  bucket = "my-data-bucket"
  
  versioning {
    enabled = true
  }
}

output "instance_ip" {
  value = aws_instance.web.public_ip
}
        </pre><br>
        
        <strong>Terraform Commands:</strong><br>
        <pre>
# Initialize
terraform init

# Plan changes
terraform plan

# Apply changes
terraform apply

# Destroy resources
terraform destroy
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: ARCHITECTURE ====================
with tabs[6]:
    st.markdown("## 🏗️ Cloud Architecture")
    
    st.markdown("### 1️⃣ Microservices Patterns")
    
    st.markdown("""
    <div class="k8s-box">
        <strong>Microservices Architecture:</strong><br>
        • Independent services<br>
        • Each service has own database<br>
        • Communicate via APIs (REST, gRPC)<br>
        • Independently deployable<br><br>
        
        <strong>Benefits:</strong><br>
        • Scalability (scale services independently)<br>
        • Flexibility (different tech stacks)<br>
        • Resilience (failure isolation)<br>
        • Faster deployment<br><br>
        
        <strong>Challenges:</strong><br>
        • Distributed system complexity<br>
        • Data consistency<br>
        • Network latency<br>
        • Monitoring and debugging<br><br>
        
        <strong>Patterns:</strong><br>
        • <strong>API Gateway:</strong> Single entry point<br>
        • <strong>Service Mesh:</strong> Service-to-service communication<br>
        • <strong>Circuit Breaker:</strong> Prevent cascade failures<br>
        • <strong>Saga:</strong> Distributed transactions<br>
        • <strong>CQRS:</strong> Command Query Responsibility Segregation
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ High Availability")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Load Balancing:</strong><br>
        • Distribute traffic across servers<br>
        • Health checks<br>
        • Session persistence<br>
        • Types: Application, Network, Classic<br><br>
        
        <strong>Auto Scaling:</strong><br>
        • Scale based on metrics (CPU, memory)<br>
        • Scheduled scaling<br>
        • Target tracking<br>
        • Min/max instances<br><br>
        
        <strong>Multi-Region Deployment:</strong><br>
        • Deploy to multiple regions<br>
        • Route 53 for DNS failover<br>
        • Data replication<br>
        • Disaster recovery<br><br>
        
        <strong>Monitoring:</strong><br>
        • CloudWatch (AWS)<br>
        • Prometheus + Grafana<br>
        • ELK Stack (Elasticsearch, Logstash, Kibana)<br>
        • Datadog, New Relic
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: YOUTUBE ====================
with tabs[7]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning Cloud Computing</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {"title": "AWS Certified Cloud Practitioner", "channel": "freeCodeCamp.org", "url": "https://www.youtube.com/watch?v=SOTamWNgDKc", "description": "AWS fundamentals", "duration": "~4 hours"},
        {"title": "Docker Tutorial", "channel": "TechWorld with Nana", "url": "https://www.youtube.com/watch?v=3c-iBn73dDE", "description": "Docker complete course", "duration": "~3 hours"},
        {"title": "Cloud Computing Explained", "channel": "IBM Technology", "url": "https://www.youtube.com/c/IBMTechnology", "description": "Cloud concepts", "duration": "Channel"}
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
        {"title": "Kubernetes Course", "channel": "TechWorld with Nana", "url": "https://www.youtube.com/watch?v=X48VuDVv0do", "description": "Complete K8s tutorial", "duration": "~4 hours"},
        {"title": "AWS Solutions Architect", "channel": "Stephane Maarek", "url": "https://www.youtube.com/c/StephaneMaarek", "description": "AWS certification prep", "duration": "Channel"},
        {"title": "DevOps Bootcamp", "channel": "TechWorld with Nana", "url": "https://www.youtube.com/watch?v=hQcFE0RD0cQ", "description": "DevOps complete course", "duration": "~7 hours"}
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
        {"title": "Kubernetes Production Patterns", "channel": "CNCF", "url": "https://www.youtube.com/c/cloudnativefdn", "description": "Advanced K8s", "duration": "Channel"},
        {"title": "AWS re:Invent", "channel": "AWS Events", "url": "https://www.youtube.com/c/AWSEventsChannel", "description": "AWS advanced topics", "duration": "Channel"},
        {"title": "Terraform Deep Dive", "channel": "HashiCorp", "url": "https://www.youtube.com/c/HashiCorp", "description": "IaC advanced", "duration": "Channel"}
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
        1. Learn cloud fundamentals (IaaS, PaaS, SaaS)<br>
        2. Get AWS/Azure/GCP free tier account<br>
        3. Master Docker and containerization<br>
        4. Learn Kubernetes basics<br>
        5. Build CI/CD pipelines<br>
        6. Study Infrastructure as Code (Terraform)<br>
        7. Practice with real projects<br>
        8. Get certified (AWS SAA, CKA)<br><br>
        
        <strong>Essential Tools:</strong><br>
        • <strong>Cloud:</strong> AWS CLI, Azure CLI, gcloud<br>
        • <strong>Containers:</strong> Docker, Docker Compose<br>
        • <strong>Orchestration:</strong> kubectl, Helm<br>
        • <strong>IaC:</strong> Terraform, CloudFormation<br>
        • <strong>CI/CD:</strong> GitHub Actions, Jenkins, GitLab CI<br><br>
        
        <strong>Career Paths:</strong><br>
        • Cloud Engineer<br>
        • DevOps Engineer<br>
        • Site Reliability Engineer (SRE)<br>
        • Cloud Architect<br>
        • Platform Engineer<br>
        • Kubernetes Administrator
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE404 - Cloud Computing</strong><br>
    <small>UTel University | Computer Engineering Program</small>
</div>
""", unsafe_allow_html=True)
