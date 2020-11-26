from datetime import datetime

from mock import MagicMock
from pytest_mock import MockFixture

from app.forecast import retrieve_forecast
from app.models import Forecast
from tests.helpers import case, autodetect_params


@autodetect_params()
@case(
    "With valid time",
    city="Muhostroy",
    temperature=100.500,
    time=datetime(1234, 5, 6, 7),
)
def test_retrieve_forecast(
    city: str, temperature: float, time: datetime, mocker: MockFixture
):
    mock = MagicMock()
    mock.status_code = 200
    mock.json.return_value = {
        "city": {"name": city},
        "list": [{"dt": time.timestamp(), "main": {"temp": temperature}}],
    }

    mocker.patch("requests.get", return_value=mock)
    assert retrieve_forecast(city, time) == Forecast(city=city, temperature=temperature)
