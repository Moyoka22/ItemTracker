import datetime

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
        i = Item(name=data['name'], description=data['description'], owner=data['owner'],created=datetime.datetime.utcnow(),is_archived=False)
        db.session.add(i)
        db.session.commit()
        flash('Item created.')
        return redirect(url_for('items.view_items'))
    return render_template('addItem.html',form=form)

@bp.route('/view', methods=['GET'])
def view_items():
    items = Item.query.filter_by(is_archived=False)
    return render_template('viewItems.html', items=items)

@bp.route('/update/<item_id>', methods=['GET','POST'])
def update_item(item_id):
    form = AddUpdateItemForm()
    i = Item.query.filter_by(id=item_id).first_or_404()
    if request.method == 'POST':
        data = request.form
        i_new = Item(name=data['name'],owner=data['owner'],description=data['description'],is_archived=False)
        db.session.add(i_new)
        db.session.add(i)
        db.session.flush()
        if not i_new.id:
            db.session.rollback()
            abort(500)
        Item.update_version(i,i_new)
        db.session.commit()
        return redirect(url_for('items.view_items'))
    form.name.data = i.name
    form.owner.data = i.owner
    form.description.data = i.description
    return render_template('updateItem.html',form=form, item=i)

@bp.route('/archive/<item_id>', methods=['GET','DELETE'])
def archive_item(item_id):
    i = Item.query.filter_by(id=item_id).first_or_404()
    i.is_archived = True
    db.session.add(i)
    db.session.commit()
    return redirect(url_for('items.view_items'))

@bp.route('/history/<item_id>',methods=['GET'])
def view_history(item_id):
    items = []
    i = Item.query.filter_by(id=item_id).first_or_404()
    items.append(i)
    prev_id = i.previous_version_id
    while prev_id:
        prev_i = Item.query.filter_by(id=prev_id).first()
        items.append(prev_i)
        prev_id = prev_i.previous_version_id
    return render_template('viewHistory.html',items=items)
