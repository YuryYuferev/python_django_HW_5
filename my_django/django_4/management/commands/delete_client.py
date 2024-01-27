from django.core.management.base import BaseCommand
from django_2.models import Client

class Command(BaseCommand):
    help = "Delete client by id."

def delete_client(client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
