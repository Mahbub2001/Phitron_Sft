from django.contrib import admin
from django.urls import path

from musician.views import addMusician,home,editMusician,deleteMusician
from album.views import addAlbum,editAlbum

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name = 'homepage'),
    path("addMusician/", addMusician, name = 'adMusician'),
    path('addAlbum/', addAlbum, name =  'adAlbum'),
    path("EditMusician/<int:id>/", editMusician, name = 'editMusician'),
    path("deleteMusician/<int:id>/", deleteMusician, name = 'deleteMusician'),
    path("editAlbum/<int:id>/", editAlbum, name = 'editAlbum'),
]
