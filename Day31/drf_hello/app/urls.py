#app/urls.py
from django.urls import path
from .views import *
urlpatterns = [ 
    path('login', login),
    path('hello', hello),
]