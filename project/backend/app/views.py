from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from .serializers import *

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class StaffPermission(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_staff

@api_view(['GET'])
@permission_classes([StaffPermission])
def hello(request):
    return Response({'message': 'Hello'})

@api_view(['POST'])
def sign_up(request):
    username = request.data.get('username')
    password = request.data.get('password')
    print('pass=', password)
    password2 = request.data.get('password2')
    if not username:
        return Response({'error': 'Tên đăng nhập không thê bỏ trống'})
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Tên đăng nhập đã tồn tại'})
    if not password or len(password) < 6:
        return Response({'error': 'Mật khẩu phải ít nhất 6 kí tự'})
    if password2 != password:
        return Response({'error': 'Mật khẩu xác thực không đúng'})
    User.objects.create_user(username=username, password=password)
    return Response({'success': True})

class CustomPermission(IsAuthenticated):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            return True
        return request.user.is_staff

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [CustomPermission]

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [CustomPermission]

@api_view(['POST'])
def orderProduct(request, pk):
    serializer = OrderInputSerializer(data=request.data)
    if serializer.is_valid():
        product = Product.objects.get(pk=pk)
        data = request.data # serializer.validated_data
        order = Order.objects.create(
            customerName=data['customerName'],
            customerPhone=data['customerPhone'],
            customerAddress=data['customerAddress'],
            total=int(data['qty']) * product.price,
            orderDate=datetime.now(),
            status='PENDING'
        )
        OrderItem.objects.create(
            order=order,
            product=product,
            priceUnit=product.price,
            qty=int(data['qty'])
        )
        return Response({'success': True})
    else:
        return Response(serializer.errors, status=400)
