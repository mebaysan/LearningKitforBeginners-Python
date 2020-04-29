from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, default=1, null=True,editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False, blank=True)
    modified_date = models.DateTimeField(blank=True, editable=False)
    slug = models.SlugField(unique=True, editable=False, blank=True)
    image = models.ImageField(upload_to='post/', default='defaults/logo.png')
    modified_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='modified_posts',editable=False)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postlar'

    def __str__(self):
        return self.title

    def get_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        number = 1
        unique = slug
        while Post.objects.filter(slug=slug).exists():
            unique = f"{slug}-{number}"
            number += 1
        return unique

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = timezone.now()
        self.modified_date = timezone.now()
        self.slug = self.get_slug()
        super(Post, self).save(*args, **kwargs)
