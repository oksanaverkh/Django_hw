from django.core.management.base import BaseCommand
from hw_app.models import Client
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Create client."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Client's name")
        parser.add_argument('email', type=str, help="Client's email")
        parser.add_argument('telephone', type=str, help="Client's telephone")
        parser.add_argument('address', type=str, help="Client's address")
        parser.add_argument('birthday', type=str, help="Client's birthday")

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        telephone = kwargs.get('telephone')
        address = kwargs.get('address')
        birthday = kwargs.get('birthday')

        client = Client(name=name, email=email, telephone=telephone,
                        address=address, birthday=birthday)

        client.save()
        self.stdout.write(f'{client}')
        logger.info('Client created')
