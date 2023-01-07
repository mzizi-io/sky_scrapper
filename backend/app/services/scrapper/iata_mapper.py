import os
import pandas as pd


class IATAMapper:
    def __init__(self) -> None:
        iata_codes_path = os.path.join(os.path.dirname(__file__), 
                                       os.pardir, os.pardir, 'config',
                                       'iata_codes.csv')
        iata_codes_df = pd.read_csv(iata_codes_path,
                                    sep=',')

        # Filter out medium and large airports
        iata_codes_df = iata_codes_df[iata_codes_df['type'].isin(['medium_airport', 'large_airport'])] # noqa

        # Filter out airports with not IATA Codes
        iata_codes_df = iata_codes_df.dropna(axis=0, subset=['iata_code'])

        # Change DF to dict
        iata_codes_mapping = iata_codes_df.set_index(['name'])

        # Remove duplicates
        iata_codes_mapping = iata_codes_mapping[~iata_codes_mapping.index.duplicated(keep='first')] # noqa

        # Get mapping
        self.iata_codes_mapping = iata_codes_mapping.to_dict(orient='index')

    def get_airport_names(self):
        return list(self.iata_codes_mapping.keys())

    def get_iata_code_from_name(self, name: str):
        return self.iata_codes_mapping[name]['iata_code']

    def calculate_distance(self):
        return 0

    def filter_codes_by_country(self, country: str):
        return [entry['iata_code'] for entry in self.iata_codes_mapping.values() if entry['iso_country'] == country]

    def filter_codes_by_distance(self):
        return []

    def filter_codes_by_continent(self, continent: str):
        return [entry['iata_code'] for entry in self.iata_codes_mapping.values() if entry['continent'] == continent]
    
