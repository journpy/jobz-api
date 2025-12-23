import sys
import os
import logging
import requests
import json
import time
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from typing import Dict, Any, List


logging.basicConfig(level=logging.INFO)
load_dotenv()

# Handle ModuleNotFoundError by adding the parent package (services) to path
SCRAPER_PATH: str = os.path.join(os.getcwd(), 'services')
sys.path.append(SCRAPER_PATH)
# print(sys.path)
try:
    from scrapers import base
except Exception as exc:
    logging.error(f"❌ Could not import Base Scraper: {exc}")
logging.info("✅ Successfully imported Base Scraper")



class AdzunaScraper(base.BaseScraper):
    """Scraper class for Adzuna API."""
    def __init__(self, api_url: str, name: str="ADZUNA"):
        """Class constructor"""
        self.name = name
        super().__init__(api_url, name)


    def scrape_jobs(self) -> Dict[str, Any]:
        """Scrape raw Remotive jobs"""
        self.api_url = os.getenv("ADZUNA_API_URL", "")
        logging.info(f"✅ Successfully accessed Adzuna's API URL {self.api_url}")
        
        try:
            data: str = requests.get(self.api_url)
            logging.info(f"✅ Successfully scraped {self.name} API")
        except Exception as exc:
            logging.error(f"❌ An error occured: {exc}") 
            while self.retries <= self.max_retries:
                logging.error(f"⚠️ Retrying {self.retries}/{self.max_retries}")
                self.retries += 1
                time.sleep(1)
                
        deserialized_data: Dict = data.json()
        if deserialized_data:
            logging.info(f'ℹ️ Data type of raw jobs data: {type(deserialized_data)}')
            return deserialized_data.get("results", {})
        return {}
        
        
    
    
    def clean_data(self) -> Any:
        """Clean raw data."""
        # Pass .content instead of .text to avoid problems with character 
        # encoding. The .content attribute holds raw bytes, which Python’s 
        # built-in HTML parser can decode better than the 
        # .text attribute of the returned data.
        try:
            ret_data = self.scrape_jobs()
            serialized_data: str = json.dumps(ret_data, indent=4)
            logging.info(f'ℹ️ Scraped job data has been serialized and has data type: {type(serialized_data)}')
            soup = BeautifulSoup(serialized_data, "html.parser")
            #logging.info(f"ℹ️ There are {len(soup)} jobs")
            return soup.get_text(strip=True)

        except Exception as exc:
            logging.error(f"An error occured: {exc}")
            return []
        
    def normalise_data(self) -> List[Any]:
        """Normalize raw job data into a consistent format"""
        adzuna_scraper = AdzunaScraper('')
        payloads = []
        try:
            jobs = json.loads(adzuna_scraper.clean_data())
        except Exception as exc:
            logging.error(f"❌ Could not deserialize Scraper JSON data.")
        logging.info(f"✅ Successfully deserialized {len(jobs)} jobs")
        for job in jobs:
           
            payload = {
                'source': job.get('source', 'Adzuna'),
                'external_id': job.get("id", ""),
                'title': job.get("title", ""),
                'company_name': job.get("company", {}).get("display_name", ""),
                'company_logo_url': job.get("company_logo", ""),
                'company_website': job.get("company_website", ""),
                'location_raw': job.get("location", {}).get("display_name", ""),
                'location_country': job.get("location", {}).get("area", "")[0],
                'location_city': job.get("location", {}).get("area", "")[-1], 
                'location_state': job.get("location", {}).get("area", "")[1] if len(job.get("location", {}).get("area", "")) > 2 else job.get("location", {}).get("area", ""),
                'is_remote': job.get('is_remote', False),
                'description': job.get('description', ''),
                'url': job.get('redirect_url', ''),
                'posted_at': job.get('created'),    
                'salary_min': job.get('salary_min'),
                'salary_max': job.get('salary_max'),
                'salary_currency': job.get('salary_currency', '') or 'USD',
                'salary_period': job.get('salary_period', ''),
                'job_type': job.get('contract_time', ''),
                'experience_level': job.get('experience_level', ''),
                'industry': job.get('category', '').get("label", ""),
                'department': job.get('category', ''),
                'tags': job.get('category', '').get("tag", ""),
                'benefits': job.get('benefits', ''),
                'contact_name': job.get('contact_name', ''),
                'contact_email': job.get('contact_email', ''),
                'contact_phone': job.get('contact_phone', ''),
                'contact_address': job.get('contact_address', ''),
                'geo_latitude': job.get('latitude'),
                'geo_longitude': job.get('longitude'),
                'timezone': job.get('timezone'), 
                'original_payload': job,
                'source_metadata': job.get('source_metadata', []),
                'is_active': job.get('is_active', True),
                'expired_at': job.get('expired_at'),
                'times_seen': job.get('times_seen', 1),
                'last_seen': job.get('last_seen')
            }
            payloads.append(payload)
        
        return payloads
                

                
                

                

      
                
        
