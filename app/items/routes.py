from flask import jsonify, render_template, request, flash, redirect, url_for, abort

from app.items import bp
from app.items.forms import AddUpdateItemForm
from app.models import Item
from app import db

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html')

@bp.route('/add', methods=['GET','POST'])
def add_item():
    form = AddUpdateItemForm()
    if request.method == 'POST':
        data = request.form
        i = Item(name=data['name'], description=data['description'], owner=data['owner'])
        db.session.add(i)
        db.session.commit()
        flash('Item created.')
        return redirect(url_for('items.view_items'))
    return render_template('addItem.html',form=form)

@bp.route('/view', methods=['GET'])
def view_items():
    items = Item.query.all()
    return render_template('viewItems.html', items=items)

@bp.route('/update/<item_id>', methods=['GET','POST'])
def update_item(item_id):
    form = AddUpdateItemForm()
    i = Item.query.filter_by(id=item_id)
    if i.count() == 0:
        abort(404)
    if request.method == 'POST':
        data = request.form
        i.update(dict(name=data['name'],owner=data['owner'],description=data['description']))
        db.session.commit()
        return redirect(url_for('items.view_items'))
    return render_template('updateItem.html',form=form)

@bp.route('/delete/<item_id>', methods=['GET','DELETE'])
def delete_item(item_id):
    i = Item.query.filter_by(id=item_id).first_or_404()
    db.session.delete(i)
    db.session.commit()
    return redirect(url_for('items.view_items'))