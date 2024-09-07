import webbrowser
import speech_recognition as sr
import pyttsx3
import platform
import os
import datetime

def say(text):
    if platform.system() == "Darwin":  # macOS
        os.system(f'say -v "Siri" {text}')
    elif platform.system() == "Windows":  # Windows
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)  # Change index to select different voice
        engine.setProperty('rate', 150)  # Adjust as needed
        engine.setProperty('volume', 1.0)  # Adjust as needed
        engine.say(text)
        engine.runAndWait()
    elif platform.system() == "Linux":  # Linux
        os.system(f'espeak "{text}"')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not catch that.")
            return None

if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am vision, your virtual assistant.")
    while True:
        query = takeCommand()
        if query:  # Check if query is not None
            sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
            for site in sites:
                if f"open {site[0]}".lower() in query.lower():
                    say("Opening " + site[0] + " sir...")
                    webbrowser.open(site[1])
                    break
            if "open music" in query.lower():
                musicpath = "C:/Users/abhay/Downloads/vinee-heights-126947.mp3"
                os.system(f"start {musicpath}")
            if "the time" in query.lower():
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                say(f"Sir, the time is {strfTime}")

            if "whatsapp" in query.lower():
                os.system(f"open/")

            # To open WhatsApp Desktop (if installed, works for Windows)
            if "whatsapp" in query.lower():
                say("Opening WhatsApp on your desktop...")
                os.system("start whatsapp:")

            if "good job" in query.lower():
                say("thank you sir")

                # Terminate the program if "go to sleep" command is detected
            if "go to sleep" in query.lower():
                say("Goodbye, sir. Going to sleep.")
                exit()  # Terminate the program