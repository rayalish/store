# Generated by Django 3.2.22 on 2024-01-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20240112_0110'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='ordered_items',
            field=models.ManyToManyField(to='cart.CartItems'),
        ),
    ]