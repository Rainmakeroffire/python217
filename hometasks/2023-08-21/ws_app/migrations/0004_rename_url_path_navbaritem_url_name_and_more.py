# Generated by Django 4.2.4 on 2023-08-26 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ws_app', '0003_navbaritem_url_path_alter_navbaritem_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='navbaritem',
            old_name='url_path',
            new_name='url_name',
        ),
        migrations.RemoveField(
            model_name='navbaritem',
            name='url',
        ),
    ]
