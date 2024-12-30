from flask import Flask, request,  make_response, redirect, render_template

app =  Flask(__name__)


items = ["ITEM A", "ITEM B", "ITEM C", "ITEM X", "ITEM Y", "ITEM Z"]
# primer end point con primera ruta
@app.route("/index") # decorador
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect("/show_information_address"))
    response.set_cookie("user_ip", user_ip_information)
    return response

@app.route("/show_information_address")
def show_information():
    user_ip = request.cookies.get("user_ip")
    context = {
        "user_ip": user_ip,
        "items": items
    }
    return render_template("ip_information.html", **context)

app.run(host='0.0.0.0', port = 3000, debug = True)