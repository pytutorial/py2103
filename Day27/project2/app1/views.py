from django.shortcuts import redirect, render

# 127.0.0.1:8000/app1/hello
def hello(request):
    #name = request.GET.get('name', '')
    name = request.session.get('username', '')
    return render(request, 'hello.html', 
                    {'name': name}) 

# 127.0.0.1:8000/app1/login
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:  #POST
        username = request.POST['username']
        password = request.POST['password']
        #TODO: Validate username/password
        request.session['username'] = username
        return redirect('/app1/hello')

# 127.0.0.1:8000/app1/send-mail
def sendMail(request):
    if request.method == 'GET':
        return render(request, 'email_form.html')
    else:
        email = request.session.get('username','')
        title = request.POST['title']
        content = request.POST['content']
        print(email, title, content)
        return render(request, 'success.html',
                    {'username': email})