import "../sensors_db.sensors.json"
import {useState, useEffect} from 'react';
import data from "../sensors_db.sensors.json"

export default function Table() {
  const goodTemp = 16.8;

  // Fetch data from Flask API when component mounts
  useEffect(() => {
    // Adjust the URL if needed based on your Flask app's location
    fetch('http://localhost:5000/api/sensors') // Flask backend is running on localhost:5000
      .then(response => response.json())
      .then(data => {
        setSensorData(data); // Set the fetched data in state
      })
      .catch(error => console.error("Error fetching data:", error));
  }, []); // Empty array ensures this runs only once when the component mounts
  return (
    <>
      <table>
        <tr>
            <th>Light Level</th>
            <th>Temperature (C)</th>
            <th>Humidity</th>
            <th>Healthy</th>
        </tr>
        {
          data.map( (item) => (
            <tr>
              <td>{item.Light}</td>
              <td>{item.Temperature}</td>
              <td>{item.Humidity}</td>
              <td>{((item.Temperature <= goodTemp + 5.0) )? "Good" : "Bad"}</td>
              {/*|| (item.Temperature >= goodTemp - 5) */}
            </tr>
          ) )
          
        }
        
      </table>
    </>
  );
}
