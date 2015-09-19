import csv
import datetime
import xlrd # Import the package
from inventory.models import Item
from merchant.models import Merchant
from sales.models import Transaction, Sales


def load1(csv_file, sheet):
    with open(csv_file, 'rt') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        for row in reader:
            import pdb
            pdb.set_trace()

    return False


def load_merchant(csv_file, sheet):
    book = xlrd.open_workbook(csv_file) # Open an .xls file
    sheet = book.sheet_by_index(sheet) # Get the first sheet
    for counter in range(11): # Loop for five times
        if counter:
            # grab the current row
            rows = sheet.row_values(counter)
            mercent = Merchant(merchant_id=rows[0], merchant_name=rows[1], merchant_address=rows[2])
            mercent.save()

    return True


def load_item(csv_file, sheet):
    book = xlrd.open_workbook(csv_file) # Open an .xls file
    sheet = book.sheet_by_index(sheet) # Get the first sheet
    for counter in range(21): # Loop for five times
        if counter:
            # grab the current row
            rows = sheet.row_values(counter)
            item = Item(item_id=rows[0], merchant_id=rows[1], item_name=rows[2], item_price=rows[3],
                        merchant_obj=Merchant.objects.get(merchant_id=rows[1]))
            item.save()

    return True

def load_sales(csv_file, sheet):
    book = xlrd.open_workbook(csv_file) # Open an .xls file
    sheet = book.sheet_by_index(sheet) # Get the first sheet
    for counter in range(21): # Loop for five times
        if counter:
            # grab the current row
            rows = sheet.row_values(counter)
            sales = Sales(sr_no=rows[0], transaction_id=rows[1], item_id=rows[2],
                          transaction_obj=Transaction.objects.get(transaction_id=rows[1]),
                          item_obj=Item.objects.get(item_id=rows[2]))
            sales.save()


    return True


def load_transaction(csv_file, sheet):
    book = xlrd.open_workbook(csv_file) # Open an .xls file
    sheet = book.sheet_by_index(sheet) # Get the first sheet
    for counter in range(7): # Loop for five times
        if counter:
            # grab the current row
            rows = sheet.row_values(counter)
            date = str(rows[0])[:8]
            stamp = datetime.datetime.strptime(date, "%Y%m%d").date()
            trans = Transaction(transaction_id=rows[1], transaction_timestamp=stamp,
                                customer_id=rows[2], cancel_flag=False)
            trans.save()

    return True