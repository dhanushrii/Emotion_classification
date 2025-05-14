import React, { useEffect, useState } from "react";
import "./App.css"; // Import the CSS file

const App = () => {
  const [data, setData] = useState({ heart_rate: null, emotion: "" });

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://127.0.0.1:5000/get_emotion");
        const result = await response.json();
        setData(result);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };

    fetchData();
    const interval = setInterval(fetchData, 5000); // Refresh every 5 seconds

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="container">
      <div className="card">
        <h2>ECG Emotion Detection</h2>
        <p><strong>Heart Rate:</strong> {data.heart_rate ? `${data.heart_rate} BPM` : "Loading..."}</p>
        <p><strong>Predicted Emotion:</strong> {data.emotion || "Loading..."}</p>
      </div>
    </div>
  );
};

export default App;
