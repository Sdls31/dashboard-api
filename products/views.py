from django.shortcuts import render
from .models import Product, Order, Client
from django.http import JsonResponse




# Create your views here.
def list_orders(request):
    orders = Order.objects.all()
    return  JsonResponse({'orders': list(orders.values())})

def list_products(request):
    products = Product.objects.all()
    return JsonResponse({'products': list(products.values())})

def list_clients(request):
    clients = Client.objects.all()
    return JsonResponse({'products': list(clients.values())})


