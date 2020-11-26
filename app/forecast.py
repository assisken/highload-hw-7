import os
from datetime import datetime
from urllib.parse import urlencode

import requests

from app.models import Forecast, Unit

API_URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.getenv("API_KEY")


def retrieve_forecast(
    city: str, timestamp: datetime, units: Unit = Unit.CELSIUS
) -> Forecast:
    query = {"appid": API_KEY, "q": city, "units": units.value}
    resp = requests.get(f"{API_URL}?{urlencode(query)}")

    if resp.status_code != 200:
        raise ValueError(f"Code is {resp.status_code}:\n{resp.content}")

    data = resp.json()
    temp = None
    for time in data["list"]:
        if time["dt"] == timestamp.timestamp():
            temp = time["main"]["temp"]
    if temp is None:
        raise ValueError("Temperature not found")
    return Forecast(city=data["city"]["name"], temperature=temp)
