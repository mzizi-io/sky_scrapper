import os
import sys

SCRIPT_DIR = os.path.dirname(__file__)
SCRIPT_DIR = os.path.join(SCRIPT_DIR, os.pardir, os.pardir, os.pardir)
sys.path.append(os.path.abspath(SCRIPT_DIR))

from fastapi import APIRouter, Depends # noqa
from typing import Union, List, Dict # noqa

from services.scrapper.iata_mapper import IATAMapper # noqa
from api.dependencies.dep_web_scrapper import launch_scrapper # noqa

web_scrapper = APIRouter()


@web_scrapper.post("/scrapper/launch", tags=["scrapper"])
async def iata_codes(result: dict = Depends(launch_scrapper)):
    return result
