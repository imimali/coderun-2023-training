from django.db import models


# Create your models here.

class Book(models.Model):
    author = models.CharField(max_length=100, default=None)
    title = models.CharField(max_length=200,default=None)
