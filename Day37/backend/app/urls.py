from django.urls import path
from .views import *

urlpatterns = [
    path('search-customer', searchCustomer),
    path('hello', hello)
]