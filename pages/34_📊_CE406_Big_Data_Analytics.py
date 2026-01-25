import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="CE406 - Big Data Analytics", page_icon="📊", layout="wide")

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
    
    .hadoop-box {
        background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
        border-left: 5px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .spark-box {
        background: linear-gradient(135deg, #fed7aa 0%, #fdba74 100%);
        border-left: 5px solid #ea580c;
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
    <div style="font-size: 1.2rem; opacity: 0.9;">CE406</div>
    <div class="course-title">Big Data Analytics</div>
    <div>📊 3 Credits | Semester 8 | Hadoop, Spark & Data Processing at Scale</div>
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
    "🐘 Hadoop Ecosystem",
    "⚡ Apache Spark",
    "🔄 Data Processing",
    "📈 Real-Time Analytics",
    "📊 Data Visualization",
    "🤖 ML at Scale",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive big data analytics course covering distributed computing frameworks (Hadoop, Spark), data processing 
        pipelines, real-time analytics, data warehousing, and machine learning at scale. Learn MapReduce, HDFS, Hive, Pig, 
        Spark SQL, Spark Streaming, Kafka, and data visualization tools. Emphasizes hands-on experience with large datasets 
        and distributed systems. Students will build end-to-end data pipelines and perform analytics on petabyte-scale data.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Process large datasets with Hadoop MapReduce",
        "Analyze data at scale with Apache Spark",
        "Build ETL pipelines with Spark and Airflow",
        "Implement real-time analytics with Kafka and Spark Streaming",
        "Query big data with Hive and Spark SQL",
        "Visualize insights with Tableau and Power BI",
        "Train ML models at scale with Spark MLlib",
        "Design data warehouses and data lakes"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Hadoop Ecosystem:**
        - HDFS (Hadoop Distributed File System)
        - MapReduce programming model
        - YARN (resource management)
        - Hive (SQL on Hadoop)
        - Pig (data flow language)
        
        **Apache Spark:**
        - RDDs, DataFrames, Datasets
        - Spark SQL
        - Spark Streaming
        - Spark MLlib
        - PySpark programming
        """)
    
    with col2:
        st.markdown("""
        **Data Processing:**
        - ETL pipelines
        - Data cleaning and transformation
        - Batch vs stream processing
        - Apache Kafka
        - Apache Airflow
        
        **Analytics & ML:**
        - Data warehousing
        - OLAP vs OLTP
        - Data visualization
        - Distributed machine learning
        - Feature engineering at scale
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Hadoop: The Definitive Guide", "author": "Tom White", "type": "Hadoop"},
        {"title": "Learning Spark", "author": "Holden Karau", "type": "Spark"},
        {"title": "Designing Data-Intensive Applications", "author": "Martin Kleppmann", "type": "Architecture"},
        {"title": "The Data Warehouse Toolkit", "author": "Ralph Kimball", "type": "Data Warehousing"}
    ]
    
    for resource in resources:
        title = resource['title']
        author = resource['author']
        rtype = resource['type']
        st.markdown(f"📖 **{title}** by {author} ({rtype})")

# ==================== TAB 2: HADOOP ====================
with tabs[1]:
    st.markdown("## 🐘 Hadoop Ecosystem")
    
    st.markdown("### 1️⃣ HDFS Architecture")
    
    st.markdown("""
    <div class="hadoop-box">
        <strong>Hadoop Distributed File System:</strong><br><br>
        
        <strong>Components:</strong><br>
        • <strong>NameNode:</strong> Master, stores metadata<br>
        • <strong>DataNode:</strong> Workers, store actual data<br>
        • <strong>Secondary NameNode:</strong> Checkpoint for NameNode<br><br>
        
        <strong>Features:</strong><br>
        • Fault-tolerant (replication factor 3)<br>
        • Scalable (petabytes of data)<br>
        • Write-once, read-many<br>
        • Block-based storage (128MB blocks)<br><br>
        
        <strong>HDFS Commands:</strong><br>
        <pre>
# List files
hdfs dfs -ls /

# Create directory
hdfs dfs -mkdir /user/data

# Upload file
hdfs dfs -put localfile.txt /user/data/

# Download file
hdfs dfs -get /user/data/file.txt

# View file
hdfs dfs -cat /user/data/file.txt

# Delete file
hdfs dfs -rm /user/data/file.txt

# Check disk usage
hdfs dfs -du -h /user/data
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ MapReduce")
    
    st.markdown("""
    <div class="theory-box">
        <strong>MapReduce Programming Model:</strong><br><br>
        
        <strong>Phases:</strong><br>
        1. <strong>Map:</strong> Transform input into key-value pairs<br>
        2. <strong>Shuffle & Sort:</strong> Group by key<br>
        3. <strong>Reduce:</strong> Aggregate values for each key<br><br>
        
        <strong>Word Count Example (Python):</strong><br>
        <pre>
from mrjob.job import MRJob

class WordCount(MRJob):
    
    def mapper(self, _, line):
        # Map: emit (word, 1) for each word
        for word in line.split():
            yield word.lower(), 1
    
    def reducer(self, word, counts):
        # Reduce: sum counts for each word
        yield word, sum(counts)

if __name__ == '__main__':
    WordCount.run()
        </pre><br>
        
        <strong>Run:</strong><br>
        <pre>
python wordcount.py input.txt
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Hive")
    
    st.markdown("""
    <div class="hadoop-box">
        <strong>Hive - SQL on Hadoop:</strong><br>
        • Query HDFS data with SQL<br>
        • Converts SQL to MapReduce jobs<br>
        • Schema-on-read<br>
        • Good for batch processing<br><br>
        
        <strong>HiveQL Example:</strong><br>
        <pre>
-- Create table
CREATE TABLE sales (
    id INT,
    product STRING,
    amount DOUBLE,
    date STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

-- Load data
LOAD DATA INPATH '/user/data/sales.csv' INTO TABLE sales;

-- Query
SELECT product, SUM(amount) as total_sales
FROM sales
WHERE date >= '2024-01-01'
GROUP BY product
ORDER BY total_sales DESC
LIMIT 10;

-- Create partitioned table
CREATE TABLE sales_partitioned (
    id INT,
    product STRING,
    amount DOUBLE
)
PARTITIONED BY (year INT, month INT)
STORED AS PARQUET;
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: SPARK ====================
with tabs[2]:
    st.markdown("## ⚡ Apache Spark")
    
    st.markdown("### 1️⃣ Spark Basics")
    
    st.markdown("""
    <div class="spark-box">
        <strong>Why Spark?</strong><br>
        • 100x faster than MapReduce (in-memory)<br>
        • Unified engine (batch, streaming, ML, graph)<br>
        • Easy to use (Python, Scala, Java, R)<br>
        • Lazy evaluation and optimization<br><br>
        
        <strong>PySpark Setup:</strong><br>
        <pre>
from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder \\
    .appName("MyApp") \\
    .config("spark.executor.memory", "4g") \\
    .getOrCreate()

# Read CSV
df = spark.read.csv("data.csv", header=True, inferSchema=True)

# Show data
df.show(5)

# Print schema
df.printSchema()

# Stop session
spark.stop()
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Spark DataFrames")
    
    st.markdown("""
    <div class="theory-box">
        <strong>DataFrame Operations:</strong><br>
        <pre>
from pyspark.sql import functions as F

# Select columns
df.select("name", "age").show()

# Filter rows
df.filter(df.age > 25).show()

# Group by and aggregate
df.groupBy("department") \\
  .agg(F.avg("salary").alias("avg_salary")) \\
  .show()

# Join DataFrames
df1.join(df2, df1.id == df2.user_id, "inner").show()

# Add new column
df = df.withColumn("age_group", 
    F.when(df.age < 18, "minor")
     .when(df.age < 65, "adult")
     .otherwise("senior"))

# Sort
df.orderBy(F.desc("salary")).show()

# Write to Parquet
df.write.parquet("output.parquet", mode="overwrite")
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Spark SQL")
    
    st.markdown("""
    <div class="spark-box">
        <strong>SQL Queries in Spark:</strong><br>
        <pre>
# Register DataFrame as temp view
df.createOrReplaceTempView("sales")

# Run SQL query
result = spark.sql(\"\"\"
    SELECT 
        product,
        SUM(amount) as total_sales,
        COUNT(*) as num_transactions
    FROM sales
    WHERE date >= '2024-01-01'
    GROUP BY product
    HAVING total_sales > 10000
    ORDER BY total_sales DESC
\"\"\")

result.show()

# Window functions
spark.sql(\"\"\"
    SELECT 
        product,
        amount,
        RANK() OVER (PARTITION BY category ORDER BY amount DESC) as rank
    FROM sales
\"\"\").show()
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: DATA PROCESSING ====================
with tabs[3]:
    st.markdown("## 🔄 Data Processing")
    
    st.markdown("### 1️⃣ ETL Pipelines")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Extract, Transform, Load:</strong><br><br>
        
        <strong>Extract:</strong><br>
        <pre>
# Read from multiple sources
df_csv = spark.read.csv("data.csv", header=True)
df_json = spark.read.json("data.json")
df_parquet = spark.read.parquet("data.parquet")

# Read from database
df_db = spark.read \\
    .format("jdbc") \\
    .option("url", "jdbc:postgresql://localhost:5432/db") \\
    .option("dbtable", "sales") \\
    .option("user", "username") \\
    .option("password", "password") \\
    .load()
        </pre><br>
        
        <strong>Transform:</strong><br>
        <pre>
from pyspark.sql import functions as F

# Data cleaning
df_clean = df \\
    .dropna() \\
    .dropDuplicates() \\
    .withColumn("amount", F.col("amount").cast("double")) \\
    .withColumn("date", F.to_date("date", "yyyy-MM-dd"))

# Feature engineering
df_features = df_clean \\
    .withColumn("year", F.year("date")) \\
    .withColumn("month", F.month("date")) \\
    .withColumn("day_of_week", F.dayofweek("date"))
        </pre><br>
        
        <strong>Load:</strong><br>
        <pre>
# Write to data warehouse
df_features.write \\
    .mode("overwrite") \\
    .partitionBy("year", "month") \\
    .parquet("warehouse/sales")
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Apache Airflow")
    
    st.markdown("""
    <div class="hadoop-box">
        <strong>Workflow Orchestration:</strong><br>
        <pre>
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'data-team',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    description='Daily ETL pipeline',
    schedule_interval='0 2 * * *',  # 2 AM daily
    start_date=datetime(2024, 1, 1),
    catchup=False,
)

def extract_data():
    # Extract logic
    pass

def transform_data():
    # Transform logic
    pass

def load_data():
    # Load logic
    pass

extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform_data,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load_data,
    dag=dag,
)

# Define dependencies
extract_task >> transform_task >> load_task
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: REAL-TIME ====================
with tabs[4]:
    st.markdown("## 📈 Real-Time Analytics")
    
    st.markdown("### 1️⃣ Apache Kafka")
    
    st.markdown("""
    <div class="spark-box">
        <strong>Distributed Streaming Platform:</strong><br><br>
        
        <strong>Producer (Python):</strong><br>
        <pre>
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send message
data = {'user_id': 123, 'action': 'click', 'timestamp': '2024-01-01'}
producer.send('events', value=data)
producer.flush()
        </pre><br>
        
        <strong>Consumer (Python):</strong><br>
        <pre>
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'events',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='analytics-group'
)

for message in consumer:
    data = message.value
    print(f"Received: {data}")
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Spark Streaming")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Structured Streaming:</strong><br>
        <pre>
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder \\
    .appName("StreamingApp") \\
    .getOrCreate()

# Read from Kafka
df = spark.readStream \\
    .format("kafka") \\
    .option("kafka.bootstrap.servers", "localhost:9092") \\
    .option("subscribe", "events") \\
    .load()

# Parse JSON
events = df.selectExpr("CAST(value AS STRING)") \\
    .select(from_json(col("value"), schema).alias("data")) \\
    .select("data.*")

# Windowed aggregation
windowed_counts = events \\
    .withWatermark("timestamp", "10 minutes") \\
    .groupBy(
        window("timestamp", "5 minutes"),
        "action"
    ) \\
    .count()

# Write to console
query = windowed_counts.writeStream \\
    .outputMode("update") \\
    .format("console") \\
    .start()

query.awaitTermination()
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: VISUALIZATION ====================
with tabs[5]:
    st.markdown("## 📊 Data Visualization")
    
    st.markdown("### 1️⃣ Visualization Tools")
    
    tools_data = {
        'Tool': ['Tableau', 'Power BI', 'Apache Superset', 'Plotly', 'Matplotlib'],
        'Type': ['Commercial', 'Commercial', 'Open Source', 'Library', 'Library'],
        'Best For': [
            'Interactive dashboards',
            'Microsoft ecosystem',
            'Open source alternative',
            'Web-based charts',
            'Static plots'
        ],
        'Big Data Support': ['Yes', 'Yes', 'Yes', 'Limited', 'Limited']
    }
    
    df_tools = pd.DataFrame(tools_data)
    st.dataframe(df_tools, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Python Visualization")
    
    st.markdown("""
    <div class="ml-box">
        <strong>Plotly Example:</strong><br>
        <pre>
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    'product': ['A', 'B', 'C', 'D'],
    'sales': [100, 150, 80, 120],
    'profit': [20, 35, 15, 25]
})

# Bar chart
fig = px.bar(df, x='product', y='sales', 
             title='Sales by Product')
fig.show()

# Scatter plot
fig = px.scatter(df, x='sales', y='profit', 
                 size='sales', color='product',
                 title='Sales vs Profit')
fig.show()
        </pre><br>
        
        <strong>Dashboard with Streamlit:</strong><br>
        <pre>
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Sales Dashboard")

# Load data
df = pd.read_csv("sales.csv")

# Filters
product = st.selectbox("Select Product", df['product'].unique())
filtered_df = df[df['product'] == product]

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${filtered_df['sales'].sum():,.0f}")
col2.metric("Avg Order", f"${filtered_df['sales'].mean():,.0f}")
col3.metric("Orders", len(filtered_df))

# Chart
fig = px.line(filtered_df, x='date', y='sales')
st.plotly_chart(fig)
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: ML AT SCALE ====================
with tabs[6]:
    st.markdown("## 🤖 Machine Learning at Scale")
    
    st.markdown("### 1️⃣ Spark MLlib")
    
    st.markdown("""
    <div class="spark-box">
        <strong>Distributed Machine Learning:</strong><br>
        <pre>
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Prepare features
assembler = VectorAssembler(
    inputCols=['feature1', 'feature2', 'feature3'],
    outputCol='features'
)

df_features = assembler.transform(df)

# Split data
train, test = df_features.randomSplit([0.8, 0.2], seed=42)

# Train model
lr = LogisticRegression(
    featuresCol='features',
    labelCol='label',
    maxIter=10
)

model = lr.fit(train)

# Predict
predictions = model.transform(test)

# Evaluate
evaluator = BinaryClassificationEvaluator()
auc = evaluator.evaluate(predictions)
print(f"AUC: {auc}")
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Feature Engineering")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Feature Transformations:</strong><br>
        <pre>
from pyspark.ml.feature import StringIndexer, OneHotEncoder
from pyspark.ml.feature import StandardScaler, MinMaxScaler
from pyspark.ml import Pipeline

# Categorical encoding
indexer = StringIndexer(inputCol="category", outputCol="category_index")
encoder = OneHotEncoder(inputCol="category_index", outputCol="category_vec")

# Numerical scaling
scaler = StandardScaler(inputCol="features", outputCol="scaled_features")

# Pipeline
pipeline = Pipeline(stages=[indexer, encoder, scaler])
model = pipeline.fit(df)
transformed_df = model.transform(df)
        </pre><br>
        
        <strong>Distributed Hyperparameter Tuning:</strong><br>
        <pre>
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

# Parameter grid
paramGrid = ParamGridBuilder() \\
    .addGrid(lr.regParam, [0.01, 0.1, 1.0]) \\
    .addGrid(lr.elasticNetParam, [0.0, 0.5, 1.0]) \\
    .build()

# Cross validation
cv = CrossValidator(
    estimator=lr,
    estimatorParamMaps=paramGrid,
    evaluator=evaluator,
    numFolds=5
)

cvModel = cv.fit(train)
best_model = cvModel.bestModel
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: YOUTUBE ====================
with tabs[7]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning Big Data Analytics</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {"title": "Big Data Explained", "channel": "IBM Technology", "url": "https://www.youtube.com/watch?v=zez2Tv-bcXY", "description": "Big data fundamentals", "duration": "~10 min"},
        {"title": "Hadoop Tutorial", "channel": "Edureka", "url": "https://www.youtube.com/watch?v=mafw2-CVYnA", "description": "Hadoop basics", "duration": "~8 hours"},
        {"title": "Apache Spark Tutorial", "channel": "freeCodeCamp.org", "url": "https://www.youtube.com/watch?v=_C8kWso4ne4", "description": "Spark fundamentals", "duration": "~5 hours"}
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
        {"title": "PySpark Complete Course", "channel": "Krish Naik", "url": "https://www.youtube.com/watch?v=_C8kWso4ne4", "description": "PySpark in depth", "duration": "~10 hours"},
        {"title": "Apache Kafka Tutorial", "channel": "Confluent", "url": "https://www.youtube.com/c/Confluent", "description": "Kafka streaming", "duration": "Channel"},
        {"title": "Data Engineering", "channel": "Seattle Data Guy", "url": "https://www.youtube.com/c/SeattleDataGuy", "description": "Data pipelines", "duration": "Channel"}
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
        {"title": "Spark Performance Tuning", "channel": "Databricks", "url": "https://www.youtube.com/c/Databricks", "description": "Optimization techniques", "duration": "Channel"},
        {"title": "Data Architecture", "channel": "Data Engineering", "url": "https://www.youtube.com/c/DataEngineeringTV", "description": "Architecture patterns", "duration": "Channel"},
        {"title": "MLOps at Scale", "channel": "MLOps Community", "url": "https://www.youtube.com/c/MLOpsCommunity", "description": "Production ML", "duration": "Channel"}
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
        1. Learn Python and SQL fundamentals<br>
        2. Understand distributed systems concepts<br>
        3. Practice with Hadoop and HDFS<br>
        4. Master Apache Spark and PySpark<br>
        5. Build ETL pipelines with Airflow<br>
        6. Learn streaming with Kafka<br>
        7. Practice data visualization<br>
        8. Work on real-world projects<br><br>
        
        <strong>Essential Tools:</strong><br>
        • <strong>Big Data:</strong> Hadoop, Spark, Hive<br>
        • <strong>Streaming:</strong> Kafka, Spark Streaming<br>
        • <strong>Orchestration:</strong> Airflow, Luigi<br>
        • <strong>Visualization:</strong> Tableau, Power BI, Plotly<br>
        • <strong>Cloud:</strong> AWS EMR, Databricks, GCP Dataproc<br><br>
        
        <strong>Career Paths:</strong><br>
        • Data Engineer<br>
        • Big Data Engineer<br>
        • Data Scientist<br>
        • Analytics Engineer<br>
        • ML Engineer<br>
        • Data Architect
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE406 - Big Data Analytics</strong><br>
    <small>UTel University | Computer Engineering Program</small>
</div>
""", unsafe_allow_html=True)
