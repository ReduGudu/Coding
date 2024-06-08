import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

link=input("Enter URL:")

list=list()
x=int(input("Enter count:"))
Z=int(input("Enter position:"))

for i in range(0,x):
    html=urllib.request.urlopen(link).read()
    ggwp=BeautifulSoup(html,'html.parser')
    tag=ggwp('a')
    link=tag[Z-1].get("href")
    list.append(link)

for w in list:
    print("Retrieving.........", w)

