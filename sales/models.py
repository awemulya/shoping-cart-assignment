from django.db import models
from inventory.models import Item


class Transaction(models.Model):
    transaction_timestamp = models.DateField(null=True)
    transaction_id = models.CharField(max_length=50)
    customer_id = models.CharField(max_length=50)
    cancel_flag = models.BooleanField(default=False)


class Sales(models.Model):
    sr_no = models.IntegerField(default=0)
    transaction_id = models.CharField(max_length=100)
    item_id = models.CharField(max_length=100)
    transaction_obj = models.ForeignKey(Transaction, related_name="sales")
    item_obj = models.ForeignKey(Item, related_name='sales')