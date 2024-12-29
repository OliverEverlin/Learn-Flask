from flask import Flask, request

app =  Flask(__name__)

# primer end point con primera ruta
@app.route("/home") # decorador
def hello():
    user_ip_information = request.remote_addr
    return f"Hola, como estâs \n tu direcciôn IP es la siguiente: {user_ip_information}"

app.run(host='0.0.0.0', port = 3000, debug = True)