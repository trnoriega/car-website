import os

from django.conf import settings
from django.db import models

class Car(models.Model):
    label = models.CharField(max_length=400, default='')

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
