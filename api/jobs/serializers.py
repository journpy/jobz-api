from jobs.models.models import Job
from rest_framework import serializers


class JobSerializer(serializers.ModelSerializer[Job]):
    class Meta:
        model = Job
        fields = (
            'id', 'source', 'external_id', 'title', 'company_name', 
            'company_logo_url', 'company_website', 'location_raw', 
            'location_country', 'location_city', 'location_state', 'is_remote',
            'description', 'url', 'posted_at', 'date_scraped', 'last_updated'
        )
