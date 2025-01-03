from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Nombre del usuario", validators=[DataRequired()])
    password = PasswordField("Constraseña", validators=[DataRequired()])
    submit = SubmitField("Enviar datos") #Dispara eventos, no requiere tener valor
