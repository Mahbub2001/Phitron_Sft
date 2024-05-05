from django.shortcuts import render, redirect
from .models import Album
from .forms import ADD_Album, Edit_Album

def addAlbum(request):
    form = ADD_Album(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('homepage')
    return render(request, 'addAlbum.html', {'form': form})

def editAlbum(request, id):
    album = Album.objects.get(id=id)
    form = Edit_Album(request.POST or None, instance=album)
    if form.is_valid():
        form.save()
        return redirect('homepage')
    return render(request, 'addAlbum.html', {'form': form})
