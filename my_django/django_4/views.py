from . import forms
from .models import Client, Order
from datetime import datetime, timedelta
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import ImageForm
from .models import Product

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


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', {'form': form})

class ImageForm(forms.Form):
    image = forms.ImageField()

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()

    return render(request, 'upload_image.html', {'form': form})
