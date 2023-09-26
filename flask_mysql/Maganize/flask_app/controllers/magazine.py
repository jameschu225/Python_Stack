from flask_app.model import magazine
from flask_app.model import user
from flask import render_template, redirect, request, session, flash
from flask_app import app


@app.route("/new")
def new_recipes():
    if "login_id" not in session:
        return redirect('/')
    
    return render_template("new_mag.html")

@app.route("/create", methods=['post'])
def create_mag():
    if not magazine.magazine.mag_validation(request.form):
        return redirect('/new')

    data = {
        "title" : request.form["title"],
        "description": request.form["description"],
        "user_id":session["login_id"]
    }

    magazine.magazine.creat_mag(data)
    return redirect('/dashboard')

@app.route("/show/<int:mag_id>")
def detail_mag(mag_id):

    mag = magazine.magazine.get_mag_by_id(mag_id)

    creator = user.User.get_user_by_id(mag[0]["user_id"])

    subscriber = magazine.magazine.get_subscribe_by_mag(mag_id)
    
    return render_template("one_mag.html", subscriber=subscriber, mag=mag[0], creator=creator, user= user.User.get_user_by_id(session["login_id"]))

@app.route("/user/account")
def user_account():
    if "login_id" not in session:
        return redirect('/')
    
    user_mag = magazine.magazine.get_mag_by_creator(session["login_id"])
    all_mags_with_count = magazine.magazine.get_count_subscribe_by_mag(session["login_id"])

    return render_template("user_account.html", all_mags_with_count=all_mags_with_count, user_mag=user_mag, user= user.User.get_user_by_id(session["login_id"]))

@app.route("/delete/<int:mag_id>")
def delete_mag(mag_id):

    magazine.magazine.delete(mag_id)
    
    return redirect("/user/account")

@app.route("/subscribe/<int:mag_id>")
def subscribe_mag(mag_id):
    print(mag_id)
    data = {
            'subscribe_id': mag_id,
            "user_id" : session["login_id"]
        }
    
    magazine.magazine.subscribe(data)
    return redirect('/dashboard')
