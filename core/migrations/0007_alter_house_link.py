# Generated by Django 4.2.13 on 2024-05-08 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_image_house_house_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
