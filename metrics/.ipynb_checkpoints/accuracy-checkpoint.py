def accuracy(y_true,y_pred):
    correct=np.sum(y_true,y_pred)
    return correct/len(y_true)