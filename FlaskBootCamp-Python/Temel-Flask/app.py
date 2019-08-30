from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Merhaba canım</h1>'


@app.route('/information')
def info():
    return '<h3>Information Technologies</h3>'

# Dinamik url tanımlama
@app.route('/dynamic/<name>')  # url'e name adında bir ek gelecek dedik
def dynamic(name):  # url'den gelen name'i yolladık
    return '<h1>Merhaba {}</h1>'.format(name.upper())


if __name__ == "__main__":
    # debug=True -> program çalışırken kodlarda değişiklik olursa otomatik kendini yeniler
    app.run(debug=True)
