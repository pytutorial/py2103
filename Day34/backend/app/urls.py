from django.urls import path
from .views import *
urlpatterns = [ 
    path('get-product-list', getProductList),
    path('hello', hello)
]