from flask_testing import TestCase
from flask import Flask
from app import app, db
from app.models import User, newList


class BaseTestCase(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app
        # app.config.from_object("config")
        # return app
