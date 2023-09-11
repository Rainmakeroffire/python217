from django.db import models
from django.contrib.auth.models import User
from ws_app.models import Product
from django.utils import timezone


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    placed = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    applied_discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    STATUS_CHOICES = [
        ('new', 'New Order'),
        ('pending', 'Pending Payment'),
        ('shipping', 'Shipping'),
        ('complete', 'Complete'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    cart_items_info = models.TextField(blank=True, null=True)

    def __str__(self):
        date_local = self.placed.astimezone(timezone.get_current_timezone())
        date_formatted = date_local.strftime("%Y-%m-%d %H:%M:%S %p")
        return f"#{self.id:05d} - {self.user} - ${self.total_cost} - {date_formatted}"


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
