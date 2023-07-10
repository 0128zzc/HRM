from flask import Blueprint,jsonify,request
from modules.upload import Upload
import calendar,time,os
from flask_jwt_extended import jwt_required
resumeload_bp = Blueprint("resumeLoad",__name__)


@resumeload_bp.route("/")
@jwt_required()
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

@resumeload_bp.route("/send",methods=['POST'])
def resumeSend():
    file = request.files.get('file')
    if file is None:
        # 表示没有发送文件
        return {
            'message': "文件上传失败"
        }
    file_name = file.filename
    # print(file.filename)
    # 获取前缀（文件名称）print(os.path.splitext(file_name)[0])
    # 获取后缀（文件类型）print(os.path.splitext(file_name)[-1])
    suffix = os.path.splitext(file_name)[-1]  # 获取文件后缀（扩展名）
    basePath = os.path.dirname(__file__)  # 当前文件所在路径print(basePath)
    # nowTime = calendar.timegm(time.gmtime())  # 获取当前时间戳改文件名print(nowTime)
    nowTime = os.path.splitext(file_name)[0]
    # print(nowTime)
    upload_path = os.path.join(basePath, 'upload',
                               str(nowTime))  # 改到upload目录下# 注意：没有的文件夹一定要先创建，不然会提示没有该路径print(upload_path)
    upload_path = os.path.abspath(upload_path)  # 将路径转换为绝对路径print("绝对路径：",upload_path)
    # print(os.path.splitext(file_name)[0])
    file.save(upload_path + suffix)  # 保存文件
    # http 路径
    url = 'http://xxxx.cn/upload/' + str(nowTime)  + suffix

    return {
        'code': 200,
        'messsge': "文件上传成功",
        'fileNameOld': file_name,
        'fileNameSave': str(nowTime) + str(nowTime) + suffix,
        'url': url
    }
