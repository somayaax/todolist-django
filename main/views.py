from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo, TodoItem
from .forms import TodoForm
# Create your views here.


def home(req):
    todos = Todo.objects.all().order_by('-created_at')
    query = req.GET.get('q')
    if query:
        todos = Todo.objects.filter(name__icontains=query)
    context = {
        'todos': todos
        }
    
    return render(req, 'home.html', context)

def completed(req):
    todos = Todo.objects.all().order_by('-created_at')
    todos = todos.filter(is_Completed=True)
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
    form = TodoForm()
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
