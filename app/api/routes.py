
from flask import jsonify 

from app.api import bp

@bp.route('/api/v1')
def index():
    return jsonify(alive=True,version='1.0.0',response='Good')