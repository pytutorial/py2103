from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.serializers import ModelSerializer
from .models import *
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

@api_view(['POST'])
def createCategory(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'success': True})
    else:
        return Response({'errors': serializer.errors})

@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})
