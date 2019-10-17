import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)
"""
flask
flask-wtf
flask-sqlalchemy
flask-migrate
flask db init
flask db migrate -m "mesaj"
flask db upgrade
"""

class Ponny(db.Model):
    __tablename__ = 'ponnies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # relationship -> diğer tablo ile birbirine bağlar
    # ONE TO MANY -> One Ponny to  Many Toys -> Bire çok
    # toy modeli ile birbirine bağladık. backref -> bağladığı tabloya da burda ne ile bağladığını verir
    # burada uselist default True gelir. bağlı olduğu değer liste olabailir sebebi ise one to many bir çok ilişkidir
    toys = db.relationship('Toy', backref='ponny', lazy='dynamic')
    # ONE TO ONE -> One Ponny to One Owner -> Bire bir
    # uselist=False -> bağlı olduğu model bir liste olmasın çünkü one to one ilişki
    owner = db.relationship('Owner', backref='ponny', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Ponny name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Ponny name is {self.name} and has no owner yet!"

    def report_toys(self):
        print("Here are my toys:")
        for toy in self.toys:
            # bağlı olduğu tablodaki oyuncağın kendi tablosundaki adı
            print(toy.item_name)


class Toy(db.Model):
    __tablename__ = 'toys'
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Text)
    # bu class'ın ponny_id adlı fieldı ponnies tablosunun id kolonuna bağlıdır
    ponny_id = db.Column(db.Integer, db.ForeignKey('ponnies.id'))

    def __init__(self, item_name, ponny_id):
        self.item_name = item_name
        self.ponny_id = ponny_id


class Owner(db.Model):
    __tablename__ = 'owners'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    ponny_id = db.Column(db.Integer, db.ForeignKey('ponnies.id'))

    def __init__(self, name, ponny_id):
        self.name = name
        self.ponny_id = ponny_id
    

if __name__ == "__main__":
    app.run(debug=True)
