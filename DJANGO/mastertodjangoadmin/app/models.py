from django.db import models

class Blog(models.Model): # admin sayfası için model oluşturuyoruz
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title

