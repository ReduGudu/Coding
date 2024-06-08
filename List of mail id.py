n=input("Enter the name and type of the file:")
file=open(n)
count=0
for line in file:
    if line.startswith("From:"):
        w=line.split()


        print(w[1])
        count=count+1
print("There were",count, "lines in the file with From as the first word")