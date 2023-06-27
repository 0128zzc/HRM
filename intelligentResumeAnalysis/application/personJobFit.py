from flask import Blueprint,jsonify,request
from modules.applications import Applications
from modules.application_position import Application_position
personfit_bp = Blueprint("person",__name__)

@personfit_bp.route('/')
def hello():
    return "Hi"

@personfit_bp.route("/selectPerson",methods=["GET"])
def getCandidates():
    age_s = int(request.args.get("startAge"))
    age_e = int(request.args.get("endAge"))
    print(age_e)
    sex = request.args.get("sex")
    education= request.args.get("education")
    schoolType = request.args.get("schoolType")
    job = request.args.get("job")
    dict_list = []
    if job == "全部":
        if schoolType == "全部":
            if education == "全部":
                results = Applications.query.filter(Applications.age>age_s,Applications.age<age_e).all()
                dict_list=[k.__dict__ for k in results]
            else:
                results = Applications.query.filter(Applications.age > age_s, Applications.age < age_e,Applications.educations==education).all()
                dict_list = [k.__dict__ for k in results]
        else:
            if education == "全部":
                results = Applications.query.filter(Applications.age > age_s, Applications.age < age_e,Applications.schoolGrade==schoolType).all()
                dict_list = [k.__dict__ for k in results]
            else:
                results = Applications.query.filter(Applications.age > age_s, Applications.age < age_e,Applications.schoolGrade==schoolType,Applications.educations==education).all()
                dict_list = [k.__dict__ for k in results]
    else:
        name_results = Application_position.query.filter(Application_position.posName==job)
        name_dicts = [k.__dict__ for k in name_results]
        if schoolType == "全部":
            if education == "全部":
                dict_list=[]
                for name_dict in name_dicts:
                    result = Applications.query.filter(Applications.age>age_s,Applications.age<age_e,Applications.name==name_dict.appName).first
                    dict_list.append(result.__dict__)
            else:
                dict_list = []
                for name_dict in name_dicts:
                    result = Applications.query.filter(Applications.age > age_s, Applications.age < age_e,
                                                       Applications.name == name_dict.appName).first,Applications.educations==education
                    dict_list.append(result.__dict__)
        else:
            if education == "全部":
                dict_list = []
                for name_dict in name_dicts:
                    result = Applications.query.filter(Applications.age > age_s, Applications.age < age_e,
                                                       Applications.name == name_dict.appName,Applications.schoolGrade == schoolType).first
                    dict_list.append(result.__dict__)
            else:
                dict_list = []
                for name_dict in name_dicts:
                    result = Applications.query.filter(Applications.age > age_s, Applications.age < age_e,
                                                       Applications.name == name_dict.appName,Applications.schoolGrade == schoolType,Applications.educations==education).first
                    dict_list.append(result.__dict__)
    json_results = [{ k:v for k,v in d.items() if k!= "_sa_instance_state"  } for d in dict_list]
    return jsonify({"data":json_results})


