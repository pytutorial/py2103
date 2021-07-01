from django.contrib import admin
# Register your models here.
from .models import *
admin.site.register(Todo)
admin.site.register(Category)
admin.site.register(Product)