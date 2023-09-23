from typing import Optional
import httpx

api_key: Optional[str] = None


async def get_report_async(city: str, state: Optional[str], country: Optional[str], units: str) -> dict:
    if state and country:
        q = f'{city},{state},{country}'
    else:
        q = f'{city}'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={q}&appid={api_key}&units={units}'

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

    data = resp.json()
    # forecast = data['main']
    return data
