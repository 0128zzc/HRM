from modules.usesr import db

class Applications(db.Model):
    __tablename__ = "applications"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    sex = db.Column(db.String(100))
    age = db.Column(db.Integer)
    contact = db.Column(db.String(100))
    educations = db.Column(db.String(100))
    undergraduate = db.Column(db.String(100))
    postgraduate = db.Column(db.String(100))
    doctor = db.Column(db.String(100))
    schoolGrade = db.Column(db.String(100))
    workTime = db.Column(db.Integer)
    vocationalSkills = db.Column(db.String(100))
    honor = db.Column(db.String(100))
    traits = db.Column(db.String(100))
    interest = db.Column(db.String(100))
    salary =db.Column(db.Integer)

