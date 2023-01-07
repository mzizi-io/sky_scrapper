from concurrent.futures import ProcessPoolExecutor
from services.scrapper.sky_scrapper import Scrapper


def scrapper_func(parameter_dict: dict):
    '''
    Test
    '''
    scrapper = Scrapper()
    scrapper.run_selenium_scraper(parameter_dict)


parameter_dict = {"from_": "MUC",
                  "departure": "230203",
                  "return_": "230303",
                  "adults": "2",
                  "children": "3",
                  "cabin_class": "economy"}

with ProcessPoolExecutor(max_workers=2) as executor:
    params = [parameter_dict] * 100
    COUNT = 0
    for result in executor.map(scrapper_func, params):
        print(result)
        COUNT += 1

    print(COUNT)
