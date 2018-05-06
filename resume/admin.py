from django.contrib import admin
from .models import *


class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'corpURL', 'image', 'desc', 'start', 'end']
    list_filter = ['start']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['company', 'projectName', 'desc']


admin.site.register(Job, JobAdmin)
admin.site.register(Project, ProjectAdmin)
