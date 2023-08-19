from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from .models import Work


def index(request):
    work = Work.objects.all()
    return render(request, 'index.html', {'works': work})


def signup_user(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': CustomUserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                login(request, user)
                return redirect('index')
            except IntegrityError:
                return render(request, 'signup.html', {'form': CustomUserCreationForm(),
                                                       'error': 'User already exists'})
        else:
            return render(request, 'signup.html', {'form': CustomUserCreationForm(),
                                                   'error': 'Passwords do not match'})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'login.html',
                          {'form': AuthenticationForm(), 'error': 'Invalid credentials'})
        else:
            login(request, user)
            return redirect('index')


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
