from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def display():

    return render_template('index.html')

@app.route('/process', methods=['post'])
def survey():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    
    return redirect('/result')

@app.route('/result')
def result():

    return render_template('result.html')

app.run(debug=True)