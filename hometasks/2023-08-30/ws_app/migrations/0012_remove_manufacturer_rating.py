# Generated by Django 4.2.4 on 2023-09-01 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ws_app', '0011_manufacturer_product_manufacturer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manufacturer',
            name='rating',
        ),
    ]