# Generated by Django 4.1.7 on 2023-04-13 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0002_stockalert'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stockalert',
            old_name='current_price',
            new_name='alert_price',
        ),
    ]
