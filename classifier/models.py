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

def url_maker(car_instance):
    """
    Generates a custom autotrader url based on
    car instance provided
    """
    year = car_instance.year
    key_words = ''
    split_model = car_instance.model.split(' ')
    if len(split_model) > 1:
        key_words = '+'.join(split_model[1:])
        # print(key_words)
        model = split_model[0]
    else:
        model = split_model[0]
    split_make = car_instance.make.split(' ')
    if len(split_make) > 1:
        make = '+'.join(split_make)
    else:
        make = split_make[0]
    body = car_instance.body_style
    if body == 'N/A':
        body = ''
    key_words = key_words + '+' + body
    url = 'https://www.autotrader.com/cars-for-sale/'+\
    '{}/{}/{}/zip=?&keywordPhrases={}'.format(
        year,
        make,
        model,
        key_words,
    )
    return url


class Car(models.Model):
    label = models.CharField(max_length=200, default='')
    make = models.CharField(max_length=100, default='')
    model = models.CharField(max_length=150, default='')
    year = models.CharField(max_length=4, default='')
    body_style = models.CharField(max_length=15, choices=BODY_STYLE_CHOICES, default='N/A')
    url = models.URLField(max_length=400)

    def save(self, *args, **kwargs):
        self.url = url_maker(self)
        super(Car, self).save(*args, **kwargs)

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
