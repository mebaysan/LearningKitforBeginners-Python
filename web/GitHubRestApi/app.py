from flask import Flask, render_template,request
import requests
app = Flask(__name__)

base_url = "https://api.github.com/users/"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        github_name = request.form.get("githubname") # request'e gelen formdaki name alanı github olan form elementinden data aldık
        response_user = requests.get(base_url+github_name) # base url'e github name ekleyip get isteği atıyoruz ki api'den data alalım
        response_repos = requests.get(base_url + github_name + "/repos")
        user_info = response_user.json() # gelen json data bir dictionary olarak kullanılabilir
        user_repos = response_repos.json()

        if "message" in user_info:
            return render_template("index.html",error="Kullanıcı Bulunamadı!")
        else:
            return render_template("index.html",profile=user_info,repos=user_repos) # aldığımız user_info(kullanıcıya ait bilgiler)'u template'a gönderiyoruz
    else:
        return (render_template("index.html"))


if __name__ == "__main__":
    app.run(debug=True)
