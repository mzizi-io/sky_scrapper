import logging
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from services.scrapper.spider import SkyScannerSpider
from services.scrapper.chrome_driver import ChromeDriver

class Scrapper:
    def __init__(self) -> None:
        pass

    def run_scrapper(self, parameter_dict: dict = {}, disable_logs: bool = True):
        if disable_logs:
            self.disable_logs()

        process = CrawlerProcess(get_project_settings())
        process.crawl(SkyScannerSpider, parameter_dict=parameter_dict)
        process.start()
        return "Done"

    def run_selenium_scraper(self, parameter_dict: dict):
        '''
        Selenium
        '''
        ChromeDriver().parse_content(parameter_dict=parameter_dict)
        return "Done"
    
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
