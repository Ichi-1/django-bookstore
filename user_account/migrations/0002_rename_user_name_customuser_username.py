# Generated by Django 4.0.5 on 2022-06-24 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='user_name',
            new_name='username',
        ),
    ]