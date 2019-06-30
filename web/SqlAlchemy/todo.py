from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/meb/Desktop/LearningKitforBeginners-Python/web/SqlAlchemy/todo.db'  # uygulamanın veritabanınının yolunu verdik
db = SQLAlchemy(
    app)  # veritabanını uygulama için entegre ettik ( aradaki köprüyü kurduk)


class Todo(db.Model):
    id = db.Column(
        db.Integer, primary_key=True
    )  # integer bir kolon ve bu bir primaryKey'dir. id adında bir kolon
    title = db.Column(
        db.String(80))  # string tipte bir kolon ve en fazla 80 karakter
    complete = db.Column(db.Boolean)  # Boolean(true or false) tipte bir kolon


@app.route("/")
def index():
    todos = Todo.query.all(
    )  # Todo classımızın methodunu kullandık. bize bütün datayı bir sözlük içerisinde verir
    return render_template("index.html", todos=todos) # todos'ları template'a yolluyoruz


@app.route("/add", methods=["POST"])
def add_todo():
    title = request.form.get("title")  # formdan gelen title değerini alıyoruz
    newTodo = Todo(
        title=title, complete=False
    )  # newTodo adında bir değişken oluşturuyoruz ve bunun title'ı formdan gelen data oluyor ve complete özelliği otomatik olarak false belirliyoruz
    db.session.add(newTodo)  # yeni objeyi veritabanına ekledik
    db.session.commit()  # veritabanında değişiklik olduğu için commit ettik
    return redirect(url_for("index"))

@app.route("/complete/<string:id>")
def completeTodo(id):
    todo = Todo.query.filter_by(id=id).first() # buraya yollanan id'yi alacak ve todo nesnesine atacak
    if todo.complete == True: # eğer gelen todo'nun complete'i True ise false yap
        todo.complete = False
    else:
        todo.complete=True
    db.session.commit() # veritabanını kaydet
    return redirect(url_for("index")) # tekrar index'e git

@app.route("/delete/<string:id>")
def deleteTodo(id):
    todo = Todo.query.filter_by(id=id).first() # todoyu yakaladık
    db.session.delete(todo) # todo'yu sildik
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    db.create_all(
    )  # uygulama çalışmadan bir önce veritabanı yoksa oluşturacak
    app.run(debug=True)