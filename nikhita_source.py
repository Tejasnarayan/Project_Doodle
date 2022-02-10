import pandas as pd
import requests 
import json

#URL = "https://www.google.com/doodles"
URL = "https://www.google.com/doodles/json/1999/10?h1=en"
data =  requests.get(URL) 

word = data.json()
table1 = pd.DataFrame(word) 


for j in range(2000,2022):
    for i in range(1,13):
        url = ("".join(["https://www.google.com/doodles/json/",str(j),"/",str(i),"?hl=en"]))
        link = requests.get(url)
        words = link.json()
        table2 = pd.DataFrame(words)
        #print(table2)

        table1 = pd.concat([table1,table2])
print(table1)
table1.to_csv('table1.csv')
