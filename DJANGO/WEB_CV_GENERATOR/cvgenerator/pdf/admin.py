from django.contrib import admin
from pdf.models import Profile
from django.contrib.auth.models import User,Group

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date')
    readonly_fields = (
    'name', 'email', 'phone', 'summary', 'degree', 'school', 'university', 'previous_work', 'skills', 'created_date')
    list_filter = ('created_date',)


admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)