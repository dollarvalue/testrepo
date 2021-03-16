import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    url = "https://www.carousell.com.hk/categories/men-s-fashion-3/mens-bags-wallets-476/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.findAll('a',{'class':'D_fj D_jZ M_mg'}):
        href = link.get('href')
        print(href)

trade_spider(1)
