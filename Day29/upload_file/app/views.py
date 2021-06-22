from django.shortcuts import render, HttpResponse

# Create your views here.
def upload(request):
    file = request.FILES.get('image')
    if file != None and file.name != '':
        print(file.name)
        return HttpResponse('Uploaded')
    else:
        return HttpResponse('No file upload')
        
def index(request):
    return render(request, 'index.html')
