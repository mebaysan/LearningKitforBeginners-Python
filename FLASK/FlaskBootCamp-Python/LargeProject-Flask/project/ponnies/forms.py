from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Ponny adı:')
    submit = SubmitField('Ekle')


class DelForm(FlaskForm):
    id = IntegerField('Ponny Id')
    submit = SubmitField('Sil')
