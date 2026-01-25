import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="CE408 - Internet of Things", page_icon="🌐", layout="wide")

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
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
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
        background: linear-gradient(135deg, #e0e7ff 0%, #c7d2fe 100%);
        border-left: 5px solid #6366f1;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .arduino-box {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .raspberry-box {
        background: linear-gradient(135deg, #fecdd3 0%, #fda4af 100%);
        border-left: 5px solid #f43f5e;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .mqtt-box {
        background: linear-gradient(135deg, #d1fae5 0%, #a7f3d0 100%);
        border-left: 5px solid #10b981;
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
    <div style="font-size: 1.2rem; opacity: 0.9;">CE408</div>
    <div class="course-title">Internet of Things (IoT)</div>
    <div>🌐 3 Credits | Semester 8 | Arduino, Raspberry Pi & Edge Computing</div>
</div>
""", unsafe_allow_html=True)

# Course Info
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Credits", "3")
with col2:
    st.metric("Semester", "8")
with col3:
    st.metric("Difficulty", "5/7")
with col4:
    st.metric("Hours/Week", "7")

st.markdown("---")

# Navigation tabs
tabs = st.tabs([
    "📚 Overview",
    "🔧 Arduino",
    "🍓 Raspberry Pi",
    "📡 Sensors & Actuators",
    "💬 Communication Protocols",
    "⚡ Edge Computing",
    "🔐 IoT Security",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive Internet of Things course covering IoT architecture, embedded systems, sensors, actuators, 
        communication protocols, edge computing, and IoT security. Learn Arduino and Raspberry Pi programming, MQTT, 
        CoAP, LoRaWAN, sensor integration, data processing at the edge, and IoT cloud platforms. Emphasizes hands-on 
        projects with real hardware. Students will build complete IoT systems from sensor to cloud, including smart home 
        automation, environmental monitoring, and industrial IoT applications.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Program Arduino and Raspberry Pi for IoT applications",
        "Interface with sensors (temperature, humidity, motion) and actuators",
        "Implement MQTT and CoAP communication protocols",
        "Build edge computing solutions for real-time processing",
        "Design and deploy IoT cloud architectures",
        "Secure IoT devices and networks",
        "Develop smart home and industrial IoT systems",
        "Optimize power consumption for battery-powered devices"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Hardware:**
        - Arduino (Uno, Nano, ESP32)
        - Raspberry Pi (3, 4, Zero)
        - Sensors (DHT22, PIR, ultrasonic)
        - Actuators (servo, relay, LED)
        - Communication modules (WiFi, Bluetooth, LoRa)
        
        **Protocols:**
        - MQTT (Message Queue Telemetry Transport)
        - CoAP (Constrained Application Protocol)
        - HTTP/REST APIs
        - WebSockets
        - LoRaWAN
        """)
    
    with col2:
        st.markdown("""
        **Edge & Cloud:**
        - Edge computing and fog computing
        - AWS IoT Core
        - Azure IoT Hub
        - Google Cloud IoT
        - Node-RED
        
        **Applications:**
        - Smart home automation
        - Environmental monitoring
        - Industrial IoT (IIoT)
        - Wearable devices
        - Smart agriculture
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "Arduino Cookbook", "author": "Michael Margolis", "type": "Arduino"},
        {"title": "Raspberry Pi Cookbook", "author": "Simon Monk", "type": "Raspberry Pi"},
        {"title": "IoT Fundamentals", "author": "David Hanes", "type": "IoT"},
        {"title": "MQTT Essentials", "author": "HiveMQ", "type": "Protocols"}
    ]
    
    for resource in resources:
        title = resource['title']
        author = resource['author']
        rtype = resource['type']
        st.markdown(f"📖 **{title}** by {author} ({rtype})")

# ==================== TAB 2: ARDUINO ====================
with tabs[1]:
    st.markdown("## 🔧 Arduino")
    
    st.markdown("### 1️⃣ Arduino Basics")
    
    st.markdown("""
    <div class="arduino-box">
        <strong>Arduino Boards:</strong><br>
        • <strong>Arduino Uno:</strong> Beginner-friendly, ATmega328P<br>
        • <strong>Arduino Nano:</strong> Compact, breadboard-friendly<br>
        • <strong>ESP32:</strong> WiFi + Bluetooth, dual-core<br>
        • <strong>Arduino Mega:</strong> More pins, more memory<br><br>
        
        <strong>Basic Blink Example:</strong><br>
        <pre>
// Blink LED on pin 13
void setup() {
  pinMode(13, OUTPUT);  // Set pin 13 as output
}

void loop() {
  digitalWrite(13, HIGH);  // Turn LED on
  delay(1000);             // Wait 1 second
  digitalWrite(13, LOW);   // Turn LED off
  delay(1000);             // Wait 1 second
}
        </pre><br>
        
        <strong>Serial Communication:</strong><br>
        <pre>
void setup() {
  Serial.begin(9600);  // Start serial at 9600 baud
}

void loop() {
  Serial.println("Hello, IoT!");
  delay(1000);
}
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Sensor Integration")
    
    st.markdown("""
    <div class="theory-box">
        <strong>DHT22 Temperature & Humidity Sensor:</strong><br>
        <pre>
#include <DHT.h>

#define DHTPIN 2       // Pin connected to DHT22
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  
  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.print("%  Temperature: ");
  Serial.print(temperature);
  Serial.println("°C");
  
  delay(2000);
}
        </pre><br>
        
        <strong>Ultrasonic Distance Sensor (HC-SR04):</strong><br>
        <pre>
#define TRIG_PIN 9
#define ECHO_PIN 10

void setup() {
  Serial.begin(9600);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  // Send pulse
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  
  // Measure echo
  long duration = pulseIn(ECHO_PIN, HIGH);
  float distance = duration * 0.034 / 2;  // cm
  
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  
  delay(500);
}
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ WiFi & IoT")
    
    st.markdown("""
    <div class="arduino-box">
        <strong>ESP32 WiFi Connection:</strong><br>
        <pre>
#include <WiFi.h>

const char* ssid = "YourWiFiSSID";
const char* password = "YourPassword";

void setup() {
  Serial.begin(115200);
  
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.println("WiFi connected!");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // Your IoT code here
}
        </pre><br>
        
        <strong>Send Data to Cloud (HTTP POST):</strong><br>
        <pre>
#include <HTTPClient.h>

void sendData(float temperature, float humidity) {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    
    http.begin("http://your-server.com/api/data");
    http.addHeader("Content-Type", "application/json");
    
    String payload = "{\"temperature\":" + String(temperature) + 
                     ",\"humidity\":" + String(humidity) + "}";
    
    int httpResponseCode = http.POST(payload);
    
    if (httpResponseCode > 0) {
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
    }
    
    http.end();
  }
}
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: RASPBERRY PI ====================
with tabs[2]:
    st.markdown("## 🍓 Raspberry Pi")
    
    st.markdown("### 1️⃣ Raspberry Pi Setup")
    
    st.markdown("""
    <div class="raspberry-box">
        <strong>Raspberry Pi Models:</strong><br>
        • <strong>Raspberry Pi 4:</strong> 4GB/8GB RAM, quad-core, USB 3.0<br>
        • <strong>Raspberry Pi Zero W:</strong> Compact, WiFi, low power<br>
        • <strong>Raspberry Pi 3 B+:</strong> Good balance, affordable<br><br>
        
        <strong>GPIO (General Purpose Input/Output):</strong><br>
        • 40 pins (26 GPIO pins)<br>
        • 3.3V logic level (not 5V!)<br>
        • PWM, I2C, SPI, UART support<br><br>
        
        <strong>Python GPIO Library:</strong><br>
        <pre>
import RPi.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
LED_PIN = 18

GPIO.setup(LED_PIN, GPIO.OUT)

# Blink LED
try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Sensor Reading")
    
    st.markdown("""
    <div class="theory-box">
        <strong>DHT22 with Raspberry Pi:</strong><br>
        <pre>
import Adafruit_DHT
import time

# Sensor type and GPIO pin
sensor = Adafruit_DHT.DHT22
pin = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    if humidity is not None and temperature is not None:
        print(f'Temp: {temperature:.1f}°C  Humidity: {humidity:.1f}%')
    else:
        print('Failed to read sensor')
    
    time.sleep(2)
        </pre><br>
        
        <strong>PIR Motion Sensor:</strong><br>
        <pre>
import RPi.GPIO as GPIO
import time

PIR_PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

print("PIR Motion Sensor Ready")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected!")
            time.sleep(1)
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Camera Module")
    
    st.markdown("""
    <div class="raspberry-box">
        <strong>Raspberry Pi Camera:</strong><br>
        <pre>
from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Take photo
camera.start_preview()
sleep(2)
camera.capture('/home/pi/image.jpg')
camera.stop_preview()

# Record video
camera.start_recording('/home/pi/video.h264')
sleep(10)
camera.stop_recording()
        </pre><br>
        
        <strong>Motion Detection with OpenCV:</strong><br>
        <pre>
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while True:
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, 
                                    cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            print("Motion detected!")
            # Take action (save image, send alert, etc.)
    
    frame1 = frame2
    ret, frame2 = cap.read()
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: SENSORS ====================
with tabs[3]:
    st.markdown("## 📡 Sensors & Actuators")
    
    st.markdown("### 1️⃣ Common Sensors")
    
    sensor_data = {
        'Sensor': ['DHT22', 'BMP280', 'PIR', 'HC-SR04', 'MQ-2'],
        'Measures': ['Temp & Humidity', 'Pressure & Altitude', 'Motion', 'Distance', 'Gas/Smoke'],
        'Interface': ['Digital', 'I2C', 'Digital', 'Digital', 'Analog'],
        'Use Case': [
            'Weather station',
            'Altitude tracking',
            'Security system',
            'Parking sensor',
            'Fire detection'
        ]
    }
    
    df_sensors = pd.DataFrame(sensor_data)
    st.dataframe(df_sensors, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Actuators")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Servo Motor Control:</strong><br>
        <pre>
#include <Servo.h>

Servo myservo;

void setup() {
  myservo.attach(9);  // Servo on pin 9
}

void loop() {
  myservo.write(0);    // 0 degrees
  delay(1000);
  myservo.write(90);   // 90 degrees
  delay(1000);
  myservo.write(180);  // 180 degrees
  delay(1000);
}
        </pre><br>
        
        <strong>Relay Control (AC Devices):</strong><br>
        <pre>
#define RELAY_PIN 7

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
}

void loop() {
  digitalWrite(RELAY_PIN, HIGH);  // Turn on AC device
  delay(5000);
  digitalWrite(RELAY_PIN, LOW);   // Turn off AC device
  delay(5000);
}
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: PROTOCOLS ====================
with tabs[4]:
    st.markdown("## 💬 Communication Protocols")
    
    st.markdown("### 1️⃣ MQTT")
    
    st.markdown("""
    <div class="mqtt-box">
        <strong>MQTT (Message Queue Telemetry Transport):</strong><br>
        • Lightweight pub/sub protocol<br>
        • Low bandwidth, low power<br>
        • Quality of Service (QoS 0, 1, 2)<br>
        • Ideal for IoT<br><br>
        
        <strong>MQTT Publisher (Python):</strong><br>
        <pre>
import paho.mqtt.client as mqtt
import time

broker = "mqtt.eclipse.org"
port = 1883
topic = "home/temperature"

client = mqtt.Client()
client.connect(broker, port)

while True:
    temperature = 25.5  # Read from sensor
    client.publish(topic, str(temperature))
    print(f"Published: {temperature}")
    time.sleep(5)
        </pre><br>
        
        <strong>MQTT Subscriber (Python):</strong><br>
        <pre>
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Received: {message.payload.decode()}")

broker = "mqtt.eclipse.org"
topic = "home/temperature"

client = mqtt.Client()
client.on_message = on_message
client.connect(broker)
client.subscribe(topic)

client.loop_forever()
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Protocol Comparison")
    
    protocol_data = {
        'Protocol': ['MQTT', 'CoAP', 'HTTP/REST', 'WebSocket', 'LoRaWAN'],
        'Transport': ['TCP', 'UDP', 'TCP', 'TCP', 'LoRa'],
        'Overhead': ['Low', 'Very Low', 'High', 'Medium', 'Very Low'],
        'Power': ['Low', 'Very Low', 'High', 'Medium', 'Very Low'],
        'Range': ['WiFi', 'WiFi', 'WiFi', 'WiFi', '10+ km']
    }
    
    df_protocols = pd.DataFrame(protocol_data)
    st.dataframe(df_protocols, use_container_width=True, hide_index=True)

# ==================== TAB 6: EDGE COMPUTING ====================
with tabs[5]:
    st.markdown("## ⚡ Edge Computing")
    
    st.markdown("### 1️⃣ Edge vs Cloud")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Edge Computing Benefits:</strong><br>
        • <strong>Low Latency:</strong> Process data locally<br>
        • <strong>Bandwidth Savings:</strong> Send only insights to cloud<br>
        • <strong>Privacy:</strong> Sensitive data stays local<br>
        • <strong>Reliability:</strong> Works offline<br><br>
        
        <strong>Example: Smart Camera:</strong><br>
        <pre>
import cv2
import requests

# Edge: Process video locally
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Only send to cloud if face detected
    if len(faces) > 0:
        # Send alert to cloud
        requests.post('https://api.example.com/alert', 
                      json={'faces': len(faces)})
        print(f"Detected {len(faces)} faces - Alert sent")
    
    # No need to send entire video stream!
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Node-RED")
    
    st.markdown("""
    <div class="mqtt-box">
        <strong>Visual Programming for IoT:</strong><br>
        • Drag-and-drop flow editor<br>
        • Connect devices, APIs, services<br>
        • Built-in MQTT, HTTP nodes<br>
        • Runs on Raspberry Pi<br><br>
        
        <strong>Example Flow:</strong><br>
        1. MQTT In node (subscribe to sensor)<br>
        2. Function node (process data)<br>
        3. Switch node (if temp > 30°C)<br>
        4. Email node (send alert)<br>
        5. Dashboard node (display chart)<br><br>
        
        <strong>Install Node-RED:</strong><br>
        <pre>
# On Raspberry Pi
bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)

# Start Node-RED
node-red-start

# Access: http://localhost:1880
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: SECURITY ====================
with tabs[6]:
    st.markdown("## 🔐 IoT Security")
    
    st.markdown("### 1️⃣ Security Threats")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Common IoT Vulnerabilities:</strong><br><br>
        
        <strong>1. Weak Authentication:</strong><br>
        • Default passwords (admin/admin)<br>
        • No password enforcement<br>
        • Hardcoded credentials<br><br>
        
        <strong>2. Insecure Communication:</strong><br>
        • Unencrypted data transmission<br>
        • No TLS/SSL<br>
        • Man-in-the-middle attacks<br><br>
        
        <strong>3. Lack of Updates:</strong><br>
        • No firmware update mechanism<br>
        • Outdated software<br>
        • Known vulnerabilities<br><br>
        
        <strong>4. Physical Security:</strong><br>
        • Devices in public spaces<br>
        • Tampering<br>
        • Theft
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Security Best Practices")
    
    st.markdown("""
    <div class="mqtt-box">
        <strong>Secure MQTT with TLS:</strong><br>
        <pre>
import paho.mqtt.client as mqtt
import ssl

client = mqtt.Client()

# Enable TLS
client.tls_set(ca_certs="ca.crt",
               certfile="client.crt",
               keyfile="client.key",
               tls_version=ssl.PROTOCOL_TLSv1_2)

# Username/password authentication
client.username_pw_set("username", "password")

client.connect("secure-broker.com", 8883)
        </pre><br>
        
        <strong>Security Checklist:</strong><br>
        ✅ Change default passwords<br>
        ✅ Use strong authentication (certificates)<br>
        ✅ Encrypt communication (TLS/SSL)<br>
        ✅ Regular firmware updates<br>
        ✅ Network segmentation (IoT VLAN)<br>
        ✅ Disable unused services<br>
        ✅ Monitor for anomalies<br>
        ✅ Physical security (tamper detection)<br><br>
        
        <strong>Secure Boot:</strong><br>
        • Verify firmware integrity<br>
        • Cryptographic signatures<br>
        • Prevent unauthorized firmware
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: YOUTUBE ====================
with tabs[7]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning IoT</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {"title": "Arduino Tutorial for Beginners", "channel": "Paul McWhorter", "url": "https://www.youtube.com/playlist?list=PLGs0VKk2DiYw-L-RibttcvK-WBZm8WLEP", "description": "Complete Arduino course", "duration": "Playlist"},
        {"title": "Raspberry Pi Tutorial", "channel": "The Raspberry Pi Guy", "url": "https://www.youtube.com/c/TheRaspberryPiGuy", "description": "Raspberry Pi basics", "duration": "Channel"},
        {"title": "IoT Explained", "channel": "IBM Technology", "url": "https://www.youtube.com/watch?v=LlhmzVL5bm8", "description": "IoT fundamentals", "duration": "~10 min"}
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
        {"title": "ESP32 Projects", "channel": "Andreas Spiess", "url": "https://www.youtube.com/c/AndreasSpiess", "description": "ESP32 tutorials", "duration": "Channel"},
        {"title": "IoT with MQTT", "channel": "Steve's Internet Guide", "url": "https://www.youtube.com/c/StevesInternetGuide", "description": "MQTT protocol", "duration": "Channel"},
        {"title": "Home Automation", "channel": "DrZzs", "url": "https://www.youtube.com/c/DrZzs", "description": "Smart home projects", "duration": "Channel"}
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
        {"title": "Industrial IoT", "channel": "Opto 22", "url": "https://www.youtube.com/c/Opto22", "description": "IIoT applications", "duration": "Channel"},
        {"title": "IoT Security", "channel": "OWASP", "url": "https://www.youtube.com/c/OWASPGLOBAL", "description": "IoT security", "duration": "Channel"},
        {"title": "Edge Computing", "channel": "Eclipse Foundation", "url": "https://www.youtube.com/c/EclipseFoundation", "description": "Edge AI", "duration": "Channel"}
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
        1. Start with Arduino basics (blink, sensors)<br>
        2. Learn Raspberry Pi and Python GPIO<br>
        3. Integrate sensors and actuators<br>
        4. Implement MQTT communication<br>
        5. Build edge computing solutions<br>
        6. Deploy to cloud (AWS IoT, Azure IoT)<br>
        7. Implement security best practices<br>
        8. Build complete IoT projects<br><br>
        
        <strong>Essential Hardware:</strong><br>
        • <strong>Starter Kit:</strong> Arduino Uno or ESP32<br>
        • <strong>Sensors:</strong> DHT22, PIR, ultrasonic<br>
        • <strong>Actuators:</strong> LED, servo, relay<br>
        • <strong>Advanced:</strong> Raspberry Pi 4<br>
        • <strong>Communication:</strong> WiFi module, LoRa<br><br>
        
        <strong>Career Paths:</strong><br>
        • IoT Developer<br>
        • Embedded Systems Engineer<br>
        • IoT Solutions Architect<br>
        • Smart Home Specialist<br>
        • Industrial IoT Engineer<br>
        • Edge Computing Engineer
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE408 - Internet of Things (IoT)</strong><br>
    <small>UTel University | Computer Engineering Program</small>
</div>
""", unsafe_allow_html=True)
