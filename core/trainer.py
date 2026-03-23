import pandas as pd

from preprocessing.train_test_split import train_test_split
from metrics.accuracy import accuracy
from algorithms.logistic_regression import LogisticRegression
from algorithms.knn import KNN
from algorithms.decision_tree import DecisionTree
from core.model_selector import best_model_selector
from sklearn.preprocessing import StandardScaler
from algorithms.random_forest import RandomForest

def train_model():

    # Load dataset
    df = pd.read_csv("data/loan_approval.csv")

    # Feature Engineering
    df = df.drop(columns=["name", "city"])

    df["loan_income_ratio"] = df["loan_amount"] / df["income"]

    # Split features and target
    X = df.drop(columns=["loan_approved", "points"])
    y = df["loan_approved"]

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Scaling
    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Convert target to numpy
    y_train = y_train.values
    y_test = y_test.values

    # Models
    models = {
        "LogisticRegression": LogisticRegression(lr=0.01, epochs=1000),
        "knn": KNN(k=5),
        "DecisionTree":DecisionTree(max_depth=3),
        "RandomForest": RandomForest(n_trees=5, max_depth=5)
    }

    # Model selection
    best_model_name, best_model = best_model_selector(
    models, X_train, y_train, X_test, y_test, accuracy
)

    # Final trainings
    for name , model in models.items():
        model.fit(X_train,y_train)

    # Prediction
    pred = best_model.predict(X_test)

    # Accuracy
    score = accuracy(y_test, pred)

    print(f"Final Best Model {best_model_name} and his Accuracy is :", score)

    import joblib

    joblib.dump(models,"model.pkl")
    joblib.dump(scaler,"scaler.pkl")

    
    print("models are saved succesfullly")
    