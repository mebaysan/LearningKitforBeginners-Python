from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Ponny adı:')
    pon_id = IntegerField('Ponny Id:')
    submit = SubmitField('Ekle')
