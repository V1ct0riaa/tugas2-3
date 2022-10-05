from django.shortcuts import render,redirect,get_object_or_404
from todolist.forms import TodolistForm
from todolist.models import TodoList
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime
from todolist.forms import TodolistForm



# Create your views here.
@login_required(login_url='login/')
def show_todolist(request):
    data_todolist = TodoList.objects.filter(user=request.user)
    context = {
    'todolist': data_todolist,
    }
    return render(request, "todolist.html",context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='login/')
def show_create_task(request):
    context= {}
    forms = TodolistForm(request.POST or None)
    if forms.is_valid() and request.method == 'POST':
        todolist = forms.save(commit=False)
        print(todolist)
        todolist.date = datetime.datetime.now()
        print(todolist.date)
        todolist.user = request.user
        print(todolist.user)
        todolist.save()
        return HttpResponseRedirect('/todolist')

    context['form'] = forms    
    return render(request, "createTask.html",context)

def finish_task(request,id):

    task = get_object_or_404(TodoList, id = id)
    task.is_finished = not task.is_finished
    task.save()

    return redirect('todolist:show_todolist')

def delete_task(request,id):

    task = get_object_or_404(TodoList, id = id)
    task.delete()

    return redirect('todolist:show_todolist')