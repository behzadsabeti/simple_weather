import json
import os
from dotenv import load_dotenv

import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from api import weather_api
from services import openweather_service
from views import home

api = fastapi.FastAPI()


def configure():
    configure_routing()
    configure_api_keys()


def configure_api_keys():
    if not os.path.isfile('.env'):
        print("WARNING: The .env file does not exist in the current directory.")
        print("Please create a .env file and add the required environment variables.")
    else:
        # Load environment variables from the .env file if it exists
        from dotenv import load_dotenv
        load_dotenv()
        openweather_service.api_key = os.environ.get('api_key')
        


def configure_routing():
    # api.mount('/static', StaticFiles(directory='static'), name='static')
    api.include_router(home.router)
    api.include_router(weather_api.router)


if __name__ == '__main__':
    configure()

