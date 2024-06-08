fname=input("Enter a file name")
file=open(fname)
text=file.read()
mylist=list()
w=text.split()
for i in w:
    if i not in mylist:
        mylist.append(i)

mylist.sort()
print(mylist, "and", len(w))
