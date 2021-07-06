#app/urls.py
from django.urls import path
from .views import *
urlpatterns = [ 
    #===== Category ======
    path('get-category-list', getCategoryList),
    path('get-category/<pk>', getCategory),
    path('create-category', createCategory),

    #===== Product =======
    path('get-product-list', getProductList),
    path('get-product/<pk>', getProduct),
    path('search-product', searchProduct),
    
    #===== Todo ==========
    path('get-todo/<pk>', getTodo),
    path('get-todo-list', getToDoList),
    #===== Misc ==========
    path('login', login),
    path('hello', hello),
]