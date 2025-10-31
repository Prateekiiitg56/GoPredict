# 🚀 GoPredict – Full Stack ML Application for Trip Duration Prediction

A **comprehensive full-stack application** that combines a **machine learning pipeline (Python/FastAPI)** for predicting trip durations with a **complete user platform (React/Node.js/MongoDB)** supporting authentication, profile management, and trip history.

**🧠 Medium Post (on the ML pipeline):**  
[How Machine Learning Predicts Trip Duration (like Uber/Zomato)](https://medium.com/@hphadtare02/how-machine-learning-predicts-trip-duration-just-like-uber-zomato-91f7db6e9ce9)

---

## 📁 Project Structure



```
GoPredict/
├── main.py # Main ML pipeline runner script
├── start_api.py # Python FastAPI (ML) server startup
├── test_api.py # Python FastAPI (ML) testing script
├── config.py # Python ML pipeline configuration
├── requirements.txt # Python dependencies
├── README.md # This file
├── CONTRIBUTING.md # Development and integration guide
├── CODE_OF_CONDUCT.md # Code of conduct and security
│
├── api/ # Python FastAPI (ML) backend
│ └── main.py # FastAPI application
│
├── backend/ # Node.js (User/Trips) backend
│ ├── src/
│ │ ├── models/ # Mongoose (User, Trip) schemas
│ │ ├── routes/ # API routes (profile, trips, users)
│ │ ├── middleware/ # Auth middleware (Firebase Admin)
│ │ ├── config/ # Firebase Admin initialization
│ │ ├── db.ts # MongoDB connection logic
│ │ └── server.ts # Express server entry point
│ ├── config/
│ │ └── serviceAccountKey.json # (Git-ignored) Firebase Admin key
│ ├── package.json
│ └── tsconfig.json
│
├── frontend/ # React frontend application
│ ├── src/
│ │ ├── components/ # Reusable components (Button, UserNav, etc.)
│ │ ├── pages/ # Page components (Home, SignIn, Profile)
│ │ ├── lib/ # Helper libraries (api.ts, utils.ts)
│ │ ├── AuthContext.tsx # Global authentication state
│ │ ├── firebase.ts # Firebase client initialization
│ │ ├── App.tsx # Main app component (routing)
│ │ └── main.tsx # React app entry point
│ ├── .env.local # (Git-ignored) Firebase client keys
│ └── package.json
│
├── data/ # Data directory (Raw, Processed, External)
│ ├── raw/
│ ├── processed/
│ └── external/
│
├── src/ # Python ML source code
│ ├── model/ # ML models, evaluation, persistence
│ ├── features/ # Feature engineering modules
│ ├── feature_pipe.py
│ ├── data_preprocessing.py
│ └── complete_pipeline.py
│
├── notebooks/ # Jupyter notebooks (EDA, Feature Eng, Training)
│ ├── 01_EDA.ipynb
│ ├── 02_Feature_Engineering.ipynb
│ ├── 03_Model_Training.ipynb
│ └── figures/
│
├── saved_models/ # (Git-ignored) Trained ML models
├── output/ # (Git-ignored) Predictions and submissions
└── logs/ # (Git-ignored) Log files 

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd GoPredict

# Install dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p logs output saved_models
```

---

## ⚙️ Full-Stack Setup Guide

This project has **three major services** that work together:

1. 🧩 **Frontend (React/Vite)** – User interface  
2. 🧑‍💻 **Backend (Node.js/Express)** – Authentication, profiles, trip history  
3. 🤖 **ML Backend (Python/FastAPI)** – Machine learning predictions  

---

### 🧱 Prerequisites

- **Node.js v18+** and **pnpm** (or npm)
- **Python 3.9+**
- **MongoDB Atlas** cluster URL
- **Firebase Project**
  - Web app credentials (`.env.local` for frontend)
  - Admin service account key (`serviceAccountKey.json` for backend)

---

## 1️⃣ Node.js Backend (User & Trips API)

Handles **user profiles**, **authentication**, and **trip history**.

```bash
# Navigate to the Node.js backend
cd backend

# Install dependencies
pnpm install

# Create .env file
MONGO_URI=mongodb+srv://gopredict:<YOUR_PASSWORD>@cluster0.xxxx.mongodb.net/gopredict?retryWrites=true&w=majority
FIREBASE_SERVICE_ACCOUNT_KEY_PATH=./config/serviceAccountKey.json

# Run the server
pnpm dev
# → Runs on http://localhost:5001
```
2️⃣ Python Backend (ML API)

Serves the machine learning model for trip duration predictions.
```
# Navigate to project root
cd ..

# Install Python dependencies
pip install -r requirements.txt

# Create required directories
mkdir -p logs output saved_models

# Run FastAPI server
python start_api.py
# → Runs on http://localhost:8000

```
3️⃣ React Frontend

The main user interface that interacts with both APIs

```
cd frontend

# Install dependencies
pnpm install

# Add Firebase config in .env.local
VITE_FIREBASE_API_KEY=AIza...
VITE_FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
VITE_FIREBASE_PROJECT_ID=your-project-id
VITE_FIREBASE_STORAGE_BUCKET=your-project.appspot.com
VITE_FIREBASE_MESSAGING_SENDER_ID=...
VITE_FIREBASE_APP_ID=...

# Start frontend server
pnpm dev
# → App runs on http://localhost:3000
```

🔌 API Documentation
🧍 User & Trips API (Node.js / MongoDB)

Base URL → http://localhost:5001
All endpoints require:
Authorization: Bearer <FIREBASE_ID_TOKEN>

👤 User Endpoints

POST /api/users/sync – Sync Firebase user to MongoDB
GET /api/profile – Fetch user profile
PUT /api/profile – Update profile info
POST /api/trips – Save trip prediction
GET /api/trips – Fetch trip history
DELETE /api/trips/:id – Delete trip by ID

🤖 ML Prediction API (Python / FastAPI)

Base URL → http://localhost:8000

Endpoint	Method	Description
/weather	GET	Get weather data
/distance	POST	Calculate distances
/time-features	POST	Extract time-based features
/predict	POST	Predict trip duration
/models	GET	List models
/models/train	POST	Train models
/health	GET	Health check

Docs:

Swagger → http://localhost:8000/docs

ReDoc → http://localhost:8000/redoc

🔗 Frontend API Usage

Example 1 – Get Prediction (Python FastAPI):
```
import { predictTravelTime } from "@/lib/api";

const prediction = await predictTravelTime({
  from: { lat: 40.767937, lon: -73.982155 },
  to: { lat: 40.748817, lon: -73.985428 },
  startTime: "2016-01-01T17:00:00",
  city: "new_york",
});
```
Example 2 – Fetch Profile (Node.js API)
```
const response = await fetch("http://localhost:5001/api/profile", {
  headers: {
    Authorization: `Bearer <FIREBASE_ID_TOKEN>`,
  },
});
const profileData = await response.json();
```
🎯 ML Pipeline Usage
```
python main.py
```
Runs the complete pipeline:

Data preprocessing

Feature engineering

Model training

Model evaluation

Prediction generation

Custom models
```
python main.py --models XGB,RF
```
Hyperparameter tuning:
```
python main.py --tune-xgb
```
📈 Outputs
Type	Path	Description
Predictions	output/[model_name]/test_prediction_*.csv	Ready-to-submit predictions
Models	saved_models/[model_name]_*.pkl	Trained models
Logs	logs/main.log	Pipeline logs
Visuals	output/prediction_comparison_*.png	Model comparison & feature plots
🧩 Configuration

Edit config.py to customize:

Model parameters

Data paths

Output directories

Logging & hyperparameter ranges

🧪 Testing
🧠 Python ML API
```
python test_api.py
```
💻 React Frontend
```
cd frontend
npm run test
npm run test:coverage
```
🤝 Contributing

See CONTRIBUTING.md
 for development guidelines.

📋 Code of Conduct

Read CODE_OF_CONDUCT.md
 for community and security policies.

📄 License

This project is licensed under the MIT License.
See the LICENSE
 file for more details
