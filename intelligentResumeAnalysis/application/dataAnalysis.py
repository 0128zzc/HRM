from flask import Blueprint,jsonify,request
from modules.applications import Applications
from modules.application_position import Application_position
from modules.position import Position
analysis_bp = Blueprint("analysis",__name__)

@analysis_bp.route("/")
def hello():
    return "hi,jay"


@analysis_bp.route("/sexRate")
def getSexRate():
    position = request.values.get("position")
    if position == "全部":
        print(position)
        print("Hello")
        womanCount = Applications.query.filter(Applications.sex == "女").count()
        manCount = Applications.query.filter(Applications.sex == "男").count()
        otherCount = Applications.query.filter(Applications.sex == "未知").count()
        return [
            {"name": "女", "value": womanCount},
            {"name": "男", "value": manCount},
            {"name": "未知", "value": otherCount}
        ]
    else:
        print(position)
        print("Hello1")
        results = Application_position.query.filter(Application_position.posName == position).all()


        womanCount = 0
        manCount = 0
        otherCount = 0
        for result in results:
            if result.application.sex == "女":
                womanCount+=1
            elif result.application.sex == "男":
                manCount+=1
            else:
                otherCount+=1
        return [
            {"name": "女", "value": womanCount},
            {"name": "男", "value": manCount},
            {"name": "未知", "value": otherCount}
        ]



@analysis_bp.route("/education")
def getEducation():
    position = request.values.get("position")
    if position == "全部":
        highSchool = Applications.query.filter(Applications.educations == "高中及以下").count()
        undergraduate = Applications.query.filter(Applications.educations == "本科").count()
        postgraduate = Applications.query.filter(Applications.educations == "研究生").count()
        docter = Applications.query.filter(Applications.educations == "博士生").count()
        return [
            {"name": "高中及以下", "value": highSchool},
            {"name": "本科", "value": undergraduate},
            {"name": "研究生", "value": postgraduate},
            {"name": "博士生", "value": docter},

        ]
    else:
        results = Application_position.query.filter(Application_position.posName == position).all()
        highSchool, undergraduate, postgraduate, docter = 0, 0, 0, 0
        for result in results:
            if result.application.educations== "本科":
                undergraduate+=1
            elif result.application.educations == "研究生":
                postgraduate+=1
            elif result.application.educations == "博士生":
                docter+=1
            else:
                highSchool+=1
        return [
            {"name": "高中及以下", "value": highSchool},
            {"name": "本科", "value": undergraduate},
            {"name": "研究生", "value": postgraduate},
            {"name": "博士生", "value": docter},

        ]

@analysis_bp.route("/schoolType")
def getSchoolType():
    position = request.values.get("position")
    if position == "全部":
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
    else:
        results = Application_position.query.filter(Application_position.posName == position).all()
        nine = 0
        two = 0
        normal = 0
        high = 0
        shuang = 0
        for result in results:
            if result.application.schoolGrade == "985":
                nine+=1
            elif result.application.schoolGrade == "211":
                two+=1
            elif result.application.schoolGrade == "双一流":
                shuang+=1
            elif result.application.schoolGrade == "普通本科":
                normal+=1
            else:
                high+=1
        return [
            {"name": "985", "value": nine},
            {"name": "211", "value": two},
            {"name": "双一流", "value": shuang},
            {"name": "普通本科", "value": normal},
            {"name": "高中及以下", "value": high},
        ]

@analysis_bp.route("/ageRate")
def getAgeRate():
    position = request.values.get("position")
    if position == "全部":
        count1 = Applications.query.filter(Applications.age.between(0, 17)).count()
        count2 = Applications.query.filter(Applications.age.between(18, 30)).count()
        count3 = Applications.query.filter(Applications.age.between(31, 40)).count()
        count4 = Applications.query.filter(Applications.age.between(41, 50)).count()
        count5 = Applications.query.filter(Applications.age.between(51, 100)).count()
        return {
            "ranges":["17岁及以下","18-30","31-40","41-50","51岁及以上"],
            "values":[count1,count2,count3,count4,count5]
        }
    else:
        results = Application_position.query.filter(Application_position.posName == position).all()
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        for result in results:
            if result.application.age>=51:
                count5+=1
            elif result.application.age>=41:
                count4+=1
            elif result.application.age>=31:
                count3+=1
            elif result.application.age>=18:
                count2+=1
            else:
                count1+=1

        return {
            "ranges": ["17岁及以下", "18-30", "31-40", "41-50", "51岁及以上"],
            "values": [count1, count2, count3, count4, count5]
        }

@analysis_bp.route("/salary")
def getSalary():
    years = Position.query.filter(Position.name == "产品运营").all()
    year_dict = [d.__dict__ for d in years]
    year_result = [v for d in year_dict for k, v in d.items() if k == "time"]
    # print(year_dict)
    # print(year_result)

    name_query = Position.query.filter(Position.time == "2020").all()
    name_dict = [d.__dict__ for d in name_query]
    name_results = [v for d in name_dict for k, v in d.items() if k == "name"]
    # print(name_results)

    json_results = []

    for jobName in name_results:
        this_result = Position.query.filter(Position.name == jobName).order_by(Position.time).all()
        this_dict = [k.__dict__ for k in this_result]
        this_query = [v for d in this_dict for k, v in d.items() if k == "salary"]
        # print(this_query)
        json_results.append({"job": jobName, "values": this_query})

    # for name_result in name_results:
    #     values = []
    #     for d in dict_list:
    #         if d["name"] == name_result:

    return jsonify({"ranges": year_result, "details": json_results})
