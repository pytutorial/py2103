from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [ 
    path('hello', hello),
]

router = DefaultRouter()
router.register('player', PlayerViewSet)
urlpatterns += router.urls