from django.db import models


# Create your models here.

class Main(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    facebook_address = models.CharField(max_length=255)
    twitter_address = models.CharField(max_length=255)
    youtube_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    set_name = models.CharField(max_length=255)

    def __str__(self):
        return self.set_name + " ({})".format(self.id)
