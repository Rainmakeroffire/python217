from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .forms import ProductForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Product
from django.contrib.auth.decorators import login_required, user_passes_test
from .utils import search_engine
from cart.models import CartItem


def is_staff_user(user):
    return user.is_staff


def index(request):
    context = search_engine(request)
    return render(request, 'index.html', context)


def about(request):
    context = search_engine(request)
    return render(request, 'about.html', context)


def product(request):
    context = search_engine(request)
    return render(request, 'product.html', context)


def testimonial(request):
    context = search_engine(request)
    return render(request, 'testimonial.html', context)


def contact(request):
    context = search_engine(request)
    return render(request, 'contact.html', context)


def signup_user(request):
    context = search_engine(request)
    if request.method == 'GET':
        context.update({'form': CustomUserCreationForm()})
        return render(request, 'signup.html', context)
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
                context.update({'form': CustomUserCreationForm(), 'error': 'User already exists'})
                return render(request, 'signup.html', context)
        else:
            context.update({'form': CustomUserCreationForm(), 'error': 'Passwords do not match'})
            return render(request, 'signup.html', context)


def login_user(request):
    context = search_engine(request)
    if request.method == 'GET':
        context.update({'form': AuthenticationForm()})
        return render(request, 'login.html', context)
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            context.update({'form': AuthenticationForm(), 'error': 'Invalid credentials'})
            return render(request, 'login.html', context)
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
    context = search_engine(request)
    if request.method == 'POST':
        try:
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('add_content')
        except ValueError:
            context.update({'form': ProductForm(), 'error': 'Incorrect data'})
            return render(request, 'add_content.html', context)
    else:
        form = ProductForm()
    context.update({'form': form})
    return render(request, 'add_content.html', context)


@user_passes_test(is_staff_user)
def view_items(request):
    context = search_engine(request)
    if request.method == 'GET':
        return render(request, 'view_items.html', context)


@user_passes_test(is_staff_user)
def update_item(request, item_id):
    context = search_engine(request)
    item = get_object_or_404(Product, pk=item_id)
    form = ProductForm(instance=item)
    if request.method == 'POST':
        try:
            form = ProductForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                return redirect('view_items')
        except ValueError:
            context.update({'item': item, 'form': form, 'error': 'Incorrect data'})
            return render(request, 'update_item.html', context)
    context.update({'item': item, 'form': form})
    return render(request, 'update_item.html', context)


@user_passes_test(is_staff_user)
def delete_item(request, item_id):
    item = get_object_or_404(Product, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('view_items')
