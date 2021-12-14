from tkinter import *
import random

root=Tk()
root.geometry("400x400")
root.title("Allison's Dice Roll Simulator")
root.configure(bg='LightBlue3')
root.attributes('-alpha', 0.9)

label1 = Label(root,font=("Helvetica",260))

def dice_roll():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label1.config(text=f'{random.choice(dice)}{random.choice(dice)}')
    label1.pack()
    label1.configure(bg='LightBlue3')

button = Button(root, text="CLICK TO ROLL THE DICE!", font = 'Helvetica 15 underline bold', foreground='black', command=dice_roll, height=2, width=25)
button.pack(side=TOP)

def close():
    root.destroy()

button1 = Button(root, text="EXIT", foreground = 'black', command=close, font = 'Helvetica 15 bold', height=2, width=5)
button1.pack(side=BOTTOM)



root.mainloop()


