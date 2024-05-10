from django.shortcuts import render
from .models import Product, Order, Client, User
from django.http import JsonResponse
from django.db.models import F 
from django.views.decorators.csrf import csrf_exempt
import json




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

def list_users(request):
    users = User.objects.all()
    # orders = Order.objects.all()
    # data = Order.objects.get(pk=1)
    # client_name = Client.objects.get(pk = data.client_id)
    return  JsonResponse({'orders': list(users.values())})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['username']
        try:
            user = User.objects.get(usernname=name)
            return  JsonResponse({'orders': user.staff})
        except: 
            return JsonResponse({'message', 'No existe ese usuario'})
    # orders = Order.objects.all()
    # data = Order.objects.get(pk=1)
    # client_name = Client.objects.get(pk = data.client_id)


@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data['name']
            flavour = data['flavour']
            stock = data['stock']
            price = data['price']
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
        data = json.loads(request.body)
        name = data['name']
        lastname = data['lastname']
        email = data['email']
        quantity_orders = data['quantity']
        try:
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
        data = json.loads(request.body)
        client_id = data['client_id']
        product_id = data['product_id']
        quantity = data['quantity'] 
        details = data['details']
        address = data['address']
        try:
            client = Client.objects.get(id=client_id)
            product = Product.objects.get(id=product_id)
        except Client.DoesNotExist:
            return JsonResponse({'error': f'El cliente con el ID proporcionado no existe {client_id}'})
        order = Order(client=client, products=product, quantity=quantity, details=details, address=address)
        order.save()
        return JsonResponse({'message': 'La orden ha sido creada'})
    else:
        return JsonResponse({'error': 'Solo se aceptan solicitudes POST'})


@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        email = data['email']
        staff = data['staff']
        try:
            user = User(username=username, password=password, email=email, staff=staff)
            user.save()
            return JsonResponse({'message': 'El User ha sido creado'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Solo se aceptan solicitudes POST'})
    

@csrf_exempt
def update_order(request):
    if request.method == 'PATCH':
        try:
            data = json.loads(request.body)
            order_id = data['id']
            order = Order.objects.get(pk=order_id)
            order.details = data['details']
            order.address = data['address']
            order.save()
            return JsonResponse({'message': 'La orden ha sido actualizada'})
        except Order.DoesNotExist:
            return JsonResponse({'error': f'La orden con el ID {order_id} no existe'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Solo se aceptan solicitudes PUT'})

@csrf_exempt
def delete_order(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            order_id = data['id']
            order = Order.objects.get(pk=order_id)
            order.delete()
            return JsonResponse({'message': 'La orden ha sido eliminada'})
        except Order.DoesNotExist:
            return JsonResponse({'error': f'La orden con el ID {order_id} no existe'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'error': 'Solo se aceptan solicitudes DELETE'})
        