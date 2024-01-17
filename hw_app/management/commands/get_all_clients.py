from django.core.management.base import BaseCommand
from hw_app.models import Client
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Get all clients."

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        self.stdout.write(f'{clients}')
        logger.info('List of clients uploaded')
