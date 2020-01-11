from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from unidecode import unidecode  # slug yaparken türkçe karakter problemi için


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()
    slug = models.SlugField(unique=True, max_length=150, editable=False)
    image = models.ImageField(upload_to='post/', null=True, blank=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='modified_by')

    class Meta:
        verbose_name = 'Yazı'
        verbose_name_plural = 'Yazılar'

    def __str__(self):
        return self.title

    def get_slug(self):
        slug = slugify(unidecode(self.title))
        unique = slug
        number = 1
        while Post.objects.filter(slug=unique).exists():
            unique = "{}-{}".format(slug, number)
            number += 1
        return unique

    def save(self, *args, **kwargs):  # save etmeden önce (save methodunu override ediyoruz)
        if not self.id:  # eğer daha id'si oluşmamışsa
            self.created = timezone.now()
        self.modified = timezone.now()  # her değişiklik olduğunda modified güncellenecek
        self.slug = self.get_slug()
        return super(Post, self).save(*args, **kwargs)
