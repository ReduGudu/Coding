import os
import urllib.request,urllib.parse,urllib.error
import json

skey=os.environ.get('API_KEY')

key=input("Enter the key")
if key==skey:
    s_url='http://py4e-data.dr-chuck.net/json?'
else:
    s_url='https://maps.googleapis.com/maps/api/geocode/json?'
    quit()
parms=dict()
parms['key']=42
address=input("Enter a location address:")
parms['address']=address

html= s_url+urllib.parse.urlencode(parms)

url=urllib.request.urlopen(html).read()

uh=url.decode()


jfile=json.loads(uh)
print(uh)




