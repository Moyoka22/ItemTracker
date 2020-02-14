from app import db 

class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(255))
    owner = db.Column(db.String(120))
    created = db.Column(db.DateTime())
    archived = db.Column(db.DateTime())
    previous_version_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    newer_version = db.relationship('Item',backref='previous_version',lazy=True,remote_side=[id],uselist=False)
    is_archived = False
    
    def archive(self):
        self.is_archived = True
    
    def has_previous(self):
        return (self.previous_version is not None)
        
    def is_latest(self):
        return (self.newer_version is None)

    def update_item(self, newer_version):
        self.archive = True
        self.newer_version =  newer_version
        newer_version.previous_version = self


    def __repr__(self):
        return f'<Item {self.id} : {self.name}>'