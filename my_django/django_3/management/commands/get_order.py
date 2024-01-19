from django.core.management.base import BaseCommand
from django_2.models import Order

class Command(BaseCommand):
    help = "Get order by id."

def get_order(order_id):
    order = Order.objects.get(id=order_id)
    return order
