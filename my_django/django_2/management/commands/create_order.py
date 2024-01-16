from django.core.management.base import BaseCommand
from django_2.models import Order

class Command(BaseCommand):
    help = "Create order."

def create_order(client, products, total_amount, order_date):
    order = Order.objects.create(
        client=client,
        total_amount=total_amount,
        order_date=order_date
    )
    order.products.set(products)
    return order
