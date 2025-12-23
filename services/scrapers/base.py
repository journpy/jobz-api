from abc import ABC, abstractmethod
from typing import Dict, Any, List


class BaseScraper(ABC):
    """Abstract Base Class Scraper"""

    def __init__(self, api_url: str, name: str):
        """Class constructor"""
        self.api_url = api_url
        self.name = name
        self.retries: int = 1
        self.max_retries: int = 3

    @abstractmethod
    def scrape_jobs(self) -> Dict:
        """Scrape raw Remotive jobs"""
        pass


    @abstractmethod
    def clean_data(self) -> Any:
        """Abstract method to be overriden in the concrete classes."""
        pass
    
    @abstractmethod
    def normalise_data(self) -> List[Any]:
        """Abstract method to be overriden in the concrete classes."""
        pass
