from flask import Blueprint
from app.controllers.views import *

bp = Blueprint('main', __name__)

#! Index
@bp.route('/')
@bp.route('/index')
def index_route():
    return index()
