from django.core.management.base import BaseCommand
from hw_app.models import Client
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Update client by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('email', type=str, help="Client's email")
        parser.add_argument('telephone', type=str, help="Client's telephone")
        parser.add_argument('address', type=str, help="Client's address")
        parser.add_argument('birthday', type=str, help="Client's birthday")

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        email = kwargs.get('email')
        telephone = kwargs.get('telephone')
        address = kwargs.get('address')
        birthday = kwargs.get('birthday')

        client = Client.objects.filter(pk=pk).first()
        client.name = name
        client.email = email
        client.telephone = telephone
        client.address = address
        client.birthday = birthday

        client.save()
        self.stdout.write(f'{client}')
        logger.info("Client's information updated")
