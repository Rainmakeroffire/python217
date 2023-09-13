from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.db.models import Q
from .models import Discount, Product, Category


@receiver(post_save, sender=Discount)
def assign_discount(sender, instance, **kwargs):

    products_to_assign = Product.objects.filter(
        Q(manufacturer__in=instance.manufacturers.all()) |
        Q(categories__in=instance.categories.all()) |
        Q(rating__in=instance.ratings.all())
    )

    sale_category, _ = Category.objects.get_or_create(title='SALE')

    for product in products_to_assign:
        product.discounts.add(instance)

        product.categories.add(sale_category)


@receiver(pre_delete, sender=Discount)
def remove_discount(sender, instance, **kwargs):
    discounted_products = instance.product_set.all()
    sale_category, _ = Category.objects.get_or_create(title='SALE')

    for product in discounted_products:
        product.discounts.remove(instance)

        remaining_discounts = product.discounts.all()
        if not remaining_discounts:
            product.categories.remove(sale_category)
