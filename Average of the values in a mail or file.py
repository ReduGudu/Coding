n=input("Enter file name")
file=open(n)
total=0
d=0
i=0
for line in file:

    if line.startswith("X-DSPAM-Confidence:"):
        i = i + 1
        pos=line.find('0')
        d=float(line[pos:pos+6])
        total+=d
average=total/i
print("Average spam confidence:", round(average,15))