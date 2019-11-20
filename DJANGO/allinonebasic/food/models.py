from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    is_free = models.BooleanField(null=True, blank=False)

    def __str__(self):
        return self.name
