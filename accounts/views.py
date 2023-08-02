from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login as base_login, logout as base_logout

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)
        if user is not None:
            base_login(request, user)
    
    return render(request, 'login.html')


def logout(request):
    base_logout(request)
    return HttpResponseRedirect('/login')