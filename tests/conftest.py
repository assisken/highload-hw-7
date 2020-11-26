from pytest import fixture

from app.create_app import create_app


@fixture
def app():
    app = create_app()
    return app
