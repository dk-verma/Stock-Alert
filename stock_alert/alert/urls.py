from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("all_alerts", views.AlertInfo ,name="all-alerts"),
    path("active_alerts", views.ActiveAlertInfo ,name="active-alerts"),
    path("create_alert/<str:symbol>/<int:alert_price>", views.CreateStockAlert ,name="alerts-create"),
    path("delete_alert/<str:symbol>/<int:alert_price>", views.DeleteStockAlert ,name="alerts-delete"),
    path("current_stock_price", views.StockCurrentInfo ,name="stock-price"),
    path("stock_triggered", views.StockHittingAlert ,name="alert-found"),
]