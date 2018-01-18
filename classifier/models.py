import os

from django.conf import settings
from django.db import models

class Car(models.Model):
    label = models.CharField(max_length=200)
    make = models.CharField(max_length=100)
    car_model = models.CharField(max_length=150)
    year = models.CharField(max_length=4)
    path = FilePathField(path=os.path.join(settings.MEDIA_DIR, 'results'))
    def __str__(self):
        return self.label

class InputImage(models.Model):
    # file will be saved to MEDIA_ROOT/uploads
    upload = models.ImageField(upload_to='uploads/')
