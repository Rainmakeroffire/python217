from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Favorite, Comparison
from ws_app.models import Product
from ws_app.utils import search_engine
from ws_app.forms import ProfileForm
from cart.models import CartItem
from django.contrib.auth.decorators import login_required
from ws_app.utils import get_discounted_price


@login_required
def user_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    context = search_engine(request)
    context.update({'profile': profile})
    return render(request, 'user/profile.html', context)


@login_required
def edit_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    context = search_engine(request)
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        try:
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('user_profile', pk=profile.pk)
        except ValueError:
            context.update({'profile': profile, 'form': form, 'error': 'Incorrect data'})
            return render(request, 'edit_profile.html', context)
    context.update({'profile': profile, 'form': form})
    return render(request, 'user/edit_profile.html', context)


@login_required
def delete_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('index')


@login_required
def favorites(request):
    user = request.user
    favorites = Favorite.objects.filter(user=user)
    context = search_engine(request)
    cart_items = CartItem.objects.filter(user=request.user)
    product_ids_in_cart = cart_items.values_list('product__id', flat=True)
    context.update({
        'favorites': favorites,
        'cart_items': cart_items,
        'product_ids_in_cart': product_ids_in_cart
    })
    return render(request, 'user/favorites.html', context)


@login_required
def add_to_favorites(request, product_id):
    product = Product.objects.get(id=product_id)
    user = request.user

    if not Favorite.objects.filter(user=user, product=product).exists():
        Favorite.objects.create(user=user, product=product)

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def remove_from_favorites(request, product_id):
    product = Product.objects.get(id=product_id)
    user = request.user

    favorite = Favorite.objects.filter(user=user, product=product).first()

    if favorite:
        favorite.delete()

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def comparison(request):
    user = request.user
    compared_products = Comparison.objects.filter(user=user).values_list('product', flat=True)
    products = Product.objects.filter(pk__in=compared_products)
    for product in products:
        get_discounted_price(product)

    context = search_engine(request)
    context['compared_products'] = products
    return render(request, 'user/comparison.html', context)


@login_required
def add_to_comparison(request, product_id):
    user = request.user
    product = get_object_or_404(Product, pk=product_id)

    comparison_count = Comparison.objects.filter(user=user).count()

    if comparison_count >= 4:
        return redirect(request.META.get('HTTP_REFERER', '/'))

    if not Comparison.objects.filter(user=user, product=product).exists():
        Comparison.objects.create(user=user, product=product)

    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def remove_from_comparison(request, product_id):
    user = request.user
    product = get_object_or_404(Product, pk=product_id)

    Comparison.objects.filter(user=user, product=product).delete()

    return redirect(request.META.get('HTTP_REFERER', '/'))
