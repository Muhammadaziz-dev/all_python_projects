from django.contrib.auth.models import User
from django.db import models

class Blog(models.Model):
    DoesNotExist = None
    objects = None
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.title