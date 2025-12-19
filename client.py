import requests

# API URL (update this if the Flask app is running on a different host or port)
api_url = ""

def chat_with_bot(message):
    """Send a message to the chatbot API and get the response."""
    try:
        # JSON payload
        payload = {"message": message}

        # Send POST request to the API
        response = requests.post(api_url, json=payload)

        # Check the HTTP response status
        if response.status_code == 200:
            # Parse and return the chatbot's response
            return response.json().get("response", "No response from chatbot")
        else:
            # Handle non-200 HTTP responses
            return f"Error: {response.status_code} - {response.json().get('error', 'Unknown error')}"
    except Exception as e:
        # Handle connection errors or other exceptions
        return f"Error: Unable to connect to the API. Details: {e}"

if __name__ == "__main__":
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        # Get user input
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break

        # Get chatbot response
        bot_response = chat_with_bot(user_input)
        print(f"Chatbot: {bot_response}")
