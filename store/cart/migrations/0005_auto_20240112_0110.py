# Generated by Django 3.2.22 on 2024-01-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_auto_20240112_0108'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='orders',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orders',
            name='order_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='payment_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='orders',
            name='payment_signature',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
