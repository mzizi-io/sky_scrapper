from services.scrapper.iata_mapper import IATAMapper # noqa

# Static init. Do IO only once
mapper = IATAMapper()


async def get_airport_names():
    return mapper.get_airport_names()


async def get_iata_codes_for_country(country: str):
    return mapper.filter_codes_by_country(country)


async def get_iata_codes_for_continent(continent: str):
    return mapper.filter_codes_by_continent(continent)