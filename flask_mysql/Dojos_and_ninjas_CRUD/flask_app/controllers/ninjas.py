from flask import render_template, redirect, request
from flask_app.models.ninjas import Ninjas
from flask_app.models.dojos import Dojos
from flask_app import app

@app.route("/ninjas")
def display_ninjas():

    all_dojos = Dojos.get_all_dojos()
    return render_template("new_ninja.html", all_dojos=all_dojos)

@app.route("/create_ninjas", methods=['post'])
def create_ninja():
    Ninjas.creat_ninja(request.form)
    id = request.form["did"]
    return redirect(f'/dojos/{id}')