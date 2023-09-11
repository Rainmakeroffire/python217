from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class NavbarItem(models.Model):
    name = models.CharField(max_length=100)
    url_name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Rating(models.Model):
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.value)


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title


class Discount(models.Model):
    name = models.CharField(max_length=100)
    ratio = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    products = models.ManyToManyField('Product', blank=True)
    manufacturers = models.ManyToManyField(Manufacturer, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    ratings = models.ManyToManyField(Rating, blank=True)

    def __str__(self):
        return f'{self.name}: {int(self.ratio * 100)}%'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(99999)])
    image = models.ImageField(null=True, blank=True, upload_to="ws_app/%Y/%m/%d", default='default.jpg')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    categories = models.ManyToManyField('Category', blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)
    characteristics = models.TextField(null=True, blank=True, default='{}')
    discounts = models.ManyToManyField(Discount, blank=True)

    def __str__(self):
        return self.name



