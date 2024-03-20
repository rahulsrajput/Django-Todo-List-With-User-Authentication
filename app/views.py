from django.shortcuts import render
from .forms import loginForm, registerForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# Create your views here.
def loginUser(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    else:
        if request.method == 'POST':
            form = loginForm(request,data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user_obj = authenticate(username=uname, password=upass)
                if user_obj is not None:
                    login(request, user_obj)
                    return HttpResponseRedirect('/')
                
        form = loginForm()
    
    return render(request, 'login.html', context={'form':form})


def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/login')
    else:
        return HttpResponseRedirect('/login')
    

def registerUser(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    else:
        if request.method == 'POST':
            form = registerForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/login')
            
        form = registerForm()
    
    return render(request, 'register.html', context={'form':form})