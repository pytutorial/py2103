import json
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

def helloAPI(request):
    data = {'message': 'Hello'}
    return HttpResponse(json.dumps(data), content_type='application/json')

#127.0.0.1:8000
def index(request):
    return render(request, 'index.html')

def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print('username=', username, 'password=', password)
    if username != 'admin':
        error = 'Tên đăng nhập không tồn tại'
    elif password != '1234':
        error = 'Mật khẩu không đúng'
    else:
        error = ''
    result = json.dumps({'error': error})
    return HttpResponse(result, 
        content_type='application/json')

todoList = [
    'Viết báo cáo doanh thu quý 2',
    'Đi tiếp khách cùng sếp',
]

def getTodos(request):
    result = json.dumps(todoList)
    return HttpResponse(result, 
        content_type='application/json')

def addTodo(request):
    todo = request.POST.get('todo')
    todoList.append(todo)
    result = json.dumps({'success': True})
    return HttpResponse(result, 
        content_type='application/json')
