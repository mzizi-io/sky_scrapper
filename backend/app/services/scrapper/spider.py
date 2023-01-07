import scrapy
import json

from .chrome_driver import ChromeDriver


class SkyScannerSpider(scrapy.Spider):
    name = "countries_spider"
    allowed_domains = ["toscrape.com"]

    custom_settings = {
        "TELNETCONSOLE_ENABLED": False,
        "TELNETCONSOLE_PORT": None
    }

    def __init__(self, parameter_dict: dict) -> None:
        self.parameter_dict = parameter_dict

    def start_requests(self):
        url = "http://quotes.toscrape.com"
        yield scrapy.Request(url=url, callback=self.parse_countries)

    def parse_countries(self, response):
        chrome_driver = ChromeDriver()
        content = chrome_driver.parse_content(self.parameter_dict)
        self.write_to_db(content)
    
    def write_to_db(self, content):
        with open("test.json", "w+") as file:
            json.dump(content, file)

