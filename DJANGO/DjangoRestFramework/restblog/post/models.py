from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) # ilk parametre ne ile foreignleyeceğimiz
    title = models.CharField(max_length=120)
    content = models.TextField()