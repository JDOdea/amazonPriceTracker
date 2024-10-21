import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/gp/product/B09R6Q8HNH/ref=ox_sc_saved_title_4?smid=A2N51JJMT2PCIM&psc=1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="title")
price = soup.find(id="priceblock_ourprice")
# converted_price = price[0:5]

print(price)