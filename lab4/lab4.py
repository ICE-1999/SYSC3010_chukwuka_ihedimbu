import requests
import urllib.request
import json


URL='https://api.thingspeak.com/update?api_key='
KEY='7481QW0APO2BO2BU'
HEADER='&field1={L1-F-4}&field2={d}&field3{chukwukaemmanuelihed@cmail.carleton.ca}'
NEW_URL=URL+KEY+HEADER
print(NEW_URL)

data = urllib.request.urlopen(NEW_URL)
print(data)
