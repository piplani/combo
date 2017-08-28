# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class data(models.Model):
    file = models.FileField()
    email = models.EmailField()
    lowerlimit = models.IntegerField(default=0)
    upperlimit = models.IntegerField(default=0)
