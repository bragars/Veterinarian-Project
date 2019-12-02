from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Lenght, Email

class SalaForm(FlaskForm):
    numero = IntegerField('Numero',
                          validators=[DataRequired(), Lenght(min=1, max=10)])
    submit = SubmitField('Cadastro')