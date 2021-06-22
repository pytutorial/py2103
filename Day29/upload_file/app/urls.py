#app/urls.py
from django.urls import path
from .views import *
urlpatterns = [ 
    path('api/hello', helloAPI),
    path('upload', upload),
    path('', index),
]