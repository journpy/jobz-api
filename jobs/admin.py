from django.contrib import admin
from jobs.models import models


@admin.register(models.Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'source', 'external_id', 'title', 'company_name', 
        'company_logo_url', 'company_website', 'location_raw', 
        'location_country', 'location_city', 'location_state', 'is_remote',
        'description', 'url', 'posted_at', 'date_scraped', 'last_updated',
    ]

