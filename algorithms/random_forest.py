import numpy as np
from collections import Counter
from algorithms.decision_tree import DecisionTree


class RandomForest:
    def __init__(self, n_trees=5, max_depth=5):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.trees = []

    def bootstrap_sample(self, X, y):
        n_samples = X.shape[0]
        indices = np.random.choice(n_samples, n_samples, replace=True)
        return X[indices], y[indices]

    def fit(self, X, y):
        self.trees = []

        for _ in range(self.n_trees):
            X_sample, y_sample = self.bootstrap_sample(X, y)

            n_features = X.shape[1]
            max_features = int(np.sqrt(n_features))

            tree = DecisionTree(
                  max_depth=self.max_depth,
                  max_features=max_features
                )
            tree.fit(X_sample, y_sample)

            self.trees.append(tree)

    def predict(self, X):
        tree_preds = []

        for tree in self.trees:
            pred = tree.predict(X)
            tree_preds.append(pred)

        tree_preds = np.array(tree_preds)
        tree_preds = tree_preds.T

        final_pred = []

        for preds in tree_preds:
            most_common = Counter(preds).most_common(1)[0][0]
            final_pred.append(most_common)

        return np.array(final_pred)