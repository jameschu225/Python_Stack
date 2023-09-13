from flask import render_template, redirect, request, session
from flask_app.models.users import Users
from flask_app import app


@app.route('/')
def reroute():
    session.clear()
    return redirect('/users')


@app.route('/users')
def display():

    allusers = Users.get_all()
    return render_template('index.html', allusers=allusers)

@app.route('/create', methods=['post'])
def create():

    allusers = Users.get_all()
    print(allusers[0].email)
    if not Users.validation(request.form, allusers):
        session["fname"] = request.form["fname"]
        session["lname"] = request.form["lname"]
        session["email"] = request.form["email"]
        return redirect('/users/new')

    result = Users.create(request.form)
    session.clear()
    return redirect(f'/users/{result}')

@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

@app.route('/users/delete/<int:user_id>')
def delete_user(user_id):

    Users.delete(user_id)
    return redirect('/')

@app.route('/users/<int:user_id>')
def display_one(user_id):

    one_user = Users.get_one(user_id)
    return render_template('one_user.html', one_user=one_user)

@app.route('/users/<int:user_id>/edit')
def edit(user_id):

    one_user = Users.get_one(user_id)
    return render_template('edit_user.html', one_user=one_user)

@app.route('/update', methods=['post'])
def update():

    Users.update(request.form)
    return redirect(f'/users/{request.form["id"]}')