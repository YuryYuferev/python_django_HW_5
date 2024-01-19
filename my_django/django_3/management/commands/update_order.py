from django.core.management.base import BaseCommand
from django_2.models import Order

class Command(BaseCommand):
    help = "Update order by id."

def update_order(order_id, client, products, total_amount):
    order = Order.objects.get(id=order_id)
    order.client = client
    order.products.set(products)
    order.total_amount = total_amount
    order.save()
    return order
