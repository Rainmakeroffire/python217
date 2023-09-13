# Generated by Django 4.2.4 on 2023-09-11 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_order_cart_items_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='applied_discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='order',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
