import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'https://www.pigiame.co.ke/tvs?page=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a', {'class': 'listing-card__inner'}):
            href = "https://www.pigiame.co.ke/" + link.get('href')
            title = link.string
            # print(href)
            # print(title)
            get_single_item_data(href) 
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item_name in soup.findAll('h1', {'class': 'listing-item__header'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = "https://www.pigiame.co.ke/" + link.get('href')
        print(href)


trade_spider(3)