from django.contrib import admin
from users.models import Manager,CustomUser

admin.site.register(Manager)
admin.site.register(CustomUser)
