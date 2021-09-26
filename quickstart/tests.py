from logging import error
import requests
from quickstart.models import Crypto
from django.test import TestCase

class CryptoTestCase(TestCase):
    def setUp(self):
        Crypto.objects.create(
            symbol = 'prueba',
            bids = [],
            asks = []
        )

        response = requests.get("https://api.blockchain.com/v3/exchange/l3/BTC-EUR")
        data = response.json()
        Crypto.objects.create(
        symbol = data['symbol'],
        bids = data['bids'],
        asks = data['asks']
        )
    
    
    def test_call_api(self):
        response = requests.get("https://api.blockchain.com/v3/exchange/l3/BTC-EUR")
        data = response.json()
        self.assertIsNotNone(data)
    
    def test_get_element(self):
        prueba = Crypto.objects.filter(symbol = 'prueba')
        eur = Crypto.objects.filter(symbol = 'BTC-EUR')
        self.assertEqual('prueba', prueba.values()[0]['symbol'])
        self.assertEqual('BTC-EUR', eur.values()[0]['symbol'])
    
    def test_not_coin(self):
        self.assertFalse(Crypto.objects.filter(symbol = 'BTC-JPY').exists())


