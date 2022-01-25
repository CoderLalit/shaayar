from django.db import models

# Create your models here.
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    poem_id = models.IntegerField()
    user_commented = models.CharField(max_length=50)
    comment_content = models.CharField(max_length=200)
    comment_date = models.DateField(auto_now_add=True)