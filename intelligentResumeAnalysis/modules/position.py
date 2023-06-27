from modules.usesr import db

class Position(db.Model):
    __tablename__ = 'position'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    time = db.Column(db.Integer)
    salary = db.Column(db.Integer)
    number = db.Column(db.Integer)