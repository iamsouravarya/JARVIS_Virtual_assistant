import tkinter as tk
from PIL import ImageTk, Image
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import subprocess
import pyjokes
import music_lib  
from googleapiclient.discovery import build
from googlesearch import search
import tkinter as tk
from PIL import ImageTk, Image
API_KEY = "AIzaSyDjDpHyYG8C-DqSRFd3cMTMaR9JER5fKfI"

from tkinter import *
from PIL import Image,ImageTk

#Creating background GUI
root = Tk()
root.geometry("250x250")
root.minsize(100, 100)
root.title("Jarvis...")

#Image 
image_path = (r"C:/Users/TestUser/Desktop/JARVIS/photos/jarvis_face.png")
image = Image.open(image_path)
photo=ImageTk.PhotoImage(image)
image_lable=Label(image=photo, background="black")
image_lable.pack(fill="x", padx=0, pady=0, side="top")
name=Label(text="BASIC CALCULATOR")
name.pack()
engine = pyttsx3.init()
#frame for Text and Button both
frame1=Frame(root, background="black")
frame1.pack(side="bottom")
#Text hELLO JARVIS HERE IN GUI
title_lable=Label(frame1,text="Hello, I'm Jarvis...", padx=10, pady=0, anchor="sw", font="15", background="black", foreground="white")
title_lable.pack(side="left")
def hello():
    engine.say("Initialzing Jarvis....")
    engine.runAndWait()
#Button
B1=Button(frame1, text="Initialize now...", command=hello , padx=10,pady=0,background="black", foreground="white", borderwidth=1)
B1.pack(anchor="ne", side="right")

def text():
    recognizer = sr.Recognizer()
    activated = False
    engine.say("Initializing Jarvis")
    engine.runAndWait()
    
    while True:
        try:
            print("Recognizing....")
            data = recognizer.recognize_google(audio)
            print(data)
            with sr.Microphone() as source:
                print("Listening...")
                # recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            

            if "jarvis" in data.lower() and not activated:
                print("Jarvis activated")
                engine.say("Ya")
                engine.runAndWait()
                activated = True  # Activate Jarvis

            if activated:
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = recognizer.listen(source, timeout=4, phrase_time_limit=2)

                if data.lower().startswith("google") or data.lower().startswith("search"):
                    search_query = data.lower().split("search for", 1)[1].strip()
                    print(f"Searching for {search_query}, Sir....") 
                    engine.say(f"Searching for {search_query}, Sir....")
                    engine.runAndWait()
                    url=f"https://www.google.com/search?q={search_query}"
                    webbrowser.open(url)


                if data.lower().startswith("play"):
                    play_query=data.lower().split("play",1)[1]
                    print(f"Playing, {play_query}, Sir....")
                    engine.say(f"Playing,{play_query}, Sir...")
                    # video_id=play_query.strip()
                    play_url = f"https://www.youtube.com/results?search_query={play_query}"
                    webbrowser.open(play_url)

                # # Open YouTube
                # if "open youtube" in data.lower():
                #     print("Opening Youtube...")
                #     engine.say("Opening Youtube....")
                #     engine.runAndWait()
                #     webbrowser.open("https://www.youtube.com/")

                # Greet
                elif "greet" in data.lower():
                    current_time = datetime.datetime.now().time()
                    if current_time < datetime.time(12, 0):
                        print("Reacting to 'greet' command...")
                        engine.say("Hello there! Good morning! I am Jarvis. Namaste and have a great day.")
                    elif current_time < datetime.time(16, 0):
                        print("Reacting to 'greet' command...")
                        engine.say("Hello there! Good afternoon! I am Jarvis. Namaste and have a great day.")
                    else:
                        print("Reacting to 'greet' command...")
                        engine.say("Hello there! Good evening! I am Jarvis. Namaste and have a great day.")
                    engine.runAndWait()

                # Introduce Yourself
                elif "yourself" in data.lower():
                    print("Introducing myself......")
                    engine.say("Hi, myself Jarvis, created using Python. Currently in testing mode, soon will be 100 percent ready. Haha hahaha.")
                    engine.runAndWait()

                # Open Notepad
                elif "notepad" in data.lower():
                    print("Opening Notepad....")
                    engine.say("Opening Notepad....")
                    engine.runAndWait()
                    subprocess.Popen(["notepad.exe"])

                # Jokes
                elif "joke" in data.lower():
                    joke = pyjokes.get_joke()
                    print(joke)
                    engine.say(joke)
                    engine.say("I am as lame as my creator, sorry.")
                    engine.runAndWait()

                # Display current date
                elif "date" in data.lower():
                    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
                    print(f"Today's date is {current_date}")
                    engine.say(f"Today's date is {current_date}")
                    engine.runAndWait()

                # Display current time
                elif "time" in data.lower():
                    current_time = datetime.datetime.now().strftime("%I:%M %p")
                    print(f"Current time is {current_time}")
                    engine.say(f"Current time is {current_time}")
                    engine.runAndWait()

                # Play Music
                elif "play" in data.lower():
                    try:
                        song = data.lower().split(" ")[1]
                        print(f"Playing {song}......")
                        engine.say(f"Playing {song}......")
                        engine.runAndWait()

                        if song in music_lib.music:
                            link = music_lib.music[song]
                            webbrowser.open(link)
                        else:
                            print("Song not found in library.")
                            engine.say("Song not found in library.")
                            engine.runAndWait()
                

                    except IndexError:
                        print("Please specify a song name to play.")
                        engine.say("Please specify a song name to play.")
                        engine.runAndWait()
                #To stop jarvis
                elif "stop" in data.lower():
                    print("Stopping Jarvis...")
                    engine.say("Stopping Jarvis...")
                    engine.runAndWait()
                    break 

                if "google" in data.lower():
                    print(f"searching for {data}, please wait")
                    engine.say()
            else:
                print("Jarvis not activated.")

        except sr.WaitTimeoutError:
            print("Listening timed out. Please speak again.")
            
        except sr.UnknownValueError:
            print("Could not understand audio, please repeat.")
            
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

