# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class PersonDescription(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    birthdate = models.DateField(auto_now=False)
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(unique=True)
    jabber = models.CharField(max_length=32)
    skype = models.CharField(max_length=32)
    other_contacts = models.TextField(null=True, blank=True)
