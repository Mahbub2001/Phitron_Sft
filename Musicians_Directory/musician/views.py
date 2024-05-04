from django.shortcuts import render, redirect
from .models import Musician
from album.models import Album
from .forms import ADD_Musician, Edit_Musician

def home(request):
    albums = Album.objects.all()
    return render(request, 'home.html', {"albums": albums})

def addMusician(request):
    if request.method == "POST":
        form = ADD_Musician(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ADD_Musician()
    return render(request, 'addMusician.html', {"form": form})

def editMusician(request, id):
    musician = Musician.objects.get(id=id)
    if request.method == "POST":
        form = Edit_Musician(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = Edit_Musician(instance=musician)
    return render(request, 'addMusician.html', {"form": form})

def deleteMusician(request, id):
    musician = Musician.objects.get(id=id)
    musician.delete()
    return redirect("homepage")
