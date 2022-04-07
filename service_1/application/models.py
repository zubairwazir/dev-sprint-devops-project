from . import db


class Drinks(db.Model):
    drinks_id = db.Column(db.Integer, nullable=False, primary_key=True)
    alc_drink = db.Column(db.String(20), nullable=False)
    soft_drink = db.Column(db.String(20), nullable=False)
    price = db.Column(db.Float)
