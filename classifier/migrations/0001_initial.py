# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-18 04:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('make', models.CharField(max_length=100)),
                ('car_model', models.CharField(max_length=150)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='InputImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
