from django.core.management.base import BaseCommand
from django_2.models import Product

class Command(BaseCommand):
    help = "Update product by id."

def update_product(product_id, name, description, price, quantity):
    product = Product.objects.get(id=product_id)
    product.name = name
    product.description = description
    product.price = price
    product.quantity = quantity
    product.save()
    return product
