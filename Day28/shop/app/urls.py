from django.urls import path
from .views import *

urlpatterns = [ 
    path('', index),
    path('view-product/<id>', viewProduct),
]