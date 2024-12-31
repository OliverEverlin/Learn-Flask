from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest

# Configuracion de la app
app =  Flask(__name__)
bootstrap = Bootstrap(app)

app.config["SECRET_KEY"]= "CLAVE SEGURA"
# app.config["SERVER_NAME"] = "localhost:3000"
# app.config["PREFERRED_URL_SCHEME"] = "http"

# Datos simulados
items = ["ITEM A", "ITEM B", "ITEM C", "ITEM X", "ITEM Y", "ITEM Z"]

class LoginForm(FlaskForm):
    username = StringField("Nombre del usuario", validators=[DataRequired()])
    password = PasswordField("Constraseña", validators=[DataRequired()])
    submit = SubmitField("Enviar datos") #Dispara eventos, no requiere tener valor

@app.cli.command()
def test():
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir="tests")
    runner = unittest.TextTestRunner()
    runner.run(tests)

# Manejador de errores
@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template('404.html', error=error)

# Obtiene la ip, la guarda y redirige a la siguiente ruta
@app.route("/index") # decorador
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect("/show_information_address"))
    session["user_ip_information"] = user_ip_information
    return response

# Renderiza datos dinamicos
@app.route("/show_information_address", methods=["GET", "POST"])
def show_information():
    user_ip = session.get("user_ip_information")
    username = session.get("username")
    login_form = LoginForm()
    context = {
        "user_ip": user_ip,
        "items": items,
        "login_form": login_form,
        "username": username
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"] = username
        flash('Nombre de usuario registrado correctamente')
        return redirect(url_for("index"))
    return render_template("ip_information.html", **context)

# Ejecucion del server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 3000, debug = True)