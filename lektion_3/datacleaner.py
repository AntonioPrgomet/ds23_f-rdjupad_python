import datetime
import logging
import pandas as pd

class DataCleaner:
    def __init__(self, data) -> None:
        self.data = data
        self.logger = logging.getLogger(__name__)

    def clean_dates(self) -> None:
        for row in self.data:
            if '-' in row['date']:
                try:
                    y, m, d = [int(x) for x in row['date'].split('-')]
                except Exception as e:
                    self.logger.error((e, row['date']))
                    new_date = pd.NaT
                else:
                    new_date = datetime.date(y, m, d)
            elif '/' in row['date']:
                try:
                    m, d, y = [int(x) for x in row['date'].split('/')]
                except Exception as e:
                    self.logger.error((e, row['date']))
                    new_date = pd.NaT
                else:
                    new_date = datetime.date(2000 + y, m, d)
            else:
                self.logger.error('Could not parse date %s', row['date'])
                new_date = pd.NaT
            row['date'] = new_date

    def clean_temps(self):
        for row in self.data:
            try:
                new_temp = float(row['temp'])
            except TypeError:  
                new_temp = pd.NA
            except ValueError:  
                new_temp = float(row['temp'].replace(',', '.'))
            except Exception as e:  
                self.logger.error(e)
                new_temp = pd.NA

            row['temp'] = new_temp

    def clean(self):
        self.clean_dates()
        self.clean_temps()
        return self.data
