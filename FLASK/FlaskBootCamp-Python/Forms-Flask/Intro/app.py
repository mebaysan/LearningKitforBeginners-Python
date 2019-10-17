from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
app = Flask('__name__')

# uygulamamız için bir adet secret_key belirledik
app.config['SECRET_KEY'] = 'mysecretkey'


# InfoForm adında bir class ve bu class FlaskForm sınıfdan inherit edildi
class InfoForm(FlaskForm):  # kendimize bir form oluşturuyoruz
    name = StringField("What is your name?")  # formun alanları ve özellikleri
    submit = SubmitField("Submit")


@app.route('/', methods=["GET", "POST"])
def index():
    name = False
    form = InfoForm()  # yukardaki form classımızdan bir nesne oluşturduk
    if form.validate_on_submit():  # eğer form başarılı bir şekilde submit olursa
        name = form.name.data  # name değişkenine form'un name field'ından gelen datayı atıyoruz
        form.name.data = ''
    # form nesnemizi ve name nesnemizi template'a yolluyoruz
    return render_template('index.html', form=form, name=name)


if __name__ == "__main__":
    app.run(debug=True)
