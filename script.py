import django

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'

django.setup()

from flowers.models import Transactions


def get_info():
    queryset = Transactions.objects.select_related()
    for i in queryset:
        salesman = i.salesman.username
        price = i.lot.price * i.lot.quantity
        buyer = i.buyer.username
        print(salesman, price, buyer)


if __name__ == '__main__':
    get_info()
