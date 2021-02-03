import tkinter as tk

from tkinter import *
from PIL import ImageTk, Image


root = Tk()
# Code to add widget will go here……..
w = Label(root, width = '80', height = '40')
my_label1 = Label(root, text="Hello World").grid(row=0, column=0)
my_label2 = Label(root, text="My name is steve ").grid(row=1, column=3)

#w.pack()

#path = "c:\Users\Steve\Pictures\2019_12_14Difty\IMG_20191214_110454.jpg"
#img = ImageTk.PhotoImage(Image.open("True1.gif"))
#anel = tk.Label(root, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")


root.mainloop()

