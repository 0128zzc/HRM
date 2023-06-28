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
    return [
        {"name": "女", "value": womanCount},
        {"name": "男", "value": manCount},
        {"name": "未知", "value": otherCount}
    ]



@analysis_bp.route("/education")
def getEducation():
    highSchool = Applications.query.filter(Applications.educations=="高中及以下").count()
    undergraduate = Applications.query.filter(Applications.educations=="本科").count()
    postgraduate = Applications.query.filter(Applications.educations == "研究生").count()
    docter = Applications.query.filter(Applications.educations == "博士生").count()
    return [
        {"name": "高中及以下", "value": highSchool},
        {"name": "本科", "value": undergraduate},
        {"name": "研究生", "value": postgraduate},
        {"name": "本科生", "value": docter},

    ]

@analysis_bp.route("/schoolType")
def getSchoolType():
    nine = Applications.query.filter(Applications.schoolGrade == "985").count()
    two = Applications.query.filter(Applications.schoolGrade == "211").count()
    normal = Applications.query.filter(Applications.schoolGrade == "普通本科").count()
    high = Applications.query.filter(Applications.schoolGrade == "高中及以下").count()
    shuang = Applications.query.filter(Applications.schoolGrade == "双一流").count()
    return [
        {"name": "985", "value": nine},
        {"name": "211", "value": two},
        {"name": "双一流", "value": shuang},
        {"name": "普通本科", "value": normal},
        {"name": "高中及以下", "value": high},
    ]

@analysis_bp.route("/ageRate")
def getAgeRate():
    count1 = Applications.query.filter(Applications.age.between(0, 17)).count()
    count2 = Applications.query.filter(Applications.age.between(18, 30)).count()
    count3 = Applications.query.filter(Applications.age.between(31, 40)).count()
    count4 = Applications.query.filter(Applications.age.between(41, 50)).count()
    count5 = Applications.query.filter(Applications.age.between(51, 100)).count()
    return {
        "ranges":["17岁及以下","18-30","31-40","41-50","51岁及以上"],
        "values":[count1,count2,count3,count4,count5]
    }

@analysis_bp.route("/salary")
def getSalary():

    years = Position.query.filter(Position.name == "产品运营").all()
    year_dict = [d.__dict__ for d in years]
    year_result = [  v  for d in year_dict for k,v in d.items() if k=="time"]
    # print(year_dict)
    # print(year_result)

    name_query = Position.query.filter(Position.time == "2020").all()
    name_dict = [d.__dict__ for d in name_query]
    name_results = [ v  for d in name_dict for k,v in d.items() if k=="name"]
    # print(name_results)

    json_results = []

    for jobName in name_results:
        this_result = Position.query.filter(Position.name == jobName).order_by(Position.time).all()
        this_dict = [ k.__dict__ for k in this_result]
        this_query = [ v  for d in this_dict for k,v in d.items() if k=="salary"]
        # print(this_query)
        json_results.append({"job":jobName,"values":this_query})

    # for name_result in name_results:
    #     values = []
    #     for d in dict_list:
    #         if d["name"] == name_result:

    return jsonify({"ranges":year_result, "details":json_results})