# Generated by Django 3.2.15 on 2023-05-16 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoApp', '0002_address_cart_category_duration_order_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]