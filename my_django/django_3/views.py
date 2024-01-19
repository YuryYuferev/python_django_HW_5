from django.shortcuts import render
from .models import Client, Order, Product
from datetime import datetime, timedelta

def client_orders(request, client_id):
    client = Client.objects.get(id=client_id)
    clients = ['Иван Иванов', 'Петр Петров', 'Сидор Сидоров']
    orders = Order.objects.filter(client=client)
    context = {
        'client': client,
        'orders': orders
    }
    return render(request, 'client_orders.html', context)

def client_products(request, client_id):
    client = Client.objects.get(id=client_id)
    client = {
        'name': 'Иван Иванов'
    }
    seven_days_ago = datetime.now() - timedelta(days=7)
    thirty_days_ago = datetime.now() - timedelta(days=30)
    one_year_ago = datetime.now() - timedelta(days=365)
    products = client.order_set.filter(order_date__range=[seven_days_ago, datetime.now()]).values('products__name', 'products__added_date')
    context = {
        'client': client,

        'products_30_days': client.order_set.filter(order_date__range=[thirty_days_ago, datetime.now()]).values('products__name', 'products__added_date'),
        'products_365_days': client.order_set.filter(order_date__range=[one_year_ago, datetime.now()]).values('products__name', 'products__added_date')
    }
    return render(request, 'client_products.html', context)


    # products_7_days = [
    #     {'name': 'сыр', 'added_date': '2024-01-19'},
    #     {'name': 'колбаса', 'added_date': '2024-01-19'},
    #     {'name': 'молоко', 'added_date': '2024-01-18'}
    # ]
    #
    # products_30_days = [
    #     {'name': 'сыр', 'added_date': '2024-01-09'},
    #     {'name': 'колбаса', 'added_date': '2024-01-09'},
    #     {'name': 'молоко', 'added_date': '2024-01-01'}
    # ]
    # products_365_days = [
    #     {'name': 'сыр', 'added_date': '2023-09-20'},
    #     {'name': 'колбаса', 'added_date': '2023-09-20'},
    #     {'name': 'молоко', 'added_date': '2023-07-19'}
    # ]
    # context = {
    #     'client': client,
    #     'products_7_days': products_7_days,
    #     'products_30_days': products_30_days,
    #     'products_365_days': products_365_days
    # }
    # return render(request, 'client_products.html', context)
