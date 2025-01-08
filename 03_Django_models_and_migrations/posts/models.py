
from django.db import models

# Create your models here.


class Post(models.Model):
    """Database schema definition for Posts"""
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
