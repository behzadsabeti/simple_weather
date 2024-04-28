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


import traceback

@router.post("/submit")
async def process_form(request: Request, city: str = Form(...), unit_system: str = Form(...)):
    try:
        report = await openweather_service.get_report_async(city=city, country=None, units=unit_system, state=None)
        return templates.TemplateResponse('home/index.html', {'request': request, "info": report})
    except Exception as e:
        traceback.print_exc()
        return fastapi.HTTPException(status_code=500, detail="Internal Server Error")





# @router.get('/favicon.ico')
# def favicon():
#     return fastapi.responses.RedirectResponse(url='/static/img/favicon.ico')
