from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=20,decimal_places=2,default=12.99)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title