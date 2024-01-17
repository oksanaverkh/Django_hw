from django.core.management.base import BaseCommand
from hw_app.models import Product
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Update product by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help="Product's ID")
        parser.add_argument('name', type=str, help="Product's name")
        parser.add_argument('description', type=str,
                            help="product's description")
        parser.add_argument('price', type=float, help="product's price")
        parser.add_argument('quantity', type=int, help="product's quantity")
        parser.add_argument('receipt_date', type=str,
                            help="product's receipt_date")

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')
        receipt_date = kwargs.get('receipt_date')

        product = Product.objects.filter(pk=pk).first()
        product.name = name
        product.description = description
        product.price = price
        product.quantity = quantity
        product.receipt_date = receipt_date

        product.save()
        self.stdout.write(f'{product}')
        logger.info("Product's information updated")
