from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config #"." por que esta en el mismo directorio

# Configuracion de la app:
# al llamarse init automaticamente python lo considera una libreria

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    # app.config["SECRET_KEY"]= "CLAVE SEGURA"
    # tambien define eso, desde config
    app.config.from_object(Config)
    
    return app