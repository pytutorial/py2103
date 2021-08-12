from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [ 
    path('order-product/<pk>', orderProduct),
    path('sign-up', sign_up),
    path('hello', hello)
]

# Category
router = DefaultRouter()
router.register('category', CategoryViewSet)
urlpatterns += router.urls

# Product
router = DefaultRouter()
router.register('product', ProductViewSet)
urlpatterns += router.urls