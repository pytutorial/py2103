#app/views.py
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import ModelSerializer, DateTimeField
from .models import *

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'name', 'status', 'createdDate'] #'__all__'
    
    createdDate = DateTimeField(format='%H:%M:%S %d/%m/%Y')

#http://127.0.0.1:8000/api/hello?name=Nguyen+Van+A
@api_view(['GET'])
def hello(request):
    name = request.GET.get('name', '')
    return Response({'message': f'Hello {name}'})

@api_view(['POST'])
def login(request):  #  http:/127.0.0.1:8000/api/login
    username = request.data.get('username', '')
    password = request.data.get('password', '')

    if username != 'admin':
        return Response({'error': 'Tên đăng nhập không tồn tại'})
    
    if password != '1234':
        return Response({'error': 'Mật khẩu không chính xác'})

    return Response({'success': True})

@api_view(['GET'])
def getToDoList(request): # 127.0.0.1:8000/api/get-todo-list
    todoList = Todo.objects.all() # Db query
    results = TodoSerializer(todoList, many=True).data
    #results = []
    #for todo in todoList:
    #    results.append({
    #        'id': todo.id,
    #        'name': todo.name,
    #        'description': todo.description,
    #        'createdDate': str(todo.createdDate),
    #        'status': todo.status
    #    })
    return Response(results)

@api_view(['GET'])
def getTodo(request, pk): # 127.0.0.1:8000/api/get-todo/1
    todo = Todo.objects.get(pk=pk)
    result = TodoSerializer(todo).data
    return Response(result)

#=================================== Category =======================
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

@api_view(['GET'])
def getCategoryList(request):
    categoryList = Category.objects.all()
    serialzer = CategorySerializer(categoryList,many=True)
    return Response(serialzer.data)

@api_view(['GET'])
def getCategory(request, pk):
    category = Category.objects.get(pk=pk)
    serilizer = CategorySerializer(category)
    return Response(serilizer.data)

@api_view(['POST'])
def createCategory(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True})
    else:
        return Response({'errors': serializer.errors})

@api_view(['PUT'])
def updateCategory(request, pk):
    category = Category.objects.get(pk=pk)
    serializer = CategorySerializer(data=request.data,
                         instance=category)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True})
    else:
        return Response({'errors': serializer.errors})
#==================================== Product ======================
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

@api_view(['GET'])
def getProductList(request):
    productList = Product.objects.all()
    serialzer = ProductSerializer(productList,many=True)
    return Response(serialzer.data)

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(pk=pk)
    serilizer = ProductSerializer(product)
    return Response(serilizer.data)

@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"success": True})
    else:
        return Response({"errors": serializer.errors})

@api_view(['GET'])
def searchProduct(request):
    keyword = request.GET.get('keyword', '')
    categoryCode = request.GET.get('categoryCode', '')
    priceMin = request.GET.get('priceMin')
    priceMax = request.GET.get('priceMax')

    productList = Product.objects.all()
    if keyword:
        productList = productList.filter(
                        name__icontains=keyword)
    
    if categoryCode:
        productList = productList.filter(
                category__code=categoryCode
        )

    if priceMin:
        ...

    if priceMax:
        ...
