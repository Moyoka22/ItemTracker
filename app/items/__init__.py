from flask import Blueprint

bp = Blueprint(__name__,'items')

from app.items import routes