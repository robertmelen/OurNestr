from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    pass

class Image(models.Model):
    image = models.ImageField(upload_to='media/image_uploads')
    sample_image = models.ImageField(upload_to='media/image_uploads', default='media/image_uploads/DJI_0062.JPG')

    def __str__(self):
        return self.image.name
    
#class to represent a House which can be added to liked houses
class House(models.Model):
    HOUSE_STATUS_STATUS = (
        ('liked', 'Liked'),
        ('dislike', 'Dislike'),
        ('maybe', 'Maybe'),
        ('viewed', 'Viewed'),
        ('offered', 'Offered'),
    )
    name = models.CharField(max_length=100, unique=True, blank=True, null=True, help_text="name of house, this can be anything unique")
    postcode = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=HOUSE_STATUS_STATUS)
    images = models.ManyToManyField(Image, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=1000, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    ordering_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    

    def __str__(self):
        return self.name
    

    
    

    
