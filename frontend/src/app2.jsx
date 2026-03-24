import React from "react";
import Counter from "./counter.jsx";
import Form from "./form.jsx";
function App2() {

  return (
    <div className="hero">
      <div className="overlay">
        <div className="hero-content">
          <h1>🚀 Rsmart</h1>
          <h2>Loan Prediction System</h2>

          <p className="subtitle">
            Predict your loan approval chances using advanced Machine Learning models.
          </p>

          <p className="desc">
            Enter your financial details, choose a model, and get instant predictions with high accuracy.
          </p>

          <button 
  className="cta-btn"
  onClick={() => {
    document.getElementById("form-section").scrollIntoView({
      behavior: "smooth"
    });
  }}
>
  Get Started
</button>
        </div>
      </div>
    </div>
  );
}

export default App2;