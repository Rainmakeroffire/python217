# Generated by Django 4.2.4 on 2023-08-31 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ws_app', '0008_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, to='ws_app.category'),
        ),
    ]
