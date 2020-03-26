# app

import os

from flask import Flask, render_template

from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.form:
        print(request.form)
    return render_template("home.html")
@app.route("/chacal")
def saludos():
    return "Esto es un mensaje de pruebaaa, internautas"

if __name__ == "__main__":
    app.run(debug=True)