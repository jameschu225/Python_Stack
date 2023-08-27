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

@app.route('/users/create', methods=['post'])
def create():

    print(request.form)
    Users.create(request.form)
    return redirect('/')

@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

if __name__ == "__main__":
    app.run(debug=True)