from django.db import models


class Trending(models.Model):
    txt = models.CharField(max_length=255)
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.txt
