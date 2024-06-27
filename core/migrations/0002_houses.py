# Generated by Django 4.2.13 on 2024-05-08 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staus', models.CharField(choices=[('liked', 'Liked'), ('viewed', 'Viewed'), ('dislike', 'Dislike'), ('maybe', 'Maybe')], max_length=20)),
                ('link', models.URLField()),
            ],
        ),
    ]
