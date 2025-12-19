import speech_recognition as sr
import pyttsx3
import pyjokes
import datetime
import pywhatkit
import os
import time
import random
import requests
from googlesearch import search

# Initialize the speech engine

engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return None
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the service.")
        return None

# Function to fetch and display search results from Google
def google_search(query):
    speak(f"Searching for {query} on Google...")
    print(f"Searching for: {query}")
    # Perform Google search using googlesearch library
    results = list(search(query, num_results=3))  # Get top 3 results
    if results:
        print("Here are the top search results:")
        for idx, result in enumerate(results, start=1):
            print(f"{idx}. {result}")
        speak(f"I found {len(results)} results. Here are the top results.")
    else:
        speak("Sorry, I couldn't find anything for that search.")
        print("No results found.")

# Function to fetch the weather (requires OpenWeatherMap API key)
def get_weather():
    api_key = ""  # Replace with your API key
    base_url = ""
    speak("Please tell me your city.")
    city = listen()
    
    if city:
        complete_url = base_url + "q=" + city + "&appid=" + api_key
        response = requests.get(complete_url)
        data = response.json()
        
        if data["cod"] != "404":
            main_data = data["main"]
            weather_desc = data["weather"][0]["description"]
            temp = main_data["temp"] - 273.15  # Convert from Kelvin to Celsius
            speak(f"The temperature in {city} is {temp:.2f}°C with {weather_desc}.")
        else:
            speak("Sorry, I couldn't find the weather information for that city.")
    else:
        speak("I didn't catch the city name. Please try again.")

# Function to play music from a local directory
def play_music():
    music_dir = "path_to_your_music_folder"  # Replace with your music folder path
    songs = os.listdir(music_dir)
    song = random.choice(songs)
    os.startfile(os.path.join(music_dir, song))
    speak(f"Playing {song}")

# Function to set reminders
def set_reminder(reminder_text, reminder_time):
    current_time = datetime.datetime.now()
    reminder_time = datetime.datetime.strptime(reminder_time, "%H:%M")
    delta = reminder_time - current_time
    if delta.days < 0:
        speak("The reminder time has already passed.")
        return
    speak(f"Reminder set for {reminder_time.strftime('%I:%M %p')}.")
    time.sleep(delta.total_seconds())
    speak(f"Reminder: {reminder_text}")

# Function to open applications (example: browser, calculator)
def open_application(query):
    if "calculator" in query:
        speak("Opening calculator.")
        os.system("calc")  # Windows calculator (change for Mac/Linux)
    elif "browser" in query:
        speak("Opening browser.")
        os.system("start chrome")  # Open Chrome browser on Windows (change for Mac/Linux)
    elif "notepad" in query:
        speak("Opening Notepad.")
        os.system("notepad")  # Notepad for Windows (change for Mac/Linux)
    else:
        speak("Sorry, I cannot open that application.")

# Main function to handle commands
def main():
    speak("Hello, I am your assistant. How can I help you today?")
    
    while True:
        query = listen()
        
        if query is None:
            continue
        
        if "time" in query:
            # Get the current time
            time_now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time_now}")

        elif "joke" in query:
            # Tell a joke
            joke = pyjokes.get_joke()
            speak(joke)

        elif "who is" in query or "what is" in query:
            # Wikipedia search (optional - needs internet)
            speak("Searching Google...")
            google_search(query)

        elif "weather" in query:
            # Fetch weather
            get_weather()

        elif "play music" in query:
            # Play music from local directory
            play_music()

        elif "reminder" in query:
            # Set reminder (example: "reminder at 14:30 to call mom")
            speak("Please tell me what the reminder is.")
            reminder_text = listen()
            speak("Please tell me the time for the reminder in HH:MM format.")
            reminder_time = listen()
            if reminder_text and reminder_time:
                set_reminder(reminder_text, reminder_time)
            else:
                speak("Sorry, I couldn't understand the reminder details.")

        elif "open" in query:
            # Open applications like browser, calculator, etc.
            open_application(query)

        elif "stop" in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
