import logging
import random

class API:
    """Class to fetch data from API."""
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def fetch_data(self):
        self.logger.info('Fetching data...')
        if random.random() >= .5:
            return [1, 5, 7]
        else:
            self.logger.error('Could not fetch data.')
            return None
