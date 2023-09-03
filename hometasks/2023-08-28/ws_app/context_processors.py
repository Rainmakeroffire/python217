from .models import NavbarItem
from cart.models import CartItem


def navbar_items(request):
    items = NavbarItem.objects.all()
    return {'navbar_items': items}


def cart_items(request):
    if request.user.is_authenticated:
        total_items = CartItem.objects.filter(user=request.user).count()
    else:
        total_items = 0

    return {'total_items': total_items}
