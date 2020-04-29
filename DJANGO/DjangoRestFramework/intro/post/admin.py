from django.contrib import admin
from post.models import Post


class PostAdmin(admin.ModelAdmin):
    actions = ('set_to_draft', 'set_to_none_draft')

    def set_to_draft(self, request, queryset):
        count = queryset.update(draft=True)
        self.message_user(request, f"{count} yazı draft=True olarak işaretlendi")

    set_to_draft.short_description = 'İşaretlenenleri Draft=True Yap'

    def set_to_none_draft(self, request, queryset):
        count = queryset.update(draft=False)
        self.message_user(request, f"{count} yazı draft=False olarak işaretlendi")

    set_to_none_draft.short_description = 'İşaretlenenleri Draft=False Yap'


admin.site.register(Post,PostAdmin)
