from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL

app=Flask(__name__)

@app.route("/")
def indeks():
	articles=[
		{"id":1,"title":"Deneme1","content":"Deneme1 İçerik"},
		{"id":2,"title":"Deneme2","content":"Deneme2 İçerik"},
		{"id":3,"title":"Deneme3","content":"Deneme3 İçerik"}
	]
	return render_template("index.html",articles=articles)
	

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/activities")
def activities():
	return render_template("index.html")







if __name__=="__main__":
	app.run(debug=True)