# Generated by Django 4.2.4 on 2023-08-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ws_app', '0002_auto_20230826_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbaritem',
            name='url_path',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='navbaritem',
            name='url',
            field=models.URLField(),
        ),
    ]
