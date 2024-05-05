from django.db import models


# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.CharField(max_length=25)
    description = models.TextField()
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
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return str(self.id)

    