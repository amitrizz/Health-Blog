from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=75)
    body=models.TextField()
    slug=models.SlugField(unique=True)
    isvarify=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)
    banner=models.ImageField(default='fallback.png',blank=True)
    # delete all post if user is not exist in database
    author=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

class Comments(models.Model):
    post_slug = models.ForeignKey(Post, on_delete=models.CASCADE,default=None)
    user = models.CharField(max_length=150)
    date=models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

