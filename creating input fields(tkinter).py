from tkinter import *
root=Tk()
search=Entry(root,text="Enter what you name",width=40,fg="black", bg="light blue")
search.insert(0,"Your name please")
search.pack()

def comment():
    mylabel=Label(root,text= "Hello " + search.get(), fg="white",bg="crimson")
    mylabel.pack()

button=Button(root,text="Click me or die!", command=comment)
button.pack()
root.mainloop()
#The Entry() is an input field
# the insert() displays a default message in the input field
