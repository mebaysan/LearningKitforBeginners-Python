from flask import render_template, request, Blueprint

# blueprint'e core adını verdik ve bu app ile bağladık
core = Blueprint('core', __name__)


@core.route('/')
def index():
    return render_template('index.html')


@core.route('/info')
def info():
    return render_template('info.html')
