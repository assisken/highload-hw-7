from datetime import datetime

from flask import Blueprint, request

from app.forecast import retrieve_forecast
from dateutil.parser import isoparse

api = Blueprint("api", __name__)


@api.route("/forecast/")
def get_forecast():
    time = isoparse(request.args.get("dt"))
    try:
        resp = retrieve_forecast(
            city=request.args.get("city"), timestamp=time
        ).as_json()
    except ValueError as e:
        resp = ({"error": str(e)}, 404)
    return resp


@api.route("/current/")
def get_current_forecast():
    time = datetime.now()
    try:
        resp = retrieve_forecast(
            city=request.args.get("city"), timestamp=time
        ).as_json()
    except ValueError as e:
        resp = ({"error": str(e)}, 404)
    return resp
