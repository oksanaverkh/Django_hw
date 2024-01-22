from django.core.management.base import BaseCommand
from hw_app.models import Product, Client, Order
from random import randint
import datetime
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generate fake orders"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int,
                            help='Number of orders to create')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        clients = Client.objects.all()

        products = Product.objects.all()
        products_variety = len(products)
        clients_variety = len(clients)
        products_in_order = set()

        for _ in range(count):
            for _ in range(randint(1, 5)):
                products_in_order.add(products[randint(0, products_variety-1)])
            total_price = sum([product.price for product in products_in_order])

            order = Order(customer=clients[randint(0, clients_variety-1)],
                          total_price=total_price, order_date=datetime.date.today())
            order.save()

            for product in products_in_order:
                order.products.add(product)

            products_in_order.clear()

            self.stdout.write(self.style.SUCCESS(f'Order created: {order}'))
        logger.info('Fake orders created')
