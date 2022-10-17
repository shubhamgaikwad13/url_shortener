from . import urlshort
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'qrj232sgsg32'

    app.register_blueprint(urlshort.bp)

    return app
