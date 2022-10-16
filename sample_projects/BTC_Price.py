import requests
from bs4 import BeautifulSoup as bs

url = "https://bitinfocharts.com/ru/crypto-kurs/"
r = requests.get(url)

soup = bs(r.text, "lxml")
BTC_Price = soup.find("a", class_="conv_cur").text[2:11]
print(BTC_Price)
