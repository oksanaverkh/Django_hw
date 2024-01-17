from django.core.management.base import BaseCommand
from hw_app.models import Product
from random import randrange, randint
import datetime
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generate fake products"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Number of products to create')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(count):
            product = Product(name=f'Product {i}', description=f'Description {i}', price=randrange(100.00,1000.00),
                            quantity=randint(0, 1000), receipt_date=datetime.date.today())
            self.stdout.write(self.style.SUCCESS(f'Product created: {product}'))
            product.save()

        logger.info('Fake products created')
