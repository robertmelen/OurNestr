# Generated by Django 4.2.13 on 2024-05-18 21:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_rename_address_house_postcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='ordering_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
