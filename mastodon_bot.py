import requests
import schedule
import os
import time

token = os.getenv('TOKEN')
coins = ['btc', 'eth', 'xmr', 'ltc', 'etc', 'dot', 'grin']
url = "https://botsin.space/api/v1/statuses"


def price_coin(arr):
    r = requests.get('https://www.bw.com/exchange/config/controller/website/pricecontroller/getassistprice')
    data = r.json()
    string = ''
    for i in range(len(arr)):
        price = data['datas']['usd'][arr[i]]
        string_coin = arr[i]
        string = string + string_coin.upper() + ': ' + price + '$' + '\n'
    return string

price_coin = price_coin(coins)
headers = {"Authorization": "Bearer " + token}
body = {"status": price_coin }


def run_func():
    r = requests.post(url, headers = headers, json = body, timeout = 10)


schedule.every().day.at("10:00").do(run_func)
schedule.every().day.at("13:00").do(run_func)
schedule.every().day.at("16:00").do(run_func)
schedule.every().day.at("19:00").do(run_func)
schedule.every().day.at("22:00").do(run_func)


while True:
    schedule.run_pending()
    time.sleep(1)