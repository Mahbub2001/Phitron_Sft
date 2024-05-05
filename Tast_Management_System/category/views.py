from django.shortcuts import render, redirect
from .forms import CategoryForm

def addCategory(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = CategoryForm()
    return render(request, 'addCategory.html', {"form": form})
