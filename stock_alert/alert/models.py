from django.db import models

# Create your models here.
# id,symbol,name,current_price

class StockPrice(models.Model):
    stock_id = models.CharField(max_length=20)
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    current_price = models.FloatField(max_length=10)


class StockAlert(models.Model):
    symbol = models.CharField(max_length=10)
    alert_price = models.FloatField(max_length=10)

class AlertLog(models.Model):
    type = models.CharField(max_length=10)
    symbol = models.CharField(max_length=10)
    alert_price = models.FloatField(max_length=10)


