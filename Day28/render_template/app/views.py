from django.shortcuts import render

PREFIX_URL = 'https://raw.githubusercontent.com/pytutorial/py2103/main/Day28/images'
# f'{{prefixUrl}}/{{p.code}}.jpg'
productList = [ 
    {'id': 1, 'code': 'IPX', 
        'name': 'IPhone', 'price': 10500000},

    {'id': 2, 'code': 'IP11', 
        'name': 'IPhone 11', 'price': 11500000},

    {'id': 3, 'code': 'IP12', 
    'name': 'IPhone 12', 'price': 12500000}
]

# Create your views here.
def index(request):
    context = {
        'productList': productList,
        'prefixUrl': PREFIX_URL
    }
    return render(request, 'index.html', context)
