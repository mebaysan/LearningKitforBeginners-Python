from django.contrib import admin
from main.models import Main,ContactForm
from django.contrib.auth.models import Permission

admin.site.register(Main)
admin.site.register(ContactForm)
admin.site.register(Permission)