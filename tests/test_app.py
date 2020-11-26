from datetime import datetime
from urllib.parse import urlencode

from flask import url_for, Response
from flask.testing import FlaskClient
from pytest_mock import MockFixture

from app.models import Forecast
from tests.helpers import autodetect_params, case


@autodetect_params()
@case(
    "With correct time",
    forecast=Forecast(city="Bob", temperature=100.500),
    time=datetime(2000, 1, 1, 1, 1),
)
def test_get_forecast(
    forecast: Forecast,
    time: datetime,
    client: FlaskClient,
    mocker: MockFixture,
):
    mocker.patch("app.api.v1.forecast.retrieve_forecast", return_value=forecast)

    query = {"city": forecast.city, "dt": time.isoformat()}
    url = f'{url_for("api.get_forecast")}?{urlencode(query)}'
    resp: Response = client.get(url)

    assert resp.json == forecast.as_json()


@autodetect_params()
@case(
    "With incorrect time",
    forecast=Forecast(city="Bob", temperature=100.500),
    message="Temperature not found!",
)
def test_get_forecast_with_error(
    forecast: Forecast,
    message: str,
    client: FlaskClient,
    mocker: MockFixture,
):
    mocker.patch(
        "app.api.v1.forecast.retrieve_forecast", side_effect=ValueError(message)
    )

    query = {"city": forecast.city, "dt": datetime(1999, 10, 10, 10).isoformat()}
    url = f'{url_for("api.get_forecast")}?{urlencode(query)}'
    resp: Response = client.get(url)

    assert resp.status_code == 404
    assert resp.json == {"error": message}


@autodetect_params()
@case("With correct time", forecast=Forecast(city="Pop", temperature=500.100))
def test_get_current_forecast(
    forecast: Forecast,
    client: FlaskClient,
    mocker: MockFixture,
):
    mocker.patch("app.api.v1.forecast.retrieve_forecast", return_value=forecast)

    query = {"city": forecast.city}
    url = f'{url_for("api.get_current_forecast")}?{urlencode(query)}'
    resp: Response = client.get(url)

    assert resp.json == forecast.as_json()


@autodetect_params()
@case(
    "With incorrect time",
    forecast=Forecast(city="Bob", temperature=100.500),
    message="Temperature not found!",
)
def test_get_current_forecast_with_error(
    forecast: Forecast,
    message: str,
    client: FlaskClient,
    mocker: MockFixture,
):
    mocker.patch(
        "app.api.v1.forecast.retrieve_forecast", side_effect=ValueError(message)
    )

    query = {"city": forecast.city}
    url = f'{url_for("api.get_current_forecast")}?{urlencode(query)}'
    resp: Response = client.get(url)

    assert resp.status_code == 404
    assert resp.json == {"error": message}
