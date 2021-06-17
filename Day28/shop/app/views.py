from django.shortcuts import render

# Create your views here.

productList = [ 
    {
        'id':1, 'code': 'ACER_0001', 'name': 'Acer 0001', 'price': 10.5,
        'category': {'id': 1, 'name': 'Acer'}
    },
    {
        'id':2, 'code': 'ACER_0002', 'name': 'Acer 0002', 'price': 11.5,
        'category': {'id': 1, 'name': 'Acer'}
    },
    {
        'id':3, 'code': 'ACER_0003', 'name': 'Acer 0003', 'price': 12.5,
        'category': {'id': 1, 'name': 'Acer'}
    },

    {
        'id':4, 'code': 'ASUS_0001', 'name': 'Asus 0001', 'price': 11,
        'category': {'id': 2, 'name': 'Asus'}
    },
    {
        'id':5, 'code': 'ASUS_0002', 'name': 'Asus 0002', 'price': 12,
        'category': {'id': 2, 'name': 'Asus'}
    },
    {
        'id':6, 'code': 'ASUS_0003', 'name': 'Asus 0003', 'price': 13,
        'category': {'id': 2, 'name': 'Asus'}
    }
]

PREFIX_URL = 'https://raw.githubusercontent.com/pytutorial/sample_projects/master/shop/static/images'

def index(request):
    context = {
        'prefixUrl': PREFIX_URL,
        'productList': productList
    }

    return render(request, 'index.html', context)

def viewProduct(request, id):
    product = productList[int(id)-1]

    context = {
        'prefixUrl': PREFIX_URL,
        'product': product
    }

    return render(request, 'detail.html', context)