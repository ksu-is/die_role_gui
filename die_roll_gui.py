from tkinter import *
import random
import tkinter

root = Tk()
root.geometry("400x400")
root.title("Allison's Dice Roll Simulator")

dice = ['dieone.jpg', 'dietwo.jpg', 'diethree.jpg', 'diefour.jpg', 'diefive.jpg', 'diesix.jpg']
image1 = PhotoImage(Image.open(random.choice(dice)))
image2 = PhotoImage(Image.open(random.choice(dice)))

label1 = tkinter.Label(root, image=image1)
label2 = tkinter.Label(root, image=image2)

label1.image = image1
label2.image = image2
label1.pack(side=tkinter.LEFT)
label2.pack(side=tkinter.RIGHT)

def roll():
    image1 = PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1
    image2  = PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image = image2

b1 = Button(root,text="Roll the Dice!",foreground='blue',command=roll)
b1.place(x=300,y=0)
b1.pack()

root.mainloop()