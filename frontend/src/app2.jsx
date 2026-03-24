import React from "react";
import Counter from "./counter.jsx";
import Form from "./form.jsx";
import Navbar from "./navbar.jsx";
function App2() {
let colors={color: "#000"};
  return (
    <div className="hero flip-scale-up-hor">
        
      <div className="overlay">
        <div className="hero-content">
          <h1 style={colors}>🚀 Rsmart</h1>
          <h2 style={colors}>Loan Prediction System</h2>

          <p className="subtitle" style={colors}>
            Predict your loan approval chances using advanced Machine Learning models.
          </p>

          <p className="desc" style={colors}>
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