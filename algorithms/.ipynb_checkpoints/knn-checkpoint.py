import numpy as np
from collections import Counter


class KNN:

    def __init__(self, k=3):
        self.k = k

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    # Euclidean distance
    def euclidean(self, x1, x2):
        return np.sqrt(np.sum((x1 - x2) ** 2))

    # Predict single data point
    def predict_point(self, x):

        distances = []

        for x_train in self.X_train:
            distance = self.euclidean(x, x_train)
            distances.append(distance)

        # nearest k indices
        k_indices = np.argsort(distances)[:self.k]

        # labels of k nearest points
        k_nearest_labels = []

        for i in k_indices:
            label = self.y_train[i]
            k_nearest_labels.append(label)

        # most common label
        most_common = Counter(k_nearest_labels).most_common(1)

        return most_common[0][0]

    # Predict for full dataset
    def predict(self, X):

        predictions = []

        for x in X:
            result = self.predict_point(x)
            predictions.append(result)

        return np.array(predictions)