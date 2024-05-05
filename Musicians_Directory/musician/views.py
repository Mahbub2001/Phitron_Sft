from django.shortcuts import render, redirect
from .models import Musician
from album.models import Album
from .forms import ad_mus, ed_mus

def home(request):
    albums = Album.objects.all()
    return render(request, 'home.html', {"albums": albums})

def add_musician(request):
    if request.method == "POST":
        form = ad_mus(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ad_mus()
    return render(request, 'addMusician.html', {"form": form})

def edit_musician(request, id):
    musician = Musician.objects.get(id=id)
    if request.method == "POST":
        form = ed_mus(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ed_mus(instance=musician)
    return render(request, 'addMusician.html', {"form": form})

def delete_musician(request, id):
    musician = Musician.objects.get(id=id)
    musician.delete()
    return redirect("homepage")
