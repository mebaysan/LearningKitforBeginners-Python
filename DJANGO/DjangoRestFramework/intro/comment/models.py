from django.db import models
from django.contrib.auth.models import User
from post.models import Post
from django.utils import timezone


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey(to='self', on_delete=models.CASCADE, related_name='replies', null=True,
                               blank=True)  # kendisi ile foreign bağlıyoruz
    content = models.TextField()
    created_date = models.DateTimeField(editable=False)

    class Meta:
        verbose_name = 'Yorum'
        verbose_name_plural = 'Yorumlar'
        ordering = ('created_date',)

    def __str__(self):
        return f"{self.post.title} - {self.user.username}"

    def get_children(self): # child instance'ları alıyoruz
        return Comment.objects.filter(parent=self)

    @property
    def any_children(self): # child instance'lar var mı ona bakıyoruz
        return Comment.objects.filter(parent=self).exists()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = timezone.now()
        super(Comment, self).save(*args, **kwargs)
