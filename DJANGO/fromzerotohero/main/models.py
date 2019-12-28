from django.db import models


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
    pic_url = models.TextField(default='-')
    pic_name = models.TextField(default='-')

    def __str__(self):
        return self.set_name + " ({})".format(self.id)


class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=False)
    is_it_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name
