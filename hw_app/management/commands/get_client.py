from django.core.management.base import BaseCommand
from hw_app.models import Client
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Get client by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        client = Client.objects.filter(pk=pk).first()
        self.stdout.write(f'{client}')
        logger.info('Info about client uploaded')
