import numpy as np
from collections import Counter

class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

class DecisionTree:
    
    def __init__(self, max_depth=5, max_features=None):
        self.max_depth = max_depth
        self.max_features = max_features 
        self.root = None

    def gini(self, y):
        if len(y) == 0: return 0
        counts = np.bincount(y)
        probs = counts / len(y)
        return 1 - np.sum(probs**2)

    def best_split(self, X, y):
        best_gini = float("inf")
        best_feature = None
        best_threshold = None
        n_features = X.shape[1]

        # Feature selection logic
        if self.max_features is None:
            feature_indices = np.arange(n_features)
        else:
            
            num_f = min(n_features, self.max_features)
            feature_indices = np.random.choice(n_features, num_f, replace=False)

        for feature in feature_indices:
            values = np.unique(X[:, feature])
            if len(values) <= 1:
                continue

            
            thresholds = (values[:-1] + values[1:]) / 2

            for threshold in thresholds:
                left_idx = X[:, feature] <= threshold
                right_idx = X[:, feature] > threshold

                if len(y[left_idx]) == 0 or len(y[right_idx]) == 0:
                    continue

                gini_left = self.gini(y[left_idx])
                gini_right = self.gini(y[right_idx])
                
                
                n = len(y)
                gini_total = (len(y[left_idx]) * gini_left + len(y[right_idx]) * gini_right) / n

                if gini_total < best_gini:
                    best_gini = gini_total
                    best_feature = feature
                    best_threshold = threshold

        return best_feature, best_threshold

    def build_tree(self, X, y, depth=0):
        # Stopping conditions
        if depth >= self.max_depth or len(np.unique(y)) == 1:
            leaf_value = Counter(y).most_common(1)[0][0]
            return Node(value=leaf_value)

        feature, threshold = self.best_split(X, y)

        if feature is None:
            leaf_value = Counter(y).most_common(1)[0][0]
            return Node(value=leaf_value)

        left_idx = X[:, feature] <= threshold
        right_idx = X[:, feature] > threshold

        # Recursion
        left_child = self.build_tree(X[left_idx], y[left_idx], depth + 1)
        right_child = self.build_tree(X[right_idx], y[right_idx], depth + 1)

        # Node constructor ke order ke hisab se pass kiya
        return Node(feature=feature, threshold=threshold, left=left_child, right=right_child)

    def fit(self, X, y):
        self.root = self.build_tree(X, y)

    def predict_row(self, x, node):
        if node.value is not None:
            return node.value

        if x[node.feature] <= node.threshold:
            return self.predict_row(x, node.left)
        else:
            return self.predict_row(x, node.right)

    def predict(self, X):
        return np.array([self.predict_row(x, self.root) for x in X])

# --- Test Case ---
if __name__ == "__main__":
    # Dummy data
    X_train = np.array([[2, 3], [10, 15], [3, 2], [12, 18]])
    y_train = np.array([0, 1, 0, 1]) # 0 = Small, 1 = Big

    dt = DecisionTree(max_depth=3)
    dt.fit(X_train, y_train)
    
    X_test = np.array([[1, 1], [15, 20]])
    print("Predictions:", dt.predict(X_test))