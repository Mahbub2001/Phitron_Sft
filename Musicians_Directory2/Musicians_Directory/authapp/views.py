from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import RegistrationForm, EditProfileForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('login')

def login_req(request):
    if not request.user.is_authenticated:
        form = AuthenticationForm()
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Log in successfully")
                    return redirect('profile')
        return render(request, 'login.html', {"form": form})
    else:
        return redirect('home')
    
def logout_req(request):
    logout(request)
    messages.success(request, "Log out successfully!")
    return redirect('home')

def signup(request):
    if not request.user.is_authenticated:
        form = RegistrationForm()
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully!')
                return redirect('profile')
        return render(request, 'signup.html', {"form": form})
    else:
        return redirect('profile')

def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user) 
            messages.success(request, "Password changed.")
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_pass.html', {'form': form})

def edit_profile(request):
    if request.user.is_authenticated:
        form = EditProfileForm(instance=request.user)
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('profile')
        return render(request, 'edit_profile.html', {"form": form})
    else:
        return redirect('login')
