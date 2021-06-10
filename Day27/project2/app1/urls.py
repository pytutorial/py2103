#app1/urls.py
from django.urls import path 
from .views import *

urlpatterns = [
    path('hello', hello), #--> app1/hello
    path('login', login),  #--> app1/login
    path('send-mail', sendMail),
]