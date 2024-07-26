import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import subprocess
import pyjokes
from googlesearch import search
from tkinter import *
from PIL import Image, ImageTk
import threading
import pywhatkit as kit
API_KEY = "AIzaSyDjDpHyYG8C-DqSRFd3cMTMaR9JER5fKfI"
engine = pyttsx3.init()

# GUI
root = Tk()
root.geometry("500x500")
root.minsize(250, 250)
root.title("Jarvis...")

# FRAME FOR TEXT AND BUTTON
frame1 = Frame(root)
frame1.pack(side="bottom")

title_label = Label(frame1, text="H e l l o,   I'm   J a r v i s...", padx=0, pady=5, anchor="sw", font=("Arial", 15, "bold"), borderwidth="2")
title_label.pack(side="top", anchor="center", fill="x")

def hello():
    print("Initializing Jarvis....")
    engine.say("Initializing Jarvis....")
    engine.runAndWait()
    threading.Thread(target=text, daemon=True).start()

def play_youtube_videos(play_query):
    try:
        kit.playonyt(play_query)
        print(f"Playing {play_query}, Sir")
        engine.say(f"Playing {play_query}, Sir")
        engine.runAndWait()
    except Exception as e:
        print("Try again Sir")

B1 = Button(frame1, text="Initialize now...", command=hello, padx=0, pady=0, borderwidth="1", font="15")
B1.pack(anchor="center", side="bottom")

# Image
image_path = r"C:/Users/TestUser/Desktop/JARVIS/photos/jarvis_lol.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
image_label = Label(image=photo, background="black")
image_label.pack(fill="x", padx=0, pady=0, side="top")

name = Label()
name.pack()

def text():
    recognizer = sr.Recognizer()
    activated = False

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                print("Recognizing....")
                data = recognizer.recognize_google(audio)
                print(data)

                if "hey jarvis" in data.lower() and not activated:
                    print("Jarvis activated")
                    engine.say("Jarvis activated Sir...")
                    engine.runAndWait()
                    activated = True  # Activate Jarvis

                if activated:
                    if "jarvis" in data.lower():
                        data = data.lower().replace("jarvis", "").strip()

                    if data.lower().startswith("google") or data.lower().startswith("search for"):
                        search_query = data.lower().split("search for", 1)[1].strip()
                        print(f"Searching for {search_query}, Sir....")
                        engine.say(f"Searching for {search_query}, Sir....")
                        engine.runAndWait()
                        url = f"https://www.google.com/search?q={search_query}"
                        webbrowser.open(url)

                    elif data.lower().startswith("play"):
                        play_query = data.lower().split("play", 1)[1].strip()
                        play_youtube_videos(play_query)

                    elif "open youtube" in data.lower():
                        print("Opening Youtube...")
                        engine.say("Opening Youtube....")
                        engine.runAndWait()
                        webbrowser.open("https://www.youtube.com/")

                    elif "jarvis greet" in data.lower():
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

                    elif "oye jarvis" in data.lower():
                        print("yes")
                        engine.say("ya")
                        engine.runAndWait()

                    elif "yourself" in data.lower():
                        print("Introducing myself......")
                        engine.say("Hello, I’m Jarvis, your Python-based smart assistant currently in testing mode. Created with Python and a Tkinter GUI, I'm here to make your life easier by handling tasks like web searches, playing music, and more. Just tell me what you need")
                        engine.runAndWait()

                    elif "notepad" in data.lower():
                        print("Opening Notepad....")
                        engine.say("Opening Notepad....")
                        engine.runAndWait()
                        subprocess.Popen(["notepad.exe"])

                    elif "joke" in data.lower():
                        joke = pyjokes.get_joke()
                        print(joke)
                        engine.say(joke)
                        engine.say("I am as lame as my creator, sorry.")
                        engine.runAndWait()

                    elif "date" in data.lower():
                        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
                        print(f"Today's date is {current_date}")
                        engine.say(f"Today's date is {current_date}")
                        engine.runAndWait()

                    elif "time" in data.lower():
                        current_time = datetime.datetime.now().strftime("%I:%M %p")
                        print(f"Current time is {current_time}")
                        engine.say(f"Current time is {current_time}")
                        engine.runAndWait()

                    elif "sing a song" in data.lower():
                        print("trying...")
                        engine.say("Let me give a try sir...")
                        engine.runAndWait()
                        engine.say("Comming over.........in my direction....so thankful for that...... such a blessing yeeh,,, turn every situation in a heaven yeh,......despacito")
                        engine.runAndWait()
                    elif "stop" in data.lower():
                        print("Stopping Jarvis sir....")
                        engine.say("Stopping Jarvis sir....")
                        engine.runAndWait()
                        break

        except sr.WaitTimeoutError:
            print("Listening timed out. Please speak again.")
            
        except sr.UnknownValueError:
            print("Could not understand audio, please repeat.")
            
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

        # except sr.IndexError as e:
        #     print("Please repeat the command, sir")
        
        except IndexError:
            print("Please repeat the command, sir.")
        
        except RuntimeError:
            print("Please repeat the command, sir.")
        

root.mainloop()
text()
# import pywhatkit as kit

# def play_youtube_video(query):
#     try:
#         kit.playonyt(query)
#         print(f"Playing {query}...")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# query = "Despacito"
# play_youtube_video(query)
