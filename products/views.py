from django.shortcuts import render
from .models import Product, Order, Client
from django.http import JsonResponse
from django.db.models import F 
from django.views.decorators.csrf import csrf_exempt




# Create your views here.
def list_orders(request):
    orders_with_client_names = Order.objects.annotate(client_name=F('client__name')).values()
    # orders = Order.objects.all()
    # data = Order.objects.get(pk=1)
    # client_name = Client.objects.get(pk = data.client_id)
    return  JsonResponse({'orders': list(orders_with_client_names)})

def list_products(request):
    products = Product.objects.all()
    return JsonResponse({'products': list(products.values())})

def list_clients(request):
    clients = Client.objects.all()
    return JsonResponse({'products': list(clients.values())})

@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            flavour = request.POST.get('flavour')
            stock = request.POST.get('stock')
            price = request.POST.get('price')
            product = Product(name=name, flavour=flavour, stock=stock, price=price)
            product.save()
            return JsonResponse({'message': 'El Producto se ha creado'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Solo se aceptan solicitudes POST'})
    
@csrf_exempt
def create_client(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            quantity_orders = request.POST.get('quantity')
            client = Client(name=name, lastname=lastname, email=email, quantity_orders=quantity_orders)
            client.save()
            return JsonResponse({'message': 'El Cliente ha sido creado'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Solo se aceptan solicitudes POST'})


@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        data = request.POST
        client_id = request.get('client_id')
        product_id = request.get('product_id') 
        quantity = request.get('quantity') 
        details = request.get('details') 
        address = request.get('address')
        try:
            client = Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return JsonResponse({'error': 'El cliente con el ID proporcionado no existe'})
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'El producto con el ID proporcionado no existe'})

        order = Order(client=client, products=product, quantity=quantity, details=details, address=address)
        order.save()
        return JsonResponse({'message': 'La orden ha sido creada'})
    else:
        return JsonResponse({'error': 'Solo se aceptan solicitudes POST'})
        