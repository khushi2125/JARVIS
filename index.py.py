import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import time
from songs import songs_dict
from songs import play_song  # Import play_song function

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen(prompt=None):
    if prompt:
        speak(prompt)
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.WaitTimeoutError:
            speak("You were silent.")
        # except sr.UnknownValueError:
        #     speak("I didn't catch that.")
        except sr.RequestError:
            speak("Please check your internet.")
    return ""

def open_app(command):
    if "notepad" in command:
        os.system("notepad")
        speak("Opening Notepad")
    elif "calculator" in command:
        os.system("calc")
        speak("Opening Calculator")
    elif "file explorer" in command:
        os.system("explorer")
        speak("Opening File Explorer")
    elif "chrome" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Chrome")
    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")
    elif "facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")
    elif "google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")
    else:
        speak("I don't recognize that app.")

def google_search(command):
    query = command.replace("search", "").strip()
    if query:
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    else:
        speak("What do you want me to search?")

# Main loop with wake word
if __name__ == "__main__":
    speak("Hello, I am Jarvis. Say 'Jarvis' to wake me up.")
    
    while True:
        wake = listen()
        if "jarvis" in wake:
            speak("Yes?")
            time.sleep(1.5)
            command = listen("What would you like to do?")
            
            if not command:
                speak("I didn't hear any command.")
                continue

            if "exit" in command or "stop" in command:
                speak("Goodbye!")
                break
            elif "play" in command:
                song_query = command.replace("play", "").strip()
                play_song(song_query, speak)
            elif "open" in command:
                open_app(command)
            elif "search" in command:
                google_search(command)
            elif "how are you" in command:
                speak("I am fully functional.")
            elif "your name" in command:
                speak("I am Jarvis.")
            else:
                speak("You said: " + command)
