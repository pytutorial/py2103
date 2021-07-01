#app/urls.py
from django.urls import path
from .views import *
urlpatterns = [ 
    path('get-todo-list', getToDoList),
    path('login', login),
    path('hello', hello),
]