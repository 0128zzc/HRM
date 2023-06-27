from modules.usesr import db

class Upload(db.Model):
    __tablename__ = 'upload'
    id = db.Column(db.Integer,primary_key=True)
    time = db.Column(db.DateTime)
    number = db.Column(db.Integer)
