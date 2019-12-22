from django.db import models


# Create your models here.

class News(models.Model):
    name = models.CharField(max_length=255)
    short_txt = models.TextField()
    body_txt = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    pic_name = models.TextField()
    pic_url = models.TextField(default='-')
    writer = models.CharField(max_length=50)
    category_name = models.CharField(max_length=255, default='-')
    category_id = models.IntegerField(default=0)
    ocategory_id = models.IntegerField(default=0)
    show = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.name
