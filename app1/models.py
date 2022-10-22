from django.db import models

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=100)
    info  = models.CharField(max_length=100, default='')

class City(models.Model):

    name = models.CharField(max_length=100)
