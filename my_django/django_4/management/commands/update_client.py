from django.core.management.base import BaseCommand
from django_2.models import Client

class Command(BaseCommand):
    help = "Update client by id."

def update_client(client_id, name, email, phone_number, address):
    client = Client.objects.get(id=client_id)
    client.name = name
    client.email = email
    client.phone_number = phone_number
    client.address = address
    client.save()
    return client