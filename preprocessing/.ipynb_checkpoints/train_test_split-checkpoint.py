import numpy as np
import pandas as pd

def train_test_split(X, y, test_size=0.2, random_state=None):
    if random_state:
        np.random.seed(random_state)
    
    # Total rows count nikalne ke liye shape[0] use kiya
    n_samples = X.shape[0]
    indices = np.arange(n_samples)
    np.random.shuffle(indices)

    test_count = int(n_samples * test_size)

    # Indices ko split kiya
    test_indices = indices[:test_count]
    train_indices = indices[test_count:]

    # --- YAHAN CHANGE HAI ---
    # Agar data Pandas hai toh .iloc use hoga, agar Numpy hai toh normal slicing
    if hasattr(X, 'iloc'):
        X_train, X_test = X.iloc[train_indices], X.iloc[test_indices]
        y_train, y_test = y.iloc[train_indices], y.iloc[test_indices]
    else:
        X_train, X_test = X[train_indices], X[test_indices]
        y_train, y_test = y[train_indices], y[test_indices]

    return X_train, X_test, y_train, y_test