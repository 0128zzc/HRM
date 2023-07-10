from modules.usesr import db
from modules.applications import Applications
class Application_position(db.Model):
    __tablename__ = 'application_position'
    id = db.Column(db.Integer,primary_key=True)
    appName = db.Column(db.String,db.ForeignKey(Applications.name))
    application = db.relationship(Applications,backref="fitJobs")
    posName = db.Column(db.String(100))
    matchRate = db.Column(db.Integer)