from flask import Flask, render_template, request
import random
# render_template -> template dosyasını kullanıcıya yollar
# Flask otomatik olarak templates klasörü altına bakar templatesler için
# Flask static dosyaları static klasörü altından alır
app = Flask(__name__)


@app.route('/')
def index():
    # img_url adında bir değişken oluşturduk
    tek_deger = 'tek_deger'
    img_url = '../static/resim.png'
    isim = 'Baysan'
    sozluk = {"name": "enes", "soyad": "baysan"}
    a = random.randint(1, 10)
    b = random.randint(-6, 12)
    toplam = a + b

    # oluşturduğumuz değişkeni template'a gönderiyoruz
    return render_template('index.html', variables=[img_url, isim], sozluk=sozluk, tek_deger=tek_deger, toplam=toplam)


@app.route('/url_for')
def url_for():
    return render_template('url_for.html')


@app.route('/forms')
def forms():
    return render_template('forms.html')


@app.route('/forms_url_for')
def forms_url_for():
    # buraya gelen action ile requestteki first ve last değişkenlerini yakalıyoruz
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('forms_url_for.html', first=first, last=last)


@app.errorhandler(404)  # 404 hataları gelirse
def error(e):  # e adında değişken yolluyoruz
    # error için hazırladığımız template'i dön ve 404 hata kodunu yolladık
    return render_template('error.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
