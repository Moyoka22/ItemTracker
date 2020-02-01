from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.api import bp as api
from app.items import bp as items
from config import Config 

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(items, url_prefix='/items' )

    app.config.from_object(Config)
    db = SQLAlchemy(app)
    
    return app

