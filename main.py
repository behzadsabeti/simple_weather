import json
import os
from dotenv import load_dotenv

import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from api import weather_api
from services import openweather_service
from views import home

app = fastapi.FastAPI()


def configure():
    configure_routing()
    configure_api_keys()


def configure_api_keys():
    api_key = os.environ.get('api_key')
    if api_key is None:
        print("ERROR: API key is not found in the environment variables.")
    else:
        openweather_service.api_key = api_key
        print("API key loaded successfully:", api_key)



        


def configure_routing():
    # api.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)
    app.include_router(weather_api.router)


configure()

