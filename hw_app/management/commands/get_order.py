from django.core.management.base import BaseCommand
from hw_app.models import Order
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Get order by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='order ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.filter(pk=pk).first()
        self.stdout.write(f'{order}')
        logger.info('Info about order uploaded')
