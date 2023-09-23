import fastapi
from fastapi import Form
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from services import openweather_service

templates = Jinja2Templates('templates')
router = fastapi.APIRouter()


@router.get('/')
def index(request: Request):
    return templates.TemplateResponse('home/index.html', {'request': request})


@router.post("/submit")
async def process_form(request: Request, city: str = Form(...), unit_system: str = Form(...)):
    # Handle the form data here

    report = await openweather_service.get_report_async(city=city, country=None, units=unit_system, state=None)

    return templates.TemplateResponse('home/index.html', {'request': request, "info": report})




# @router.get('/favicon.ico')
# def favicon():
#     return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')