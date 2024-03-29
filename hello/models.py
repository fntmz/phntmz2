from django.db import models
# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    role = models.BigIntegerField()


class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    img = models.ImageField(upload_to="posts/", blank=True)
    description = models.CharField(max_length=1024)
    detail = models.CharField(max_length=32768)
    author = models.CharField(max_length=128)
    views = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.CharField(max_length=16)
    detail = models.CharField(max_length=1024)
    author_id = models.CharField(max_length=16)
    hidden = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ratings(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.CharField(max_length=16)
    author_id = models.CharField(max_length=16)
    rating = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    author_id = models.CharField(max_length=16, default="anonymous")
    mail = models.CharField(max_length=256, default="no mail")
    detail = models.CharField(max_length=1024)
    reviewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)