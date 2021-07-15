from django.db import models

# Create your models here.

class Product(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/images')