import os
import requests

api_key = os.environ.get("SAMBANOVA_API_KEY") # Get the API key from the environment variable

                                                                # URLs for sensor data and ML results from the backend ( Example Links )
sensor_data_url = "http://your-backend-url/sensor-data"
ml_results_url = "http://your-backend-url/ml-results"

# Fetch sensor data
sensor_response = requests.get(sensor_data_url)
if sensor_response.status_code == 200:
    sensor_data = sensor_response.json()
else:
    print(f"Error fetching sensor data: {sensor_response.status_code}")
    sensor_data = {}

# Fetch ML results
ml_response = requests.get(ml_results_url)
if ml_response.status_code == 200:
    ml_results = ml_response.json()
else:
    print(f"Error fetching ML results: {ml_response.status_code}")
    ml_results = {}

# Greet the user
print("Let Analyze The Sensor Data")

# Get input from the user
user_input = input("Input Questions")

# Combine user input with sensor data and ML results
combined_prompt = f"User Query: , Here is the sensor data the user is asing questions related so{user_input}\nSensor Data: {sensor_data}\nML Results: {ml_results}"

# Define the request details for SambaNova API
url = "https://api.sambanova.ai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}
data = {
    "model":  "Meta-Llama-3.1-8B-Instruct",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": combined_prompt},
    ],
    "temperature": 0.1,
    "top_p": 0.1,
}

# Make the API call to SambaNova
response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    print("\nAssistant's Response:")
    print(response.json().get("choices", [])[0].get("message", {}).get("content"))
else:
    print(f"Error: {response.status_code} - {response.text}")
    