from flask import Blueprint,request

load_bp = Blueprint("load_bp",__name__)


@load_bp.route('/load')
def load():
    return "Hi,Jay"


@load_bp.route('/register')
def register():
    return "I`m Gloria"