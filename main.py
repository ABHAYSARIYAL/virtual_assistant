import webbrowser
import speech_recognition as sr
import pyttsx3
import platform
import os
import datetime
import time
import threading

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

def say(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    r.pause_threshold = 0.6
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            return r.recognize_google(audio, language="en-in")
        except sr.UnknownValueError:
            return None

def listenForActivation():
    r = sr.Recognizer()
    r.pause_threshold = 0.6
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            if "hello vision" in r.recognize_google(audio, language="en-in").lower():
                say("Yes sir, I am here.")
                return True
        except sr.UnknownValueError:
            return False
    return False

if __name__ == '__main__':
    while True:
        if listenForActivation():
            say("vision, your virtual assistant.")
            last_valid_command_time = time.time()
            TIMEOUT_DURATION = 120

            while True:
                query = takeCommand()
                current_time = time.time()

                if current_time - last_valid_command_time > TIMEOUT_DURATION:
                    say("I am sleeping sir. Wake me up when you need any help.")
                    break

                if query:
                    last_valid_command_time = current_time

                    commands = {
                        "open youtube": lambda: os.startfile("https://www.youtube.com"),
                        "open google": lambda: os.startfile("https://www.google.com"),
                        "open music": lambda: os.system("start C:/Users/abhay/Downloads/vinee-heights-126947.mp3"),
                        "the time": lambda: say(f"Sir, the time is {datetime.datetime.now().strftime('%H:%M:%S')}")
                    }

                    for command, action in commands.items():
                        if command in query.lower():
                            action()
                            break

                    if "good job" in query.lower():
                        say("Thank you, sir")

                    if "go to sleep" in query.lower():
                        say("Goodbye, sir. Going to sleep.")
                        break
