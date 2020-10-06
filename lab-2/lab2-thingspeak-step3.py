import urllib.request
import requests
import threading
import json

import random

""" https://api.thingspeak.com/channels/1163307/fields
    /1.json?api_key=8D9B5YGAOXY43433&results=2
"""

def read_data_thingspeak():
 
    URL='https://api.thingspeak.com/channels/1163307/fields/1.json?api_key='
    KEY='8D9B5YGAOXY43433'
    HEADER='&results=2'
    NEW_URL=URL+KEY+HEADER
    print(NEW_URL)

    get_data=requests.get(NEW_URL).json()
    #print(get_data)
    channel_id=get_data['channel']['id']

    feild_1=get_data['feeds']
    #print(feild_1)

    t=[]
    for x in feild_1:
        print(x['field1'])
        t.append(x['field1'])

if __name__ == '__main__':
    #thingspeak_post()
    read_data_thingspeak()
