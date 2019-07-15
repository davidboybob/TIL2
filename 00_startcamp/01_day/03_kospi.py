import requests
from bs4 import BeautifulSoup

html = requests.get('https://finance.naver.com/marketindex/').text
soup = BeautifulSoup(html, 'html.parser')

dallors_per_won = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text

print(dallors_per_won)

