from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200,editable=False)
    email = models.CharField(max_length=200,editable=False)
    phone = models.CharField(max_length=200,editable=False)
    summary = models.TextField(editable=False)
    degree = models.CharField(max_length=200,editable=False)
    school = models.CharField(max_length=200,editable=False)
    university = models.CharField(max_length=200,editable=False)
    previous_work = models.TextField(editable=False)
    skills = models.TextField(editable=False)
    created_date = models.DateTimeField(auto_now_add=True,editable=False,null=True,blank=False)
    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profiller'

    def __str__(self):
        return self.name
