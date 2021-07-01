#app/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view

#http://127.0.0.1:8000/api/hello
@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})
