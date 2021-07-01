#app/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import ModelSerializer, DateTimeField
from .models import *

class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
    
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
