from flask import (
    Flask,
    jsonify,  # json response dönmek için bu fonksiyonu kullanırız
    request, # gelen isteği parçalayibilirz
    redirect, # string url'e yönlendirirz
    url_for, # kendi url'lerimize yönlendirebiliriz
    session, # oturum işlemlerini yönetiriz
    render_template
)


app = Flask(__name__)

app.config['DEBUG'] = True # uygulamamıza ait configurasyonları set edebiliriz. debug True iken hata mesajlarını vs alabiliriz
app.config['SECRET_KEY'] = 'asd123ssd' # cookie'ler için gereklidir


@app.route('/')
def index():
    return '<h1>Index</h1>'


@app.route('/contact')
def contact():
    return '<h1>Contact Page</h1>'


@app.route('/json')
def json():
    return jsonify({'data': [
        {'id': 1},
        {'id': 2}
    ]}
    )

# bu route yalnızca POST isteklere izin verir
@app.route('/only-post', methods=['POST'])
def only_post():
    return jsonify({'message': 'success'})


@app.route('/with-name/<string:name>') # istersek parametreli route'lar oluşturabiliriz
def with_name(name): # gelen parametreleri sırasıyla burada set etmemiz gerek
    return f"Merhaba {name}"

@app.route('/with-id/<int:id>')
def with_id(id):
    return f"Id -> {id}"


@app.route('/query')
def query():
    name = request.args.get('name') # url'deki parametreleri (query) yakalayabiliriz
    id = request.args.get('id')
    return f'Merhaba {name}! {id} id ile query sayfasına hoş geldin!'


@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name') # form'dan girilen verileri yakalayabiliriz
        return f"Formdan gelen [name] = {name}"
    return render_template('form.html')

@app.route('/json',methods=['POST'])
def get_json():
    req_json = request.get_json() # gelen istek içerisindeki json'u yakalıyoruz
    name = req_json['name'] # json'dan name'i alıyoruz
    return jsonify({'message':'success','name':name})


@app.route('/redirect')
def to_redirect():
    return redirect('/') # istediğimiz string url'e yönlendiriyoruz

@app.route('/url-for')
def to_url_for():
    # return redirect(url_for('index')) # istersek kendi fonksiyonlarımıza (url - route) yönlendiririz. içeriye fonksiyon adını yazmamız yeter
    return redirect(url_for('query',name='DENNE',id=1)) # route'lara parametreler ile yönlendirebiliriz


@app.route('/is-authenticated')
def is_auth():
    if 'user' in session: # session'da user varsa
        return f"User is authenticated -> {session['user']}"    
    return "User is not authenticated!"


@app.route('/login')
def login():
    if 'user' in session:
      return redirect(url_for('is_auth'))  
    user = 'Baysan'
    session['user'] = user # session'a user adında bir key ekle value'si user (değişken) olan
    return redirect(url_for('is_auth'))

@app.route('/logout')
def logout():
    session.pop('user') # session'daki user'i sil
    return redirect(url_for('is_auth'))

@app.route('/variable')
def variable():
    name = 'Baysan' # ister tek değişken göndeririz
    sozluk = {'username':'mebaysan','IP':'127.0.0.1','names':['Enes','Yusuf','Yavuz']} # ister sözlük olarak göndeririz
    return render_template('variable.html',name=name,sozluk=sozluk)

if __name__ == '__main__':
    app.run()