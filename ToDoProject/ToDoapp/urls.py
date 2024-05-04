from django.urls import path
from .views import home
from django.conf import settings
from django.conf.urls.static import static
from .views import delete_todo

urlpatterns = [
    path('', home, name="home"),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
