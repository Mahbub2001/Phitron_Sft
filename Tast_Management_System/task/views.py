from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def addTask(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = TaskForm()
    return render(request, 'addTask.html', {"form": form})

def editTask(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = TaskForm(instance=task)
    return render(request, 'editTask.html', {"form": form})

def deleteTask(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect("homepage")
