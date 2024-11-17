// This is meant for geting the information from the backend and, data from mongodb and the API 

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

function App() {
  const [sensorData, setSensorData] = useState([]);
  const [idealConditions, setIdealConditions] = useState({});

  useEffect(() => {
    // This pretty much fethc the sensor data from backend
    const fetchSensorData = async () => {
      const response = await axios.get('http://localhost:5000/api/sensor_data');  // Adjust URL based on Flask server port
      setSensorData(response.data);
    };

    // Fetch the ideal data from the model after its done running
    const fetchIdealConditions = async () => {
      const response = await axios.get('http://localhost:5000/api/ideal_conditions');
      setIdealConditions(response.data);
    };

    fetchSensorData();
    fetchIdealConditions();

    const intervalId = setInterval(fetchSensorData, 5000); // Poll every 5 seconds for real-time updates

    return () => clearInterval(intervalId); // Cleanup interval on component unmount
  }, []);

  // Prepare data for charting (assuming temperature data)
  const chartData = {
    labels: sensorData.map((data) => new Date(data.timestamp).toLocaleTimeString()),
    datasets: [
      {
        label: 'Temperature',
        data: sensorData.map((data) => data.temperature),
        fill: false,
        borderColor: 'rgba(75,192,192,1)',
      },
      // Add more datasets for humidity and sunlight if needed
    ],
  };

  return (
    <div>
      <h1>Real-Time Sensor Dashboard</h1>
      <div>
        <h2>Ideal Conditions</h2>
        <p>Temperature: {idealConditions.temperature}°C</p>
        <p>Humidity: {idealConditions.humidity}%</p>
        <p>Sunlight: {idealConditions.sunlight} hours</p>
      </div>

      <div>
        <h2>Sensor Data (Real-Time)</h2>
        <Line data={chartData} />
      </div>
    </div>
  );
}

