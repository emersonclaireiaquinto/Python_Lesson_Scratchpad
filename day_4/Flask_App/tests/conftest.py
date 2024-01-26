import pytest
import src
from flask import Flask

@pytest.fixture
def app():
    app = src.make_app()
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