text()
root.mainloop()




# main.py

# import tkinter as tk
# from PIL import ImageTk, Image
# import webbrowser
# import pyttsx3
# import speech_recognition as sr
# import datetime
# import subprocess
# import pyjokes
# import music_lib  
# from face import FaceDisplay  # Import FaceDisplay from face.py
# from tkinter import *
# from PIL import Image,ImageTk

# class JarvisApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Jarvis")

#         # Initialize the FaceDisplay instance
#         self.face_display = FaceDisplay(root, r"C:\Users\TestUser\Desktop\JARVIS\photos\jarvis_face.png")

#         # Example: Displaying text
#         self.text_label = tk.Label(root, text="Hello, I'm Jarvis!", font=("Helvetica", 16))
#         self.text_label.pack()

#         # Start Button
#         self.start_button = tk.Button(root, text="Start Jarvis", command=self.start_jarvis)
#         self.start_button.pack()

#         # Speech Recognition Variables
#         self.recognizer = sr.Recognizer()
#         self.engine = pyttsx3.init()
#         self.activated = False

#     def start_jarvis(self):
#         self.engine.say("Initializing Jarvis")
#         self.engine.runAndWait()

#         while True:
#             with sr.Microphone() as source:
#                 print("Listening...")
#                 audio = self.recognizer.listen(source, timeout=2, phrase_time_limit=2)
                
#             try:
#                 print("Recognizing....")
#                 data = self.recognizer.recognize_google(audio)
#                 print(data)

#                 if "jarvis" in data.lower() and not self.activated:
#                     print("Jarvis activated")
#                     self.engine.say("Yes, how can I help you?")
#                     self.engine.runAndWait()
#                     self.activated = True  # Activate Jarvis

#                 if self.activated:

