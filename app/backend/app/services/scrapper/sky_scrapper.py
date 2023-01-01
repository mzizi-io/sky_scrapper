import logging
from scrapy.crawler import CrawlerProcess
from scrapy import signals
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher
from services.scrapper.spider import SkyScannerSpider


class Scrapper:
    def __init__(self) -> None:
        pass

    def run_scrapper(self, disable_logs: bool = True):
        if disable_logs:
            self.disable_logs()

        results = []

        def crawler_results(signal, sender, item, response, spider):
            results.append(item)

        dispatcher.connect(crawler_results, signal=signals.item_scraped)

        process = CrawlerProcess(get_project_settings())
        process.crawl(SkyScannerSpider)
        process.start()
        return results

    def disable_logs(self):
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
