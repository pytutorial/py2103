#app/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET']) # 127.0.0.1:8000/api/hello
def hello(request):
    return Response({'message': 'Hello'})