from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:pk>', views.user_profile, name='user_profile'),
    path('edit_profile/<str:pk>', views.edit_profile, name='edit_profile'),
    path('delete_profile/<str:pk>', views.delete_profile, name='delete_profile'),
    path('favorites/', views.favorites, name='favorites'),
    path('add_to_favorites/<int:product_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<int:product_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('comparison/', views.comparison, name='comparison'),
    path('add_to_comparison/<int:product_id>/', views.add_to_comparison, name='add_to_comparison'),
    path('remove_from_comparison/<int:product_id>/', views.remove_from_comparison, name='remove_from_comparison'),
]

