from datetime import datetime 
import json

from app import db 

class TimestampMixin(object):
    created = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.now)
class Item(db.Model,TimestampMixin):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(255))
    owner = db.Column(db.String(120))
    archived_timestamp = db.Column(db.DateTime())
    previous_version_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    previous_version = db.relationship('Item',backref='newer_version',lazy=True,remote_side=[id],uselist=False)
    is_archived = db.Column(db.Boolean)
    
    def archive(self):
        self.is_archived = True
        self.archived_timestamp = datetime.utcnow()
    
    def has_previous(self):
        return (self.previous_version is not None)
        
    def is_latest(self):
        if not self.newer_version:
            return True
        else:
            return False

    @staticmethod
    def update_version(older_version, newer_version):
        older_version.archive()
        newer_version.previous_version_id = older_version.id

    def update(self,name,owner,description):
        self.name = name
        self.owner = owner
        self.description = description

    def __repr__(self):
        return f'<Item {self.id} : {self.name}>'

    def json(self):
        data = {}
        data['name'] = self.name
        data['id'] = self.id
        data['owner'] = self.owner
        data['description'] = self.description
        data['archived'] = self.is_archived
        return data