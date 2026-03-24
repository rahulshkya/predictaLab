from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import uvicorn
import os
import sys
from fastapi.middleware.cors import CORSMiddleware


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

models = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "scaler.pkl"))

#input model 
class InputData(BaseModel):
    income: float
    credit_score: int
    loan_amount: float
    years_employed: int

app=FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # 🔥 testing ke liye (baad me specific karenge)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if __name__ == "__main__":
    uvicorn.run("index:app", host="127.0.0.1", port=8000, reload=True)


@app.get("/")
def read_root():
    return {"hello world"}

@app.post("/predict/{model_name}")
def predict(model_name:str,input_data:InputData):
    if model_name not in models:
        return {
            "error":"Invalid model",
            "available_models":list(models.keys())
        }
    if input_data.income == 0:
        return {"error": "Income cannot be zero"}
    model=models[model_name]
    loan_income_ratio=input_data.loan_amount/input_data.income
    input_df=[
        input_data.income,
        input_data.credit_score,
        input_data.loan_amount,
        input_data.years_employed,
        loan_income_ratio
    ]
    import pandas as pd

    input_features = pd.DataFrame([{
     "income": input_data.income,
     "credit_score": input_data.credit_score,
     "loan_amount": input_data.loan_amount,
     "years_employed": input_data.years_employed,
     "loan_income_ratio": loan_income_ratio
    }])

    input_scaled = scaler.transform(input_features)
    prediction=model.predict(input_scaled)
    if prediction[0] == 1:
        return {
            "model_name":model_name,
            "prediction":1,
            "status": "success"
            
        }
    else:
        return{
            "model_name":model_name,
            "prediction":0,
            "status": "failed"
        }