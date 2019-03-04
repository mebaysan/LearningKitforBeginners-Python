from django.db import models

# Create your models here.

class Job(models.Model):
    email=models.CharField(max_length=75)
    content=models.TextField(verbose_name="Ne İstiyor")
    def __str__(self):
        return self.email
