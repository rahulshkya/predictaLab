# 🚀 PredictaLab — End-to-End AutoML Loan Prediction System

PredictaLab is a **full-stack machine learning application** that combines **custom-built ML algorithms**, an **AutoML-style model selection engine**, and a **production-ready API with a modern React UI**.

Unlike typical ML projects that stop at notebooks, PredictaLab delivers a **complete product pipeline** — from data processing and model training to real-time prediction via API and user interface.

---

# 🌐 Live System Overview

```text
User Input (React UI)
        ↓
FastAPI Backend (Prediction API)
        ↓
Scaler + Feature Engineering
        ↓
Multiple ML Models (From Scratch)
        ↓
Best Model Prediction
        ↓
Result Returned to UI
```

---

# 🎯 Key Highlights

• Built **multiple ML algorithms from scratch (no sklearn models used)**
• Designed a **custom AutoML-style model selection system**
• Implemented a **complete ML pipeline architecture**
• Integrated **FastAPI backend for real-time predictions**
• Developed a **React-based frontend UI**
• Enabled **dynamic model selection (KNN, Logistic, Decision Tree, etc.)**
• Achieved **end-to-end ML system deployment locally**

---

# 🧠 Core Concept — AutoML System

PredictaLab behaves like a **mini AutoML engine**:

```text
Train Multiple Models
        ↓
Evaluate Performance
        ↓
Compare Metrics
        ↓
Select Best Model Automatically
        ↓
Use Best Model for Predictions
```

This replicates how real-world ML platforms optimize model performance.

---

# ⚙️ Machine Learning Pipeline

```text
Raw Dataset
   ↓
Data Cleaning & Feature Engineering
   ↓
Train-Test Split (Custom Implementation)
   ↓
Feature Scaling (StandardScaler)
   ↓
Model Training (Multiple Algorithms)
   ↓
Model Evaluation (Accuracy)
   ↓
Best Model Selection
   ↓
Model Persistence (joblib)
```

---

# 🧩 Algorithms Implemented

### 🔹 Logistic Regression (From Scratch)

• Sigmoid activation
• Gradient Descent optimization
• Binary classification

---

### 🔹 K-Nearest Neighbors (KNN) (From Scratch)

• Euclidean distance
• Majority voting
• Configurable K

---

### 🔹 Decision Tree *(Custom Implementation)*

• Recursive splitting
• Depth control
• Feature-based decisions

---

### 🔹 Random Forest *(Custom Implementation)*

• Ensemble of decision trees
• Feature randomness
• Improved generalization

---

# 🏦 Use Case — Loan Approval Prediction

PredictaLab predicts whether a loan application should be approved based on financial attributes such as:

• Income
• Credit Score
• Loan Amount
• Years Employed
• Loan-Income Ratio

---

# 📊 Example Output

```json
{
  "model_name": "knn",
  "prediction": "Loan Approved",
  "status": "success"
}
```

---

# 🧱 Project Architecture

```text
PredictaLab
│
├── algorithms/            # Custom ML algorithms
│   ├── logistic_regression.py
│   ├── knn.py
│   ├── decision_tree.py
│   └── random_forest.py
│
├── core/                  # Training & model selection
│   ├── trainer.py
│   └── model_selector.py
│
├── preprocessing/         # Data processing
│   ├── train_test_split.py
│   ├── scaler.py
│   └── encoder.py
│
├── metrics/               # Evaluation metrics
│   └── accuracy.py
│
├── backend/               # FastAPI backend
│   └── index.py
│
├── ui/                    # React frontend (Vite)
│   └── src/App.jsx
│
├── data/                  # Dataset
│   └── loan_approval.csv
│
├── models.pkl             # Saved trained models
├── scaler.pkl             # Saved scaler
├── requirements.txt
└── README.md
```

---

# 🛠️ Tech Stack

### 🔹 Machine Learning

• Python
• NumPy
• Pandas
• Custom ML Implementations

### 🔹 Backend

• FastAPI
• Uvicorn

### 🔹 Frontend

• React (Vite)
• Axios

### 🔹 Model Persistence

• Joblib

---

# 📥 Installation

```bash
git clone https://github.com/your-username/PredictaLab.git
cd PredictaLab
```

---

# ⚙️ Backend Setup

```bash
cd backend
pip install -r ../requirements.txt
uvicorn index:app --reload
```

API will run at:

```text
http://127.0.0.1:8000/docs
```

---

# 💻 Frontend Setup

```bash
cd ui
npm install
npm run dev
```

Frontend will run at:

```text
http://localhost:5173
```

---

# 🔌 API Endpoint

### Predict Loan Approval

```http
POST /predict/{model_name}
```

### Example Request

```json
{
  "income": 50000,
  "credit_score": 700,
  "loan_amount": 10000,
  "years_employed": 5
}
```

---

# 🚀 Future Enhancements

• Cross-validation system
• Hyperparameter tuning engine
• Model explainability (SHAP/LIME)
• Cloud deployment (AWS / Render / Vercel)
• Authentication system
• Dashboard with analytics

---

# 📚 Learning Outcomes

This project demonstrates:

• Deep understanding of ML algorithms
• Ability to build systems **without high-level abstractions**
• Backend API development for ML
• Frontend integration with ML models
• Real-world ML product architecture

---

# 👨‍💻 Author

**Rahul Shakya**
BCA Student | Aspiring AI/ML Engineer/Full stack developer

---

# ⭐ Final Note

PredictaLab is not just a project — it is a **complete ML system built from the ground up**, demonstrating both **algorithmic understanding and engineering execution**.

If you find this project valuable, consider giving it a ⭐ on GitHub.
