from tkinter import *

root= Tk()
mylabel1=Label(root, text="Hello", fg="Brown")
mylabel2=Label(root, text= "Hi", fg="Purple")
mylabel3=Label(root, text= "Bye", fg="Orange")
mylabel4=Label(root, text= "Bye", fg="blue")

mylabel1.grid(row=0, column=1)
mylabel2.grid(row=0, column=2)
mylabel3.grid(row=0, column=5)
mylabel4.grid(row=1, column=2)

root.mainloop()

#the grid() function lets us specify the position of the label
#the position of the label are relative to the positions of the othe labels(see the position of mylabel3)
# fg is the front color of the text....bg is the background colour of the text
#if we had use pack() insted of grid(), we couldn't have selected the position of the label