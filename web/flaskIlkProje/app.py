from flask import Flask, render_template, redirect, url_for, session, logging, request, flash
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
import sqlite3
from functools import wraps # decorator kullanmak için
from datetime import datetime


# Kullanıcı kayıt formu
class RegisterForm(Form):  # Bir form class oluşturduk
    name = StringField("İsim Soyisim", validators=[validators.length(min=4, max=25), validators.DataRequired()])
    userName = StringField("Kullanıcı Adı", validators=[validators.length(min=5, max=35), validators.DataRequired()])
    email = StringField("Email Adresi", validators=[validators.DataRequired(),
                                                    validators.Email(message="Lütfen geçerli bir mail adresi gir  ")])
    password = PasswordField("Parola", validators=[validators.DataRequired(message="Lütfen parola belirle"),
                                                   validators.EqualTo(fieldname="confirm", message="Parola uyuşmadı!")])
    confirm = PasswordField("Parola doğrula")


class LoginForm(Form):
    userName = StringField("Kullanıcı Adı")
    password = PasswordField("Şifre")


class User():
    def __init__(self, name, userName, email, password):
        self.name = name
        self.userName = userName
        self.email = email
        self.password = password


app = Flask(__name__)
app.secret_key = "baysanblog"  # flash mesajalrını kullanmamız için secret keyimizin olması lazım


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/register', methods=["GET", "POST"])  # bu url'e hem post hem get request yapılacak dedik
def register():
    form = RegisterForm(request.form)  # bu url' göndereceğimiz form'u oluşturduk
    if request.method == "POST" and form.validate():  # eğer url'e gelen request POST ise ve form.validate -> formda
        # sıkıntı yoksa true gelecek
        name = form.name.data  # form içindeki name değerinin datası(değeri)
        userName = form.userName.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)  # parolayı şifreleyerek alıyoruz
        user = User(name, userName, email, password)
        # VERİTABANI BAĞLANTISI
        conn = sqlite3.connect('baysanblog.db')
        sorgu = "Insert into users (name,email,userName,password) VALUES (?,?,?,?)"
        conn.execute(sorgu, (user.name, user.email, user.userName, user.password))
        conn.commit()  # veritabanına sorgu attığımızda bir şeyler değişiyor ise(insert,update,delete) commit yapmalıyız
        conn.close()  # işimiz bitince bağlantıyı kapatıyoruz
        flash('Başarıyla Kayıt Oldunuz..', 'success')
        return redirect(url_for("login"))  # redirect(url_for()) -> içeri gelen parametre adındaki method(fonksiyon) a
        # bağlı fonksiyondaki url'e gönder
    else:  # eğer gelen request get ise
        return render_template("register.html", form=form)  # register.html döndür ve form değişkenini yolla


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":  # eğer method post ise
        userName = form.userName.data  # url'deki form'dan veriyi al
        password_entered = form.password.data
        conn = sqlite3.connect('baysanblog.db')
        cursor = conn.cursor()  # bir cursor oluşturduk
        sorgu = "Select * from users where userName = ?"  # sorgumuzu hazırlıyoruz
        result = cursor.execute(sorgu, (
        userName,)).fetchone()  # result değişkenine sorgumuzu atıyoruz, fethone -> gelen değerin değerini(data(dictionary)) alır
        if result:  # eğer result true (döner) ise
            userName_real = result[3]  # gelen result(dictionary)ın 4. değişkenini al
            password_real = result[4]  # gelen result(dictionary)ın 5. değişkenini al
            if sha256_crypt.verify(password_entered,
                                   password_real):  # eğer password_entered ile password_real eşleşirse(encrypt edilip)
                flash("Başarıyla Giriş Yaptınız..", "success")  # flash mesajı patlat
                session["logged_in"] = True # session değeri atadık bu sayede mesela navbar'da çeşitli oynamalar yapabildik
                session["userName"] = userName
                return redirect(url_for("index"))  # ve index fonksiyonuna redirect at
            else:  # eğer şifre(encrypt) eşleşmez ise
                flash("Parolanızı yanlış girdiniz!", "danger")
                return redirect(url_for('login'))  # tekrar login methoduna(fonksiyon) yönlendir

        else:  # eğer result gelmezse(false)
            flash("Böyle bir kullanıcı bulunmuyor!", "danger")
            return redirect(url_for("login"))

    return render_template('login.html', form=form)  # eğer method post değil ise(get vs..) form değerini yolla


@app.route('/logout')
def logout():
    session.clear() # session'ı öldürecek
    return redirect(url_for("index"))

#Kullanıcı giriş decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session: # sesion içinde "logged_in" değeri var mı yok mu
            return f(*args, **kwargs)
        else:
            flash("Lütfen Giriş Yapın...","danger")
            return redirect(url_for("login"))
    return decorated_function


