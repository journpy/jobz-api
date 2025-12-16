from django.contrib import admin
from jobs.models import models


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'source', 'title']
