# # # import pyttsx3
# # # import speech_recognition as sr
# # # import datetime
# # # import pyjokes
   
# # # # Initialize the pyttsx3 engine
# # # engine = pyttsx3.init()

# # # # Get details of all available voices
# # # voices = engine.getProperty('voices')

# # # # Select a different voice (index 1 in this example)
# # # engine.setProperty('voice', voices[0].id)

# # # # Speak the text
# # # engine.say("Initializing Jarvis......")
# # # engine.runAndWait()
# # # engine.say("I'm listening Sir.......")
# # # engine.runAndWait()
# # # import speech_recognition as sr

# # # # Initialize recognizer class (for recognizing speech)
# # # recognizer = sr.Recognizer()

# # # # Function to recognize speech
# # # while True:
# # #     def recognize_speech():
# # #         with sr.Microphone() as source:
# # #             print("Listening...")

# # #             # Adjust for ambient noise
# # #             recognizer.adjust_for_ambient_noise(source)

# # #             # Capture the audio
# # #             audio = recognizer.listen(source)
            

# # #             try:
# # #                 print("Recognizing...")

# # #                 # Use Google Web Speech API to recognize the audio
# # #                 text = recognizer.recognize_google(audio)

# # #                 print(f"You said: {text}")
# # #                 engine.say(f"You said {text}")
# # #                 engine.runAndWait()

# # #                 if text.lower() == "stop":
# # #                     print("Stopping Jarvis...")
# # #                     engine.say("Stopping Jarvis...")
# # #                     engine.runAndWait()
# # #                     return False


# # #             except sr.UnknownValueError:
# # #                 print("Sorry, I could not understand what you said.")
# # #                 engine.say("Sorry, I could not understand what you said.")
# # #                 engine.runAndWait()

# # #             except sr.RequestError as e:
# # #                 print(f"Request error from Google Speech Recognition service; {e}")
                

# # #     # Call the function to start recognizing speech
# # #     recognize_speech()

# # # import pyttsx3
# # # import speech_recognition as sr
# # # import webbrowser
# # # import subprocess
# # # import pyjokes
# # # import datetime

# # # # Initialize the pyttsx3 engine
# # # engine = pyttsx3.init()

# # # # Get details of all available voices
# # # voices = engine.getProperty('voices')

# # # # Select a voice (adjust index as needed)
# # # engine.setProperty('voice', voices[0].id)

# # # # Speak the initialization message
# # # engine.say("Initializing Jarvis...")
# # # engine.say("Listening.....")
# # # engine.runAndWait()

# # # # Initialize recognizer class (for recognizing speech)
# # # recognizer = sr.Recognizer()

# # # # Function to recognize speech with a timeout of 2 seconds
# # # def recognize_speech():
# # #     with sr.Microphone() as source:
# # #         print("Listening...")

# # #         # Adjust for ambient noise
# # #         recognizer.adjust_for_ambient_noise(source)

# # #         try:
# # #             # Capture the audio with a timeout of 2 seconds
# # #             audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

# # #             print("Recognizing...")

# # #             # Use Google Web Speech API to recognize the audio
# # #             text = recognizer.recognize_google(audio)

# # #             print(f"You said: {text}")
# # #             engine.runAndWait()

# # #             # Check if the command is "STOP" to exit the loop
# # #             if "stop" in text.lower():
# # #                 print("Stopping Jarvis...")
# # #                 engine.say("Stopping Jarvis...")
# # #                 engine.runAndWait()
# # #                 return False  # Exit the function and stop listening
            

# # #             #Jarvis will respond to the wake word "JARVIS"
# # #             elif text.lower() == "jarvis":
# # #                 print("YAA")
# # #                 engine.say("ya")
# # #                 engine.runAndWait()


# # #             #Reacting to the word "Greet" and Jarvis will Greet the user
# # #             def time():
# # #                 time=datetime.datetime.now().time()
# # #                 if "greet" in text.lower():
# # #                     if time < datetime(0, 12):
# # #                         print("Reacting to 'greet' command...")
# # #                         engine.say("Hello there!, Good morning!, i am Jarvis, Namaastey.......... and......... have a great day")
# # #                         engine.runAndWait()
# # #                     elif time < datetime(12, 16):
# # #                         print("Reacting to 'greet' command...")
# # #                         engine.say("Hello there!, Good Afternoon!, i am Jarvis, Namaastey.......... and......... have a great day")
# # #                         engine.runAndWait()

