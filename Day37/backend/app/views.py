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
    start = int(request.GET.get('start') or 0)
    count = int(request.GET.get('count') or 10)
    keyword = request.GET.get('keyword', '')
    lst = Customer.objects.filter(name__icontains=keyword)
    total = lst.count()
    lst = lst[start:start+count]
    data = CustomerSerializer(instance=lst, many=True).data
    return Response({'items': data, 'total': total})

@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})

