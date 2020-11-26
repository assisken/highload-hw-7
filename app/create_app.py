from flask import Flask

from app.api.v1.forecast import api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix="/v1")
    return app
