# __init__.py 'project' dizini altında,
from project.owners.views import owners_blueprint
from project.ponnies.views import ponnies_blueprint
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)
# uygulamamızı böldüğümüz için blueprints'lerimizi uygulama ile birleştirdik
"""
Flask Blueprint ne işe yarar?
uygulamamızı bölmemize ve daha rahat kontrol edebilmemizi sağlar.
Django'daki gibi uygulamayı daha rahat kontrol edebiliriz.
"""
app.register_blueprint(owners_blueprint, url_prefix='/owners')
app.register_blueprint(ponnies_blueprint, url_prefix='/ponnies')
