from django import template
import json
from user.models import Favorite, Comparison
from cart.models import CartItem
from django.utils import timezone


register = template.Library()


@register.filter
def get_star_range(value):
    return range(value)


@register.filter
def total_price(cart_items):
    total = sum(cart_item.subtotal for cart_item in cart_items)
    return f"{total:.2f}"


@register.filter(name='json_loads')
def json_loads(value):
    return json.loads(value)


@register.filter(name='filter_categories')
def filter_categories(products, category_id):
    return products.filter(categories__id=category_id)


@register.filter
def is_in_favorites(product, user):
    return Favorite.objects.filter(product=product, user=user).exists()


@register.filter
def is_in_comparison(product, user):
    return Comparison.objects.filter(product=product, user=user).exists()


@register.filter(name='get_json_key')
def get_json_key(json_string, key):
    data = json.loads(json_string)
    return data.get(key, '')


@register.filter
def is_in_cart(product, user):
    return CartItem.objects.filter(product=product, user=user).exists()


@register.filter
def get_discount_info(product):
    current_time = timezone.now()
    discounts = product.discounts.all()

    discount_info = {
        "discount_value": None,
        "valid_until": None,
        "valid_discount": None,
    }

    if discounts:
        valid_discounts = discounts.filter(end_date__gte=current_time)
        if valid_discounts.exists():
            valid_discount = max(valid_discounts, key=lambda d: d.ratio)
            discount_info["discount_value"] = int(valid_discount.ratio * 100)
            discount_info["valid_until"] = valid_discount.end_date.strftime('%d.%m')
            discount_info["valid_discount"] = valid_discount

    return discount_info


@register.filter
def has_valid_discount(product):
    return get_discount_info(product)["valid_discount"]
