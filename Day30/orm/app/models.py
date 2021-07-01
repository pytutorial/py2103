from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    gender = models.CharField(max_length=20, blank=True) # MALE/FEMALE
    birthDate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT) #SET_NULL(null=True)/CASCADE
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    orderDate = models.DateTimeField()
    qty = models.IntegerField()
    priceUnit = models.IntegerField()
    total = models.IntegerField()

# python manage.py makemigrations --> SQL generator
# python manage.py migrate        --> SQL executor
# python manage.py shell

