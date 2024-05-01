
from django.contrib import admin
from django.urls import path
from meals.views import meals

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', meals)
]
