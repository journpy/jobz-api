from django.db import models
from uuid import uuid4
from django.utils.translation import gettext_lazy as _


class BaseJob(models.Model):
    """Model a job."""
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    source = models.CharField(max_length=100)
    external_id = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, db_index=True)
    company_name = models.CharField(max_length=100)
    company_logo_url = models.URLField(null=True, blank=True)
    company_website = models.URLField(null=True, blank=True)
    location_raw = models.CharField(max_length=200, null=True, blank=True)
    location_country = models.CharField(max_length=100, null=True, blank=True)
    location_city = models.CharField(max_length=100, null=True, blank=True)
    location_state = models.CharField(max_length=100, null=True, blank=True)
    is_remote = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    posted_at = models.CharField(null=True, blank=True)
    date_scraped = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    # Optional / extended
    salary_min = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    salary_max = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    salary_currency = models.CharField(max_length=10, null=True, blank=True)
    salary_period = models.CharField(max_length=20, null=True, blank=True)  # e.g. 'year', 'month', 'hour'

    job_type = models.CharField(max_length=50, null=True, blank=True)
    experience_level = models.CharField(max_length=50, null=True, blank=True)
    industry = models.CharField(max_length=200, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)
    tags = models.JSONField(null=True, blank=True)
    benefits = models.TextField(null=True, blank=True)

    contact_name = models.CharField(max_length=200, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=50, null=True, blank=True)
    contact_address = models.TextField(null=True, blank=True)

    geo_latitude = models.FloatField(null=True, blank=True)
    geo_longitude = models.FloatField(null=True, blank=True)
    timezone = models.CharField(max_length=50, null=True, blank=True)

    original_payload = models.JSONField(null=True, blank=True)
    source_metadata = models.JSONField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    expired_at = models.DateTimeField(null=True, blank=True)
    times_seen = models.IntegerField(default=1)
    last_seen = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['-posted_at']

    def __str__(self):
        """String representation of the Model object."""
        return self.title
