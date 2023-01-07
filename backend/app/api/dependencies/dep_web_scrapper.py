import logging
from services.scrapper.iata_mapper import IATAMapper # noqa
from services.scrapper.sky_scrapper import Scrapper # noqa
from models.web_scrapper import ParameterDict


def launch_scrapper(attributes: ParameterDict):
    scrapper = Scrapper()
    scrapper.run_selenium_scraper()