@app.route('/dashboard')
@login_required # bu fonksiyon öncesinde bu decorator çalışacak
def dashboard():
    conn = sqlite3.connect("baysanblog.db")
    cursor = conn.cursor()
    sorgu = "Select * from articles where author = ?"
    result = cursor.execute(sorgu,(session["userName"],)).fetchall()
    if result :
        articles = result
        return render_template("dashboard.html",articles=articles)
    else:
        return render_template('dashboard.html')


@app.route("/addArticle",methods=["GET","POST"])
def addArticle():
    form = ArticleForm(request.form)
    if request.method=="POST" and form.validate():
        title = form.title.data
        content = form.content.data
        dateNow = datetime.now().strftime("%B %d, %Y %I:%M%p") # gelen datayı formatladık
        conn = sqlite3.connect('baysanblog.db')
        cursor = conn.cursor()  # bir cursor oluşturduk
        sorgu = "Insert into articles(title,author,content,createdDate) VALUES (?,?,?,?)"
        cursor.execute(sorgu,(title,session["userName"],content,dateNow))
        conn.commit()
        conn.close()
        flash("Makale Başarıyla Oluşturuldu","success")
        return redirect(url_for("dashboard"))
    else:
        return render_template("addArticle.html", form=form)


#Makale Form
class ArticleForm(Form):
    title = StringField("Makale Başlığı",validators=[validators.length(min=5, max=100)])
    content = TextAreaField("İçerik",validators=[validators.length(min=10)])


@app.route('/articles')
def articles():
    conn = sqlite3.connect('baysanblog.db')
    cursor = conn.cursor()  # bir cursor oluşturduk
    sorgu = "Select * from articles"
    result = cursor.execute(sorgu).fetchall()
    #print("result = {}".format(result[0][0]))
    if result:
        articles = result
        return render_template('articles.html',articles=articles)
    else:
        return render_template('articles.html')




@app.route("/article/<string:id>")
def article(id):
    conn = sqlite3.connect("baysanblog.db")
    cursor = conn.cursor()
    sorgu = "Select * from articles where id = ?"
    result = cursor.execute(sorgu,(id,)).fetchone()
    #print(result)
    if result:
        article = result
        return render_template("article.html",article=article)
    else:
        return render_template("article.html")


#Makale silme
@app.route("/delete/<string:id>")
@login_required
def delete(id):
    conn = sqlite3.connect("baysanblog.db")
    cursor = conn.cursor()
    sorgu = "Select * from articles where author = ? and id = ?"
    result = cursor.execute(sorgu,(session["userName"],id)).fetchone()
    if result:
        sorgu2 = "Delete from articles where id = ?"
        cursor.execute(sorgu2,(id,))
        conn.commit()
        flash("Makale Başarıyla Silindi...","success")
        return redirect(url_for("dashboard"))

    else:
        flash("Böyle bir makale yok veya makaleyi silme yetkiniz yok...","danger")
        return redirect(url_for("index"))




#Makale güncelleme
@app.route("/update/<string:id>",methods=["GET","POST"])
@login_required
def update(id):
    if request.method=="GET":
        conn = sqlite3.connect("baysanblog.db")
        cursor = conn.cursor()
        sorgu = "Select * from articles where id = ? and author = ?"
        result = cursor.execute(sorgu,(id,session["userName"])).fetchone()
        if result:
            article = result
            form = ArticleForm()
            form.title.data= article[2]
            form.content.data=article[3]
            return render_template("update.html",form=form)

        else:
            flash("Böyle bir makale yok veya bu işleme yetkiniz yok!","danger")
            return redirect(url_for("index"))
    else:
        conn = sqlite3.connect("baysanblog.db")
        cursor = conn.cursor()
        form = ArticleForm(request.form)
        newTitle = form.title.data
        newContent = form.content.data
        sorgu2 = "Update articles Set title = ?,content = ? where id = ? "
        cursor.execute(sorgu2,(newTitle,newContent,id))
        conn.commit()
        flash("Makale başarıyla güncellendi","success")
        return redirect(url_for("dashboard"))





#Arama URL
@app.route("/search",methods=["GET","POST"])
def search():
    if request.method=="GET":
        return redirect(url_for("index"))
    else:
        keyWord = request.form.get("keyWord")
        conn = sqlite3.connect("baysanblog.db")
        cursor = conn.cursor()
        sorgu ="Select * from articles where title like '%" + keyWord+"%'"
        result = cursor.execute(sorgu).fetchall()
        if result:
            articles = result
            return render_template("articles.html",articles=articles)
        else:
            flash("Aranan kelimeye uygun makale bulunamadı...","warning")
            return redirect(url_for("articles"))



if __name__ == '__main__':
    app.run(debug=True)
