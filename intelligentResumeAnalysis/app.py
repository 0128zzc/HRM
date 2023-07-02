from flask import Flask
from modules.config import Config
from modules.usesr import db
from application.resumeUpload.resumeLoad import resumeload_bp
from application.dataAnalysis import analysis_bp
from application.personJobFit import personfit_bp
from application.load import load_bp
from datetime import timedelta
from flask_cors import CORS
from flask_jwt_extended import JWTManager



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


if __name__ == '__main__':

    app.run()
