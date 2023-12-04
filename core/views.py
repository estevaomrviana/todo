from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import Todo

#  Register new account
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# Rendering home page
@login_required
def index(request):
    todos = Todo.objects.filter(user=request.user).order_by('-id')
    return render(request, 'index.html', {'todos': todos})


# Creating a new Todo
@login_required
def create_todo(request):
    title = request.POST.get('title')
    todo = Todo.objects.create(title=title, user=request.user)
    todo.save()
    todos = Todo.objects.filter(user=request.user).order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})


# Marking completed True
@login_required
def mark_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = True
    todo.save()
    todos = Todo.objects.filter(user=request.user).order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})


# Deleting a Todo
@login_required
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    todos = Todo.objects.filter(user=request.user).order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})


