from tkinter import *
root=Tk()
root.title("Calculator")

e=Entry(root, text="what do you want to calculate today?", fg="black",bg="silver", borderwidth=10, width=40)
e.grid(row=0, column=0, columnspan=4)

#Button functions

def digit(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(number))

def buttonclear():
    e.delete(0,END)

def buttonadd():
    first_number = e.get()
    global fnum
    global math
    fnum = int(first_number)
    math="addition"
    e.delete(0,END)


def button_equal():
    if math=='addition':
        second_number=e.get()
        e.delete(0,END)
        e.insert(0, fnum + int(second_number))


    elif math=='subtract':
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, fnum - int(second_number))

    elif math=='multiply':
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, fnum * int(second_number))

    elif math=='divide':
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, fnum / int(second_number))
def button_subtract():
    first_number = e.get()
    global fnum
    global math
    fnum = int(first_number)
    math = "subtract"
    e.delete(0, END)

    return

def button_divide():
    first_number = e.get()
    global fnum
    global math
    fnum = int(first_number)
    math = "divide"
    e.delete(0, END)
    return

def button_multiply():
    first_number = e.get()
    global fnum
    global math
    fnum = int(first_number)
    math = "multiply"
    e.delete(0, END)
    return



#Button description
button_1=Button(root, text= "1",padx=35,pady=20, borderwidth=5,bg="sky blue",command=lambda:digit(1))
button_2=Button(root, text= "2",padx=35,pady=20, borderwidth=5,bg="sky blue",command=lambda:digit(2))
button_3=Button(root, text= "3",padx=35,pady=20, borderwidth=5,bg="sky blue",command=lambda:digit(3))
button_4=Button(root, text= "4",padx=35,pady=20, borderwidth=5,bg="sky blue",command=lambda:digit(4))
button_5=Button(root, text= "5",padx=35,pady=20, borderwidth=5,bg="sky blue",command=lambda:digit(5))
button_6=Button(root, text= "6",padx=35,pady=20, borderwidth=5,bg="sky blue",command=lambda:digit(6))
button_7=Button(root, text= "7",padx=35,pady=20, borderwidth=5,bg="sky blue",command=lambda:digit(7))
button_8=Button(root, text= "8",padx=35,pady=20, borderwidth=5,bg="sky blue",command=lambda:digit(8))
button_9=Button(root, text= "9",padx=35,pady=20, borderwidth=5,bg="sky blue",command=lambda:digit(9))
button_0=Button(root, text= "0",padx=80,pady=30, borderwidth=5,bg="sky blue",command=lambda:digit(0))
button_plus=Button(root, text= "+",padx=35,pady=30, borderwidth=5,bg="grey",command=buttonadd)
button_equal=Button(root, text= "=",padx=126,pady=30,borderwidth=5,bg="sky blue",command=button_equal)
button_clear=Button(root, text= "clr",padx=35,pady=20,borderwidth=5,bg="crimson",fg="silver",command=buttonclear)
button_divide=Button(root, text= "/",padx=40,pady=20,borderwidth=5,bg="grey",command=button_divide)
button_multiply=Button(root, text= "x",padx=40,pady=75,borderwidth=5,bg="grey",command=button_multiply)
button_subtract=Button(root, text= "-",padx=40,pady=20,borderwidth=5,bg="grey",command=button_subtract)

#Button Position
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0, columnspan=2)
button_plus.grid(row=4, column=2)
button_equal.grid(row=5, column=0, columnspan=3)
button_clear.grid(row=1,column=3)

button_divide.grid(row=2,column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=4, column=3, rowspan=2)
root.mainloop()


#Everytime we crete a button, we need to specify the button location and the funtion almost immediately to avoid forgetting about them later
