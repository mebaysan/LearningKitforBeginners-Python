from django.contrib import admin
from reports.models import Report,ProblemReported

admin.site.register(Report)
admin.site.register(ProblemReported)