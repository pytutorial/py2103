from django.urls import path
from .views import *

urlpatterns = [
    path('create-category', createCategory),
    path('hello', hello)
]