import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="CE403 - Mobile App Development", page_icon="📱", layout="wide")

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
    
    .react-box {
        background: linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%);
        border-left: 5px solid #3b82f6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .flutter-box {
        background: linear-gradient(135deg, #ddd6fe 0%, #c4b5fd 100%);
        border-left: 5px solid #8b5cf6;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
    }
    
    .native-box {
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
    <div style="font-size: 1.2rem; opacity: 0.9;">CE403</div>
    <div class="course-title">Mobile Application Development</div>
    <div>📱 3 Credits | Semester 8 | React Native, Flutter & Native Development</div>
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
    "⚛️ React Native",
    "🦋 Flutter",
    "📱 Mobile UI/UX",
    "🔌 Native APIs",
    "🔔 Push Notifications",
    "🚀 App Store Deployment",
    "📺 YouTube Resources"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.markdown("## 📚 Course Overview")
    
    st.markdown("""
    <div class="theory-box">
        <h3>Course Description</h3>
        <p>Comprehensive mobile application development course covering cross-platform frameworks (React Native, Flutter) 
        and native development (iOS, Android). Learn mobile UI/UX design, navigation, state management, native APIs, 
        push notifications, offline storage, and app store deployment. Emphasizes hands-on development with real-world 
        projects. Students will build complete mobile apps from scratch and publish them to App Store and Google Play.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🎯 Learning Outcomes")
    
    outcomes = [
        "Build cross-platform apps with React Native and Flutter",
        "Design mobile-first UI/UX with platform-specific guidelines",
        "Implement navigation and state management",
        "Access native device APIs (camera, GPS, sensors)",
        "Integrate push notifications and background tasks",
        "Implement offline-first architecture with local storage",
        "Deploy apps to App Store and Google Play",
        "Optimize app performance and bundle size"
    ]
    
    for outcome in outcomes:
        st.markdown(f"✅ {outcome}")
    
    st.markdown("### 📋 Course Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Cross-Platform:**
        - React Native (JavaScript/TypeScript)
        - Flutter (Dart)
        - Expo framework
        - Component libraries (NativeBase, React Native Paper)
        - Hot reload and debugging
        
        **UI/UX:**
        - Material Design (Android)
        - Human Interface Guidelines (iOS)
        - Responsive layouts
        - Animations and gestures
        - Dark mode support
        """)
    
    with col2:
        st.markdown("""
        **Native Features:**
        - Camera and photo library
        - GPS and maps
        - Sensors (accelerometer, gyroscope)
        - Biometric authentication
        - File system access
        
        **Backend & Deployment:**
        - REST API integration
        - Firebase (Auth, Firestore, Storage)
        - Push notifications (FCM, APNs)
        - App Store submission
        - Google Play submission
        """)
    
    st.markdown("### 📚 Recommended Resources")
    
    resources = [
        {"title": "React Native Documentation", "author": "Meta", "type": "React Native"},
        {"title": "Flutter Documentation", "author": "Google", "type": "Flutter"},
        {"title": "iOS Human Interface Guidelines", "author": "Apple", "type": "Design"},
        {"title": "Material Design", "author": "Google", "type": "Design"}
    ]
    
    for resource in resources:
        title = resource['title']
        author = resource['author']
        rtype = resource['type']
        st.markdown(f"📖 **{title}** by {author} ({rtype})")

# ==================== TAB 2: REACT NATIVE ====================
with tabs[1]:
    st.markdown("## ⚛️ React Native")
    
    st.markdown("### 1️⃣ Getting Started")
    
    st.markdown("""
    <div class="react-box">
        <strong>Setup:</strong><br>
        <pre>
# Install React Native CLI
npm install -g react-native-cli

# Create new project
npx react-native init MyApp

# Or use Expo (recommended for beginners)
npx create-expo-app MyApp
cd MyApp
npm start
        </pre><br>
        
        <strong>Basic Component:</strong><br>
        <pre>
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function App() {
  return (
    &lt;View style={styles.container}&gt;
      &lt;Text style={styles.title}&gt;Hello, React Native!&lt;/Text&gt;
    &lt;/View&gt;
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
  },
});
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Core Components")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Essential Components:</strong><br><br>
        
        <strong>View:</strong> Container (like div in web)<br>
        <strong>Text:</strong> Display text<br>
        <strong>Image:</strong> Display images<br>
        <strong>ScrollView:</strong> Scrollable container<br>
        <strong>FlatList:</strong> Efficient list rendering<br>
        <strong>TextInput:</strong> Text input field<br>
        <strong>TouchableOpacity:</strong> Touchable button<br>
        <strong>Button:</strong> Platform-specific button<br>
        <strong>Modal:</strong> Modal dialog<br>
        <strong>ActivityIndicator:</strong> Loading spinner<br><br>
        
        <strong>Example - FlatList:</strong><br>
        <pre>
&lt;FlatList
  data={items}
  keyExtractor={(item) => item.id}
  renderItem={({ item }) => (
    &lt;View style={styles.item}&gt;
      &lt;Text&gt;{item.title}&lt;/Text&gt;
    &lt;/View&gt;
  )}
/&gt;
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Navigation")
    
    st.markdown("""
    <div class="react-box">
        <strong>React Navigation:</strong><br>
        <pre>
npm install @react-navigation/native
npm install @react-navigation/stack

import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

function App() {
  return (
    &lt;NavigationContainer&gt;
      &lt;Stack.Navigator&gt;
        &lt;Stack.Screen name="Home" component={HomeScreen} /&gt;
        &lt;Stack.Screen name="Details" component={DetailsScreen} /&gt;
      &lt;/Stack.Navigator&gt;
    &lt;/NavigationContainer&gt;
  );
}

// Navigate between screens
navigation.navigate('Details', { itemId: 42 });
        </pre><br>
        
        <strong>Navigation Types:</strong><br>
        • <strong>Stack Navigator:</strong> Push/pop screens<br>
        • <strong>Tab Navigator:</strong> Bottom tabs<br>
        • <strong>Drawer Navigator:</strong> Side menu<br>
        • <strong>Bottom Sheet:</strong> Modal from bottom
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 3: FLUTTER ====================
with tabs[2]:
    st.markdown("## 🦋 Flutter")
    
    st.markdown("### 1️⃣ Getting Started")
    
    st.markdown("""
    <div class="flutter-box">
        <strong>Setup:</strong><br>
        <pre>
# Install Flutter SDK
# Download from flutter.dev

# Create new project
flutter create my_app
cd my_app
flutter run
        </pre><br>
        
        <strong>Basic Widget:</strong><br>
        <pre>
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text('Hello Flutter'),
        ),
        body: Center(
          child: Text(
            'Hello, Flutter!',
            style: TextStyle(fontSize: 24),
          ),
        ),
      ),
    );
  }
}
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Widgets")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Stateless vs Stateful:</strong><br><br>
        
        <strong>Stateless Widget:</strong><br>
        • Immutable<br>
        • No internal state<br>
        • Rebuilds when parent changes<br><br>
        
        <strong>Stateful Widget:</strong><br>
        • Mutable state<br>
        • Can update UI with setState()<br>
        • Has lifecycle methods<br><br>
        
        <strong>Example - Stateful Widget:</strong><br>
        <pre>
class Counter extends StatefulWidget {
  @override
  _CounterState createState() => _CounterState();
}

class _CounterState extends State&lt;Counter&gt; {
  int _count = 0;

  void _increment() {
    setState(() {
      _count++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text('Count: $_count'),
        ElevatedButton(
          onPressed: _increment,
          child: Text('Increment'),
        ),
      ],
    );
  }
}
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Layout & Styling")
    
    st.markdown("""
    <div class="flutter-box">
        <strong>Layout Widgets:</strong><br>
        • <strong>Container:</strong> Box with padding, margin, decoration<br>
        • <strong>Row:</strong> Horizontal layout<br>
        • <strong>Column:</strong> Vertical layout<br>
        • <strong>Stack:</strong> Overlapping widgets<br>
        • <strong>ListView:</strong> Scrollable list<br>
        • <strong>GridView:</strong> Grid layout<br><br>
        
        <strong>Example - Responsive Layout:</strong><br>
        <pre>
Container(
  padding: EdgeInsets.all(16),
  decoration: BoxDecoration(
    color: Colors.blue,
    borderRadius: BorderRadius.circular(12),
  ),
  child: Row(
    mainAxisAlignment: MainAxisAlignment.spaceBetween,
    children: [
      Icon(Icons.star, color: Colors.white),
      Text('Featured', style: TextStyle(color: Colors.white)),
    ],
  ),
)
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 4: MOBILE UI/UX ====================
with tabs[3]:
    st.markdown("## 📱 Mobile UI/UX")
    
    st.markdown("### 1️⃣ Design Principles")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Mobile-First Design:</strong><br><br>
        
        <strong>Touch Targets:</strong><br>
        • Minimum 44x44 points (iOS)<br>
        • Minimum 48x48 dp (Android)<br>
        • Adequate spacing between elements<br><br>
        
        <strong>Typography:</strong><br>
        • Readable font sizes (16sp minimum)<br>
        • Clear hierarchy (headings, body, captions)<br>
        • Line height for readability<br><br>
        
        <strong>Colors:</strong><br>
        • Sufficient contrast (WCAG AA: 4.5:1)<br>
        • Consistent color palette<br>
        • Dark mode support<br><br>
        
        <strong>Navigation:</strong><br>
        • Clear back navigation<br>
        • Bottom navigation for primary actions<br>
        • Swipe gestures for common actions
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Platform Guidelines")
    
    comparison_data = {
        'Aspect': ['Navigation', 'Buttons', 'Icons', 'Typography', 'Gestures'],
        'iOS (HIG)': [
            'Tab bar, navigation bar',
            'Rounded, filled or outlined',
            'SF Symbols',
            'San Francisco font',
            'Swipe back, long press'
        ],
        'Android (Material)': [
            'Bottom nav, top app bar',
            'Rectangular, elevated or flat',
            'Material Icons',
            'Roboto font',
            'Swipe to dismiss, FAB'
        ]
    }
    
    df_comparison = pd.DataFrame(comparison_data)
    st.dataframe(df_comparison, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Animations")
    
    st.markdown("""
    <div class="react-box">
        <strong>React Native Animated API:</strong><br>
        <pre>
import { Animated } from 'react-native';

const fadeAnim = useRef(new Animated.Value(0)).current;

useEffect(() => {
  Animated.timing(fadeAnim, {
    toValue: 1,
    duration: 1000,
    useNativeDriver: true,
  }).start();
}, []);

return (
  &lt;Animated.View style={{ opacity: fadeAnim }}&gt;
    &lt;Text&gt;Fading In&lt;/Text&gt;
  &lt;/Animated.View&gt;
);
        </pre><br>
        
        <strong>Flutter Animations:</strong><br>
        <pre>
class FadeInWidget extends StatefulWidget {
  @override
  _FadeInWidgetState createState() => _FadeInWidgetState();
}

class _FadeInWidgetState extends State&lt;FadeInWidget&gt;
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation&lt;double&gt; _animation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: Duration(seconds: 1),
      vsync: this,
    );
    _animation = Tween&lt;double&gt;(begin: 0, end: 1).animate(_controller);
    _controller.forward();
  }

  @override
  Widget build(BuildContext context) {
    return FadeTransition(
      opacity: _animation,
      child: Text('Fading In'),
    );
  }
}
        </pre>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 5: NATIVE APIs ====================
with tabs[4]:
    st.markdown("## 🔌 Native APIs")
    
    st.markdown("### 1️⃣ Camera & Photos")
    
    st.markdown("""
    <div class="native-box">
        <strong>React Native - expo-image-picker:</strong><br>
        <pre>
import * as ImagePicker from 'expo-image-picker';

const pickImage = async () => {
  const result = await ImagePicker.launchImageLibraryAsync({
    mediaTypes: ImagePicker.MediaTypeOptions.Images,
    allowsEditing: true,
    aspect: [4, 3],
    quality: 1,
  });

  if (!result.canceled) {
    setImage(result.assets[0].uri);
  }
};

const takePhoto = async () => {
  const result = await ImagePicker.launchCameraAsync({
    allowsEditing: true,
    aspect: [4, 3],
    quality: 1,
  });
};
        </pre><br>
        
        <strong>Flutter - image_picker:</strong><br>
        <pre>
import 'package:image_picker/image_picker.dart';

final ImagePicker _picker = ImagePicker();

Future&lt;void&gt; pickImage() async {
  final XFile? image = await _picker.pickImage(
    source: ImageSource.gallery,
  );
  
  if (image != null) {
    setState(() {
      _imageFile = File(image.path);
    });
  }
}
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Location & Maps")
    
    st.markdown("""
    <div class="theory-box">
        <strong>React Native - expo-location:</strong><br>
        <pre>
import * as Location from 'expo-location';

const getLocation = async () => {
  let { status } = await Location.requestForegroundPermissionsAsync();
  
  if (status !== 'granted') {
    alert('Permission denied');
    return;
  }

  let location = await Location.getCurrentPositionAsync({});
  console.log(location.coords.latitude, location.coords.longitude);
};
        </pre><br>
        
        <strong>Maps Integration:</strong><br>
        • <strong>React Native:</strong> react-native-maps<br>
        • <strong>Flutter:</strong> google_maps_flutter<br>
        • Requires API keys (Google Maps, Apple Maps)<br>
        • Display markers, polylines, polygons<br>
        • Custom map styling
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ Other Native Features")
    
    st.markdown("""
    <div class="native-box">
        <strong>Biometric Authentication:</strong><br>
        • Fingerprint, Face ID, Touch ID<br>
        • expo-local-authentication (React Native)<br>
        • local_auth (Flutter)<br><br>
        
        <strong>Sensors:</strong><br>
        • Accelerometer, gyroscope, magnetometer<br>
        • expo-sensors (React Native)<br>
        • sensors_plus (Flutter)<br><br>
        
        <strong>File System:</strong><br>
        • Read/write files<br>
        • expo-file-system (React Native)<br>
        • path_provider (Flutter)<br><br>
        
        <strong>Contacts:</strong><br>
        • Access device contacts<br>
        • expo-contacts (React Native)<br>
        • contacts_service (Flutter)<br><br>
        
        <strong>Calendar:</strong><br>
        • Create, read, update events<br>
        • expo-calendar (React Native)<br>
        • device_calendar (Flutter)
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 6: PUSH NOTIFICATIONS ====================
with tabs[5]:
    st.markdown("## 🔔 Push Notifications")
    
    st.markdown("### 1️⃣ Firebase Cloud Messaging (FCM)")
    
    st.markdown("""
    <div class="react-box">
        <strong>Setup Firebase:</strong><br>
        1. Create Firebase project<br>
        2. Add iOS and Android apps<br>
        3. Download config files (google-services.json, GoogleService-Info.plist)<br>
        4. Install Firebase SDK<br><br>
        
        <strong>React Native - expo-notifications:</strong><br>
        <pre>
import * as Notifications from 'expo-notifications';

// Request permission
const { status } = await Notifications.requestPermissionsAsync();

// Get push token
const token = (await Notifications.getExpoPushTokenAsync()).data;

// Listen for notifications
Notifications.addNotificationReceivedListener(notification => {
  console.log(notification);
});

// Send local notification
await Notifications.scheduleNotificationAsync({
  content: {
    title: "Hello!",
    body: "This is a notification",
  },
  trigger: { seconds: 5 },
});
        </pre>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Notification Types")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Local Notifications:</strong><br>
        • Scheduled by the app<br>
        • Don't require internet<br>
        • Use cases: Reminders, alarms<br><br>
        
        <strong>Push Notifications:</strong><br>
        • Sent from server<br>
        • Require FCM/APNs<br>
        • Use cases: Messages, updates, alerts<br><br>
        
        <strong>Notification Channels (Android 8+):</strong><br>
        • Group notifications by type<br>
        • Users can customize per channel<br>
        • Priority levels (high, default, low)<br><br>
        
        <strong>Best Practices:</strong><br>
        • Request permission at appropriate time<br>
        • Don't spam users<br>
        • Provide opt-out option<br>
        • Use rich notifications (images, actions)<br>
        • Handle notification taps (deep linking)
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 7: DEPLOYMENT ====================
with tabs[6]:
    st.markdown("## 🚀 App Store Deployment")
    
    st.markdown("### 1️⃣ iOS App Store")
    
    st.markdown("""
    <div class="native-box">
        <strong>Requirements:</strong><br>
        • Apple Developer account ($99/year)<br>
        • Mac with Xcode<br>
        • App icons (various sizes)<br>
        • Screenshots (required sizes)<br>
        • Privacy policy URL<br><br>
        
        <strong>Submission Steps:</strong><br>
        1. <strong>Prepare App:</strong><br>
           • Set bundle identifier<br>
           • Configure app icons and splash screen<br>
           • Set version and build number<br><br>
        
        2. <strong>Build for Release:</strong><br>
           • Archive in Xcode<br>
           • Upload to App Store Connect<br><br>
        
        3. <strong>App Store Connect:</strong><br>
           • Create app listing<br>
           • Add screenshots and description<br>
           • Set pricing and availability<br>
           • Submit for review<br><br>
        
        4. <strong>Review Process:</strong><br>
           • Typically 1-3 days<br>
           • Follow App Store Review Guidelines<br>
           • Respond to rejection feedback
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 2️⃣ Google Play Store")
    
    st.markdown("""
    <div class="theory-box">
        <strong>Requirements:</strong><br>
        • Google Play Developer account ($25 one-time)<br>
        • App icons and screenshots<br>
        • Privacy policy URL<br>
        • Content rating questionnaire<br><br>
        
        <strong>Submission Steps:</strong><br>
        1. <strong>Build APK/AAB:</strong><br>
           <pre>
# React Native
cd android
./gradlew bundleRelease

# Flutter
flutter build appbundle
           </pre><br>
        
        2. <strong>Sign App:</strong><br>
           • Generate keystore<br>
           • Sign APK/AAB with keystore<br><br>
        
        3. <strong>Google Play Console:</strong><br>
           • Create app<br>
           • Upload APK/AAB<br>
           • Add store listing<br>
           • Set pricing and distribution<br>
           • Submit for review<br><br>
        
        4. <strong>Review Process:</strong><br>
           • Usually faster than iOS (hours to 1 day)<br>
           • Follow Google Play policies
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 3️⃣ App Updates")
    
    st.markdown("""
    <div class="native-box">
        <strong>Over-the-Air (OTA) Updates:</strong><br>
        • <strong>Expo Updates:</strong> Update JS bundle without app store<br>
        • <strong>CodePush:</strong> Microsoft's OTA solution<br>
        • Only for JS changes, not native code<br><br>
        
        <strong>Version Management:</strong><br>
        • Semantic versioning (1.2.3)<br>
        • Increment build number for each release<br>
        • Maintain changelog<br><br>
        
        <strong>Beta Testing:</strong><br>
        • <strong>TestFlight:</strong> iOS beta testing<br>
        • <strong>Google Play Internal Testing:</strong> Android beta<br>
        • Get feedback before public release
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: YOUTUBE ====================
with tabs[7]:
    st.markdown("## 📺 YouTube Learning Resources")
    
    st.markdown("""
    <div class="youtube-box">
        <h3>🎓 Curated YouTube Channels & Playlists</h3>
        <p>High-quality video tutorials for learning Mobile App Development</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Beginner Level
    st.markdown("### 🟢 Beginner Level")
    
    beginner_resources = [
        {"title": "React Native Tutorial", "channel": "Programming with Mosh", "url": "https://www.youtube.com/watch?v=0-S5a0eXPoc", "description": "Complete React Native course", "duration": "~6 hours"},
        {"title": "Flutter Tutorial for Beginners", "channel": "freeCodeCamp.org", "url": "https://www.youtube.com/watch?v=pTJJsmejUOQ", "description": "Flutter fundamentals", "duration": "~37 hours"},
        {"title": "Mobile UI Design", "channel": "DesignCourse", "url": "https://www.youtube.com/c/DesignCourse", "description": "Mobile design principles", "duration": "Channel"}
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
        {"title": "React Native Advanced", "channel": "William Candillon", "url": "https://www.youtube.com/c/wcandillon", "description": "Advanced animations", "duration": "Channel"},
        {"title": "Flutter State Management", "channel": "Reso Coder", "url": "https://www.youtube.com/c/ResoCoder", "description": "BLoC, Provider, Riverpod", "duration": "Channel"},
        {"title": "Firebase for Mobile", "channel": "Fireship", "url": "https://www.youtube.com/c/Fireship", "description": "Firebase integration", "duration": "Channel"}
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
        {"title": "React Native Performance", "channel": "React Native EU", "url": "https://www.youtube.com/c/ReactNativeEU", "description": "Performance optimization", "duration": "Channel"},
        {"title": "Flutter Architecture", "channel": "Flutter", "url": "https://www.youtube.com/c/flutterdev", "description": "Official Flutter channel", "duration": "Channel"},
        {"title": "Native Modules", "channel": "Notjust.dev", "url": "https://www.youtube.com/c/notjustdev", "description": "Custom native modules", "duration": "Channel"}
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
        1. Learn JavaScript/TypeScript or Dart<br>
        2. Understand React basics (for React Native)<br>
        3. Build simple apps (todo, weather, calculator)<br>
        4. Learn navigation and state management<br>
        5. Integrate APIs and backend services<br>
        6. Add native features (camera, location)<br>
        7. Implement push notifications<br>
        8. Deploy to app stores<br><br>
        
        <strong>Essential Tools:</strong><br>
        • <strong>IDE:</strong> VS Code, Android Studio, Xcode<br>
        • <strong>Emulators:</strong> Android Emulator, iOS Simulator<br>
        • <strong>Debugging:</strong> React Native Debugger, Flutter DevTools<br>
        • <strong>Design:</strong> Figma, Sketch<br>
        • <strong>Backend:</strong> Firebase, Supabase, AWS Amplify<br><br>
        
        <strong>Career Paths:</strong><br>
        • Mobile App Developer<br>
        • React Native Developer<br>
        • Flutter Developer<br>
        • iOS Developer<br>
        • Android Developer<br>
        • Full-Stack Mobile Developer
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #9ca3af; padding: 1rem;">
    <strong>CE403 - Mobile Application Development</strong><br>
    <small>UTel University | Computer Engineering Program</small>
</div>
""", unsafe_allow_html=True)
