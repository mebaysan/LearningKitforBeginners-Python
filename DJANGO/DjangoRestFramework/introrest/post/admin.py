from django.contrib import admin
from post.models import Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)


admin.site.register(Post, PostAdmin)
