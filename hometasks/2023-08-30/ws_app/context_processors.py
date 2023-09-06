from .models import NavbarItem
from cart.models import CartItem
from user.models import Profile
from django.contrib.auth.models import User


def navbar_items(request):
    items = NavbarItem.objects.all()
    return {'navbar_items': items}


def cart_items(request):
    if request.user.is_authenticated:
        total_items = CartItem.objects.filter(user=request.user).count()
    else:
        total_items = 0

    return {'total_items': total_items}


def profile_image(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            return {'profile_image': profile.profile_image.url}
        except Profile.DoesNotExist:
            pass
    return {'profile_image': '/static/profiles/user-default.png'}