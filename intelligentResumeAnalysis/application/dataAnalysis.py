from flask import Blueprint,jsonify
from modules.applications import Applications
from modules.position import Position
analysis_bp = Blueprint("analysis",__name__)

@analysis_bp.route("/")
def hello():
    return "hi,jay"


@analysis_bp.route("/sexRate")
def getSexRate():
    womanCount = Applications.query.filter(Applications.sex=="女").count()
    manCount = Applications.query.filter(Applications.sex == "男").count()
    otherCount = Applications.query.filter(Applications.sex == "未知").count()
    return {"woman":womanCount,"man":manCount,"other":otherCount}


@analysis_bp.route("/education")
def getEducation():
    highSchool = Applications.query.filter(Applications.educations=="高中及以下").count()
    undergraduate = Applications.query.filter(Applications.educations=="本科").count()
    postgraduate = Applications.query.filter(Applications.educations == "研究生").count()
    docter = Applications.query.filter(Applications.educations == "博士生").count()
    return {"高中及以下":highSchool,"本科生":undergraduate,"研究生":postgraduate,"博士生":docter}

@analysis_bp.route("/ageRate")
def getAgeRate():
    count1 = Applications.query.filter(Applications.age.between(0, 17)).count()
    count2 = Applications.query.filter(Applications.age.between(18, 30)).count()
    count3 = Applications.query.filter(Applications.age.between(31, 40)).count()
    count4 = Applications.query.filter(Applications.age.between(41, 50)).count()
    count5 = Applications.query.filter(Applications.age.between(51, 100)).count()
    return {"17岁及以下":count1,"18-30岁":count2,"31-40岁":count3,"41-50岁":count4,"51岁及以上":count5}

@analysis_bp.route("/salary")
def getSalary():
    results = Position.query.all()
    dict_list = [obj.__dict__ for obj in results]
    json_results = [{k:v for k,v in d.items() if k=="name" or k=="time" or k=="salary"} for d in dict_list]
    return jsonify({"date":json_results})