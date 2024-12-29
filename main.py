from flask import Flask

app =  Flask(__name__)

# primer end point con primera ruta
@app.route("/home") # decorador
def hello():
    return "Hello world"

app.run(host='0.0.0.0', port=3000)