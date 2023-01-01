import logging
from services.scrapper.iata_mapper import IATAMapper # noqa
from services.scrapper.sky_scrapper import Scrapper # noqa
from models.web_scrapper import ParameterDict
from services.scrapper.spider import SkyScannerSpider
from scrapy.crawler import CrawlerRu
from scrapy import signals
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher


def launch_scrapper(attributes: ParameterDict):
    logger = logging.getLogger('scrapy')
    logger.propagate = False

    logger = logging.getLogger('filelock')
    logger.propagate = False

    logger = logging.getLogger('py.warnings')
    logger.propagate = False

    logger = logging.getLogger('selenium')
    logger.propagate = False

    logger = logging.getLogger('urllib3')
    logger.propagate = False

    results = []

    def crawler_results(signal, sender, item, response, spider):
        results.append(item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    process = CrawlerProcess(get_project_settings())
    process.crawl(SkyScannerSpider, args=attributes)
    process.start()
    return results
