from flask import Blueprint
from flask import redirect, request

bp = Blueprint('evals', __name__)

@bp.route('/')
@bp.route('/home')
def home():
    return 'Welcome to evals!'

@bp.route('/profile/<uid>')
def profile( uid ):
    return uid;

@bp.route('/admin')
def admin():
    return 'this is for admin'

@bp.route('/attendance')
def attendance():
    return 'this is for taking attendance'

@bp.route('/meeting/<kind>/<ident>')
def meeting( kind, ident ):
    return 'A meeting of type ' + kind + ' with id ' + ident

@bp.route('/meetings/<kind>')
def meetings( kind ):
    return 'All ' + kind + ' meetings'

@bp.route('/projects')
def projects():
    return 'projects'

@bp.route('/contributions')
def contributions():
    return '/contributions'

@bp.route('/overview')
@bp.route('/standings')
@bp.route('/rankings')
def overview():
    return 'this is where you can see everyone'
