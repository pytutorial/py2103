#app/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


@api_view(['GET']) # 127.0.0.1:8000/api/hello
@permission_classes([IsAuthenticated])
def hello(request):
    return Response({'message': 'Hello'})