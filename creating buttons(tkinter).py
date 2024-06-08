from tkinter import *
def clicked():
    label=Label(root, text="Contratutions! you have clicked a button")
    label.pack()
root= Tk()
button=Button(root, text="Click me or die!", command=clicked, fg="white", bg="crimson")
button.pack()
root.mainloop()

#when entering the command function of the button, we shouldn't use ().
#padx and pady can be used in the button function to specify the size of the button
"""Introduce a type in the button funtion called "state". This type tells us if the button is disabled or enabled. 
That means, if state=DISABLED, then the button won't work"""