# # #                     if time < datetime(16,24):
# # #                         print("Reacting to 'greet' command...")
# # #                         engine.say("Hello there!, Good evening!, i am Jarvis, Namaastey.......... and......... have a great day")
# # #                         engine.runAndWait()
                    
            
# # #             #Jarvis will introduce himself

# # #                 elif "yourself" in text.lower():
# # #                     print("Introducing myself......")
# # #                     engine.say("Hi, myself Jarvis, created using python......currently in testing mode.......soon will be 100 percent ready hahahhahahaha")
# # #                     engine.runAndWait()

# # #                 #Open Youtube
# # #                 elif "youtube" in text.lower():
# # #                     print("Opening Youtube....")
# # #                     engine.say("pening Youtube....")
# # #                     engine.runAndWait()
# # #                     webbrowser.open("https://www.youtube.com/")

# # #                 #Open Notepad
# # #                 elif "notepad" in text.lower():
# # #                     print("Opening Notepad....")
# # #                     engine.say("Opening Notepad....")
# # #                     engine.runAndWait()
# # #                     subprocess.Popen(["notepad.exe"])

                
# # #                 #Jokes
# # #                 elif "joke" in text.lower():
# # #                     joke=pyjokes.get_joke()
# # #                     print(joke)
# # #                     engine.say(joke)
# # #                     engine.say("I am as Lame as my creator, sorry")
# # #                     engine.runAndWait()

# # #             # %A: Full weekday name (e.g., Monday, Tuesday).
# # #             # %B: Full month name (e.g., January, February).
# # #             # %d: Day of the month as a zero-padded decimal number (e.g., 01, 02, ..., 31).
# # #             # %Y: Year with century as a decimal number (e.g., 2023, 2024).

# # #                 elif "date" in text.lower():
# # #                     current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
# # #                     print(f"Today's date is {current_date}")
# # #                     engine.say(f"Today's date is {current_date}")
# # #                     engine.runAndWait

# # #                 # %I: Hour (12-hour clock) 
# # #                 # %M: Minute 
# # #                 # %p: AM or PM 

# # #                 elif "time" in text.lower():
# # #                     engine.say(f"Current time is {time}, Thankyou")
# # #                     engine.runAndWait




# # #         #For Not showing to non detectable commands
# # #         except sr.UnknownValueError:
# # #             print("Sorry, I could not understand what you said.")
# # #             engine.say("Sorry, I could not understand what you said.")
# # #             engine.runAndWait()


# # #         #Not showing error to "WAIT_TIME_ERROR"
# # #         except sr.WaitTimeoutError:
# # #             print("Timeout: No speech detected within 5 seconds.")
# # #             # engine.say("Timeout: No speech detected within 5 seconds.")
# # #             engine.runAndWait()

# # #         except sr.RequestError as e:
# # #             print(f"Request error from Google Speech Recognition service; {e}")
# # #             engine.say(f"Request error from Google Speech Recognition service; {e}")
# # #             engine.runAndWait()

# # #         return True  # Continue listening

# # # # Main loop to continuously recognize speech
# # # while recognize_speech():
# # #     pass  # Continue listening until "STOP" command is received

# # # print("Exiting Jarvis...")


# import pyttsx3
# import speech_recognition as sr
# import webbrowser
# import subprocess
# import pyjokes
# import datetime
# import music_lib
# # engine = pyttsx3.init()
# # voices = engine.getProperty('voices')
# # engine.setProperty('voice', voices[0].id)
# # engine.say("Initializing Jarvis...")
# # engine.say("Listening.....")
# # engine.runAndWait()
# # recognizer = sr.Recognizer()
# # text=recognizer.recognize_google(audio)
# # activated=False

# # def recognize_speech():
# #         while True:
# #             with sr.Microphone() as source:
# #              # Adjust for ambient noise
# #                 recognizer.adjust_for_ambient_noise(source)

