# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class PersonDescription(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    birthdate = models.DateField(auto_now=False)
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=24)
