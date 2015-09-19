from sales.models import Transaction, Sales
from inventory.models import Item
from merchant.models import Merchant

from django.http import HttpResponse
from django.shortcuts import render
import os
from django.test import TestCase
from inventory.utils import load_transaction, load_sales, load_item, load_merchant

def load(request):
    path = os.path.join(os.getcwd(), 'assignment_table_load.xls')

    merchant = load_merchant(path, 3)
    item = load_item(path, 2)
    transaction = load_transaction(path, 0)
    sales = load_sales(path, 1)
    return HttpResponse("okeys")

def monthly_sales(request):
    sales_list= []
    for month in range(12):
        total_price = 0
        if Transaction.objects.filter(transaction_timestamp__month=month).exists():
            tl = Transaction.objects.filter(transaction_timestamp__month=month)
            for t in tl:
                sl = t.sales.all()
                if sl:
                    for s in sl:
                        price = s.item_obj.item_price
                        total_price += price
            # import pdb
            # pdb.set_trace()
            sales_list.append({'id':month,'amount':total_price })


    return render(request, 'monthly_sales.html', {'sl': sales_list})




