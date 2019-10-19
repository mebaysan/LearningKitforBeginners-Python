from flask import Flask,render_template,request

app = Flask(__name__)
app.config['DEBUG']=True

@app.route("/")
def index():
    return render_template("index.html") # bu şekilde bir template döndürebilirz.

@app.route("/theform",methods=["GET","POST"])
def theform():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        name = request.form.get("name")
        location = request.form.get("location")
        return render_template("form2.html",name=name,location=location)
if __name__ == "__main__":
    app.run()