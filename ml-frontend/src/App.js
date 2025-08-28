import React, { useState } from "react";
import axios from "axios";

function App() {
  const [value1, setValue1] = useState("");
  const [value2, setValue2] = useState("");
  const [prediction, setPrediction] = useState("");

  // Replace with your Railway backend URL after deployment
  const API_URL = "https://your-railway-backend.up.railway.app/predict";

  const handlePredict = async () => {
    try {
      const response = await axios.post(API_URL, {
        values: [parseFloat(value1), parseFloat(value2)]
      });
      setPrediction(response.data.prediction);
    } catch (error) {
      console.error("Error fetching prediction:", error);
      setPrediction("Error occurred");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h2>Day0 Model Predictor</h2>
      <input
        type="number"
        value={value1}
        onChange={(e) => setValue1(e.target.value)}
        placeholder="Enter first value"
        style={{ margin: "5px", padding: "8px" }}
      />
      <input
        type="number"
        value={value2}
        onChange={(e) => setValue2(e.target.value)}
        placeholder="Enter second value"
        style={{ margin: "5px", padding: "8px" }}
      />
      <br />
      <button
        onClick={handlePredict}
        style={{ padding: "10px 20px", marginTop: "10px" }}
      >
        Predict
      </button>
      <h3>Prediction: {prediction}</h3>
    </div>
  );
}

export default App;
