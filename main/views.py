from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo, TodoItem
from .forms import TodoForm, UserCreate
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(req):
    try:
        user = req.user
        todos = Todo.objects.all().filter(user= user).order_by('-created_at')
    except:
        return redirect('/signin')

    query = req.GET.get('q')
    if query:
        todos = Todo.objects.filter(name__icontains=query)
    context = {
        'todos': todos
        }
    
    return render(req, 'home.html', context)

def completed(req):
    try:
        user = req.user
        todos = Todo.objects.all().filter(user= user, is_Completed = True).order_by('-created_at')
    except:
        return redirect('/signin')
    query = req.GET.get('q')
    if query:
        todos = todos.filter(name__icontains=query)
    context = {
        'todos': todos
        }
    return render(req, 'home.html', context)


def details(req,id):

    todo = Todo.objects.get(id = id)
    todo_items = todo.todoitem_set.all()
    context = {
        "todo": todo,
        "items": todo_items
    }
    return render(req, 'details.html',context)

def create(req):
    form = TodoForm(initial={'user': req.user})
    if req.method == 'POST':
        form = TodoForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context= {
        'form': form,
    }
    return render(req, 'create.html',context)

def update(req, id):
    todo = Todo.objects.get(id=id)
    form = TodoForm(instance=todo)
    if req.method == 'POST':
        form = TodoForm(req.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    context= {
        'form': form,
    }
    return render(req, 'update.html',context)    

def delete(req, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/') 

def signup(req):
    form = UserCreate()
    if req.method == 'POST':
        form = UserCreate(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/signin')
    context = {
        "form" : form,
    }
    return render(req, 'signup.html', context)

def signin(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username = username, password = password)
        if user is not None:
            login(req, user)
            return redirect('/')
    context={

    }
    return render(req, 'signin.html' , context)

def signout(req):
    logout(req)
    return  redirect('/signin')
