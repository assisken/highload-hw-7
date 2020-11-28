from datetime import datetime

from flask import Blueprint, request

from app.forecast import retrieve_forecast, form_forecast

api = Blueprint("api", __name__)


def handle_post():
    try:
        return form_forecast(**request.json).as_json()
    except TypeError as e:
        return {'error': str(e)}, 404


@api.route("/forecast/", methods=['GET', 'POST', 'PUT'])
def get_forecast():
    if request.method in ('POST', 'PUT'):
        return handle_post()
    time = request.args.get("dt")
    try:
        resp = retrieve_forecast(
            city=request.args.get("city"), timestamp=time
        ).as_json()
    except ValueError as e:
        resp = ({"error": str(e)}, 404)
    return resp


@api.route("/current/", methods=['GET', 'POST', 'PUT'])
def get_current_forecast():
    if request.method in ('POST', 'PUT'):
        return handle_post()
    time = datetime.now()
    try:
        resp = retrieve_forecast(city=request.args.get("city")).as_json()
    except ValueError as e:
        resp = ({"error": str(e)}, 404)
    return resp
