import os
from urllib.parse import urlencode

import requests
from dateutil.parser import isoparse

from app.models import Forecast, Unit
import app.rediska as rediska

API_URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.getenv("API_KEY")


@rediska.save
def form_forecast(
    city: str, timestamp: str, temperature: float, unit: Unit = Unit.celsius
) -> Forecast:
    return Forecast(city=city, temperature=temperature, unit=unit)


@rediska.cache
def retrieve_forecast(
    city: str, timestamp: str, unit: Unit = Unit.celsius
) -> Forecast:
    query = {"appid": API_KEY, "q": city, "units": unit.value}
    resp = requests.get(f"{API_URL}?{urlencode(query)}")

    if resp.status_code != 200:
        raise ValueError(f"Code is {resp.status_code}:\n{resp.content}")

    data = resp.json()
    temp = None
    for time in data["list"]:
        if time["dt"] == isoparse(timestamp).timestamp():
            temp = time["main"]["temp"]
    if temp is None:
        raise ValueError("Temperature not found")
    return Forecast(city=data["city"]["name"], temperature=round(temp - 273, 2))
