from flask import jsonify, render_template, request

from app.items import bp
from app.items.forms import AddItemForm
@bp.route('/')
@bp.route('/index')
def index():
    return 'Hello World!'

@bp.route('/add', methods=['GET','POST'])
def add_item():
    form = AddItemForm()
    if request.method == 'POST':
        pass # TODO : Implement
    return render_template('addItem.html',form=form)

@bp.route('/view', methods=['GET'])
def view_items():
    if request.method == 'POST':
        pass # TODO : Implement
    return render_template('viewItems.html')

@bp.route('/update/<item_id>', methods=['GET','POST'])
def update_items():
    form = UpdateItemForm()
    if request.method == 'POST':
        pass # TODO : Implement
    return render_template('updateItem.html',form=form)