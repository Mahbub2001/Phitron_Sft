from django.urls import path
from task.views import home, addTask, editTask, deleteTask

urlpatterns = [
    path("", home, name='homepage'),
    path("addTask/", addTask, name='addTask'),
    path('editTask/<int:id>/', editTask, name='editTask'),
    path('deleteTask/<int:id>/', deleteTask, name='deleteTask'),
]
