from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_order, name='orders'),
    path('products/', views.list_products, name='products'),
    path('clients/', views.list_clients, name='clients'),
]