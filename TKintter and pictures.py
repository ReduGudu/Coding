from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.iconbitmap('D:logo_8dx_icon.ico')

picture=ImageTk.PhotoImage(Image.open("Screenshot (20200823-231208).jpg"))
piclabel=Label(image=picture)

piclabel.pack()
root.mainloop()

#If the picture is in the same directory as the python program, then the path of the image is not necessary(as seen in line 6)
#The main library of the output window is TKinter. So, we have to register the image into the root via TKinter as seen in line 7( we can also create a picture button)