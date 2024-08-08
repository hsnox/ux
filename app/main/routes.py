from flask import render_template
from app.main import bp


@bp.route('/')
def index():
    print("Index")
    return render_template('index.html')

@bp.route('/development_objectives')
def development_objectives():
    print("Development Objectives")
    return render_template('development_objectives.html')