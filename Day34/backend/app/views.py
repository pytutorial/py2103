from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product

@api_view(['GET'])
def hello(request):
    return Response({'message': 'Hello'})

@api_view(['GET'])
def getProductList(request):
    productList = Product.objects.all()
    results = []
    for p in productList:
        results.append({
            'id': p.id,
            'code': p.code,
            'name': p.name,
            'price': p.price,
            'image': p.image.url
        })
    return Response(results)