
# import tkinter library to create GUI
from tkinter import *

# import random library to randomly select numbers for the die
import random
<<<<<<< Updated upstream
=======
import tkinter
from PIL import Image, ImageTk
>>>>>>> Stashed changes

# tkinter root window is created
root = Tk()
# sets size for the window and positions it on the screen (parameters (width x height))
root.geometry("400x400")

# creation of dice label
l1 = Label(root,font=("Helvetica",260))

# function to create dice roll simulation
def roll():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(dice)}{random.choice(dice)}')
    l1.pack()

# creation of button that will trigger dice rolling and say 'Roll the Dice!'
b1 = Button(root,text="Roll the Dice!",foreground='blue',command=roll)
b1.place(x=300,y=0)
b1.pack()

# terminated when close button clicked in titlebar
root.mainloop()