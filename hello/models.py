from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    role = models.BigIntegerField()


class Posts(models.Model):
    title = models.CharField(max_length=256)
    img = models.ImageField(upload_to="posts/", blank=True)
    description = models.CharField(max_length=1024)
    detail = models.CharField(max_length=32768)
    author = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    post_id = models.CharField(max_length=16)
    detail = models.CharField(max_length=1024)
    author_id = models.CharField(max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)