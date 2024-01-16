from django.core.management.base import BaseCommand
from django_2.models import Product

class Command(BaseCommand):
    help = "Get product by id."

def get_product(product_id):
    product = Product.objects.get(id=product_id)
    return product
