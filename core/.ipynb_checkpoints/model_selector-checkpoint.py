from metrics.accuracy import accuracy

def best_model_selector(models,X_train,y_train,X_test,y_test,accuracy):
    results={}
    for name,model in models.items():

        #train
        model.fit(X_train,y_train)

        #predict
        y_pred=model.predict(X_test)

        #evaluation

        score=accuracy(y_test,y_pred)

        #store results model name and their accuracy score
        results[name]=score

        print(f"{name} accuracy: {score*100:.2f}%")

    best_model_name=max(results,key=results.get)


    best_model = models[best_model_name]

    return best_model_name,best_model