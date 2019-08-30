import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddForm, DelForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
###########################
### SQL DATABASE BÖLÜMÜ ###
###########################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + \
    os.path.join(basedir+"data.sqlite")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)
###########################
###    MODELS    BÖLÜMÜ ###
###########################


class Ponny(db.Model):
    __tablename__ = 'ponnies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Ponny name is {self.name}"
###########################
###    VİEWS     BÖLÜMÜ ###
###########################
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add',methods=['GET','POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_ponny = Ponny(name)
        db.session.add(new_ponny)
        db.session.commit()
        return redirect(url_for('liste'))
    return render_template('add.html', form=form)


@app.route('/list')
def liste():
    ponnies = Ponny.query.all()
    return render_template('list.html', ponnies=ponnies)


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        ponny = Ponny.query.get(id)
        db.session.delete(ponny)
        db.session.commit()
        return redirect(url_for('liste'))
    return render_template('delete.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
