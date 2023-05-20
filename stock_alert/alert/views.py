from dataclasses import fields
import traceback
import requests
import os
import json
# import jwt

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseServerError
from django.core.exceptions import ObjectDoesNotExist
from django.template.response import TemplateResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import datetime
# from utils.resource import email
from . import controller
from .models import StockPrice

def home(request):
    return HttpResponse("Hello, Django!")


def AlertInfo(request):
    """
    Return a list of all the alerts.
    """
    try:
        result=controller.all_alerts(request)
        if result:
            return HttpResponse(["all alerts are = ",result],status=status.HTTP_200_OK)
        else:
            return HttpResponse(result,status=status.HTTP_400_BAD_REQUEST)
    except:
        raise HttpResponseServerError()


def ActiveAlertInfo(request):
    """
    Return a list of all the alerts.
    """
    try:
        result=controller.active_alerts(request)
        if result:
            return HttpResponse(["active alerts are = ",result],status=status.HTTP_200_OK)
        else:
            return HttpResponse(result,status=status.HTTP_400_BAD_REQUEST)
    except:
        raise HttpResponseServerError()


def CreateStockAlert(request, symbol, alert_price):
    """
    Create a new alert with symbol and alertprice.
    """
    try:
        result=controller.create_alert(request, symbol, alert_price)
        if result["status"]:
            return HttpResponse(result['message'],status=status.HTTP_200_OK)
        else:
            return HttpResponse(result['message'],status=status.HTTP_400_BAD_REQUEST)
    except:
        raise HttpResponseServerError()


def DeleteStockAlert(request, symbol, alert_price):
    """
    Delete a new alert with symbol and alertprice.
    """
    try:
        response = controller.delete_alert(request, symbol, alert_price)
        if response["status"]:
            return HttpResponse(response['message'], status=status.HTTP_200_OK)
        else:
            return HttpResponse(response['message'],status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex:
        raise HttpResponseServerError()


def StockCurrentInfo(request):
    # def put(self,request,client_id=None):
    try:
        # user = request.user
        # client_id = client_id
    #     if user.role == 'admin' or (user.role == 'client' and  user.staff.client_id == client_id):
        response=controller.update_stock(request)
        if response['status']:                    
            return HttpResponse(["stock values are updated for = ",response['result']],status=status.HTTP_200_OK)
        else:
            return HttpResponse(response['message'],status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     return Response(status=status.HTTP_401_UNAUTHORIZED)

    except Exception as ex:
        result={
            "status": False,
            "message":str(ex),
            "result":"Internal server error"
        }
        return HttpResponse(result,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def StockHittingAlert(request):
    #write logic to check matching alert
    try:
        response=controller.check_alert(request)
        if response['status']:                    
            return HttpResponse([response["message"],response['result']],status=status.HTTP_200_OK)
        else:
            return HttpResponse(response['message'],status=status.HTTP_400_BAD_REQUEST)
    except Exception as ex:
        result={
            "status": False,
            "message":str(ex),
            "result":"Internal server error"
        }
        return HttpResponse(result,status=status.HTTP_500_INTERNAL_SERVER_ERROR)



