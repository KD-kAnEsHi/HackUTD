import os
import requests

# Get the API key from the environment variable
api_key = os.environ.get("SAMBANOVA_API_KEY")

# Greet the user
print("Hello. How can I assist you today?")

# Get input from the user
user_input = input("Enter your prompt: ")

# Define the request details
url = "https://api.sambanova.ai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}
data = {
    "model": "Meta-Llama-3.1-8B-Instruct",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": user_input},
    ],
    "temperature": 0.1,
    "top_p": 0.1,
}

# Make the API call
response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    print("\nAssistant's Response:")
    print(response.json().get("choices", [])[0].get("message", {}).get("content"))
else:
    print(f"Error: {response.status_code} - {response.text}")