import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # pip install flask-migrate
"""
export/set FLAS_APP=app.py
flask db migrate -"message"
flask db migrate -m "crated person database"
flask db upgrade
flask db migrate -m "added new columns"
flask db upgrade
"""
# /home/el-nasyab/Desktop/FlaskBootCamp-Python/SQLDatabases-Flask
# -> programın çalıştığı dizini verir
basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ -> app.py

app = Flask('__name__')
# sqlalchemy için veri tabanının yerini veriyoruz
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                        os.path.join(basedir, 'data.sqlite')
app.config['SQLACHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # bu uygulama için bir veri tabanı oluşturur
Migrate(app, db) # uygulamamızı ve database'imizi birbirine bağlıyoruz


class Person(db.Model):
    # eğer bunu vermezsek otomatik olarak model aldığı class'ın adını verir(person)
    __tablename__ = 'persons'
    # integer tipinde bir kolon ve primary olacak dedik
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person {self.name} is {self.age} years old"


if __name__ == '__main__':
    app.run(debug=True)
