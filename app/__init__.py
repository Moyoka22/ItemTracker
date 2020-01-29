from flask import Flask

from app.api import bp as api
from app.main import bp as main
from config import Config 

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    app.register_blueprint(main)

    app.config.from_object(Config)
    return app

