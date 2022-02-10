from unicodedata import name
import pandas as pd
import requests 
import json

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
df = pd.DataFrame(table1)
cols = ['name', 'alternate_url', 'high_res_url', 'high_res_width', 'high_res_height','translations', 'translated_blog_posts', 'query', 'share_text']
df1 = df.drop(cols, axis=1)
df1["url"] = df1["url"].apply(lambda x:x.lstrip("//"))
df1["run_date_array"] = df1["run_date_array"].apply(lambda x:'-'.join([str(i).zfill(2) for i in x][3::-1]))
print(df1)
df1.to_csv('df1.csv')
