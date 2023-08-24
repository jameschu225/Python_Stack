from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def guest():
    session['answer'] = random.randint(1, 100)
    session['result']= None
    session['try'] = 0
    print(session['answer'])
    return render_template('index.html')

@app.route('/guest', methods = ['post'])
def check():
    guest = int(request.form['guest'])
    session['try'] += 1
    if guest != session['answer'] and session['try'] < 5:
        session['result']= False
        if guest > session['answer']:
                session['clue'] = 'Too high!'
                return render_template('index.html')
        elif guest < session['answer']:
                session['clue'] = 'Too low!'
                return render_template('index.html')
    elif guest != session['answer'] and session['try'] == 5:
        session['clue'] = 'You Lose!!'
        session['result'] = 'draw'
        return render_template('index.html')
    else:
        session['result'] = True
        session['clue'] = f"{session['answer']} was the number!"
        return render_template('index.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)