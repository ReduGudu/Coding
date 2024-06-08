import tkinter
tk=list(dir(tkinter))
count=0
for w in tk:
    count=count+1
    print(count,".",w)
