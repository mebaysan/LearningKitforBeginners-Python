from django.db import models
from news.models import News


class Comment(models.Model):
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    txt = models.TextField()
    is_published = models.BooleanField(default=False)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return self.news.name
