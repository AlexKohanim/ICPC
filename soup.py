#!/usr/bin/env python3
from bs4 import *
import urllib3
import json
http = urllib3.PoolManager()

url = 'https://www.reddit.com/r/earthporn/.json?limit=100'
response = http.request('GET', url)
#print(response.data)
#soup = BeautifulSoup(response.data, features="JSON")
newDictionary=json.loads(response.data)
for img in newDictionary['data']['children']:
    print(img['data']['url'])

