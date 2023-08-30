from .models import NavbarItem


def navbar_items(request):
    items = NavbarItem.objects.all()
    return {'navbar_items': items}
