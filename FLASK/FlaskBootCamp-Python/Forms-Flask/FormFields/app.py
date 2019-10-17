from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField, SelectField, TextField,
                     TextAreaField, SubmitField)  # çoklu satırda import bu şekilde
from wtforms.validators import DataRequired
app = Flask("__name__")

app.config['SECRET_KEY'] = 'mykey'


class User():
    def __init__(self, name, neutered, mood, food_choice, feed_back):
        self.name = name
        self.neutered = neutered
        self.mood = mood
        self.food_choice = food_choice
        self.feed_back = feed_back


class InfoForm(FlaskForm):
    # adın nedir? -> bu bu form nesnesinin label'i oluyor
    # validators -> bu form nesnesi için doğrulayıcıları belirler. liste olarak alır
    name = StringField('Adın nedir?', validators=[DataRequired()])
    neutered = BooleanField(
        'Evlenebilecek yetkinliğe sahip misin?')
    mood = RadioField('Modunu seç:', choices=[
                      ('mood_one', 'Mutlu'), ('mood_two', 'Yorgun')])
    # radio field bize seçenek sunar. Modunu seç onun label'i. choices -> seçeneklerdir. Liste alır ve liste içine değerleri tuple olarak veririz. mood_one bize gelen id gibi düşünürüz. 'Mutlu' ise bu choice'in label'idir.
    food_choice = SelectField('Vejeteryan mısın?', choices=[
                              ('food_one', "Evet"), ('food_two', 'Hayır')])
    feed_back = TextAreaField()
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        # user_name adında bir session oluşturduk ve formdan gelen name datasını aldık
        session['name'] = form.name.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food_choice'] = form.food_choice.data
        session['feed_back'] = form.feed_back.data
        user = User(form.name.data, form.neutered.data,
                    form.mood.data, form.food_choice.data, form.feed_back.data)
        flash('Bilgi için teşekkürler!')
        flash('Sayfaya yönlendiriliyorsunuz...')
        return redirect(url_for('thankyou'))  # thankyou adlı fonsiyona gider
    return render_template('index.html', form=form)


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == "__main__":
    app.run(debug=True)
