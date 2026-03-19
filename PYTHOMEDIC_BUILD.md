# Pythomedic — AI Plant Disease Detection & Pesticide Sprayer App

> A collaborative Android application that brings the published ML research to farmers' hands.
> Diagnose crop diseases in real-time, control the robotic sprayer, and track field health.

---

## Team

| Name | Role | Handle |
|---|---|---|
| Emmanuel Oppong | ML Engineer + Backend | `@oppong` |
| Emmanuel Acheampong | Android Lead (UI/UX) | `@acheampong` |
| Micheal Akontoke | Backend API + DevOps | `@akontoke` |

---

## Why This Stack Stands Out to Recruiters

| Layer | Technology | Why It's Impressive |
|---|---|---|
| Android | Kotlin + Jetpack Compose | Modern declarative UI, industry standard 2024+ |
| ML Inference | TensorFlow Lite (on-device) | No internet needed in rural fields |
| Backend | FastAPI (Python) | Async, typed, auto-generates Swagger docs |
| Computer Vision | OpenCV + NumPy | Matches your published research stack |
| Real-time Comms | MQTT (HiveMQ) | IoT protocol for robot ↔ app control |
| Database | Firebase Firestore | Real-time sync, offline support |
| Auth | Firebase Auth | Google sign-in, phone OTP (for farmers) |
| Storage | Firebase Storage | Stores field images per user |
| CI/CD | GitHub Actions | Auto-build APK on push |
| Deployment | Railway (FastAPI) | Free tier, one-click deploy |

---

## Project Structure

```
pythomedic/
│
├── android/                          # Jetpack Compose Android App
│   ├── app/
│   │   ├── src/main/
│   │   │   ├── java/com/pythomedic/
│   │   │   │   ├── ui/
│   │   │   │   │   ├── screens/
│   │   │   │   │   │   ├── HomeScreen.kt
│   │   │   │   │   │   ├── ScanScreen.kt         ← Camera + ML inference
│   │   │   │   │   │   ├── ResultScreen.kt       ← Disease result + spray advice
│   │   │   │   │   │   ├── RobotControlScreen.kt ← Sprayer joystick UI
│   │   │   │   │   │   ├── HistoryScreen.kt      ← Past scans + reports
│   │   │   │   │   │   └── DashboardScreen.kt    ← Field health overview
│   │   │   │   │   ├── components/
│   │   │   │   │   │   ├── DiseaseCard.kt
│   │   │   │   │   │   ├── ConfidenceBar.kt
│   │   │   │   │   │   └── SprayStatusChip.kt
│   │   │   │   │   └── theme/
│   │   │   │   │       ├── Color.kt
│   │   │   │   │       └── Theme.kt              ← Green/earth tone palette
│   │   │   │   ├── ml/
│   │   │   │   │   ├── PlantDiseaseClassifier.kt ← TFLite model runner
│   │   │   │   │   └── ImagePreprocessor.kt
│   │   │   │   ├── data/
│   │   │   │   │   ├── repository/
│   │   │   │   │   │   ├── ScanRepository.kt
│   │   │   │   │   │   └── RobotRepository.kt
│   │   │   │   │   ├── model/
│   │   │   │   │   │   ├── DiagnosisResult.kt
│   │   │   │   │   │   └── SprayCommand.kt
│   │   │   │   │   └── remote/
│   │   │   │   │       └── ApiService.kt         ← Retrofit calls to FastAPI
│   │   │   │   ├── viewmodel/
│   │   │   │   │   ├── ScanViewModel.kt
│   │   │   │   │   └── RobotViewModel.kt
│   │   │   │   └── MainActivity.kt
│   │   │   └── assets/
│   │   │       └── plant_disease_model.tflite    ← Converted ML model
│   │   └── build.gradle.kts
│   └── gradle/
│
├── backend/                          # FastAPI Python Backend
│   ├── app/
│   │   ├── main.py                   ← FastAPI entry point
│   │   ├── routers/
│   │   │   ├── diagnose.py           ← POST /diagnose (image → result)
│   │   │   ├── robot.py              ← POST /robot/spray, GET /robot/status
│   │   │   └── history.py            ← GET /history/{user_id}
│   │   ├── ml/
│   │   │   ├── classifier.py         ← OpenCV + model inference
│   │   │   ├── preprocessor.py       ← Image normalization pipeline
│   │   │   └── model/
│   │   │       └── plant_disease.pkl ← Your trained model (3,243 image dataset)
│   │   ├── mqtt/
│   │   │   └── robot_broker.py       ← MQTT publisher for sprayer commands
│   │   ├── firebase/
│   │   │   └── firestore.py          ← Save diagnosis history
│   │   └── schemas/
│   │       ├── diagnosis.py          ← Pydantic models
│   │       └── robot.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
│
├── ml-research/                      # Your published ML work
│   ├── dataset/                      ← 3,243 training images
│   ├── train.py                      ← Original training script
│   ├── convert_to_tflite.py          ← Export model for Android
│   └── evaluate.py                   ← 99.4% accuracy benchmarks
│
├── robot/                            # Embedded / IoT code
│   └── sprayer_controller.py         ← Runs on Raspberry Pi, receives MQTT
│
├── .github/
│   └── workflows/
│       ├── android-build.yml         ← Auto-build APK on push
│       └── backend-deploy.yml        ← Auto-deploy FastAPI to Railway
│
└── PYTHOMEDIC_BUILD.md               ← This file
```

