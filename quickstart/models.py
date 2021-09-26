from django.db import models
from djongo import models

class Bid(models.Model):
    px = models.FloatField()
    qty = models.FloatField()
    num = models.IntegerField()

    class Meta:
        abstract = True

class Ask(models.Model):
    px = models.FloatField()
    qty = models.FloatField()
    num = models.IntegerField()

    class Meta:
        abstract = True
    
class Crypto(models.Model):
    symbol = models.CharField(primary_key=True, max_length = 200)
    bids = models.ArrayField(model_container = Bid)
    asks = models.ArrayField(model_container = Ask)