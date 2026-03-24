import React, { useState } from "react";
import axios from "axios";
import App2 from './app2.jsx'
import './App.css'
function App() {
   
  const [form, setForm] = useState({
    income: "",
    credit_score: "",
    loan_amount: "",
    years_employed: ""
  });

  const [model, setModel] = useState("knn");
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async () => {
    try {
      const res = await axios.post(
        `http://localhost:8000/predict/${model}`,
        {
          income: Number(form.income),
          credit_score: Number(form.credit_score),
          loan_amount: Number(form.loan_amount),
          years_employed: Number(form.years_employed)
        }
      );
      console.log(res.data);
      setResult(res.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <>
    <App2/>
    <div id="form-section" className="container form-container">
  <div className="card">
    <h2>Loan Prediction</h2>

    <div className="form-group">
      <label>Income</label>
      <input name="income" onChange={handleChange} placeholder="Enter income" />
    </div>

    <div className="form-group">
      <label>Credit Score</label>
      <input name="credit_score" onChange={handleChange} placeholder="Enter credit score" />
    </div>

    <div className="form-group">
      <label>Loan Amount</label>
      <input name="loan_amount" onChange={handleChange} placeholder="Enter loan amount" />
    </div>

    <div className="form-group">
      <label>Years Employed</label>
      <input name="years_employed" onChange={handleChange} placeholder="Years employed" />
    </div>

    <div className="form-group">
      <label>Select Model</label>
      <select onChange={(e) => setModel(e.target.value)}>
        <option value="knn">KNN</option>
        <option value="LogisticRegression">Logistic</option>
        <option value="DecisionTree">Decision Tree</option>
        <option value="RandomForest">Random Forest</option>
      </select>
    </div>

    <button onClick={handleSubmit}>Predict</button>
  </div>
   </div>
      
      {result && (
  <div className="result-container">
    <div className="result-card">
      
      <h2 className="result-title">Prediction Result</h2>

      <div className="result-item">
        <span className="label">Prediction:</span>
        <span className={`value ${result.prediction === 1 ? "approved" : "rejected"}`}>
  {result.prediction === 1 ? "Approved ✅" : "Rejected ❌"}
</span>
      </div>

      <div className="result-item">
        <span className="label">Model Used:</span>
        <span className="value">{result.model_name}</span>
      </div>

     {result.status && (
  <div className="result-item">
    <span className="label">Request Status:</span>
    <span className="value success">
      {result.status === "success" ? "Processed Successfully ✅" : "Error ❌"}
    </span>
  </div>
)}

    </div>
  </div>
)}

      
  
    </>
  );
}

export default App;