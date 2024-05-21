import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import tkinter as tk
from tkinter import *
import os
import threading

def talk(text):                                 #VA speaking text given as input
    os.system(f"say '{text}'")


def take_command():
    try:
        with sr.Microphone() as source:             #source of audio 
            print("Listening...")
            voice = listener.listen(source)                 #calling the recognizer to listen to the source
            command = listener.recognize_google(voice)     #pass the audio to google to understand the text
            command = command.lower()
            return command
    except:
        pass
    return None

def run_assistant():
    command = take_command()
    Output['text'] = command
    speak = ""
    if command is None:
        return
    
    if 'play' in command:
        print(f"[User]: {command}")
        song = command.lstrip('play ')
        user_request['text']=  (f"[User]: {command}")
        Output['text'] = '[Response]: playing ' + song
        speak = "playing " + song
        print('[Response]: Playing', song)
        pywhatkit.playonyt(song)
        
    elif 'time' in command:
        print(f"[User]: {command}")
        time = datetime.datetime.now().strftime('%I:%M %p')
        user_request['text']=  (f"[User]: {command}")
        Output['text'] = '[Response]: Current time is '  + time
        speak = 'Current time is ' + time
        print('[Response]: Current time is', time)
        
    elif 'who is' in command:
        person = command.replace('who is', '')
        print(f"[User]: {command}")
        info = wikipedia.summary(person, 1)
        print("[Response]:", info)
        user_request['text']=  (f"[User]: {command}")
        Output['text'] = "[Response]:"  + info
        speak = 'I have found something' + info
        
    elif 'how are you' in command:
        print(f"[User]: {command}")
        user_request['text']=  (f"[User]: {command}")
        Output['text'] = "[Response]: I am doing great."
        speak = "I am doing great."
        print("[Response]: I am doing great.")

    elif 'joke' in command:
        print(f"[User]: {command}")
        joke = pyjokes.get_joke()
        print("[Response]:", joke)
        user_request['text']=  (f"[User]: {command}")
        Output['text'] = "[Response]:" + joke
        speak = 'The joke is' + joke

    else:
        print(f"[User]: {command}")
        speak = "I am not sure if I understand."
        user_request['text']=  (f"[User]: {command}")
        Output['text'] =  "I am not sure if I understand."
        print("[Response]: I am not sure if I understand.")
        
    speak = speak.replace('"', '')
    speak = speak.replace("'", '')
    
    t = threading.Thread(target=talk, args=(speak,), daemon=True)
    t.start()
   

    
listener = sr.Recognizer()
root = Tk()
T = Text(root, height = 5, width = 50)
canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()
engine = pyttsx3.init(debug=False)
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.1)
user_request = Message(frame,
                       width = 350,
                       text='')
Output = Message(frame,
              width = 400,
              text='')
start = tk.Button(root, text="Activate", padx=10, pady=5, fg="black", bg="#263D42", command=lambda:run_assistant())
end = tk.Button(root, text="Exit", padx=30, pady=5, fg="black", bg="#263D42", command=sys.exit)
start.pack()
end.pack()
user_request.pack(side="top")
Output.pack(side="left")


root.mainloop()
