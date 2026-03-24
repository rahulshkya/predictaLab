export default function Form({ handleChange, handleSubmit, setModel }) {
  return (
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
  );
}