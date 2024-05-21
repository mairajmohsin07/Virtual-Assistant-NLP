# Virtual Assistant NLP Project

## Overview
This project implements a simple voice-activated virtual assistant using Natural Language Processing (NLP). The assistant can respond to various voice commands, such as playing music, providing the current time, retrieving information from Wikipedia, telling jokes, and more. It uses speech recognition to process voice commands and uses text-to-speech for responses.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
  - [Install the required libraries](#install-the-required-libraries)
  - [Running the Virtual Assistant](#running-the-virtual-assistant)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Activating the Virtual Assistant](#activating-the-virtual-assistant)
  - [Available Commands](#available-commands)
  - [Deactivating the Virtual Assistant](#deactivating-the-virtual-assistant)
  - [Example Commands](#example-commands)
- [Contributions](#contributions)
- [License](#license)

## Features
- Voice command recognition using Google's Speech Recognition API.
- Text-to-speech responses.
- Play music from YouTube.
- Provide the current time.
- Retrieve and read out information from Wikipedia.
- Tell jokes using the pyjokes library.
- Graphical User Interface (GUI) using Tkinter.

## Requirements
- Python 3.9
- `speech_recognition`
- `pyttsx3`
- `pywhatkit`
- `wikipedia`
- `pyjokes`
- `tkinter`
- `opencv-python` (for macOS, replace `os.system(f"say '{text}'")` with `engine.say(text)` and `engine.runAndWait()` in the `talk` function)

## Setup

### Install the required libraries
You can install the necessary libraries using pip:
```sh
pip install speechrecognition pyttsx3 pywhatkit wikipedia pyjokes opencv-python
```

### Running the Virtual Assistant
1. Clone the repository:
```sh
git clone https://github.com/yourusername/virtual-assistant-nlp.git
```
2. Navigate to the project directory:
```sh
cd virtual-assistant-nlp
```
3. Run the main script:
```sh
python main.py
```

## Project Structure
```
├── main.py    # Main script with the complete code
```

## Usage

### Activating the Virtual Assistant
1. Run the `main.py` script.
2. Click the "Activate" button in the GUI.
3. Speak your command when prompted ("Listening...").

### Available Commands
- **Play Music**: "Play [song name]"
- **Current Time**: "time"
- **Wikipedia Information**: "Who is [person's name]"
- **Check Status**: "how are you"
- **Tell a Joke**: "joke"

### Deactivating the Virtual Assistant
- Click the "Exit" button in the GUI to close the application.

## Example Commands
- "Play Shape of You"
- "What time is it?"
- "Who is Albert Einstein?"
- "How are you?"
- "Tell me a joke"

## Contributions
Feel free to fork this repository and contribute by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.
