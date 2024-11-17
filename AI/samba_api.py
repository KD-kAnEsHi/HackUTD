import os
import requests
from pymongo import MongoClient
from MLModel import get_ideal_temperature, get_ideal_humidity, get_ideal_sunlight

# Set the API key directly (for testing purposes)
api_key = "61b887b1-aa89-4f51-8240-1b740d3e5a13"  # Change this after the event

# Step 1: Fetch Ideal Conditions from AI Model once at startup
ideal_temperature = get_ideal_temperature()
ideal_humidity = get_ideal_humidity()
ideal_sunlight = get_ideal_sunlight()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["sensors_db"]  
collection = db["sensors"]  

# Greet the user
print("Let's Analyze the sensor Data (Type 'quit' to exit)")

# Main loop for continuous interaction
while True:
    try:
        # Fetch fresh sensor data for each query
        sensor_data_cursor = collection.find()
        sensor_data_list = list(sensor_data_cursor)
        sensor_data_str = "\n".join([str(doc) for doc in sensor_data_list])
 
        # Get input from the user
        user_input = input("\nQuestions: ")
        
        # Check if user wants to quit
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Thank you for using the system. Goodbye!")
            break

        combined_prompt = (
            f"User Query: {user_input}\n"
            f"Ideal Temperature: {ideal_temperature}°C\n"
            f"Ideal Humidity: {ideal_humidity}%\n"
            f"Ideal Sunlight: {ideal_sunlight} hours\n"
            f"Sensor Data:\n{sensor_data_str}\n"
            "Please provide suggestions based on these values (this values are meant to help build the perfect ecossytem for plants in indoor farms to grow)"
        )

        # Define the request details for SambaNova API
        url = "https://api.sambanova.ai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        data = {
            "model": "Meta-Llama-3.1-8B-Instruct",
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

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please try again.")
        continue
