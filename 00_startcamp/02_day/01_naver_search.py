import requests
from bs4 import BeautifulSoup

#1. 원하는 주소로 요청을 보내 응답을 저장한다.
html = requests.get('https://www.naver.com').text
soup = BeautifulSoup(html, 'html.parser')
# print(type(soup))
# print(type(html))


i = soup.select(
    '#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li > a > span.ah_k'
)
    
for d in i:
    print(d.text)       

    
#두번째 커밋을 위한 주석
# print(type(kospi))
# print(kospi)
