import os
import re
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium_stealth import stealth
from dotenv import load_dotenv

load_dotenv()
DEFAULT_URL = os.getenv("DEFAULT_URL")

class ChromeDriver:
    def __init__(self) -> None:
        self.load_driver()

    def load_driver(self):
        # Use headless option to not open a new browser window
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-extensions")

        self.driver = webdriver.Chrome(chrome_options=chrome_options)
    
    def parse_content(self):
        stealth(self.driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True)

        # Getting list of Countries
        self.driver.get(DEFAULT_URL)

        # Accept cookies
        self.accept_cookies()

        # Get flight details
        return self.get_flight_details()

    def accept_cookies(self):
        try:
            time.sleep(30)
            chain = ActionChains(self.driver)
            button = self.driver.find_element(By.ID, "acceptCookieButton")
            chain.move_to_element(button).click().perform()
        except:
            print('\n\n\n No cookie button found')

    def get_country_specific_details(self, country_element):
        chain = ActionChains(self.driver)

        # Click on div
        time.sleep(2)
        chain.move_to_element(country_element).click().perform()

        # Get all links from container divs
        try:
            wait = WebDriverWait(self.driver, timeout=10)
            wait.until(lambda d: d.find_element(By.CLASS_NAME, "city-list"))

        except:
            print('\n\n\n Failed to load elements')
        
        time.sleep(5)
        city_list = self.driver.execute_script(f'''
                    return document.
                            getElementsByClassName('browse-list-category open')
                    ''')
        
        # In case of multiple open boxes
        city_list = city_list[-1]

        # Get the links for each destination
        links = city_list.find_elements(By.CLASS_NAME, 'browse-data-entry')
        country_div = country_element.find_element(By.CLASS_NAME, 'browse-data-route')

        # Get destination name
        country_name = country_div.find_element(By.XPATH, 'h3').text

        # Get destinations for country
        destinations = [self.collect_destination_details(index) for index in range(len(links))]

        # Close chevron
        chevron_down = country_element.find_element(By.CLASS_NAME, 'chevron-down')
        chain.move_to_element(chevron_down).click().perform()

        return country_name, destinations
    
    def collect_destination_details(self, index):
        destination = self.driver.execute_script(f'''
                    return document.
                            getElementsByClassName('browse-list-category open')[0].
                            getElementsByClassName('browse-data-entry')[{index}]
                    ''')

        # Get destination name
        try:
            destination_name = destination.find_element(By.TAG_NAME, 'h3').text

            # Get flight link
            flight_link = destination.find_element(By.CLASS_NAME, 'flightLink').get_attribute('href')

            # Get hotel link
            hotel_link = destination.find_element(By.CLASS_NAME, 'hotelLink').get_attribute('href')

            # Get Prices
            prices = destination.find_elements(By.CLASS_NAME, 'price')
            flight_price = re.sub("[^0-9]", "", prices[0].text)
            hotel_price = re.sub("[^0-9]", "", prices[1].text)

            result =  {'destination': destination_name, 
                    'flight_link': flight_link, 
                    'hotel_link': hotel_link,
                    'flight_price': flight_price,
                    'hotel_price': hotel_price}

        except:
            print('\n\n\n\n\n !!!!!!!!!!!!! ERROR. FAILED TO RETRIEVE DETAILS !!!!!!!!!!!!!')
        return result

    def get_flight_details(self):
        country_divs = self.driver.find_elements(By.CLASS_NAME, 'browse-list-category')
        results = {}
        for country in country_divs:
            country_name, destinations = self.get_country_specific_details(country)
            results[country_name] = destinations
        return results
