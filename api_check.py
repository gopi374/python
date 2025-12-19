import requests

# Load the API key and URL from your .env file
GROQ_API_KEY = "API_KEY"
GROQ_API_URL = "API_URL"

# Set up the headers and data for the request
headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

data = {
    "model": "mixtral-8x7b-32768",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is data?"}
    ],
    "max_tokens": 150,
    "temperature": 0.7
}

# Make the request
try:
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    print(f"Status Code: {response.status_code}")
    print("Response:", response.json())
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")