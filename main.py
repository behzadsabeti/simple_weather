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
    if not os.path.isfile('.env'):
        print("WARNING: The .env file does not exist in the current directory.")
        print("Please create a .env file and add the required environment variables.")
    else:
        # Load environment variables from the .env file if it exists
        from dotenv import load_dotenv
        load_dotenv()
        api_key = os.environ.get('api_key')
        if api_key is None:
            print("ERROR: API key is not found in the environment variables.")
        else:
            openweather_service.api_key = api_key

        


def configure_routing():
    # api.mount('/static', StaticFiles(directory='static'), name='static')
    app.include_router(home.router)
    app.include_router(weather_api.router)


configure()

