from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Product


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'rating']