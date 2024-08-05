from flask import render_template
from app.main import bp


@bp.route('/')
def index():
    print("Index")
    return render_template('index.html')