import logging

class DataSaver:
    "Class to save data to SQL table."

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)

    def save_data(self, data):
        self.logger.info('Saving data...')