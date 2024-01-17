from django.core.management.base import BaseCommand
from hw_app.models import Order
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Get all orders."

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        self.stdout.write(f'{orders}')
        logger.info('List of orders uploaded')
