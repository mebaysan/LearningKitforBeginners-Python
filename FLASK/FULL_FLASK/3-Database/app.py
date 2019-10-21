from flask import Flask,render_template,redirect,url_for,g,request
import sqlite3 
import os

app = Flask(__name__)
app.config['DEBUG']=True
app.config['SECRET_KEY'] = "cokgizlisifre"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_URL = os.path.join(BASE_DIR, "3-Database","database.db")
def connect_db():
    conn = sqlite3.connect(DB_URL)
    conn.row_factory = sqlite3.Row
    return conn
def get_db():
    if not hasattr(g,'sqlite3'):
        g.sqlite_db=connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g,'sqlite_db'):
        g.sqlite_db.close()

@app.route("/")
def index():
    db = get_db()
    cursor = db.execute('select * from Users')
    results = cursor.fetchall()
    return render_template("index.html",results=results)

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template("form.html")
    elif request.method=="POST":
        name = request.form['name']
        location = request.form['location']
        db = get_db()
        db.execute("insert into Users (name,location) values (?,?)",[name,location])
        db.commit()
        return redirect(url_for('index'))





if __name__=="__main__":
    app.run()