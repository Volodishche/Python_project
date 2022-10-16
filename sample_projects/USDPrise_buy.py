import requests
from bs4 import BeautifulSoup as bs

url = "https://kurs.com.ua/valyuta/usd"
r = requests.get(url)
#print(r.text)

soup = bs(r.text, "lxml")
USDPrice_buy = soup.find("tbody", class_="text-right").find_all("td")[2].find(class_="course").text[:6]
print(USDPrice_buy)

				
			