import React, { useState } from "react";
import axios from "axios";
import App2 from './app2.jsx'
import './App.css'
import Navbar from "./navbar.jsx";
import Form from "./form.jsx";
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
    <Navbar />
    <App2/>
     <Form handleChange={handleChange} handleSubmit={handleSubmit} setModel={setModel} />
      
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