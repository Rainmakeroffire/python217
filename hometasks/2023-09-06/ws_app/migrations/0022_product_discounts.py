# Generated by Django 4.2.4 on 2023-09-08 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ws_app', '0021_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discounts',
            field=models.ManyToManyField(blank=True, to='ws_app.discount'),
        ),
    ]
