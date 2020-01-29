from flask import Blueprint

bp = Blueprint(__name__,'main')

from app.main import routes