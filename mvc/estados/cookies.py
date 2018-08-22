from django.shortcuts import render
from .sessions import FormLogin


def cookies_demo(request):
    username = None  # default value
    form_login = FormLogin()
    if request.method == 'GET':
        if 'action' in request.GET:
            action = request.GET.get('action')
            if action == 'logout':
                if request.COOKIES.has_key('username'):
                    request.COOKIES.flush()
                return redirect('demos-sessions')
 
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
            print("GET:Usuario:" + request.COOKIES['username'])
           # datetime.datetime object which represents the moment in time at which the session will expire
 
    elif request.method == 'POST':
        form_login = FormLogin(request.POST)
        if form_login.is_valid():
            username = form_login.cleaned_data['username']
            password = form_login.cleaned_data['password']
            if username.strip() == 'leandre96' and password.strip() == 'avatar12':
                request.COOKIES['username'] = username
            else:
                username = None
    response = render(request, 'cookies.html', {
        'demo_title': 'Cookies in Django',
        'form': form_login,
        })
    response.set_cookie('username',username)
    
    return response
        
