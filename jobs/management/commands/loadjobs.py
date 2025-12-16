from django.core.management.base import BaseCommand
from services.scrapers.remotive import RemotiveScraper
from jobs.models.models import Job
import logging


logging.basicConfig(level=logging.INFO)

class Command(BaseCommand):
    """Custom Management command class"""
    help = "Save jobs to database"

    def handle(self, *args, **kwargs):
        remotive_scraper = RemotiveScraper('').normalise_data()
        scrapers = remotive_scraper
        counter = 0
        for job in scrapers:
            try:
                Job.objects.update_or_create(
                    defaults={'source': 'Remotive'},
                    **job
                    )
                self.stdout.write(self.style.SUCCESS(f"✅ Successfully saved job to the database"))
                counter += 1
            except Exception as exc:
                self.stdout.write(self.style.ERROR(f"❌ Could not save job data to the database: {exc}"))
            

        self.stdout.write(self.style.SUCCESS(f"✅ {counter} jobs have been saved to the database."))

