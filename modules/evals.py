from flask import Blueprint
from flask import redirect, request

bp = Blueprint('evals', __name__)

@bp.route('/')
@bp.route('/home')
def home():
    return 'Welcome to evals!'
