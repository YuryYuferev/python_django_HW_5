from django.core.management.base import BaseCommand
from django_2.models import Client

class Command(BaseCommand):
    help = "Get client by id."

def get_client(client_id):
    client = Client.objects.get(id=client_id)
    return client
