from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Product
from user.models import Profile


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'image', 'rating', 'categories', 'manufacturer']
        widgets = {
            'categories': CheckboxSelectMultiple()
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_image', 'shipping_address']
