from django.core.management.base import BaseCommand
from hw_app.models import Product
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Get product by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='product ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        product = Product.objects.filter(pk=pk).first()
        self.stdout.write(f'{product}')
        logger.info('Info about product uploaded')
