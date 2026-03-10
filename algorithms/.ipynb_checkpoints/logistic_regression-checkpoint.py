import numpy as np
class LogisticRegression :
    def __init__(self,lr,epochs):
        self.lr=lr
        self.epochs=epochs
        
    def sigmoid(self, z):
      z = np.clip(z, -500, 500)
      return 1/(1+np.exp(-z))
        
    def fit(self,X_train,y_train):
        self.X_train=X_train
        self.y_train=y_train
        n_samples,n_features=X_train.shape
        
        self.weights=np.zeros(n_features)
        self.bias=0

        for _ in range(self.epochs):

           z = np.dot(X_train, self.weights) + self.bias
           y_pred=self.sigmoid(z)

           loss=-np.mean(y_train*np.log(y_pred+1e-9)+(1-y_train)*np.log(1-y_pred+1e-9))

           error=y_pred-y_train

           dw=(1/n_samples)*np.dot(X_train.T,error)
           db=(1/n_samples)*np.sum(error)
           
           self.weights=self.weights -self.lr * dw
           self.bias=self.bias-self.lr*db

    
    def predict(self,X):
        z = np.dot(X, self.weights) + self.bias
        y_pred=self.sigmoid(z)
        y_pred_labels=[1 if i > 0.5 else 0 for i in y_pred]

        return np.array(y_pred_labels)
        