import logging
from api import API
from datacleaner import DataCleaner
from datasaver import DataSaver

logger = logging.getLogger(__name__)

logging.basicConfig(
    filename='pipeline.log', 
    format='[%(asctime)s][%(name)s] %(message)s', 
    datefmt='%Y-%m-%d %H:%M:%S', 
    level=logging.INFO)

api = API()
dc = DataCleaner()
ds = DataSaver()

logger.info('Starting data pipeline...')

data = api.fetch_data()
cleaned_data = dc.clean_data(data)
ds.save_data(cleaned_data)