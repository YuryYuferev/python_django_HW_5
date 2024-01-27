from django.core.management.base import BaseCommand
from django_2.models import Client

class Command(BaseCommand):
    help = "Create client."

def create_client(name, email, phone_number, address, registration_date):
    client = Client.objects.create(
        name=name,
        email=email,
        phone_number=phone_number,
        address=address,
        registration_date=registration_date
    )
    return client
