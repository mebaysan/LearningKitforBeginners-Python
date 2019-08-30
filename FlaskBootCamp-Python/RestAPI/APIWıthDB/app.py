from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
app = Flask(__name__)
api = Api(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + \
    os.path.join(basedir, "data.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)
ponnies = list()


class Ponny(db.Model):
    name = db.Column(db.String(80), primary_key=True)

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name}


class PonnyNames(Resource):
    def get(self, name):
        pon = Ponny.query.filter_by(name=name).first()
        if pon:
            return pon.json()
        else:
            return {'name': None}, 404

    def post(self, name):
        pon = Ponny(name=name)
        db.session.add(pon)
        db.session.commit()
        return pon.json()

    def delete(self, name):
        pon = Ponny.query.filter_by(name=name).first()
        db.session.delete(pon)
        db.session.commit()
        return {"note": "delete success"}


class AllNames(Resource):
    def get(self):
        ponnies = Ponny.query.all()
        return [pon.json() for pon in ponnies]


# ponny names isimli class'a bu url'i bağladık
api.add_resource(PonnyNames, '/ponny/<string:name>')
# allnames adlı class'a bu urli bağladık
api.add_resource(AllNames, '/ponnies')
if __name__ == "__main__":
    app.run(debug=True)
