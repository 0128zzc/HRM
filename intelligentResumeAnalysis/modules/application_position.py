from modules.usesr import db

class Application_position(db.Model):
    __tablename__ = 'application_position'
    id = db.Column(db.Integer,primary_key=True)
    appName = db.Column(db.String(100))
    posName = db.Column(db.String(100))
    matchRate = db.Column(db.Integer)