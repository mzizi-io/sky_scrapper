from fastapi import FastAPI
import uvicorn

from api.routers.locations import locations
from api.routers.web_scrapper import web_scrapper

app = FastAPI()

# Add routers
app.include_router(locations)
app.include_router(web_scrapper)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
