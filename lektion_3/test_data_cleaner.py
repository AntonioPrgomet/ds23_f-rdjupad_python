import json
from datacleaner import DataCleaner

data = json.load(open('data/temps2.json'))

def test_data_cleaner_dates():
    dc = DataCleaner(data=data)
    dc.clean_dates()

def test_data_cleaner_temps():
    dc = DataCleaner(data=data)
    dc.clean_temps()
