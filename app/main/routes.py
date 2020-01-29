from flask import jsonify, render_template, request

from app.main import bp
from app.main.forms import AddItemForm
@bp.route('/')
@bp.route('/index')
def index():
    return 'Hello World!'


@bp.route('/items/add', methods=['GET','POST'])
def add_item():
    form = AddItemForm()
    if request.method == 'POST':
        return jsonify({
            'item' : form.item.data,
            'owner': form.owner.data,
            'description' : form.description.data
        })
    return render_template('addItem.html',form=form)
