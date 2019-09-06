from extensions import db

class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sell = db.Column(db.Integer)
    list = db.Column(db.Integer)
    living = db.Column(db.Integer)
    rooms = db.Column(db.Integer)
    beds = db.Column(db.Integer)
    baths = db.Column(db.Integer)
    age = db.Column(db.Integer)
    acres = db.Column(db.Float)
    taxes = db.Column(db.Integer)