from flask import Flask
from modules.config import Config
from modules.usesr import db
from application.resumeUpload.resumeLoad import resumeload_bp
from application.dataAnalysis import analysis_bp
from application.personJobFit import personfit_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(resumeload_bp,url_prefix='/resumeLoad')
app.register_blueprint(analysis_bp,url_prefix="/analysis")
app.register_blueprint(personfit_bp,url_prefix="/jobFit")

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
