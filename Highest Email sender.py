w=dict()
lst=list()
n=input("Enter a file:")
file=open(n)

for line in file:
    if line.startswith("From:"):
        lines=line
        word=line.split()
        lst.append(word[1])



count=0
for word in lst :
    count=count+1
    w[word]=w.get(word,0)+1



bigcount=None
bigsender=None
for word,count in w.items():
    if bigcount is None or count>bigcount:
        bigcount=count
        bigsender=word

print(bigsender,bigcount)