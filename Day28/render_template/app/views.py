from django.shortcuts import render

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
        'productList': productList
    }
    return render(request, 'index.html', context)