#                     if data.lower().startswith("google") or data.lower().startswith("search"):
#                         search_query = data.lower().split("search for", 1)[1].strip()
#                         print(f"Searching for {search_query}, Sir....") 
#                         self.engine.say(f"Searching for {search_query}, Sir....")
#                         self.engine.runAndWait()
#                         url = f"https://www.google.com/search?q={search_query}"
#                         webbrowser.open(url)

#                     if data.lower().startswith("play"):
#                         play_query = data.lower().split("play", 1)[1]
#                         print(f"Playing, {play_query}, Sir....")
#                         self.engine.say(f"Playing, {play_query}, Sir...")
#                         play_url = f"https://www.youtube.com/results?search_query={play_query}"
#                         webbrowser.open(play_url)

#                     # Greet
#                     elif "greet" in data.lower():
#                         current_time = datetime.datetime.now().time()
#                         if current_time < datetime.time(12, 0):
#                             print("Reacting to 'greet' command...")
#                             self.engine.say("Hello there! Good morning! I am Jarvis. Namaste and have a great day.")
#                         elif current_time < datetime.time(16, 0):
#                             print("Reacting to 'greet' command...")
#                             self.engine.say("Hello there! Good afternoon! I am Jarvis. Namaste and have a great day.")
#                         else:
#                             print("Reacting to 'greet' command...")
#                             self.engine.say("Hello there! Good evening! I am Jarvis. Namaste and have a great day.")
#                         self.engine.runAndWait()

#                     # Introduce Yourself
#                     elif "yourself" in data.lower():
#                         print("Introducing myself...")
#                         self.engine.say("Hi, myself Jarvis, created using Python. Currently in testing mode, soon will be 100 percent ready.")
#                         self.engine.runAndWait()

#                     # Open Notepad
#                     elif "notepad" in data.lower():
#                         print("Opening Notepad....")
#                         self.engine.say("Opening Notepad....")
#                         self.engine.runAndWait()
#                         subprocess.Popen(["notepad.exe"])

#                     # Jokes
#                     elif "joke" in data.lower():
#                         joke = pyjokes.get_joke()
#                         print(joke)
#                         self.engine.say(joke)
#                         self.engine.runAndWait()

#                     # Display current date
#                     elif "date" in data.lower():
#                         current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
#                         print(f"Today's date is {current_date}")
#                         self.engine.say(f"Today's date is {current_date}")
#                         self.engine.runAndWait()

#                     # Display current time
#                     elif "time" in data.lower():
#                         current_time = datetime.datetime.now().strftime("%I:%M %p")
#                         print(f"Current time is {current_time}")
#                         self.engine.say(f"Current time is {current_time}")
#                         self.engine.runAndWait()

#                     # Play Music
#                     elif "play" in data.lower():
#                         try:
#                             song = data.lower().split(" ")[1]
#                             print(f"Playing {song}...")
#                             self.engine.say(f"Playing {song}...")
#                             self.engine.runAndWait()

#                             if song in music_lib.music:
#                                 link = music_lib.music[song]
#                                 webbrowser.open(link)
#                             else:
#                                 print("Song not found in library.")
#                                 self.engine.say("Song not found in library.")
#                                 self.engine.runAndWait()

#                         except IndexError:
#                             print("Please specify a song name to play.")
#                             self.engine.say("Please specify a song name to play.")
#                             self.engine.runAndWait()

#                     # Stop Jarvis
#                     elif "stop" in data.lower():
#                         print("Stopping Jarvis...")
#                         self.engine.say("Stopping Jarvis...")
#                         self.engine.runAndWait()
#                         break 

#                     if "google" in data.lower():
#                         print(f"Searching for {data}, please wait")
#                         self.engine.say("Searching, please wait.")
#                         self.engine.runAndWait()

#             except sr.WaitTimeoutError:
#                 print("Listening timed out. Please speak again.")
                
#             except sr.UnknownValueError:
#                 print("Could not understand audio, please repeat.")
                
#             except sr.RequestError as e:
#                 print(f"Could not request results; {e}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = JarvisApp(root)
#     root.mainloop()
