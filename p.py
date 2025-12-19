import requests
import json

# Replace with your OpenAI API key
API_KEY = ""
API_URL = ""

# User input (this could come from a function or input prompt)
user_input = "what is data?"

# Request data payload
data = {
    "model": "gpt-3.5-turbo",  # You can change the model if needed
    "prompt": user_input,
    "max_tokens": 150
}

# Set up headers for the request
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Make the POST request to the OpenAI API
response = requests.post(API_URL, headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.status_code == 200:
    response_data = response.json()
    print("Bot response:", response_data['choices'][0]['text'].strip())
else:
    print(f"Error: {response.status_code}, {response.text}")
