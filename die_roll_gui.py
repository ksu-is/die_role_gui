from tkinter import *
import random
import tkinter
from PIL import Image, ImageTk, ImageSequence
import time

root = Tk()
root.geometry("400x400")
root.title("Allison's Dice Roll Simulator")

dilist = ['dieone.jpg', 'dietwo.jpg', 'diethree.jpg', 'diefour.jpg', 'diefive.jpg', 'diesix.jpg']
diopen = ImageTk.PhotoImage(Image.open('dieone.jpg'))
label = Label(root)
label.pack()

def dice_roll():
    path = random.choice(dilist)
    imag = ImageTk.PhotoImage(Image.open(path))
    label.place(x=150, y=300)
    label.configure(image=imag)
    label.image = imag
    time.sleep(0.03)

Button(root,text="Click to roll the die!", height=5, width=10, bg='green', command=dice_roll).place(x=400, y=300)
root.mainloop()
