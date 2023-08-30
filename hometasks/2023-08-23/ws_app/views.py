from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .forms import ProductForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Product
from django.contrib.auth.decorators import login_required, user_passes_test


def is_staff_user(user):
    return user.is_staff


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def about(request):
    return render(request, 'about.html')


def product(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})


def testimonial(request):
    return render(request, 'testimonial.html')


def contact(request):
    return render(request, 'contact.html')


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


@login_required
def logout_user(request):
    if request.method == 'GET':
        logout(request)
        return redirect('index')


@user_passes_test(is_staff_user)
def add_content(request):
    if request.method == 'POST':
        try:
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('add_content')
        except ValueError:
            return render(request, 'add_content.html', {'form': ProductForm(), 'error': 'Incorrect data'})
    else:
        form = ProductForm()
    return render(request, 'add_content.html', {'form': form})


@user_passes_test(is_staff_user)
def view_items(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return render(request, 'view_items.html', {'products': products})


@user_passes_test(is_staff_user)
def update_item(request, item_id):
    item = get_object_or_404(Product, pk=item_id)
    form = ProductForm(instance=item)
    if request.method == 'POST':
        try:
            form = ProductForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                return redirect('view_items')
        except ValueError:
            return render(request, 'update_item.html', {'item': item, 'form': form, 'error': 'Incorrect data'})

    return render(request, 'update_item.html', {'item': item, 'form': form})


@user_passes_test(is_staff_user)
def delete_item(request, item_id):
    item = get_object_or_404(Product, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('view_items')
