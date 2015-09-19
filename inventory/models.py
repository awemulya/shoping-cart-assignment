from django.db import models
from merchant.models import Merchant


class Item(models.Model):
    item_id = models.CharField(max_length=20)
    merchant_id  = models.CharField(max_length=20)
    item_name  = models.CharField(max_length=254)
    item_price  = models.FloatField(default=0.0)
    expiry_date = models.DateField(null=True, blank=True)
    merchant_obj = models.ForeignKey(Merchant, related_name='items')


class Cart(models.Model):
    date = models.DateField(null=True)
    status = models.FloatField(default=True)
    customer = models.CharField(max_length=30, null=True)

    def cancel(self):
        self.status=False
        self.save()

    def item_update(self, sn, old, new):
        rows = self.rows.filter(sn=sn, item=old)
        if rows:
            row= rows[0]
            row.item = new
            row.save()
            return row.item.item_name


class Rows(models.Model):
    sn  = models.IntegerField(default=0)
    cart = models.ForeignKey(Cart, related_name='rows')
    item = models.ForeignKey(Item)
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=50)