# #             try:
# #                 # Capture the audio with a timeout of 5 seconds
# #                 audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)

# #                 print("Recognizing...")
# #                 try:


# #                 if "hey jarvis" in text.lower() and not activated:
# #                     print("Activated Jarvis...")
# #                     engine.say("Yes, sir?")
# #                     engine.runAndWait()
# #                     activated = True
# #                  # Jarvis will respond to the wake word "JARVIS"
                
# #                 # Check if the command is "STOP" to exit the loop
# #                 if "stop" in text.lower():
# #                         print("Stopping Jarvis...")
# #                         engine.say("Stopping Jarvis...")
# #                         engine.runAndWait()
# #                         return False  # Exit the function and stop listening

# #                 if activated:
# #                 # Reacting to the word "Greet" and Jarvis will Greet the user
# #                     if "greet" in text.lower():
# #                         current_time = datetime.datetime.now().time()
# #                         if current_time < datetime.time(12, 0):
# #                             print("Reacting to 'greet' command...")
# #                             engine.say("Hello there! Good morning! I am Jarvis. Namaastey and have a great day.")
# #                         elif current_time < datetime.time(16, 0):
# #                             print("Reacting to 'greet' command...")
# #                             engine.say("Hello there! Good afternoon! I am Jarvis. Namaastey and have a great day.")
# #                         else:
# #                             print("Reacting to 'greet' command...")
# #                             engine.say("Hello there! Good evening! I am Jarvis. Namaastey and have a great day.")
# #                         engine.runAndWait()

# #                 # Jarvis will introduce himself
# #                     elif "yourself" in text.lower():
# #                         print("Introducing myself......")
# #                         engine.say("Hi, myself Jarvis, created using Python. Currently in testing mode, soon will be 100 percent ready. Haha hahaha.")
# #                         engine.runAndWait()

# #                 # Open Youtube
# #                     elif "youtube" in text.lower():
# #                         print("Opening Youtube....")
# #                         engine.say("Opening Youtube....")
# #                         engine.runAndWait()
# #                         webbrowser.open("https://www.youtube.com/")
                  
# #                 # Open Notepad
# #                     elif "notepad" in text.lower():
# #                         print("Opening Notepad....")
# #                         engine.say("Opening Notepad....")
# #                         engine.runAndWait()
# #                         subprocess.Popen(["notepad.exe"])

# #                 # Jokes
# #                     elif "joke" in text.lower():
# #                         joke = pyjokes.get_joke()
# #                         print(joke)
# #                         engine.say(joke)
# #                         engine.say("I am as lame as my creator, sorry.")
# #                         engine.runAndWait()

# #                 # Display current date
# #                     elif "date" in text.lower():
# #                         current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
# #                         print(f"Today's date is {current_date}")
# #                         engine.say(f"Today's date is {current_date}")
# #                         engine.runAndWait()

# #                 # Display current time
# #                     elif "time" in text.lower():
# #                         current_time = datetime.datetime.now().strftime("%I:%M %p")
# #                         print(f"Current time is {current_time}")
# #                         engine.say(f"Current time is {current_time}")
# #                         engine.runAndWait()

# #                 #Play Music
# #                 # if "justin" in text.lower():
# #                 #     print("Playing.....")
# #                 #     engine.say("Playing.....")
# #                 #     engine.runAndWait()
# #                 #     webbrowser.open("https://youtu.be/euCqAq6BRa4?si=jMun6xJNSQfNzC7T")

# #                     elif "play" in text.lower():
# #                         try:
# #                             song=text.lower().split(" ")[1]
# #                             print(f"Playing {song}......")
# #                             engine.say("song")
# #                             if song in music_lib.music:
# #                                 link=music_lib.music[song]
# #                                 webbrowser.open(link)
# #                             else:
# #                                 print("Please repeat the song name sir")
# #                                 engine.say("Please repeat the song name sir")
# #                         except KeyError:
# #                             print("Please specify a song name to play.")
# #                             engine.say("Please specify a song name to play.")
# #                             engine.runAndWait()  # Ensure the message is spoken immediately
# #             # except sr.KeyError:
# #             #     print("Please repeat the song name sir")
# #             #     engine.runAndWait()


                
# #           #Handle unrecognized speech
# #                     except sr.UnknownValueError:
# #                     print("Sorry, I could not understand what you said.")
# #                     # engine.say("Sorry, I could not understand what you said.")
# #                     engine.runAndWait()

