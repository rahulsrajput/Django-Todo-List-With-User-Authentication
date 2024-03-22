from django.shortcuts import render
from .forms import loginForm, registerForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import Task
from django.contrib import messages

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
                    messages.success(request, 'Logged In..')
                    return HttpResponseRedirect('/')
                
        form = loginForm()
    
    return render(request, 'login.html', context={'form':form})


def logoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged out..')
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
                messages.success(request, 'Account Created..')
                return HttpResponseRedirect('/login')
            
        form = registerForm()
    
    return render(request, 'register.html', context={'form':form})





def task_list(request):
    if request.user.is_authenticated:
        current_user = request.user
        
        if request.method == 'POST':
            search = request.POST['search']
            objs = Task.objects.filter(task__icontains = search, user=current_user)
        else:
            objs = Task.objects.filter(user=current_user)
        
        return render(request, 'task_list.html', context={'objs':objs})
    
    else:
        return HttpResponseRedirect('/login')
    

def task_add(request):
    page = 'add'

    if request.user.is_authenticated:
        if request.method == 'POST':
            task = request.POST['task']
            current_user = request.user
            Task(task=task, user=current_user).save()
            messages.success(request, 'Task Created..')
            return HttpResponseRedirect('/')
        

        return render(request, 'task_form.html', context={'page':page})
    else:
        return HttpResponseRedirect('/login')
    

def task_update(request,pk):
    page = 'update'
    if request.user.is_authenticated:
        obj = Task.objects.get(pk=pk)
        status = obj.complete

        if request.method == 'POST':
            task = request.POST['task']
            current_user = request.user
            
            # print(task,status)
            
            status = True if request.POST.get('checkbox') == 'on' else False
            
            Task(pk=pk, task=task, complete=status, user=current_user).save()
            messages.success(request, 'Task Updated...')
            return HttpResponseRedirect('/')
        
        return render(request, 'task_form.html', context={'page':page, 'obj':obj, 'status':status})
    else:
        return HttpResponseRedirect('/login')
  
    
def task_delete(request, pk):
    obj = Task.objects.get(pk=pk)
    obj.delete()
    messages.success(request, 'Task Deleted..')
    return HttpResponseRedirect('/')