from flask import Blueprint,request,jsonify
from modules.usesr import User
from flask_jwt_extended import create_access_token
from sqlalchemy.orm import sessionmaker
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
load_bp = Blueprint("load_bp",__name__)
from modules.usesr import db


@load_bp.route('/login',methods=['POST'])
def login():
    username = request.args.get("username", None)
    password = request.args.get("password", None)
    reuest = User.query.filter(User.name == username,User.password==password).count()
    if  reuest == 0:
        return "用户名或密码错误"
    access_token = create_access_token(identity=username)
    return access_token


@load_bp.route('/register')
def register():
    return "I`m Gloria"

@load_bp.route('/ttt')
@jwt_required()
def ttt():
    # user = User(name='aaa',password='zzz')
    # db.session.add(user)
    # db.session.commit()
    # username = get_jwt_identity()
    userInfo = get_jwt_identity()
    return jsonify(userInfo)
