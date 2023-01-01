import scrapy

from .chrome_driver import ChromeDriver


class SkyScannerSpider(scrapy.Spider):
    name = "countries_spider"
    allowed_domains = ["toscrape.com"]

    def start_requests(self):
        url = "http://quotes.toscrape.com"
        yield scrapy.Request(url=url, callback=self.parse_countries)

    def parse_countries(self, response):
        chrome_driver = ChromeDriver()
        content = chrome_driver.parse_content()
        return content