# #          # Handle timeout during listening
# #             except sr.WaitTimeoutError:
# #                 print("Timeout: No speech detected within 5 seconds.")
# #                 # engine.say("Timeout: No speech detected within 5 seconds.")
# #                 engine.runAndWait()

# #         # Handle errors from Google Speech Recognition service
# #             except sr.RequestError as e:
# #                 print(f"Request error from Google Speech Recognition service; {e}")
# #                 engine.say(f"Request error from Google Speech Recognition service; {e}")
# #                 engine.runAndWait()

# # # Main loop to continuously recognize speech
# # while recognize_speech():
# #     pass  # Continue listening until "STOP" command is received

# # print("Exiting Jarvis...")



import tkinter as tk
from PIL import ImageTk, Image
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import subprocess
import pyjokes
import music_lib
import threading

engine = pyttsx3.init()

# GUI Setup
root = tk.Tk()
root.geometry("250x250")
root.minsize(100, 100)
root.title("Jarvis...")

# Frame and Labels
frame1 = tk.Frame(root, background="black")
frame1.pack(side="bottom")

title_label = tk.Label(frame1, text="Hello, I'm Jarvis...", padx=10, pady=0, anchor="sw", font="15", background="black", foreground="white")
title_label.pack(side="left")

def hello():
    print("Initializing Jarvis....")
    engine.say("Initializing Jarvis....")
    engine.runAndWait()
    threading.Thread(target=text, daemon=True).start()

B1 = tk.Button(frame1, text="Initialize now...", command=hello, padx=10, pady=0, background="black", foreground="white", borderwidth=1)
B1.pack(anchor="ne", side="right")

# Image
image_path = r"C:/Users/TestUser/Desktop/JARVIS/photos/jarvis_face.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(image=photo, background="black")
image_label.pack(fill="x", padx=0, pady=0, side="top")

name = tk.Label(text="BASIC CALCULATOR")
name.pack()

def text():
    recognizer = sr.Recognizer()
    activated = False
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                # recognizer.adjust_for_ambient_noise(source, duration=5)
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                
                print("Recognizing...")
                data = recognizer.recognize_google(audio)
                print(data)
            
            if "jarvis" in data.lower() and not activated:
                print("Jarvis activated")
                engine.say("Yes")
                engine.runAndWait()
                activated = True  # Activate Jarvis

            if activated:
                with sr.Microphone() as source:
                    print("Listening for command...")
                    recognizer.adjust_for_ambient_noise(source, duration=5)
                    audio = recognizer.listen(source, timeout=4, phrase_time_limit=3)

                    try:
                        data = recognizer.recognize_google(audio)
                        print(data)
                        
                        if "google" in data.lower() or "search" in data.lower():
                            if "search for" in data.lower():
                                search_query = data.lower().split("search for", 1)[1].strip()
                                print(f"Searching for {search_query}, Sir....")
                                engine.say(f"Searching for {search_query}, Sir....")
                                engine.runAndWait()
                                url = f"https://www.google.com/search?q={search_query}"
                                webbrowser.open(url)
                            else:
                                print("No search query provided.")
                                engine.say("Please specify what to search for.")
                                engine.runAndWait()
                        
                        elif "play" in data.lower():
                            if "play" in data.lower():
                                play_query = data.lower().split("play", 1)[1].strip()
                                print(f"Playing, {play_query}, Sir....")
                                engine.say(f"Playing, {play_query}, Sir...")
                                play_url = f"https://www.youtube.com/results?search_query={play_query}"
                                webbrowser.open(play_url)
                        
                        # Add other commands here...

                    except sr.UnknownValueError:
                        print("Could not understand audio, please repeat.")
                    except sr.RequestError as e:
                        print(f"Could not request results; {e}")

        except sr.WaitTimeoutError:
            print("Listening timed out. Please speak again.")
            
        except sr.UnknownValueError:
            print("Could not understand audio, please repeat.")
            
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

root.mainloop()
