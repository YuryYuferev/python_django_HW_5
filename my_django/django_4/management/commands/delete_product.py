from django.core.management.base import BaseCommand
from django_2.models import Product

class Command(BaseCommand):
    help = "Delete product by id."

def delete_product(product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
