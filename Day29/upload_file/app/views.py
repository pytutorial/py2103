from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage()
# Create your views here.
def upload(request):
    file = request.FILES.get('image')
    if file != None and file.name != '':
        file_path = 'static/' + file.name 
        saved_path = fs.save(file_path, file)
        print(saved_path)
        return HttpResponse(f'<a href="/{saved_path}">{file.name}</a>')
    else:
        return HttpResponse('No file upload')
        
def index(request):
    return render(request, 'index.html')
