from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    