from flask import Blueprint
from flask import redirect, request

bp = Blueprint('profiles', __name__)

@bp.route('/')
@bp.route('/home')
def home():
    return 'Welcome to profiles!'
