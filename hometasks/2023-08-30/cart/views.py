from django.shortcuts import render, redirect, get_object_or_404, reverse
from ws_app.models import Product
from .models import CartItem, Order
from django.contrib.auth.decorators import login_required
from django.db import transaction
import json
from ws_app.utils import search_engine


@login_required
def cart(request):
    context = search_engine(request)
    cart_items = CartItem.objects.filter(user=request.user)
    if request.method == 'POST':
        action = request.POST.get('action', None)
        if action == 'checkout':
            for cart_item in cart_items:
                new_quantity = int(request.POST.get(f'quantity_{cart_item.id}', 0))
                if new_quantity > 0:
                    cart_item.quantity = new_quantity
                    cart_item.save()
                else:
                    cart_item.delete()
            return redirect('checkout')
        if action == 'save':
            for cart_item in cart_items:
                new_quantity = int(request.POST.get(f'quantity_{cart_item.id}', 0))
                if new_quantity > 0:
                    cart_item.quantity = new_quantity
                    cart_item.save()
                else:
                    cart_item.delete()
    for cart_item in cart_items:
        cart_item.subtotal = cart_item.product.price * cart_item.quantity
    context.update({'cart_items': cart_items})
    return render(request, 'cart/cart.html', context)


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart')


@login_required
def checkout(request):
    context = search_engine(request)
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items:
        return redirect('cart')
    for cart_item in cart_items:
        cart_item.subtotal = cart_item.product.price * cart_item.quantity
    context.update({'cart_items': cart_items})
    return render(request, 'cart/checkout.html', context)


@login_required
def delete_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id, user=request.user)
    if request.method == 'GET':
        cart_item.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def orders(request):
    context = search_engine(request)
    user_orders = Order.objects.filter(user=request.user).order_by('-placed')
    context.update({'user_orders': user_orders})
    return render(request, 'cart/orders.html', context)


@login_required
def order_details(request, order_id):
    context = search_engine(request)
    order = get_object_or_404(Order, pk=order_id, user=request.user)
    if request.method == 'POST':
        if 'cancel_order' in request.POST:
            order.status = 'cancelled'
            order.save()
            return redirect('orders')
    context.update({'order': order})
    return render(request, 'cart/order_details.html', context)


@login_required
@transaction.atomic
def place_order(request):
    context = search_engine(request)
    cart_items = CartItem.objects.filter(user=request.user)
    total_cost = sum(cart_item.product.price * cart_item.quantity for cart_item in cart_items)

    if request.method == 'POST':
        order = Order.objects.create(user=request.user, cost=total_cost)
        cart_items_info = []

        for cart_item in cart_items:
            cart_item.order = order
            cart_item.save()
            cart_items_info.append({
                'product_name': cart_item.product.name,
                'product_price': cart_item.product.price,
                'quantity': cart_item.quantity,
            })

        order.cart_items_info = json.dumps(cart_items_info)
        order.save()

        cart_items.delete()
        order_number = f"#{order.id:05d}"
        context.update({'order_number': order_number})
        return render(request, 'cart/order_placed.html', context)

    return redirect('checkout')

