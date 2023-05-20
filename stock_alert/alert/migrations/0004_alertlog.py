# Generated by Django 4.1.7 on 2023-05-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0003_rename_current_price_stockalert_alert_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('symbol', models.CharField(max_length=10)),
                ('alert_price', models.FloatField(max_length=10)),
            ],
        ),
    ]