---

## App Screens (Feature Map)

```
[ Login / OTP ]
       │
       ▼
[ Dashboard ] ── Field health score, solar status, recent alerts
       │
       ├──► [ Scan Plant ]
       │         │
       │         ├── Take photo / upload
       │         ├── On-device TFLite inference (works offline)
       │         └──► [ Result Screen ]
       │                   ├── Disease name + confidence %
       │                   ├── Recommended pesticide dosage
       │                   └── "Spray Now" → Robot Control
       │
       ├──► [ Robot Control ]
       │         ├── Live sprayer status (MQTT)
       │         ├── Manual spray trigger
       │         └── Battery + solar charge level
       │
       └──► [ Scan History ]
                 ├── Past diagnoses per field
                 └── Export PDF report
```

---

## Work Division

### Emmanuel Oppong — ML Engineer + Backend Core

**Owns:** `ml-research/` + `backend/app/ml/` + `backend/app/routers/diagnose.py`

```
Tasks:
  [ ] Convert trained model to TFLite format
        → python ml-research/convert_to_tflite.py
  [ ] Build /diagnose API endpoint (FastAPI)
        → accepts image upload, returns { disease, confidence, advice }
  [ ] Write image preprocessor matching OpenCV pipeline from research
  [ ] Place plant_disease_model.tflite in android/app/src/main/assets/
  [ ] Document model classes (disease labels) in backend/schemas/diagnosis.py
  [ ] Write evaluate.py to benchmark and log accuracy metrics
```

**Key Files:**
- `backend/app/routers/diagnose.py`
- `backend/app/ml/classifier.py`
- `ml-research/convert_to_tflite.py`

---

### Emmanuel Acheampong — Android Lead

**Owns:** `android/` (all Kotlin/Compose code)

```
Tasks:
  [ ] Set up Android project with Jetpack Compose + Material 3
  [ ] Build ScanScreen — CameraX integration, capture button
  [ ] Build PlantDiseaseClassifier.kt — run TFLite model on captured image
  [ ] Build ResultScreen — show disease card, confidence bar, spray CTA
  [ ] Build RobotControlScreen — MQTT status display, spray button
  [ ] Build HistoryScreen — fetch from Firestore, list past scans
  [ ] Build DashboardScreen — field health, solar status widget
  [ ] Implement green/earth tone Material 3 theme
  [ ] Connect Retrofit to FastAPI backend endpoints
```

**Key Files:**
- `android/app/src/main/java/com/pythomedic/ui/screens/ScanScreen.kt`
- `android/app/src/main/java/com/pythomedic/ml/PlantDiseaseClassifier.kt`
- `android/app/src/main/java/com/pythomedic/ui/screens/ResultScreen.kt`

