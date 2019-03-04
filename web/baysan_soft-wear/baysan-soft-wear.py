from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators

    






app=Flask(__name__)


app.config["MYSQL_HOST"]="127.0.0.1"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="baysan_soft-wear"
app.config["MYSQL_CURSORCLASS"]="DictCursor"

mysql=MySQL(app)

@app.route("/",methods=["GET","POST"])
def index():
     if request.method == "GET":
        email = request.form.get
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO mails(email) VALUES(%s)",(email,))
        mysql.connection.commit()
        cursor.close()
        return render_template("index.html")
    
    



if __name__ == "__main__":
    app.run(debug=True)