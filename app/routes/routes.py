from flask import Blueprint
from app.controllers.views import *

bp = Blueprint('main', __name__)

#! Index
@bp.route('/')
@bp.route('/index')
def index_route():
    return index()

#! Register
@bp.route('/register', methods=['GET', 'POST'])
def register_route():
    return register()

#! Login
@bp.route('/login', methods=['GET', 'POST'])
def login_route():
    return login()

#!logout
@bp.route("/logout")
def logout_route():
    return logout()

#! Dashboard
@bp.route("/dashboard", methods=["GET"])
def dashboard_route():
    return dashboard()

#! Tasks
@bp.route("/tasks", methods=['GET', 'POST'])
def tasks_route():
    return tasks()