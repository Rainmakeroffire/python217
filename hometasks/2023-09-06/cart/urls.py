from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart/<int:cart_item_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('delete_from_cart/<int:cart_item_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('orders/', views.orders, name='orders'),
    path('order_details/<int:order_id>/', views.order_details, name='order_details'),
    path('place_order/', views.place_order, name='place_order'),
    path('order_placed/<int:order_id>/', views.order_placed, name='order_placed'),
]
