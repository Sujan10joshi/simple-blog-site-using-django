from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    thumb = models.ImageField(upload_to="my_imgs", null=True)
