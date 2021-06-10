#views.py
from django.shortcuts import HttpResponse

#127.0.0.1:8000?name=Nguyen+Van+A
def index(request):
    name = request.GET.get('name', '')
    return HttpResponse("Hello " + name)

# cd hello_prj
# dir --> confirm "manage.py" existed
# python manage.py runserver