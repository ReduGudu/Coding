import json
import urllib.parse,urllib.request,urllib.error
link=(input("Enter the link:"))

html=urllib.request.urlopen(link).read()

jlink=json.loads(html)

print(jlink,"\n")

i=0
count=0
for w in jlink["comments"]:
    count=count+1
    print(count,w)

counts=0
sum=0
print("========================================================================================")
print("                         SUM OF THE COMMENT COUNTS OF THE NAMES ")
print("========================================================================================")
for i in range(len(jlink["comments"])):
    counts=counts+1

    m=jlink["comments"][i]["count"]
    s=jlink["comments"][i]["name"]
    sum=sum+m
    print(counts,".","The retrieved count for",s,"is:", m,"\nThe apparent sum is", sum)
    i=i+1

print("----------------------------------------------------------------------------------")
print("The sum total is:", sum)