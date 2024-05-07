from django.contrib import admin
from django.urls import path,include

from musician.views import add_musician,home,edit_musician,delete_musician
from album.views import addAlbum,editAlbum

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name = 'homepage'),
    path("addMusician/", add_musician, name = 'adMusician'),
    path('addAlbum/', addAlbum, name =  'adAlbum'),
    path("EditMusician/<int:id>/", edit_musician, name = 'editMusician'),
    path("deleteMusician/<int:id>/", delete_musician, name = 'deleteMusician'),
    path("editAlbum/<int:id>/", editAlbum, name = 'editAlbum'),
    path("", include("authapp.urls")),
]
