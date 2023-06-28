from flask import Blueprint,jsonify
from modules.upload import Upload
resumeload_bp = Blueprint("resumeLoad",__name__)


@resumeload_bp.route("/")
def Hello():
    return "Helloo"


@resumeload_bp.route('/uploadSum')
def getUploadSum():
    results = Upload.query.count()
    return jsonify({"data":results})


@resumeload_bp.route("/uploadDetails")
def getUploadDetails():
    results = Upload.query.all()
    dict_list = [obj.__dict__ for obj in results]
    json_results = [{k: v for k, v in d.items() if k != "_sa_instance_state" and k != "isNewAdd"} for d in dict_list]
    return jsonify({'data': json_results})