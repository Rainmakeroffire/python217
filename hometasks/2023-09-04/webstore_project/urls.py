"""webstore_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from ws_app.views import index, about, product, testimonial, contact, signup_user, login_user, logout_user, \
    add_content, view_items, update_item, delete_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('product/', product, name='product'),
    path('testimonial/', testimonial, name='testimonial'),
    path('contact/', contact, name='contact'),

    path('signup/', signup_user, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_content/', add_content, name='add_content'),
    path('view_items/', view_items, name='view_items'),
    path('update_item/<int:item_id>/', update_item, name='update_item'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),

    path('cart/', include('cart.urls')),
    path('user/', include('user.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
