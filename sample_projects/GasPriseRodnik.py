import requests
from bs4 import BeautifulSoup as bs

url = "https://index.minfin.com.ua/markets/fuel/tm/rodnik"
r = requests.get(url)
#print(r.text)

soup = bs(r.text, "lxml")
GasPriseRodnik = soup.find ("big").text
print(GasPriseRodnik)

				
			