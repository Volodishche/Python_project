import requests
from bs4 import BeautifulSoup as bs

url = "https://kurs.com.ua/valyuta/usd"
r = requests.get(url)
#print(r.text)

soup = bs(r.text, "lxml")
USDPrice_sell = soup.find("tbody", class_="text-right").find_all("td")[1].find(class_="course").text[:6]
print(USDPrice_sell)

				
			