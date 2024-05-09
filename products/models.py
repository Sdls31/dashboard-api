from django.db import models



# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.CharField(max_length=25)
    quantity_orders = models.IntegerField()
    
    def __str__(self):
        return self.name 
    

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    flavour = models.CharField(max_length=15, default="")
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name 


class Order(models.Model):
    reception = 'Recepcion'
    stored = 'Almacenado'
    packaging = 'Envasado'
    packaged = 'Empaquetado'
    quality = 'Calidad'
    distribution = 'Distribucion'

    
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    products = models.ForeignKey(Product,  on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    details = models.CharField(max_length=15, choices=[(reception , 'Recepcion'), (stored , 'Almacenado'), (packaging , 'Envasado'), (packaged ,'Empaquetado'), ( quality , 'Calidad'), ( distribution , 'Distribucion')], default="Recepcion")
    address = models.CharField(max_length=50, default="Mexico")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        
        return str(self.id)

    