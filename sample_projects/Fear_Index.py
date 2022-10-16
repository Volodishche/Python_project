import requests
from bs4 import BeautifulSoup as bs

url = "https://alternative.me/crypto/fear-and-greed-index"
r = requests.get(url)
#print(r.text)

soup = bs(r.text, "lxml")
Fear_Index = soup.find("div", class_="fng-circle").text
print(Fear_Index)

				
			