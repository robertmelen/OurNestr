# Generated by Django 4.2.13 on 2024-05-12 23:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_house_image_house_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='media/image_uploads'),
        ),
    ]
