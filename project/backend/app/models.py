from django.db import models
from enum import Enum
# Create your models here.

class Category(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/images')

    def __str__(self):
        return self.name

class Order(models.Model):
    class Status(Enum):
        PENDING = 'Đang chờ giao hàng'
        DELIVERED = 'Đã giao hàng'
        CANCELED = 'Đang huỷ'

    customerName = models.CharField(max_length=100)
    customerPhone = models.CharField(max_length=30)
    customerAddress = models.CharField(max_length=200)
    total = models.IntegerField()
    orderDate = models.DateTimeField()
    deliverDate = models.DateTimeField(blank=True, null=True)
    cancelDate = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    priceUnit = models.IntegerField()
    qty = models.IntegerField()