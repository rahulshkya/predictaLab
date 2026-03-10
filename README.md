# 🚀 PredictaLab — AutoML Loan Prediction System (From Scratch)

PredictaLab is a **machine learning AutoML-style system built from scratch in Python** designed to automatically train multiple machine learning algorithms, evaluate their performance, and select the best performing model.

The project focuses on understanding **how machine learning algorithms and ML pipelines work internally** by implementing core components without relying on high-level ML frameworks.

Currently, PredictaLab is applied to a **Loan Approval Prediction problem**, where the system predicts whether a loan should be approved based on applicant data.

---

# 📌 Project Objective

The main objective of PredictaLab is to:

• Build machine learning algorithms **from scratch**
• Design a **complete ML pipeline**
• Automatically **compare multiple models**
• Select the **best performing model automatically**
• Understand **how AutoML systems work internally**

---

# ⚙️ Machine Learning Pipeline

PredictaLab follows a structured ML workflow:

```text
Dataset
   ↓
Feature Engineering
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Automatic Best Model Selection
```

This pipeline allows the system to behave like a **basic AutoML engine**.

---

# ✨ Current Features

• Logistic Regression implemented **from scratch**
• K-Nearest Neighbors (KNN) implemented **from scratch**
• Custom **train_test_split** implementation
• Custom **accuracy metric**
• Automatic **model comparison system**
• Feature scaling using StandardScaler
• Modular ML pipeline architecture

---

# 🧠 Algorithms Implemented (Current)

### Logistic Regression

Implemented using:

• Sigmoid activation
• Gradient Descent optimization
• Binary classification

---

### K-Nearest Neighbors (KNN)

Implemented using:

• Euclidean distance
• Majority voting
• Configurable K value

---

# 📊 Example Output

```text
LogisticRegression accuracy: 93.00%
knn accuracy: 97.75%

Final Best Model: knn
Final Best Model Accuracy: 97.75%
```

The system automatically determines the best performing model.

---

# 🏦 Use Case — Loan Prediction

PredictaLab is currently applied to a **Loan Approval Prediction dataset**.

The model predicts whether a loan application should be approved based on applicant features such as:

• income
• loan amount
• loan-income ratio
• applicant profile data

This helps simulate how machine learning can assist **financial decision systems**.

---

# 📂 Project Structure

```text
PredictaLab
│
├── algorithms
│   ├── logistic_regression.py
│   └── knn.py
│
├── core
│   ├── trainer.py
│   └── model_selector.py
│
├── preprocessing
│   └── train_test_split.py
│
├── metrics
│   └── accuracy.py
│
├── data
│   └── loan_approval.csv
│
├── requirements.txt
├── README.md
└── main.py
```

---

# 🛠️ Technologies Used

Python
NumPy
Pandas
Scikit-learn (for feature scaling)

---

# 📥 Installation

Clone the repository

```bash
git clone https://github.com/your-username/PredictaLab.git
```

Navigate to project directory

```bash
cd PredictaLab
```

Install required libraries

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
python main.py
```

---

# 🚀 Future Improvements

PredictaLab will be expanded into a more powerful AutoML system with additional algorithms and capabilities.

Planned upgrades include:

• Decision Tree (from scratch)
• Random Forest Classifier
• Naive Bayes Classifier
• Ensemble Learning techniques
• Hyperparameter tuning
• Automatic K selection for KNN
• Cross Validation
• Model persistence (saving trained models)

The goal is to gradually evolve PredictaLab into a **mini machine learning framework**.

---

# 📚 Learning Goals

This project helps in understanding:

• Machine learning algorithms internally
• Data preprocessing techniques
• ML pipeline architecture
• Model evaluation and comparison
• Debugging and building ML systems from scratch

---

# 👨‍💻 Author

Rahul

BCA Student
Aspiring **AI Engineer**

---

# ⭐ Project Motivation

PredictaLab was created to deeply understand **machine learning algorithms and AutoML systems** by implementing core ML components from scratch instead of relying completely on existing libraries.

If you found this project interesting, consider giving it a ⭐.
