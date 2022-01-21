from django.db import models
from django.contrib.auth.models import auth


# Create your models here.
class Poem(models.Model):
    poemID = models.AutoField(primary_key=True)
    lang = models.CharField(max_length=15)
    publish_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)