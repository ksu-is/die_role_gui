from tkinter import *
import random
import tkinter

root=Tk()
root.geometry("400x400")
root.title("Allison's Dice Roll Simulator")
root.configure(bg='gray77')

label1 = Label(root,font=("Helvetica",260))

def dice_roll():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label1.config(text=f'{random.choice(dice)}{random.choice(dice)}')
    label1.pack()
    label1.configure(bg='gray77')

button = Button(root, text="Click to Roll the Dice!", foreground='green',command=dice_roll)
button.place(x=300,y=0)
button.pack()

root.mainloop()


