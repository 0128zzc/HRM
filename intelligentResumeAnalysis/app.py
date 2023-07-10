from flask import Flask,request,jsonify
from modules.config import Config
from modules.usesr import db
from application.resumeUpload.resumeLoad import resumeload_bp
from application.dataAnalysis import analysis_bp
from application.personJobFit import personfit_bp
from application.load import load_bp
from datetime import timedelta
from flask_cors import CORS
from flask_jwt_extended import JWTManager,get_jwt_identity



app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(resumeload_bp,url_prefix='/resumeLoad')
app.register_blueprint(analysis_bp,url_prefix="/analysis")
app.register_blueprint(personfit_bp,url_prefix="/jobFit")
app.register_blueprint(load_bp)
cors = CORS(app,supports_credentials=True)
jwt = JWTManager()
app.config['SECRET_KEY'] = "secret key"
# 设置普通JWT过期时间
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=3)
# 设置刷新JWT过期时间
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
jwt.init_app(app)
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# @app.before_request
# def before_request():
#     # 获取JWT令牌
#     token = request.headers.get('Authorization')
#     print("检验检验")
#     # 在这里可以进行JWT令牌的验证逻辑
#     # 例如，使用Flask-JWT-Extended提供的方法验证令牌的有效性
#
#     # 如果令牌验证失败，可以根据需求返回适当的响应或执行其他操作
#
#     # 如果令牌验证成功，可以使用get_jwt_identity()获取当前用户的身份信息
#     current_user = get_jwt_identity()
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify(msg='token过期了哟'),201


if __name__ == '__main__':

    app.run()
