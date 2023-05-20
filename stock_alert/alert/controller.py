import requests
from .models import StockPrice, StockAlert, AlertLog
import traceback

 
# Making a get request
# response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=10&page=1&sparkline=false')
# response = response.json()
# print(response.json())



# stock_id,symbol,name,current_price

def current_stock_price():
    pass

def all_alerts(request):
    try:
        res=[]
        client_details = AlertLog.objects.all()
        if client_details is not None:
            for entry in client_details:
                type,symbol,current_price = entry.type,entry.symbol,entry.alert_price
                # print(f"id : {stock_id}, symbol : {symbol}, name : {name}, current_price : {current_price}")
                res.append((type,symbol,current_price))
            return res
        else:
            return None
    except Exception as ex:
        resp = {
            "status":"false",
            "error":str(ex),
        }
        return resp


def active_alerts(request):
    try:
        res=[]
        client_details = StockAlert.objects.all()
        if client_details is not None:
            for entry in client_details:
                symbol,current_price = entry.symbol,entry.alert_price
                # print(f"id : {stock_id}, symbol : {symbol}, name : {name}, current_price : {current_price}")
                res.append((symbol,current_price))
            return res
        else:
            return None
    except Exception as ex:
        resp = {
            "status":"false",
            "error":str(ex),
        }
        return resp


def create_alert(request, symbol, alert_price):
    try:
        entry = StockAlert.objects.filter(symbol=symbol, alert_price=alert_price)
        if not entry:
            entry = StockAlert(symbol=symbol, alert_price=alert_price)
            entry.save()
            AlertLog.objects.create(type="created",symbol=symbol, alert_price=alert_price)
        return {
            "status" : True,
            "message" : f"alert created for {symbol} with {alert_price}",
        }
    except:
        return {
            "status" : False,
            "message" : f"alert not created for {symbol} with {alert_price}",
        }


def delete_alert(request, symbol, alert_price):
    try:
        entry = StockAlert.objects.filter(symbol=symbol, alert_price=alert_price)
        if entry:
            entry.delete()
            AlertLog.objects.create(type="deleted",symbol=symbol, alert_price=alert_price)
            return {
                "status" : True,
                "message" : f"alert deleted for {symbol} with {alert_price}",
            }
        else:
            return {
                "status" : True,
                "message" : f"no alert for for {symbol} with {alert_price}",
            }
    except Exception as ex:
        return {
            "status" : False,
            "message" : str(ex),
        }


def update_stock(request):
    try:
        stocks = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&sparkline=false&')#per_page=10&page=2')
        stocks = stocks.json()
        # if stocks["status"]["error_code"]==429:
        #     return  {
        #         "status": True,
        #         "message": "Entries are updated",
        #         "result": stocks["status"]["error_message"]
        #     }
        resp = []
        for entry in stocks:
            stock_id,symbol,name,current_price = entry['id'],entry['symbol'],entry['name'],entry['current_price']
            resp.append({'symbol':symbol, 'name':name,'current_price':current_price})
            member1 = StockPrice.objects.filter(stock_id=stock_id)
            if member1:
                member1.update(current_price=current_price)
            else:
                member1 = StockPrice(stock_id=stock_id, symbol=symbol, name=name, current_price=current_price)
                member1.save()

        response = {
            "status": True,
            "message": "Entries are updated",
            "result": resp
        }
        return response

    except Exception as ex:
        print(traceback.format_exc())
        response = {
            "status":False,
            "message":str(ex),
            "result": "Internal server error"
        }
        return response

def check_alert(request):
    #write logic to check matching alert
    try:
        stock_hitting_alert=[]
        present_alert = active_alerts(request)
        for entry in present_alert:
            symbol,alert_price = entry[0], entry[1]
            stock_entry = StockPrice.objects.filter(symbol=symbol)
            # print(f" stock price = {alert_price}, stock_entry = {stock_entry[0].current_price}")
            if abs(alert_price-stock_entry[0].current_price)<=1:
                stock_hitting_alert.append((symbol,alert_price))
                AlertLog.objects.create(type="triggered",symbol=symbol, alert_price=alert_price)
        
        response = {
            "status": True,
            "message": "These stocks are hitting alert price",
            "result": stock_hitting_alert
        }
        return response
    
    except Exception as ex:
        print(traceback.format_exc())
        response = {
            "status":False,
            "message":str(ex),
            "result": "Internal server error"
        }
        return response