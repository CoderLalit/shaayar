from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username