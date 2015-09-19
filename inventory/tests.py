import os
from django.test import TestCase
from inventory.models import Cart, Rows, Item
from inventory.utils import load_transaction, load_sales, load_item, load_merchant
from merchant.models import Merchant


class LoadTestCase(TestCase):
    def setUp(self):
        self.path = os.path.join(os.getcwd(), 'assignment_table_load.xls')
        self.sheet = 2
        self.mercent = Merchant(merchant_id='001',merchant_name="test merchant", merchant_address="address")
        self.mercent.save()
        self.test_item = Item(item_id="0001",merchant_id="0002",item_name="one Item", item_price=200,merchant_obj=self.mercent)
        self.test_item.save()
        self.new_item = Item(item_id="0002",merchant_id="0002",item_name="one Item new", item_price=200,merchant_obj=self.mercent)
        self.new_item.save()

        self.cart = Cart(customer="test Customer")
        self.cart.save()

    def test_data_found(self):
        """Data found according to search"""
        merchant = load_merchant(self.path, 3)
        item = load_item(self.path, 2)
        transaction = load_transaction(self.path, 0)
        sales = load_sales(self.path, 1)
        assert merchant
        assert item
        assert transaction
        assert sales

    def test_cart_create(self):

        row1 = Rows(sn=1,item=self.test_item,quantity=2.5, unit='piece', cart = self.cart)
        row2 = Rows(sn=2,item=self.test_item,quantity=3.5, unit='piece', cart = self.cart)
        row3 = Rows(sn=3,item=self.test_item,quantity=42.5, unit='piece', cart = self.cart)
        row1.save()
        row2.save()
        row3.save()

        assert self.cart.rows.all()
        assert self.cart.status

        name = self.cart.item_update(1, self.test_item, self.new_item)
        assert name == self.new_item.item_name

        self.cart.cancel()
        assert not self.cart.status
