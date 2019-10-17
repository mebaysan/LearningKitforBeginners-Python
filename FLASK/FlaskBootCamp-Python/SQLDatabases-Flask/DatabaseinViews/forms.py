from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    name = StringField('Ponny Adı:')
    submit = SubmitField('Ekle')

class DelForm(FlaskForm):
    id = IntegerField('Sİlmek istediğiniz Ponny Id girin:')
    submit = SubmitField('Ponny sil')