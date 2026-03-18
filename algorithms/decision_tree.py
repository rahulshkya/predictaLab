import numpy as np
import pandas as pd

class Node:
    def __init__(self,left_node=None,right_node=None,value=None,threshold=None):
        self.node=node
        self.right_node
        self.value=value
        self.threshold=threshold
        self.left_node=left_node
class DecisionTree:
    def __init__(self,root,max_depth):
        self.root = root
        self.max_depth = max_depth

    def gini(self,y):
        counts=np.bincount(y)
        probs=counts/len(y)
        gini=1-np.sum(probs**2)
        return gini

    def best_split(self,X,best_gini,best_threshold,best_feature):
        best_gini=float(inf)
        best_threshold=None
        best_feature=None
        n_features=X.shape[1]
        for feature in range(n_features):
            thresholds=np.unique(X[:,feature])
            for threshold in thresholds:
                left_idx=X[:,feature] >= threshold
                right_idx=X[:,feature] < threshold

                if len(y[left_idx]) == 0 or len(y[right_idx]) == 0 :
                    continue
                gini_total=(left_idx/len(y)*self.gini(left_idx))+(right_idx/len(y)*self.gini(right_idx))
                
                