import requests
from alert.models import StockPrice
 
# Making a get request
response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=10&page=1&sparkline=false')
# print(response.json())
# print(type(response))
response = response.json()

for entry in response:
    stock_id,symbol,name,current_price = entry['id'],entry['symbol'],entry['name'],entry['current_price']
    print(f"id : {stock_id}, symbol : {symbol}, name : {name}, current_price : {current_price}")
    member1 = StockPrice(stock_id=stock_id, symbol=symbol, name=name, current_price=current_price)
    member1.save()
    
# print json content
# print(response.json())