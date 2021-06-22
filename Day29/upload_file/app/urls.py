#app/urls.py
from django.urls import path
from .views import *
urlpatterns = [ 
    path('api/get-todos', getTodos),
    path('api/add-todo', addTodo),
    path('api/login', login),
    path('api/hello', helloAPI),
    path('upload', upload),
    path('', index),
]