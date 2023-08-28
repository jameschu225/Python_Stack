from flask import Flask, render_template, redirect, request, url_for
from users import Users
app = Flask(__name__)

@app.route('/')
def reroute():
    return redirect('/users')


@app.route('/users')
def display():

    allusers = Users.get_all()
    return render_template('index.html', allusers=allusers)

@app.route('/create', methods=['post'])
def create():

    result = Users.create(request.form)
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


if __name__ == "__main__":
    app.run(debug=True)