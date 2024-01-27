from django.core.management.base import BaseCommand
from django_2.models import Client

class Command(BaseCommand):
    help = "Get all client."


def get_all_clients():
    clients = Client.objects.all()
    return clients
