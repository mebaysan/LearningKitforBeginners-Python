from django.db import models
from django.contrib.auth.models import User


class Manager(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    ip = models.TextField(default='')
    country = models.TextField(default='')
    def __str__(self):
        return self.name
