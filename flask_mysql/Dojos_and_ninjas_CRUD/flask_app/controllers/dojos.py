from flask import render_template, redirect, request
from flask_app.models.dojos import Dojos
from flask_app import app

@app.route("/")
def reroute():
    return redirect('/dojos')

@app.route("/dojos", methods=['get'])
def display():

    all_dojos = Dojos.get_all_dojos()
    return render_template("index.html", all_dojos=all_dojos)

@app.route("/create_dojos", methods=['post'])
def create():
    Dojos.creat_dojo(request.form)
    return redirect('/')

@app.route("/dojos/<int:dojo_id>")
def display_dojo_with_ninjas(dojo_id):
    dojo = Dojos.get_dojos_with_ninjas(dojo_id)
    return render_template("dojo_show.html", dojo=dojo)