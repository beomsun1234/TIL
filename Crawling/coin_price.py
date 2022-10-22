from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

current_url = 'https://kr.investing.com/crypto/'
headers = {'User-Agent':'Mozilla/5.0'}
req = Request(current_url, headers = headers)

# http source 추출을 위한 변수설정
html = urlopen(req)
source = html.read().decode("utf-8")
code = html.getcode()

# html 구문을 객체화한다.
soup = BeautifulSoup (source)

# 코인정보가  담긴 태그 변수설정
coins = soup.select("table.genTbl > tbody tr")

coininfo=[]

for coin in coins:
    coin_name = coin.select("td.js-currency-name a")
    coin_symbol = coin.select("td.js-currency-symbol")
    coin_price = coin.select("td.js-currency-price a")
    coin_market_cap = coin.select("td.js-market-cap")
    coin_24h_volume = coin.select("td.js-24h-volume")
    coin_total_vol = coin.select("td.js-total-vol")
    coin_change_24h = coin.select("td.js-currency-change-24h")
    
    if len(coin_price) > 0 or len(coin_name) > 0 :
        coininfo.append({
        "종목" : coin_name[0].text,
        "기호" : coin_symbol[0].text,
        "가격(KRW)" : coin_price[0].text,
        "총 시가" : coin_market_cap[0].text,
        "거래량(24h)" : coin_24h_volume[0].text,
        "총 거래량" : coin_total_vol[0].text,
        "시세변동(24h)": coin_change_24h[0].text
        })

print(coininfo , type(coininfo))
