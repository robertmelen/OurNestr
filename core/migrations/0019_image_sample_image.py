# Generated by Django 4.2.13 on 2024-05-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_house_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='sample_image',
            field=models.ImageField(default='media/image_uploads/Old_Road_006.JPG', upload_to='media/image_uploads'),
        ),
    ]
