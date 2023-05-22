# stock_alert
## python, djangorestframework

It's an end to end model to send alarms/notifications for any stock, based upon previously defined alert price and their live prices.
after cloning, goto project directory in terminal follow these steps

## setup
### pre-requisite
- `git clone  https://github.com/dk-verma/stock_alert.git`
- install all the dependency using - `pip install -r requirements.txt`

1. to start server - `python3 manage.py runserver`
2. to get all alert - http://127.0.0.1:8000/alert/all_alerts
3. to get all active alerts - http://127.0.0.1:8000/alert/active_alerts
4. to create alert - http://127.0.0.1:8000/alert/create_alert/symbol/int_value
5. to delete alert - http://127.0.0.1:8000/alert/delete_alert/symbol/int_value
  P.S. for step 4 and 5 get the stock symbol from https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=400&page=1&sparkline=false
6. hit this to update all the stock price - http://127.0.0.1:8000/alert/current_stock_price
7. to find out triggered stock - http://127.0.0.1:8000/alert/stock_triggered

6 and 7 step should be executed per min, for now we'll hitting these endpoints manually, also we are allowed to hit these 30times/min

