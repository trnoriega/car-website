import os

from django.conf import settings
from django.db import models

BODY_STYLE_CHOICES = (
        ('N/A', 'N/A'),
        ('SEDAN', 'SEDAN'),
        ('SUV', 'SUV'),
        ('PICKUP', 'PICKUP'),
        ('VAN', 'VAN'),
        ('MINIVAN', 'MINIVAN'),
        ('HATCHBACK', 'HATCHBACK'),
        ('CONVERTIBLE', 'CONVERTIBLE'),
        ('COUPE', 'COUPE'),
        ('WAGON', 'WAGON'),
    )

class Car(models.Model):
    label = models.CharField(max_length=200, default='')
    make = models.CharField(max_length=100, default='')
    model = models.CharField(max_length=150, default='')
    year = models.CharField(max_length=4, default='')
    body_style = models.CharField(max_length=15, choices=BODY_STYLE_CHOICES, default='N/A')
    url = models.URLField(max_length=400, default='https://www.autotrader.com/')

    class Meta:
        db_table = 'car'

    def __str__(self):
        return self.label

class InputImage(models.Model):
    # file will be saved to MEDIA_ROOT/uploads
    image = models.ImageField(upload_to='uploads/')
    predictions1 = models.CharField(max_length=200, default='')
    predictions2 = models.CharField(max_length=200, default='')
    predictions3 = models.CharField(max_length=200, default='')

    class Meta:
        db_table = 'input_image'