---

### Micheal Akontoke — Backend API + DevOps

**Owns:** `backend/app/routers/` (robot + history) + `backend/mqtt/` + CI/CD

```
Tasks:
  [ ] Set up FastAPI project structure + requirements.txt
  [ ] Build /robot/spray and /robot/status endpoints
  [ ] Implement MQTT publisher (robot_broker.py) using paho-mqtt
  [ ] Set up Firebase Firestore — save every diagnosis with user ID + timestamp
  [ ] Build /history/{user_id} endpoint
  [ ] Write Dockerfile for backend
  [ ] Set up GitHub Actions: android-build.yml (generate APK)
  [ ] Set up GitHub Actions: backend-deploy.yml (auto-deploy to Railway)
  [ ] Write .env.example with all required environment variables
  [ ] Write robot/sprayer_controller.py for Raspberry Pi MQTT subscriber
```

**Key Files:**
- `backend/app/routers/robot.py`
- `backend/app/mqtt/robot_broker.py`
- `backend/firebase/firestore.py`
- `.github/workflows/android-build.yml`

---

## How to Collaborate (Git Workflow)

```bash
# Branch naming convention
feature/oppong-tflite-conversion
feature/acheampong-scan-screen
feature/akontoke-mqtt-broker

# Each person works on their branch, opens PR to main
# Require 1 review before merging (set in GitHub branch protection)
```

### Integration Points (Where You Connect Each Other's Work)

| Who Provides | What | Who Consumes |
|---|---|---|
| Oppong | `plant_disease_model.tflite` | Acheampong (drops into `assets/`) |
| Oppong | `/diagnose` API response schema | Acheampong (Retrofit model) + Akontoke (Firestore schema) |
| Akontoke | FastAPI base URL + endpoints | Acheampong (ApiService.kt) |
| Akontoke | MQTT topic names | Acheampong (RobotControlScreen) + Robot hardware |

---

## Getting Started

### 1. Clone & Branch
```bash
git clone https://github.com/your-org/pythomedic.git
cd pythomedic
git checkout -b feature/yourname-task
```

### 2. Backend Setup (Oppong + Akontoke)
```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env          # fill in Firebase + MQTT credentials
uvicorn app.main:app --reload
# Swagger docs at http://localhost:8000/docs
```

### 3. Android Setup (Acheampong)
```bash
# Open android/ folder in Android Studio (Hedgehog or later)
# Add google-services.json from Firebase Console to android/app/
# Build > Make Project
```

### 4. ML Model Conversion (Oppong)
```bash
cd ml-research
pip install tensorflow opencv-python numpy
python convert_to_tflite.py
# Outputs: plant_disease.tflite → copy to android/app/src/main/assets/
```

---

## Recruiter-Impressive Features to Highlight

- **On-device ML inference** — works with zero internet in rural areas (TFLite)
- **Published research backing** — 99.4% accuracy on 3,243 image dataset
- **IoT integration** — real Android app controls real hardware via MQTT
- **Solar-aware UX** — battery/solar status shown in app, addressing farmer sustainability
- **Offline-first design** — Firebase offline persistence + local model
- **CI/CD pipeline** — auto-generates signed APK on every push

---

## Timeline Suggestion

```
Week 1:  Oppong → TFLite conversion + /diagnose endpoint
         Akontoke → FastAPI scaffold + Firebase setup
         Acheampong → Android project + theme + navigation

Week 2:  Oppong → classifier.py + preprocessor.py finalized
         Akontoke → MQTT broker + /robot endpoints + CI/CD
         Acheampong → ScanScreen + TFLite integration

Week 3:  Acheampong → ResultScreen + RobotControlScreen + HistoryScreen
         Akontoke → Firestore history + Dockerfile + deploy to Railway
         Oppong → API docs + model accuracy report

Week 4:  Full integration testing → polish → record demo video
```

---

*Built on published research — Robotic Pythomedic and Pesticide Sprayer (April 2022)*
