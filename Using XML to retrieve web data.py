import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
link=input("Enter the website name:")
html=urllib.request.urlopen(link).read()

for w in html:
    tree=ET.fromstring(html)
    lst=tree.findall("comments/comment")
sum=0
for m in lst:
    gg=int(m.find("count").text)
    sum=sum+gg
    print("Retried number:", gg, "\nApparent Sum:", sum,"\n")
print("---------------------------------------------")
print("Total:", sum)