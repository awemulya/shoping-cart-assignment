from django.db import models


class Merchant(models.Model):
    merchant_id = models.CharField(max_length=20)
    merchant_name = models.CharField(max_length=100)
    merchant_address = models.CharField(max_length=254)

