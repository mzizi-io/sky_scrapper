import os
import sys

SCRIPT_DIR = os.path.dirname(__file__)
SCRIPT_DIR = os.path.join(SCRIPT_DIR, os.pardir, os.pardir, os.pardir)
sys.path.append(os.path.abspath(SCRIPT_DIR))

from fastapi import APIRouter, Depends # noqa
from typing import Union, List, Dict # noqa

from services.scrapper.iata_mapper import IATAMapper # noqa
from api.dependencies.dep_locations import get_iata_codes_for_continent, get_airport_names, get_iata_codes_for_country # noqa

locations = APIRouter()


@locations.get("/airports/names", tags=["locations"])
async def iata_codes(result: dict = Depends(get_airport_names)):
    return result


@locations.get("/airports/codes/country={country}", tags=["locations"])
async def iata_codes_for_country(result: dict = Depends(get_iata_codes_for_country)): # noqa
    return result


@locations.get("/airports/codes/continent={continent}", tags=["locations"])
async def iata_codes_for_continent(result: dict = Depends(get_iata_codes_for_continent)): # noqa
    return result
