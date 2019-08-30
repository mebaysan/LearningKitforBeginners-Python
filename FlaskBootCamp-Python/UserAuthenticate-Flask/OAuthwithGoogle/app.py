from flask import Flask, redirect, url_for, render_template
from flask_dance.contrib.google import make_google_blueprint, google
import os
# os içerisindeki OAUTHLIB_INSECURE_TRANSPORT değerini 1 ile değiştiriyoruz
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
blueprint = make_google_blueprint(
    client_id='846442587444-1cgpb4pfads13om9p8d51rukhdb1f769.apps.googleusercontent.com', client_secret='yllWN9RN9-0FNKXQWWlwThvR', offline=True, scope=['profile', 'email'])

app.register_blueprint(blueprint, url_prefix='/login')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome')
def welcome():
    # Eğer giriş yapılmazsa ERROR INTERNAL SERVER hatası döndürür
    response = google.get('/oauth2/v2/userinfo')
    assert response.ok, response.text
    email = response.json()['email']
    return render_template('welcome.html', email=email)


@app.route('/login/google')
def login():
    if not google.authorized:
        # google login sayfası flask-dance tarafından bize otomatik olarak verilir
        return render_template(url_for('google.login'))
    response = google.get('/oauth2/v2/userinfo')
    assert response.ok, response.text
    email = response.json()['email']  # response'daki email'i yakala
    return render_template('welcome.html', email=email)


if __name__ == "__main__":
    app.run(debug=True)
