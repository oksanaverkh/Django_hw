from django.core.management.base import BaseCommand
from hw_app.models import Client
import datetime
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Generate fake clients"

    def handle(self, *args, **kwargs):
        for i in range(1, 10):
            client = Client(name=f'Client {i}', email=f'mailOfClient{i}@mail.ru', telephone=f'+7999000{i*1111}',
                            address=f'address {i}', birthday=datetime.date(1980, 1, i))
            self.stdout.write(self.style.SUCCESS(f'Client created: {client}'))
            client.save()
    
    logger.info('Fake clients created')
