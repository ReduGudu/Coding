import re
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

html=urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_765206.html").read()
sac= BeautifulSoup(html, "html.parser")

tags=sac("scan")
smash=str(tags)
print(tags)
y=re.findall('[0-9]+',smash)
count=0
sum=0


for w in y:
    T=int(w)
    sum=sum+T
    print(T,"\n","present sum is",sum)

print("---------------------------------------------------------------------------------\nThe Final Sum is:",sum)




























