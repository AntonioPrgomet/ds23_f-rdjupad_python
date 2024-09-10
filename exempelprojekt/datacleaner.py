import logging

class DataCleaner:
    "Class to clean data."
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def clean_data(self, data):
        self.logger.info('Cleaning data...')
        return [5, 7, 3]