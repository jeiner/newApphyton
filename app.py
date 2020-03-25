# app

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")
@app.route("/chacal")
def saludos():
    return "Esto es un mensaje de pruebaaa, internautas"

if __name__ == "__main__":
    app.run(debug=True)