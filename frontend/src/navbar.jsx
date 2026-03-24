import React from "react";

function Navbar() {
  return (
    <nav className="navbar">
      <div className="nav-logo">🚀 Rsmart</div>

      <ul className="nav-links">
        <li>Home</li>
        <li>Predict</li>
        <li>About</li>
      </ul>

      <button
        className="nav-btn"
        onClick={() => {
          document.getElementById("form-section").scrollIntoView({
            behavior: "smooth",
          });
        }}
      >
        Get Started
      </button>
    </nav>
  );
}

export default Navbar;