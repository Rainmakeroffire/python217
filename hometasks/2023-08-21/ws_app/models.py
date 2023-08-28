from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class NavbarItem(models.Model):
    name = models.CharField(max_length=100)
    url_name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(99999)])
    image = models.ImageField(null=True, blank=True, upload_to="ws_app/%Y/%m/%d", default='default.jpg')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name
