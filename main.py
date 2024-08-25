import pyttsx3
import platform
import os

def say(text):
    # Check the operating system
    if platform.system() == "Darwin":  # macOS
        # Use Siri's voice with the 'say' command
        os.system(f'say -v "Siri" {text}')
    elif platform.system() == "Windows":  # Windows
        # Initialize pyttsx3 engine
        engine = pyttsx3.init()

        # List available voices
        voices = engine.getProperty('voices')
        for index, voice in enumerate(voices):
            print(f"Voice {index}: {voice.name}")

        # Choose a voice (example index 0, change as needed)
        # You may need to experiment with different voices to find one you like
        engine.setProperty('voice', voices[0].id)  # Change index to select different voice

        # Set speech rate (words per minute)
        engine.setProperty('rate', 150)  # Adjust as needed

        # Set volume (0.0 to 1.0)
        engine.setProperty('volume', 1.0)  # Adjust as needed

        # Speak the text
        engine.say(text)
        engine.runAndWait()
    elif platform.system() == "Linux":  # Linux
        # On Linux, you can use 'espeak' or 'festival'
        os.system(f'espeak "{text}"')

if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am Edith your virtual assistant")
