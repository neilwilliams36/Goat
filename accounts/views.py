import sys
from django.contrib.auth import authenticate
from .authentication import PersonalAuthenticationBackend
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import redirect

# Create your views here.

def login(request):
    print('login view', file=sys.stderr)
    #user = PersonalAuthenticationBackend().authenticate(request.POST['assertion'])
    print(request.POST.get('assertion', False))
    user = authenticate(assertion = request.POST['assertion'])
    print('login view',user)
    if user is not None:
        auth_login(request, user)
    return redirect('/')

def logout(request):
    auth_logout(request)
    return redirect('/')
