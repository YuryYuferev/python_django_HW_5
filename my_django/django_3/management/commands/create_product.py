from django.core.management.base import BaseCommand
from django_2.models import Product

class Command(BaseCommand):
    help = "Create product."

def create_product(name, description, price, quantity, added_date):
    product = Product.objects.create(
        name=name,
        description=description,
        price=price,
        quantity=quantity,
        added_date=added_date
    )
    return product

