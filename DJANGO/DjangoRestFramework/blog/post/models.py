from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    modified_date = models.DateTimeField(editable=False)
    slug = models.SlugField(unique=True, max_length=150, editable=False)
    image = models.ImageField(upload_to='media/post/')
    def get_slug(self):
        slug = slugify(self.title.replace("ı", "i"))
        unique = slug
        number = 1
        while Post.objects.filter(slug=unique).exists():
            unique = '{}-{}'.format(slug, number)
            number += 1
        return unique

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        self.slug = self.get_slug()
        return super(Post, self).save(*args, **kwargs)
