from requests import get, post
from bs4 import BeautifulSoup

url = 'https://www.binance.com/en/trade/BTC_BUSD?type=spot'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15'
}

page = get(url, headers=headers)
soup = BeautifulSoup(page.content, 'lxml')
## Header information
title = soup.find_all('title')
print(title)