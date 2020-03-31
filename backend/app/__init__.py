from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config 

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app,db)

    from app.api.v1 import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    from app.items import bp as items_bp
    app.register_blueprint(items_bp, url_prefix='/items' )

 

    return app

from app import models