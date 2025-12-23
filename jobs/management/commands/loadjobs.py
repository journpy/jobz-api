from django.core.management.base import BaseCommand
from services.scrapers.remotive import RemotiveScraper
from services.scrapers.adzuna import AdzunaScraper
from jobs.models.models import Job
import logging


logging.basicConfig(level=logging.INFO)

class Command(BaseCommand):
    """Custom Management command class"""
    help = "Save jobs to database"

    def handle(self, *args, **kwargs):
        remotive_scraper = RemotiveScraper('').normalise_data()
        adzuna_scraper = AdzunaScraper('').normalise_data()
        scrapers = remotive_scraper + adzuna_scraper
        counter: int = 0
        created_counter: int = 0
        update_counter: int = 0
        for job in scrapers:
            try:
                job, created = Job.objects.update_or_create(**job)
                self.stdout.write(self.style.SUCCESS(
                    f"✅ Successfully saved job to the database"
                    ))
                if created:
                    created_counter += 1
                else:
                    update_counter += 1
                #print(f"New job? {created}") #tell whether this job was created or updated
                counter += 1
            except Exception as exc:
                self.stdout.write(self.style.ERROR(
                    f"❌ Could not save job data to the database: {exc}"
                    ))
            

        self.stdout.write(self.style.SUCCESS(f"""\n
                                             ✅ SUCCESS:
                                             {created_counter} new jobs added 
                                             and {update_counter} jobs updated. 
                                             In total, {counter} jobs have been 
                                             saved to the database."""))

