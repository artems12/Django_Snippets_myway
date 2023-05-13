from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)


class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(#тут юзера добавь потом, on_delete=models.CASCADE)

    def _str_(self):
         return self.title





