from django.db import models

# Create your models here.

class Todo(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    createdDate = models.DateTimeField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,
             on_delete=models.PROTECT)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Customer(models.Model):
    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    createdDate = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    orderDate = models.DateTimeField()
    total = models.IntegerField()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    qty = models.IntegerField()
    priceUnit = models.IntegerField()
    total = models.IntegerField()


# python manage.py makemigrations   --> SQL Generate
# python manage.py migrate          --> SQL Execute
# - Add Product/Category --> admins.py
# - Goto admin panel --> add records
# - Create API: List/get Category,Product,searchProduct: name,categoryCode,priceMin-priceMax