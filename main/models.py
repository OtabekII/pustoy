from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    


class NewsImg(models.Model):
    img = models.ImageField(upload_to='news-img/')
    news = models.ForeignKey(News, on_delete=models.CASCADE)


class NewsVideo(models.Model):
    video = models.FileField(upload_to='news-video/')
    news = models.ForeignKey(News, on_delete=models.CASCADE)


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Athor(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


