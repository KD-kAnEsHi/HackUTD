import os
import requests

api_key = os.environ.get("SAMBANOVA_API_KEY")

print("Hello. How can I assist you today?")

user_input = input("Enter your prompt: ")

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

response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    print("\nAssistant's Response:")
    print(response.json().get("choices", [])[0].get("message", {}).get("content"))
else:
    print(f"Error: {response.status_code} - {response.text}")
