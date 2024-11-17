import "../styles.css"
import { useEffect, useState } from "react";

export default function Input() {
  const [output, setOutput] = useState("");
  const outputGen = () => {
    setOutput("Hi");
  };

  

  return (
    <>
      <input className="input-box" placeholder="Type to ask AI a question" />
      <button className="input-button" onclick={outputGen}>Submit</button>
      <p>AI OUTPUT: </p>
      <p>{output}</p>
      <p>Based on the ideal temperatures and sensor data, here are some suggestions to create an
optimal environment for plant growth: </p>
<p>**Temperature:**</p>
<p>Current Temperature: 25°C (Sensor Data)</p>
<p>Ideal Temperature: 28°C</p>
<p>* Suggestion: Increase the temperature by 3°C to reach the ideal temperature. This can be
achieved by:</p>
<p>+ Using heating elements (e.g., heaters, heat mats) to warm the environment.</p>
<p>+ Adjusting the air circulation to ensure even heat distribution.</p>
<p>+ Considering using a temperature control system to maintain a stable temperature.</p>
<p>**Humidity:**</p>
<p>Current Humidity: 60% (Sensor Data)</p>
<p>Ideal Humidity: 64%</p>
<p>* Suggestion: Increase the humidity by 4% to reach the ideal level. This can be achieved by:</p>
<p>+ Using a humidifier to add moisture to the air.</p>
<p>+ Ensuring proper air circulation to prevent water condensation.</p>
<p>+ Monitoring the humidity levels regularly to avoid over-humidification.</p>
<p>**Sunlight:**</p>
<p>Current Sunlight: 6 hours (Sensor Data)</p>
<p>Ideal Sunlight: 7 hours</p>
<p>* Suggestion: Increase the sunlight exposure by 1 hour to reach the ideal level. This can be
achieved by:</p>
<p>+ Adjusting the lighting schedule to provide more light during the day.</p>
<p>+ Using supplemental lighting (e.g., LED grow lights) to extend the daylight period.</p>
<p>+ Considering using a photoperiod control system to maintain a consistent light-dark cycle.</p>
<p>**Additional Suggestions:**</p>
<p>* Monitor the CO2 levels: Ensure the CO2 levels are within the optimal range (400-600 ppm) for
plant growth.</p>
<p>* Maintain air circulation: Ensure proper air circulation to prevent the buildup of CO2 and
maintain a healthy environment.</p>
<p>* Monitor pH levels: Ensure the pH levels are within the optimal range (5.5-6.5) for plant growth.</p>
<p>* Watering schedule: Adjust the watering schedule to ensure the plants receive the right amount
of water, taking into account the humidity and temperature levels.</p>
<p>By implementing these suggestions, you can create an optimal environment for plant growth in
your indoor farm.</p>
<p>Old Accuracy (Cross-Validation): 0.6962962962962963</p>
<p>New Accuracy (Test Set): 0.7461538461538462
</p>
    </>
  );
}