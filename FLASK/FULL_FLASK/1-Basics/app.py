from flask import Flask, jsonify,request,url_for,redirect,session

app = Flask(__name__)
app.config['DEBUG']=True # bu şekilde uygulamanın config'lerini ayarlayabiliriz
app.config['SECRET_KEY'] = 'Cokgizlisifre!'
@app.route("/") # her url için bir decorator gereklidir
def index():
    return "<h1>Hello From Flask</h1>"


@app.route("/home",methods=['GET','POST']) # hem get hem de post methodu gelebilir dedik
def home():
    return "<h1>Home Page</h1>"


@app.route("/json")
def json():
    return jsonify({"key": "value", "key2": [1, 2, 3]}) # bu şekilde json'da döndürebiliriz



@app.route("/deneme",defaults={'parametre':'İsim'}) # bu şekilde bu sayfaya gelen parametrelerin defaultunu belirleyebiliriz
@app.route("/deneme/<string:parametre>") # gelecek parametrelerin tiplerini belirleyebiliriz
def deneme(parametre): # bu şekilde parametreleri yakalayabiliriz
    return "<h1>Merhaba {} deneme sayfasındasın</h1>".format(parametre)


@app.route('/query')
def query():
    # http://127.0.0.1:5000/query?name=Enes&location=İstanbul
    name = request.args.get('name') # bu şekilde GET parametrelerini yakalayabiliriz
    location = request.args.get('location')
    return "<h1>Merhaba {}! Aramıza {}'dan katılıyorsun. Şuanda Query sayfasındasın.</h1>".format(name,location)


@app.route('/theform',methods=['GET','POST'])
def theform():
    if request.method == 'GET': # eğer method GET ise formu göster
        return '''<form method="POST" action="/theform">
                    <input type="text" name="name">
                    <input type="text" name="location">
                    <input type="submit" value="Submit">
                </form>'''
    else: # eğer method GET değilse (ki bu durumda POST olur) formdan değerleri yakala ve döndür
        name = request.form['name'] 
        # location = request.form['location']
        # return "<h3>Merhaba {}! Aramıza {}'dan katılıyorsun. Başarıyla kayıt oldun...</h3>".format(name,location)
        return redirect(url_for('deneme',parametre=name))  # bu şekilde bir url'e yönlendirme yapabiliriz. İçeri string olarak url'in methodunun adını yazıyoruz. Aynı zamanda o sayfaya parametre yollayabiliriz
       



@app.route('/process',methods=['POST'])
def process():
    name = request.form['name'] # requestteki form içindeki name'i name olan inputu yakalıyoruz
    location = request.form['location']
    return "<h3>Merhaba {}! Aramıza {}'dan katılıyorsun. Başarıyla kayıt oldun...</h3>".format(name,location)

@app.route('/process_json',methods=['POST'])
def process_json():
    data = request.get_json() # request içerisindeki json'ı yakaladık
    name = data['name'] # yakaladığımız json objesi içindeki name'i aldık.
    location = data['location']
    return jsonify({'resulst':'Success!','name':name,'location':location})
    
@app.route('/login')
def login():
    session['username'] = request.args.get('username')
    isim = session['username']
    if isim == None:
        return "<h2>Lütfen giriş yapın!</h2>"
    else:
        return "<h2>Hoşgeldiniz {}</h2>".format(isim)


if __name__ == "__main__":
    app.run()