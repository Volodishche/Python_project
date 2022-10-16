import requests
from bs4 import BeautifulSoup as bs

url = "https://index.minfin.com.ua/markets/fuel/reg/harkovskaya"
r = requests.get(url)
#print(r.text)

soup = bs(r.text, "lxml")
BenzinPrice95 = soup.findAll ("big")[1].text
print(BenzinPrice95)

				
			