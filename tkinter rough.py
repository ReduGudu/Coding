from tkinter import *
from math import sqrt

root=Tk()
root.title="Calculator"
root.iconbitmap('Dtafalonso-Android-Lollipop-Calculator.ico')
e=Entry(root,bg='grey',fg='black', width=50)
e.grid(row=0, column=0, columnspan=4)

#3.Button Function:
def digit(number):
    current=e.get()
    e.delete(0,END)

    e.insert(0, str(current)+str(number))

def cleardata():
    e.delete(0,END)

def button_equal():
    if math=="addition":
        second_number=e.get()
        e.delete(0,END)
        e.insert(0, fnum+int(second_number))
        global total
        total=fnum+ int(second_number)


    if math=="subtraction":
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, fnum - int(second_number))
        global difference
        difference=fnum-int(second_number)
        e.delete(0, END)


    if math=="multiply":
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, fnum * int(second_number))
        global product
        product=fnum*int(second_number)
        e.delete(0, END)

    if  math=="division":
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, fnum / int(second_number))
        global divide_result
        divide_result=fnum / int(second_number)
        e.delete(0, END)

    if math=="sqroot":
        second_number = e.get()
        e.delete(0, END)
        e.insert(0, sqrt(fnum))
        global rooted 
        rooted=sqrt(fnum)
        e.delete(0, END)

def addition():
    first_number=e.get()
    global fnum
    global math
    math='addition'
    fnum=int(first_number)
    e.delete(0,END)

def subtraction():
    first_number=e.get()
    global fnum
    global math
    math='subtraction'
    fnum=int(first_number)
    e.delete(0,END)

def multiply():
    first_number = e.get()
    global fnum
    global math
    math = 'multiply'
    fnum = int(first_number)
    e.delete(0, END)


def division():
    first_number = e.get()
    global fnum
    global math
    math = 'division'
    fnum = int(first_number)
    e.delete(0, END)


def sqroot():
    first_number = e.get()
    global fnum
    global math
    math = 'sqroot'
    fnum = int(first_number)
    e.delete(0, END)

def Ans():
    if math=='addition':
        Answer=total
    if math=='subtraction':
        Answer=difference
    if math=='multiply':
        Answer=product
    if math=='division':
        Answer=divide_result
    if math=="sqroot":
        Answer=rooted


#1.Button Discription"
button1=Button(root,text=1, bg="sky blue", fg="white", padx=30 , pady=20, command=lambda:digit(1))
button2=Button(root,text=2, bg="sky blue", fg="white", padx=30 , pady=20, command=lambda:digit(2))
button3=Button(root,text=3, bg="sky blue", fg="white", padx=30 , pady=20, command=lambda:digit(3))
button4=Button(root,text=4, bg="sky blue", fg="white", padx=30 , pady=20, command=lambda:digit(4))
button5=Button(root,text=5, bg="sky blue", fg="white", padx=30 , pady=20, command=lambda:digit(5))
button6=Button(root,text=6, bg="sky blue", fg="white", padx=30 , pady=20, command=lambda:digit(6))
button7=Button(root,text=7, bg="sky blue", fg="white", padx=30 , pady=20, command=lambda:digit(7))
button8=Button(root,text=8, bg="sky blue", fg="white", padx=30 , pady=20, command=lambda:digit(8))
button9=Button(root,text=9, bg="sky blue", fg="white", padx=30 , pady=20, command=lambda:digit(9))
button0=Button(root,text=0, bg="sky blue", fg="white", padx=30 , pady=20, command=lambda:digit(0))



button_clr=Button(root,text="clr", bg="red", fg="white", padx=26 , pady=20, command=cleardata)
button_equal=Button(root, text="=", bg='light green', fg='white', padx=66.5,pady=20, command=button_equal)


button_add=Button(root,text="+", bg="silver", fg="black", padx=34, pady=20, command=addition)
button_subtract=Button(root,text="-", bg="silver", fg="black", padx=35, pady=20, command=subtraction)
button_multiply=Button(root,text="x", bg="silver", fg="black", padx=35, pady=20, command=multiply)
button_divide=Button(root,text="/", bg="silver", fg="black", padx=35, pady=20, command=division)
button_root=Button(root,text="√", bg="silver", fg="black", padx=29, pady=20, command=sqroot)

button_Ans=Button(root,text="Ans", bg="silver", fg="black", padx=27, pady=20, command=Ans)

#2.Button Position:
button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button0.grid(row=5, column=0)



button_clr.grid(row=1, column=0)
button_equal.grid(row=5, column=1,columnspan=2)


button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_divide.grid(row=3, column=3)
button_multiply.grid(row=4, column=3)
button_Ans.grid(row=5, column=3)
button_root.grid(row=1, column=2)






root.mainloop()
