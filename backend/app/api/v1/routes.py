import datetime

from flask import abort, jsonify, request

from app.api.v1 import bp
from app.models import Item
from app import db

@bp.route('/')
def index():
    return jsonify(success=True,version='1.0.0',message='')


@bp.route('/addItem',methods=['GET','POST'])
def add_item():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({'success' : False, 'message' : "Invalid JSON supplied", 'timestamp' : datetime.datetime.utcnow(), 'id' : None}), 400
        try:
            i = Item(name=data['name'],description=data['description'], owner=data['owner'],created=datetime.datetime.utcnow(),is_archived=False)
            db.session.add(i)
            db.session.flush()
            item_id = i.id
        except KeyError as e:
            return jsonify({'success' : False, 'message' : "Invalid data supplied", 'timestamp' : datetime.datetime.utcnow(), 'id' : None}), 400
        return jsonify({'success' : True, 'message' : "Item created", 'timestamp' : datetime.datetime.utcnow(), 'id' : item_id})
    else:
        return jsonify({'success' : False, 'message' : "Only POST allowed", 'timestamp' : datetime.datetime.utcnow(), 'id' : None}), 405


@bp.route('/getItem/<id>',methods=['GET'])
def get_item(id):
    i = Item.query.filter_by(id=id).first()
    if not i:
        return jsonify({'success' : False, 'message' : "Invalid id", 'timestamp' : datetime.datetime.utcnow(), 'id' : None, 'archived' : None}), 404
    else:
        return jsonify(i.json())

@bp.route('/archiveItem/<id>',methods=['GET'])
def archive_item(id):
    i = Item.query.filter_by(id=id).first()
    if not i:
        return jsonify({'success' : False, 'message' : "Invalid id", 'timestamp' : datetime.datetime.utcnow(), 'id' : None}), 404
    i.is_archived = True
    db.session.add(i)
    db.session.commit()
    return jsonify({'success' : True, 'message' : "Item archived", 'timestamp' : datetime.datetime.utcnow(), 'id' : i.id})