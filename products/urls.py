from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_order, name='orders'),
    path('products/', views.list_products, name='products'),
    path('clients/', views.list_clients, name='clients'),
    path('user/', views.list_users, name='saveus'),
    path('saveproduct/', views.create_product, name='savepr'),
    path('saveclient/', views.create_client, name='savecl'),
    path('saveorder/', views.create_order, name='saveor'),
    path('saveuser/', views.create_user, name='saveus'),
    path('delete/', views.delete_order, name='delete')
]