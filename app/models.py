from app import db 


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(255))
    owner = db.Column(db.String(120))

    def __repr__(self):
        return f'<Item {self.id} : {self.name}>'