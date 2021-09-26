from types import BuiltinFunctionType

from numpy.ma.core import count
from quickstart.models import Crypto
from django.http import HttpResponse
import numpy as np
import json
import requests
import re


#Metodo que carga la consulta en bd
def data_load(request):
    data = {}

    try:
        response = requests.get("https://api.blockchain.com/v3/exchange/l3/"+request.GET['coin'])
        data = response.json()
    except:
        return HttpResponse(status = 400)

    try:
        #Borramos en BD si ya existe esa busqueda para actualizar los datos
        if Crypto.objects.filter(symbol = data['symbol']).exists(): Crypto.objects.filter(symbol = data['symbol']).delete()

        Crypto.objects.create(
            symbol = data['symbol'],
            bids = data['bids'],
            asks = data['asks']
        )

        return HttpResponse(status = 201)
    except KeyError as e:
        print("No existe esa moneda")
        return HttpResponse(status = 400)

def statistics_bids(request):

    bids_list = []
    average_value = 0
    max_value = 0
    max_value_index = 0
    min_malue = 0
    min_malue_index = 0
    total_qty = 0
    total_px = 0

    data_to_send = {}
    try:
        crypto_aux = Crypto.objects.filter(symbol = request.GET['coin'])
    except:
        return HttpResponse(status = 400)
    
    try:
        #Limpiamos los valores que no necesitamos
        crypto_aux = crypto_aux.values()[0]
        
        for index,bid in enumerate(crypto_aux.get('bids')):
            bid.update([('value' ,round(np.multiply(bid['px'],bid['qty']), 2))])
            bids_list.append(bid)
        
        average_value = round(np.mean(list(i['value'] for i in bids_list)),2)
        max_value = max(list(i['value'] for i in bids_list))
        max_value_index = list(i['value'] for i in bids_list).index(max_value)
        min_malue = min(list(i['value'] for i in bids_list))
        min_malue_index = list(i['value'] for i in bids_list).index(min_malue)
        total_qty = round(sum(list(i['qty'] for i in bids_list)))
        total_px = round(sum(list(i['px'] for i in bids_list)))

        data_to_send['bids'] = {'average_value' : average_value,
        'greater_value' : bids_list.__getitem__(max_value_index),
        'lesser_value' : bids_list.__getitem__(min_malue_index),
        'total_qty' : total_qty,
        'total_px' : total_px}

        return HttpResponse(json.dumps(data_to_send), content_type="application/json")
    except IndexError as e:
        print("No existe esa moneda en la BD, realice una carga con esa moneda")
        return HttpResponse(status = 404)

def statistics_asks(request):

    asks_list = []
    average_value = 0
    max_value = 0
    max_value_index = 0
    min_malue = 0
    min_malue_index = 0
    total_qty = 0
    total_px = 0

    data_to_send = {}

    try:
        crypto_aux = Crypto.objects.filter(symbol = request.GET['coin'])
    except:
        return HttpResponse(status = 400)
    
    try:

        #Limpiamos los valores que no necesitamos
        crypto_aux = crypto_aux.values()[0]

        for index,ask in enumerate(crypto_aux.get('asks')):
            ask.update([('value' ,round(np.multiply(ask['px'],ask['qty']), 2))])
            asks_list.append(ask)
        
        average_value = round(np.mean(list(i['value'] for i in asks_list)),2)
        max_value = max(list(i['value'] for i in asks_list))
        max_value_index = list(i['value'] for i in asks_list).index(max_value)
        min_malue = min(list(i['value'] for i in asks_list))
        min_malue_index = list(i['value'] for i in asks_list).index(min_malue)
        total_qty = round(sum(list(i['qty'] for i in asks_list)))
        total_px = round(sum(list(i['px'] for i in asks_list)))

        data_to_send['asks'] = {'average_value' : average_value,
        'greater_value' : asks_list.__getitem__(max_value_index),
        'lesser_value' : asks_list.__getitem__(min_malue_index),
        'total_qty' : total_qty,
        'total_px' : total_px}

        return HttpResponse(json.dumps(data_to_send), content_type="application/json")
    except IndexError as e:
        print("No existe esa moneda en la BD, realice una carga con esa moneda")
        return HttpResponse(status = 404)

def statistics(request):

    data_to_send = {}
    bids_list = []
    asks_list = []

    crypto_list_aux = Crypto.objects.all()

    for x in crypto_list_aux:
        for bid in x.bids:
            bid.update([('value' ,round(np.multiply(bid['px'],bid['qty']), 2))])
            bids_list.append(bid)
        for ask in x.asks:
            ask.update([('value' ,round(np.multiply(ask['px'],ask['qty']), 2))])
            asks_list.append(ask)
        data_to_send[x.symbol] = {
            "bids":{
                "count" : count(x.bids),
                "qty" : round(sum(list(i['qty'] for i in bids_list))),
                "value" : round(sum(list(i['value'] for i in bids_list)))
            },
            "asks":{
                "count" : count(x.asks),
                "qty" : round(sum(list(i['qty'] for i in asks_list))),
                "value" : round(sum(list(i['value'] for i in asks_list)))
            }
        }

    return HttpResponse(json.dumps(data_to_send), content_type="application/json")