from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.serializers import ModelSerializer
from .models import *

class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

@api_view(['GET'])
def searchCustomer(request):
    lst = Customer.objects.all()
    data = CustomerSerializer(instance=lst, many=True).data
    return Response(data)

@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})

