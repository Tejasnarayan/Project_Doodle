import json
import requests

for j in range(2000,2001):
    for i in range(1,2):
        url = ("".join(["https://www.google.com/doodles/json/",str(j),"/",str(i),"?hl=en"]))
        link = requests.get(url)
        json_string = link.json()
        
        
        for x in json_string:
            keys = x.keys()
            print(keys)
            values = x.values()
            print(values)
