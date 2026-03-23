import React, { useState } from "react";
import axios from "axios";
import App2 from './app2.jsx'

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

      setResult(res.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      
      <App2 />

      <input name="income" onChange={handleChange} placeholder="Income" />
      <input name="credit_score" onChange={handleChange} placeholder="Credit Score" />
      <input name="loan_amount" onChange={handleChange} placeholder="Loan Amount" />
      <input name="years_employed" onChange={handleChange} placeholder="Years Employed" />

      <br /><br />

      <select onChange={(e) => setModel(e.target.value)}>
        <option value="knn">KNN</option>
        <option value="LogisticRegression">Logistic</option>
        <option value="DecisionTree">Decision Tree</option>
        <option value="RandomForest">Random Forest</option>
      </select>

      <br /><br />

      <button onClick={handleSubmit}>Predict</button>

      <br /><br />

      {result && (
        <div>
          <h2>{result.prediction}</h2>
          <p>Model: {result.model_name}</p>
          {result.status && <p>Status: {result.status}</p>}
        </div>
      )}

    </div>
  );
}

export default App;