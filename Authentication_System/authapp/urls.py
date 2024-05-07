from django.urls import path
from authapp.views import home,login_req,signup,logout_req,edit_profile,change_pass,profile

urlpatterns = [
    path("", home, name="home"),
    path('login/', login_req, name="login"),
    path('signup/', signup, name="signup"),
    path('logout/', logout_req, name="logout"),
    path('edit_profile/', edit_profile, name="edit_profile"),
    path('reset_password/', change_pass, name="change_pass"),
    path('profile/', profile, name="profile"),
]