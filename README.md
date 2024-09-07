---

# Virtual Assistant using Python

This is a simple Python-based virtual assistant that can perform various tasks like opening websites, playing music, checking the time, and opening WhatsApp. The assistant listens to your voice commands, processes them, and responds accordingly.

## Features
- **Voice Interaction**: The assistant uses `speech_recognition` to listen for voice commands and `pyttsx3` to respond with spoken feedback.
- **Web Automation**: You can open popular websites like YouTube, Wikipedia, and Google just by speaking.
- **Play Music**: Play local music files on your computer through voice command.
- **Check Time**: Ask for the current time and get a voice response.
- **WhatsApp Access**: Open WhatsApp on your desktop through voice command.
- **Go to Sleep**: End the assistant's operation by saying "go to sleep".

## Requirements

To run this virtual assistant, you need the following Python packages:

- `speech_recognition`
- `pyttsx3`
- `webbrowser`
- `platform`
- `os`
- `datetime`

You can install the required packages using:

```bash
pip install SpeechRecognition pyttsx3
```

For using the microphone with `speech_recognition`, you may need to install additional dependencies, such as `pyaudio`:
```bash
pip install pyaudio
```

## How to Use

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/virtual-assistant.git
cd virtual-assistant
```

2. **Run the Python script**:

Make sure you have a working microphone connected.

```bash
python virtual_assistant.py
```

3. **Give voice commands**:
   - **Open websites**: Say "Open YouTube", "Open Wikipedia", or "Open Google".
   - **Play music**: Say "Open music" to play a predefined music file.
   - **Check the time**: Say "What is the time?" or "The time".
   - **Open WhatsApp**: Say "Open WhatsApp".
   - **End the session**: Say "Go to sleep" to terminate the program.

## Example Voice Commands

- **"Open YouTube"**: Opens YouTube in your web browser.
- **"Open music"**: Plays a local MP3 file.
- **"What is the time?"**: Announces the current time.
- **"Open WhatsApp"**: Opens the WhatsApp desktop application.
- **"Go to sleep"**: Terminates the virtual assistant.

## Customization

- You can customize the websites opened by modifying the `sites` list in the script.
- Change the local music file path to your own file in the `"open music"` section.
- To change the voice or speed of the text-to-speech engine, modify the `pyttsx3` properties under the `say()` function.

## Known Issues
- The script relies on the default microphone input and may not work properly if your system doesn't have a configured microphone.
- On Linux, `espeak` is required for text-to-speech functionality.
- On Windows, if WhatsApp is not installed, the command to open WhatsApp will fail.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributing

Feel free to submit pull requests or report issues to help improve this project.

---

**Author**: [abhay sariyal](https://github.com/ABHAYSARIYAL)

---

