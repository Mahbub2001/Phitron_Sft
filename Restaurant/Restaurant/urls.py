from django.contrib import admin
from django.urls import path
from meal.views import home,show_meals
from about_us.views import  about_us

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home') ,
    path('show_meal/',show_meals,name='meals'),
    path('about_us/',about_us,name='about_us'),
]
