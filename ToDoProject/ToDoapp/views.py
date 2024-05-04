from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TodoForm()

    todos = Todo.objects.all()
    context = {
        'form': form,
        'todos': todos
    }
    return render(request, 'home.html', context)


def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')