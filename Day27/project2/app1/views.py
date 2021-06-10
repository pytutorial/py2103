from django.shortcuts import render, HttpResponse

# 127.0.0.1:8000/app1/hello
def hello(request):
    name = request.GET.get('name', '')
    return HttpResponse("Hello " + name)
