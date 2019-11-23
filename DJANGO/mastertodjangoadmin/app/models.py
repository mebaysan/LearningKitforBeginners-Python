from django.db import models
from djgeojson.fields import PointField # 3rd party kütüphaneler sayesinde gelen field

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category" # bu sayede admin panelde tekil ve çoğul isimleri belirleyebiliriz
        verbose_name_plural = "Categories"


class Blog(models.Model):  # admin sayfası için model oluşturuyoruz
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100)
    categories = models.ManyToManyField(Category)

    def __str__(self):  # instance'lar listelenirken self.title'ı gözükecek. object olarak değil
        return self.title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Place(models.Model):
    name = models.CharField(max_length=255)
    location = PointField()
    def __str__(self):
        return self.name