# Generated by Django 4.2.13 on 2024-05-08 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_house_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image',
            field=models.ManyToManyField(blank=True, null=True, to='core.image'),
        ),
    ]
