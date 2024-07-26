# face.py

import tkinter as tk
from PIL import ImageTk, Image

class FaceDisplay:
    def __init__(self, root, image_path):
        self.root = root
        self.image_path = image_path

        self.face_image = ImageTk.PhotoImage(Image.open(r"C:\Users\TestUser\Desktop\JARVIS\photos\jarvis_face.png"))
        self.face_label = tk.Label(root, image=self.face_image)
        self.face_label.pack()

    def update_image(self, new_image_path):
        self.image_path = new_image_path
        self.face_image = ImageTk.PhotoImage(Image.open(r"C:\Users\TestUser\Desktop\JARVIS\photos\jarvis_face.png"))
        self.face_label.configure(image=self.face_image)




# from tkinter import *
# from PIL import Image,ImageTk

# root = Tk()
# def hello():
#     print("Initialzing Jarvis....")

# root.geometry("250x250")
# root.minsize(100, 100)
# root.title("Jarvis...")


# frame1=Frame(root, background="black")
# frame1.pack(side="bottom")

# title_lable=Label(frame1,text="Hello, I'm Jarvis...", padx=10, pady=0, anchor="sw", font="15", background="black", foreground="white")
# title_lable.pack(side="left")


# B1=Button(frame1, text="Initialize now...", command=hello , padx=10,pady=0,background="black", foreground="white", borderwidth=1)
# B1.pack(anchor="ne", side="right")


# #Image 
# image_path = (r"C:/Users/TestUser/Desktop/JARVIS/photos/jarvis_face.png")
# image = Image.open(image_path)
# photo=ImageTk.PhotoImage(image)
# image_lable=Label(image=photo, background="black")
# image_lable.pack(fill="x", padx=0, pady=0, side="top")
# name=Label(text="BASIC CALCULATOR")
# name.pack()


# root.mainloop()
















