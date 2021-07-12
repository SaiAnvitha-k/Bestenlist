# scrap the data of webpage and insert class data and save in excel
import pandas as pd
import requests
from bs4 import BeautifulSoup
x = requests.get("https://www.spotify.com")
soup = BeautifulSoup(x.text, 'lxml')
a = soup.find_all('div', class_='maincounter-number')
data = []
for i in a:
    span = i.find('span')
    data.append(span.string)
print(data)

df = pd.DataFrame({"Classdata" : data})
df.index = ['Title']
df.to_csv('Classdata.csv')
