# Generated by Django 4.0.5 on 2022-07-08 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliveryoptions',
            old_name='delivery_method',
            new_name='method',
        ),
        migrations.RenameField(
            model_name='deliveryoptions',
            old_name='delivery_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='deliveryoptions',
            old_name='delivery_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='deliveryoptions',
            old_name='delivery_timeframe',
            new_name='timeframe',
        ),
        migrations.RenameField(
            model_name='deliveryoptions',
            old_name='delivery_window',
            new_name='window',
        ),
    ]
