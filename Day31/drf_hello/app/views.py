#app/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view

#http://127.0.0.1:8000/api/hello?name=Nguyen+Van+A
@api_view(['GET'])
def hello(request):
    name = request.GET.get('name', '')
    return Response({'message': f'Hello {name}'})

@api_view(['POST'])
def login(request):  #  http:/127.0.0.1:8000/api/login
    username = request.data.GET('username', '')
    password = request.data.GET('password', '')

    if username != 'admin':
        return Response({'error': 'Tên đăng nhập không tồn tại'})
    
    if password != '1234':
        return Response({'error': 'Mật khẩu không chính xác'})

    return Response({'success': True})
