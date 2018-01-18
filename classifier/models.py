from django.db import models

class Car(models.Model):
    label = models.CharField(max_length=200)
    make = model.CharField(max_length=100)
    model = model.CharField(max_length=150)
    year = model.CharField(max_length=4)

class InputImage(models.Model):
    # file will be saved to MEDIA_ROOT/uploads
    upload = models.ImageField(upload_to='uploads/')

