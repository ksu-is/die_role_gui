from tkinter import *
import random

root=Tk()
root.geometry("400x400")
root.title("Allison's Dice Roll Simulator")
root.configure(bg='gray77')
root.attributes('-alpha', 0.9)

label1 = Label(root,font=("Helvetica",260))

def dice_roll():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label1.config(text=f'{random.choice(dice)}{random.choice(dice)}')
    label1.pack()
    label1.configure(bg='gray77')

button = Button(root, text="Click to Roll the Dice!", font = 'Helvetica 15 underline' , bg='light blue', foreground='black',command=dice_roll, height=3, width=15)
button.pack(side=TOP)


button1 = Button(root, text="Exit", foreground = 'black', command=root.destroy, height=2, width=4)
button1.pack(side=BOTTOM)



root.mainloop()


