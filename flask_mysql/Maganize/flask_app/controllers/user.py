from flask_app.model import user
from flask_app.model import magazine
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def display():
    return render_template ("index.html")

@app.route("/register", methods=["post"])
def create():

    if not user.User.validation(request.form, user.User.get_all()):
        session["fname"] = request.form["fname"]
        session["lname"] = request.form["lname"]
        session["email"] = request.form["email"]
        return redirect('/')
    
    session.clear()
    pw_hash = bcrypt.generate_password_hash(request.form["password"])

    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
        "password" : pw_hash
    }

    user_id = user.User.save(data)
    session["login_id"] = user_id

    return redirect("/dashboard")
    
@app.route("/dashboard")
def dashboard():
    if "login_id" not in session:
        return redirect('/')
    
    # data ={
    #     'id' : session["login_id"]
    # }

    return render_template("dashboard.html", user= user.User.get_user_by_id(session["login_id"]), all_mag = magazine.magazine.get_all_mags_with_creator())

@app.route("/login", methods=["post"] )
def login():
    if not user.User.login_validation(request.form):
        return redirect('/')
    
    user_in_db = user.User.get_user_by_email(request.form)

    if not bcrypt.check_password_hash(user_in_db[0]["password"], request.form["password"]):
        flash("Invalid Email/Password")
        return redirect('/')
    session["login_id"] = user_in_db[0]["id"]
    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')

@app.route("/update/user",  methods=["post"] )
def update():
    if not user.User.update_validation(request.form):
        return redirect('/user/account')

    user.User.update(request.form)

    return redirect("/user/account")

