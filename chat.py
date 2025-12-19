import speech_recognition as sr
import pyttsx3
import requests
from datetime import datetime

# Replace this with your API key from OpenAI
API_KEY = ""
API_URL = ""

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level

def listen_to_audio():
    """Listen to audio input from the user and return the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

    try:
        # Convert audio to text
        user_input = recognizer.recognize_google(audio)
        print(f"You said: {user_input}")
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I could not understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, the speech recognition service is down.")
        return ""

def get_response(user_input):
    """Get a response from the chatbot based on user input."""
    user_input = user_input.lower()

    # Predefined responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "what are you doing" in user_input:
        return "I'm here waiting to assist you. How can I help?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm functioning as expected! How about you?"
    elif "your name" in user_input:
        return "I'm a chatbot created in Python. What's your name?"
    elif "weather" in user_input:
        return "I cannot check the weather, but you can check a weather app or website."
    elif "time" in user_input:
        current_time = datetime.now().strftime('%H:%M:%S')
        return f"The current time is {current_time}."
    elif "date" in user_input:
        current_date = datetime.now().strftime('%Y-%m-%d')
        return f"Today's date is {current_date}."
    elif "joke" in user_input:
        return "Why don’t scientists trust atoms? Because they make up everything!"
    else:
        return fetch_api_response(user_input)

def fetch_api_response(query):
    """Fetch response from OpenAI API based on the query."""
    try:
        headers = {
            "Authorization": "Bearer {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}"
            "Content-Type" "application/json"
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ],
            "max_tokens": 150,
            "temperature": 0.7
        }
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"API error: {e}")
        return "I'm sorry, I couldn't process that."

def speak(text):
    """Speak the given text using text-to-speech."""
    print(f"Bot: {text}")  # Print the bot's response on screen
    engine.say(text)
    engine.runAndWait()

def chatbot():
    """Run the chatbot, continuously listening for user input and providing responses."""
    print("Hello! I'm your chatbot. Say 'exit' to end the conversation.")
    
    while True:
        # Get audio input from the user
        user_input = listen_to_audio()

        # If the user says 'exit', stop the chatbot
        if 'exit' in user_input.lower():
            speak("Goodbye! Take care.")
            break

        if user_input:
            # Get the chatbot's response
            response = get_response(user_input)

            # Output the response through text-to-speech
            speak(response)

if __name__ == "__main__":
    # Run the chatbot in a continuous loop
    chatbot()
