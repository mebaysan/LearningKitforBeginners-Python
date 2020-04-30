from django.db import models
from post.models import Post
from django.contrib.auth.models import User


class Favourite(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='favoriler')
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='favoriler')
    content = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Favori'
        verbose_name_plural = 'Favoriler'

    def __str__(self):
        return f"{self.post.title} - {self.user.username}"
