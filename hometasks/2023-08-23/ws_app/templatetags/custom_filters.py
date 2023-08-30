from django import template
import json

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
