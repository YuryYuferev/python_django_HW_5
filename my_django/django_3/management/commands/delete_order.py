from django.core.management.base import BaseCommand
from django_2.models import Order

class Command(BaseCommand):
    help = "Delete order."

def delete_order(order_id):
    order = Order.objects.get(id=order_id)
    order.delete()

